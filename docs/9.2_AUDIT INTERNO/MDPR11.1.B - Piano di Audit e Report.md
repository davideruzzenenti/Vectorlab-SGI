# MDPR11.1.B - Piano di Audit e Report

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** | **Classificazione** |
| -------- | ---------- | --------------- | ----------- | ------------- | ------------------- |
| 0.0      | 24/04/2026 | Prima emissione (modello) | RSGI | Amministratore Unico | Interno |
| 0.1      | 04/11/2026 | Modello adattato a Vectorlab e allineato al programma MDPR11.1.A rev 0.3: una sola modalità, per funzione (tolta la modalità per processo); funzioni reali dell'organigramma al posto di «Area XXXX», PM, DPO e CISO separato; tolti i controlli ISO 27017/27018 (fuori dal campo di certificazione) e i controlli non applicabili da SoA (A.7.12, A.8.11, A.8.30); aggiunta la sezione dati dell'audit (obiettivi, campo, criteri, auditor); rilievi collegati alla lista ClickUp «Non conformità e miglioramento» (PR13.1) | RSGI | Da approvare | Interno |

Modulo previsto da *PR11.1 - Audit Interno* §2.6 (piano) e §2.7.1 (report).
Si compila una copia per ogni audit: prima dell'audit le sezioni 1 e 2
(piano, condiviso con le funzioni coinvolte), dopo l'audit le sezioni 3–5
(report). Le aree e i requisiti sono quelli del programma
*MDPR11.1.A - Programma Audit* §3: per gli audit degli anni 2027 e 2028
si tolgono le righe non previste in quell'anno.

## 1 Dati dell'audit

| Voce | Contenuto |
| --- | --- |
| N°/Anno | |
| Data/e | |
| Tipo | Audit interno di prima parte sul SGI (ISO 9001 + ISO/IEC 27001) |
| Obiettivi | Verificare che il SGI sia conforme ai requisiti delle norme e ai documenti interni, che sia attuato ed efficace (PR11.1 §2.1) |
| Campo | Campo di applicazione del SGI (PO02): «Progettazione, sviluppo software e consulenza in particolare in ambito deep tech»; unico sito di Piazza Borgo Pila 39/22, piano 8, 16129 Genova, più i servizi cloud nel campo |
| Criteri | ISO 9001 e UNI CEI EN ISO/IEC 27001:2024+A1:2024 secondo MDPR11.1.A §1; Annex A come da SoA in vigore; documenti del SGI; requisiti cogenti (MDPO29.C) e contrattuali |
| Metodo | Interviste, esame di documenti e registrazioni, verifica a campione negli strumenti (repository, ClickUp, Google Workspace, console cloud); checklist MDPR11.1.D (27001) e MDPR11.1.L (9001) |
| Responsabile dell'audit (auditor) | |
| Altri auditor / osservatori | |
| Referente Vectorlab | RSGI |

## 2 Piano

L'auditor non verifica il proprio lavoro (PR11.1 §2.1). Le aree di cui
RSGI o l'Amministratore Unico sono responsabili operativi sono verificate
da un auditor esterno (PR11.1 §2.4; MDPR11.1.A §4).

