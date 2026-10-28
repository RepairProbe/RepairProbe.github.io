# Website-Status

Diese Datei hält fest, wo das Projekt steht. Der Skill `website-bauen` liest sie bei jedem Aufruf und macht dort weiter.

Status: ✅ erledigt · 🔄 läuft · ⬜ offen

| Phase | Name | Status | Datum |
|---|---|---|---|
| 0 | Einrichten | ✅ | 2026-10-10 |
| 1 | Fundament | ✅ | 2026-10-10 |
| 2 | Recherche | ✅ | 2026-10-10 |
| 3 | Texte | ✅ | 2026-10-10 |
| 4 | Design-Richtung | ✅ | 2026-10-10 |
| 5 | Bauen | ✅ | 2026-10-10 |
| 6 | Prüfen und Feinschliff | ✅ | 2026-10-10 (Content-Review: ship; Visual-Review: ship, 8/8 Seiten) |
| 7 | Livegang | ✅ | 2026-10-10 (PR #10 gemerged, main 33e08d1, Live-Verifikation im sichtbaren Browser, Live-Crawl 0 defekte Links, Org-Profil via .github PR #3 angeglichen und live verifiziert) |
| 8 | Danach | ⬜ | (Search Console/Profilabgleich: Projekteinhaber, siehe unten) |

## Phase-7-Ergebnis Cookies/AGB (2026-10-10)

Gemessen mit Playwright über alle vier Seiten: angefragte Hosts ausschließlich `localhost` (bzw. live `repairprobe.github.io`), keine Cookies, kein localStorage/sessionStorage, keine Drittanbieter-Skripte, Schriften selbst gehostet. **Damit ist keine Cookie-Einwilligung und keine AGB nötig.** Hinweis: Das ist keine Rechtsberatung; ein Impressum fehlt weiterhin (offene Frage unten).

## Ausgangslage

- Bestehende Website oder Marke: `https://repairprobe.github.io/` (diese Repo, statisch, deutschsprachig). Marke „RepairProbe“, Organisations-Avatar auf GitHub.
- Hauptziel der Seite: informieren — was RepairProbe ist, warum Reparaturdiagnose schwer ist, wie das Evidenzmodell funktioniert, was heute existiert und was nicht. Sekundär: Kontakt/GitHub-Besuch.
- Hosting: GitHub Pages (`RepairProbe/RepairProbe.github.io`, kanonische URL `https://repairprobe.github.io/`). Kein Webspace, kein PHP, kein Build-Step.
- Werkzeuge: impeccable ⬜ (Plugin für Claude Code/Codex, in diesem Harness nicht installierbar ohne globale Eingriffe; die im Skill enthaltenen Design-Regeln werden manuell angewendet, die unabhängige Abnahme übernimmt ein frischer Review-Subagent gemäß Phase 6) · Playwright ✅ (Python 3.12 + Chromium) · DataForSEO ⬜ (bewusst weggelassen: gemeinnütziges Open-Source-Projekt, Recherche läuft über den Ersatzweg aus Phase 2) · Hosting-MCP ⬜ (nicht nötig, Deployment über GitHub Pages) · Formular-Ziel ⬜ (kein Formular, Kontakt per Mailto/GitHub)
- Skill-Installation: Quelle `https://github.com/Julian-Ivanov/website-bauen`, Commit `ee7c4cbfa3fd2e7c2e169b2831f4218a27edc9ca`, Pfad `.zcode/skills/website-bauen/`, Installationsart Kopie des Repos (ohne `.git`).

## Auftragrahmen (steht an der Stelle der Personen-Entscheidungen)

Der Auftrag läuft automatisiert (Agenten-Mission vom Projektinhaber). Die in den Phasen angelegten Personen-Entscheidungen werden durch die Vorgaben des Missionsauftrags ersetzt: ehrlicher Projektstand, Evidenzmodell sichtbar machen, kein KI-Einheitslook, keine erfundenen Fakten, deutschsprachige Zielgruppe (Repair-Café, Bastler, Fachleute, Förderer), Barrierefreiheit und Responsiveness sind Teil der Abnahme.

## Marke

| Rolle | Wert |
|---|---|
| Hauptfarbe | (Phase 1: gemessen wird nachgereicht) |
| Akzent | |
| helle Fläche | |
| Text | |
| Überschriften | |
| Fließtext | |
| Merkmale | |

## Entscheidungen

Jede Entscheidung der Person mit Datum, damit sie nicht erneut diskutiert wird.

- 2026-10-10: Sprache bleibt Deutsch (`lang="de"`), bestehende Inhalte und Tonfall werden bewahrt, nicht übersetzt.
- 2026-10-10: Architektur bleibt statisches HTML/CSS ohne Build-Step und ohne Drittanbieter-Skripte (Skill-Empfehlung Phase 5 deckungsgleich mit Repo-README).
- 2026-10-10: Kein Tracking, keine Cookies, kein Analytics (Projektgrundsatz, macht Cookie-Banner und AGB-Pflicht obsolet; Ergebnis in Phase 7 dokumentiert).
- 2026-10-10: PR #7 („about section more personal“) wird vor dem Redesign auf `main` gemerged und sein Inhalt in das Redesign übernommen (Merge-First, Governance-Issue #9).

## Offene Fragen an die Person

- Impressum: Für eine vollständige Impressumsangabe fehlt die Anschrift. Solange sie nicht vorliegt, wird kein unvollständiges Impressum veröffentlicht; Kontakt bleibt E-Mail (repairprobe@gmail.com) und GitHub.
- Echtes Porträtfoto von Raik Müller (auch PR #7 wünscht es sich, hat es aber bewusst weggelassen): bisher keines im Repo, wird nicht erfunden.
- Der „Öffentliche Fahrplan“-Link im Organisationsprofil zeigt auf `https://github.com/orgs/RepairProbe/projects`; prüfen, ob er öffentlich erreichbar ist, sonst auf `https://repairprobe.github.io/roadmap.html` umbiegen (separater PR in `RepairProbe/.github`).

## Update-Ablauf nach dem Livegang

1. Änderung in der Seite und in `texte.md`
2. `git`-Commit auf Branch, PR nach `main`, Merge (GitHub Pages deployt automatisch)
3. Live prüfen: `python .zcode/skills/website-bauen/werkzeuge/pruefen.py https://repairprobe.github.io/`
4. Cache: GitHub Pages CDN refreshed automatisch; bei Stale-Verdacht Hard-Reload im Browser prüfen

## Neuausrichtung 28.10.2026

Phase 3–5 vollständig neu umgesetzt: verständlicher Reparaturnutzen, geplantes Radio-Szenario, klare Stand-Trennung, n=1-Forschung ehrlich eingeordnet. Phase 6 lokal geprüft: alle fünf Seiten in fünf Viewports, Screenshots angesehen, 0 defekte interne Links, keine Fremdrequests oder Speicherung, Textkontraste mindestens 5,45:1. Details: website-arbeit/pruefung-2026-10-28.md. Unabhängige Abnahme und Veröffentlichung dieser Fassung noch ausstehend.

Impressum: `BLOCKED_OWNER_INPUT`, Anschrift fehlt; keine privaten Pflichtangaben veröffentlicht. Phase 8 bleibt beim Projekteinhaber.

Unabhängige lokale Abnahme abgeschlossen: ursprünglicher separater Review meldete drei P2, korrigiert und von der unabhängigen Root-Instanz gezielt nachgeprüft. Kein offener P1/P2. Details und technische Grenze des Reviewer-Neustarts im Prüfbericht. Veröffentlichung/Live-Abnahme dieser Fassung steht noch aus.
