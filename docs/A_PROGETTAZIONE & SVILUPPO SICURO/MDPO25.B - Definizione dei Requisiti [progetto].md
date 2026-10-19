# MDPO25.B - Definizione dei Requisiti [progetto]

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>&lt;Cliente&gt;</strong></p>
<p><strong>&lt;Progetto&gt;</strong></p>
<p><strong>Definizione dei Requisiti</strong></p></td>
</tr>
</tbody>
</table>

### Revisioni

|          |            |                 |                      |               |
|----------|------------|-----------------|----------------------|---------------|
| **Rev.** | **Data**   | **Descrizione** | **Redatto**          | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | Responsabile di Area | CTO           |
|          |            |                 |                      |               |
|          |            |                 |                      |               |
|          |            |                 |                      |               |

# Indice

#  

|                   |                                            |
|-------------------|--------------------------------------------|
| **Approvatore**   | Menzionare la risorsa coinvolta            |
| **Collaboratori** | Menzionare le risorse coinvolte            |
| **Informati**     | Menzionare le risorse coinvolte            |
| **Committente**   | Denominazione del committente del progetto |
| **Progetto**      | Denominazione del progetto                 |

# 1. Introduzione 

# 1.1. Obiettivo

Il presente paragrafo indica qual è l’obiettivo del documento che si è prodotto. Inoltre, indica l’utenza a cui è diretto.

# 1.2. Campo di applicazione 

Specifica il nome del prodotto che si appresta a sviluppare. È importante includere gli obiettivi del prodotto e i principali benefici che derivano dal suo impiego. Infine, specifica il campo d’applicazione, ovvero le problematiche che si intendono analizzare.

# 1.3. Definizioni, acronimi e abbreviazioni

Il presente paragrafo dovrebbe includere la definizione di tutti i termini utilizzati, acronimi e abbreviazioni.

# 1.4. Fonti

Riporta l’elenco completo di tutte le fonti in termini di documenti, libri, siti o altro analizzati, identificando ciascuno di questi con il titolo, la data, l’editore etc.

|                                 |     |             |            |
|---------------------------------|-----|-------------|------------|
| **Titolo / Nome / Riferimento** |     |             | **Fonti**  |
| **Tipologia**                   |     | **Editore** |            |
| **Versione**                    |     | **Data**    | gg/mm/aaaa |
| **Descrizione**                 |     |             |            |

# 2. Descrizione generale (Requisiti di business)

La presente sezione dovrebbe descrivere i principali fattori che riguardano il prodotto e i suoi requisiti. In sostanza, riporta le regole fondamentali per il concreto funzionamento del prodotto e per il soddisfacimento dei requisiti che verranno discussi nella sezione seguente.

# 2.1. Funzionalità di sistema (requisiti iniziali)

Elenca le principali funzionalità che il sistema offre, riconducibili ai requisiti descritti e riportati in offerta. Di solito, questa parte può essere integrata con la documentazione precedentemente prodotta e riguarda le macro-funzionalità comprese e accordate con il Cliente e le forma testuale o grafica delle differenti funzionalità e le relazioni principali tra queste.

# 2.2. Caratteristiche degli utenti

Delinea le caratteristiche degli utenti del sistema in termini di esperienza, capacità tecnica e

livello di istruzione.

# 2.3. Vincoli generali

Esprime i vincoli che verranno affrontati durante lo sviluppo in termini di interfacciamento con altri sistemi, operazioni parallele e elementi di criticità.

# 2.4. Assunzioni e dipendenze

Indica le ipotesi di partenza su cui si basa la fase di analisi e specifica dei requisiti. Inoltre, elenca i fattori che, eventualmente modificati, hanno ripercussioni su quanto contenuto nel documento.

# 2.5. Requisiti da analizzare in futuro

Una volta inquadrato il prodotto che verrà sviluppato, alcuni requisiti possono essere individuati ma l’approfondimento posticipato per il futuro. È auspicabile determinare almeno con approssimazione i tempi e le persone che verranno coinvolte.

# 2.6. Casi d’uso

…

# 3. Specifica dei requisiti 

La presente sezione è fondamentale e riporta i requisiti sia i requisiti di interfaccia esterna, funzionali e quelli non funzionali.

