# Design-Referenzen — Notizen (Phase 2A)

Sichtungen 2026-10-10, Screenshots in `referenzen/`. Auswahl nach Branchennähe (reparierbare Elektronik, Open-Source-Glaubwürdigkeit) statt nach Branche allein.

## Betrachtet

| Referenz | Sichtung | Befund |
|---|---|---|
| frame.work | blockiert (HTTP 408 auf Bot-Zugriff) | nicht auswertbar |
| fairphone.com/de | `fairphone-oben.png` | wahre Fotografie, einfache Nav, dunkelgrüner Schriftzug, einspaltige Botschaft. Fotografie-Welt ist stark, aber ohne eigene lizenzierte Fotos nicht übernehmbar. |
| signal.org/de | `signal-oben.png` | heller Grund, eine Akzentfläche, riesige schwarze Headline, genau ein primärer Button, nüchterner OSS-Ton. |
| de.ifixit.com | `ifixit-oben.png` | dichte kommerzielle Marktplatz-Optik; als Kontrastbeispiel, nicht als Richtung. |
| openrepair.org | `openrepair-oben.png` | Reparatur-Werkbank-Welt (Menschen, Tische, Werkzeug), Outline-Wortmarke als Badge, kräftige Akzentfarbe, Cookie-Banner (Negativbeispiel: Tracking vermeiden). |

## Gewählte Referenzen

**Referenz A: Signal (Struktur und Haltung).** Übernommen: heller Grund als Normalzustand, genau eine Akzentfarbe, große klare Headline, ein einziger primärer Handlungsbutton, nüchterner Ton, kurze Abschnitte. Ausdrücklich weg gelassen: Produktfotografie von Smartphones, Download-Button-Optik, Blau.

**Referenz B: Open Repair Alliance (Welt und Motiv).** Übernommen: Reparatur-Werkbank als inhaltliche Welt (Tische, Prüfprotokolle, Werkstatt statt SaaS), Outline/Badge-Motiv für Marken- und Zustandsmarken (Stempel), kräftiger Zustands-Akzent nur an Schlüsselstellen. Weg gelassen: Foto-Hero (keine eigenen Fotos vorhanden), Werbung-Banner, Cookie-Banner (entfällt, weil kein Tracking).

## Markenmessung (Phase 1, Werkzeug `marke_auslesen.py` + Organisations-Avatar)

Live-Seite (bisher): Hintergrund `#0D1411`, Panels `#16231D`/`#111B16`, Akzent `#9EE493`, Text `#F2F7F3`/`#B9C8BE`, Schrift system-ui.

Organisations-Avatar (verbindliches Markenzeichen, `org-avatar.png`, 420px): Prüfspitzen-Symbol, **Cyan `#6AC9D7` auf Hell `#F0F0F0`**. Die Website-Palette (dunkelgrün) passt bisher nicht zum eigenen Markenzeichen.

**Markenprofil (entscheidend):**

| Rolle | Wert |
|---|---|
| Hauptfarbe | Papier-Hell `#F0F0F0`-Familie (aus Avatar) |
| Akzent | Cyan `#6AC9D7` (aus Avatar), als Text nur in abgedunkelter Form (Kontrast) |
| dunkle Fläche | Tiefes Tannengrün `#0D1411` (Kontinuität zur bisherigen Seite, für dunkle Abschnitte) |
| Text | Tinte `#101B17` (hell) / `#E9F2ED` (dunkel) |
| Überschriften | IBM Plex Sans, 600/700, eng geführt |
| Fließtext | IBM Plex Sans 400, Zeilenabstand 1.6 |
| Messwerte/Stempel | IBM Plex Mono |
| Merkmale | Prüfprotokoll-Haltung: Linien, Stempel, Messwerte monospace; Cyan sparsam |
