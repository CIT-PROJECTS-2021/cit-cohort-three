![CIT Python Cloud Software Engineering](https://socialify.git.ci/CIT-PROJECTS-2021/cit-cohort-three/image?description=1&descriptionEditable=CIT%20Python%20Cloud%20Software%20Engineering&font=Source%20Code%20Pro&forks=1&language=1&name=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)

# CIT Python Cloud Software Engineering

Course materials for Python for CIT Students, Cohort 3. Twelve weeks from your
first line of Python to a finished project, covering language fundamentals,
object-oriented programming, data structures and algorithms, cryptography, web
scraping, APIs, and data analysis.

You don't need to be a maths wizard to learn to code.

## 📚 Read the notes

**[Read the course online →](https://cit-projects-2021.github.io/cit-cohort-three/)**

The documentation site has the full notes, cross-linked, searchable, and in
order. New here? Start with **Start Here** → **Set Up Your Machine** →
**Week 1**.

To run it locally:

```bash
cd docs
npm install
npm run dev
```

Then open <http://localhost:3000>.

## What's in this repository

| Path | What it is |
| :- | :- |
| `docs/` | The documentation site. **The notes live here** |
| `docs/content/docs/` | The notes themselves, as MDX |
| `week1/` … `week12/` | Original lesson code and legacy markdown (see below) |
| `assignments/` | Exercise and project code, including group projects |
| `quiz/` | Quiz code |
| `extras/` | Regex and command-line argument examples |
| `block_chain/` | A standalone blockchain example |
| `banking_app.py`, `bank.py` | Final project source |

The runnable `.py` files stay where they are, and the notes link to them by path.

## The course

The twelve weeks are sequenced so each one only needs what came before it.

**Python foundations**

| Week | Topic |
| :- | :- |
| 1 | Getting started: what Python is, syntax, variables, numbers |
| 2 | Operators and control flow: every operator, then `if`, `while`, `for` |
| 3 | Collections: strings, lists, tuples, sets, dictionaries |
| 4 | Functions and modules: arguments, lambdas, recursion, imports |

**Structuring programs**

| Week | Topic |
| :- | :- |
| 5 | Object-oriented programming: classes, the four pillars, composition |
| 6 | Errors and files: exceptions, file handling, paths, CSV and JSON |

**Computer science**

| Week | Topic |
| :- | :- |
| 7 | Data structures: stacks, queues, linked lists |
| 8 | Algorithms: five sorting algorithms and Big-O |

**Building real things**

| Week | Topic |
| :- | :- |
| 9 | Cryptography: ciphers and hashing |
| 10 | APIs: CRUD with Flask, status codes, and auth built on Week 9's hashing |
| 11 | Web scraping: requests, BeautifulSoup, and the RSS scraper project |
| 12 | Data analysis: NumPy and Pandas |

Then the final project, a console banking application.

## Contributing

The notes are MDX files under `docs/content/docs/`. Each week is a folder with an
`index.mdx` overview, one page per topic, and a `recap.mdx`. The sidebar order
lives in each folder's `meta.json`.

To add a page:

1. Create `docs/content/docs/weekN/your-topic.mdx` with `title`, `description`,
   and `icon` in the frontmatter.
2. Add its slug to `docs/content/docs/weekN/meta.json` in the position you want.
3. Link to it from the week's `index.mdx` and from related pages.

Every topic page follows the same shape: explanation, examples, **Rules**,
**Common Mistakes**, practice, then a **Keep going** section of links. Please
keep that up when adding pages, so nothing is a dead end.

## Deployment

The site is published to GitHub Pages by
[`.github/workflows/docs.yml`](.github/workflows/docs.yml) on every push to
`main` that touches `docs/`. Pull requests build the site but do not publish it.

The workflow builds a fully static export, so the site needs no server. Search
is prebuilt into a static index rather than served by an API route.

To reproduce the deployed build locally:

```bash
cd docs
npm run build:pages     # writes docs/out/
npx serve out
```

`npm run build` and `npm run start` are unaffected and still produce a normal
server build for local use.

**One-time repository setup:** under **Settings → Pages**, set
*Build and deployment → Source* to **GitHub Actions**.

## Legacy markdown

The `week*/` folders also contain the original markdown notes from the GitBook
version of this course, indexed by [SUMMARY.md](SUMMARY.md). They're kept for
history. **They are not maintained.** Everything in them has been carried into
the documentation site, which is more complete and correctly linked.

The `week*/` folders are numbered by the original cohort calendar. The
documentation site renumbers the weeks into a better teaching order, so
`week3/` on disk is not the same week as `/docs/week3` on the site.

## License

[MIT](LICENSE)