# 3.1. Requisiti di Interfaccia esterna

I requisiti vengono codificati usando come prefisso la sigla:

- RIE, per i requisiti di interfaccia esterna

Il suffisso del codice è un numero progressivo a partire da 01.

### 3.1.1. Interfaccia sistema/utente

Elenca le caratteristiche dell’interfaccia sistema/utente e le funzionalità a cui il sistema deve assolvere. Inoltre, è necessario elencare le caratteristiche dell’interfaccia utente in termini di formato dello screen, layout di pagine, contenuti del report o dei menu, la lunghezza dei messaggi di errore (corti, lunghi).

<span class="mark">Specificare:</span>

1.  <span class="mark">Le caratteristiche logiche di ogni interfaccia tra il prodotto software e i suoi utenti.</span>

2.  <span class="mark">Tutti gli aspetti dell'ottimizzazione dell'interfaccia con la persona che deve usare il sistema</span>

<span class="mark">Questa è una descrizione di come il sistema interagirà con i suoi utenti. C'è una GUI, una linea di comando o qualche altro tipo di interfaccia? Ci sono requisiti speciali per l'interfaccia?</span>

|                 |              |                                      |
|-----------------|--------------|--------------------------------------|
| **Codice**      | es. (RIE03)  | **Requisiti di interfaccia esterna** |
|                 |              | **Interfaccia sistema/utente**       |
| **Descrizione** | … oppure N/A |                                      |

### 3.1.2. Interfaccia hardware

Riporta le informazioni che servono per configurare il sistema in modo adeguato (numeri di porta, set di istruzioni etc), i dispositivi supportati etc.

Specificare le caratteristiche logiche di ogni interfaccia tra il prodotto software e i componenti hardware del sistema. Questo include le caratteristiche di configurazione. Riguarda anche questioni come quali dispositivi devono essere supportati, come devono essere supportati e i protocolli.

|                 |              |                                      |
|-----------------|--------------|--------------------------------------|
| **Codice**      | es. (RIE03)  | **Requisiti di interfaccia esterna** |
|                 |              | **Interfaccia hardware**             |
| **Descrizione** | … oppure N/A |                                      |

### 3.1.3. Interfaccia software

Specifica, nel caso ci sia bisogno, la necessità d’uso di altri pacchetti software di supporto e l’interfacciamento con altre applicazioni (interne, esterne).

Specificare l'uso di altri prodotti software richiesti e le interfacce con altri sistemi applicativi. Per ogni prodotto software richiesto, includere:

1.  Nome

2.  Codice mnemonico

3.  Numero di specifica

4.  Numero di versione

5.  Fonte

Per ogni interfaccia, fornire:

1.  Descrizione dello scopo del software di interfaccia in relazione a questo prodotto software.

2.  Definizione dell'interfaccia in termini di contenuto del messaggio e formato.

|                 |              |                                      |
|-----------------|--------------|--------------------------------------|
| **Codice**      | es. (RIE03)  | **Requisiti di interfaccia esterna** |
|                 |              | **Interfaccia software**             |
| **Descrizione** | … oppure N/A |                                      |

### 3.1.4. Interfaccia di comunicazione

Riporta i protocolli di comunicazione, ad esempio TCP/IP.

|                 |              |                                      |
|-----------------|--------------|--------------------------------------|
| **Codice**      | es. (RIE03)  | **Requisiti di interfaccia esterna** |
|                 |              | **Interfaccia di comunicazione**     |
| **Descrizione** | … oppure N/A |                                      |

# 3.2. Requisiti funzionali

I requisiti vengono codificati usando come prefisso la sigla:

- RF, per i requisiti funzionali

Il suffisso del codice è un numero progressivo a partire da 01.

- **titolo**: strutturato in tre sezioni:

  - codice: identifica il requisito,

  - area di riferimento: collocazione del requisito,

  - titolo specifico: descrive brevemente la funzionalità del requisito.

- **input**: sono le informazioni che sono inserite all’interno del processo come ingresso

- **processo**: sequenza di azioni eseguite dall’operatore, eventuali messaggi di errore come risposta ad anomalie e parametri che incidono sull’output

- **output**: risultato del processo

- **livello di rischio**: (Assente, Basso, Medio, Alto)

