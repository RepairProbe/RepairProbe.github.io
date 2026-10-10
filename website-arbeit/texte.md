# texte.md — alle Texte der Seite (Phase 3)

Sprache: Deutsch, `lang="de"`. Schreibregeln geprüft (siehe Ende). Quelle aller Fakten: `website-arbeit/PRODUCT.md` mit Repo-Belegen. Personenvorgaben aus PR #7 (gemerged 2026-10-10) werden wörtlich übernommen.

---

## Claim-/Evidenz-Audit des Ist-Zustands (vor Redesign)

| # | Bestehende Aussage | Klasse | Maßnahme |
|---|---|---|---|
| 1 | „Quelloffene Reparaturhilfe“ | VERIFIED_PARTIAL | Behalten, stets mit „in Entwicklung“ gekoppelt |
| 2 | Hero-Beispiel „Fernseher … Eine Spannung wurde gemessen“ | PARTIALLY GROUND (generisch formuliert) | Ersetzt durch den dokumentierten echten Ablauf aus ADR-0002 (Diodentest statt pauschaler Spannung), klar als Entwicklungsfall gekennzeichnet |
| 3 | „Vier einfache Schritte“ als „So geht’s“ | MISLEADING (App existiert nicht) | Umbenannt in geplanten Ablauf, mit dem echten Fall verschmolzen und als „so soll es einmal laufen“ markiert |
| 4 | Evidenz-Gitter Gesehen/Gemessen/Nachgeschlagen/Vermutet/Bestätigt | VERIFIED_CURRENT | Behalten, ausgebaut mit kanonischen Beispielen aus ADR-0002 |
| 5 | „Noch nicht fertig.“ | VERIFIED_CURRENT | Behalten |
| 6 | „Messdaten können geprüft, gespeichert und mit ihrer Herkunft festgehalten werden“ | VERIFIED_CURRENT | Präzisiert (vier Baseline-Tests, Replay, SafetyGate) |
| 7 | Fahrplan „Stand 28.09.2026“, „Am 1. Oktober 2026 soll … abgeglichen werden“ | OUTDATED | Aktualisiert auf Stand 10.10.2026, Readiness-Prüfung vom 9.10.2026, „nichts eingereicht, nichts bewilligt“ |
| 8 | 850-Stunden-/Monatsplanung | VERIFIED_CURRENT (readiness 2026-10-09) | Ergänzt |
| 9 | Technische-Baseline-Seite | VERIFIED_CURRENT | Detailrefresh, Ökosystem-Einordnung ergänzt |
| 10 | Person CNC-Hintergrund | VERIFIED_CURRENT (PUBLIC_COPY) | Behalten, persönliche Motivation ergänzt |
| 11 | „Keine Nutzungsverfolgung · keine erfundenen Messwerte“ | VERIFIED_CURRENT | Behalten |
| 12 | Unterseiten verlinken `index.html#idee` | BROKEN (Anker existiert nicht) | Behoben (neue Ankerstruktur) |
| 13 | Org-Profil verlinkt „Öffentlicher Fahrplan“ auf GitHub-Projects | STALE/RISK (Erreichbarkeit ungeprüft) | Eigener PR in `RepairProbe/.github` auf `https://repairprobe.github.io/roadmap.html` |
| 14 | „Öffentlicher Fahrplan · Stand 28.09.2026“ (Fahrplan-Unterseiten-Nav verweist auf `#idee`, `#pruefung` teils fehlend) | BROKEN/PARTIAL | Nav auf allen Seiten vereinheitlicht |

Nicht vorhandene, aber nötige Korrekturen: keine. Es wurden keine Testimonials, Zahlen, Partner oder Erfolgsquoten erfunden; die einzige Statistik (Open Repair Alliance 2024) ist mit Quelle belegt.

---

## Seite 1: index.html (Startseite)

**Meta**
- Titel: `RepairProbe – Reparaturdiagnose mit klaren Belegen`
- Beschreibung: `Quelloffene Reparaturdiagnose in Entwicklung: Beobachtungen, echte Messwerte, Quellen und Vermutungen bleiben getrennt. Offen einsehbar auf GitHub.`

