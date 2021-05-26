


  
********  
Repository: [verona-data-specifications](https://github.com/iqb-berlin/verona-data-specifications)  
Description: This repo contains of all iqb data specifications related to verona-interfaces.  
********  
********  
Repository: [verona-editor-aspect](https://github.com/iqb-berlin/verona-editor-aspect) Release: [0.0.1](https://github.com/iqb-berlin/verona-editor-aspect/releases/tag/0.0.1)  
*There is no description for this repository*  
********  
********  
Repository: [verona-editor-dan](https://github.com/iqb-berlin/verona-editor-dan) Release: [v3.1.0](https://github.com/iqb-berlin/verona-editor-dan/releases/tag/v3.1.0)  
*There is no description for this repository*  
**JSON LD from HTML file**  
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
********  
********  
Repository: [verona-editor-plaintext](https://github.com/iqb-berlin/verona-editor-plaintext) Release: [v1.0.1](https://github.com/iqb-berlin/verona-editor-plaintext/releases/tag/v1.0.1)  
Description: Provides one big text input element to edit script based unit definitions or to hack others.  
**JSON LD from HTML file**  
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
********  
********  
Repository: [verona-player-abi](https://github.com/iqb-berlin/verona-player-abi) Release: [v3.3.2](https://github.com/iqb-berlin/verona-player-abi/releases/tag/v3.3.2)  
Description: A programmable item-player for surveys. Contains: Player-Plugin, Editor-Plugin   
**JSON LD from HTML file**  
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
********  
********  
Repository: [verona-player-dan](https://github.com/iqb-berlin/verona-player-dan) Release: [v3.0.0](https://github.com/iqb-berlin/verona-player-dan/releases/tag/v3.0.0)  
Description: The current default IQB Item for computer based accessment: The Dan-Player. Contains: Player-Plugin, Editor-Plugin  
**JSON LD from HTML file**  
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
********  
********  
Repository: [verona-player-simple](https://github.com/iqb-berlin/verona-player-simple) Release: [1.1.0](https://github.com/iqb-berlin/verona-player-simple/releases/tag/1.1.0)  
Description: A dependency-free, vanilla-js Verona2-Player which can run HTML-forms as Units  
********  
********  
Repository: [verona-player-testbed](https://github.com/iqb-berlin/verona-player-testbed) Release: [1.0.1](https://github.com/iqb-berlin/verona-player-testbed/releases/tag/1.0.1)  
Description: web application to test offline player and unit definition  
********  
********  
Repository: [verona-registry](https://github.com/iqb-berlin/verona-registry)  
Description: This registry helps applications for online assessment to find players, editors and other verona-interfaces related modules.  
********