// Reviewer-tab checks for the desk features: grouped sidebar, blur mode, sticky heading bar, progress.
const {chromium}=require('playwright');
(async()=>{
  const out=process.argv[3]||'build';
  const b=await chromium.launch({executablePath:process.env.CHROMIUM||undefined});
  for (const [w,h,scheme] of [[400,860,'light'],[1280,860,'dark']]){
    const p=await b.newPage({viewport:{width:w,height:h},colorScheme:scheme});const errs=[];p.on('pageerror',e=>errs.push(e.message));
    await p.goto('file://'+require('path').resolve(process.argv[2]||'build/site.html'));
    await p.click('#tabRev');
    const groups=await p.$$eval('#rsecs .grp',els=>els.map(e=>e.textContent));
    const opt=await p.$$eval('#rsel optgroup',els=>els.map(e=>e.label));
    const cur=await p.$eval('#rcontent section.rv:not([hidden])',s=>s.id);
    const mtoc=await p.$$eval('#mtoc a',a=>a.length);
    await p.click('#blurBtn');
    const bl=await p.$$eval('#rcontent section.rv:not([hidden]) .bl',e=>e.length);
    await p.screenshot({path:`${out}/rev_${w}_blur.png`});
    await p.locator('#rcontent section.rv:not([hidden]) .bl').first().scrollIntoViewIfNeeded();
    await p.locator('#rcontent section.rv:not([hidden]) .bl').first().click();
    const ct=await p.textContent('#blurCt');
    await p.click('#blurBtn');
    await p.evaluate(()=>window.scrollBy(0,3000)); await p.waitForTimeout(300);
    const prog=await p.$eval('#rprog',e=>e.style.width);
    const active=await p.$$eval('#mtoc a[aria-current="true"]',a=>a.map(x=>x.textContent));
    await p.screenshot({path:`${out}/rev_${w}_${scheme}.png`});
    // search
    await p.fill('#rq','Matabuena'); await p.waitForTimeout(400);
    const hits=await p.$$eval('#rresults .res',e=>e.length);
    // quiz preset
    await p.click('#tabQuiz'); await p.click('[data-p=pr]'); const pool=await p.textContent('#poolCt');
    await p.screenshot({path:`${out}/quiz_${w}_${scheme}.png`});
    const sw=await p.evaluate(()=>document.documentElement.scrollWidth);
    console.log(JSON.stringify({w,scheme,groups,opt:opt.length,cur,mtoc,bl,ct,prog,active,hits,pool,sw,errs}));
    await p.close();
  }
  await b.close();
})();