- **livello di rischio privacy**: (Assente, Basso, Medio, Alto)

- **dipendenze**: con altri requisiti

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 60%" />
<col style="width: 21%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Codice</strong></td>
<td>es. (RF01)</td>
<td><strong>Requisiti funzionali</strong></td>
</tr>
<tr class="even">
<td><strong>Area di riferimento</strong></td>
<td colspan="2"><p>collocazione del requisito,</p>
<p>(es. Anagrafica contatti)</p></td>
</tr>
<tr class="odd">
<td><strong>Titolo specifico</strong></td>
<td colspan="2">(es. Cancellazione contatto)</td>
</tr>
<tr class="even">
<td><strong>Input</strong></td>
<td colspan="2">Sono le informazioni che sono inserite all’interno del processo come ingresso (Dati da modificare)</td>
</tr>
<tr class="odd">
<td><strong>Processo</strong></td>
<td colspan="2"><p>Sequenza di azioni eseguite dall’operatore, eventuali messaggi di errore come risposta ad anomalie e parametri che incidono sull’output</p>
<p>Esempio: L’operatore coinvolto accede al sistema con il suo identificativo, alla sezione Archivio nominativi e seleziona il contatto che vuole eliminare e clicca sull’apposita icona per richiedere la cancellazione, il sistema chiede conferma</p>
<p>dell’operazione e se la risposta è affermativa il contatto non viene eliminato fisicamente dal sistema, ma non è più nella lista dell’anagrafica contatti. I dati di tale contatto rimangono comunque disponibili nelle attività in cui sia stato precedentemente inserito.</p></td>
</tr>
<tr class="even">
<td><strong>Output</strong></td>
<td colspan="2"><p>Risultato del processo</p>
<p>Esempio: Il contatto cancellato non è più selezionabile dalla lista dell’anagrafica dei contatti, ma i dati che lo caratterizzano sono consultabili nelle attività in cui è stato precedentemente inserito</p></td>
</tr>
<tr class="odd">
<td><strong>Livello di rischio</strong></td>
<td colspan="2"><p>Selezionare e descrivere un livello di rischio tra:</p>
<p>assente / basso / medio / alto</p></td>
</tr>
<tr class="even">
<td><strong>Livello di rischio privacy</strong></td>
<td colspan="2"><p>Selezionare e descrivere un livello di rischio tra:</p>
<p>assente / basso / medio / alto</p></td>
</tr>
<tr class="odd">
<td><strong>Dipendenze</strong></td>
<td colspan="2">Scrivere se tale requisito dipende da altri requisiti</td>
</tr>
</tbody>
</table>

# 3.3. Requisiti non funzionali

I requisiti non funzionali non sono collegati direttamente con le funzioni implementate dal sistema, ma piuttosto alle modalità operative e di gestione. In sintesi, essi definiscono i vincoli sullo sviluppo del sistema. Certe volte possono essere più critici di quelli funzionali.

I requisiti vengono codificati usando come prefisso la sigla:

- RNF, per i requisiti non funzionali

Il suffisso del codice è un numero progressivo a partire da 01.

### 3.3.1. Requisiti prestazionali

I requisiti prestazionali includono i requisiti in termini di numero di terminali supportati, numero di utenti che hanno l’accesso al sistema in modo concorrenziale, quantità e tipo di informazioni che possono essere contemporaneamente manipolate.

|                       |                                                                                                                                                                                |                             |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| **Codice**            | es. (RNF01)                                                                                                                                                                    | **Requisiti prestazionali** |
| **Tempi di risposta** | …                                                                                                                                                                              |                             |
| **Descrizione**       | Il software deve consentire all’utente di ottenere risposte in tempo reale. Nel caso in cui il server su cui è pubblicato possa essere accessibile in modalità locale (LAN), … |                             |

### 3.3.2. Database

È opportuno indicare il tipo di database che si intende utilizzare (vincoli di integrità e altre informazioni specifiche del DB) e DB non compatibili con le caratteristiche del prodotto.

|                 |                                                                                                              |              |
|-----------------|--------------------------------------------------------------------------------------------------------------|--------------|
| **Codice**      | es. (RNF02)                                                                                                  | **Database** |
| **Descrizione** | Il software deve mettere a disposizione un sistema in grado di garantire la persistenza delle informazioni … |              |

