# DESIGN.md — Design-System der RepairProbe-Website

Aus der fertigen Seite dokumentiert (Phase 6 des website-bauen-Skills), nicht aus Absichten. Grundlage für künftige Unterseiten im selben Stil.

## Richtung

**Messprotokoll/Prüfbuch** (Vertrag: `website-arbeit/design-vertrag.md`). Die Seite tritt wie ein sorgfältig geführtes Reparatur-Protokoll auf: Protokollzeilen mit Herkunftsstempeln, Messwerte in Mono, Haarlinien, eine dunkle Instrumentenfläche als Rhythmusabschnitt.

## Marke

- Markenzeichen: Prüfspitze (aus dem GitHub-Organisations-Avatar vermessen: Kopf 210×135 bei (105,35), Querbalken 350×75 bei (35,170), Stiel 70×140 bei (175,245) im 420er-Raster).
- Inline-SVG im Header, `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png` (180), `favicon-512.png`, Vorschaubild `og-image.png` (1200×630).

## Farben (Kontraste gegen Papier bzw. Dunkel gemessen, alle Textpaare ≥ 4,7:1)

| Token | Wert | Verwendung |
|---|---|---|
| `--paper` | `#f1f1ee` | Seitenhintergrund (aus Avatar-Hell abgeleitet) |
| `--paper-2` | `#e8eae4` | Hover-Fläche |
| `--paper-3` | `#fbfbfa` | Karten-/Callout-Fläche |
| `--ink` | `#101b17` | Text, Primärbuttons (15,6:1) |
| `--ink-soft` | `#3e4a44` | Fließtext sekundär (8,2:1) |
| `--teal-ink` | `#0b6b7b` | Links, Akzent-Text auf Hell (5,45:1) |
| `--dark` | `#0d1411` | Dunkle Abschnitte, Instrumentenpanel (Kontinuität zur Vorgänger-Seite) |
| `--dark-text` / `--dark-muted` | `#e9f2ed` / `#a9bbb0` | Text auf Dunkel (16,3:1 / 9,3:1) |
| `--cyan` | `#6ac9d7` | Markenakzent, nur auf Dunkel oder als Flächenakzent (9,7:1 auf Dunkel) |
| `--line` / `--line-dark` | `#d9dbd2` / `#24352c` | Haarlinien |

Zustandsfarben (nur an Evidenz-Stempeln): OBSERVED `--teal-ink`/Cyan, MEASURED `--green-ink #1f7a4d` (gefüllter Punkt), RETRIEVED `--slate-ink #5a6b75`, INFERRED `--amber-ink #8a5a00`, CONFIRMED `--green-ink` (gefüllter Punkt; `stamp solid` = gefüllte Fläche).

## Typografie

- IBM Plex Sans (self-hosted woff2, 400/500/600/700) für alles Fließende; IBM Plex Mono (400/500/600) für Stempel, Messwerte, Statuszeilen, Abschnittsnummern.
- H1 `clamp(2.5rem, 6.2vw, 4.4rem)`/700; H2 `clamp(1.65rem, 3.4vw, 2.5rem)`/600; Fließtext 17px/1.65 (mobil 16px).
- Abschnittsköpfe: schwarze 2px-Kopfline + Mono-Nummer (01–07), bewusst keine Werbe-Etiketten über Überschriften.

## Komponenten

- `section-head` + `section-index`: Protokoll-Nummerierung.
- `protocol`/`protocol-row`: Zeilenraster 10.5rem Stempelspalte + Textspalte; alle `p` in Spalte 2.
- `stamp` (+ `observed/measured/retrieved/inferred/confirmed/solid`): Umriss-Kästchen mit Testpunkt-Marker.
- `panel-instrument`/`status-rows`: dunkles Statuspanel mit Mono-Zeilen.
- `inventory`: zweispaltige Bestandsliste mit Haarlinien, `single` für einspaltig.
- `compare`: Zwei-Panels-Gegenüberstellung (erlaubt/verboten, grün/bernstein Top-Linie).
- `callout`, `honesty`: hervorgehobene Regeln bzw. Ehrlichkeitszeilen (Cyan-Border).
- `faq details/summary`: natives Aufklapp-Element, tastaturbedienbar, ohne JS.
- `button` (`primary`, Standard, `quiet`): Rechteck 6px Radius, mindestens 44px Hoch.

## Bewegung

Nur Hover-Übergänge (0,15s). `prefers-reduced-motion` schaltet Scroll-Smoothing und Transitionen ab. Keine Scroll-Animationen, kein JS auf der Seite.

## Verboten (Richtungs-Disziplin)

Keine Verläufe/Glows, keine gleichförmigen Karten-Dreier-Raster, keine Großetiketten über Überschriften, keine Emojis außer in der wörtlichen Personenvorgabe, Akzentfarbe nie als Flächenfüllung auf Hell außer Stempeln.

## Assets-Herkunft

- Schriften: Fontsource (IBM Plex Sans/Mono, latin, OFL-Lizenz), self-hosted unter `assets/fonts/`.
- Markenzeichnung und OG-Bild: aus dem Organisations-Avatar abgemessen und im Projekt neu gezeichnet (PIL/SVG), repository-eigen.
- Keine Stockfotos, keine Fremdbilder.
