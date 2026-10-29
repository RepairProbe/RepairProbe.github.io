# Website-Texte · Neuausrichtung 28.10.2026

## Gemeinsame Navigation und Footer

RepairProbe
Start
Prinzip
Projektstand
Technische Basis
Kontakt
Zum Inhalt springen
Unabhängiges Projekt von Raik Müller.
Keine Nutzungsverfolgung. Schriften lokal gehostet.
Website-Code: Apache-2.0. Produktcode derzeit privat; FOSS-Veröffentlichung geplant.
GitHub ↗

## index.html

Titel: Reparieren beginnt mit Verstehen. | RepairProbe
Beschreibung: RepairProbe entwickelt offene Reparaturhilfe für Elektronik: Quellen einordnen, echte Messungen und Vermutungen unterscheiden. Prototyp geplant.

Offene Software für die Elektronikreparatur
Reparieren beginnt
mit Verstehen.
In Entwicklung · Kleine technische Basis vorhanden · Noch keine fertige App
RepairProbe soll Ehrenamtlichen in Repair-Cafés und offenen Werkstätten helfen, einen Elektronikfehler zu prüfen. In einem geplanten Reparaturfall sollen Hinweise zum Gerät, eigene Beobachtungen und Messungen nachvollziehbar bleiben.
Den geplanten Ablauf ansehen
↓
Projektstand &amp; Fahrplan →
Die Idee an einem Beispiel
Das Radio bleibt stumm.
Eine Anleitung hier, ein Hinweis im Forum dort. Aber was passt zum eigenen Gerät? Und was wurde tatsächlich überprüft?
Geplantes Nutzungsszenario, keine Produktoberfläche.
Das Problem
Informationen gibt es viele.
Der Zusammenhang fehlt oft.
Bei einer Reparatur verteilt sich das Wissen auf Schaltpläne, Datenblätter, Foren und persönliche Erfahrung. Das passende Material zu finden kostet Zeit. Auch der Zugang zum Gerät und die Suche nach Ersatzteilen können aufhalten.
RepairProbe soll diese Informationen mit dem konkreten Gerät und dem bisherigen Reparaturverlauf verbinden. Die reparierende Person soll nachvollziehen können, woher eine Aussage kommt und wie sicher sie ist.
So könnte es künftig funktionieren
Ein Radio geht nicht mehr an. Was nun?
Geplant
Dieses Beispiel erklärt den vorgesehenen Ablauf. Es zeigt keine bereits verfügbare App und ist keine Reparaturanleitung. RepairProbe soll weder selbstständig eine Diagnose bestätigen noch ein Gerät reparieren.
Geöffnete Netzgeräte, Lithium-Akkupacks und spannungsführende Schaltungen sind keine Einsteigerfälle. Die geplante Assistenz ersetzt keine Fachkenntnis und keine Sicherheitsfreigabe.
01
Gerät und Problem erfassen
Die Person hält das Modell, ein Foto und das Fehlerbild fest: Das Radio reagiert beim Einschalten nicht.
02
Passende Informationen finden
RepairProbe soll bei der Einordnung gerätespezifischer Quellen helfen. Woher ein Hinweis stammt und ob er zum Gerät passt, bleibt sichtbar.
03
Beobachtung und Messung trennen
„Keine Anzeige“ ist eine Beobachtung. Ein mit einem vorhandenen Messgerät erfasster Wert ist eine Messung. Ein Foto ersetzt sie nicht.
04
Vermutungen sichtbar lassen
Ein möglicher Fehler bleibt eine Vermutung, bis eine passende Prüfung ihn stützt oder widerlegt. Fehlende Informationen werden benannt.
05
Den nächsten Prüfschritt verstehen
Der Prototyp soll erklären, warum ein Schritt sinnvoll ist und welche Voraussetzungen gelten. Bei gefährlichen oder unbekannten Energiezuständen soll er stoppen.
06
Den Verlauf nachvollziehen
Neue Ergebnisse sollen in einem lokalen Reparaturfall erhalten bleiben. Die Person entscheidet über eine spätere Weitergabe.
Das Produktprinzip
Eine plausible Antwort
ist noch kein Messwert.
Eine KI kann Hinweise einordnen und Erklärungen formulieren. RepairProbe soll dabei jede Aussage mit ihrer Herkunft verbinden. Beobachtungen, echte Messwerte, Quellen und Vermutungen bleiben unterscheidbar.
Anders als ein ChatGPT-Gespräch oder eine Anleitung soll der geplante Reparaturfall diese Unterschiede auch nach dem Speichern und Weitergeben erhalten. Ob das im Alltag hilft, muss erst geprüft werden.
Die fünf Informationsarten verstehen →
Beobachtet
 Das Radio zeigt keine Reaktion.
