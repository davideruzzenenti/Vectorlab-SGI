# MDPR10.1.A - Tabella Indicatori

## Cover

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** | **Classificazione** |
| -------- | ---------- | --------------- | ----------- | ------------- | ------------------- |
| 0.0 | 17/11/2026 | Emissione | RSGI | Da approvare | Interno |
| 0.1 | 23/11/2026 | Aggiunte le regole del monitoraggio e della soddisfazione del cliente, prima in PR10.1 (ritirata) | RSGI | Da approvare | Interno |

## Regole del monitoraggio

Cosa Vectorlab misura per capire se il Sistema di Gestione Integrato
funziona, chi raccoglie i dati, quando, e come i risultati portano ad
azioni. Vale per tutti i processi del SGI; gli indicatori sono pochi e
ognuno ha un responsabile: si misura solo ciò che serve a decidere.

### Responsabilità

| Ruolo | Compiti |
| --- | --- |
| Amministratore Unico | Approva indicatori, obiettivi e soglie; decide le azioni nel Riesame |
| RSGI | Tiene la Tabella Indicatori, raccoglie i valori dai responsabili, li analizza e li porta al Riesame |
| Responsabile di ogni indicatore | Fornisce il valore a ogni scadenza, con l'evidenza (colonna «Responsabile» della tabella) |
| PM | Manda il questionario di soddisfazione al cliente (vedi «Soddisfazione del cliente») |

### Gestione degli indicatori

Per ogni indicatore la tabella più sotto indica: cosa si misura e con quale formula, obiettivo, soglia di
accettabilità, frequenza, fonte dei dati e responsabile.

1. **Definizione.** RSGI propone gli indicatori, l'Amministratore Unico li
   approva. Ogni indicatore deve dare risultati ripetibili e confrontabili
   nel tempo, e avere una fonte dati che esiste davvero (registro, lista
   ClickUp, console di un servizio).
2. **Raccolta.** Alla scadenza indicata, il responsabile comunica il
   valore a RSGI, che lo registra nella tabella, nella colonna del semestre.
3. **Analisi.** RSGI confronta il valore con obiettivo e soglia:
   - sotto soglia: apre un'azione nella lista ClickUp «Non conformità e
     miglioramento» ([PR13.1](../10_GESTIONE%20NON%20CONFORMITA_%20E%20MIGLIORAMENTO/PR13.1%20-%20Gestione%20delle%20Non%20Conformit%C3%A0%20e%20Azioni%20di%20Miglioramento.md));
   - tra soglia e obiettivo: lo segnala nel Riesame.
4. **Riesame.** Una volta l'anno RSGI porta al Riesame della Direzione
   ([PR12.1](../9.3_RIESAME%20DIREZIONE/PR12.1%20-%20Riesame%20della%20Direzione.md)) l'andamento di tutti gli indicatori. L'Amministratore Unico
   decide azioni, nuovi obiettivi e indicatori da cambiare o togliere.

Gli obiettivi del Sistema di Gestione e il loro avanzamento sono in
[MDPO03.A](../6.2_OBIETTIVI/MDPO03.A%20-%20Lista%20Obiettivi.md); quando un obiettivo si misura con un indicatore, il rimando è
nella tabella più sotto.

### Soddisfazione del cliente

1. Il PM manda al cliente il questionario di soddisfazione (pagina web):
   - alla chiusura di ogni commessa;
   - una volta l'anno, a novembre, per i clienti con commesse
     continuative.
2. Le risposte arrivano a RSGI [DA CONFERMARE: dove le salva la pagina
   web, in preparazione da parte del System Administrator].
3. Ogni semestre RSGI riassume le risposte in [MDPR10.1.B](MDPR10.1.B%20%20-%20Analisi%20Soddisfazione%20Cliente.md) e aggiorna
   l'indicatore PS5. Un voto basso o un commento negativo si tratta come
   reclamo (indicatore PS4) e si registra nella lista ClickUp «Non
   conformità e miglioramento».

Contano come informazioni sulla soddisfazione anche reclami, complimenti
e richieste dei clienti ricevuti durante il lavoro: il PM li segnala a
RSGI.

### Verifiche tecniche

Le verifiche periodiche che producono dati per gli indicatori (prove di
ripristino, revisione degli accessi, operato degli amministratori di
sistema, scansioni delle vulnerabilità) sono pianificate in [MDPR11.1.A](../9.2_AUDIT%20INTERNO/MDPR11.1.A%20-%20Programma%20Audit.md) §6
e descritte nelle procedure di riferimento ([PR21.1](../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore.md), [PR16.1](../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md), [PR23.1](../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche.md),
[PR32.1](../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT.md)).

### Registrazioni

| Registrazione | Dove | Chi | Conservazione |
| --- | --- | --- | --- |
| Tabella Indicatori con i valori | Questo documento, repo SGI | RSGI | 3 anni |
| Risposte ai questionari e sintesi | [MDPR10.1.B](MDPR10.1.B%20%20-%20Analisi%20Soddisfazione%20Cliente.md); risposte [DA CONFERMARE] | RSGI | 3 anni |
| Azioni per indicatori sotto soglia | Lista ClickUp «Non conformità e miglioramento» | RSGI | 3 anni |
| Analisi annuale | Verbale del Riesame della Direzione | RSGI | 3 anni |

## Indicatori