### Hero
- Sprunglink: `Zum Inhalt springen`
- Marke: RepairProbe (Stempelzeichen: Prüfspitze), Link auf Startseite
- Nav: `Evidenzmodell` · `Fahrplan` · `Technische Basis` · `GitHub` (extern, mit Hinweis „öffnet github.com“ als title/aria)
- H1: `Gemessen ist nur, was wirklich gemessen wurde.`
- Lede: `RepairProbe ist ein quelloffenes Projekt, das Reparaturdiagnose nachvollziehbar machen will. Beobachtungen, echte Messwerte, technische Quellen und KI-Einordnungen bleiben hier getrennt. So bleibt erkennbar, was bekannt ist und was nur vermutet wird.`
- Ehrlichkeitszeile: `Noch in Entwicklung. Eine fertige App gibt es nicht. Alles hier ist öffentlich einsehbar.`
- Aktionen: Button `Den Ansatz verstehen` → #ansatz · Button `Was heute existiert` → #stand · Textlink `Projekt auf GitHub`
- Hero-Seitenpanel (Statusblock, Mono-Stempel):
  - `BASELINE` → `vorhanden`
  - `APP` → `in Planung`
  - `ANTRAG` → `in Vorbereitung`
  - `FÖRDERUNG` → `nicht bewilligt`
  - Zeile darunter: `Stand 10.10.2026`

### Abschnitt: Das Problem (id="problem")
- Index `01`, H2: `Reparieren scheitert selten am Löten. Meist fehlt das passende Wissen.`
- Text: `Ein defektes Gerät stellt Fragen, die sich nicht per Foto beantworten lassen. Welche Spannung ist hier normal? Welche Bauteile fallen bei diesem Modell öfter aus? Wie kommt man überhaupt an die betreffende Stelle? Und welches Ersatzteil passt?`
- Text: `Diese Informationen liegen verstreut: in Datenblättern, Schaltplänen, Forumbeiträgen und im Kopf erfahrener Menschen. Wer sie nicht findet oder nicht verbinden kann, bricht ab oder entsorgt ein Gerät, das zu retten gewesen wäre.`
- Belegabsatz: `Das Open Repair Alliance berichtet in seinem Jahresbericht 2024 über 18.921 dokumentierte Reparaturfälle mit Hindernis: In 12 Prozent der Fälle fehlte die Reparaturinformation, in 10 Prozent fehlten Werkzeug oder Messgerät.` Link: `Bericht des Open Repair Alliance (2024, englisch)` → https://openrepair.org/wp-content/uploads/2024/10/ORA-report-2024-The-rise-of-community-repair.pdf

### Abschnitt: Der Ansatz (id="ansatz")
- Index `02`, H2: `Beobachtung, Messung, Quelle und Vermutung bleiben getrennt.`
- Text: `RepairProbe führt vier Arten von Information zusammen und verwaltet sie in einem Repair Case, einem nachvollziehbaren Reparaturfall. Der Kern des Projekts ist eine harte Grenze:`
- Hervorhebungsblock (Markenkern): `Eine KI darf einordnen und Vermutungen bilden. Sie darf keine Messwerte erfinden. Was gemessen wurde, steht im Fall. Was nur vermutet wird, ist als Vermutung markiert.`
- Text: `Ein Foto darf zum Beispiel nie einen ESR-Wert erfinden. Es darf aber begründet sagen: Dieser Elko ist ein hochpriorisierter Prüfkandidat. Die Entscheidung, was geprüft wird, bleibt bei der reparierenden Person.`
- Fünf Evidenzklassen als Protokollzeilen (Vorschau, Mono-Stempel + Kurztext):
  - `OBSERVED` — `Gesehen: direkt sichtbar oder von einer Person beobachtet.`
  - `MEASURED` — `Gemessen: tatsächlich mit einem Messgerät erfasst.`
  - `RETRIEVED` — `Nachgeschlagen: aus Schaltplan, Datenblatt oder Reparaturfall.`
  - `INFERRED` — `Vermutet: von der KI aus vorhandenen Hinweisen abgeleitet.`
  - `CONFIRMED` — `Bestätigt: durch Gegenprobe, Bauteilprüfung oder gelungene Reparatur.`