| Funzione / persone intervistate | Processo / tema | Requisiti | Sistema | Data / ora | Durata | Auditor |
| --- | --- | --- | --- | --- | --- | --- |
| Tutte le funzioni coinvolte | **Riunione di apertura** | — | SGI | | | |
| **Direzione** (Amministratore Unico) | Contesto e campo di applicazione | 4 | SGI | | | |
| | Leadership, politica, ruoli | 5; A.5.1, A.5.2, A.5.4 | SGI | | | |
| | Rischi e opportunità, obiettivi | 6.1, 6.2 | SGI | | | |
| | Risorse | 7.1 | SGI | | | |
| | Riesame della direzione | 9.3 | SGI | | | |
| | Miglioramento | 10 | SGI | | | |
| | Continuità operativa | A.5.29, A.5.30 | SGSI | | | |
| **CTO / CISO** (Amministratore Unico), con **IT esterno** | Pianificazione dei cambiamenti | 6.3; A.8.32 | SGI | | | |
| | Fornitori e servizi cloud | 8.4 (9001); A.5.19–A.5.23 | SGI | | | |
| | Controllo accessi e identità | A.5.15–A.5.18, A.8.2–A.8.5 | SGSI | | | |
| | Gestione degli asset | A.5.9–A.5.11, A.5.14, A.7.8–A.7.10, A.7.13, A.8.1 | SGSI | | | |
| | Configurazioni, patch, backup, crittografia | A.8.7–A.8.9, A.8.13, A.8.18, A.8.19, A.8.24 | SGSI | | | |
| | Capacità, continuità ICT, ridondanza | A.8.6, A.8.14 | SGSI | | | |
| | Sistemi e reti, monitoraggio e log | A.8.15, A.8.16, A.8.20–A.8.23 | SGSI | | | |
| | Minacce e vulnerabilità | A.5.7, A.8.8 | SGSI | | | |
| | Incidenti di sicurezza | A.5.24–A.5.28, A.6.8 | SGSI | | | |
| **RSGI** | Contesto, parti interessate | 4 | SGI | | | |
| | Valutazione e trattamento dei rischi di sicurezza | 6.1.2, 6.1.3, 8.1–8.3 (27001) | SGSI | | | |
| | Comunicazione e informazioni documentate | 7.4, 7.5; A.5.37 | SGI | | | |
| | Governance della sicurezza | A.5.5, A.5.6 | SGSI | | | |
| | Monitoraggio, audit interno | 9.1, 9.2; A.5.35, A.5.36, A.8.34 | SGI | | | |
| | Non conformità e miglioramento | 10 | SGI | | | |
| | Classificazione e protezione delle informazioni | A.5.12, A.5.13, A.5.33, A.5.34, A.8.10, A.8.12 | SGSI | | | |
| | Conformità legale e contrattuale | A.5.31, A.5.32 | SGSI | | | |
| **Business Development** | Gestione del cliente e offerte | 8.2 (9001) | SGQ | | | |
| **Digital** (Digital Technical Manager e sviluppatori a campione) | Progettazione e sviluppo del software | 8.3 (9001); A.5.8, A.8.25–A.8.29, A.8.31, A.8.33 | SGI | | | |
| | Erogazione, rilascio, output non conformi | 8.5–8.7 (9001) | SGQ | | | |
| **Amministrazione** | Fornitori: selezione, valutazione, accordi | 8.4 (9001); A.5.19–A.5.22, A.6.6 | SGI | | | |
| **HR** | Risorse, competenze, consapevolezza | 7.1–7.3 | SGI | | | |
| | Persone prima, durante e dopo il rapporto | A.5.10, A.6.1–A.6.7 | SGSI | | | |
| | Sicurezza fisica e ambientale (con CTO) | A.7.1–A.7.7 | SGSI | | | |
| **Referente Privacy** | Privacy e dati personali | A.5.34 | SGSI | | | |
| | Data breach (con CTO) | A.5.24–A.5.28 | SGSI | | | |
| | Requisiti cogenti | A.5.31 | SGSI | | | |
| Tutte le funzioni coinvolte | **Riunione di chiusura** | — | SGI | | | |

I numeri senza prefisso sono punti dei capitoli 4–10 comuni alle due
norme, salvo indicazione (9001) o (27001); i codici A.x.x sono controlli
dell'Annex A della ISO/IEC 27001.

## 3 Non conformità

Ogni rilievo si registra nella lista ClickUp «Non conformità e
miglioramento» con Origine = audit interno (PR13.1).

| N. | Requisito | Descrizione ed evidenza | Funzione | Task ClickUp |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## 4 Osservazioni e opportunità di miglioramento

| N. | Requisito | Descrizione | Funzione | Task ClickUp |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

## 5 Considerazioni finali

Conclusione sulla conformità ed efficacia del SGI, punti di forza, aree
da rafforzare, documenti di riferimento consultati.

&nbsp;

| | Nome | Data | Firma |
| --- | --- | --- | --- |
| Auditor | | | |
| RSGI | | | |
