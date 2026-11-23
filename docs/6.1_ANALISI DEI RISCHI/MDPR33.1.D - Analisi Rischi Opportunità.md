# MDPR33.1.D - Analisi Rischi Opportunità

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0 | 17/11/2026 | Emissione | RSGI | Da approvare |
| 0.1 | 23/11/2026 | Rimando a PR10.1 (ritirata) sostituito da MDPR10.1.A | RSGI | Da approvare |

Registro dei rischi e delle opportunità per la qualità del servizio e la
soddisfazione dei clienti (ISO 9001:2026, 6.1; [PR33.1](PR33.1%20-%20Processo%20Analisi%20del%20Rischio%20e%20Trattamento.md) «Rischi e
opportunità per la qualità»). I rischi per la sicurezza delle
informazioni sono valutati con ERA ([MDPR33.1.A](../B_REGISTRAZIONI/Analisi%20dei%20Rischi/2026/MDPR33.1.A%20-%20Report%20Analisi%20dei%20Rischi%20-%202026.md), [MDPR33.1.B](../B_REGISTRAZIONI/Analisi%20dei%20Rischi/2026/MDPR33.1.B%20-%20Piano%20di%20Trattamento%20dei%20Rischi%20-%202026.md)).

<span style="color:#B3392A">**Bozza del 17/11/2026 preparata da RSGI.**
Fattori, valutazioni G e V e azioni sono proposte da confermare con
l'Amministratore Unico prima del Riesame della Direzione.</span>

**Metodo.** Ri = G × V, con G (gravità) e V (probabilità) da 1 a 4.
Ri da 6 a 16: serve un'azione con responsabile, indicatore e data. Per
le opportunità: azione per coglierle. Rf = indice dopo l'azione; 1–4
basso, 6–8 medio, 9–16 alto.

## 1 Rischi

| # | Fattore (I/E) | Parti interessate | Rischio | G | V | Ri | Misure in essere | Azione | Resp. | Indicatore | Entro | Rf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | Concentrazione del fatturato su pochi clienti con commesse lunghe (E) | Clienti, Amministratore Unico | La perdita o la riduzione di un cliente principale riduce molto il lavoro | 4 | 2 | 8 | Rapporti consolidati | Sviluppo di nuovi clienti con la BU Ynsera e le altre BU; monitoraggio trimestrale del portafoglio | Business Development | GC2, GC3 | 31/12/2027 | 4 |
| R2 | Team piccolo e ruoli chiave concentrati in poche persone (I) | Clienti, personale | Assenza o uscita di una persona chiave blocca commesse o processi | 3 | 2 | 6 | Codice e documenti su strumenti aziendali ([REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md)) | Passaggio di consegne documentato ([PR05.1](../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale.md) §10); almeno due persone che conoscono ogni progetto | CTO | Progetti con almeno due persone informate | 30/06/2027 | 3 |
| R3 | Lavoro dentro gli ambienti e con le regole dei clienti (I/E) | Clienti | Requisiti del cliente (qualità, sicurezza, privacy) non chiariti all'avvio | 3 | 2 | 6 | Avvio commessa secondo [PR35.1](../8.2_PRODOTTI%20%26%20SERVIZI/PR35.1%20-%20Digital.md) | Checklist di avvio commessa con requisiti, strumenti e accessi concordati | PM | PS4 (reclami) | 31/03/2027 | 3 |
| R4 | Uso di strumenti di intelligenza artificiale nello sviluppo (I/E) | Clienti, Garante, legislatore (AI Act) | Dati o codice del cliente inseriti in servizi non autorizzati; obblighi AI Act | 3 | 2 | 6 | Strumenti autorizzati ([PR35.1](../8.2_PRODOTTI%20%26%20SERVIZI/PR35.1%20-%20Digital.md) §2.3); [REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) | Formazione annuale sull'uso dell'AI; verifica nel Riesame dei requisiti AI Act | CTO / RSGI | RU1 | 30/06/2027 | 3 |
| R6 | Dipendenza da fornitori cloud e dal server Aruba (E) | Clienti, personale | Interruzione dei servizi interni | 2 | 2 | 4 | BIA ([MDPR28.1.A](../A_CONTINUITA_%20OPERATIVA/MDPR28.1.A%20-%20BIA_Business%20Impact%20Analysis%20%2827001%29.md)); backup del server ([PR21.1](../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore.md)) | — | — | — | — | — |
| R7 | Soddisfazione dei clienti non misurata in modo sistematico (I) | Clienti | Problemi di qualità scoperti tardi | 3 | 3 | 9 | — | Questionario a fine commessa e annuale ([MDPR10.1.A](../9.1_MONITORAGGIO%20KPI/MDPR10.1.A%20-%20Tabella%20Indicatori.md), «Soddisfazione del cliente») | PM / RSGI | PS5 | 15/12/2026 | 3 |

## 2 Opportunità

| # | Fattore (I/E) | Parti interessate | Opportunità | Azione per coglierla | Resp. | Indicatore | Entro |
| --- | --- | --- | --- | --- | --- | --- | --- |
| O1 | Certificazione ISO 9001 e ISO/IEC 27001 (I) | Clienti, Pubblica Amministrazione | Accesso a clienti e gare che richiedono la certificazione (es. MePA) | Ottenere la certificazione; comunicarla ai clienti | Amministratore Unico | Certificazione ottenuta | 31/03/2027 |
| O2 | Collaborazioni di ricerca sull'intelligenza artificiale (E) | Enti di ricerca, clienti | Competenze e referenze in ambito deep tech | Valorizzare i progetti di ricerca nell'offerta commerciale | Business Development | GC2 | 31/12/2027 |
| O3 | Domanda di soluzioni di intelligenza artificiale per le imprese (E) | Clienti | Nuovi servizi e nuovi clienti | Offerta dedicata delle business unit | Business Development | GC2, GC3 | 31/12/2027 |

## 3 Riesame

Il registro si aggiorna una volta l'anno prima del Riesame della Direzione
e quando cambia il contesto ([PO02](../4_CONTESTO/PO02%20-%20Gestione%20del%20Contesto.md)). Le azioni rilevanti diventano
obiettivi ([MDPO03.A](../6.2_OBIETTIVI/MDPO03.A%20-%20Lista%20Obiettivi.md)) o azioni nella lista ClickUp «Non conformità e
miglioramento» ([PR13.1](../10_GESTIONE%20NON%20CONFORMITA_%20E%20MIGLIORAMENTO/PR13.1%20-%20Gestione%20delle%20Non%20Conformit%C3%A0%20e%20Azioni%20di%20Miglioramento.md)).
