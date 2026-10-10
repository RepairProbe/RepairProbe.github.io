# RepairProbe public website

Dependency-free static site for `RepairProbe/RepairProbe.github.io`, deployed via GitHub Pages at https://repairprobe.github.io/.

No build step, runtime dependency, analytics, tracker, cookie or private CI is required. Fonts (IBM Plex Sans/Mono) are self-hosted under `assets/fonts/`. German-language content, `lang="de"`.

## Pages

- `index.html` — identity, problem, approach, real workflow example, status, person, FAQ, contact
- `evidenzmodell.html` — the five evidence classes and the Inference-is-not-Measurement boundary
- `roadmap.html` — public roadmap, funding-application status, planned scope, explicit limits
- `technical-baseline.html` — pre-funding technical baseline and what it does not prove
- `404.html` — not-found page

## Working files

- `AGENTS.md` — contract for AI agents working in this repository
- `WEBSITE-STATUS.md` — phase state of the website-bauen process
- `website-arbeit/` — design contract, copy source (`texte.md`), research notes, `DESIGN.md`
- `.zcode/skills/website-bauen/` — installed website skill (source: https://github.com/Julian-Ivanov/website-bauen, commit `ee7c4cbfa3fd2e7c2e169b2831f4218a27edc9ca`)

Excluded from crawling via `robots.txt` (`/.zcode/`, `/website-arbeit/`).

## Validation

Serve locally (`python3 -m http.server 8111`), then run the bundled check: `python3 .zcode/skills/website-bauen/werkzeuge/pruefen.py http://localhost:8111`. See `AGENTS.md` for the full validation contract (contrast, keyboard, viewports, crawl, no third-party requests).

Apache License 2.0. See the canonical project license at https://github.com/RepairProbe/repair-probe/blob/main/LICENSE.
