# Gezielte Aktualisierung des technischen Nachweises

28.10.2026. Quelle: kanonisches Produkt-main nach geprüftem PR #28, Commit `b0a85abcf8eb352ce2365125aba022fbef741437`. Tatsächlich ausgeführt: 24 Tests; drei synthetische Messereignis-Roundtrips. Kein echter KI-Vergleich, keine Nutzerprüfung, keine fertige App. Keine privaten Quelldateien oder Forschungsdaten veröffentlicht.

Nur Teststand und verständliche Grenzen aktualisiert: zuerst texte.md, dann Startseite, Roadmap, technische Basis und llms.txt. Keine Design-, Farb-, Navigations- oder Ressourcenänderung. Schreibregeln geprüft; keine Erfolgs-/Förderbehauptung hinzugefügt. Die vorhandene Darstellung von n=1, Privatstatus und geplanter Förderung bleibt zutreffend. Organisationsprofil enthält keine veraltete Testzahl und braucht keine Änderung.

## Lokale Prüfung

- Gebündelter Skill-Prüflauf auf localhost:8111 ohne gemeldete Probleme.
- Alle fünf HTML-Seiten bei 320, 390, 820, 1366 und 1440 px gerendert; 25 Screenshots unter `/tmp/repairprobe-evidence-qa/` zur visuellen Abnahme.
- Kein horizontaler Überlauf, je ein H1, keine Überschriftensprünge, keine fehlenden Alt-Attribute oder Konsolenfehler.
- Zehn Tab-Schritte je Seite bei 390 px: Links mit sichtbarer Fokuslinie.
- Elf interne Link-/Ankerziele geprüft: `INTERNAL_BROKEN_LINKS=0`.
- Alle Requests ausschließlich localhost:8111; keine Cookies, localStorage oder sessionStorage.
- Farben und styles.css unverändert; die im bisherigen Abnahmebericht gemessenen Textkontraste ab 5,45:1 bleiben anwendbar.
- Ein Fehler im einmaligen Linkprüfskript (Navigation innerhalb derselben Seite liefert keine Response) wurde im Prüflauf korrigiert; anschließend alle elf Ziele über HTTP plus Anker geprüft. Kein Websitefehler.

Unabhängige visuelle Abnahme und Remote-/Live-Nachweis werden nach dem jeweiligen Schritt ergänzt. Kein öffentlicher Codeexport, keine erneute Neugestaltung.

## Unabhängige Abnahme

Die separate Reviewinstanz hat alle 15 Screenshots der drei geänderten Seiten bei fünf Viewports tatsächlich angesehen und Texte gegen texte.md sowie die unabhängig geprüften Produktbelege verglichen. Keine Überlagerung oder abgeschnittenen Inhalte, auch der lange Absatz auf 320/390 px bleibt vollständig in der vorgesehenen Fläche. Keine P1/P2-Befunde; visuelle und inhaltliche Freigabe erteilt.