### 3.3.3. Vincoli generali di progetto

I vincoli generali del progetto elencano i vincoli imposti da altri standard, limitazioni hardware o altro.

#### Standard Adottati

In questa sezione si elencano i requisiti che derivano dagli standard esistenti e/o già applicati oppure dalle normative vigenti.

|                 |              |                                   |
|-----------------|--------------|-----------------------------------|
| **Codice**      | es. (RNF03)  | **Vincoli generali del progetto** |
|                 |              | **Standard adottati**             |
| **Descrizione** | … oppure N/A |                                   |

#### Tecnologici

In questa sezione si elencano i requisiti che derivano da vincoli tecnologici da adottare.

|                 |              |                                   |
|-----------------|--------------|-----------------------------------|
| **Codice**      | es. (RNF03)  | **Vincoli generali del progetto** |
|                 |              | **Tecnologici**                   |
| **Descrizione** | … oppure N/A |                                   |

### 3.3.4. Attributi del sistema

Elenchiamo alcune delle caratteristiche principali del software che possono essere considerate come requisiti veri e propri.

#### Affidabilità

È necessario specificare le condizioni che determineranno il grado di affidabilità accettabile del software al momento del rilascio.

|                 |              |                           |
|-----------------|--------------|---------------------------|
| **Codice**      | es. (RNF04)  | **Attributi del sistema** |
|                 |              | **Affidabilità**          |
| **Descrizione** | … oppure N/A |                           |

#### Accessibilità del sistema

Elenco dei parametri che determinano l’accessibilità dell’intero prodotto software in termini di checkpoint, le funzionalità di recovery e altri parametri di accessibilità;

Specifica le operazioni di inizializzazione del sistema, le operazioni di backup e recovery.

|                 |              |                               |
|-----------------|--------------|-------------------------------|
| **Codice**      | es. (RNF05)  | **Attributi del sistema**     |
|                 |              | **Accessibilità del sistema** |
| **Descrizione** | … oppure N/A |                               |

#### Sicurezza

Elenco delle proprietà che servono a proteggere il software dagli accessi accidentali o di utenti malintenzionati.

|                 |                                      |                           |
|-----------------|--------------------------------------|---------------------------|
| **Codice**      | es. (RNF06)                          | **Attributi del sistema** |
|                 |                                      | **Sicurezza**             |
| **Descrizione** | … e riferimento alle checklist OWASP |                           |

#### Privacy

Elenco delle proprietà che servono a proteggere i dati contenuti nel software in conformità ai regolamenti applicabili, incluse best practices di privacy by design e privacy by default. o vincoli del cliente.

|                 |             |                           |
|-----------------|-------------|---------------------------|
| **Codice**      | es. (RNF07) | **Attributi del sistema** |
|                 |             | **Privacy**               |
| **Descrizione** | …           |                           |

#### Manutenibilità

Elenco delle proprietà che rendono il prodotto software mantenibile, ad esempio la modularità, software organizzato a moduli, elementi critici parametrizzati.

|                 |             |                           |
|-----------------|-------------|---------------------------|
| **Codice**      | es. (RNF08) | **Attributi del sistema** |
|                 |             | **Manutenibilità**        |
| **Descrizione** | …           |                           |

#### Portabilità

Elenco delle proprietà che rendono il prodotto software ad esempio indipendente dal sistema operativo, dal DBMS e simile.

|                 |              |                           |
|-----------------|--------------|---------------------------|
| **Codice**      | es. (RNF09)  | **Attributi del sistema** |
|                 |              | **Portabilità**           |
| **Descrizione** | … oppure N/A |                           |

### 3.3.5. Vincoli relativi all’occupazione di memoria

Specifica le caratteristiche e i limiti dei supporti di memoria primaria e secondaria.

### 3.3.6. Vincoli per installazione

Specifica per ciascun nodo (server, client) i vincoli, ad esempio la sequenza di inizializzazione, livello di sicurezza richiesto etc.

### 3.3.7. Altri requisiti

Elenco dei requisiti che descrivono ad esempio:

- Gruppi di utenti e relativi permessi per l’accesso alle funzionalità del sistema

- Commenti addizionali – scalabilità – aumento del numero di utenti – implicazione sulla performance, costi
