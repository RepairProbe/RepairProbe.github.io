# Keyword- und GEO-Karte (Phase 2B)

Ersatzweg ohne DataForSEO (Begründung in WEBSITE-STATUS.md): manuelle Suche, Autovervollständigung, Trends-Vergleich. **Suchvolumen-Zahlen fehlen** und sind entsprechend nicht belegbar; die Karte priorisiert deshalb nach Relevanz für die Zielgruppen, nicht nach Volumen.

## Relevante Begriffe (deutsch)

| Begriff | Volumen | Wettbewerb | Einschätzung |
|---|---|---|---|
| repairprobe | unbekannt | sehr niedrig | Markenbegriff, Hauptziel: hier ranken und korrekt beschrieben werden |
| reparatur diagnose software | unbekannt | mittel | Nebensatz auf Startseite/Evidenzmodell |
| elektronik fehlersuche hilfe | unbekannt | mittel | Problem-Abschnitt Startseite |
| repair café werkzeug / repair café digitale hilfe | unbekannnt | niedrig | Repair-Café-Abschnitt, Org-Profil |
| messwerte dokumentieren reparatur | unbekannt | niedrig | Evidenzmodell-Seite |
| ki reparaturhilfe | unbekannt | niedrig-mittel | Ansatz-Abschnitt, Grenzen ehrlich benennen |
| schaltplan finden reparatur | unbekannt | mittel | Problem-Abschnitt (RETRIEVED-Kontext) |
| open source reparatur projekt | unbekannt | niedrig | Startseite/Status |

## Google/KI-Situation

Nicht gemessen (kein DataForSEO). Beobachtbar: „RepairProbe“ führt aktuell auf GitHub-Organisation und Website; KI-Assistenten beschreiben das Projekt aus GitHub-Profil und Website. **Konsequenz (aus kanonischer Synthese):** Faktensätze konsistent auf Website, Org-Profil und `llms.txt` verteilen, damit KI-Suchen keine falschen Annahmen übernehmen (z. B. „fertige App“ oder „Förderung bewilligt“).

## Keyword-Karte (Begriff → Stelle)

| Stelle der Seite | Begriff/Fokus |
|---|---|
| Titel Startseite | RepairProbe + Reparatur + Messwert/Evidenz |
| H1 Startseite | „Gemessen ist nur, was wirklich gemessen wurde.“ (Kernsatz, gleichzeitig Markenkern) |
| Meta-Beschreibung Startseite | Reparaturdiagnose + Beobachtung/Messung/Quelle/Vermutung getrennt + offen/quelloffen/in Entwicklung |
| H1 Evidenzmodell | Evidenzklassen + Grenze |
| H1 Fahrplan | Fahrplan/Stand |
| H1 Technische Basis | Baseline/Vorarbeit |
| Abschnitt Problem | Fehlersuche-Wissen, Schaltplan, Ersatzteil, Demontage |
| Abschnitt Ansatz | Evidenzklassen, KI-Grenze |
| FAQ | Fragen wie sie Zielgruppe tippt (Ist RepairProbe eine App? Brauche ich Messhardware? …) |
| llms.txt | Faktensätze 1:1 aus texte.md |

## GEO-Maßnahmen

1. Faktensätze am Ende von `texte.md`, daraus `llms.txt` und JSON-LD (`Organization`, `FAQPage`) erzeugen.
2. Dieselben Fakten stehen im Org-Profil (Abgleich im separaten `.github`-PR).
3. `robots.txt` erlaubt Suchmaschinen und KI-Crawler ausdrücklich, Sitemap verlinkt.
4. `sitemap.xml` mit allen Seiten.
5. Kanonische URLs auf `https://repairprobe.github.io/…`.

## Themen für spätere Unterseiten (nicht Teil dieses Laufs)

- Messwerte-Dokumentation in der Praxis (Repair Measurement Event v1 erklären)
- Repair-Café-Begleitung/Feedback-Pipeline
- Reparaturfall-Protokolle (sobald es mehr belegte Fälle gibt)
