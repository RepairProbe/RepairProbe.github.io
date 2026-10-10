# Wettbewerber- und Einordnungsanalyse (Phase 2C)

Grundlage: kanonische Analyse `repair-probe/docs/funding/prior-art-and-ecosystem.md` (geprüft 2026-09-02, Architektur-Update 2026-10-01) und `competitive-landscape-note.md`. Diese Seite positioniert die Öffentlichkeitsarbeit, sie erfindet keine Marktanalyse neu.

## Wer ist in derselben Welt unterwegs

| System | Was es ist | Verhältnis zu RepairProbe |
|---|---|---|
| iFixit | Reparaturanleitungen, Teile, Community | Ergänzung; Anleitungen sind kein Evidenz-/Sicherheitsvertrag für eine laufende Reparatursitzung. Verlinken, nicht nachbauen. |
| Open Repair Alliance / ORDS | offener Standard für Reparatur-Ereignisdaten | Ergänzung; kein elektrisches Messereignis, kein Safety-Kontrakt. Erwähnung als Belegquelle (ORA-Report 2024). |
| sigrok/libsigrok, SCPI, OpenTAP | Messhardware-Zugriff, Instrumentensteuerung, Testautomatisierung | Optionale Integrationspfade, keine Konkurrenz. Nicht nachbauen. |
| Wrench Board, BoardFix, BoardScope | Brett-diagnose-Arbeitsumgebungen mit KI-Agent, Messprotokoll, Boardview | Aktive Produktkategorie; beweist Nachfrage. Unterschied: RepairProbe bleibt offen, instrumentenneutral und setzt Safety/Provenienz außerhalb des Modells als FOSS-Schicht. |
| re:trace | PCB-Reverse-Engineering-Toolkit | Nachbarwerkzeug, kein Leistungsversprechen von RepairProbe. |

## Gemeinsamkeiten der starken Anbieterseiten (für Erwartungshaltung)

- Sie benennen konkret, was das Werkzeug tut (nicht „Revolution“).
- Ablauf in klar nummerierten Schritten sichtbar.
- Vertrauen über konkrete Belege (Dokumentation, Quellen, Offenlegung) statt Aussagen.
- KI wird begrenzt und explained beschrieben, nicht mystifiziert.

## Lücke, die RepairProbe öffentlich sauber besetzen kann

Kein-reviewed Projekt der Landschaft demonstriert dieselbe **kombinierte** Offenheit: normiertes Reparatur-Messereignis + Herkunft (Provenienz) + deterministische, modellunabhängige Safety-Grenze + getypte Erklärungs-Verträge als FOSS. Diese Kombination ist eine **zu prüfende Hypothese**, kein behaupteter Neuheitsbeweis. Öffentlich wichtig: Der breite Gedanke „KI führt durch Elektronik-Fehlersuche“ ist nachweislich nicht neu (Historie bis US4709366A); RepairProbe behauptet das auch nicht.

## Übertragung in die Texte (Phase 3)

1. Keine Überlegenheitsbehauptung gegenüber KI-Chat.
2. „Was anders ist“ als Schicht-Beschreibung (Evidenz/Herkunft/Sicherheit offen), nicht als Produkt-Hype.
3. Ökosystem ehrlich nennen (Ergänzung statt Ersatz) — das ist ein Vertrauenssignal für Fachpublikum und Förderer.
4. Kein Framework-/Fairphone-ähnlicher Markenton (die sind Produktmarken); nüchtern-protokollarischer Ton passt zur Infrastruktur-Ehrlichkeit.