- Link: `Das Evidenzmodell im Detail ansehen` → evidenzmodell.html
- Nebensatz: `Darüber hinaus bleibt die Sicherheit eine Sache der Software, nicht des Sprachmodells: gefährliche oder unbekannte Energiezustände führen zu einer klaren Ablehnung, nicht zu einer Wagnis-Empfehlung.`

### Abschnitt: Ein echter Ablauf (id="fall")
- Index `03`, H2: `Ein Fernseher, der nicht mehr angeht.`
- Einordnung (wichtig, ehrlich): `Dieser Ablauf ist in der Entwicklungsarbeit real so durchlaufen worden. Er zeigt, wie das Projekt Reparatur versteht. Die App dafür existiert noch nicht.`
- Protokoll-Einträge (Mono-Stempel + Text):
  - `OBSERVED` — `Fotos vom Netzteil-Board und eine Beschreibung des Fehlers: der Fernseher bleibt schwarz.`
  - `RETRIEVED` — `Zu diesem Board bekannte Fehlerbilder recherchieren: bei dieser Bauart fällt häufig der Gleichrichter im Sekundärkreis aus.`
  - `INFERRED` — `Die Diode wird zum höchsten Prüfkandidaten erklärt. Das ist eine Einordnung, kein Messergebnis.`
  - `MEASURED` — `Ein Mensch führt den Diodentest durch. Der Wert kommt vom Messgerät, nicht vom Modell.`
  - `CONFIRMED` — `Mit angehobener Leitung bestätigt der Test den Kurzschluss. Die Vermutung wird zum belegten Befund.`
  - `INFERRED` — `Weil das Netzteil diese Bauart hat, werden die umliegenden Elkos als nächste Prüfkandidaten priorisiert.`
  - `MEASURED` — `Kapazität und ESR werden extern gemessen und in den Fall zurückgeschrieben.`
- Abschlusszeile: `Jeder Eintrag trägt seine Herkunft im Fall. Wer später weitermacht, sieht genau, was belegt ist und was Vermutung blieb.`

### Abschnitt: Aktueller Stand (id="stand")
- Index `04`, H2: `Was heute existiert. Was Hypothese bleibt.`
- Spalte `Vorhanden` (Stempel `VORHANDEN`):
  - `Ein geprüfter Vertrag für Messereignisse (Repair Measurement Event v1) mit fail-closed Validierung.`
  - `Ein anhängungssicherer Evidence Store und ein deterministisches Fixture-Replay für reproduzierbare Tests.`
  - `Eine passive Safety-Baseline, die unsichere Aktionen standardmäßig ablehnt.`
  - `Vier Baseline-Tests im Kernrepository, ausführbar ohne Hardware, Konto oder Cloud.`
- Spalte `Hypothese und Planung` (Stempel `OFFEN`):
  - `Die Smartphone-App mit Foto-Eingabe und geführter Fehlersuche ist noch nicht gebaut.`
  - `Ob der Ansatz Reparaturen tatsächlich erleichtert, muss mit echten Fällen gezeigt werden. Diese Wirkung ist bisher nicht belegt.`
- Unterabschnitt `Erste Rückmeldung aus der Praxis`:
  - `Ein Repair-Café hat einen Fragebogen beantwortet, eine weitere Person hat ein Gespräch zugesagt. Das ist wenig, und es ist die einzige Rückmeldung, die bislang vorliegt.`
  - `Die Antworten bestärken: Smartphone-Unterstützung ist hilfreich, die Trennung von Beobachtung, Messung und Quelle wird geschätzt, und begrenzte KI-Rollen (Fotos einordnen, Verlauf zusammenfassen) werden akzeptiert.`
  - `Die Antworten korrigieren: Statt „Welcher Prüfschritt kommt als Nächstes?“ steht im Alltag offenbar mehr der Zugang zu Reparaturinformationen, das Öffnen des Geräts und das Finden passender Ersatzteile im Weg. RepairProbe hat die Planung daraufhin angepasst.`
  - Kennzeichnung: `Eine Rückmeldung, n=1, explorativ. Keine Partnerschaft, keine Empfehlung.`
- Aktionen: Button `Fahrplan ansehen` → roadmap.html · Button `Technische Basis` → technical-baseline.html

