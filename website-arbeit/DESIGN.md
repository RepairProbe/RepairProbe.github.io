# Design-System · 28.10.2026

Umgesetzt gemäß design-vertrag.md. Statisches HTML/CSS, ohne JavaScript-Verhalten oder Buildschritt.

## Tokens
Papier #f6f7f4, Tinte/Dunkelfläche #173039, sekundärer Text #4d6268, Cyan #6ac9d7, Link #086575, Linien #c9d5d4, Szenariofläche #e1efed. Schriften IBM Plex Sans 400/500/600/700 und Mono 400 aus assets/fonts, vorhandene OFL-Lizenz unverändert.

## Typografie und Layout
Maximalbreite 1180px. H1 2,7 bis 4,6rem, H2 1,9 bis 2,8rem, Fließtext 18px/1,65, mobil 17px. CSS-Variablen für Abschnittsabstand und Heroabstand. Zweispaltige Layouts werden unter 650px einspaltig. Navigation bleibt sichtbar und bricht um.

## Komponenten
hero mit erklärender hero-note, rein dekoratives CSS-Radio (aria-hidden), steps als geordnete Liste, status-list für Vorhanden/Geplant/Später, principle als dunkler Kontrastabschnitt, timeline als lineare Monatsplanung, contact mit Mail/GitHub, gemeinsame Navigation und Footer. Native Links mit mindestens 40px Navigationshöhe und sichtbarem 3px-Fokus; Skip-Link. Keine Bewegungsanimation.

## Assets
Bestehende Prüfspitze als favicon.svg, bestehende lokale Favicon- und Schriftdateien. Radiozeichnung ausschließlich CSS. Keine Fotografie oder generierten Bilder. Bestehende Lizenzangaben bleiben erhalten.
