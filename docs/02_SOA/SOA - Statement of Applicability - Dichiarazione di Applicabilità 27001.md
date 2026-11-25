<!-- File GENERATO da tools/genera_soa.py: non modificarlo a mano. Le modifiche vanno nella sorgente tools/soa/SOA-sorgente.md -->

# SOA - Statement of Applicability - Dichiarazione di Applicabilità 27001

## Cover

| Rev. | Data | Descrizione | Redatto | Approvato | Classificazione |
|---|---|---|---|---|---|
| 0.0 | 25/11/2026 | Emissione | RSGI | Da approvare | Interno |

| | |
|---|---|
| Data ultima versione | 25/11/2026 |
| Versione | 0.0 |
| Set di Controlli inclusi | • ISO/IEC 27002 • GDPR |
| Controlli Non Applicabili | 7.12, 8.11, 8.30 |
| Acronimi Controllo | ID X.X: ISO/IEC 27002 |
| Numero controlli | 93 |

## Riepilogo

**93 controlli**: 90 applicabili, di cui 51 attuati e 39 non ancora attuati; 3 non applicabili.

Motivo di inclusione: **L** = Requisito legale · **C** = Obbligo contrattuale · **B** = Requisito business / best practice · **R** = Risultato analisi dei rischi.
Clic sull'ID per aprire il dettaglio del controllo.

### 5. Controlli organizzativi (Organizational controls)