### Abschnitt: Person (id="person")
- Index `05`, H2: `Ich bin Raik Müller.`
- Zeile: `39+ Jahre jung 😜` (wörtlich aus PR #7 des Projektinhabers)
- Text: `Mein Hintergrund liegt im technischen/CNC-Bereich. Ich beschäftige mich praktisch mit Reparatur, Elektronik, Software und Automatisierung.`
- Text: `Reparieren hat mich schon interessiert, lange bevor es KI-Werkzeuge gab. Die eigentliche Hürde war selten die Arbeit am Gerät. Sie war, die richtigen Informationen zu finden und zu verbinden: Forumsbeiträge, Datenblätter, Serviceunterlagen, Messwerte und Erfahrung anderer. Genau daran setzt RepairProbe an.`
- Ziel (wörtlich aus PR #7): `Mein Ziel mit RepairProbe: Fehlersuche verständlicher machen, damit leichter erkennbar ist, was wirklich bekannt ist, was nur vermutet wird und was als Nächstes sinnvoll geprüft werden sollte.`

### Abschnitt: FAQ (id="fragen")
- Index `06`, H2: `Häufige Fragen`
- Q: `Ist RepairProbe eine fertige App?` — A: `Nein. Es gibt eine kleine, geprüfte technische Basis im Kernrepository. Die Smartphone-App und die geführte Fehlersuche sind geplant und noch nicht gebaut.`
- Q: `Brauche ich spezielle Messhardware von RepairProbe?` — A: `Nein. RepairProbe ist reine Software und passt sich den Werkzeugen an, die vorhanden sind. Ein Multimeter oder Komponententester liefert zusätzliche Messwerte, nötig ist das nicht.`
- Q: `Darf die KI bei RepairProbe Messwerte erfinden?` — A: `Nein. KI-Ausgaben sind Einordnungen und bleiben als solche markiert. Messwerte kommen nur von echten Messgeräten und von Menschen. Diese Grenze ist im Projekt eine Grundregel: Inference is not Measurement.`
- Q: `Ist die Förderung schon bewilligt?` — A: `Nein. Ein Antrag zum Prototype Fund ist in Vorbereitung. Eingereicht ist er noch nicht, bewilligt ist nichts.`
- Q: `Wie kann ich Feedback geben oder mitmachen?` — A: `Schreib eine Mail an repairprobe@gmail.com oder schau auf GitHub vorbei. Rückmeldung aus Repair-Cafés und aus der praktischen Reparatur ist ausdrücklich willkommen.`

### Kontakt-Abschnitt (id="kontakt")
- H2: `Fragen oder Hinweise?`
- Button `repairprobe@gmail.com` (mailto) · Button `Projekt auf GitHub` → https://github.com/RepairProbe

### Footer (alle Seiten)
- Marke + `Unabhängiges Open-Source-Projekt`
- Links: `Evidenzmodell` · `Fahrplan` · `Technische Basis` · `Kontakt`
- Zeile: `Keine Nutzungsverfolgung. Keine erfundenen Messwerte. Code lizenziert unter Apache-2.0.`

---

## Seite 2: evidenzmodell.html

**Meta**
- Titel: `Evidenzmodell – RepairProbe`
- Beschreibung: `Fünf Evidenzklassen von OBSERVED bis CONFIRMED. Warum KI-Einordnungen keine Messwerte ersetzen und Unsicherheit sichtbar bleibt.`

### Hero
- H1: `Fünf Evidenzklassen. Eine harte Grenze.`
- Lede: `Jede Information in einem Reparaturfall trägt eine Herkunft. Fünf Klassen trennen, was gesehen, gemessen, nachgeschlagen, vermutet und bestätigt wurde. Sie sind nicht austauschbar.`
- Ehrlichkeitszeile: `Diese Klassen sind im Kernrepository als technische Verträge angelegt, nicht nur als Idee.`

### Die fünf Klassen mit kanonischen Beispielen
Jede Klasse: Stempel + Definition + Beispielzeile (aus ADR-0002):
- `OBSERVED` — `Direkt sichtbar oder von einer Person unmittelbar beobachtet.` Beispiel: `Auf dem Foto ist der Deckel des Elkos gewölbt.`
- `MEASURED` — `Ein Wert, der tatsächlich mit einem Messgerät erfasst wurde.` Beispiel: `Der Komponententester zeigt ESR = 3,6 Ω.`
- `RETRIEVED` — `Aus einer technischen Quelle oder einem dokumentierten Reparaturfall abgerufen.` Beispiel: `Das Servicehandbuch zeigt: D318 hängt an der Sekundärkreis-Gleichrichtung.`
- `INFERRED` — `Eine Schlussfolgerung aus der vorhandenen Evidenz, zum Beispiel von der KI.` Beispiel: `Der Elko ist ein Hauptverdächtiger. Bleibt eine Vermutung, solange nichts gemessen wurde.`
- `CONFIRMED` — `Durch Gegenprobe, Bauteilprüfung oder Reparaturergebnis bestätigt.` Beispiel: `D318 ist mit angehobener Leitung immer noch kurzschlüssig. Die Diode ist defekt.`

### Die Grenze
- H2: `Inference is not Measurement.`
- Text: `Das Modell darf fehlende Messungen nicht simulieren und Vermutungen nicht stillschweigend zu Tatsachen befördern. Wer später in den Fall schaut, soll jeder Aussage ansehen, woher sie kommt.`
- Gegenüberstellung (zwei Panels):
  - `Was ein Foto leisten darf:` `Gerätelabels und Bauteilbezeichnungen erkennen, Bauteilfamilien einordnen, sichtbare Schäden benennen, räumliche Zusammenhänge für die Führung nutzen.`
  - `Was ein Foto nie liefern darf:` `ESR, Leckstrom, Kapazität, Widerstand, Rail-Spannungen oder Halbleiterzustände. Diese Werte kommen nur aus echten Messungen.`

### Unsicherheit
- H2: `Unsicherheit bleibt sichtbar.`
- Text: `Eine brauchbare Erklärung beschreibt, was bekannt ist, was erwartet wird, was abweicht und was weiterhin unklar ist. „U17 ersetzen“ ist keine Diagnose. Wo kein Messgerät vorhanden ist, bleibt der Fall bei Beobachtung, Recherche und begründeter Wahrscheinlichkeit, und die Grenze wird ausdrücklich gekennzeichnet.`

### Sicherheit
- H2: `Anfängerfreundlich heißt nicht gefahrlos.`
- Text: `Die Wissensbarriere soll sinken, die elektrische Sicherheitsbarriere nicht. Bei unbekannten oder gefährlichen Energiezuständen lehnt die Software riskante Schritte standardmäßig ab (fail-closed). Sicherheitsregeln liegen außerhalb des Sprachmodells und können von ihm nicht überschrieben werden. Jede Empfehlung wird erklärt, bevor etwas passiert: explanation before action.`
- Nebensatz: `Auch das ersetzt keine elektrische Sicherheitszertifizierung und keine Sorgfalt der Person am Gerät.`

### Ausblick
- Zeile: `Der Ausbau des Evidenzmodells ist Teil des geplanten Förderumfangs.`
- Aktionen: Button `Zum Fahrplan` → roadmap.html · Button `Technische Basis` → technical-baseline.html

---

## Seite 3: roadmap.html

**Meta**
- Titel: `Fahrplan – RepairProbe`
- Beschreibung: `Aktueller Stand, Antragsvorbereitung, geplanter Förderumfang und bewusste Grenzen von RepairProbe. Nichts eingereicht, nichts bewilligt.`

### Hero
- Epoche: `Öffentlicher Fahrplan · Stand 10.10.2026`
- H1: `Was ist schon da? Was kommt als Nächstes?`
- Lede: `Dieser Fahrplan trennt vorhandene Vorarbeit, laufende Antragsvorbereitung und geplante Förderarbeit. Ein Antrag zum Prototype Fund ist in Vorbereitung. Eingereicht ist er noch nicht. Eine Förderung ist weder beantragt noch bewilligt.`
- Aktionen: Button `Zum aktuellen Stand` → #heute · Button `Technische Vorarbeit` → technical-baseline.html
- Ehrlichkeitszeile: `Vorhanden ≠ geplant · geplant ≠ bewilligt · Wirkung wird erst geprüft`
- Seitenpanel Statuslegende: `VORHANDEN` bereits umgesetzt · `IN ARBEIT` aktuell vorbereitet · `GEPLANT` nur bei Förderung · `OPTIONAL` noch nicht entschieden · `OFFEN` nicht versprochen

### Heute (id="heute")
- H2: `Der technische Ausgangspunkt ist vorhanden.`
- Text: `RepairProbe startet nicht bei null, aber die vorhandene Baseline ist noch kein fertiges Produkt.`
- Karten (Stempel `Vorhanden`):
  - `Messereignis & Evidenzbasis` — `Strukturierte Messereignisse, Evidence Store und die Trennung von realer Messung und Ableitung sind als technische Baseline vorhanden.`
  - `Validierung & Replay` — `Fail-closed Validierung, Mock-Adapter und deterministische Fixture-Replays erlauben reproduzierbare Softwaretests ohne echte Hardware.`
  - `Öffentliche Projektseite` — `Die öffentliche Website dokumentiert Idee, Evidenzmodell, Projektstatus, technische Vorarbeit und Kontaktmöglichkeiten.`

### In Arbeit (id="antrag")
- H2: `Vor der Einreichung: den Antrag prüfen, nicht Features stapeln.`
- Text: `Für den Prototype Fund (Jahrgang 03) wird ein Bewerbung vorbereitet. Gegenstand ist Software-Infrastruktur, geplanter Umfang sind 850 Stunden über sechs Monate. Der Entwurf wird derzeit gegen das tatsächlich geöffnete Antragsformular geprüft, zuletzt am 9. Oktober 2026.`
- Text: `Geprüft werden Fragen, Wort- und Zeichenlimits, Antragsberechtigung, FOSS-Anforderungen, Arbeitsstunden und die optionale Second Stage. Offen sind persönliche Angaben, die reale zeitliche Verfügbarkeit und ein externes Gegenlesen durch Nicht-Fachleute.`
- Text: `Ob das Projekt solo oder als zweiköpfiges Team antritt, und ob die Second Stage mitgeht, ist noch nicht entschieden.`
- Callout: `Nutzerinterviews und Fragebögen liefern zusätzliche Evidenz. Sie sind kein Gate für die technische Weiterentwicklung.`

### Förderphase (id="foerderphase")
- H2: `Sechs Monate für einen offenen, überprüfbaren Prototyp.`
- Text: `Diese Schritte sind der geplante Förderumfang. Sie sind noch nicht bewilligt und werden erst nach einer positiven Förderentscheidung umgesetzt.`
- Karten (Stempel `Monat 1` … `Monat 6`, Inhalte unverändert aus bestehender Seite, sie sind kanonisch): Evidenz- und Repair-Case-Vertrag · Visueller Smartphone-Intake · Prüfschritte & Sicherheitsgrenzen · Austauschbare KI- & Quellenanbindung · Local-first & Interoperabilität · Validierung, Hardening & Release (Vergleich gegen einen normalen multimodalen KI-Chat)

### Second Stage (id="second-stage")
- H2: `Mögliche Second Stage: Nutzung statt Feature-Sammlung.`
- Text: `Diese vier zusätzlichen Monate sind eine vorbereitete Option. Die Entscheidung dafür ist offen; bewilligt ist nichts.` (Karten Monat 7–10 unverändert: Nutzbarkeit & Dokumentation · Interoperabilität & Beiträge · Community & reale Nutzung · Nachhaltigkeit)

### Grenzen (id="grenzen")
- H2: `Was dieser Fahrplan ausdrücklich nicht verspricht.`
- Text: `RepairProbe plant im Förderkern kein eigenes LLM, keine universellen Gerätetreiber, kein Boardview-System, keine eigene Pflicht-Cloud und keine dedizierte RepairProbe-Messhardware.`
- Text: `Bestehende Reparaturquellen, Messsoftware, Testframeworks und KI-Modelle werden über offene Grenzen angebunden statt nachgebaut. Auch universelle Diagnose, zertifizierte elektrische Sicherheit, nachgewiesene Umweltwirkung oder garantierte Reparaturerfolge werden nicht versprochen.`
- Callout: `Ziel: ein kleiner, offener und reproduzierbarer Softwarekern, dessen Nutzen sich anschließend anhand realer Evidenz bewerten lässt.`

### Weiterlesen
- Buttons: `Zur Startseite` · `Technische Vorarbeit` · `RepairProbe auf GitHub`

---

## Seite 4: technical-baseline.html

**Meta**
- Titel: `Technische Basis – RepairProbe`
- Beschreibung: `Die vorhandene Baseline vor einer Förderung: Messereignis, Validierung, Mock-Adapter, Evidence Store, Replay und Safety. Und was sie nicht beweist.`

### Hero
- H1: `Was bereits existiert, und was noch nicht.`
- Lede: `RepairProbe startet nicht bei null. Gleichzeitig soll vorhandene Vorarbeit nicht mit der beantragten Neuentwicklung vermischt werden. Diese Seite dokumentiert den technischen Ausgangspunkt und seine Grenzen.`
- Aktionen: `Baseline ansehen` → #vorhanden · `RepairProbe auf GitHub`
- Ehrlichkeitszeile: `Vorarbeit ≠ Förderarbeit · Softwaretest ≠ Reparaturerfolg · Inference ≠ Measurement`
- Seitenpanel: `BASELINE` vor Förderung · `FOSS` Förderergebnisse geplant · `LOCAL-FIRST` Kern ohne Pflicht-Cloud · `VALIDIERUNG` noch ausstehend; Panel-Kernsatz: `Machbarkeit gezeigt. Produktwirkung offen.`

### Baseline (id="vorhanden")
- H2: `Diese Bausteine sind bereits vorhanden.`
- Text: `Die aktuelle Baseline ist bewusst klein und hardwarefrei. Sie ist ein technischer Ausgangspunkt, kein Beleg für Produktwirkung.`
- Karten (Stempel `Vorhanden`): Repair Measurement Event v1 · Fail-closed Validierung · Mock-Adapter · Evidence Store (append-only) · Fixture-Replay · Safety-Baseline (passive, fail-closed Basis; ersetzt keine Sicherheitszertifizierung)
- Ergänzende Zeile: `Vier Baseline-Tests laufen ohne Hardware, ohne LLM-Zugang, ohne Konto und ohne bezahlten Dienst. Ein Replay-Skript schreibt ausschließlich in ein lokal ignoriertes Verzeichnis und kennzeichnet seine Ausgabe als Software-Fixture, nicht als reale Reparaturevidenz.`

### Grenzen (id="grenzen")
- H2: `Was diese Baseline ausdrücklich nicht beweist.`
- Text: `Die vorhandenen Tests belegen, dass definierte Softwareverträge und Fixtures wie erwartet verarbeitet werden.`
- Text: `Sie belegen nicht, dass RepairProbe ein Gerät korrekt diagnostiziert, Bauteile zuverlässig aus Fotos erkennt, einer allgemeinen KI überlegen ist oder Reparaturen erfolgreicher macht.`
- Callout: `Evidence before claim: Diese Wirkungen sollen erst im geförderten Prototyp systematisch geprüft werden.`

### Förderarbeit (id="foerderung")
- H2: `Die Förderung beginnt oberhalb der Baseline.`
- Text: `Der geplante Förderumfang konzentriert sich auf eine offene, wiederverwendbare Repair-Case- und Evidenzschicht.`
- Schritte 01–05 (unverändert kanonisch): Repair Case · Evidenztypen · Safety · Interoperabilität · Validierung

### Prüfbarkeit (id="pruefung")
- H2: `Klare Trennung zwischen vorhanden, geplant und unbewiesen.`
- Karten: `Vor Förderung` Technischer Ausgangspunkt · `Förderarbeit` Neue Entwicklung · `Noch offen` Produktwirkung

### Ökosystem (id="oekosystem")
- H2: `Ergänzung statt Ersatz.`
- Text: `RepairProbe erfindet Reparaturwissen und Messsoftware nicht neu, sondern bindet Bestehendes an: Reparaturanleitungen von Plattformen wie iFixit, offene Reparaturdaten (Open Repair Data Standard), Messhardware-Zugriff über Projekte wie sigrok und übliche Instrumente der Reparierenden.`
- Text: `Der engere Beitrag des Projekts ist eine offene Schicht für Evidenz, Herkunft, Sicherheit und Reparaturfälle, die vorhandene Werkzeuge verbindet, statt sie zu ersetzen.`

---

## Seite 5: 404.html
- H1: `Seite nicht gefunden.`
- Text: `Diese Adresse existiert nicht. Startseite, Evidenzmodell und Fahrplan sind erreichbar.`
- Buttons: `Zur Startseite` · `Zum Fahrplan`

---

## Meta-Texte übergreifend
- OG-Titel: `RepairProbe – Gemessen ist nur, was wirklich gemessen wurde.`
- OG-Beschreibung: `Quelloffene Reparaturdiagnose in Entwicklung. Beobachtung, Messung, Quelle und Vermutung bleiben getrennt.`
- Vorschaubild: 1200×630, Papier-Hell, Tinte-Schriftzug, Cyan-Stempelmarke.

## Formular-Texte
Kein Formular auf der Seite (Kontakt per Mailto und GitHub). Keine Zusagen zu Antwortzeiten.

## Faktensätze (Quelle für llms.txt und JSON-LD)

1. RepairProbe ist ein unabhängiges Open-Source-Projekt von Raik Müller.
2. RepairProbe entwickelt offene Software-Infrastruktur für smartphone-gestützte, KI-geführte Elektronikdiagnose.
3. Der Kern des Projekts trennt fünf Evidenzklassen: OBSERVED, MEASURED, RETRIEVED, INFERRED und CONFIRMED.
4. KI-Ausgaben gelten als Einordnung und dürfen Messwerte nicht ersetzen oder erfinden.
5. Die Architektur ist software-only, smartphone-first und local-first. Eine Pflicht-Cloud gibt es nicht, dedizierte Messhardware ist nicht erforderlich.
6. Vorhanden ist eine kleine geprüfte Baseline: Messereignis-Vertrag, fail-closed Validierung, Mock-Adapter, append-only Evidence Store, deterministisches Fixture-Replay, passive Safety-Baseline und vier Tests.
7. Eine Smartphone-App existiert noch nicht. Sie ist Teil der Planung.
8. Ein Antrag zum Prototype Fund (Jahrgang 03) ist in Vorbereitung, geplanter Umfang 850 Stunden über sechs Monate. Eingereicht ist er nicht, bewilligt ist nichts.
9. Ein Repair-Café hat einen Fragebogen beantwortet (n=1, explorativ), eine weitere Person hat ein Gespräch zugesagt. Daraufhin wurde die Planung von „nächster Prüfschritt“ stärker Richtung Reparaturinformationszugang, Demontage und Ersatzteile angepasst.
10. Kontakt: repairprobe@gmail.com. GitHub: https://github.com/RepairProbe. Website: https://repairprobe.github.io/.
11. Neue Projektarbeit wird unter Apache-2.0 veröffentlicht.
12. Die Website verwendet kein Tracking, keine Cookies und keine Analyse-Dienste.

## Offene Fragen an die Projektinhaberin/den Projektinhaber

1. Impressum: Für eine vollständige Angabe fehlt die Anschrift. Kein Impressum zu veröffentlichen, solange diese nicht vorliegt.
2. Porträtfoto für den Personenabschnitt (wird nicht erfunden).
3. Datenschutzseite: Derzeit reicht die Footer-Aussage (kein Tracking). Falls gewünscht, kann eine faktische Datenschutzerklärung ergänzt werden.

## Schreibregel-Check (Abhaken)

- Keine Gedankenstriche als Satzzeichen: erfüllt (bitte im Build erneut gegenprüfen)
- Keine Werbe- und Modewörter (erstklassig, innovativ, nahtlos, ganzheitlich): erfüllt
- Keine unbelegten Zahlen: erfüllt (ORA-Zahl mit Quelle, n=1 gekennzeichnet)
- Keine Zusagen zu Antwortzeit, Ablaufdauer oder Kosten: erfüllt
- Echte Umlaute und ß: erfüllt
- Anrede durchgehalten (neutral, Person in Ich-Form): erfüllt
- Deutsche Anführungszeichen im finalen HTML: im Build umsetzen
- Kein Etikett-mit-Doppelpunkt-Aufbau in Fließtexten außer in der wörtlichen Personenvorgabe: erfüllt
