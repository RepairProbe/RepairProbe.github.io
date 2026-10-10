# Design-Richtungsvertrag (Phase 4)

Gewählt am 2026-10-10 im automatisierten Auftrag (die in `WEBSITE-STATUS.md` dokumentierte Entscheidungsvertretung).

## Sieben Richtungen aus der Welt der Zielgruppe

Materialfamilien: Papier/Protokoll · Holz/Stahl-Werkstatt · Technische Zeichnung · Metall/Instrument · Druck/Datenblatt · Fotografie · PCB/Bestückungsdruck.

| # | Richtung | Kernidee | Ehrliche Bewertung |
|---|---|---|---|
| 1 | **Messprotokoll/Prüfbuch** | Die Seite ist ein Reparatur-Protokoll: Evidenzzeilen mit Herkunftsstempeln, Messwerte in Mono, Linien wie auf Formularpapier | Stärkste Deckung mit dem Kernversprechen (Evidenz, Nachvollziehbarkeit); für Laien sofort lesbar, wenn die Stempel erklärt sind |
| 2 | Werkbank-Draufsicht | Abschnitte wie Werkbankzonen, Werkzeuge und Bauteile ordnen die Seite | Ohne echte Fotos nur als Illustration; Gefahr der Deko |
| 3 | Schaltplan | Linien, Knoten, Testpunkte strukturieren Layout und Ablauf | Stark für Ablauf-Darstellung; als Ganzes zu technisch für Laien |
| 4 | Messgerät-Frontplatte | Dunkle Panels, gravierte Beschriftungen, Anzeigen | Schöner Kontinuitäts-Bezug zur bisherigen dunklen Seite; als Ganzes aber „Dashboard“-Gefahr |
| 5 | Datenblatt | Tabellen, Kennwerte, Präzisionstypografie | Passt zu Infrastruktur-Ehrlichkeit; wirkt für Laien trocken |
| 6 | Werkstatt-Fotodokumentation | Echte Reparaturfotografie trägt die Seite | **Vom Los gewählt, aber disqualifiziert:** keine lizenzierten eigenen Fotos vorhanden (auch PR #7 lehnte es ab, Bilder zu erfinden). Ohne Fotos wird die Richtung leer oder unecht |
| 7 | Leiterplatte/Bestückungsdruck | Kupferlinien, Pads, Siebdruck als Layoutsprache | Das Klischee jeder Elektronik-Seite; höchster KI-Einheitslook-Verdacht |

## Lotterie und Entscheidung

Los (deterministisch, sha256 von `repairprobe-redesign-2026-10-10`): Richtung 6. **Disqualifikation mit Grund:** fehlende legale Fotografie. Gewählt stattdessen: **Richtung 1 „Messprotokoll/Prüfbuch“** als Hauptrichtung. Die verworfenen Richtungen geben je eine Stärke ab:

- Von 3 (Schaltplan): Testpunkt-Marker als Evidenz-Stempel-Ornament.
- Von 4 (Frontplatte): eine dunkle Instrumentenfläche als Rhythmusabschnitt und als Statuspanel im Hero (Kontinuität zur bisherigen Identität).
- Von 5 (Datenblatt): Präzisions-Mono für Messwerte und Kennwerte.
- Von 6 (Fotografie): Konkretheitszwang — der echte Fernseher-Fall und echte Werte („ESR = 3,6 Ω“) stehen zentral, keine abstrakten Behauptungen.
- Von 7 (PCB): ausdrücklich nicht übernommen.

## Richtungsvertrag

- **These:** Reparaturdiagnose wird nachvollziehbar, wenn jede Information ihre Herkunft zeigt. Die Seite macht diese Haltung sichtbar, indem sie selbst wie ein sorgfältig geführtes Protokoll aufgebaut ist.
- **Eigene Welt:** Prüfprotokoll auf Papier (hell, warmgrau `#F1F1EE`, Haarlinien), Marken-Stempel in Cyan (`#6AC9D7`, aus dem Organisations-Avatar), eine dunkle Instrumentenfläche (`#0D1411`) als Kontrast-Abschnitt, Messwerte in IBM Plex Mono, Text in IBM Plex Sans.
- **Geschichte beim Scrollen:** Problem (warum scheitert Reparatur) → Ansatz (Evidenzklassen) → echter Fall (Protokoll, dunkel) → Stand (ehrliche Bestandsaufnahme) → Person → Fragen/Kontakt. Jeder Abschnitt trägt eine fortlaufende Protokollnummer (01–06) statt Werbe-Etiketten.
- **Erster Bildschirm:** H1 „Gemessen ist nur, was wirklich gemessen wurde.“, Lede mit Projektidentifikation, ehrliche Statuszeile, ein primärer Button, daneben dunkles Statuspanel mit vier Mono-Stempeln (BASELINE/APP/ANTRAG/FÖRDERUNG).
- **Formensprache:** Rechtecke, Radius 4–6px, Haarlinien 1px, Stempel als Umriss-Kästchen mit farbigem Testpunkt-Marker, keine Schatten-Glow, keine Verläufe außer dezenter Flächenabtönung, keine gleichförmigen Dreier-Kartenraster (Bestandslisten laufen als Protokollzeilen).
- **Akzentdisziplin:** Cyan nur an einer Stelle pro Abschnitts-Sicht (aktive Markierung, primärer Button auf dunkler Fläche, Markenstempel); Zustandsfarben nur an Evidenz-Stempeln.
- **Abschluss:** Kontakt nüchtern (Mail + GitHub), Footer mit Ehrlichkeitszeile und Lizenz.

## Farb-Kontraste (zu messen, Ziel ≥ 4,5:1 für Text)

Tinte auf Papier, weicher Tinte-Text, Teal-Ink-Akzent auf Papier (abgedunkeltes Cyan für Textzwecke), Cyan auf Dunkel, dunkle Abschnittstexte. Werte werden im Build gemessen und dokumentiert (siehe pruefung).
