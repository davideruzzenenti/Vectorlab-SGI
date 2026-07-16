# MDPO25.C - Documentazione Tecnica [progetto]

**Modulo — Template Documentazione Tecnica di Progetto**

<div style="border-left:4px solid #2A5C8A;background:#EAF1F7;padding:.75rem 1rem;margin:1rem 0">
<strong>DOCUMENTO IN BOZZA — generato il 16/07/2026</strong> per colmare una lacuna rilevata durante la revisione della documentazione (citato nella SOA ma non ancora creato). Contenuto basato su pratiche reali già note da altri documenti del SGI; le parti evidenziate in rosso sono da confermare prima dell'approvazione formale.
</div>

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.1      | 16/07/2026 | Prima bozza — documento mancante generato per colmare una lacuna rilevata nella SOA | IA          | Da approvare  |
|          |            |                 |             |               |

## 1 Scopo

Il presente modulo, allegato a "*PO25 - Sviluppo Sicuro*", costituisce
il template di documentazione tecnica da compilare per ciascun
progetto di sviluppo software, a supporto delle attività di
progettazione, architettura, test e rilascio. Il documento raccoglie
le informazioni tecniche di progetto e le evidenze delle verifiche di
sicurezza effettuate, ai fini di tracciabilità secondo quanto previsto
da "*PR19.1 - Gestione del Cambiamento*".

**Da duplicare per ciascun progetto**, sostituendo "\[progetto\]" con
il nome del progetto/Cliente e mantenendo traccia della versione.

## 2 Dati Generali del Progetto

| **Campo**                    | **Valore** |
| ------------------------------ | ---------- |
| Nome progetto                  |            |
| Cliente / Committente (se applicabile) |    |
| Referente/Owner tecnico del progetto |      |
| Data compilazione documento    |            |
| Versione documento             |            |
| Riferimento a MDPO25.B associato |          |

## 3 Architettura della Soluzione

| **Campo**                                | **Descrizione** |
| -------------------------------------------- | ----------------- |
| Descrizione generale dell'architettura        |                    |
| Componenti principali e loro isolamento       |                    |
| Diagramma di architettura (link/allegato)     |                    |
| Tecnologie e framework utilizzati             |                    |
| Repository GitHub di riferimento              |                    |
| Servizi/piattaforme cloud utilizzati          |                    |
| Database e sistemi di persistenza (es. MongoDB) |                  |
| Integrazioni con servizi/API di terze parti   |                    |

## 4 Ambienti

| **Ambiente**   | **Descrizione/Configurazione** | **Accesso limitato a** |
| --------------- | -------------------------------- | -------------------------- |
| Sviluppo         |                                    |                             |
| Test             |                                    |                             |
| Produzione       |                                    |                             |

## 5 Gestione dei Dati

| **Campo**                                          | **Valore** |
| ------------------------------------------------------ | ---------- |
| Dati personali/sensibili trattati (Si/No)                |            |
| Modalità di protezione dei dati (cifratura, mascheramento, ecc.) |    |
| Dati utilizzati in ambienti di test (reali/mascherati/sintetici) |    |
| Politiche di backup applicate                            |            |

## 6 Attività di Test e Verifica di Sicurezza

| **Data** | **Tipologia di test (funzionale/sicurezza/API/altro)** | **Strumento utilizzato** | **Esito** | **Riferimento evidenza/report** |
| -------- | ---------------------------------------------------------- | --------------------------- | --------- | ------------------------------------ |
|          |                                                               |                              |           |                                       |
|          |                                                               |                              |           |                                       |

## 7 Non Conformità e Vulnerabilità Rilevate

| **ID** | **Descrizione** | **Severità (Critica/Alta/Media/Bassa)** | **Stato (Aperta/In gestione/Risolta/Accettata)** | **Data chiusura** |
| ------ | ----------------- | ------------------------------------------- | ----------------------------------------------------- | ---------------------- |
|        |                     |                                              |                                                         |                         |
|        |                     |                                              |                                                         |                         |

## 8 Storico delle Modifiche Rilevanti

| **Data** | **Descrizione modifica** | **Riferimento commit/PR/Change** | **Approvato da** |
| -------- | --------------------------- | -------------------------------------- | ---------------------- |
|          |                              |                                          |                         |
|          |                              |                                          |                         |

## 9 Rilascio in Produzione

| **Campo**                    | **Valore** |
| ------------------------------ | ---------- |
| Data rilascio                  |            |
| Versione rilasciata            |            |
| Esito verifiche pre-rilascio (MDPO25.A compilata Si/No) |  |
| Approvato da                   |            |
| Piano di rollback disponibile (Si/No) |             |

## 10 Riferimenti

> PO25 - Sviluppo Sicuro

> MDPO25.A - OWASP ASVS Checklist

> MDPO25.B - Definizione dei Requisiti \[progetto\]

> PR19.1 - Gestione del Cambiamento

> PR21.1 - Gestione dei Backup e Restore.