Nachgeschlagen
 Ein Hinweis aus einer passenden Unterlage.
Vermutet
 Eine mögliche Ursache, noch ungeprüft.
Eine Vermutung wird durch Wiederholung nicht zur Messung.
Ehrlicher Projektstand
Was da ist. Was entstehen soll.
Die technische Basis →
Vorhanden
Eine kleine technische Software-Basis
Sie prüft und speichert Messereignisse und kann vorbereitete Abläufe reproduzieren. Automatisierte Tests prüfen dieses Softwareverhalten. Eine nutzbare Diagnose-App ist das noch nicht.
Geplant
Ein nutzbarer, offener Prototyp
Fotos und Beobachtungen erfassen, Quellen und Messwerte einordnen, einen Reparaturverlauf erhalten und Prüfschritte verständlich erklären. Dafür sind 850 Arbeitsstunden über sechs Monate vorgesehen.
Später möglich
Mehr Geräte und gemeinsames Weiterentwickeln
Ein offenes Austauschformat soll weitere Werkzeuge und Beiträge ermöglichen. Ein öffentlicher Community-Dienst gehört nicht zum geplanten Kernumfang.
Förderbewerbung in Vorbereitung.
RepairProbe bereitet eine Bewerbung beim Prototype Fund vor. Sie ist noch nicht eingereicht; eine Förderung ist nicht bewilligt.
Den Sechsmonatsplan lesen →
Forschung &amp; Open Source
Die Idee muss sich
in der Praxis bewähren.
Eine erste explorative Rückmeldung aus der Reparaturpraxis liegt vor: ein beantworteter Fragebogen, also n=1. Genannt wurden vor allem Informationssuche, Ersatzteile und mechanischer Zugang als Zeitkosten. Unklarheit über den nächsten Test und verlorener Kontext wurden dagegen als selten berichtet.
Das ist keine repräsentative Untersuchung und kein Wirksamkeitsnachweis. Weitere Gespräche und sichere Falltests sollen prüfen, wo die Software tatsächlich hilft. Bessere Reparaturergebnisse oder eine Umweltwirkung sind bisher nicht nachgewiesen.
Das Produktrepository ist derzeit privat. Die geplanten geförderten Ergebnisse sollen als freie, quelloffene Software veröffentlicht werden. Eine verpflichtende RepairProbe-Cloud oder eigene Messhardware ist nicht vorgesehen.
Hinter dem Projekt
Aus Interesse am Reparieren.
RepairProbe ist ein unabhängiges Projekt von Raik Müller. Sein praktischer Hintergrund verbindet CNC, Elektronik, Reparaturen, Automatisierung und Softwareentwicklung.
Rückmeldungen aus Repair-Cafés, offenen Werkstätten und der eigenen Reparaturpraxis sind willkommen. Auch Fragen zum Vorhaben helfen weiter.
Eine E-Mail schreiben ↗
RepairProbe auf GitHub ↗
repairprobe@gmail.com


## evidenzmodell.html

Titel: Was wissen wir wirklich? | RepairProbe
Beschreibung: Wie RepairProbe Beobachtungen, Messungen, Quellen, Vermutungen und Bestätigungen nachvollziehbar trennen soll.