| ID | Controllo | Applicabile | Attuato | Motivo | Riferimenti |
|---|---|---|---|---|---|
| [5.1](#c-5-1) | Politiche per la sicurezza delle informazioni | Sì | No | B R | [PO01](../../01_POLITICA%20SISTEMA%20INTEGRATO/PO01%20-%20Sistema%20Integrato-Rev%200.0/), [PO02](../../4_CONTESTO/PO02%20-%20Gestione%20del%20Contesto/), [MDPO03.A](../../6.2_OBIETTIVI/MDPO03.A%20-%20Lista%20Obiettivi/), [PO07](../../7.4_COMUNICAZIONI/PO07%20-%20Politica%20Gestione%20della%20Comunicazione/), [PO15](../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/), [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/), [PR21.1](../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore/), [PR23.1](../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche/), [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/), [PR26.1](../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/), [PR27.1](../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/), [PR28.1](../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/), [PO29](../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/), [PO31](../../A_CONFORMITA_/PO31%20-%20Misure%20di%20sicurezza%20protezione%20dati%20personali/) |
| [5.2](#c-5-2) | Ruoli e responsabilità per la sicurezza delle informazioni | Sì | Sì | L B R | [ALPO01.A](../../01_POLITICA%20SISTEMA%20INTEGRATO/ALPO01.A%20-%20Organigramma-Rev%200.0/), [ALPO01.B](../../01_POLITICA%20SISTEMA%20INTEGRATO/ALPO01.B%20-%20Mansionario-Rev%200.0/), [ALPO02.A](../../4_CONTESTO/ALPO02.A%20-%20Contesto%20e%20Processi/), [ALPO02.B](../../4_CONTESTO/ALPO02.B-%20Analisi%20Stakeholder/) |
| [5.3](#c-5-3) | Separazione dei compiti | Sì | No | B R | [ALPO01.A](../../01_POLITICA%20SISTEMA%20INTEGRATO/ALPO01.A%20-%20Organigramma-Rev%200.0/), [ALPO01.B](../../01_POLITICA%20SISTEMA%20INTEGRATO/ALPO01.B%20-%20Mansionario-Rev%200.0/) |
| [5.4](#c-5-4) | Responsabilità della direzione | Sì | Sì | B R | [PR05.1](../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [MDPR05.1.A](../../7_GESTIONE%20RISORSE/MDPR05.1.A%20-%20Checklist%20Documenti%20per%20Inserimento%20Personale/), [MDPR05.1.V](../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze/) |
| [5.5](#c-5-5) | Contatti con le autorità | Sì | Sì | L B | [MDPR08.1.A](../../7.5_INFORMAZIONI%20DOCUMENTATE/MDPR08.1.A%20-%20Elenco%20Informazioni%20documentate/), [PR27.1](../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/) |
| [5.6](#c-5-6) | Contatti con gruppi di interesse | Sì | No | B | [MDPR08.1.A](../../7.5_INFORMAZIONI%20DOCUMENTATE/MDPR08.1.A%20-%20Elenco%20Informazioni%20documentate/), [PR23.1](../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche/) |
| [5.7](#c-5-7) | Monitoraggio delle minacce | Sì | Sì | B | [PR23.1](../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche/), [MDPR23.1.B](../../A_MINACCE%20%26%20VULNERABILITA_/MDPR23.1.B%20-%20Monitoraggio%20delle%20minacce%202026/) |
| [5.8](#c-5-8) | Sicurezza delle informazioni nella gestione dei progetti | Sì | No | L B R |  |
| [5.9](#c-5-9) | Inventario delle informazioni e degli altri asset associati | Sì | Sì | L B R | [MDPR05.1.V](../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/), [PO15](../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/) |
| [5.10](#c-5-10) | Uso accettabile delle informazioni e degli altri asset associati | Sì | Sì | L B R | [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/) |
| [5.11](#c-5-11) | Restituzione degli asset | Sì | Sì | B R | [MDPR05.1.V](../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/) |
| [5.12](#c-5-12) | Classificazione delle informazioni | Sì | No | L B R | [PO15](../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/), [MDPR31.4.A](../../A_CONFORMITA_/MDPR31.4.A%20-%20Registro%20dei%20Trattamenti%20Titolare/), [MDPR31.4.B](../../A_CONFORMITA_/MDPR31.4.B%20-%20Registro%20dei%20Trattamenti%20Responsabile/) |
| [5.13](#c-5-13) | Etichettatura delle informazioni | Sì | No | L B R | [PO15](../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/), [MDPR31.4.A](../../A_CONFORMITA_/MDPR31.4.A%20-%20Registro%20dei%20Trattamenti%20Titolare/), [MDPR31.4.B](../../A_CONFORMITA_/MDPR31.4.B%20-%20Registro%20dei%20Trattamenti%20Responsabile/) |
| [5.14](#c-5-14) | Trasferimento delle informazioni | Sì | Sì | L C B R | [PO07](../../7.4_COMUNICAZIONI/PO07%20-%20Politica%20Gestione%20della%20Comunicazione/), [ALPR26.1.B.3](../../A_FORNITORI/ALPR26.1.B.3%20-%20Accordo%20di%20Riservatezza%20con%20le%20Terze%20Parti/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/) |
| [5.15](#c-5-15) | Controllo degli accessi | Sì | Sì | L B R | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [5.16](#c-5-16) | Gestione delle identità | Sì | Sì | L B R | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/) |
| [5.17](#c-5-17) | Informazioni di autenticazione | Sì | Sì | L B R | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/) |
| [5.18](#c-5-18) | Diritti di accesso | Sì | Sì | L B R | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/), [MDPR11.1.A](../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/) |
| [5.19](#c-5-19) | Sicurezza delle informazioni nelle relazioni con i fornitori | Sì | Sì | L B R | [PR26.1](../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/), [PR26.1](../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/), [MDPR26.1.B](../../A_FORNITORI/MDPR26.1.B%20-%20Elenco%20fornitori%20qualificati/), [ALPR26.1.A](../../A_FORNITORI/ALPR26.1.A%20-%20Comunicazione%20e%20requisiti%20di%20sicurezza%20per%20i%20fornitori/), [ALPR26.1.B.3](../../A_FORNITORI/ALPR26.1.B.3%20-%20Accordo%20di%20Riservatezza%20con%20le%20Terze%20Parti/), [ALPR26.1.C](../../A_FORNITORI/ALPR26.1.C%20-%20Contratto%20di%20fornitura/), [ALPR26.1.A](../../A_FORNITORI/ALPR26.1.A%20-%20Comunicazione%20e%20requisiti%20di%20sicurezza%20per%20i%20fornitori/) |
| [5.20](#c-5-20) | Sicurezza delle informazioni negli accordi con i fornitori | Sì | Sì | L C B R | [ALPR26.1.C](../../A_FORNITORI/ALPR26.1.C%20-%20Contratto%20di%20fornitura/), [ALPR26.1.D](../../A_FORNITORI/ALPR26.1.D%20-%20Nomina%20Responsabile%20Trattamenti%20Dati%20Personali/), [ALPR26.1.A](../../A_FORNITORI/ALPR26.1.A%20-%20Comunicazione%20e%20requisiti%20di%20sicurezza%20per%20i%20fornitori/) |
| [5.21](#c-5-21) | Sicurezza delle informazioni nella filiera di fornitura ICT | Sì | Sì | L C B R | [ALPR26.1.B.3](../../A_FORNITORI/ALPR26.1.B.3%20-%20Accordo%20di%20Riservatezza%20con%20le%20Terze%20Parti/), [ALPR26.1.C](../../A_FORNITORI/ALPR26.1.C%20-%20Contratto%20di%20fornitura/), [ALPR26.1.D](../../A_FORNITORI/ALPR26.1.D%20-%20Nomina%20Responsabile%20Trattamenti%20Dati%20Personali/), [ALPR26.1.A](../../A_FORNITORI/ALPR26.1.A%20-%20Comunicazione%20e%20requisiti%20di%20sicurezza%20per%20i%20fornitori/) |
| [5.22](#c-5-22) | Monitoraggio, riesame e gestione dei cambiamenti dei servizi dei fornitori | Sì | Sì | L C B R | [PR26.1](../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/), [PR26.1](../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/), [MDPR26.1.B](../../A_FORNITORI/MDPR26.1.B%20-%20Elenco%20fornitori%20qualificati/) |
| [5.23](#c-5-23) | Sicurezza delle informazioni per l’uso dei servizi cloud | Sì | Sì | B R | [PR26.1](../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/) |
| [5.24](#c-5-24) | Pianificazione e preparazione per la gestione degli incidenti relativi alla sicurezza delle informazioni | Sì | Sì | L B R | [PR27.1](../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/) |
| [5.25](#c-5-25) | Valutazione e decisione sugli eventi relativi alla sicurezza delle informazioni | Sì | Sì | L B R | [PR27.1](../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/) |
| [5.26](#c-5-26) | Risposta agli incidenti relativi alla sicurezza delle informazioni | Sì | Sì | L B R | [PR27.1](../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/), [ALPR27.1.A](../../A_EVENTI%20%26%20INCIDENTI/ALPR27.1.A%20-%20Notifica%20Data%20Breach%20all%E2%80%99interessato/) |
| [5.27](#c-5-27) | Apprendimento dagli incidenti relativi alla sicurezza delle informazioni | Sì | Sì | L B R | [PR27.1](../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/) |
| [5.28](#c-5-28) | Raccolta di prove | Sì | No | L B R | [PR27.1](../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/), [MDPR27.1.A](../../A_EVENTI%20%26%20INCIDENTI/MDPR27.1.A%20-%20Registro%20Data%20Breach/) |
| [5.29](#c-5-29) | Sicurezza delle informazioni durante le interruzioni | Sì | Sì | L B R | [PR28.1](../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/), [PR28.1](../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/), [MDPR28.1.A](../../A_CONTINUITA_%20OPERATIVA/MDPR28.1.A%20-%20BIA_Business%20Impact%20Analysis%20%2827001%29/), [MDPR21.1.A](../../A_BACKUP%20%26%20RESTORE/MDPR21.1.A%20-%20Piano%20di%20Restore/) |
| [5.30](#c-5-30) | Preparazione dell’ICT per la continuità operativa | Sì | Sì | B R | [PR21.1](../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore/), [PR28.1](../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/), [PR28.1](../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/), [MDPR28.1.A](../../A_CONTINUITA_%20OPERATIVA/MDPR28.1.A%20-%20BIA_Business%20Impact%20Analysis%20%2827001%29/), [MDPR21.1.A](../../A_BACKUP%20%26%20RESTORE/MDPR21.1.A%20-%20Piano%20di%20Restore/) |
| [5.31](#c-5-31) | Requisiti legali, statutari, regolamentari e contrattuali | Sì | Sì | L C B R | [MDPR08.1.A](../../7.5_INFORMAZIONI%20DOCUMENTATE/MDPR08.1.A%20-%20Elenco%20Informazioni%20documentate/), [PO29](../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/) |
| [5.32](#c-5-32) | Diritti di proprietà intellettuale | Sì | Sì | L C B R | [PO29](../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/) |
| [5.33](#c-5-33) | Protezione delle registrazioni | Sì | No | L B R | [MDPR08.1.A](../../7.5_INFORMAZIONI%20DOCUMENTATE/MDPR08.1.A%20-%20Elenco%20Informazioni%20documentate/), [PO29](../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/) |
| [5.34](#c-5-34) | Privacy e protezione dei dati personali | Sì | Sì | L C B R | [PO29](../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/), [MDPO29.A](../../A_CONFORMITA_/MDPO29.A%20-%20Elenco%20AdS/), [PO31](../../A_CONFORMITA_/PO31%20-%20Misure%20di%20sicurezza%20protezione%20dati%20personali/), [ALPO31.A](../../A_CONFORMITA_/ALPO31.A%20-%20Lettera%20incarico%20AdS/), [ALPO31.B](../../A_CONFORMITA_/ALPO31.B%20-%20Atto%20di%20Nomina%20ad%20Autorizzato%20del%20Trattamento/), [ALPO31.D](../../A_CONFORMITA_/ALPO31.D%20-%20Atto%20di%20Nomina%20a%20Referente%20Privacy/), [PR31.1](../../A_CONFORMITA_/PR31.1%20-%20Gestione%20dei%20Diritti%20degli%20Interessati/), [MDPR31.1.A](../../A_CONFORMITA_/MDPR31.1.A%20-%20Registro%20delle%20richieste/), [PR31.2](../../A_CONFORMITA_/PR31.2%20-%20Gestione%20dei%20Consensi/), [ALPR31.2.A](../../A_CONFORMITA_/ALPR31.2.A%20-%20Informativa%20Privacy%20Dipendenti/), [ALPR31.2.B](../../A_CONFORMITA_/ALPR31.2.B%20-%20Informativa%20Privacy%20Candidati/), [ALPR31.2.C](../../A_CONFORMITA_/ALPR31.2.C%20-%20Informativa%20Privacy%20Visitatori/), [ALPR31.2.D](../../A_CONFORMITA_/ALPR31.2.D%20-%20Informativa%20Privacy%20Fornitori/), [ALPR31.2.E](../../A_CONFORMITA_/ALPR31.2.E%20-%20Informativa%20Privacy%20Clienti/), [ALPR31.2.F](../../A_CONFORMITA_/ALPR31.2.F%20-%20Informativa%20Privacy%20Sito/), [ALPR31.2.G](../../A_CONFORMITA_/ALPR31.2.G%20-%20Liberatoria%20Foto-Video/), [PR31.3](../../A_CONFORMITA_/PR31.3%20-%20Procedura%20Valutazione%20d_impatto%20sulla%20protezione%20dei%20dati%20%28DPIA%29/), [PR31.4](../../A_CONFORMITA_/PR31.4%20-%20Gestione%20registro%20dei%20trattamenti/), [MDPR31.4.A](../../A_CONFORMITA_/MDPR31.4.A%20-%20Registro%20dei%20Trattamenti%20Titolare/), [MDPR31.4.B](../../A_CONFORMITA_/MDPR31.4.B%20-%20Registro%20dei%20Trattamenti%20Responsabile/) |
| [5.35](#c-5-35) | Riesame indipendente della sicurezza delle informazioni | Sì | No | L B R | [PR11.1](../../9.2_AUDIT%20INTERNO/PR11.1%20-%20Audit%20Interno/), [PO29](../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/) |
| [5.36](#c-5-36) | Conformità con le politiche, le regole e le norme di sicurezza delle informazioni | Sì | No | L B R | [PR11.1](../../9.2_AUDIT%20INTERNO/PR11.1%20-%20Audit%20Interno/), [MDPR11.1.A](../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/), [MDPR11.1.B](../../9.2_AUDIT%20INTERNO/MDPR11.1.B%20-%20Piano%20di%20Audit%20e%20Report/), [MDPR11.1.A](../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/), [PO29](../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/) |
| [5.37](#c-5-37) | Procedure operative documentate | Sì | No | L B R | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/), [PR05.1](../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/), [PR06.1](../../7_GESTIONE%20RISORSE/PR06.1%20-%20Gestione%20delle%20Performance/), [PR08.1](../../7.5_INFORMAZIONI%20DOCUMENTATE/PR08.1%20-%20Gestione%20Informazioni%20Documentate/), [PR09.1](../../8.2_PRODOTTI%20%26%20SERVIZI/PR09.1%20-%20Gestione%20Commerciale/), [MDPR10.1.A](../../9.1_MONITORAGGIO%20KPI/MDPR10.1.A%20-%20Tabella%20Indicatori/), [PR11.1](../../9.2_AUDIT%20INTERNO/PR11.1%20-%20Audit%20Interno/), [PR12.1](../../9.3_RIESAME%20DIREZIONE/PR12.1%20-%20Riesame%20della%20Direzione/), [PR13.1](../../10_GESTIONE%20NON%20CONFORMITA_%20E%20MIGLIORAMENTO/PR13.1%20-%20Gestione%20delle%20Non%20Conformit%C3%A0%20e%20Azioni%20di%20Miglioramento/), [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/), [PR19.1](../../A_CAMBIAMENTO/PR19.1%20-%20Gestione%20del%20Cambiamento/), [PR21.1](../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore/), [PR23.1](../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche/), [PR26.1](../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/), [PR27.1](../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/), [PR28.1](../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/), [PR31.1](../../A_CONFORMITA_/PR31.1%20-%20Gestione%20dei%20Diritti%20degli%20Interessati/), [PR31.2](../../A_CONFORMITA_/PR31.2%20-%20Gestione%20dei%20Consensi/), [PR31.3](../../A_CONFORMITA_/PR31.3%20-%20Procedura%20Valutazione%20d_impatto%20sulla%20protezione%20dei%20dati%20%28DPIA%29/), [PR31.4](../../A_CONFORMITA_/PR31.4%20-%20Gestione%20registro%20dei%20trattamenti/), [PR33.1](../../6.1_ANALISI%20DEI%20RISCHI/PR33.1%20-%20Processo%20Analisi%20del%20Rischio%20e%20Trattamento/), [PR33.2](../../6.1_ANALISI%20DEI%20RISCHI/PR33.2%20-%20Processo%20Analisi%20del%20Rischio%20Privacy/) |

### 6. Controlli relativi alle persone (People controls)

| ID | Controllo | Applicabile | Attuato | Motivo | Riferimenti |
|---|---|---|---|---|---|
| [6.1](#c-6-1) | Screening | Sì | No | L B R | [PR05.1](../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/), [MDPR06.1.E](../../7_GESTIONE%20RISORSE/MDPR06.1.E%20-%20Griglia%20delle%20competenze/) |
| [6.2](#c-6-2) | Termini e condizioni di impiego | Sì | Sì | L C B | [PR05.1](../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [MDPR05.1.A](../../7_GESTIONE%20RISORSE/MDPR05.1.A%20-%20Checklist%20Documenti%20per%20Inserimento%20Personale/) |
| [6.3](#c-6-3) | Consapevolezza, istruzione, formazione e addestramento sulla sicurezza delle informazioni | Sì | No | L C B R | [PR05.1](../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [MDPR06.1.C](../../7_GESTIONE%20RISORSE/MDPR06.1.C%20-%20Piano%20della%20formazione_%5Baaaa%5D/) |
| [6.4](#c-6-4) | Processo disciplinare | Sì | No | L C B R | [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [MDPR05.1.H](../../7_GESTIONE%20RISORSE/MDPR05.1.H%20-%20Processo%20Disciplinare/), [ALPR05.1.H](../../7_GESTIONE%20RISORSE/ALPR05.1.H%20-%20Documenti%20per%20il%20personale/) |
| [6.5](#c-6-5) | Responsabilità dopo la cessazione o variazione del rapporto di lavoro | Sì | Sì | C B | [PR05.1](../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [MDPR05.1.L](../../7_GESTIONE%20RISORSE/MDPR05.1.L%20-%20Checklist%20documenti%20per%20uscita%20personale/), [MDPR05.1.V](../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze/) |
| [6.6](#c-6-6) | Accordi di riservatezza o di non divulgazione | Sì | Sì | L C B R | [PR05.1](../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/), [MDPR05.1.V](../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze/) |
| [6.7](#c-6-7) | Lavoro remoto | Sì | Sì | C B | [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [ALPR05.1.E](../../7_GESTIONE%20RISORSE/ALPR05.1.E%20-%20Accordo%20Lavoro%20Agile/), [ALPR05.1.F](../../7_GESTIONE%20RISORSE/ALPR05.1.F%20-%20Informativa%20Lavoro%20Agile/) |
| [6.8](#c-6-8) | Segnalazione degli eventi di sicurezza delle informazioni | Sì | Sì | L B R | [PR27.1](../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/), [ALPR27.1.A](../../A_EVENTI%20%26%20INCIDENTI/ALPR27.1.A%20-%20Notifica%20Data%20Breach%20all%E2%80%99interessato/) |

### 7. Controlli fisici (Physical controls)

| ID | Controllo | Applicabile | Attuato | Motivo | Riferimenti |
|---|---|---|---|---|---|
| [7.1](#c-7-1) | Perimetri di sicurezza fisica | Sì | No | B R | [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/), [ALPR18.1.A](../../A_SICUREZZA%20FISICA%20AMBIENTALE/ALPR18.1.A%20-%20Piantina%20accessi.pptx), [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/) |
| [7.2](#c-7-2) | Accessi fisici | Sì | No | L B R | [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/), [ALPR18.1.A](../../A_SICUREZZA%20FISICA%20AMBIENTALE/ALPR18.1.A%20-%20Piantina%20accessi.pptx), [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [MDPR18.1.D](../../A_SICUREZZA%20FISICA%20AMBIENTALE/MDPR18.1.D%20-%20Registri%20interventi%20ambientali/), [MDPR05.1.U](../../7_GESTIONE%20RISORSE/MDPR05.1.U%20-%20Gestione%20chiavi/), [MDPR05.1.U](../../7_GESTIONE%20RISORSE/MDPR05.1.U%20-%20Gestione%20chiavi/) |
| [7.3](#c-7-3) | Sicurezza degli uffici, stanze e strutture | Sì | No | L B R | [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/) |
| [7.4](#c-7-4) | Monitoraggio della sicurezza fisica | Sì | No | B R | [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/) |
| [7.5](#c-7-5) | Protezione dalle minacce fisiche e ambientali | Sì | No | L B R | [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/) |
| [7.6](#c-7-6) | Lavorare in aree sicure | Sì | No | L B R | [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/) |
| [7.7](#c-7-7) | Scrivania e schermo puliti | Sì | No | B R | [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/) |
| [7.8](#c-7-8) | Disposizione delle apparecchiature e loro protezione | Sì | No | B R | [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/), [ALPR18.1.A](../../A_SICUREZZA%20FISICA%20AMBIENTALE/ALPR18.1.A%20-%20Piantina%20accessi.pptx), [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/) |
| [7.9](#c-7-9) | Sicurezza delle apparecchiature e degli asset all’esterno delle sedi | Sì | No | B R | [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [ALPR05.1.E](../../7_GESTIONE%20RISORSE/ALPR05.1.E%20-%20Accordo%20Lavoro%20Agile/) |
| [7.10](#c-7-10) | Supporti di memorizzazione | Sì | No | L B R | [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/) |
| [7.11](#c-7-11) | Infrastrutture di supporto | Sì | No | B R | [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/) |
| [7.12](#c-7-12) | Sicurezza dei cablaggi | No | — | B | [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/) |
| [7.13](#c-7-13) | Manutenzione delle apparecchiature | Sì | No | B R | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/), [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/) |
| [7.14](#c-7-14) | Dismissione sicura o riutilizzo delle apparecchiature | Sì | No | B R | [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |

### 8. Controlli tecnologici (Technological controls)

| ID | Controllo | Applicabile | Attuato | Motivo | Riferimenti |
|---|---|---|---|---|---|
| [8.1](#c-8-1) | Dispostivi finali degli utenti | Sì | No | B R | [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [PR18.1](../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/) |
| [8.2](#c-8-2) | Diritti di accesso privilegiato | Sì | No | L B R | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.3](#c-8-3) | Restrizione degli accessi alle informazioni | Sì | No | L B R | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.4](#c-8-4) | Controllo degli accessi al codice sorgente dei programmi | Sì | Sì | L B R | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/), [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/) |
| [8.5](#c-8-5) | Autenticazione sicura | Sì | No | L B R | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/) |
| [8.6](#c-8-6) | Gestione della capacità | Sì | No | B R | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.7](#c-8-7) | Protezione contro il malware | Sì | Sì | B R | [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/) |
| [8.8](#c-8-8) | Gestione delle vulnerabilità tecniche | Sì | Sì | L B R | [PR23.1](../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche/), [PR11.1](../../9.2_AUDIT%20INTERNO/PR11.1%20-%20Audit%20Interno/), [MDPR11.1.A](../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/) |
| [8.9](#c-8-9) | Gestione delle configurazioni sicure e dell’hardening | Sì | No | B R | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.10](#c-8-10) | Cancellazione delle informazioni | Sì | Sì | L C B R | [PO15](../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.11](#c-8-11) | Mascheramento e anonimizzazione dei dati | No | — | L B | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/) |
| [8.12](#c-8-12) | Prevenzione dalla perdita di dati | Sì | Sì | L B R | [PO15](../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.13](#c-8-13) | Backup delle informazioni | Sì | Sì | L B | [PR21.1](../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore/), [MDPR21.1.A](../../A_BACKUP%20%26%20RESTORE/MDPR21.1.A%20-%20Piano%20di%20Restore/) |
| [8.14](#c-8-14) | Ridondanza delle strutture di elaborazione delle informazioni | Sì | Sì | L B R | [PR28.1](../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/), [MDPR28.1.A](../../A_CONTINUITA_%20OPERATIVA/MDPR28.1.A%20-%20BIA_Business%20Impact%20Analysis%20%2827001%29/), [MDPR21.1.A](../../A_BACKUP%20%26%20RESTORE/MDPR21.1.A%20-%20Piano%20di%20Restore/) |
| [8.15](#c-8-15) | Logging | Sì | No | L B R | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/), [MDPR11.1.A](../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/) |
| [8.16](#c-8-16) | Attività di monitoraggio | Sì | No | B R | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.17](#c-8-17) | Sincronizzazione degli orologi | Sì | Sì | B | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.18](#c-8-18) | Uso di programmi di utilità privilegiati | Sì | No | L B R | [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [ALPR05.1.G](../../7_GESTIONE%20RISORSE/ALPR05.1.G%20-%20Lista%20software%20permessi/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.19](#c-8-19) | Installazione del software sui sistemi di produzione | Sì | Sì | B R | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/), [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [ALPR05.1.G](../../7_GESTIONE%20RISORSE/ALPR05.1.G%20-%20Lista%20software%20permessi/) |
| [8.20](#c-8-20) | Sicurezza delle reti | Sì | No | L B R | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.21](#c-8-21) | Sicurezza dei servizi di rete | Sì | Sì | L B R | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.22](#c-8-22) | Segregazione delle reti | Sì | No | L B R | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.23](#c-8-23) | Filtro del web | Sì | No | B R | [REG01](../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.24](#c-8-24) | Uso della crittografia | Sì | Sì | L B R | [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.25](#c-8-25) | Ciclo di vita dello sviluppo sicuro | Sì | Sì | B | [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/), [ALPO25.A](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/ALPO25.A%20-%20Linee%20guida%20per%20lo%20sviluppo%20software/) |
| [8.26](#c-8-26) | Requisiti di sicurezza delle applicazioni | Sì | Sì | L B R | [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/) |
| [8.27](#c-8-27) | Principi di architettura e ingegnerizzazione dei sistemi sicuri | Sì | Sì | B R | [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/) |
| [8.28](#c-8-28) | Codifica sicura | Sì | Sì | C B | [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/) |
| [8.29](#c-8-29) | Test di sicurezza durante lo sviluppo e per l’accettazione | Sì | Sì | B R | [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/) |
| [8.30](#c-8-30) | Sviluppo affidato all’esterno | No | — | B | [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/) |
| [8.31](#c-8-31) | Separazione degli ambienti di sviluppo, test e produzione | Sì | Sì | B | [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/), [PR16.1](../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/), [PR32.1](../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/) |
| [8.32](#c-8-32) | Gestione dei cambiamenti | Sì | Sì | B R | [PR19.1](../../A_CAMBIAMENTO/PR19.1%20-%20Gestione%20del%20Cambiamento/), [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/) |
| [8.33](#c-8-33) | Dati di test | Sì | Sì | B | [PO25](../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/) |
| [8.34](#c-8-34) | Protezione dei sistemi informativi durante i test di audit | Sì | Sì | B | [MDPR11.1.A](../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/) |

## Dettaglio dei controlli

### 5. Controlli organizzativi (Organizational controls)

<details class="soa-ctrl" id="c-5-1">
<summary><strong>5.1</strong> Politiche per la sicurezza delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Politiche per la sicurezza delle informazioni <br/>(Policies for information security)<br><em>Information security policy and topic-specific policies should be defined, approved by management, published, communicated to and acknowledged by relevant personnel and relevant interested parties, and reviewed at planned intervals and if significant changes occur.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione ha definito, implementato e mantiene un insieme strutturato di politiche per la sicurezza delle informazioni, formalizzate all’interno del proprio sistema di gestione (ISMS).<br/><br/>Le politiche coprono la protezione di tutti gli asset aziendali, inclusi:<br/><br/>infrastrutture IT e di rete (es. server cloud, rete interna, dispositivi client)<br/>software e servizi (es. Google Workspace, sistemi di ticketing, strumenti di sviluppo)<br/>dati aziendali e dei clienti (contratti, codice sorgente, dati amministrativi)<br/>risorse umane e competenze (know-how interno)<br/><br/>Le politiche sono documentate e mantenute aggiornate (rif. asset A0037-A0038) e includono, tra le altre:<br/><br/>controllo degli accessi ai sistemi e ai dati<br/>gestione degli asset e classificazione delle informazioni<br/>utilizzo accettabile delle risorse aziendali<br/>gestione delle credenziali e autenticazione<br/>protezione dei dati dei clienti e del codice sorgente<br/>gestione dei fornitori e servizi terzi (es. cloud, software SaaS)<br/>monitoraggio e logging (rif. asset A0035)<br/>gestione degli incidenti di sicurezza<br/><br/>L’implementazione è supportata da:<br/><br/>utilizzo di piattaforme centralizzate e controllate (es. Google Workspace, sistemi cloud)<br/>segregazione degli ambienti e controllo degli accessi ai repository<br/>tracciamento delle attività tramite sistemi di logging e audit<br/>uso di strumenti di collaborazione e ticketing per garantire tracciabilità operativa<br/><br/>Le politiche sono coerenti con il modello organizzativo aziendale, che privilegia:<br/><br/>collaborazione continua e trasparenza<br/>rapidità di adattamento (approccio agile)<br/>responsabilizzazione diretta delle risorse<br/><br/>in linea con i principi operativi dell’azienda<br/><br/>Infine:<br/><br/>le politiche vengono comunicate a tutto il personale<br/>sono soggette a revisione periodica<br/>sono verificate tramite attività di audit interno (rif. asset A0033)</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../01_POLITICA%20SISTEMA%20INTEGRATO/PO01%20-%20Sistema%20Integrato-Rev%200.0/">PO01 - Sistema Integrato</a><br/><a href="../../4_CONTESTO/PO02%20-%20Gestione%20del%20Contesto/">PO02 - Gestione del Contesto</a><br/><a href="../../6.2_OBIETTIVI/MDPO03.A%20-%20Lista%20Obiettivi/">MDPO03.A - Lista Obiettivi</a><br/><a href="../../7.4_COMUNICAZIONI/PO07%20-%20Politica%20Gestione%20della%20Comunicazione/">PO07 - Gestione della Comunicazione</a><br/><a href="../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/">PO15 - Classificazione delle Informazioni</a> <br/><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/><a href="../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore/">PR21.1 - Gestione dei Backup e Restore</a><br/><a href="../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche/">PR23.1 - Gestione delle Minacce e delle Vulnerabilità Tecniche</a><br/><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a><br/><a href="../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/">PR26.1 - Gestione dei fornitori</a><br/><a href="../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/">PR27.1 - Gestione Incidenti e Data Breach</a><br/><a href="../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/">PR28.1 - Gestione della continuità operativa</a><br/><a href="../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/">PO29 - Gestione della conformità</a><br/><a href="../../A_CONFORMITA_/PO31%20-%20Misure%20di%20sicurezza%20protezione%20dati%20personali/">PO31 - Misure di sicurezza protezione dati personali</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Governance<br>Domini di sicurezza: #Governance_ and_Ecosystem #Resilience<br>Processi: #Governance</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-2">
<summary><strong>5.2</strong> Ruoli e responsabilità per la sicurezza delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Ruoli e responsabilità per la sicurezza delle informazioni<br/>(Information security roles and responsibilities)<br><em>Information security roles and responsibilities should be defined and allocated according to the organization needs.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione ha definito e formalizzato ruoli e responsabilità per la sicurezza delle informazioni, integrandoli nei principali processi aziendali.<br/><br/>Per ciascun processo sono identificati:<br/><br/>un Asset Owner, responsabile della gestione operativa e della protezione degli asset informativi<br/>un Risk Owner, responsabile della valutazione e del trattamento dei rischi<br/><br/>I ruoli sono assegnati come segue:<br/><br/>IT: Asset Owner Andrea Ruzzenenti (IT), Risk Owner Andrea Ruzzenenti (CEO)<br/>Software Development: Asset Owner Andrea Ruzzenenti (SD), Risk Owner Andrea Ruzzenenti (CEO)<br/>Amministrazione: Asset Owner Francesco Cappetti (AMM), Risk Owner Andrea Ruzzenenti (CEO)<br/>Risorse Umane: Asset Owner Francesco Cappetti (HR), Risk Owner Andrea Ruzzenenti (CEO)<br/>Business Development: Asset Owner Davide Ruzzenenti, Risk Owner Andrea Ruzzenenti (CEO)<br/><br/>Gli Asset Owner garantiscono la corretta gestione e protezione degli asset, applicando le politiche di sicurezza e segnalando eventuali criticità .<br/><br/>Il Risk Owner supervisiona i rischi a livello aziendale, valuta gli impatti e approva le azioni di mitigazione.<br/><br/>I ruoli e le responsabilità sono comunicati alle risorse coinvolte e riesaminati periodicamente o in caso di cambiamenti organizzativi.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../01_POLITICA%20SISTEMA%20INTEGRATO/ALPO01.A%20-%20Organigramma-Rev%200.0/">ALPO01.A - Organigramma</a><br/><a href="../../01_POLITICA%20SISTEMA%20INTEGRATO/ALPO01.B%20-%20Mansionario-Rev%200.0/">ALPO01.B - Mansionario</a><br/><a href="../../4_CONTESTO/ALPO02.A%20-%20Contesto%20e%20Processi/">ALPO02.A - Contesto e Processi</a><br/><a href="../../4_CONTESTO/ALPO02.B-%20Analisi%20Stakeholder/">ALPO02.B - Analisi Stakeholder</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Governance<br>Domini di sicurezza: #Governance_and_ Ecosystem<br/>#Protection <br/>#Resilience<br>Processi: #Governance</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-3">
<summary><strong>5.3</strong> Separazione dei compiti <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Separazione dei compiti<br/>(Segregation of duties)<br><em>Conflicting duties and conflicting areas of responsibility should be segregated.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (23/11/2026):</strong> in ERA il controllo risulta solo pianificato (Plan).<br/><br/>L’organizzazione riconosce che, data la dimensione e la struttura attuale, non è sempre possibile garantire una completa separazione dei compiti e delle responsabilità tra le diverse funzioni.<br/><br/>In particolare, alcune figure chiave ricoprono più ruoli operativi e decisionali (es. gestione IT, sviluppo software e supervisione dei rischi), con potenziali sovrapposizioni tra responsabilità operative e di controllo.<br/><br/>Per mitigare i rischi derivanti da tale situazione, l’organizzazione ha adottato le seguenti misure:<br/><br/>definizione formale di ruoli e responsabilità (Asset Owner e Risk Owner)<br/>tracciamento delle attività tramite sistemi di logging e strumenti di ticketing<br/>utilizzo di repository e strumenti collaborativi con storico delle modifiche<br/>revisione delle attività critiche quando possibile (es. codice, configurazioni, accessi)<br/>audit interni periodici<br/><br/>L’organizzazione prevede, con la crescita e l’evoluzione della struttura, di migliorare progressivamente la separazione dei compiti, introducendo una maggiore distinzione tra ruoli operativi e di controllo.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../01_POLITICA%20SISTEMA%20INTEGRATO/ALPO01.A%20-%20Organigramma-Rev%200.0/">ALPO01.A - Organigramma</a><br/><a href="../../01_POLITICA%20SISTEMA%20INTEGRATO/ALPO01.B%20-%20Mansionario-Rev%200.0/">ALPO01.B - Mansionario</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Governance <br/>#Identity_and_ access_management<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Governance</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-4">
<summary><strong>5.4</strong> Responsabilità della direzione <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Responsabilità della direzione<br/>(Management responsibilities)<br><em>Management should require all personnel to apply information security in accordance with the established information security policy, topic-specific policies and procedures of the organization.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione garantisce che la direzione richieda attivamente a tutto il personale di operare nel rispetto delle politiche e delle procedure di sicurezza delle informazioni definite.<br/><br/>La responsabilità ultima della sicurezza delle informazioni è in capo alla direzione, che:<br/><br/>definisce e approva le politiche di sicurezza<br/>assicura che siano comunicate e comprese dal personale<br/>promuove una cultura aziendale orientata alla sicurezza<br/><br/>Il personale è tenuto ad applicare le politiche e le procedure di sicurezza nell’ambito delle proprie attività operative, in particolare per quanto riguarda:<br/><br/>utilizzo degli strumenti aziendali<br/>gestione degli accessi e delle credenziali<br/>protezione dei dati aziendali e dei clienti<br/>sviluppo e gestione del software<br/><br/>L’adozione delle politiche è supportata da:<br/><br/>utilizzo di strumenti centralizzati e controllati (es. sistemi cloud, repository, piattaforme collaborative)<br/>tracciamento delle attività tramite sistemi di logging e ticketing<br/>supervisione diretta della direzione e dei responsabili di processo<br/><br/>Il rispetto delle politiche è verificato tramite attività di monitoraggio e audit interni periodici.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/">PR05.1 - Gestione del personale</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento sull’utilizzo degli strumenti aziendali</a><br/><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.A%20-%20Checklist%20Documenti%20per%20Inserimento%20Personale/">MDPR05.1.A - Checklist Documenti per Inserimento Personale</a><br/><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze/">MDPR05.1.V - Modulo_consegna_riconsegna_HW_utenze</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Governance<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Governance</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-5">
<summary><strong>5.5</strong> Contatti con le autorità <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Contatti con le autorità<br/>(Contact with authorities)<br><em>The organization should establish and maintain contact with relevant authorities.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione utilizza principalmente servizi cloud forniti da provider qualificati per la gestione dei dati aziendali e dei clienti (es. servizi di collaborazione, repository e infrastrutture).<br/><br/>Pur delegando parte delle misure tecniche di sicurezza ai fornitori, l’organizzazione mantiene la responsabilità sulla gestione dei dati e sulla conformità normativa.<br/><br/>Sono stati identificati i principali riferimenti istituzionali per la gestione di eventuali incidenti di sicurezza, tra cui:<br/><br/>il Garante per la Protezione dei Dati Personali<br/>le autorità competenti in materia di sicurezza informatica<br/><br/>La direzione è responsabile della valutazione degli incidenti e dell’eventuale attivazione dei contatti con le autorità , in conformità agli obblighi normativi applicabili.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7.5_INFORMAZIONI%20DOCUMENTATE/MDPR08.1.A%20-%20Elenco%20Informazioni%20documentate/">MDPR08.1.A - Elenco Informazioni Documentate / Forum</a><br/><a href="../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/">PR27.1 - Gestione Incidenti e Data Breach</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Protect #Respond #Recover<br>Capacità operative: #Governance<br>Domini di sicurezza: #Defence <br/>#Resilience<br>Processi: #Governance</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-6">
<summary><strong>5.6</strong> Contatti con gruppi di interesse <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Contatti con gruppi di interesse<br/>(Contact with special interest groups)<br><em>The organization should establish and maintain contact with special interest groups or other specialist security forums and professional associations.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (24/11/2026):</strong> non sono ancora definite le fonti di aggiornamento seguite. Previste CSIRT Italia, avvisi di sicurezza dei fornitori (Aruba, Google Workspace, GitHub, Bitwarden) e avvisi delle dipendenze su GitHub, con iscrizioni a cura del System Administrator, entro il 15/12/2026 (azione T33 del piano di trattamento MDPR33.1.B).<br/><br/>informazioni attraverso il monitoraggio di fonti pubbliche, documentazione tecnica e community professionali.<br/><br/>Il personale tecnico partecipa attivamente a community di sviluppo software e tecnologia, e si aggiorna costantemente su best practice e vulnerabilità attraverso:<br/><br/>documentazione ufficiale dei fornitori tecnologici<br/>piattaforme di sviluppo e collaborazione<br/>risorse online e community tecniche<br/><br/>Data la natura dell’organizzazione, non sono attualmente formalizzati rapporti con specifiche associazioni o gruppi strutturati di sicurezza, ma viene comunque garantito un aggiornamento continuo e informale sulle tematiche rilevanti.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7.5_INFORMAZIONI%20DOCUMENTATE/MDPR08.1.A%20-%20Elenco%20Informazioni%20documentate/">MDPR08.1.A - Elenco Informazioni Documentate / Forum</a><br/><a href="../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche/">PR23.1 - Gestione delle Minacce e delle Vulnerabilità Tecniche</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect #Respond #Recover<br>Capacità operative: #Governance<br>Domini di sicurezza: #Defence<br>Processi: #Governance</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-7">
<summary><strong>5.7</strong> Monitoraggio delle minacce <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Monitoraggio delle minacce<br/>(Threat intelligence)<br><em>Information relating to information security threats should be collected and analysed to produce threat intelligence.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione monitora le minacce alla sicurezza delle informazioni attraverso l’analisi di fonti informative rilevanti e l’utilizzo di tecnologie e servizi aggiornati.<br/><br/>In particolare, il monitoraggio è effettuato tramite:<br/><br/>aggiornamenti e comunicazioni dei fornitori di servizi cloud e software utilizzati<br/>documentazione ufficiale e canali di sicurezza dei principali strumenti tecnologici adottati<br/>community tecniche e risorse online relative allo sviluppo software e alla sicurezza<br/>attività di sviluppo e manutenzione che includono aggiornamento delle dipendenze e verifica delle vulnerabilità note<br/><br/>Le informazioni raccolte vengono valutate dal personale tecnico e dalla direzione al fine di identificare eventuali impatti sugli asset aziendali e definire le azioni necessarie.<br/><br/>Data la dimensione dell’organizzazione, non è presente un sistema strutturato di threat intelligence, ma è comunque garantito un monitoraggio continuo e proporzionato ai rischi.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche/">PR23.1 - Gestione delle Minacce e delle Vulnerabilità Tecniche</a><br/><a href="../../A_MINACCE%20%26%20VULNERABILITA_/MDPR23.1.B%20-%20Monitoraggio%20delle%20minacce%202026/">MDPR23.1.B - Monitoraggio delle minacce 2026</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Detective <br/>#Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Detect <br/>#Respond<br>Capacità operative: #Threat_and_ vulnerability_management<br>Domini di sicurezza: #Defence <br/>#Resilience<br>Processi: #Minacce e Vulnerabilità</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-8">
<summary><strong>5.8</strong> Sicurezza delle informazioni nella gestione dei progetti <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza delle informazioni nella gestione dei progetti<br/>(Information security in project management)<br><em>Information security shall be integrated into project management.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (24/11/2026):</strong> manca una registrazione della sicurezza nei progetti. Prevista una checklist di sicurezza in apertura di ogni progetto, come passo della pipeline di progetto del software interno VectorHub, entro il 15/12/2026 o al più tardi entro febbraio 2027 (azione T34 del piano di trattamento MDPR33.1.B).<br/><br/>L’organizzazione integra la sicurezza delle informazioni nella gestione dei progetti, in particolare nei progetti di sviluppo software e nelle attività tecniche.<br/><br/>Durante le fasi di progettazione e sviluppo vengono considerate le principali esigenze di sicurezza, tra cui:<br/><br/>gestione degli accessi ai sistemi e ai repository<br/>protezione dei dati dei clienti e delle informazioni sensibili<br/>utilizzo di infrastrutture e servizi cloud sicuri<br/>aggiornamento e manutenzione delle dipendenze software<br/><br/>Le attività progettuali sono gestite tramite strumenti di collaborazione e versionamento che garantiscono tracciabilità e controllo delle modifiche.<br/><br/>Il personale tecnico applica buone pratiche di sviluppo sicuro e tiene conto delle implicazioni di sicurezza durante l’intero ciclo di vita del progetto.<br/><br/>Data la natura agile dell’organizzazione, la sicurezza è integrata in modo continuo nelle attività operative, piuttosto che gestita come fase separata.</td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Protect<br>Capacità operative: #Governance<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Governance</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-9">
<summary><strong>5.9</strong> Inventario delle informazioni e degli altri asset associati <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Inventario delle informazioni e degli altri asset associati<br/>(Inventory of information and other associated assets)<br><em>An inventory of information and other associated assets, including owners, should be developed and maintained.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione ha definito e mantiene un inventario aggiornato degli asset informativi e degli altri asset associati.<br/><br/>L’inventario include diverse categorie di asset, tra cui:<br/><br/>infrastrutture hardware e dispositivi<br/>software e servizi (inclusi servizi cloud)<br/>dati aziendali e dei clienti<br/>documentazione e procedure<br/>risorse umane e competenze<br/><br/>Per ciascun asset sono identificati:<br/><br/>una classificazione e tipologia<br/>lo stato (attivo/inattivo)<br/>la localizzazione (es. sede, cloud)<br/>il responsabile della gestione (Asset Owner)<br/><br/>L’inventario è mantenuto aggiornato e riesaminato periodicamente, al fine di garantire una corretta gestione e protezione degli asset durante tutto il loro ciclo di vita.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze/">MDPR05.1.V - Modulo_consegna_riconsegna_HW_utenze</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/><a href="../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/">PO15 - Classificazione delle Informazioni</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a><br/>Asset Inventory ERA<br/>Software di CMDB</td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Asset_management<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Gestione Asset</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-10">
<summary><strong>5.10</strong> Uso accettabile delle informazioni e degli altri asset associati <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Uso accettabile delle informazioni e degli altri asset associati<br/>(Acceptable use of information and other associated assets)<br><em>Rules for the acceptable use and procedures for handling information and other associated assets should be identified, documented and implemented.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione ha definito e applica regole per l’utilizzo accettabile delle informazioni e degli asset aziendali, al fine di garantirne un uso corretto e sicuro.<br/><br/>Il personale è tenuto a utilizzare gli asset aziendali esclusivamente per scopi lavorativi e nel rispetto delle politiche di sicurezza definite.<br/><br/>In particolare:<br/><br/>l’accesso ai sistemi e ai dati è consentito solo agli utenti autorizzati<br/>le credenziali di accesso devono essere mantenute riservate e non condivise<br/>i dati aziendali e dei clienti devono essere gestiti tramite strumenti e piattaforme approvate<br/>è vietato l’utilizzo di strumenti non autorizzati per la gestione o la condivisione di informazioni aziendali<br/>è richiesto il rispetto delle normative applicabili in materia di protezione dei dati<br/><br/>L’utilizzo degli asset è supportato da strumenti centralizzati e controllati (es. servizi cloud, repository, piattaforme collaborative), che garantiscono tracciabilità e controllo delle attività .<br/><br/>Le regole di utilizzo sono comunicate al personale e fanno parte delle procedure operative dell’organizzazione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Asset_management <br/>#Information_protection<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Gestione Risorse</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-11">
<summary><strong>5.11</strong> Restituzione degli asset <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Restituzione degli asset<br/>(Return of assets)<br><em>Personnel and other interested parties as appropriate should return all the organization’s assets in their possession upon change or termination of their employment, contract or agreement.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione prevede la restituzione degli asset aziendali da parte del personale e di eventuali collaboratori al termine o alla modifica del rapporto di lavoro o collaborazione.<br/><br/>Gli asset includono, a titolo esemplificativo:<br/><br/>dispositivi hardware (es. PC, dispositivi mobili)<br/>supporti di memorizzazione<br/>chiavi di accesso fisico agli uffici<br/>credenziali e accessi ai sistemi informativi<br/><br/>Alla cessazione del rapporto, vengono effettuate le seguenti attività :<br/><br/>restituzione degli asset fisici assegnati<br/>revoca degli accessi ai sistemi e ai servizi aziendali<br/>verifica della corretta gestione delle informazioni aziendali<br/><br/>La gestione del processo è affidata alla direzione e ai responsabili dei processi coinvolti (IT e Risorse Umane).</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze/">MDPR05.1.V - Modulo_consegna_riconsegna_HW_utenze</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Asset_management<br>Domini di sicurezza: #Protection<br>Processi: #Gestione Asset</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-12">
<summary><strong>5.12</strong> Classificazione delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Classificazione delle informazioni<br/>(Classification of information)<br><em>Information should be classified according to the information security needs of the organization based on confidentiality, integrity, availability and relevant interested party requirements.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce l’importanza della classificazione delle informazioni in base ai requisiti di riservatezza, integrità e disponibilità .<br/><br/>Attualmente, le informazioni sono gestite attraverso strumenti e piattaforme centralizzate che garantiscono un controllo degli accessi e una protezione adeguata dei dati.<br/><br/>Lo schema di classificazione è formalizzato in “<a href="../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/">PO15</a> - Classificazione delle Informazioni”, che definisce tre livelli di riservatezza (Pubblico, Interno, Confidenziale) e cinque classi di criticità, con responsabilità dell’Owner dell’informazione nell’attribuzione del livello e revisione in occasione del Riesame della Direzione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/">PO15 - Classificazione delle Informazioni</a><br/>Asset Inventory ERA<br/><a href="../../A_CONFORMITA_/MDPR31.4.A%20-%20Registro%20dei%20Trattamenti%20Titolare/">MDPR31.4.A - Registro dei trattamenti del Titolare</a><br/><a href="../../A_CONFORMITA_/MDPR31.4.B%20-%20Registro%20dei%20Trattamenti%20Responsabile/">MDPR31.4.B - Registro dei trattamenti del Responsabile</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Information_protection<br>Domini di sicurezza: #Protection <br/>#Defence<br>Processi: #Classificazione e Protezione delle Informazioni</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-13">
<summary><strong>5.13</strong> Etichettatura delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Etichettatura delle informazioni<br/>(Labelling of information)<br><em>An appropriate set of procedures for information labelling should be developed and implemented in accordance with the information classification scheme adopted by the organization.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione applica modalità di etichettatura delle informazioni coerenti con la classificazione adottata.<br/><br/>Le informazioni sono gestite secondo livelli di classificazione (es. pubblico, interno, riservato), che vengono riflessi nelle modalità di gestione e accesso ai dati.<br/><br/>L’etichettatura non è sempre esplicita tramite marcature formali, ma è implementata attraverso:<br/><br/>controllo degli accessi ai sistemi e ai repository<br/>organizzazione dei dati in ambienti e strumenti distinti<br/>gestione dei permessi in base al ruolo<br/><br/>In questo modo, le informazioni sono trattate in maniera coerente con il loro livello di sensibilità .</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/">PO15 - Classificazione delle Informazioni</a><br/>Asset Inventory ERA<br/><a href="../../A_CONFORMITA_/MDPR31.4.A%20-%20Registro%20dei%20Trattamenti%20Titolare/">MDPR31.4.A - Registro dei trattamenti del Titolare</a><br/><a href="../../A_CONFORMITA_/MDPR31.4.B%20-%20Registro%20dei%20Trattamenti%20Responsabile/">MDPR31.4.B - Registro dei trattamenti del Responsabile</a><br/>Software di CMDB</td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Information_protection<br>Domini di sicurezza: #Defence <br/>#Protection<br>Processi: #Classificazione e Protezione delle Informazioni</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-14">
<summary><strong>5.14</strong> Trasferimento delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Trasferimento delle informazioni<br/>(Information transfer)<br><em>Information transfer rules, procedures, or agreements should be in place for all types of transfer facilities within the organization and between the organization and other parties.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione utilizza procedure e strumenti controllati per il trasferimento delle informazioni sia internamente sia verso soggetti esterni.<br/><br/>Il trasferimento delle informazioni avviene principalmente tramite:<br/><br/>servizi cloud e piattaforme collaborative approvate<br/>repository di sviluppo software con controllo degli accessi<br/>sistemi di comunicazione e condivisione documentale aziendali<br/><br/>Le informazioni vengono trasferite secondo il principio del minimo accesso necessario e nel rispetto della classificazione delle informazioni.<br/><br/>Per i dati e i contenuti sensibili, l’organizzazione limita l’utilizzo di strumenti non autorizzati e utilizza piattaforme gestite da fornitori qualificati.<br/><br/>I rapporti con clienti, fornitori e collaboratori prevedono il rispetto della riservatezza delle informazioni condivise e delle misure di sicurezza applicabili.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7.4_COMUNICAZIONI/PO07%20-%20Politica%20Gestione%20della%20Comunicazione/">PO07 - Gestione della Comunicazione</a><br/><a href="../../A_FORNITORI/ALPR26.1.B.3%20-%20Accordo%20di%20Riservatezza%20con%20le%20Terze%20Parti/">ALPR26.1.B.3</a> - Accordo di Riservatezza con le Terze Parti<br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Asset_management <br/>#Information_protection<br>Domini di sicurezza: #Protection<br>Processi: #Gestione Asset</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-15">
<summary><strong>5.15</strong> Controllo degli accessi <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Controllo degli accessi<br/>(Access control)<br><em>Rules to control physical and logical access to information and other associated assets should be established and implemented based on business and information security requirements.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione ha definito e applica regole per il controllo degli accessi fisici e logici alle informazioni e agli asset associati, in funzione delle esigenze operative e dei requisiti di sicurezza.<br/><br/>L’accesso ai sistemi, ai servizi cloud, ai repository e alle informazioni aziendali è consentito esclusivamente agli utenti autorizzati, sulla base del ruolo e delle necessità operative.<br/><br/>Le misure adottate includono:<br/><br/>gestione centralizzata degli account e delle credenziali<br/>utilizzo di repository e piattaforme collaborative con controllo degli accessi<br/>limitazione degli accessi alle sole risorse necessarie<br/>revoca degli accessi in caso di cessazione o modifica del rapporto di lavoro o collaborazione<br/>controllo degli accessi fisici agli uffici e agli asset aziendali<br/><br/>L’organizzazione utilizza principalmente servizi cloud e piattaforme gestite da fornitori qualificati, che forniscono ulteriori misure di sicurezza e autenticazione.<br/><br/>Le autorizzazioni vengono gestite dai responsabili dei processi e riesaminate quando necessario.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Identity_and_ access_management<br>Domini di sicurezza: #Protection<br>Processi: #Controllo Accessi</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-16">
<summary><strong>5.16</strong> Gestione delle identità <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Gestione delle identità<br/>(Identity management)<br><em>The full life cycle of identities should be managed.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce il ciclo di vita delle identità digitali associate al personale e ai collaboratori che accedono ai sistemi e agli asset aziendali.<br/><br/>Le identità vengono create, modificate e revocate in funzione delle esigenze operative e dei cambiamenti nel rapporto di lavoro o collaborazione.<br/><br/>La gestione include:<br/><br/>creazione di account individuali per l’accesso ai servizi aziendali<br/>assegnazione dei permessi in base al ruolo e alle necessità operative<br/>aggiornamento o revoca degli accessi in caso di variazioni organizzative<br/>disattivazione degli account non più necessari<br/><br/>L’accesso ai principali sistemi aziendali avviene tramite piattaforme centralizzate e servizi cloud che consentono la gestione controllata delle identità e delle autorizzazioni.<br/><br/>La supervisione della gestione delle identità è affidata ai responsabili dei processi e alla direzione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Identity_and_ access_management<br>Domini di sicurezza: #Protection<br>Processi: #Controllo Accessi</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-17">
<summary><strong>5.17</strong> Informazioni di autenticazione <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Informazioni di autenticazione<br/>(Authentication information)<br><em>Allocation and management of authentication information should be controlled by a management process, including advising personnel on the appropriate handling of authentication information.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce le informazioni di autenticazione attraverso procedure e pratiche finalizzate a garantirne la riservatezza e il corretto utilizzo.<br/><br/>Le credenziali di accesso ai sistemi e ai servizi aziendali sono assegnate individualmente agli utenti autorizzati e devono essere mantenute riservate.<br/><br/>Il personale è informato sulle corrette modalità di gestione delle credenziali, inclusi:<br/><br/>divieto di condivisione delle password<br/>utilizzo di password adeguate e non riutilizzate<br/>protezione delle informazioni di autenticazione da accessi non autorizzati<br/><br/>Ove disponibile, vengono utilizzati meccanismi di autenticazione avanzata, inclusa l’autenticazione multifattore (MFA), tramite i servizi cloud e le piattaforme adottate dall’organizzazione.<br/><br/>Le informazioni di autenticazione eventualmente conservate localmente sono protette tramite sistemi di cifratura dei dispositivi aziendali e strumenti di gestione sicura delle credenziali.<br/><br/>Le credenziali e gli accessi vengono aggiornati o revocati in caso di modifica o cessazione del rapporto di lavoro o collaborazione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Identity_and_ access_management<br>Domini di sicurezza: #Protection<br>Processi: #Controllo Accessi</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-18">
<summary><strong>5.18</strong> Diritti di accesso <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Diritti di accesso<br/>(Access rights)<br><em>Access rights to information and other associated assets should be provisioned, reviewed, modified and removed in accordance with the organization’s topic-specific policy on and rules for access control.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce i diritti di accesso alle informazioni e agli asset associati in funzione dei ruoli e delle necessità operative.<br/><br/>Gli accessi ai sistemi, ai servizi cloud, ai repository e agli strumenti aziendali vengono assegnati esclusivamente agli utenti autorizzati, secondo il principio del minimo privilegio necessario.<br/><br/>La gestione dei diritti di accesso include:<br/><br/>assegnazione iniziale degli accessi in base al ruolo<br/>modifica dei permessi in caso di variazioni operative o organizzative<br/>revoca degli accessi in caso di cessazione del rapporto di lavoro o collaborazione<br/>revisione degli accessi quando necessario<br/><br/>L’organizzazione utilizza piattaforme e servizi centralizzati che consentono il controllo delle autorizzazioni e la gestione degli accessi agli asset informativi.<br/><br/>La supervisione dei diritti di accesso è affidata ai responsabili dei processi e alla direzione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/><a href="../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/">MDPR11.1.A - Programma Audit (§6 verifiche tecniche)</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Identity_and_ access_management<br>Domini di sicurezza: #Protection<br>Processi: #Controllo Accessi</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-19">
<summary><strong>5.19</strong> Sicurezza delle informazioni nelle relazioni con i fornitori <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza delle informazioni nelle relazioni con i fornitori<br/>(Information security in supplier relationships)<br><em>Processes and procedures should be defined and implemented to manage the information security risks associated with the use of supplier’s products or services.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce i rischi legati alla sicurezza delle informazioni associati ai prodotti e ai servizi forniti da terze parti e fornitori esterni.<br/><br/>I servizi e le piattaforme utilizzate vengono selezionati privilegiando fornitori qualificati e ampiamente riconosciuti, in particolare per quanto riguarda:<br/><br/>infrastrutture cloud<br/>servizi di collaborazione e produttività <br/>repository e strumenti di sviluppo<br/>piattaforme software e servizi SaaS<br/><br/>Nella gestione dei fornitori vengono considerate:<br/><br/>affidabilità del fornitore<br/>misure di sicurezza offerte dal servizio<br/>gestione degli accessi e delle autorizzazioni<br/>protezione dei dati aziendali e dei clienti<br/>continuità operativa del servizio<br/><br/>L’organizzazione limita l’utilizzo di strumenti e servizi non autorizzati per il trattamento delle informazioni aziendali.<br/><br/>La supervisione delle relazioni con i fornitori e dei relativi rischi è affidata alla direzione e ai responsabili dei processi coinvolti.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/">PR26.1 - Gestione dei fornitori</a><br/><a href="../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/">PR26.1 - Gestione dei Fornitori</a><br/><a href="../../A_FORNITORI/MDPR26.1.B%20-%20Elenco%20fornitori%20qualificati/">MDPR26.1.B - Elenco fornitori qualificati</a><br/><a href="../../A_FORNITORI/ALPR26.1.A%20-%20Comunicazione%20e%20requisiti%20di%20sicurezza%20per%20i%20fornitori/">ALPR26.1.A - Comunicazione e requisiti di sicurezza per i fornitori - Rev1.0 Data 20210512</a><br/><a href="../../A_FORNITORI/ALPR26.1.B.3%20-%20Accordo%20di%20Riservatezza%20con%20le%20Terze%20Parti/">ALPR26.1.B.3</a> - Accordo di Riservatezza con le Terze Parti<br/><a href="../../A_FORNITORI/ALPR26.1.C%20-%20Contratto%20di%20fornitura/">ALPR26.1.C</a> - Contratto di fornitura<br/><a href="../../A_FORNITORI/ALPR26.1.A%20-%20Comunicazione%20e%20requisiti%20di%20sicurezza%20per%20i%20fornitori/">ALPR26.1.A - Comunicazione e requisiti di sicurezza per i fornitori</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Supplier_relationships_security<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Gestione Fornitori</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-20">
<summary><strong>5.20</strong> Sicurezza delle informazioni negli accordi con i fornitori <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza delle informazioni negli accordi con i fornitori<br/>(Addressing information security within supplier agreements)<br><em>Relevant information security requirements should be established and agreed with each supplier based on the type of supplier relationship.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione definisce requisiti di sicurezza delle informazioni proporzionati alla tipologia di rapporto con fornitori, collaboratori e prestatori di servizi esterni.<br/><br/>I requisiti di sicurezza vengono considerati nella selezione e nell’utilizzo dei fornitori che trattano informazioni aziendali o forniscono servizi critici, in particolare per:<br/><br/>servizi cloud e infrastrutture IT<br/>strumenti di collaborazione e sviluppo software<br/>servizi SaaS e piattaforme esterne<br/><br/>I rapporti con i fornitori prevedono, ove applicabile:<br/><br/>limitazione degli accessi alle sole risorse necessarie<br/>utilizzo di account e credenziali controllate<br/>rispetto della riservatezza delle informazioni condivise<br/>utilizzo di piattaforme e strumenti autorizzati dall’organizzazione<br/><br/>Per i servizi forniti da provider qualificati, l’organizzazione fa inoltre riferimento alle misure di sicurezza e alle condizioni contrattuali messe a disposizione dai fornitori stessi.<br/><br/>La supervisione dei rapporti con i fornitori è affidata alla direzione e ai responsabili dei processi coinvolti.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_FORNITORI/ALPR26.1.C%20-%20Contratto%20di%20fornitura/">ALPR26.1.C</a> - Contratto di fornitura<br/><a href="../../A_FORNITORI/ALPR26.1.D%20-%20Nomina%20Responsabile%20Trattamenti%20Dati%20Personali/">ALPR26.1.D - Nomina Responsabile Trattamenti Dati Personali</a><br/><a href="../../A_FORNITORI/ALPR26.1.A%20-%20Comunicazione%20e%20requisiti%20di%20sicurezza%20per%20i%20fornitori/">ALPR26.1.A - Comunicazione e requisiti di sicurezza per i fornitori</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Supplier_relationships_security<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Gestione Fornitori</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-21">
<summary><strong>5.21</strong> Sicurezza delle informazioni nella filiera di fornitura ICT <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza delle informazioni nella filiera di fornitura ICT<br/>(Managing information security in the ICT supply chain)<br><em>Processes and procedures should be defined and implemented to manage the information security risks associated with the ICT products and services supply chain.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce i rischi di sicurezza delle informazioni associati alla filiera di fornitura ICT attraverso la selezione e l’utilizzo controllato di prodotti e servizi tecnologici.<br/><br/>L’infrastruttura aziendale si basa prevalentemente su servizi e piattaforme fornite da provider qualificati e ampiamente riconosciuti, inclusi:<br/><br/>servizi cloud<br/>strumenti di collaborazione e produttività <br/>repository e piattaforme di sviluppo software<br/>sistemi operativi e strumenti di sviluppo<br/>servizi SaaS e servizi AI/LLM<br/><br/>Nella gestione della supply chain ICT vengono considerate:<br/><br/>affidabilità e reputazione dei fornitori<br/>aggiornamento e manutenzione dei componenti software<br/>gestione delle vulnerabilità note e degli aggiornamenti di sicurezza<br/>controllo degli accessi ai servizi e alle piattaforme utilizzate<br/>continuità e disponibilità dei servizi critici<br/><br/>L’organizzazione limita l’utilizzo di componenti, strumenti o servizi non autorizzati e monitora periodicamente i servizi ICT utilizzati nei processi aziendali.<br/><br/>La supervisione dei rischi associati alla filiera ICT è affidata alla direzione e ai responsabili dei processi tecnici coinvolti.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_FORNITORI/ALPR26.1.B.3%20-%20Accordo%20di%20Riservatezza%20con%20le%20Terze%20Parti/">ALPR26.1.B.3</a> - Accordo di Riservatezza con le Terze Parti<br/><a href="../../A_FORNITORI/ALPR26.1.C%20-%20Contratto%20di%20fornitura/">ALPR26.1.C</a> - Contratto di fornitura<br/><a href="../../A_FORNITORI/ALPR26.1.D%20-%20Nomina%20Responsabile%20Trattamenti%20Dati%20Personali/">ALPR26.1.D - Nomina Responsabile Trattamenti Dati Personali</a><br/><a href="../../A_FORNITORI/ALPR26.1.A%20-%20Comunicazione%20e%20requisiti%20di%20sicurezza%20per%20i%20fornitori/">ALPR26.1.A - Comunicazione e requisiti di sicurezza per i fornitori</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Supplier_relationships_security<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Gestione Fornitori</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-22">
<summary><strong>5.22</strong> Monitoraggio, riesame e gestione dei cambiamenti dei servizi dei fornitori <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Monitoraggio, riesame e gestione dei cambiamenti dei servizi dei fornitori<br/>(The organization should regularly monitor, review, evaluate and manage change in supplier information security practices and service delivery)<br><em>The organization should regularly monitor, review, evaluate and manage change in supplier information security practices and service delivery</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione monitora e riesamina periodicamente i servizi e le piattaforme fornite da terze parti che supportano i processi aziendali e il trattamento delle informazioni.<br/><br/>Il monitoraggio riguarda principalmente:<br/><br/>continuità e disponibilità dei servizi<br/>aggiornamenti rilevanti dei servizi utilizzati<br/>modifiche che possano avere impatti sulla sicurezza o sull’operatività <br/>gestione degli accessi e delle autorizzazioni<br/><br/>L’organizzazione utilizza prevalentemente servizi e piattaforme fornite da provider qualificati e consolidati, per i quali vengono seguite le comunicazioni ufficiali relative a sicurezza, aggiornamenti e modifiche dei servizi.<br/><br/>Eventuali cambiamenti rilevanti vengono valutati dal personale tecnico e dalla direzione al fine di verificare possibili impatti sugli asset aziendali e sulle modalità operative.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/">PR26.1 - Gestione dei fornitori</a><br/><a href="../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/">PR26.1 - Gestione dei Fornitori</a><br/><a href="../../A_FORNITORI/MDPR26.1.B%20-%20Elenco%20fornitori%20qualificati/">MDPR26.1.B - Elenco fornitori qualificati</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Supplier_relationships_security<br/>#Information_ security_assurance<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection <br/>#Defence<br>Processi: #Gestione Fornitori</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-23">
<summary><strong>5.23</strong> Sicurezza delle informazioni per l’uso dei servizi cloud <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza delle informazioni per l’uso dei servizi cloud<br/>(Information security for use of cloud services)<br><em>Processes for acquisition, use, management and exit from cloud services should be established in accordance with the organization’s information security requirements.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione utilizza servizi cloud per supportare le attività operative, collaborative e di sviluppo software, adottando misure proporzionate ai requisiti di sicurezza delle informazioni.<br/>L’acquisizione e l’utilizzo dei servizi cloud avvengono privilegiando fornitori qualificati e ampiamente riconosciuti, valutando:<br/><br/>affidabilità del servizio<br/><br/>misure di sicurezza offerte dal provider<br/><br/>gestione degli accessi e delle autorizzazioni<br/><br/>continuità e disponibilità del servizio<br/><br/>protezione dei dati aziendali e dei clienti<br/><br/>I servizi cloud utilizzati sono gestiti tramite account controllati e accessi autorizzati, secondo il principio del minimo privilegio necessario.<br/>L’organizzazione monitora i principali cambiamenti relativi ai servizi cloud utilizzati e valuta eventuali impatti operativi o di sicurezza.<br/>In caso di cessazione o sostituzione di un servizio cloud, vengono gestite la revoca degli accessi e la conservazione o migrazione delle informazioni rilevanti.<br/>La supervisione dei servizi cloud è affidata alla direzione e ai responsabili dei processi tecnici coinvolti.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/">PR26.1 - Gestione dei fornitori</a> §6</td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Supplier_relationships_security<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Gestione Fornitori</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-24">
<summary><strong>5.24</strong> Pianificazione e preparazione per la gestione degli incidenti relativi alla sicurezza delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Pianificazione e preparazione per la gestione degli incidenti relativi alla sicurezza delle informazioni<br/>(Information security incident management planning and preparation)<br><em>The organization should plan and prepare for managing information security incidents by defining, establishing and communicating information security incident management processes, roles and responsibilities.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione ha definito modalità operative per la gestione degli incidenti relativi alla sicurezza delle informazioni, proporzionate alla propria dimensione e struttura organizzativa.<br/><br/>La gestione degli incidenti è supervisionata dalla direzione e dai responsabili dei processi tecnici coinvolti.<br/><br/>In caso di incidente di sicurezza, l’organizzazione prevede:<br/><br/>identificazione e segnalazione dell’evento<br/>valutazione dell’impatto sugli asset e sulle informazioni aziendali<br/>gestione e contenimento dell’incidente<br/>eventuale ripristino dell’operatività <br/>analisi dell’evento e definizione di eventuali azioni correttive<br/><br/>Le attività sono supportate da:<br/><br/>sistemi di logging e tracciamento delle attività <br/>utilizzo di piattaforme e servizi cloud gestiti da provider qualificati<br/>controllo degli accessi e gestione centralizzata degli account<br/><br/>L’organizzazione non ha registrato incidenti significativi relativi alla sicurezza delle informazioni, ma mantiene comunque un approccio di monitoraggio e preparazione proporzionato ai rischi identificati.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/">PR27.1 - Gestione Incidenti e Data Breach</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Respond #Recover<br>Capacità operative: #Governance #Information_security_event_management<br>Domini di sicurezza: #Defence<br>Processi: #Eventi e Incidenti di Sicurezza</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-25">
<summary><strong>5.25</strong> Valutazione e decisione sugli eventi relativi alla sicurezza delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Valutazione e decisione sugli eventi relativi alla sicurezza delle informazioni<br/>(Assessment and decision on information security events)<br><em>The organization should assess information security events and decide if they are to be categorized as information security incidents.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione valuta gli eventi relativi alla sicurezza delle informazioni al fine di determinare se debbano essere classificati come incidenti di sicurezza.<br/><br/>Gli eventi possono essere identificati tramite:<br/><br/>anomalie operative<br/>problemi di accesso ai sistemi<br/>notifiche provenienti dai servizi cloud e dalle piattaforme utilizzate<br/>segnalazioni del personale o dei collaboratori<br/>attività di monitoraggio e logging<br/><br/>Gli eventi rilevati vengono analizzati dal personale tecnico e dalla direzione, considerando:<br/><br/>impatto sugli asset aziendali e sulle informazioni<br/>possibile compromissione di riservatezza, integrità o disponibilità <br/>necessità di azioni correttive o di contenimento<br/><br/>Qualora un evento venga ritenuto rilevante per la sicurezza delle informazioni, viene gestito come incidente secondo le modalità operative definite dall’organizzazione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/">PR27.1 - Gestione Incidenti e Data Breach</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Detective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Detect <br/>#Respond<br>Capacità operative: #Information_security_event_management<br>Domini di sicurezza: #Defence<br>Processi: #Eventi e Incidenti di Sicurezza</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-26">
<summary><strong>5.26</strong> Risposta agli incidenti relativi alla sicurezza delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Risposta agli incidenti relativi alla sicurezza delle informazioni<br/>(Response to information security incidents)<br><em>Information security incidents should be responded to in accordance with the documented procedures.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce gli incidenti relativi alla sicurezza delle informazioni secondo modalità operative definite e proporzionate alla propria struttura organizzativa.<br/><br/>In caso di incidente di sicurezza, vengono svolte le seguenti attività :<br/><br/>identificazione e segnalazione dell’evento<br/>valutazione dell’impatto e della criticità <br/>contenimento dell’incidente e protezione degli asset coinvolti<br/>eventuale revoca o limitazione degli accessi interessati<br/>ripristino dell’operatività e verifica della corretta risoluzione<br/>analisi dell’evento e definizione di eventuali azioni correttive<br/><br/>La gestione degli incidenti coinvolge la direzione e i responsabili dei processi tecnici interessati.<br/><br/>Le attività sono supportate da sistemi di logging, controllo degli accessi e utilizzo di servizi cloud e piattaforme gestite da fornitori qualificati.<br/><br/>L’organizzazione non ha registrato incidenti significativi relativi alla sicurezza delle informazioni, ma mantiene comunque procedure operative per garantire una risposta tempestiva ed efficace in caso di necessità .</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/">PR27.1 - Gestione Incidenti e Data Breach</a><br/><a href="../../A_EVENTI%20%26%20INCIDENTI/ALPR27.1.A%20-%20Notifica%20Data%20Breach%20all%E2%80%99interessato/">ALPR27.1.A - Notifica Data Breach all'interessato</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Respond #Recover<br>Capacità operative: #Information_security_event_management<br>Domini di sicurezza: #Defence<br>Processi: #Eventi e Incidenti di Sicurezza</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-27">
<summary><strong>5.27</strong> Apprendimento dagli incidenti relativi alla sicurezza delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Apprendimento dagli incidenti relativi alla sicurezza delle informazioni<br/>(Learning from information security incidents)<br><em>Knowledge gained from information security incidents should be used to strengthen and improve the information security controls.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione utilizza le informazioni derivanti da eventi e incidenti relativi alla sicurezza delle informazioni per migliorare progressivamente le misure di sicurezza e le modalità operative.<br/>Eventuali anomalie, problemi operativi o incidenti vengono analizzati dal personale tecnico e dalla direzione al fine di:<br/><br/>identificare le cause dell’evento<br/><br/>valutare eventuali impatti sugli asset aziendali<br/><br/>definire azioni correttive o migliorative<br/><br/>ridurre la probabilità di eventi analoghi futuri<br/><br/>Le conoscenze acquisite vengono utilizzate per aggiornare, ove necessario:<br/><br/>configurazioni e controlli di sicurezza<br/><br/>gestione degli accessi e delle autorizzazioni<br/><br/>modalità operative e procedure interne<br/><br/>utilizzo degli strumenti e dei servizi adottati<br/><br/>L’organizzazione non ha registrato incidenti significativi relativi alla sicurezza delle informazioni, ma applica comunque un approccio orientato al miglioramento continuo e alla prevenzione dei rischi.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/">PR27.1 - Gestione Incidenti e Data Breach</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Protect<br>Capacità operative: #Information_security_event_management<br>Domini di sicurezza: #Defence<br>Processi: #Eventi e Incidenti di Sicurezza</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-28">
<summary><strong>5.28</strong> Raccolta di prove <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Raccolta di prove<br/>(Collection of evidence)<br><em>The organization should establish and implement procedures for the identification, collection, acquisition and preservation of evidence related to information security events.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce l’importanza della raccolta e conservazione delle evidenze relative agli eventi e agli incidenti di sicurezza delle informazioni.<br/><br/>Attualmente, le informazioni utili all’analisi degli eventi sono principalmente ottenute tramite:<br/><br/>sistemi di logging e tracciamento delle attività <br/>servizi cloud e piattaforme utilizzate dall’organizzazione<br/>repository e strumenti collaborativi<br/><br/>Non è ancora stato formalizzato un processo strutturato per la raccolta, acquisizione e conservazione delle evidenze con finalità forensi.<br/><br/>L’organizzazione prevede di definire procedure proporzionate alla propria dimensione e ai rischi identificati, al fine di migliorare la gestione e la conservazione delle evidenze relative agli incidenti di sicurezza delle informazioni.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/">PR27.1 - Gestione Incidenti e Data Breach</a><br/><a href="../../A_EVENTI%20%26%20INCIDENTI/MDPR27.1.A%20-%20Registro%20Data%20Breach/">MDPR27.1.A - Registro Data Breach</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Detect <br/>#Respond<br>Capacità operative: #Information_security_event_management<br>Domini di sicurezza: #Defence<br>Processi: #Eventi e Incidenti di Sicurezza</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-29">
<summary><strong>5.29</strong> Sicurezza delle informazioni durante le interruzioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza delle informazioni durante le interruzioni<br/>(Information security during disruption)<br><em>The organization should plan how to maintain information security at an appropriate level during disruption.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione adotta misure proporzionate per mantenere un adeguato livello di sicurezza delle informazioni anche in caso di interruzioni o problemi operativi.<br/><br/>Le attività aziendali si basano prevalentemente su servizi cloud e piattaforme gestite da provider qualificati, che garantiscono elevati livelli di disponibilità , protezione dei dati e continuità operativa.<br/><br/>In caso di interruzioni o malfunzionamenti, l’organizzazione prevede:<br/><br/>utilizzo di piattaforme e servizi alternativi ove necessario<br/>controllo degli accessi e protezione delle informazioni durante le attività di ripristino<br/>verifica della disponibilità dei dati e dei repository utilizzati nei processi operativi<br/>coordinamento tra direzione e personale tecnico per la gestione delle problematiche operative<br/><br/>L’organizzazione mantiene un approccio proporzionato alla propria dimensione e alla natura delle attività svolte.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/">PR28.1 - Gestione della continuità operativa</a> <br/><a href="../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/">PR28.1 - Gestione della continuità operativa</a><br/><a href="../../A_CONTINUITA_%20OPERATIVA/MDPR28.1.A%20-%20BIA_Business%20Impact%20Analysis%20%2827001%29/">MDPR28.1.A - Piani di Continuità Operativa</a><br/><a href="../../A_BACKUP%20%26%20RESTORE/MDPR21.1.A%20-%20Piano%20di%20Restore/">MDPR21.1.A - Piano di Restore</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect #Respond<br>Capacità operative: #Continuity<br>Domini di sicurezza: #Protection <br/>#Resilience<br>Processi: #Continuità operativa</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-30">
<summary><strong>5.30</strong> Preparazione dell’ICT per la continuità operativa <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Preparazione dell’ICT per la continuità operativa<br/>(ICT readiness for business continuity)<br><em>ICT readiness should be planned, implemented, maintained and tested based on business continuity objectives and ICT continuity requirements.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Attuato dal 18/11/2026:</strong> backup settimanale dei volumi delle applicazioni, scaricato da un server secondario separato dal principale e conservato 3 settimane; copie cifrate; configurazione ricostruibile da Ansible; prima prova di ripristino riuscita il 18/11/2026 (MDPR21.1.A).<br/><br/>L’organizzazione riconosce l’importanza della continuità operativa dei sistemi ICT a supporto delle attività aziendali.<br/><br/>L’operatività aziendale si basa prevalentemente su servizi cloud e piattaforme gestite da provider qualificati, che forniscono misure di disponibilità , backup e continuità del servizio.<br/><br/>Attualmente, non è presente un piano formalizzato e testato di continuità ICT interno.<br/><br/>L’organizzazione prevede di definire progressivamente misure e procedure proporzionate alla propria dimensione e ai rischi identificati, con particolare attenzione a:<br/><br/>disponibilità dei servizi critici<br/>accessibilità dei dati e dei repository<br/>gestione delle interruzioni operative<br/>ripristino degli accessi e delle attività essenziali<br/><br/>Le esigenze di continuità ICT vengono comunque considerate nella selezione dei servizi cloud e dei fornitori tecnologici utilizzati.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore/">PR21.1 - Gestione dei Backup e Restore</a><br/><a href="../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/">PR28.1 - Gestione della continuità operativa</a> <br/><a href="../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/">PR28.1 - Gestione della continuità operativa</a><br/><a href="../../A_CONTINUITA_%20OPERATIVA/MDPR28.1.A%20-%20BIA_Business%20Impact%20Analysis%20%2827001%29/">MDPR28.1.A - Piani di Continuità Operativa</a><br/><a href="../../A_BACKUP%20%26%20RESTORE/MDPR21.1.A%20-%20Piano%20di%20Restore/">MDPR21.1.A - Piano di Restore</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Corrective<br>Proprietà di sicurezza: #Availability<br>Concetti cybersecurity: #Respond<br>Capacità operative: #Continuity<br>Domini di sicurezza: #Resilience<br>Processi: #Continuità operativa</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-31">
<summary><strong>5.31</strong> Requisiti legali, statutari, regolamentari e contrattuali <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Requisiti legali, statutari, regolamentari e contrattuali<br/>(Legal, statutory, regulatory and contractual requirements)<br><em>Legal, statutory, regulatory and contractual requirements relevant to information security and the organization’s approach to meet these requirements should be identified, documented and kept up to date</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione identifica e gestisce i requisiti legali, normativi, regolamentari e contrattuali rilevanti per la sicurezza delle informazioni.<br/><br/>In particolare, sono considerati:<br/><br/>obblighi in materia di protezione dei dati personali (es. GDPR)<br/>requisiti contrattuali con clienti e fornitori<br/>normative applicabili alla gestione dei dati aziendali e amministrativi<br/>condizioni di utilizzo dei servizi e delle piattaforme adottate<br/><br/>I requisiti vengono gestiti attraverso:<br/><br/>utilizzo di strumenti e piattaforme conformi e forniti da provider qualificati<br/>gestione controllata degli accessi e delle informazioni<br/>rispetto delle clausole di riservatezza nei rapporti con clienti e collaboratori<br/>supervisione da parte della direzione e dei responsabili dei processi<br/><br/>L’organizzazione mantiene un approccio proporzionato alla propria dimensione e aggiorna le proprie pratiche in funzione dei requisiti applicabili.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7.5_INFORMAZIONI%20DOCUMENTATE/MDPR08.1.A%20-%20Elenco%20Informazioni%20documentate/">MDPR08.1.A - Elenco Informazioni Documentate / Compliance</a><br/><a href="../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/">PO29 - Gestione della conformità</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Legal_and_compliance<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Gestione Conformità</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-32">
<summary><strong>5.32</strong> Diritti di proprietà intellettuale <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Diritti di proprietà intellettuale<br/>(Intellectual property rights)<br><em>The organization should implement appropriate procedures to protect intellectual property rights.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione protegge i diritti di proprietà intellettuale relativi agli asset informativi e al software sviluppato o gestito.<br/><br/>In particolare, sono considerate:<br/><br/>proprietà intellettuale dell’organizzazione (es. codice sorgente, know-how tecnico, documentazione interna)<br/>proprietà intellettuale dei clienti gestita nell’ambito dei progetti<br/>licenze software e condizioni di utilizzo degli strumenti adottati<br/><br/>La protezione della proprietà intellettuale è garantita attraverso:<br/><br/>controllo degli accessi ai repository di codice e ai sistemi informativi<br/>utilizzo di piattaforme centralizzate con gestione dei permessi (es. repository di sviluppo, strumenti collaborativi)<br/>rispetto delle clausole contrattuali e degli accordi di riservatezza (NDA) con clienti e collaboratori<br/>gestione controllata del codice sorgente e delle informazioni tecniche durante l’intero ciclo di vita dei progetti<br/><br/>L’organizzazione utilizza software e servizi nel rispetto delle relative licenze e condizioni d’uso.<br/><br/>La supervisione delle attività è affidata alla direzione e ai responsabili dei processi coinvolti.</td></tr>
<tr><th>Riferimenti documentali</th><td>Documento di offerta e ordine<br/><a href="../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/">PO29 - Gestione della conformità</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Legal_and_compliance<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Gestione Conformità</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-33">
<summary><strong>5.33</strong> Protezione delle registrazioni <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Protezione delle registrazioni<br/>(Protection of records)<br><em>Records should be protected from loss, destruction, falsification, unauthorized access and unauthorized release.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce l’importanza della protezione delle registrazioni e delle informazioni documentate rilevanti per le attività aziendali.<br/><br/>Le registrazioni includono, tra le altre:<br/><br/>dati amministrativi e contrattuali<br/>documentazione tecnica e operativa<br/>informazioni relative ai progetti e allo sviluppo software<br/>log e informazioni generate dai sistemi utilizzati<br/><br/>Attualmente, le registrazioni sono gestite attraverso strumenti e piattaforme centralizzate (es. servizi cloud, repository, sistemi collaborativi), che garantiscono un adeguato livello di protezione e controllo degli accessi.<br/><br/>Non è ancora formalizzato un sistema completo di gestione delle registrazioni, in particolare per quanto riguarda:<br/><br/>raccolta strutturata dei log<br/>conservazione e retention delle informazioni<br/>tracciabilità completa degli eventi (audit trail)<br/><br/>L’organizzazione prevede di definire e implementare procedure proporzionate alla propria dimensione per migliorare la gestione, la protezione e la conservazione delle registrazioni.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7.5_INFORMAZIONI%20DOCUMENTATE/MDPR08.1.A%20-%20Elenco%20Informazioni%20documentate/">MDPR08.1.A - Elenco Informazioni Documentate</a><br/><a href="../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/">PO29 - Gestione della conformità</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Protect<br>Capacità operative: #Legal_and_compliance <br/>#Asset_management <br/>#Information_protection<br>Domini di sicurezza: #Defence<br>Processi: #Classificazione e Protezione delle Informazioni</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-34">
<summary><strong>5.34</strong> Privacy e protezione dei dati personali <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Privacy e protezione dei dati personali<br/>(Privacy and protection of PII)<br><em>The organization should identify and meet the requirements regarding the preservation of privacy and protection of PII according to applicable laws and regulations and contractual requirements.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce e protegge i dati personali trattati nell’ambito delle proprie attività , in conformità ai requisiti normativi applicabili (es. GDPR).<br/><br/>I dati personali trattati includono, a titolo esemplificativo:<br/><br/>dati di clienti e contatti aziendali<br/>dati amministrativi e contrattuali<br/>dati relativi a fornitori e collaboratori<br/>CV e informazioni raccolte nei processi di selezione<br/><br/>La protezione dei dati personali è garantita attraverso:<br/><br/>utilizzo di servizi e piattaforme cloud fornite da provider qualificati<br/>controllo degli accessi ai sistemi e alle informazioni<br/>gestione dei dati tramite strumenti autorizzati e centralizzati<br/>rispetto delle clausole contrattuali e degli obblighi di riservatezza<br/>limitazione dell’accesso ai dati in base al ruolo e alle necessità operative<br/><br/>L’organizzazione adotta un approccio proporzionato alla propria dimensione e mantiene la responsabilità sul trattamento dei dati, anche quando questi sono gestiti tramite fornitori esterni.<br/><br/>La supervisione è affidata alla direzione e ai responsabili dei processi coinvolti.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/">PO29 - Gestione della conformità</a><br/><a href="../../A_CONFORMITA_/MDPO29.A%20-%20Elenco%20AdS/">MDPO29.A - Elenco AdS</a><br/><a href="../../A_CONFORMITA_/PO31%20-%20Misure%20di%20sicurezza%20protezione%20dati%20personali/">PO31 - Misure di sicurezza protezione dati personali</a><br/><a href="../../A_CONFORMITA_/ALPO31.A%20-%20Lettera%20incarico%20AdS/">ALPO31.A - Lettera Incarico AdS</a><br/><a href="../../A_CONFORMITA_/ALPO31.B%20-%20Atto%20di%20Nomina%20ad%20Autorizzato%20del%20Trattamento/">ALPO31.B - Atto di Nomina ad Autorizzato del Trattamento</a><br/><a href="../../A_CONFORMITA_/ALPO31.D%20-%20Atto%20di%20Nomina%20a%20Referente%20Privacy/">ALPO31.D - Atto di Nomina a Referente Privacy</a><br/><a href="../../A_CONFORMITA_/PR31.1%20-%20Gestione%20dei%20Diritti%20degli%20Interessati/">PR31.1 - Gestione dei diritti degli interessati</a><br/><a href="../../A_CONFORMITA_/MDPR31.1.A%20-%20Registro%20delle%20richieste/">MDPR31.1.A - Registro delle Richieste</a><br/><a href="../../A_CONFORMITA_/PR31.2%20-%20Gestione%20dei%20Consensi/">PR31.2 - Gestione dei consensi</a><br/><a href="../../A_CONFORMITA_/ALPR31.2.A%20-%20Informativa%20Privacy%20Dipendenti/">ALPR31.2.A - Informativa Privacy Dipendenti</a><br/><a href="../../A_CONFORMITA_/ALPR31.2.B%20-%20Informativa%20Privacy%20Candidati/">ALPR31.2.B - Informativa Privacy Candidati</a><br/><a href="../../A_CONFORMITA_/ALPR31.2.C%20-%20Informativa%20Privacy%20Visitatori/">ALPR31.2.C - Informativa Privacy Visitatori</a><br/><a href="../../A_CONFORMITA_/ALPR31.2.D%20-%20Informativa%20Privacy%20Fornitori/">ALPR31.2.D - Informativa Privacy Fornitori</a><br/><a href="../../A_CONFORMITA_/ALPR31.2.E%20-%20Informativa%20Privacy%20Clienti/">ALPR31.2.E - Informativa Privacy Clienti</a><br/><a href="../../A_CONFORMITA_/ALPR31.2.F%20-%20Informativa%20Privacy%20Sito/">ALPR31.2.F - Informativa Privacy Sito</a><br/><a href="../../A_CONFORMITA_/ALPR31.2.G%20-%20Liberatoria%20Foto-Video/">ALPR31.2.G - Liberatoria Foto-Video Dipendenti</a><br/><a href="../../A_CONFORMITA_/PR31.3%20-%20Procedura%20Valutazione%20d_impatto%20sulla%20protezione%20dei%20dati%20%28DPIA%29/">PR31.3 - Valutazione d'impatto sulla protezione dei dati (DPIA)</a><br/><a href="../../A_CONFORMITA_/PR31.4%20-%20Gestione%20registro%20dei%20trattamenti/">PR31.4 - Gestione dei registri di trattamento</a><br/><a href="../../A_CONFORMITA_/MDPR31.4.A%20-%20Registro%20dei%20Trattamenti%20Titolare/">MDPR31.4.A - Registro trattamenti Titolare</a><br/><a href="../../A_CONFORMITA_/MDPR31.4.B%20-%20Registro%20dei%20Trattamenti%20Responsabile/">MDPR31.4.B - Registro trattamenti Responsabile</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Protect<br>Capacità operative: #Information_protection <br/>#Legal_and_compliance<br>Domini di sicurezza: #Protection<br>Processi: #Classificazione e Protezione delle Informazioni</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-35">
<summary><strong>5.35</strong> Riesame indipendente della sicurezza delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Riesame indipendente della sicurezza delle informazioni<br/>(Independent review of information security)<br><em>The organization’s approach to managing information security and its implementation including people, processes and technologies should be reviewed independently at planned intervals, or when significant changes occur.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce l’importanza del riesame indipendente delle attività di gestione della sicurezza delle informazioni.<br/><br/>Attualmente, le attività di supervisione e controllo sono svolte dalla direzione e dai responsabili dei processi, nell’ambito della gestione operativa.<br/><br/>Il processo di riesame indipendente è formalizzato in “<a href="../../9.2_AUDIT%20INTERNO/PR11.1%20-%20Audit%20Interno/">PR11.1</a> - Audit Interno”, che definisce programma triennale, criteri di qualifica degli auditor e obbligo di ricorso ad auditor esterno per le aree in cui l’auditor interno (RSGI) sia anche responsabile operativo, per prevenire l’auto-audit.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../9.2_AUDIT%20INTERNO/PR11.1%20-%20Audit%20Interno/">PR11.1 - Audit Interno</a><br/><a href="../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/">PO29 - Gestione della conformità</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Protect<br>Capacità operative: #Information_security_assurance<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Valutazione delle Prestazioni</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-36">
<summary><strong>5.36</strong> Conformità con le politiche, le regole e le norme di sicurezza delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Conformità con le politiche, le regole e le norme di sicurezza delle informazioni<br/>(Compliance with policies, rules and standards for information security)<br><em>Compliance with the organization’s information security policy, topic-specific policies, rules and standards should be regularly reviewed.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce l’importanza della verifica della conformità alle politiche, alle regole e alle norme di sicurezza delle informazioni definite.<br/><br/>Le politiche e le procedure di sicurezza sono comunicate e applicate nell’ambito delle attività operative, in particolare per quanto riguarda:<br/><br/>gestione degli accessi ai sistemi e alle informazioni<br/>utilizzo degli strumenti e dei servizi aziendali<br/>protezione dei dati e delle informazioni aziendali e dei clienti<br/>sviluppo e gestione del software<br/><br/>Attualmente, la verifica della conformità è effettuata principalmente attraverso la supervisione della direzione e dei responsabili dei processi.<br/><br/>Non è ancora formalizzato un sistema strutturato di verifica e monitoraggio della conformità , con strumenti o controlli periodici dedicati.<br/><br/>L’organizzazione prevede di introdurre, in modo proporzionato alla propria dimensione, attività di verifica più strutturate, che potranno includere:<br/><br/>controlli periodici sugli accessi e sulle configurazioni<br/>verifiche interne dei processi operativi<br/>audit interni sulle politiche di sicurezza</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../9.2_AUDIT%20INTERNO/PR11.1%20-%20Audit%20Interno/">PR11.1 - Audit Interno</a><br/><a href="../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/">MDPR11.1.A - Programma Audit</a><br/><a href="../../9.2_AUDIT%20INTERNO/MDPR11.1.B%20-%20Piano%20di%20Audit%20e%20Report/">MDPR11.1.B - Piano di Audit e Report</a><br/><a href="../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/">MDPR11.1.A - Programma Audit (§6 verifiche tecniche)</a><br/><a href="../../A_CONFORMITA_/PO29%20-%20Gestione%20della%20conformit%C3%A0/">PO29 - Gestione della conformità</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Protect<br>Capacità operative: #Legal_and_compliance <br/>#Information_security_assurance<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Valutazione delle Prestazioni</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-5-37">
<summary><strong>5.37</strong> Procedure operative documentate <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Procedure operative documentate<br/>(Documented operating procedures)<br><em>Operating procedures for information processing facilities should be documented and made available to personnel who need them.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce l’importanza della definizione e documentazione delle procedure operative relative alla gestione dei sistemi, delle informazioni e delle attività tecniche.<br/><br/>Le attività operative sono attualmente svolte attraverso pratiche consolidate e condivise dal personale tecnico, in particolare per quanto riguarda:<br/><br/>sviluppo e gestione del software<br/>utilizzo dei sistemi e delle piattaforme cloud<br/>gestione degli accessi e delle configurazioni<br/>gestione operativa dei progetti<br/><br/>Tuttavia, tali procedure non sono ancora formalizzate in modo strutturato e documentato.<br/><br/>L’organizzazione prevede di definire e documentare progressivamente le procedure operative principali, con particolare riferimento a:<br/><br/>gestione delle configurazioni<br/>gestione dei cambiamenti<br/>gestione dei sistemi e degli ambienti<br/>attività operative ricorrenti<br/><br/>Le procedure saranno rese disponibili al personale coinvolto e aggiornate in funzione delle esigenze operative.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/><a href="../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/">PR05.1 - Gestione del Personale</a><br/><a href="../../7_GESTIONE%20RISORSE/PR06.1%20-%20Gestione%20delle%20Performance/">PR06.1 - Gestione delle Performance</a><br/><a href="../../7.5_INFORMAZIONI%20DOCUMENTATE/PR08.1%20-%20Gestione%20Informazioni%20Documentate/">PR08.1 - Gestione delle Informazioni Documentate</a><br/><a href="../../8.2_PRODOTTI%20%26%20SERVIZI/PR09.1%20-%20Gestione%20Commerciale/">PR09.1 - Gestione Commerciale</a><br/><a href="../../9.1_MONITORAGGIO%20KPI/MDPR10.1.A%20-%20Tabella%20Indicatori/">MDPR10.1.A - Tabella Indicatori</a><br/><a href="../../9.2_AUDIT%20INTERNO/PR11.1%20-%20Audit%20Interno/">PR11.1 - Audit Interno</a><br/><a href="../../9.3_RIESAME%20DIREZIONE/PR12.1%20-%20Riesame%20della%20Direzione/">PR12.1 - Riesame della Direzione</a><br/><a href="../../10_GESTIONE%20NON%20CONFORMITA_%20E%20MIGLIORAMENTO/PR13.1%20-%20Gestione%20delle%20Non%20Conformit%C3%A0%20e%20Azioni%20di%20Miglioramento/">PR13.1 - Gestione delle Non Conformità e Azioni di Miglioramento</a><br/><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a><br/><a href="../../A_CAMBIAMENTO/PR19.1%20-%20Gestione%20del%20Cambiamento/">PR19.1 - Gestione del Cambiamento</a><br/><a href="../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore/">PR21.1 - Gestione dei Backup e Restore</a><br/><a href="../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche/">PR23.1 - Gestione delle Minacce e delle Vulnerabilità Tecniche</a><br/><a href="../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/">PR26.1 - Gestione dei Fornitori</a><br/><a href="../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/">PR27.1 - Gestione Incidenti e Data Breach</a><br/><a href="../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/">PR28.1 - Gestione della continuità operativa</a><br/><a href="../../A_CONFORMITA_/PR31.1%20-%20Gestione%20dei%20Diritti%20degli%20Interessati/">PR31.1 - Gestione dei diritti degli interessati</a><br/><a href="../../A_CONFORMITA_/PR31.2%20-%20Gestione%20dei%20Consensi/">PR31.2 - Gestione dei consensi</a><br/><a href="../../A_CONFORMITA_/PR31.3%20-%20Procedura%20Valutazione%20d_impatto%20sulla%20protezione%20dei%20dati%20%28DPIA%29/">PR31.3 - Valutazione d'impatto sulla protezione dei dati (DPIA)</a><br/><a href="../../A_CONFORMITA_/PR31.4%20-%20Gestione%20registro%20dei%20trattamenti/">PR31.4 - Gestione dei registri di trattamento</a><br/><a href="../../6.1_ANALISI%20DEI%20RISCHI/PR33.1%20-%20Processo%20Analisi%20del%20Rischio%20e%20Trattamento/">PR33.1 - Processo Analisi del Rischio e Trattamento</a> <br/><a href="../../6.1_ANALISI%20DEI%20RISCHI/PR33.2%20-%20Processo%20Analisi%20del%20Rischio%20Privacy/">PR33.2 - Processo di Analisi del Rischio Privacy DPIA</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect <br/>#Recover<br>Capacità operative: #Asset_management<br/>#Physical_security <br/>#System_and_network_security <br/>#Application_security <br/>#Secure_configuration <br/>#Identity_ and_access_management <br/>#Threat_and_ vulnerability_management <br/>#Continuity <br/>#Information_security_event_management<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection <br/>#Defence<br>Processi: #Governance</td></tr>
</table>
</details>

### 6. Controlli relativi alle persone (People controls)

<details class="soa-ctrl" id="c-6-1">
<summary><strong>6.1</strong> Screening <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Screening<br><em>Background verification checks on all candidates to become personnel should be carried out prior to joining the organization and on an ongoing basis taking into consideration applicable laws, regulations and ethics and be proportional to the business requirements, the classification of the information to be accessed and the perceived risks.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce l’importanza della verifica delle competenze e dell’affidabilità del personale e dei collaboratori coinvolti nelle attività aziendali.<br/><br/>Attualmente, la selezione del personale e dei collaboratori avviene attraverso:<br/><br/>valutazione dei CV e delle esperienze professionali<br/>colloqui conoscitivi e tecnici<br/>valutazione delle competenze rispetto alle attività da svolgere<br/><br/>Non è ancora formalizzata una procedura strutturata di screening del personale in relazione ai requisiti di sicurezza delle informazioni.<br/><br/>L’organizzazione prevede di definire, in modo proporzionato alla propria dimensione, modalità di screening più strutturate, che potranno includere:<br/><br/>verifica delle competenze tecniche e professionali<br/>valutazione dell’affidabilità dei collaboratori<br/>definizione di criteri minimi per l’accesso a ruoli con accesso a informazioni sensibili</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/">PR05.1 - Gestione del Personale</a><br/><a href="../../7_GESTIONE%20RISORSE/MDPR06.1.E%20-%20Griglia%20delle%20competenze/">MDPR06.1.E - Griglia delle competenze</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Human_resource_security<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Gestione Risorse</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-6-2">
<summary><strong>6.2</strong> Termini e condizioni di impiego <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Termini e condizioni di impiego<br/>(Terms and conditions of employment)<br><em>The employment contractual agreements should state the personnel’s and the organization’s responsibilities for information security.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione definisce e applica termini e condizioni di impiego e collaborazione che includono aspetti relativi alla sicurezza delle informazioni.<br/><br/>I rapporti con personale, collaboratori e fornitori prevedono:<br/><br/>rispetto della riservatezza delle informazioni trattate<br/>utilizzo corretto degli strumenti e delle risorse aziendali<br/>accesso alle informazioni limitato in base al ruolo e alle necessità operative<br/><br/>Tali requisiti sono gestiti attraverso:<br/><br/>accordi contrattuali e/o accordi di riservatezza (NDA)<br/>assegnazione controllata degli accessi ai sistemi e alle informazioni<br/>supervisione da parte della direzione e dei responsabili dei processi<br/><br/>L’organizzazione mantiene un approccio proporzionato alla propria dimensione e alla natura delle attività svolte.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/">PR05.1 - Gestione del Personale</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a><br/><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.A%20-%20Checklist%20Documenti%20per%20Inserimento%20Personale/">MDPR05.1.A - Checklist Documenti per Inserimento Risorse</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Human_resource_security<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Gestione Risorse</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-6-3">
<summary><strong>6.3</strong> Consapevolezza, istruzione, formazione e addestramento sulla sicurezza delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Consapevolezza, istruzione, formazione e addestramento sulla sicurezza delle informazioni<br/>(Information security awareness, education and training)<br><em>Personnel of the organization and relevant interested parties should receive appropriate information security awareness, education and training and regular updates of the organization's information security policy, topic-specific policies and procedures, as relevant for their job function.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce l’importanza della consapevolezza e della formazione del personale in materia di sicurezza delle informazioni.<br/><br/>Attualmente, le conoscenze e le pratiche di sicurezza sono diffuse attraverso l’esperienza del personale e il coordinamento operativo tra i membri del team.<br/><br/>Non è ancora formalizzato un programma strutturato di formazione e sensibilizzazione sulla sicurezza delle informazioni.<br/><br/>L’organizzazione prevede di introdurre, in modo proporzionato alla propria dimensione, attività di awareness e formazione, che potranno includere:<br/><br/>condivisione delle buone pratiche di sicurezza<br/>formazione sui principali rischi informatici<br/>indicazioni sull’utilizzo corretto degli strumenti e delle informazioni<br/>aggiornamenti periodici sulle politiche di sicurezza</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/">PR05.1 - Gestione del Personale</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento sull’utilizzo degli strumenti aziendali</a><br/>Lista ClickUp «Consapevolezza e formazione»<br/><a href="../../7_GESTIONE%20RISORSE/MDPR06.1.C%20-%20Piano%20della%20formazione_%5Baaaa%5D/">MDPR06.1.C - Piano della formazione annuale</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Human_resource_security<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Gestione Risorse</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-6-4">
<summary><strong>6.4</strong> Processo disciplinare <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Processo disciplinare<br/>(Disciplinary process)<br><em>A disciplinary process should be formalized and communicated to take actions against personnel and other relevant interested parties who have committed an information security policy violation.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Le violazioni delle regole di sicurezza da parte di personale e collaboratori sono gestite con il processo descritto in <a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01</a> §11: segnalazione, messa in sicurezza, valutazione della Direzione, sanzioni secondo il codice disciplinare del contratto collettivo (art. 7 L. 300/1970) per i dipendenti e misure contrattuali per collaboratori e fornitori. Il processo è comunicato con la presa visione di <a href="../../7_GESTIONE%20RISORSE/ALPR05.1.H%20-%20Documenti%20per%20il%20personale/">ALPR05.1.H</a> e registrato in <a href="../../7_GESTIONE%20RISORSE/MDPR05.1.H%20-%20Processo%20Disciplinare/">MDPR05.1.H</a>.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento sull’utilizzo degli strumenti aziendali</a><br/><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.H%20-%20Processo%20Disciplinare/">MDPR05.1.H - Processo Disciplinare</a><br/><a href="../../7_GESTIONE%20RISORSE/ALPR05.1.H%20-%20Documenti%20per%20il%20personale/">ALPR05.1.H - Documenti per il personale</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect #Respond<br>Capacità operative: #Human_resource_security<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Gestione Risorse</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-6-5">
<summary><strong>6.5</strong> Responsabilità dopo la cessazione o variazione del rapporto di lavoro <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Responsabilità dopo la cessazione o variazione del rapporto di lavoro<br/>(Responsibilities after termination or change of employment)<br><em>Information security responsibilities and duties that remain valid after termination or change of employment should be defined, enforced and communicated to relevant personnel and other interested parties.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Obbligo contrattuale, Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce le responsabilità relative alla sicurezza delle informazioni in caso di cessazione o variazione del rapporto di lavoro o collaborazione.<br/><br/>In particolare, sono previste le seguenti attività :<br/><br/>revoca o modifica degli accessi ai sistemi e alle informazioni<br/>aggiornamento delle autorizzazioni in funzione del nuovo ruolo<br/>cessazione dell’accesso agli strumenti e alle piattaforme aziendali<br/>mantenimento degli obblighi di riservatezza anche dopo la cessazione del rapporto<br/><br/>Tali attività sono gestite attraverso:<br/><br/>controllo centralizzato degli accessi ai sistemi e ai servizi cloud<br/>gestione degli account e delle autorizzazioni<br/>accordi contrattuali e accordi di riservatezza (NDA)<br/><br/>La supervisione è affidata alla direzione e ai responsabili dei processi coinvolti.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/">PR05.1 - Gestione del Personale</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento sull’utilizzo degli strumenti aziendali</a><br/><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.L%20-%20Checklist%20documenti%20per%20uscita%20personale/">MDPR05.1.L - Checklist Documenti per Uscita Personale</a><br/><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze/">MDPR05.1.V - Modulo_consegna_riconsegna_HW_utenze</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Human_resource_security <br/>#Asset_management<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Gestione Risorse</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-6-6">
<summary><strong>6.6</strong> Accordi di riservatezza o di non divulgazione <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Accordi di riservatezza o di non divulgazione<br/>( Confidentiality or non-disclosure agreements)<br><em>Confidentiality or non-disclosure agreements reflecting the organization’s needs for the protection of information should be identified, documented, regularly reviewed and signed by personnel and other relevant interested parties.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce e tutela la riservatezza delle informazioni attraverso accordi di non divulgazione e clausole contrattuali applicabili ai rapporti con clienti, collaboratori e fornitori.<br/><br/>In particolare, sono previsti:<br/><br/>obblighi di riservatezza nei contratti e negli accordi con i clienti<br/>accordi di non divulgazione (NDA) con collaboratori e partner, ove applicabile<br/>limitazione dell’accesso alle informazioni in base al ruolo e alle necessità operative<br/><br/>La protezione delle informazioni è inoltre supportata da:<br/><br/>utilizzo di strumenti e piattaforme con controllo degli accessi<br/>gestione centralizzata delle informazioni aziendali e dei dati dei clienti<br/>supervisione da parte della direzione e dei responsabili dei processi<br/><br/>L’organizzazione mantiene un approccio proporzionato alla propria dimensione e alla natura delle attività svolte.</td></tr>
<tr><th>Riferimenti documentali</th><td>Contratti<br/><a href="../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/">PR05.1 - Gestione del Personale</a><br/><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze/">MDPR05.1.V - Modulo_consegna_riconsegna_HW_utenze</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Human_resource_security <br/>#Information_protection <br/>#Supplier_relationships<br>Domini di sicurezza: #Governance_ and_Ecosystem<br>Processi: #Gestione Risorse<br/>#Gestione Fornitori</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-6-7">
<summary><strong>6.7</strong> Lavoro remoto <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Lavoro remoto<br/>(Remote working)<br><em>Security measures should be implemented when personnel are working remotely to protect information accessed, processed or stored outside the organization’s premises.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Obbligo contrattuale, Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce le attività di lavoro remoto garantendo un adeguato livello di sicurezza delle informazioni.<br/><br/>Le attività operative sono svolte prevalentemente tramite strumenti e piattaforme cloud centralizzate, che consentono l’accesso controllato alle informazioni indipendentemente dalla posizione fisica.<br/><br/>La sicurezza del lavoro remoto è garantita attraverso:<br/><br/>utilizzo di servizi e piattaforme cloud con autenticazione e controllo degli accessi<br/>accesso alle informazioni limitato in base al ruolo e alle necessità operative<br/>utilizzo di dispositivi personali o aziendali con accesso controllato ai sistemi<br/>gestione centralizzata dei dati, evitando la memorizzazione locale non controllata<br/><br/>La supervisione delle attività è affidata alla direzione e ai responsabili dei processi coinvolti.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a><br/><a href="../../7_GESTIONE%20RISORSE/ALPR05.1.E%20-%20Accordo%20Lavoro%20Agile/">ALPR05.1.E - Accordo individuale lavoro agile</a><br/><a href="../../7_GESTIONE%20RISORSE/ALPR05.1.F%20-%20Informativa%20Lavoro%20Agile/">ALPR05.1.F - Informativa sulla salute e sicurezza nel lavoro agile</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Asset_management <br/>#Information_protection <br/>#Physical_security <br/>#System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Gestione Risorse</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-6-8">
<summary><strong>6.8</strong> Segnalazione degli eventi di sicurezza delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Segnalazione degli eventi di sicurezza delle informazioni<br/>(Information security event reporting)<br><em>The organization should provide a mechanism for personnel to report observed or suspected information security events through appropriate channels in a timely manner.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione prevede modalità per la segnalazione di eventi o anomalie relative alla sicurezza delle informazioni.<br/><br/>Il personale e i collaboratori possono segnalare eventi sospetti o problematiche di sicurezza attraverso i canali di comunicazione aziendali utilizzati nelle attività operative (es. strumenti collaborativi, email, comunicazione diretta).<br/><br/>Le segnalazioni vengono gestite dalla direzione e dai responsabili dei processi, che valutano l’evento e definiscono eventuali azioni correttive.<br/><br/>L’organizzazione mantiene un approccio proporzionato alla propria dimensione, garantendo che le segnalazioni possano essere effettuate in modo tempestivo e senza ostacoli operativi.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/">PR27.1 - Gestione Incidenti e Data Breach</a><br/><a href="../../A_EVENTI%20%26%20INCIDENTI/ALPR27.1.A%20-%20Notifica%20Data%20Breach%20all%E2%80%99interessato/">ALPR27.1.A - Notifica Data Breach all'interessato</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Detective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Detect<br>Capacità operative: #Information_security_event_management<br>Domini di sicurezza: #Defence<br>Processi: #Eventi e Incidenti di Sicurezza</td></tr>
</table>
</details>

### 7. Controlli fisici (Physical controls)

<details class="soa-ctrl" id="c-7-1">
<summary><strong>7.1</strong> Perimetri di sicurezza fisica <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Perimetri di sicurezza fisica<br/>(Physical security perimeters)<br><em>Security perimeters should be defined and used to protect areas that contain information and other associated assets.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (24/11/2026):</strong> manca la pianta della sede con il perimetro (ALPR18.1.A). Prevista entro il 15/12/2026 (azione T35 del piano di trattamento MDPR33.1.B).<br/><br/>L’organizzazione definisce e mantiene un perimetro di sicurezza fisica per proteggere le aree in cui sono presenti informazioni e asset aziendali.<br/><br/>Le attività operative sono svolte presso sedi e uffici con accesso controllato, in cui l’ingresso è limitato al personale autorizzato.<br/><br/>La protezione fisica è garantita attraverso:<br/><br/>accesso agli uffici controllato tramite chiavi o sistemi equivalenti<br/>presenza di aree operative destinate alle attività aziendali<br/>supervisione degli accessi da parte del personale autorizzato<br/><br/>L’organizzazione adotta un approccio proporzionato alla propria dimensione e alla natura delle attività svolte, in cui la maggior parte delle informazioni è gestita tramite sistemi digitali e piattaforme cloud.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a><br/><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/ALPR18.1.A%20-%20Piantina%20accessi.pptx">ALPR18.1.A - Piantina accessi</a><br/><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Fisica ed Ambientale</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-2">
<summary><strong>7.2</strong> Accessi fisici <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Accessi fisici<br/>(Physical entry)<br><em>Secure areas should be protected by appropriate entry controls and access points.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce la necessità di definire perimetri di sicurezza fisica per la protezione delle aree in cui sono presenti informazioni e asset aziendali.<br/><br/>Attualmente le attività operative sono svolte presso sedi e uffici con accesso limitato al personale autorizzato, e la protezione fisica è garantita attraverso:<br/><br/>accesso agli uffici tramite chiavi o sistemi equivalenti<br/>presenza di aree operative dedicate<br/>controllo informale degli accessi da parte del personale<br/><br/>Non è ancora formalizzata una gestione strutturata dei perimetri di sicurezza fisica e dei controlli di accesso.<br/><br/>L’organizzazione prevede di definire e implementare misure proporzionate alla propria dimensione, tra cui:<br/><br/>identificazione delle aree fisiche rilevanti per la sicurezza delle informazioni<br/>definizione delle modalità di accesso agli uffici<br/>introduzione di regole per la gestione degli accessi da parte di personale e visitatori</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a><br/><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/ALPR18.1.A%20-%20Piantina%20accessi.pptx">ALPR18.1.A - Piantina accessi</a><br/><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/MDPR18.1.D%20-%20Registri%20interventi%20ambientali/">MDPR18.1.D - Registro Interventi Ambientali</a><br/><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.U%20-%20Gestione%20chiavi/">MDPR05.1.U - Gestione chiavi</a><br/><a href="../../7_GESTIONE%20RISORSE/MDPR05.1.U%20-%20Gestione%20chiavi/">MDPR05.1.U - Gestione Chiavi</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security <br/>#Identity_and_Access_Management<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Fisica ed Ambientale</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-3">
<summary><strong>7.3</strong> Sicurezza degli uffici, stanze e strutture <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza degli uffici, stanze e strutture<br/>(Securing offices, rooms and facilities)<br><em>Physical security for offices, rooms and facilities should be designed and implemented.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce la necessità di garantire la sicurezza fisica degli uffici, delle stanze e delle strutture in cui vengono svolte le attività operative.<br/><br/>Le attività sono attualmente svolte in ambienti fisici dedicati, con accesso limitato al personale autorizzato.<br/><br/>La protezione fisica delle aree è attualmente garantita attraverso:<br/><br/>accesso agli uffici tramite chiavi o sistemi equivalenti<br/>utilizzo di spazi operativi dedicati alle attività aziendali<br/>supervisione informale degli accessi<br/><br/>Non sono ancora state definite e formalizzate misure strutturate per la protezione delle diverse aree e per la gestione dei livelli di accesso.<br/><br/>L’organizzazione prevede di definire misure proporzionate alla propria dimensione, che potranno includere:<br/><br/>identificazione delle aree con diversi livelli di criticità <br/>definizione delle modalità di accesso alle stanze e agli ambienti operativi<br/>introduzione di regole per la protezione degli spazi e degli asset presenti</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security <br/>#Asset_management<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Fisica ed Ambientale</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-4">
<summary><strong>7.4</strong> Monitoraggio della sicurezza fisica <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Monitoraggio della sicurezza fisica<br/>(Physical security monitoring)<br><em>Premises should be continuously monitored for unauthorized physical access.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce l’importanza del monitoraggio della sicurezza fisica per la rilevazione di accessi non autorizzati alle aree in cui sono presenti asset e informazioni.<br/><br/>Attualmente, il monitoraggio degli accessi fisici è limitato a forme di controllo informale basate sulla presenza del personale e sulla supervisione diretta degli ambienti operativi.<br/><br/>Non sono presenti sistemi strutturati di monitoraggio fisico quali sistemi di videosorveglianza, controllo accessi o sistemi di allarme.<br/><br/>L’organizzazione prevede di valutare l’introduzione di misure proporzionate alla propria dimensione e al livello di rischio, che potranno includere:<br/><br/>definizione di modalità di monitoraggio degli accessi agli uffici<br/>eventuale introduzione di strumenti di controllo degli accessi<br/>definizione di responsabilità per la supervisione degli ambienti fisici</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Detective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect <br/>#Detect<br>Capacità operative: #Physical_security<br>Domini di sicurezza: #Protection <br/>#Defence<br>Processi: #Sicurezza Fisica ed Ambientale</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-5">
<summary><strong>7.5</strong> Protezione dalle minacce fisiche e ambientali <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Protezione dalle minacce fisiche e ambientali<br/>(Protecting against physical and environmental threats)<br><em>Protection against physical and environmental threats, such as natural disasters and other intentional or unintentional physical threats to infrastructure should be designed and implemented.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione riconosce la necessità di proteggere gli asset e le informazioni da minacce fisiche e ambientali, quali eventi accidentali, interruzioni di alimentazione elettrica e altri fattori esterni.<br/><br/>Attualmente, la protezione da tali minacce è garantita principalmente attraverso:<br/><br/>utilizzo di ambienti di lavoro standard destinati ad attività d’ufficio<br/>gestione prevalente delle informazioni tramite piattaforme cloud, che riducono la dipendenza da infrastrutture fisiche locali<br/>presenza di dispositivi informatici con protezioni di base<br/><br/>Non sono presenti sistemi strutturati per la gestione delle minacce ambientali (es. gruppi di continuità , sistemi di monitoraggio ambientale o protezioni avanzate).<br/><br/>L’organizzazione prevede di valutare, in modo proporzionato alla propria dimensione e al livello di rischio, l’introduzione di misure adeguate, quali:<br/><br/>soluzioni per la continuità dell’alimentazione elettrica<br/>misure di protezione degli ambienti di lavoro<br/>valutazioni periodiche dei rischi fisici e ambientali</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Fisica ed Ambientale</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-6">
<summary><strong>7.6</strong> Lavorare in aree sicure <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Lavorare in aree sicure<br/>(Working in secure areas)<br><em>Security measures for working in secure areas should be designed and implemented.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Le aree in cui vengono trattate informazioni aziendali sono identificate come ambienti di lavoro ordinari (uffici e postazioni remote).<br/><br/>Sono adottate misure di sicurezza proporzionate al contesto operativo, tra cui:<br/><br/>controllo degli accessi fisici agli uffici<br/>utilizzo di dispositivi aziendali protetti<br/>politiche di clean desk e protezione delle informazioni visibili<br/>utilizzo di connessioni sicure per il lavoro remoto<br/><br/>Non sono presenti aree ad alta criticità (es. data center), pertanto le misure adottate sono proporzionate ai rischi identificati.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Fisica ed Ambientale</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-7">
<summary><strong>7.7</strong> Scrivania e schermo puliti <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Scrivania e schermo puliti<br/>(Clear desk and clear screen)<br><em>Clear desk rules for papers and removable storage media and clear screen rules for information processing facilities should be defined and appropriately enforced.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione definisce e adotta misure per garantire la protezione delle informazioni attraverso l’applicazione dei principi di ’scrivania pulita’ e ’schermo pulito’.<br/><br/>In particolare:<br/><br/>il personale è tenuto a non lasciare documenti contenenti informazioni sensibili incustoditi sulle postazioni di lavoro;<br/>i dispositivi devono essere bloccati automaticamente o manualmente in caso di assenza dell’utente;<br/>l’accesso alle informazioni è limitato alle sole persone autorizzate;<br/>l’utilizzo di dispositivi personali e ambienti condivisi è soggetto a misure di protezione adeguate.<br/><br/>Le regole operative sono formalizzate nelle policy interne di sicurezza e comunicate al personale.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Fisica ed Ambientale</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-8">
<summary><strong>7.8</strong> Disposizione delle apparecchiature e loro protezione <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Disposizione delle apparecchiature e loro protezione<br/>(Equipment siting and protection)<br><em>Equipment should be sited securely and protected.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione garantisce che le apparecchiature informatiche siano posizionate e utilizzate in modo sicuro, al fine di prevenire accessi non autorizzati, danneggiamenti o manomissioni.<br/><br/>In particolare:<br/><br/>i dispositivi aziendali sono assegnati agli utenti e utilizzati in ambienti controllati o adeguatamente protetti;<br/>l’accesso fisico alle postazioni di lavoro è limitato al personale autorizzato;<br/>i dispositivi portatili sono gestiti secondo regole di sicurezza definite (es. uso in mobilità , protezione durante il trasporto);<br/>vengono adottate misure di base per la protezione delle apparecchiature (es. blocco schermo, cifratura, gestione accessi);<br/>le apparecchiature critiche sono collocate in ambienti con adeguate misure di sicurezza fisica.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a><br/><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/ALPR18.1.A%20-%20Piantina%20accessi.pptx">ALPR18.1.A - Piantina accessi</a><br/><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security <br/>#Asset_management<br>Domini di sicurezza: #Protection<br>Processi: #Gestione Asset</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-9">
<summary><strong>7.9</strong> Sicurezza delle apparecchiature e degli asset all’esterno delle sedi <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza delle apparecchiature e degli asset all’esterno delle sedi<br/>(Security of assets off-premises)<br><em>Off-site assets should be protected.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione adotta misure per garantire la protezione delle apparecchiature e degli asset informativi utilizzati al di fuori delle sedi aziendali.<br/><br/>In particolare:<br/><br/>i dispositivi portatili sono assegnati agli utenti e protetti mediante autenticazione e cifratura;<br/>l’accesso alle informazioni aziendali da remoto avviene attraverso sistemi sicuri e controllati;<br/>il personale è istruito a proteggere i dispositivi durante l’utilizzo in ambienti esterni e a non lasciarli incustoditi;<br/>sono definite regole per il trasporto, l’utilizzo e la conservazione delle apparecchiature fuori sede;<br/>in caso di smarrimento o furto sono previste procedure di segnalazione e gestione dell’incidente.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a><br/><a href="../../7_GESTIONE%20RISORSE/ALPR05.1.E%20-%20Accordo%20Lavoro%20Agile/">ALPR05.1.E - Accordo Lavoro Agile</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security <br/>#Asset_management<br>Domini di sicurezza: #Protection<br>Processi: #Gestione Asset</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-10">
<summary><strong>7.10</strong> Supporti di memorizzazione <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Supporti di memorizzazione<br/>(Storage media)<br><em>Storage media should be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organization’s classification scheme and handling requirements.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione definisce e adotta misure per la gestione sicura dei supporti di memorizzazione lungo tutto il loro ciclo di vita, in conformità con le politiche di sicurezza delle informazioni.<br/><br/>In particolare:<br/><br/>l’utilizzo di dispositivi di memorizzazione rimovibili è regolamentato e limitato al personale autorizzato;<br/>i dati archiviati su supporti di memorizzazione sono protetti mediante misure di sicurezza adeguate (es. cifratura, controllo degli accessi);<br/>il trasporto dei supporti contenenti informazioni è effettuato in modo da prevenire accessi non autorizzati o smarrimenti;<br/>sono definite procedure per la cancellazione sicura o la distruzione dei supporti dismessi;<br/>l’uso di dispositivi personali è soggetto a specifiche regole di sicurezza.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security <br/>#Asset_management<br>Domini di sicurezza: #Protection<br>Processi: #Gestione Asset</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-11">
<summary><strong>7.11</strong> Infrastrutture di supporto <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Infrastrutture di supporto<br/>(Supporting utilities)<br><em>Information processing facilities should be protected from power failures and other disruptions caused by failures in supporting utilities.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione adotta misure proporzionate per la protezione delle infrastrutture di supporto ai sistemi informativi, al fine di ridurre i rischi derivanti da interruzioni o malfunzionamenti dei servizi ausiliari.<br/><br/>In particolare:<br/><br/>i servizi IT critici sono prevalentemente erogati tramite fornitori cloud che garantiscono adeguate misure di continuità operativa;<br/>le postazioni di lavoro sono dotate di misure di base per la protezione da interruzioni improvvise (es. gestione corretta dello spegnimento e backup automatici);<br/>l’organizzazione considera i rischi legati a alimentazione, temperatura e condizioni ambientali nei processi di gestione dei rischi;<br/>sono adottate misure organizzative per la gestione degli incidenti legati a indisponibilità dei servizi.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Detective<br>Proprietà di sicurezza: #Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect <br/>#Detect<br>Capacità operative: #Physical_security<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Fisica ed Ambientale</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-12">
<summary><strong>7.12</strong> Sicurezza dei cablaggi <span class="soa-stato">Applicabile: No · Attuato: —</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza dei cablaggi<br/>(Cabling security)<br><em>Cables carrying power, data or supporting information services should be protected from interception, interference or damage.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>No / —</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice</td></tr>
<tr><th>Motivo di esclusione</th><td>Il controllo è applicabile ma non applicato in quanto l’organizzazione non gestisce infrastrutture fisiche complesse o ambienti con cablaggio strutturato critico.<br/><br/>I sistemi informativi sono principalmente erogati tramite fornitori cloud e le postazioni di lavoro utilizzano infrastrutture standard (uffici o ambienti domestici) non soggette a requisiti specifici di protezione dei cablaggi.<br/><br/>Eventuali rischi residui legati ai cablaggi sono considerati trascurabili rispetto al contesto operativo e gestiti indirettamente attraverso misure di sicurezza generali e l’utilizzo di servizi esternalizzati.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality #Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Fisica ed Ambientale</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-13">
<summary><strong>7.13</strong> Manutenzione delle apparecchiature <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Manutenzione delle apparecchiature<br/>(Equipment maintenance)<br><em>Equipment should be maintained correctly to ensure availability, integrity and confidentiality of information.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Le apparecchiature utilizzate dall’organizzazione (principalmente dispositivi informatici quali laptop e periferiche) sono gestite e mantenute per garantire la continuità operativa e la sicurezza delle informazioni.<br/><br/>Sono adottate misure proporzionate al contesto operativo, tra cui:<br/><br/>aggiornamento periodico dei sistemi operativi e software<br/>sostituzione dei dispositivi obsoleti o non più adeguati<br/>utilizzo di strumenti di protezione (es. antivirus, cifratura, gestione accessi)<br/>backup dei dati critici<br/><br/>Non sono presenti infrastrutture complesse o apparati soggetti a manutenzione tecnica avanzata; le misure adottate sono pertanto proporzionate ai rischi identificati.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security <br/>#Asset_management<br>Domini di sicurezza: #Protection <br/>#Resilience<br>Processi: #Gestione Asset</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-7-14">
<summary><strong>7.14</strong> Dismissione sicura o riutilizzo delle apparecchiature <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Dismissione sicura o riutilizzo delle apparecchiature<br/>(Secure disposal or re-use of equipment)<br><em>Items of equipment containing storage media should be verified to ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal or re-use.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Le apparecchiature contenenti dati aziendali, al termine del loro ciclo di vita, sono gestite in modo da prevenire accessi non autorizzati alle informazioni.<br/><br/>Prima della dismissione o del riutilizzo, i dispositivi di memorizzazione sono sottoposti a cancellazione sicura dei dati o distruzione fisica, ove necessario.<br/><br/>Le attività sono svolte tramite:<br/><br/>reset dei dispositivi ai parametri di fabbrica<br/>cancellazione sicura dei dati<br/>eventuale distruzione dei supporti non più utilizzabili<br/><br/>Le misure adottate sono proporzionate alla tipologia di dispositivi utilizzati e ai rischi identificati.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Physical_security <br/>#Asset_management<br>Domini di sicurezza: #Protection<br>Processi: #Gestione Asset</td></tr>
</table>
</details>

### 8. Controlli tecnologici (Technological controls)

<details class="soa-ctrl" id="c-8-1">
<summary><strong>8.1</strong> Dispostivi finali degli utenti <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Dispostivi finali degli utenti<br/>(User endpoint devices)<br><em>Information stored on, processed by or accessible via user endpoint devices should be protected.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>I dispositivi finali utilizzati dagli utenti (laptop, smartphone e altri endpoint) sono configurati e gestiti per garantire la protezione delle informazioni trattate.<br/><br/>In particolare sono adottate le seguenti misure:<br/><br/>utilizzo di autenticazione per l’accesso ai dispositivi e ai servizi<br/>configurazione di timeout e blocco automatico delle sessioni inattive<br/>utilizzo di connessioni sicure (VPN o protocolli cifrati) per l’accesso a sistemi aziendali<br/>limitazione e controllo dell’uso di dispositivi di memorizzazione removibili<br/>aggiornamento periodico dei sistemi operativi e delle applicazioni<br/><br/>Le misure adottate sono proporzionate al contesto operativo e ai rischi identificati.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a><br/><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1 - Gestione Sicurezza Fisica e Ambientale</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Asset_management <br/>#Information_protection<br>Domini di sicurezza: #Protection<br>Processi: #Gestione Asset</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-2">
<summary><strong>8.2</strong> Diritti di accesso privilegiato <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Diritti di accesso privilegiato<br/>(Privileged access rights)<br><em>The allocation and use of privileged access rights should be restricted and managed.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’assegnazione e l’utilizzo dei diritti di accesso privilegiato sono limitati e controllati.<br/><br/>In particolare:<br/><br/>i privilegi amministrativi sono assegnati solo quando necessario e secondo il principio del minimo privilegio<br/>gli account privilegiati sono separati, ove possibile, dagli account standard<br/>l’accesso ai sistemi critici è protetto da meccanismi di autenticazione adeguati (es. password robuste e, ove disponibile, autenticazione a più fattori)<br/>le credenziali privilegiate sono gestite in modo sicuro e non condivise<br/>l’elenco degli accessi privilegiati viene mantenuto e periodicamente verificato<br/><br/>Le modalità di gestione sono proporzionate alla dimensione e complessità dell’organizzazione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Identity_and_ access_management<br>Domini di sicurezza: #Protection<br>Processi: #Controllo Accessi</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-3">
<summary><strong>8.3</strong> Restrizione degli accessi alle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Restrizione degli accessi alle informazioni<br/>(Information access restriction)<br><em>Access to information and other associated assets should be restricted in accordance with the established topic-specific policy on access control.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (23/11/2026):</strong> in ERA nessuna contromisura registrata sugli asset collegati.<br/><br/>L’accesso alle informazioni e agli asset informativi è limitato in base alle esigenze operative e al principio del minimo privilegio.<br/><br/>In particolare:<br/><br/>l’accesso ai dati è concesso solo agli utenti autorizzati<br/>le informazioni sono condivise in modo controllato, evitando accessi non necessari<br/>le risorse informative sono organizzate per limitare la visibilità ai soli soggetti interessati<br/>gli accessi vengono rivisti periodicamente in funzione delle necessità operative<br/><br/>Le modalità di controllo sono proporzionate alla dimensione e complessità dell’organizzazione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Identity_and_ access_management<br>Domini di sicurezza: #Protection<br>Processi: #Controllo Accessi</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-4">
<summary><strong>8.4</strong> Controllo degli accessi al codice sorgente dei programmi <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Controllo degli accessi al codice sorgente dei programmi<br/>(Access to source code)<br><em>Read and write access to source code, development tools and software libraries should be appropriately managed.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’accesso al codice sorgente dei programmi è limitato e controllato per prevenire accessi non autorizzati o modifiche non consentite.<br/><br/>In particolare:<br/><br/>il codice sorgente è accessibile solo al personale autorizzato<br/>i repository o sistemi di archiviazione del codice sono protetti da credenziali di accesso adeguate<br/>ove applicabile, vengono utilizzati sistemi di versionamento (es. Git) per tracciare le modifiche<br/>l’accesso al codice è concesso in base alle esigenze operative e al principio del minimo privilegio<br/><br/>Le modalità di gestione sono proporzionate alla dimensione e complessità dell’organizzazione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Identity_ and_access_ management #Application_security <br/>#Secure_configuration<br>Domini di sicurezza: #Protection<br>Processi: #Controllo Accessi</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-5">
<summary><strong>8.5</strong> Autenticazione sicura <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Autenticazione sicura<br/>(Secure authentication)<br><em>Secure authentication technologies and procedures should be implemented based on information access restrictions and the topic-specific policy on access control.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (23/11/2026):</strong> verifica in due passaggi obbligatoria dal 24/11/2026 (azione T1 del piano di trattamento MDPR33.1.B).<br/><br/>I meccanismi di autenticazione sono implementati per garantire che l’accesso ai sistemi e alle informazioni sia consentito solo agli utenti autorizzati.<br/><br/>In particolare:<br/><br/>gli accessi sono protetti da credenziali individuali (username e password)<br/>le password rispettano requisiti minimi di sicurezza (complessità e lunghezza)<br/>ove disponibile, viene utilizzata l’autenticazione a più fattori (MFA)<br/>le credenziali non sono condivise tra utenti<br/>sono adottate misure per prevenire accessi non autorizzati<br/><br/>Le modalità di autenticazione sono proporzionate alla dimensione e complessità dell’organizzazione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Identity_and_ access_management<br>Domini di sicurezza: #Protection<br>Processi: #Controllo Accessi</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-6">
<summary><strong>8.6</strong> Gestione della capacità <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Gestione della capacità<br/>(Capacity management)<br><em>The use of resources should be monitored and adjusted in line with current and expected capacity requirements.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (24/11/2026):</strong> nessun controllo automatico delle risorse del server (disco, memoria, carico). Arriva con il monitoraggio dal server secondario, entro febbraio 2027 (azione T32 del piano di trattamento MDPR33.1.B).<br/><br/>Le risorse infrastrutturali e le capacità dei sistemi utilizzati per l’erogazione dei servizi sono monitorate e gestite al fine di garantire adeguate prestazioni e continuità operativa. Eventuali esigenze di incremento delle risorse vengono valutate e pianificate in funzione dell’evoluzione dei progetti e dei carichi di lavoro.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Detective<br>Proprietà di sicurezza: #Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Protect <br/>#Detect<br>Capacità operative: #Continuity<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Continuità operativa</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-7">
<summary><strong>8.7</strong> Protezione contro il malware <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Protezione contro il malware<br/>(Protection against malware)<br><em>Protection against malware should be implemented and supported by appropriate user awareness.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione adotta misure di protezione contro il malware sui dispositivi degli utenti, inclusi sistemi antivirus/antimalware aggiornati e configurati automaticamente.<br/><br/>Sono attivi meccanismi di aggiornamento automatico dei sistemi operativi e dei software utilizzati.<br/><br/>Vengono inoltre adottate misure di sensibilizzazione degli utenti rispetto ai rischi legati a phishing, download di file non sicuri e utilizzo improprio delle risorse informatiche.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Detective <br/>#Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect <br/>#Detect<br>Capacità operative: #System_and_ network_security #Information_protection<br>Domini di sicurezza: #Protection <br/>#Defence<br>Processi: #Sicurezza Sistemi e Reti</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-8">
<summary><strong>8.8</strong> Gestione delle vulnerabilità tecniche <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Gestione delle vulnerabilità tecniche<br/>(Management of technical vulnerabilities)<br><em>Information about technical vulnerabilities of information systems in use should be obtained, the organization’s exposure to such vulnerabilities should be evaluated and appropriate measures should be taken.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione gestisce le vulnerabilità tecniche attraverso l’adozione di aggiornamenti regolari dei sistemi operativi e dei software utilizzati.<br/><br/>Viene effettuato il monitoraggio delle vulnerabilità note tramite fonti pubbliche e aggiornamenti dei fornitori, e le patch di sicurezza vengono applicate tempestivamente compatibilmente con il contesto operativo.<br/><br/>Sono inoltre adottate misure per garantire che i sistemi e le applicazioni siano mantenuti aggiornati e configurati in modo sicuro.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche/">PR23.1 - Gestione delle Minacce e delle Vulnerabilità Tecniche</a><br/><a href="../../9.2_AUDIT%20INTERNO/PR11.1%20-%20Audit%20Interno/">PR11.1 - Audit Interno</a><br/><a href="../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/">MDPR11.1.A - Programma Audit (§6 verifiche tecniche)</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Protect<br>Capacità operative: #Threat_and_ vulnerability_management<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection <br/>#Defence<br>Processi: #Minacce e Vulnerabilità</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-9">
<summary><strong>8.9</strong> Gestione delle configurazioni sicure e dell’hardening <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Gestione delle configurazioni sicure e dell’hardening<br/>(Configuration management)<br><em>Configurations, including security configurations, of hardware, software, services and networks should be established, documented, implemented, monitored and reviewed.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (23/11/2026):</strong> in ERA nessuna contromisura registrata; è la vulnerabilità «mancato processo di gestione delle configurazioni» dei 5 asset a rischio 45. Diventa attuato con l'applicazione di PR32.1 e la rivalutazione in ERA.<br/><br/>L’organizzazione adotta configurazioni sicure per sistemi, dispositivi e applicazioni utilizzate, basandosi sulle impostazioni di sicurezza raccomandate dai fornitori.<br/><br/>Sono disabilitate funzionalità non necessarie e vengono applicate configurazioni standard per garantire un adeguato livello di sicurezza.<br/><br/>Le configurazioni vengono mantenute aggiornate e riviste nel tempo in funzione delle esigenze operative.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Secure_configuration<br>Domini di sicurezza: #Protection<br>Processi: #Configurazione Sicura</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-10">
<summary><strong>8.10</strong> Cancellazione delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Cancellazione delle informazioni<br/>(Information deletion)<br><em>Information stored in information systems, devices or in any other storage media should be deleted when no longer required.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Obbligo contrattuale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione prevede la cancellazione delle informazioni quando non più necessarie, in linea con le esigenze operative e normative.<br/><br/>I dati vengono eliminati dai sistemi informativi e dai supporti di memorizzazione attraverso le funzionalità standard disponibili, garantendo che non rimangano accessibili oltre il periodo di utilizzo previsto.<br/><br/>Sono inoltre adottate misure per la gestione e la cancellazione degli account e dei dati associati quando non più necessari.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/">PO15 - Classificazione delle Informazioni</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Information_protection <br/>#Legal_and_compliance<br>Domini di sicurezza: #Protection<br>Processi: #Classificazione e Protezione delle Informazioni</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-11">
<summary><strong>8.11</strong> Mascheramento e anonimizzazione dei dati <span class="soa-stato">Applicabile: No · Attuato: —</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Mascheramento e anonimizzazione dei dati<br/>(Data masking)<br><em>Data masking should be used in accordance with the organization’s topic-specific policy on access control and other related topic-specific policies, and business requirements, taking applicable legislation into consideration.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>No / —</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice</td></tr>
<tr><th>Motivo di esclusione</th><td>L’organizzazione non effettua trattamenti di dati personali in contesti che richiedano tecniche di mascheramento o anonimizzazione (es. ambienti di test, condivisione con terze parti o utilizzo per analisi esterne).<br/><br/>I dati sono utilizzati esclusivamente in contesti operativi controllati e non vengono esposti o riutilizzati in modalità tali da richiedere tali misure.</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Utilizzo di protocollo HTTPS per siti web e servizi aziendali</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Information_protection<br>Domini di sicurezza: #Protection<br>Processi: #Classificazione e Protezione delle Informazioni</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-12">
<summary><strong>8.12</strong> Prevenzione dalla perdita di dati <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Prevenzione dalla perdita di dati<br/>(Data leakage prevention)<br><em>Data leakage prevention measures should be applied to systems, networks and any other devices that process, store or transmit sensitive information.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione adotta misure per prevenire la perdita o la divulgazione non autorizzata dei dati, attraverso controlli sugli accessi, utilizzo di sistemi di backup e gestione controllata delle informazioni.<br/><br/>I dati sono protetti da accessi non autorizzati e da perdita accidentale mediante l’utilizzo di strumenti e procedure adeguate al contesto operativo.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni/">PO15 - Classificazione dell Informazioni</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Detective<br>Proprietà di sicurezza: #Confidentiality<br>Concetti cybersecurity: #Protect <br/>#Detect<br>Capacità operative: #Information_protection<br>Domini di sicurezza: #Protection<br>Processi: #Classificazione e Protezione delle Informazioni</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-13">
<summary><strong>8.13</strong> Backup delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Backup delle informazioni<br/>(Information backup)<br><em>Backup copies of information, software and systems should be maintained and regularly tested in accordance with the agreed topic-specific policy on backup.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Attuato dal 18/11/2026:</strong> backup settimanale dei volumi delle applicazioni, scaricato da un server secondario separato dal principale e conservato 3 settimane; copie cifrate; configurazione ricostruibile da Ansible; prima prova di ripristino riuscita il 18/11/2026 (MDPR21.1.A).<br/><br/>L’organizzazione effettua copie di backup delle informazioni rilevanti al fine di garantirne la disponibilità e il ripristino in caso di perdita o incidente.<br/><br/>I backup sono gestiti tramite strumenti cloud, con accesso controllato e adeguate misure di protezione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore/">PR21.1 - Gestione dei Backup e Restore</a><br/><a href="../../A_BACKUP%20%26%20RESTORE/MDPR21.1.A%20-%20Piano%20di%20Restore/">MDPR21.1.A - Piano di Restore</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Corrective<br>Proprietà di sicurezza: #Integrity <br/>#Availability<br>Concetti cybersecurity: #Recover<br>Capacità operative: #Continuity<br>Domini di sicurezza: #Protection<br>Processi: #Continuità operativa</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-14">
<summary><strong>8.14</strong> Ridondanza delle strutture di elaborazione delle informazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Ridondanza delle strutture di elaborazione delle informazioni<br/>(Redundancy of information processing facilities)<br><em>Information processing facilities should be implemented with redundancy sufficient to meet availability requirements.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Il livello di ridondanza è deciso in base ai requisiti di disponibilità definiti nella BIA. I servizi interni girano su un unico server principale (Aruba), senza ridondanza attiva: il fermo fino al tempo di ripristino previsto è accettato nella BIA. A copertura, il server secondario scarica ogni settimana le copie dei volumi e la configurazione è nel repository Ansible, così il server può essere ricostruito; la prova di ripristino del 18/11/2026 è riuscita.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/">PR28.1 - Gestione della continuità operativa</a><br/><a href="../../A_CONTINUITA_%20OPERATIVA/MDPR28.1.A%20-%20BIA_Business%20Impact%20Analysis%20%2827001%29/">MDPR28.1.A - Piani di Continuità Operativa</a><br/><a href="../../A_BACKUP%20%26%20RESTORE/MDPR21.1.A%20-%20Piano%20di%20Restore/">MDPR21.1.A - Piano di Restore</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Continuity <br/>#Asset_management<br>Domini di sicurezza: #Protection <br/>#Resilience<br>Processi: #Continuità operativa</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-15">
<summary><strong>8.15</strong> Logging <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Logging<br><em>Logs that record activities, exceptions, faults and other relevant events should be produced, stored, protected and analysed.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (23/11/2026):</strong> in ERA attuato solo su 4 dei 40 asset collegati.<br/><br/>L’organizzazione utilizza sistemi che registrano gli accessi e le attività rilevanti sugli strumenti informatici utilizzati.<br/><br/>I log sono gestiti automaticamente dai servizi adottati e consentono la tracciabilità delle operazioni effettuate, contribuendo alla sicurezza delle informazioni.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/><a href="../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/">MDPR11.1.A - Programma Audit (§6 verifiche tecniche)</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Detective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Detect<br>Capacità operative: #Information_security_event_management<br>Domini di sicurezza: #Protection <br/>#Defence<br>Processi: #Monitoraggio dei Sistemi e Logging</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-16">
<summary><strong>8.16</strong> Attività di monitoraggio <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Attività di monitoraggio<br/>(Monitoring activities)<br><em>Networks, systems and applications should be monitored for anomalous behaviour and appropriate actions taken to evaluate potential information security incidents.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (24/11/2026):</strong> nessun monitoraggio con avvisi sul server. È previsto un monitoraggio eseguito da un server secondario sul server principale, con avvisi a sicurezza@, entro febbraio 2027 (azione T32 del piano di trattamento MDPR33.1.B).<br/><br/>L’organizzazione adotta attività di monitoraggio dei sistemi e dei servizi digitali mediante gli strumenti di logging e supervisione messi a disposizione dalle piattaforme cloud e dalle soluzioni software utilizzate. Gli eventi rilevanti vengono registrati e analizzati al fine di individuare anomalie, problemi di sicurezza e malfunzionamenti, consentendo un intervento tempestivo.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Detective <br/>#Corrective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Detect <br/>#Respond<br>Capacità operative: #Information_security_event_management<br>Domini di sicurezza: #Defence<br>Processi: #Monitoraggio dei Sistemi e Logging</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-17">
<summary><strong>8.17</strong> Sincronizzazione degli orologi <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sincronizzazione degli orologi<br/>(Clock synchronization)<br><em>The clocks of information processing systems used by the organization should be synchronized to approved time sources.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>La sincronizzazione degli orologi è gestita automaticamente dai servizi cloud e dalle piattaforme utilizzate, senza necessità né possibilità di configurazioni dirette da parte dell’organizzazione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Detective<br>Proprietà di sicurezza: #Integrity<br>Concetti cybersecurity: #Protect <br/>#Detect<br>Capacità operative: #Information_security_event_management<br>Domini di sicurezza: #Protection <br/>#Defence<br>Processi: #Sicurezza Sistemi e Reti</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-18">
<summary><strong>8.18</strong> Uso di programmi di utilità privilegiati <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Uso di programmi di utilità privilegiati<br/>(Use of privileged utility programs)<br><em>The use of utility programs that can be capable of overriding system and application controls should be restricted and tightly controlled.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’uso di account e strumenti con privilegi elevati è limitato agli utenti autorizzati ed è gestito secondo il principio del minimo privilegio.<br/><br/>Gli accessi amministrativi sono concessi solo quando necessario per attività operative e vengono utilizzati in modo controllato, evitando l’utilizzo per attività quotidiane.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../7_GESTIONE%20RISORSE/ALPR05.1.G%20-%20Lista%20software%20permessi/">ALPR05.1.G - Lista software permessi</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #System_and_network_security <br/>#Secure_configuration <br/>#Application_security<br>Domini di sicurezza: #Protection<br>Processi: #Configurazione Sicura</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-19">
<summary><strong>8.19</strong> Installazione del software sui sistemi di produzione <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Installazione del software sui sistemi di produzione<br/>(Installation of software on operational systems)<br><em>Procedures and measures should be implemented to securely manage software installation on operational systems.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’installazione di software sui sistemi utilizzati dall’organizzazione è limitata agli utenti autorizzati e viene effettuata in modo controllato.<br/><br/>Vengono utilizzati esclusivamente software provenienti da fonti affidabili e aggiornati regolarmente per ridurre i rischi di sicurezza.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a><br/><a href="../../7_GESTIONE%20RISORSE/ALPR05.1.G%20-%20Lista%20software%20permessi/">ALPR05.1.G - Lista software permessi</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Secure_configuration <br/>#Application_security<br>Domini di sicurezza: #Protection<br>Processi: #Configurazione Sicura</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-20">
<summary><strong>8.20</strong> Sicurezza delle reti <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza delle reti<br/>(Networks security)<br><em>Networks and network devices should be secured, managed and controlled to protect information in systems and applications.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’unica infrastruttura di rete presente è un router con password WPA2 con firewall integrato</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/>Schema ICT (documento riservato, fuori dal repository)</td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Detective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect <br/>#Detect<br>Capacità operative: #System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Sistemi e Reti</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-21">
<summary><strong>8.21</strong> Sicurezza dei servizi di rete <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sicurezza dei servizi di rete<br/>(Security of network services)<br><em>Security mechanisms, service levels and service requirements of network services should be identified, implemented and monitored.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>I servizi di rete utilizzati dall’organizzazione sono forniti da piattaforme cloud e SaaS che garantiscono adeguati livelli di sicurezza, inclusi autenticazione, autorizzazione e cifratura delle comunicazioni.<br/><br/>L’accesso è limitato agli utenti autorizzati e gestito</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/>Schema ICT (documento riservato, fuori dal repository)</td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality #Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Sistemi e Reti</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-22">
<summary><strong>8.22</strong> Segregazione delle reti <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Segregazione delle reti<br/>(Segregation of networks)<br><em>Groups of information services, users and information systems should be segregated in the organization’s networks.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td><strong>Non ancora attuato (24/11/2026):</strong> firewall attivo sul server con sole porte web e SSH consentite, ma la scansione esterna del 24/11/2026 ha rilevato servizi in container raggiungibili oltre le regole del firewall. Rischio accettato temporaneamente dall'Amministratore Unico il 24/11/2026, da mitigare con l'azione T31 del piano di trattamento MDPR33.1.B.<br/><br/>L’organizzazione utilizza infrastrutture e servizi cloud che prevedono la separazione logica degli ambienti e dei servizi esposti, adottando meccanismi di segregazione delle reti e di isolamento delle risorse messi a disposizione dai fornitori delle piattaforme utilizzate. L’accesso ai servizi è limitato agli utenti autorizzati e gestito mediante configurazioni dedicate e controlli di autenticazione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a><br/>Schema ICT (documento riservato, fuori dal repository)</td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Sistemi e Reti</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-23">
<summary><strong>8.23</strong> Filtro del web <span class="soa-stato">Applicabile: Sì · Attuato: No</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Filtro del web<br/>(Web filtering)<br><em>Access to external websites should be managed to reduce exposure to malicious content.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / No</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione implementa sistemi di filtraggio centralizzato del traffico web con filtro alla base del router verso i maggiori siti di contenuti malevoli.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01 - Regolamento di utilizzo degli strumenti informatici aziendali</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Sicurezza Sistemi e Reti</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-24">
<summary><strong>8.24</strong> Uso della crittografia <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Uso della crittografia<br/>(Use of cryptography)<br><em>Rules for the effective use of cryptography, including cryptographic key management, should be defined and implemented.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione utilizza meccanismi di crittografia per proteggere i dati durante la trasmissione, in particolare tramite l’utilizzo di protocolli sicuri (HTTPS/TLS) nei servizi cloud e SaaS adottati.<br/><br/>I dati sono protetti mediante le misure di sicurezza implementate dai fornitori dei servizi.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Secure_configuration<br>Domini di sicurezza: #Protection<br>Processi: #Configurazione Sicura</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-25">
<summary><strong>8.25</strong> Ciclo di vita dello sviluppo sicuro <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Ciclo di vita dello sviluppo sicuro<br/>(Secure development life cycle)<br><em>Rules for the secure development of software and systems should be established and applied.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>L’organizzazione adotta un processo strutturato per lo sviluppo del software, che include attività di progettazione, sviluppo, test e rilascio.<br/><br/>Il codice è gestito tramite sistemi di versionamento e le modifiche vengono controllate prima della messa in produzione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a><br/><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/ALPO25.A%20-%20Linee%20guida%20per%20lo%20sviluppo%20software/">ALPO25.A - Linee guida per lo sviluppo software</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Application_security <br/>#System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Progettazione e Sviluppo Sicuro</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-26">
<summary><strong>8.26</strong> Requisiti di sicurezza delle applicazioni <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Requisiti di sicurezza delle applicazioni<br/>(Application security requirements)<br><em>Information security requirements should be identified, specified and approved when developing or acquiring applications.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito legale, Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Durante lo sviluppo delle applicazioni vengono considerati i requisiti di sicurezza, inclusi autenticazione, controllo degli accessi e protezione dei dati. Nei progetti per i clienti i requisiti di sicurezza sono definiti dal cliente e recepiti nel progetto; per gli strumenti interni si applica PO25.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Application_security <br/>#System_and_network_security<br>Domini di sicurezza: #Protection <br/>#Defence<br>Processi: #Progettazione e Sviluppo Sicuro</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-27">
<summary><strong>8.27</strong> Principi di architettura e ingegnerizzazione dei sistemi sicuri <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Principi di architettura e ingegnerizzazione dei sistemi sicuri<br/>(Secure system architecture and engineering principles)<br><em>Principles for engineering secure systems should be established, documented, maintained and applied to any information system development activities.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Durante la progettazione dei sistemi e delle applicazioni vengono adottati principi di architettura sicura, inclusi isolamento dei componenti, gestione degli accessi, protezione dei dati e riduzione delle superfici di attacco.<br/><br/>Le soluzioni sono progettate considerando i rischi di sicurezza e applicando misure adeguate al contesto operativo.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Application_security <br/>#System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Progettazione e Sviluppo Sicuro</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-28">
<summary><strong>8.28</strong> Codifica sicura <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Codifica sicura<br/>(Secure coding)<br><em>Secure coding principles should be applied to software development.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Obbligo contrattuale, Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Durante lo sviluppo del software vengono adottate pratiche di codifica sicura, includendo la validazione degli input, la gestione corretta degli accessi e la protezione dei dati.<br/><br/>Il codice è sviluppato considerando i principali rischi di sicurezza applicativa in relazione al contesto operativo.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Application_security <br/>#System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Progettazione e Sviluppo Sicuro</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-29">
<summary><strong>8.29</strong> Test di sicurezza durante lo sviluppo e per l’accettazione <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Test di sicurezza durante lo sviluppo e per l’accettazione<br/>(Security testing in development and acceptance)<br><em>Security testing processes should be defined and implemented in the development life cycle.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Durante lo sviluppo delle applicazioni vengono eseguiti test funzionali e verifiche di sicurezza di base, al fine di identificare e correggere eventuali vulnerabilità prima del rilascio.<br/><br/>Le attività di test sono adeguate al contesto operativo e mirano a garantire un livello di sicurezza coerente con i rischi associati.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify<br>Capacità operative: #Application_security <br/>#Information_security_assurance #System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Progettazione e Sviluppo Sicuro</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-30">
<summary><strong>8.30</strong> Sviluppo affidato all’esterno <span class="soa-stato">Applicabile: No · Attuato: —</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Sviluppo affidato all’esterno<br/>(Outsourced development)<br><em>The organization should direct, monitor and review the activities related to outsourced system development.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>No / —</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice</td></tr>
<tr><th>Motivo di esclusione</th><td>Il controllo è applicabile ma non applicato in quanto lo sviluppo software non è affidato a fornitori esterni, ma gestito internamente. Pertanto, il controllo relativo alla gestione e supervisione dello sviluppo esternalizzato non risulta applicabile nel contesto aziendale.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive <br/>#Detective<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Identify <br/>#Protect <br/>#Detect<br>Capacità operative: #System_and_ network_security <br/>#Application_security <br/>#Supplier_relationships_security<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Progettazione e Sviluppo Sicuro</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-31">
<summary><strong>8.31</strong> Separazione degli ambienti di sviluppo, test e produzione <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Separazione degli ambienti di sviluppo, test e produzione<br/>(Separation of development, test and production environments)<br><em>Development, testing and production environments should be separated and secured.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Gli ambienti di sviluppo, test e produzione sono logicamente separati.<br/>L’accesso agli ambienti è controllato e limitato in base ai ruoli.<br/>Le modifiche vengono testate in ambienti dedicati prima del rilascio in produzione.<br/>Non è consentito effettuare sviluppo direttamente in ambiente di produzione.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a><br/><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1 - Gestione degli Accessi</a><br/><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1 - Gestione delle Configurazioni e dell'Infrastruttura IT</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Application_security <br/>#System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Progettazione e Sviluppo Sicuro</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-32">
<summary><strong>8.32</strong> Gestione dei cambiamenti <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Gestione dei cambiamenti<br/>(Change management)<br><em>Changes to information processing facilities and information systems should be subject to change management procedures.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice, Risultato analisi dei rischi</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Le modifiche a sistemi, configurazioni e applicazioni sono gestite in modo controllato.<br/>Prima dell’introduzione in produzione, i cambiamenti vengono valutati, testati e approvati.<br/>Le modifiche sono tracciate e documentate, con possibilità di ripristino in caso di problemi.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_CAMBIAMENTO/PR19.1%20-%20Gestione%20del%20Cambiamento/">PR19.1 - Gestione del Cambiamento</a><br/><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Application_security <br/>#System_and_network_security<br>Domini di sicurezza: #Protection<br>Processi: #Gestione del Cambiamento</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-33">
<summary><strong>8.33</strong> Dati di test <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Dati di test<br/>(Test information)<br><em>Test information should be appropriately selected, protected and managed.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>I dati utilizzati per test e sviluppo sono gestiti in modo da evitare l’utilizzo di dati reali sensibili.<br/>Quando necessario, i dati sono anonimizzati o sostituiti con dati fittizi.<br/>L’accesso ai dati di test è controllato e limitato al personale autorizzato.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro/">PO25 - Sviluppo Sicuro</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality<br/>#Integrity<br>Concetti cybersecurity: #Protect<br>Capacità operative: #Information_ protection<br>Domini di sicurezza: #Protection<br>Processi: #Progettazione e Sviluppo Sicuro</td></tr>
</table>
</details>

<details class="soa-ctrl" id="c-8-34">
<summary><strong>8.34</strong> Protezione dei sistemi informativi durante i test di audit <span class="soa-stato">Applicabile: Sì · Attuato: Sì</span></summary>
<table class="soa-scheda">
<tr><th>Controllo</th><td>Protezione dei sistemi informativi durante i test di audit<br/>(Protection of information systems during audit testing)<br><em>Audit tests and other assurance activities involving assessment of operational systems should be planned and agreed between the tester and appropriate management.</em></td></tr>
<tr><th>Set di controlli</th><td>ISO/IEC 27002</td></tr>
<tr><th>Applicabile / Attuato</th><td>Sì / Sì</td></tr>
<tr><th>Motivo di inclusione</th><td>Requisito business / best practice</td></tr>
<tr><th>Descrizione dell'attuazione</th><td>Le attività di test, audit e verifica sui sistemi informativi sono pianificate e controllate per evitare impatti negativi sull’operatività .<br/>Durante tali attività vengono adottate misure per proteggere i sistemi, i dati e le prestazioni dei servizi.<br/>Gli accessi per audit e test sono limitati, monitorati e autorizzati.</td></tr>
<tr><th>Riferimenti documentali</th><td><a href="../../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit/">MDPR11.1.A - Programma Audit (§6 verifiche tecniche)</a></td></tr>
<tr><th>Attributi ISO/IEC 27002</th><td>Tipo di controllo: #Preventive<br>Proprietà di sicurezza: #Confidentiality <br/>#Integrity <br/>#Availability<br>Concetti cybersecurity: #Protect<br>Capacità operative: #System_and_network_security #Information_protection<br>Domini di sicurezza: #Governance_ and_Ecosystem #Protection<br>Processi: #Valutazione delle Prestazioni</td></tr>
</table>
</details>

<script>
/* Apre il dettaglio del controllo quando si arriva da un link #c-x-y */
(function () {
  function apri() {
    var el = location.hash && document.getElementById(location.hash.slice(1));
    if (el && el.tagName === "DETAILS") { el.open = true; el.scrollIntoView(); }
  }
  window.addEventListener("hashchange", apri);
  document.addEventListener("DOMContentLoaded", apri);
  if (typeof document$ !== "undefined") { document$.subscribe(apri); }
})();
</script>
