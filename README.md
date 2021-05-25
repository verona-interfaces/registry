


  
verona-editor-dan  
``` json  
{
    "@context": "https://w3id.org/iqb/verona-modules",
    "@type": "editor",
    "@id": "iqb-editor-dan",
    "name": {
        "de": "IQB-Editor für komplexe Testaufgaben (Dan)",
        "en": "IQB editor for complex test units (Dan)"
    },
    "maintainer": {
        "name": {
            "de": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen",
            "en": "IQB - Institute for Educational Quality Improvement"
        },
        "url": "https://www.iqb.hu-berlin.de",
        "email": "iqb-tbadev@hu-berlin.de"
    },
    "description": {
        "de": "Dieser Editor verarbeitet Aufgabendefinitionen in einem eigenen, undokumentierten Format. Anzeige- und Interaktionselemente können frei positioniert werden auf einer oder über mehreren Seiten.",
        "en": "This Verona Editor uses a specific undocumented unit definition format. You can place elements for display or interaction purposes freely on one or more pages."
    },
    "version": "3.1.0",
    "apiVersion": "2.0",
    "repository": {
        "type": "git",
        "url": "https://github.com/iqb-berlin/verona-editor-plaintext"
    },
    "notSupportedFeatures": [
        "report-eager"
    ]
}  
```  
verona-editor-plaintext  
``` json  
{
    "@context": "https://w3id.org/iqb/verona-modules",
    "@type": "editor",
    "@id": "iqb-editor-plaintext",
    "name": {
        "de": "IQB-Editor für Text",
        "en": "IQB editor for plain text"
    },
    "maintainer": {
        "name": {
            "de": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen",
            "en": "IQB - Institute for Educational Quality Improvement"
        },
        "url": "https://www.iqb.hu-berlin.de",
        "email": "iqb-tbadev@hu-berlin.de"
    },
    "description": {
        "de": "Dieser Editor verarbeitet Aufgaben-/Seitendefinitionen als Text. Dies ist sinnvoll z. B. für Xml-, Html- oder scriptbasierte Formate, für die kein separater Editor bereitgestellt wird.\n\nAchtung: Für binäre oder JSON-Formate sollten andere Editoren genutzt werden, die die Konsistenz der Daten sicherstellen. Eine Bearbeitung dieser Formate mit diesem Text-Editor kann die Aufgaben-/Seitendefinitionen unbrauchbar machen.",
        "en": "You can use this Verona Editor for all unit definitions, because the data format of unit definitions is technically always string/text. But be careful: improper changes may damage the definition so it's not usable anymore."
    },
    "version": "1.0.1",
    "apiVersion": "2.0",
    "repository": {
        "type": "git",
        "url": "https://github.com/iqb-berlin/verona-editor-plaintext"
    },
    "notSupportedFeatures": [
        "report-eager"
    ]
}  
```  
verona-player-abi  
``` json  
{
    "@context": "https://w3id.org/iqb/verona-modules",
    "@type": "player",
    "@id": "iqb-player-abi",
    "name": {
        "de": "IQB-Player für Skripte (Abi)",
        "en": "IQB player for script language"
    },
    "maintainer": {
        "name": {
            "de": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen",
            "en": "IQB - Institute for Educational Quality Improvement"
        },
        "url": "https://www.iqb.hu-berlin.de",
        "email": "iqb-tbadev@hu-berlin.de"
    },
    "description": {
        "de": "Dieser Player interpretiert eine Script-Sprache, die speziell für die effiziente Erstellung umfangreicher Befragungen entwickelt wurde. Über die gängigen Frageformate hinaus werden bedingte Formularblöcke, dynamische Wiederholungen von Blöcken und Likert-skalen unterstützt.",
        "en": "You can use this Verona Player for surveys where you need a large number of questions. By interpreting it's own script language, the player just need one line per control definition. You can setup conditional blocks, repeating blocks or likert scale tables."
    },
    "version": "3.3.2",
    "apiVersion": "2.1",
    "repository": {
        "type": "git",
        "url": "https://github.com/iqb-berlin/verona-player-abi"
    },
    "notSupportedFeatures": []
}  
```  
verona-player-dan  
``` json  
{
    "@context": "https://w3id.org/iqb/verona-modules",
    "@type": "player",
    "@id": "iqb-player-dan",
    "name": {
        "de": "IQB-Player für komplexe Testaufgaben (Dan)",
        "en": "IQB player for complex assessment units"
    },
    "maintainer": {
        "name": {
            "de": "IQB - Institut zur Qualitätsentwicklung im Bildungswesen",
            "en": "IQB - Institute for Educational Quality Improvement"
        },
        "url": "https://www.iqb.hu-berlin.de",
        "email": "iqb-tbadev@hu-berlin.de"
    },
    "description": {
        "de": "Dieser Player interpretiert Aufgabendefinitionen in einem eigenen, undokumentierten Format. Anzeige- und Interaktionselemente können frei positioniert werden auf einer oder über mehreren Seiten.",
        "en": "This Verona Player uses a specific undocumented unit definition format. You can place elements for display or interaction purposes freely on one or more pages."
    },
    "version": "3.0.0",
    "apiVersion": "2.1",
    "repository": {
        "type": "git",
        "url": "https://github.com/iqb-berlin/verona-player-abi"
    },
    "notSupportedFeatures": []
}  
```