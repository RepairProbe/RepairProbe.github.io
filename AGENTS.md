# AGENTS.md — Projektvertrag für KI-Agenten

Gilt für alle agentengetriebenen Arbeiten an diesem Repository. Stand: 2026-10-10.

## Projektidentität

- Projekt: **RepairProbe** — unabhängiges Open-Source-Projekt (Projektinhaber: Raik Müller).
- Dieses Repository: **öffentliche Website**, statisch (HTML/CSS, keine Build-Abhängigkeit), deployed via GitHub Pages.
- Kanonische Remote (HTTPS und SSH gelten als äquivalent): `https://github.com/RepairProbe/RepairProbe.github.io`
- Kanonischer Default-Branch: `main`
- Live-URL: `https://repairprobe.github.io/`
- Sprache der Website: Deutsch (`lang="de"`).

## Repository-Beziehungen

| Repository | Rolle | Schreibregeln |
|---|---|---|
| `RepairProbe/RepairProbe.github.io` | dieses Repo, öffentliche Website | normales Branch/PR-Workflow |
| `RepairProbe/repair-probe` | **privates kanonisches Produkt-Repo** (Evidence-Quelle) | read-only als Referenz; keine privaten Details hier veröffentlichen |
| `RepairProbe/.github` | Organisationsprofil | Änderungen nur in eigenem governed Branch/PR dieses Repos |

## Wichtige Pfade

- `index.html`, `evidenzmodell.html`, `roadmap.html`, `technical-baseline.html`, `404.html` — Seiten
- `styles.css` — gesamtes Design-System (Design-Vertrag: `website-arbeit/design-vertrag.md`, Dokumentation: `website-arbeit/DESIGN.md`)
- `assets/fonts/`, `assets/img/` — self-hosted Schriften (IBM Plex), Marken-/Vorschaubilder
- `robots.txt`, `llms.txt`, `sitemap.xml` — SEO/GEO
- `website-arbeit/` — Arbeitsdateien (texte.md ist Textquelle; Änderungen an Seitentexten immer in beiden Dateien)
- `.zcode/skills/website-bauen/` — installierter Website-Skill (Quelle: `https://github.com/Julian-Ivanov/website-bauen`, Commit `ee7c4cbfa3fd2e7c2e169b2831f4218a27edc9ca`)

## Schutzzonen und erlaubte Änderungen

- Geschützt: `LICENSE`, Lizenzangaben, `.zcode/skills/website-bauen/` (nur durch gezielte Skill-Updates ändern), kanonische Fakteninhalte (siehe Evidenz-Regel unten).
- Erlaubt: HTML-Seiten, `styles.css`, Assets, SEO-Dateien, `website-arbeit/`, dieses AGENTS.md, README.
- **NO_NESTED_PROJECT_ROOT:** Kein zweites Kopie/Checkout dieses Projekts in sich selbst anlegen. Vor jedem Schreibvorgang Git-Root (`git rev-parse --show-toplevel`) und Ziel-Pfad auflösen; Symlink-Eskapen und nicht existierende Elternordner prüfen.
- Keine Drittanbieter-Skripte, kein Tracking, keine Analytics, keine externen Fonts (DSGVO-Haltung des Projekts).

## Repo-/Workspace-Wechsel-Preflight

Vor Arbeit in diesem Ordner: `pwd` prüfen, Git-Root und Remote-Identität verifizieren (`git remote -v`), Zweig und Divergenz zu `origin/main` prüfen, `git status` klassifizieren (fremde Arbeit niemals blind resetten/verwerfen), AGENTS.md/AGENTS.override.md-Kaskade beachten. Bei Root-/Workspace-Wechsel: alte Kontexte verwerfen und Preflight wiederholen.

## Evidenz vor Behauptung

Produktfakten auf der Website müssen durch das kanonische Repo `RepairProbe/repair-probe` gedeckt sein (README, ADRs, `docs/funding/application-readiness-*.md`, `docs/research/`). Keine erfundenen Messwerte, Testimonials, Partner, Zahlen oder Erfolgsversprechen. Vorhanden ≠ geplant ≠ bewilligt muss auf allen Seiten erkennbar bleiben. Textänderungen: erst `website-arbeit/texte.md`, dann die HTML-Seiten, dann Schreibregel-Check (`.zcode/skills/website-bauen/schreibregeln.md`).

## Website-Validierung (Definition of Done für Seitenänderungen)

1. Lokal servieren (z. B. `python3 -m http.server 8111`).
2. Gebündelter Prüfdurchgang: `python3 .zcode/skills/website-bauen/werkzeuge/pruefen.py http://localhost:8111` (Konsolenfehler, horizontales Scrollen, Alt-Texte, Überschriften).
3. Textkontrast ≥ 4,5:1 (bei Farbänderungen neu messen), Tastaturnavigation und Fokus-Sichtbarkeit prüfen.
4. Viewports mindestens 320, 390, 820, 1366, 1440 px prüfen; Screenshots ansehen.
5. Alle internen Links/Anker crawlen (`INTERNAL_BROKEN_LINKS=0`).
6. Keine neuen Fremdanfragen (Cookie-/Tracking-Freiheit erhalten; Messung wie in WEBSITE-STATUS.md dokumentiert).

## Headed-Browser-Pflicht

Visuelle Abnahme (vor Merge und nach Livegang) im **sichtbaren** Browser oder mit gerenderten Screenshots pro Viewport; Headless-Checks allein sind keine visuelle Abnahme.

## Unabhängige Prüfung und Konvergenz

- Der Implementierer ist nicht der alleinige Validator: vor dem Merge eine unabhängige Instanz (frischer Review-Agent/Review-Pass) gegen DESIGN-Vertrag, texte.md und Screenshots prüfen lassen; legitimate P1/P2 blockieren den Merge.
- **Konvergenz zu `main` (Merge First):** vor neuer Arbeit offene PRs/Branches inventarisieren und sinnvolle, aktuelle Arbeit zuerst integrieren; nicht direkt auf `main` committen; keine Force-Pushes; Merge erst nach grünen Prüfungen und unabhängiger Abnahme; nach dem Merge Live-Deployment verifizieren.

## Bekannte offene Punkte (nicht selbst schließen)

- Impressum: Anschrift fehlt; kein unvollständiges Impressum veröffentlichen.
- Porträtfoto Raik Müller: keines vorhanden; nicht erfinden.
- Phase 8 des Skills (Search Console, Profilabgleich): braucht Projekteinhaber-Konten.