Prinzip &amp; Evidenzmodell
Was wissen wir wirklich?
Bei einer Reparatur zählt nicht nur die Aussage. Es zählt auch, wie sie zustande gekommen ist. RepairProbe soll diese Herkunft bei jeder Information sichtbar halten.
Architekturprinzip festgelegt · Vollständiger Ausbau geplant
Fünf Arten von Information.
OBSERVED
Beobachtet
Was eine Person unmittelbar sieht oder feststellt. Im geplanten Radio-Beispiel: Beim Einschalten bleibt die Anzeige dunkel. Das sagt noch nichts über die Ursache aus.
MEASURED
Gemessen
Ein Wert, der tatsächlich mit einem Messgerät erfasst wurde. Gerät, Messbedingungen und Herkunft gehören dazu. Eine KI darf einen fehlenden Wert weder erfinden noch aus einem Foto als Messung ableiten.
RETRIEVED
Nachgeschlagen
Eine Information aus einer Quelle, etwa einem Datenblatt oder einer Serviceunterlage. Sie braucht einen Herkunftsnachweis und muss zum jeweiligen Gerät passen.
INFERRED
Vermutet
Eine Schlussfolgerung aus den bisherigen Informationen. Auch ein überzeugender KI-Hinweis bleibt eine Vermutung. Die Grundlage und offene Fragen sollen erkennbar sein.
CONFIRMED
Bestätigt
Eine Aussage, die durch eine geeignete Gegenprobe, Bauteilprüfung oder ein nachvollziehbares Reparaturergebnis bestätigt wurde. Die Bestätigung braucht selbst einen Beleg.
Die feste Grenze
Eine Einordnung
ersetzt keine Messung.
Ein Foto kann sichtbare Schäden oder eine Bauteilbezeichnung zeigen. Elektrische Eigenschaften wie Kapazität, Widerstand oder Spannung lassen sich daraus nicht als echte Messwerte gewinnen.
Unsicherheit gehört zum Ergebnis.
Fehlt ein Messgerät, soll die Software bei Beobachtung, Recherche und begründeten Vermutungen bleiben. Eine Lücke wird benannt und nicht mit einem erfundenen Ergebnis gefüllt.
Sicherheitsgrenzen
Erst verstehen.
Dann prüfen.
Der geplante Prototyp soll erklären, was bekannt ist, welche Frage ein Prüfschritt klärt und welche Voraussetzungen dafür nötig sind. Die Person bleibt verantwortlich für das reale Gerät und ihre Handlungen.
Feste Sicherheitsregeln sollen außerhalb des austauschbaren KI-Modells liegen. Gefährliche oder unbekannte Energiezustände müssen einen Schritt blockieren können. Die vorhandene passive Sicherheits-Baseline belegt noch keine Sicherheit eines vollständigen Reparaturablaufs.
Was die vorhandenen Tests tatsächlich belegen →


## roadmap.html

Titel: Der Weg zum ersten Prototyp. | RepairProbe
Beschreibung: RepairProbe plant 850 Arbeitsstunden über sechs Monate. Der Fahrplan trennt vorhandene Basis, beantragte Entwicklung und spätere Möglichkeiten.

Projektstand &amp; Fahrplan
Der Weg zum ersten Prototyp.
Aus einer kleinen technischen Basis soll eine nutzbare Reparaturassistenz werden. Die Planung umfasst 850 Arbeitsstunden einer Person über sechs Monate.
Bewerbung beim Prototype Fund in Vorbereitung · Noch nicht eingereicht · Nicht bewilligt
Heute
Der Anfang ist technisch.
Der nächste Schritt wird praktisch.
Vorhanden sind ein Format für Messereignisse, Prüfregeln, ein Testadapter, ein anfügbarer Evidenzspeicher, reproduzierbare Testabläufe und eine passive Sicherheits-Baseline. Die Tests prüfen diese Bausteine ohne echte Hardware oder KI-Modell.
Die Smartphone-Erfassung, ein dauerhaft gespeicherter Reparaturfall und die geführte Diagnose sind noch nicht gebaut.
Die vorhandene Basis im Detail →
Während einer möglichen Förderung geplant
Sechs Monate mit klaren Grenzen.
Monat 1
Den Reparaturfall definieren
Informationsarten, Herkunft, Unsicherheit und zulässige Zustandswechsel festlegen. Tests sollen unzulässige Übergänge ablehnen.
Monat 2
Fotos und Beobachtungen aufnehmen
Eine Smartphone-Erfassung entwickeln, die Gerät und Fehlerbild dokumentiert. Fotos werden als Beobachtung eingeordnet, nicht als elektrische Messung.
Monat 3
Prüfschritte verständlich machen
Den Ablauf an vorhandene Werkzeuge anpassen. Feste Sicherheitsregeln prüfen Schritte unabhängig vom KI-Modell.
Monat 4
Quellen nachvollziehbar einbinden
Einen begrenzten Testpfad für gerätespezifische Quellen bauen. Herkunft und Unsicherheit sollen sichtbar bleiben. Eine globale Reparaturdatenbank ist nicht vorgesehen.
Monat 5
Fälle lokal erhalten und austauschen
Einen lokalen Speicher und ein offenes Import- und Exportformat umsetzen. Ein dokumentiertes Beispiel soll die Anschlussfähigkeit des Formats prüfen.
Monat 6
Erproben und offen veröffentlichen
Mit sicheren Fällen und freiwilligem Feedback prüfen, was funktioniert. Den Prototyp mit reproduzierbaren Tests und Dokumentation als freie Software veröffentlichen.
Was geprüft werden muss
Nutzen ist eine Frage.
Kein fertiges Ergebnis.
Die geplante Erprobung soll den Prototyp mit einem allgemeinen multimodalen KI-Chat vergleichen: Bleiben Quellen, Unsicherheit und Fallverlauf nachvollziehbar? Werden Gegenproben und Sicherheitsgrenzen eingehalten?
Bewusst begrenzter Umfang
Kein eigenes KI-Modell, keine neue Messhardware und keine verpflichtende RepairProbe-Cloud. Der Prototyp soll die vorhandenen Mittel der reparierenden Person nutzen.
Ein öffentlicher Community-Dienst und breite Geräteunterstützung sind mögliche spätere Schritte.
Danach möglich
Erproben, erklären,
Weiterentwicklung ermöglichen.
Eine zusätzliche Second Stage ist in der Bewerbung vorgesehen. Eine spätere Auswahl und Bewilligung sind offen. Geplant sind Aufgabenprüfungen mit Freiwilligen, verständliche Einstiege, dokumentierte Austauschformate und ein realistischer Wartungsweg.
Diese Phase soll Nutzung und Nachhaltigkeit vorbereiten. Zusätzliche Kernfunktionen sind dafür nicht eingeplant. Es gibt keine behaupteten Pilotpartnerschaften.
Zum Projekt Kontakt aufnehmen →