Indicatori di monitoraggio del Sistema di Gestione Integrato. I
valori si registrano a ogni rilevazione nelle colonne del semestre e si
analizzano nel Riesame della Direzione ([PR12.1](../9.3_RIESAME%20DIREZIONE/PR12.1%20-%20Riesame%20della%20Direzione.md)). Ultimo aggiornamento:
GG/MM/AAAA.

**Bozza (16/11/2026): obiettivi, soglie, frequenze e responsabili da
confermare con Amministratore Unico e Amministrazione.** Per il 2026 AR2 è
non applicabile: il piano di trattamento non prevede azioni (rischi
accettati).

| ID | Requisito / Controllo | KPI | Formula | Valore I sem. | Valore II sem. | Obiettivo | Soglia di accettabilità | Frequenza | Fonte dei dati | Responsabile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PS5 | 9.1.2 (9001) | Soddisfazione del cliente | Media delle risposte al questionario di soddisfazione (scala 1–5) |  |  | ≥ 4 | ≥ 3 | A ogni fine commessa e una volta l'anno per i clienti continuativi; sintesi semestrale | Questionario web di soddisfazione (vedi «Soddisfazione del cliente»); sintesi in [MDPR10.1.B](MDPR10.1.B%20%20-%20Analisi%20Soddisfazione%20Cliente.md) | PM; sintesi RSGI |
| PS4 | 9.1.2 / 10.2 (9001) | Reclami clienti | Numero di reclami ricevuti dai clienti nell'anno |  |  | 0 | ≤ 2 | Semestrale | Task Prospect; lista ClickUp «Non conformità e miglioramento» | RSGI |
| GC2 | 8.2 (9001) | Efficacia del processo commerciale | Offerte accettate / offerte emesse nell'anno (%) |  |  | ≥ 30% | ≥ 20% | Annuale | Cartella offerte su Drive | Business Development |
| GC3 | 8.2 (9001) | Andamento del fatturato | Variazione del fatturato rispetto all'anno precedente (%) |  |  | +5% | ≥ 0% | Annuale | Bilancio di esercizio | Amministrazione |
| IN1 | A.5.24–5.27 | Incidenti di sicurezza critici | Numero di incidenti di sicurezza critici nell'anno |  |  | 0 | ≤ 1 | Semestrale | Registro incidenti ([PR27.1](../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach.md)) | CISO |
| IN4 | A.5.34 | Data breach | Numero di violazioni di dati personali nell'anno |  |  | 0 | 0 | Semestrale | Registro Data Breach [MDPR27.1.A](../A_EVENTI%20%26%20INCIDENTI/MDPR27.1.A%20-%20Registro%20Data%20Breach.md) | Referente Privacy |
| DA1 | A.5.18 | Revisione dei diritti di accesso | Numero di revisioni delle utenze nell'anno |  |  | 2 | 1 | Annuale | Task ClickUp della revisione semestrale ([PR16.1](../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md) §6) | RSGI |
| CN1 | A.8.1 / A.8.24 | Portatili cifrati | Portatili con disco cifrato / totale portatili (%) |  |  | 100% | ≥ 90% | Semestrale | Verifica sui portatili | CTO |
| SO3 | A.8.13 | Prove di ripristino | Ripristini riusciti / ripristini provati (%) |  |  | 100% | 100% | Annuale | Piano di Restore [MDPR21.1.A](../A_BACKUP%20%26%20RESTORE/MDPR21.1.A%20-%20Piano%20di%20Restore.md) | System Administrator |
| RF6 | A.5.20 | Accordi di riservatezza con i fornitori critici | Fornitori critici con NDA firmato / fornitori critici (%) |  |  | 100% | 100% | Annuale | Elenco fornitori qualificati [MDPR26.1.B](../A_FORNITORI/MDPR26.1.B%20-%20Elenco%20fornitori%20qualificati.md) | Amministrazione |
| PS1 | 10.1–10.3 | Azioni di miglioramento chiuse in tempo | Azioni chiuse entro la data prevista / azioni previste (%) |  |  | ≥ 80% | ≥ 60% | Semestrale | Lista ClickUp «Non conformità e miglioramento» | RSGI |
| PS3 | 10.2 | Rilievi chiusi in ritardo | Rilievi chiusi oltre la data prevista / totale rilievi (%) |  |  | ≤ 20% | ≤ 40% | Semestrale | Lista ClickUp «Non conformità e miglioramento» | RSGI |
| RU1 | 7.2 / 7.3; A.6.3 | Formazione sul sistema di gestione | Persone formate sul sistema di gestione / totale del personale (%) |  |  | 100% | ≥ 90% | Annuale | Prese visione e registri presenze | Risorse Umane |
| AR2 | 6.1.3 (27001) | Attuazione del piano di trattamento dei rischi | Azioni del piano completate entro i tempi / azioni previste (%) |  |  | 100% | ≥ 80% | Annuale | Piano di trattamento [MDPR33.1.B](../B_REGISTRAZIONI/Analisi%20dei%20Rischi/2026/MDPR33.1.B%20-%20Piano%20di%20Trattamento%20dei%20Rischi%20-%202026.md) | CISO |

## Riferimenti

- ISO 9001:2026 e ISO/IEC 27001:2022, 9.1 Monitoraggio, misurazione, analisi e valutazione; ISO 9001:2026, 9.1.2 Soddisfazione del cliente
