# Study-site kit

A single-file law study website: a quiz bank with source tags and explanations, an encyclopedic reviewer, and spaced-repetition drills. It was first built for UP Law PFR (Atty. Uribe) and is meant to be adapted to new subjects.

**New agent: read `HANDOFF.md` first.** Section 5 explains how to adapt the kit to a new professor's testing style before you write any content.

Quick start:

```bash
python3 app/build.py --data example_data --out build/site.html       # one self-contained HTML file
python3 app/print_pdf.py --data example_data --out build/reviewer.pdf --size 8.5in,13in
```

For a new course, create `my_course/` with the same layout as `example_data/` and run the same commands with `--data my_course`.