## technical-baseline.html

Titel: Was heute tatsächlich funktioniert. | RepairProbe
Beschreibung: Die kleine RepairProbe-Software-Baseline prüft Messereignisse und reproduziert Testabläufe. Sie belegt keine KI-Diagnosequalität oder Reparaturwirkung.

Technische Basis
Was heute tatsächlich funktioniert.
RepairProbe hat eine kleine Software-Baseline. Sie prüft, wie Messereignisse verarbeitet und nachvollziehbar gespeichert werden. Eine fertige Reparaturassistenz ist daraus noch nicht entstanden.
Vor einer möglichen Förderung vorhanden · Produktrepository derzeit privat
Die vorhandenen Bausteine.
Format
Repair Measurement Event v1
Ein festgelegtes Format beschreibt Messereignisse und ihre Herkunft. Ein Validator lehnt ungültige Ereignisse ab, statt fehlende Angaben stillschweigend zu ergänzen.
Speicher
Anfügbarer Evidenzspeicher
Akzeptierte Ereignisse werden angefügt. Der Verlauf soll überprüfbar bleiben, anstatt frühere Einträge unbemerkt zu ersetzen.
Testdaten
Mock-Adapter und reproduzierbares Replay
Ein Testadapter liefert vorbereitete Ereignisse. Dieselben Testdaten können erneut abgespielt werden. Dafür sind weder echte Hardware noch Cloudzugang oder ein KI-Modell nötig.
Sicherheit
Passive SafetyGate-Baseline
Ein kleiner Satz fester Regeln begrenzt erlaubtes Softwareverhalten. Das ist ein Ausgangspunkt für spätere Sicherheitsprüfungen, keine Freigabe für Arbeiten an elektrischen Geräten.
Aussagekraft der Tests
44 Softwaretests.
Eine begrenzte Aussage.
Die aktuelle Testsuite umfasst 44 bestandene Tests. Sie prüft die Softwarebausteine, ungültige Eingaben und die Repository-Verträge. Drei erfundene Beispiele zeigen, dass Messereignisse bei Speicherung, Wiederholung und erneutem Einlesen erhalten bleiben. Fehlende Werte bleiben als fehlend erkennbar. Beobachtungen, Quellen und Vermutungen sind dabei getrennte Testkarten, noch kein vollständiger Reparaturfall. Die Software erkennt inhaltliche Quellenwidersprüche noch nicht selbst. Die Tests belegen weder reale Messgenauigkeit noch KI-Diagnosequalität oder Reparaturerfolg.
Noch nicht vorhanden
Smartphone-Erfassung, dauerhaft gespeicherte Reparaturfälle, geführte Diagnose, eine ausgebaute Quellenanbindung und ein offenes Austauschpaket gehören zur geplanten Entwicklung.
Den geplanten Umfang ansehen →
Architektur &amp; Offenheit
Am Gerät orientiert.
Mit nachvollziehbaren Grenzen.
Die geplante Architektur führt Fotos, Nutzerbeobachtungen, optionale reale Messwerte und recherchierte Quellen in einem lokalen Reparaturfall zusammen. Eine austauschbare KI soll Einordnungen und Erklärungen liefern. Feste Sicherheitsregeln liegen außerhalb des Modells.
Der Kern soll ohne verpflichtenden RepairProbe-Cloud-Dienst und ohne eigene RepairProbe-Messhardware nutzbar werden. Für die spätere Anbindung externer KI-Dienste sind Datenfluss und Voraussetzungen gesondert zu klären.
Das Produktrepository ist derzeit privat. Geplante geförderte Ergebnisse sollen unter einer freien Open-Source-Lizenz öffentlich werden. Die öffentliche Website und das Organisationsprofil sind bereits zugänglich.
Öffentliche Projektorganisation auf GitHub ↗


