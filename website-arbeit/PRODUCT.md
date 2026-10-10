# PRODUCT.md — RepairProbe Öffentlichkeitsseite

 Quelle der Fakten: kanonisches Repository `RepairProbe/repair-probe` (Stand 2026-10-10, HEAD b9658cff), insbesondere `README.md`, `docs/architecture/ADR-0002…0004`, `docs/funding/application-readiness-2026-10-09.md`, `docs/research/research-synthesis-2026-10-09.md`, `docs/public-presence/PUBLIC_COPY.md`, `docs/funding/one-liners.md`, `docs/funding/impact-and-applicant-case.md`.

## Wofür ist die Seite da?

Hauptziel: **verstehen und vertrauen**. Ein erster Besucher soll in wenigen Minuten verstehen, was RepairProbe ist, welches Problem es angeht, was den Ansatz unterscheidet, was heute existiert und was ausdrücklich Hypothese bleibt. Sekundärziele: GitHub-Besuch, Kontakt per Mail, Fahrplan-Ansicht.

## Für wen ist die Seite?

1. Normaler Besucher ohne Vorwissen.
2. Person mit defektem Gerät, die prüft, ob RepairProbe später helfen könnte.
3. Repair-Café-Aktive und offene Werkstätten.
4. Reparatur- und Elektronikfachleute.
5. Entwickler und Open-Source-Interessierte.
6. Potenzielle Mitwirkende und Kollaborateure.
7. Förder- und Grant-Evaluatoren.
8. GitHub-Besucher, die der Organisation-Link hierher führt.

Besucher kommen über: GitHub-Organisation, Repo-Links, persönliche Empfehlungen aus Repair-Café-Kontext, zunehmend KI-Suchmaschinen (deshalb `llms.txt` und Faktensätze).

## Was die Seite sagen muss (Belege im Repo)

- RepairProbe ist ein unabhängiges Open-Source-Projekt von Raik Müller (PUBLIC_COPY).
- Kanonischer Selbstbeschrieb: „Offene Software-Infrastruktur für smartphone-gestützte, KI-geführte Elektronikdiagnose und kontextbezogenes Reparaturlernen“ (README).
- Architektur: software-only, smartphone-first, local-first (ADR-0002/0003). Keine eigene Messhardware nötig, keine Pflicht-Cloud.
- Evidenzklassen OBSERVED/MEASURED/RETRIEVED/INFERRED/CONFIRMED als Kerninvariante `INFERENCE_IS_NOT_MEASUREMENT` (ADR-0002).
- Vorhandene Baseline: Repair Measurement Event v1, fail-closed Validierung, MockAdapter, append-only Evidence Store, deterministisches Fixture-Replay, passive-first SafetyGate, vier Baseline-Tests (README, PRE_FUNDING_BASELINE).
- Reale Reparatursitzung (Fernseher-Netzteil) als erprobter Ablauf dokumentiert (ADR-0002 Kontext).
- Erste Repair-Café-Rückmeldung: ein ausgefüllter Fragebogen (n=1, explorativ) + ein Gesprächswunsch (RC-R001, RC-C002, Synthese 2026-10-09). Betonung hat sich verschoben: Informationszugang, Demontage, Ersatzteile.
- Prototype-Fund-Antrag in Vorbereitung, Stand 2026-10-09 `ACTIVE_PRE_SUBMISSION_AUDIT`. Nichts eingereicht, nichts bewilligt. Geplanter Umfang 850 Stunden / 6 Monate.
- Externer Beleg fürs Problem: Open Repair Alliance Report 2024, 18.921 dokumentierte Fälle mit Hindernis: 12 % Reparaturinformation fehlt, 10 % Werkzeug fehlt.

## Was ausdrücklich NICHT auf die Seite gehört

- Keine erfundenen Testimonials, Nutzerzahlen, Partner, Erfolgsquoten.
- Keine Behauptung, die App existiere bereits.
- Keine Förderzusage, keine Partnerschaft aus Repair-Café-Kontakt.
- Keine privaten Daten (Anschrift, private Repos, Antragsinterna jenseits des öffentlichen Fahrplanstands).
- Kein Tracking, keine Analytics, keine Drittanbieter-Skripte.
- Keine Behauptung technischer Überlegenheit gegenüber allgemeinem KI-Chat (bewusst nicht behauptet, README).

## Tonalität und Sprache

- Deutsch (`lang="de"`), du/neutral fürs Projekt, Ich-Form im Personenabschnitt.
- Schreibregeln des website-bauen-Skills (schreibregeln.md) gelten: konkret statt groß, keine Werbewörter, keine Gedankenstrich-Satzzeichen, keine Dreierreihen, echte Umlaute, deutsche Anführungszeichen.
- Alles, was nicht belegt ist, wird als Plan, Hypothese oder offene Frage markiert.