## 404.html

Titel: Diese Seite ist nicht da. | RepairProbe
Beschreibung: Die gesuchte Seite wurde nicht gefunden. Zurück zur RepairProbe-Startseite oder zum Projektfahrplan.

Fehler 404
Diese Seite ist nicht da.
Vielleicht hat sich die Adresse geändert. Auf der Startseite geht es weiter.
Zur Startseite →
Zum Projektfahrplan →

## Kompatible Abschnittsanker

Bestehende Deep-Links bleiben gültig. Aliasanker verweisen auf den semantisch passenden neuen Abschnitt; sie führen keine alten Inhalte wieder ein. Frühere Fragen zum Reifegrad führen auf den Projektstand.

- `index.html#hero-title` → `h1`
- `index.html#problem-title` → `#problem h2`
- `index.html#ansatz` → `.principle`
- `index.html#ansatz-title` → `.principle h2`
- `index.html#fall` → `#beispiel`
- `index.html#fall-title` → `#beispiel h2`
- `index.html#stand-title` → `#stand h2`
- `index.html#person` → `#kontakt`
- `index.html#person-title` → `#kontakt h2`
- `index.html#fragen` → `#stand`
- `index.html#fragen-title` → `#stand h2`
- `index.html#kontakt-title` → `#kontakt h2`
- `roadmap.html#hero-title` → `h1`
- `roadmap.html#heute-title` → `#heute h2`
- `roadmap.html#antrag` → `.page-hero .status-line`
- `roadmap.html#antrag-title` → `.page-hero .status-line`
- `roadmap.html#foerderphase` → `#foerderung`
- `roadmap.html#foerderphase-title` → `#foerderung h2`
- `roadmap.html#second-stage` → `#spaeter`
- `roadmap.html#second-stage-title` → `#spaeter h2`
- `roadmap.html#grenzen` → `.principle`
- `roadmap.html#grenzen-title` → `.principle h3`
- `technical-baseline.html#hero-title` → `h1`
- `technical-baseline.html#vorhanden` → `.status-list`
- `technical-baseline.html#vorhanden-title` → `.section h2`
- `technical-baseline.html#grenzen` → `.principle`
- `technical-baseline.html#grenzen-title` → `.principle h2`
- `technical-baseline.html#foerderung` → `.principle>div:nth-of-type(2)`
- `technical-baseline.html#foerderung-title` → `.principle h3`
- `technical-baseline.html#pruefung` → `.principle`
- `technical-baseline.html#pruefung-title` → `.principle h2`
- `technical-baseline.html#oekosystem` → `.split`
- `technical-baseline.html#oekosystem-title` → `.split h2`
- `evidenzmodell.html#hero-title` → `h1`
- `evidenzmodell.html#klassen-title` → `#klassen h2`
- `evidenzmodell.html#grenze-title` → `#grenze h2`
- `evidenzmodell.html#unsicherheit` → `#grenze>div:nth-of-type(2)`
- `evidenzmodell.html#unsicherheit-title` → `#grenze h3`
- `evidenzmodell.html#sicherheit-title` → `#sicherheit h2`
- `evidenzmodell.html#ausblick` → `#sicherheit .prose`
- `evidenzmodell.html#ausblick-title` → `#sicherheit .prose`
- `404.html#hero-title` → `h1`
