# MDPR33.1.A - Report Analisi dei Rischi

**Report Analisi dei Rischi**

### Revisioni

|          |            |                 |             |               |
|----------|------------|-----------------|-------------|---------------|
| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | CISO        | CDA           |
|          |            |                 |             |               |
|          |            |                 |             |               |

### Indice 

# 1 Introduzione

Il presente documento ha lo scopo di riportare il risultato dell’Analisi del Rischio svolta sull’ambito di certificazione del Sistema di Gestione della Sicurezza delle Informazioni.

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>INFORMAZIONI ANALISI DEI RISCHI</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Data aggiornamento Asset Inventory</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Numero di Asset</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Rischio Accettabile</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Tool Analisi del rischio e relativa versione</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Data effettuazione Analisi del Rischio</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Codice Analisi del rischio</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Data compilazione Checklist</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Team di compilazione Analisi del Rischio</strong></td>
<td><p>1) <u>Asset Inventory e AR</u>:</p>
<p>2) <u>Checklist</u>:</p></td>
</tr>
<tr class="odd">
<td><strong>Prossima data di revisione/compilazione</strong></td>
<td></td>
</tr>
</tbody>
</table>

Tabella 1 - Informazioni sull'Analisi dei Rischi

# 1.1 Applicabilità

L’attività di Analisi del Rischio è relativa all’ambito di certificazione ISO/IEC 27001 relativo all’ambito di certificazione:

***“Progettazione ed sviluppo software e consulenza in particolare in ambito deep tech” - “Design and development of software applications and consultancy primarily in Deep Tech”.***

# 1.2 Riferimenti e Allegati

ISO/IEC 27001 – ”Sicurezza delle informazioni, cybersecurity e protezione della privacy — Sistemi di gestione della sicurezza delle informazioni – Requisiti”

PR33.1 – Processo Analisi del Rischio e Trattamento.

# 1.3 Definizioni, Acronimi, Abbreviazioni

ASSET - Beni dell’organizzazione

ERA - Portale web di analisi dei rischi ERA (Environmental Risk Analysis)

RECORD - Terna asset-vulnerabilità-minaccia

RID - Proprietà di Riservatezza, Integrità, Disponibilità di una Informazione

RISCHIO - Effetto dell'incertezza sugli obiettivi, ma è spesso espresso in termini di una combinazione delle conseguenze di un evento

SGSI - Sistema di Gestione della Sicurezza delle Informazioni.

# 2 Impostazione per calcolo dei rischi

Secondo quanto specificato nella metodologia *“PR33.1 – Processo Analisi del Rischio“,* sono stati applicati i seguenti passaggi per svolgere l’analisi e la valutazione dei rischi:

1.  definizione dello staff avente ruolo di **Process Owner** (PO) sui processi primari e di supporto;

2.  definizione dei **Processi aziendali** e relativo PO al fine di identificare i processi su cui si evidenziano maggiori rischi;

3.  compilazione di un **Asset Inventory** che collega le classi di asset ai processi sopra definiti;

4.  definizione di **Rischio Accettabile** (RA) al fine di stabilire quali rischi trattare.

Per poter eseguire l’analisi del rischio sono stati inoltre:

1.  attribuiti i **valori di criticità** ad ogni Asset;

2.  valutate le **Vulnerabilità** di ogni Asset;

3.  valutate le **Minacce** che, sfruttando le precedenti vulnerabilità, impattano sulla Riservatezza, Integrità e Disponibilità delle informazioni;

4.  valutata la **Probabilità** di accadimento delle Minacce.

L’elenco completo di tali impostazioni e valori viene conservato nell’istanza di analisi del rischio effettuata con il tool indicato in Tabella 1.

# 2.1 Processi primari e di supporto

Di seguito è riportato l’elenco di processi, sia primari che di supporto, e relative codifiche rispetto ai quali sono stati classificati gli asset:

| **Processo** | **Tipo** | **Codice** |
|--------------|----------|------------|
|              |          |            |
|              |          |            |
|              |          |            |
|              |          |            |
|              |          |            |
|              |          |            |
|              |          |            |
|              |          |            |
|              |          |            |
|              |          |            |
|              |          |            |
|              |          |            |

Tabella 2 – Processi primari e a supporto

In fase di analisi del rischio ogni asset è stato messo in relazione con i processi aziendali.

# 2.2 Asset Inventory

L’Asset Inventory è uno degli input all’analisi del rischio ed è essenziale nel determinare l’output finale in quanto i valori di rischio vengono rappresentati suddivisi per singolo asset.

Questo elenco contiene tutti gli asset informativi che afferiscono all’ambito di certificazione del sistema di gestione SGSI.

L’asset inventory contiene esattamente <span class="mark">\<#numero\></span> asset.

Ad ogni asset sono state associate le seguenti informazioni (Figura 1):

- *Codice*: codice identificativo univoco dell’asset;

- *Nome*: nome identificativo assegnato all’asset dall’azienda;

- *Stato*: stato dell’asset, usato o dismesso; la dismissione permette di tenere traccia dell’asset anche nelle successive analisi di rischio qualora un asset non fosse più presente nell’asset inventory dell’organizzazione;

- *Descrizione*: descrizione dell'asset;

- *Classe*: classe di appartenenza dell’asset, selezionata da un elenco definito a sistema ed aggiornabile;

- *Criticità*: valore di criticità dell’asset in termini di RID delle informazioni ad esso associate. Tale valore viene attribuito dall’Asset Owner;

- *Asset Owner*: persona all'interno dell'organizzazione a cui è affidata la gestione dello specifico asset;

- *Risk Owner*: persona o entità con la responsabilità e l'autorità per gestire un rischio; tale responsabilità prevede quindi la gestione ed accettazione di un trattamento qualora un asset evidenzi un rischio superiore al RA;

- *Collocazione/sede*: collocazione dell'asset all’interno del perimetro fisico dell’organizzazione;

- *Processi*: processi su cui l’asset impatta.

<img src="MDPR33.1.A - Report Analisi dei Rischi/media/image1.png" style="width:6.29167in;height:2.48958in" />

Figura 1 – Esempio di asset e relative informazioni

# 2.3 Assegnazione Rischio Accettabile

A seguito di una precedente analisi su un sub-set di asset ritenuti sicuri in termini di RID, è stato identificato il valore di rischio accettabile, al di sopra del quale l’Organizzazione ritiene necessario definire i trattamenti di riduzione del rischio.

Il rischio accettabile della presente analisi è riportato nella Tabella 1 e viene riportato nel piano di Trattamento dei Rischi dove viene espressamente accettato dalla Direzione (Figura 2).

<img src="MDPR33.1.A - Report Analisi dei Rischi/media/image2.png" style="width:5.65625in;height:0.375in" />

<span class="mark">Figura 2 –</span> <span class="mark">Valore RA</span>

Il valore di RA viene stabilito dalla Direzione in fase di analisi di rischio e durante il Riesame della Direzione viene proposto un “Piano di rischio accettabile” (Figura 3) in cui si dà evidenza del valore in essere e del valore proposto per la successiva analisi di rischio, la data del Riesame, le funzioni che hanno approvato tale piano ed eventuali Note.

| **Piano di Rischio accettabile** |                                         |                        |                  |                  |          |
|----------------------------------|-----------------------------------------|------------------------|------------------|------------------|----------|
| **Anno**                         | **Soglia rischio accettabile definita** | **Proposta futuro RA** | **Data Riesame** | **Accettazione** | **Note** |
|                                  |                                         |                        |                  |                  |          |
|                                  |                                         |                        |                  |                  |          |
|                                  |                                         |                        |                  |                  |          |

Figura 3 – Piano di rischio accettabile

# 3 Checklist – Maturity Model

La Checklist utilizzata per definire la maturità del SGSI consiste in una serie di domande che coprono i punti ed i controlli dell’Annex A della norma ISO/IEC 27001.

Il punteggio ottenuto fornisce un’indicazione del livello di copertura del Sistema di Gestione rispetto alla norma di riferimento.

Ogni Process Owner ha compilato una checklist progettata sul ruolo specifico, e successivamente le risposte sono state riunite in un elenco riassuntivo che unisce i valori ottenuti.

Il risultato della Checklist finale fornisce il livello di maturità dei requisiti e dei controlli del sistema di gestione ed è usato come strumento per misurare la maturità dei processi e del Sistema di Gestione, e quindi lo stato di miglioramento.

<img src="MDPR33.1.A - Report Analisi dei Rischi/media/image3.png" style="width:6.3in;height:2.01667in" alt="Immagine che contiene testo, schermata, linea, numero Il contenuto generato dall&#39;IA potrebbe non essere corretto." />

Figura 4 - Esempio di domande di una Checklist

Si riporta di seguito la tabella con i risultati e la mappa del Maturity Level.

| **Etichette di riga**  | **Media di % APPL** | **Media di RIFERIMENTO** |
|------------------------|---------------------|--------------------------|
| 04.01                  |                     | 50,00%                   |
| 04.02                  |                     | 50,00%                   |
| 04.03                  |                     | 50,00%                   |
| 04.04                  |                     | 50,00%                   |
| 05.01                  |                     | 50,00%                   |
| 05.02                  |                     | 50,00%                   |
| 05.03                  |                     | 50,00%                   |
| 06.01                  |                     | 50,00%                   |
| 06.02                  |                     | 50,00%                   |
| 07.01                  |                     | 50,00%                   |
| 07.02                  |                     | 50,00%                   |
| 07.03                  |                     | 50,00%                   |
| 07.04                  |                     | 50,00%                   |
| 07.05                  |                     | 50,00%                   |
| 08.01                  |                     | 50,00%                   |
| 08.02                  |                     | 50,00%                   |
| 09.01                  |                     | 50,00%                   |
| 09.02                  |                     | 50,00%                   |
| 09.03                  |                     | 50,00%                   |
| 10.01                  |                     | 50,00%                   |
| 10.02                  |                     | 50,00%                   |
| A.05.01                |                     | 50,00%                   |
| A.05.02                |                     | 50,00%                   |
| A.05.03                |                     | 50,00%                   |
| A.05.04                |                     | 50,00%                   |
| A.05.05                |                     | 50,00%                   |
| A.05.06                |                     | 50,00%                   |
| A.05.07                |                     | 50,00%                   |
| A.05.08                |                     | 50,00%                   |
| A.05.09                |                     | 50,00%                   |
| A.05.10                |                     | 50,00%                   |
| A.05.11                |                     | 50,00%                   |
| A.05.12                |                     | 50,00%                   |
| A.05.13                |                     | 50,00%                   |
| A.05.14                |                     | 50,00%                   |
| A.05.15                |                     | 50,00%                   |
| A.05.16                |                     | 50,00%                   |
| A.05.17                |                     | 50,00%                   |
| A.05.18                |                     | 50,00%                   |
| A.05.19                |                     | 50,00%                   |
| A.05.20                |                     | 50,00%                   |
| A.05.21                |                     | 50,00%                   |
| A.05.22                |                     | 50,00%                   |
| A.05.23                |                     | 50,00%                   |
| A.05.24                |                     | 50,00%                   |
| A.05.25                |                     | 50,00%                   |
| A.05.26                |                     | 50,00%                   |
| A.05.27                |                     | 50,00%                   |
| A.05.28                |                     | 50,00%                   |
| A.05.29                |                     | 50,00%                   |
| A.05.30                |                     | 50,00%                   |
| A.05.31                |                     | 50,00%                   |
| A.05.32                |                     | 50,00%                   |
| A.05.33                |                     | 50,00%                   |
| A.05.34                |                     | 50,00%                   |
| A.05.35                |                     | 50,00%                   |
| A.05.36                |                     | 50,00%                   |
| A.05.37                |                     | 50,00%                   |
| A.06.01                |                     | 50,00%                   |
| A.06.02                |                     | 50,00%                   |
| A.06.03                |                     | 50,00%                   |
| A.06.04                |                     | 50,00%                   |
| A.06.05                |                     | 50,00%                   |
| A.06.06                |                     | 50,00%                   |
| A.06.07                |                     | 50,00%                   |
| A.06.08                |                     | 50,00%                   |
| A.07.01                |                     | 50,00%                   |
| A.07.02                |                     | 50,00%                   |
| A.07.03                |                     | 50,00%                   |
| A.07.04                |                     | 50,00%                   |
| A.07.05                |                     | 50,00%                   |
| A.07.06                |                     | 50,00%                   |
| A.07.07                |                     | 50,00%                   |
| A.07.08                |                     | 50,00%                   |
| A.07.09                |                     | 50,00%                   |
| A.07.10                |                     | 50,00%                   |
| A.07.11                |                     | 50,00%                   |
| A.07.12                |                     | 50,00%                   |
| A.07.13                |                     | 50,00%                   |
| A.07.14                |                     | 50,00%                   |
| A.08.01                |                     | 50,00%                   |
| A.08.02                |                     | 50,00%                   |
| A.08.03                |                     | 50,00%                   |
| A.08.04                |                     | 50,00%                   |
| A.08.05                |                     | 50,00%                   |
| A.08.06                |                     | 50,00%                   |
| A.08.07                |                     | 50,00%                   |
| A.08.08                |                     | 50,00%                   |
| A.08.09                |                     | 50,00%                   |
| A.08.10                |                     | 50,00%                   |
| A.08.11                |                     | 50,00%                   |
| A.08.12                |                     | 50,00%                   |
| A.08.13                |                     | 50,00%                   |
| A.08.14                |                     | 50,00%                   |
| A.08.15                |                     | 50,00%                   |
| A.08.16                |                     | 50,00%                   |
| A.08.17                |                     | 50,00%                   |
| A.08.22                |                     | 50,00%                   |
| A.08.23                |                     | 50,00%                   |
| A.08.24                |                     | 50,00%                   |
| A.08.25                |                     | 50,00%                   |
| A.08.18                |                     | 50,00%                   |
| A.08.19                |                     | 50,00%                   |
| A.08.20                |                     | 50,00%                   |
| A.08.21                |                     | 50,00%                   |
| A.08.26                |                     | 50,00%                   |
| A.08.27                |                     | 50,00%                   |
| A.08.28                |                     | 50,00%                   |
| A.08.29                |                     | 50,00%                   |
| A.08.30                |                     | 50,00%                   |
| A.08.31                |                     | 50,00%                   |
| A.08.32                |                     | 50,00%                   |
| A.08.33                |                     | 50,00%                   |
| A.08.34                |                     | 50,00%                   |
| **Totale complessivo** |                     | **50,00%**               |

Figura 5 - Livelli di copertura dei punti norma

Figura 6 - Livelli di copertura in funzione delle risposte fornite

<span class="mark">Dal Maturity Level si possono quindi evidenziare i controlli che mostrano un livello di copertura inferiore al **XX%** nei quali l’organizzazione evidenzia dei rischi alla sicurezza delle informazioni e ai processi del sistema stesso.</span>

# 4 Compilazione analisi del rischio

Sulla base degli input definiti al punto 4 è stata definita una istanza di analisi del rischio identificata dal codice “**<span class="mark">XXX</span>**”.

<img src="MDPR33.1.A - Report Analisi dei Rischi/media/image4.png" style="width:6.49653in;height:1.35833in" />

Figura 7 - Istanza analisi di rischio

Il concetto di record è alla base della logica del tool Analisi del Rischio.

Il singolo record è espressione del rischio sull’asset dovuto all’impatto di una minaccia (modulato sulla probabilità di accadimento) che sfrutta una vulnerabilità dell’asset.

Ogni record rappresenta quindi il valore di rischio associato a una terna univoca rappresentata da:

**asset-minaccia-vulnerabilità**

Tale valore è l’espressione del rischio calcolato su di un asset ed è determinato dall’impatto, modulato sulla probabilità di accadimento, che una minaccia sfrutti una vulnerabilità nota dell’asset stesso.

Nella pagina di configurazione di ogni asset, ed in funzione delle minacce associate elencate, sono inserite le seguenti informazioni:

- *<u>Probabilità di accadimento</u> – È la probabilità che si presenti la minaccia derivante da valori storicamente stimati o semplicemente ipotizzata*

- *<u>RID dell’Informazione</u> - Rappresentano il valore dell’impatto che la minaccia considerata ha sulla classe di asset considerata in termini di riservatezza, integrità e disponibilità dell’informazione. E’ assegnato di default dal sistema.*

  - *Vulnerabilità, Vulnerabilità associate all'asset. Il “Livello di vulnerabilità” valore scelto dal Process Owner in base a quanto tale vulnerabilità risulta insita nell'asset, al netto di eventuali contromisure già in atto per mitigare il rischio.*

<img src="MDPR33.1.A - Report Analisi dei Rischi/media/image5.png" style="width:6.29134in;height:3.16535in" />

Figura 8 – Esempio Asset-Minaccia-Vulnerabilità

Le informazioni inserite riportano automaticamente il livello di rischio associato alla terna.

<img src="MDPR33.1.A - Report Analisi dei Rischi/media/image6.png" style="width:2.15833in;height:1.15069in" />

> Figura 9 – Livello rischio

# 5 Risultato dell’analisi del rischio

Sulla base degli input utilizzati, sono stati effettuati i calcoli per determinare i valori di rischio visualizzabili in maniera interattiva direttamente sullo strumento all’indirizzo indicato nella Tabella 1.

I risultati sono rappresentati in un grafico a barre contenente:

- la distribuzione dei record (minaccia-asset-vulnerabilità) per fasce di rischio;

- la numerosità di record contenuti in ogni fascia di rischio;

- la suddivisione dei record in tre zone di compliance rispetto alla soglia di rischio accettabile:

  - valori accettabili -\> valore rischio basso

  - valori limite -\> valore rischio medio

  - superiori al rischio accettabile -\> valore rischio alto.

<img src="MDPR33.1.A - Report Analisi dei Rischi/media/image7.png" style="width:6.49653in;height:4.11319in" />

Figura 10 - Distribuzione rischio

È possibile visualizzare per ogni fascia di rischio le vulnerabilità e minacce coinvolte ordinate per asset.

Similmente per ogni per ogni asset è rappresentato il colore della fascia più alta in cui si esso colloca (Figura 11)

- Rosso: valore non accettabile;

- Giallo: valore limite;

- Verde: valore accettabile;

e le vulnerabilità e minacce associate (Figura 8).

> <img src="MDPR33.1.A - Report Analisi dei Rischi/media/image8.png" style="width:3.90625in;height:1.27083in" />

Figura 11 – Colore rischio asset

<img src="MDPR33.1.A - Report Analisi dei Rischi/media/image9.png" style="width:6.49653in;height:3.04236in" />

Figura 12 - Asset e Informazioni rischio associato

**<span class="mark">Il risultato dell’analisi del rischio evidenzia che TUTTI gli asset sono sotto la soglia di rischio accettabile e quindi nessun asset con rischio ALTO.</span>**

**<span class="mark">Da questo si evidenzia che gli asset oggetto di questa analisi non richiedono alcuna tipologia di trattamento.</span>**

**<span class="mark">OPPURE</span>**

**<span class="mark">Il risultato dell’analisi del rischio evidenzia un numero di record sopra il valore di rischio accettabile pari a X record relativo a 7 a X Asset e un numero di record sul valore di soglia di rischio accettabile pari a X record relativo a 6 asset (di questi X, X asset ricade anche tra quelli sopra soglia). Quindi il numero complessivo di asset portati all’attenzione è X.</span>**

<span class="mark">Di seguito verranno analizzati:</span>

- <span class="mark">gli asset con valore di rischio superiore al RA = X per fasce di rischio</span>

- <span class="mark">per completezza gli asset con valore di rischio pari alla soglia di rischio accettabile e ritenuti necessari di successivo trattamento per ridurre il rischio da parte dell’azienda.</span>

1)  **<span class="mark">valore di rischio nell’intervallo X – X coinvolti X Asset</span>**

2)  **<span class="mark">valore di rischio nell’intervallo X – X coinvolti X Asset</span>**

**<span class="mark">Livello di Rischio: xx - xx</span>**

> Gli asset riportati di seguito presentano un rischio compreso tra <span class="mark">xx</span> e <span class="mark">xx</span>: <span class="mark">x</span> asset per un totale di 4 record.

| ID Asset | Valore di rischio MAX |
|----------|-----------------------|
|          |                       |
|          |                       |

| **ID Asset** | **Descrizione** | **Classe Asset** | **Criticità** | **Minaccia** | **Livello Impatto Minaccia** | **Vulnerabilità** | **Livello Impatto Vulnerabilità** | **Valore di Rischio** |
|--------------|-----------------|------------------|---------------|--------------|------------------------------|-------------------|-----------------------------------|-----------------------|
|              |                 |                  |               |              |                              |                   |                                   |                       |
|              |                 |                  |               |              |                              |                   |                                   |                       |
|              |                 |                  |               |              |                              |                   |                                   |                       |
|              |                 |                  |               |              |                              |                   |                                   |                       |

La tabella sopra riportata evidenzia le minacce e le vulnerabilità a cui sono esposti gli asset:

- **xxx – “X”:** si evidenzia la difficoltà di X e quindi soggette a X, in quanto XXX.

- **xxx – “X”:** si evidenzia la difficoltà di X e quindi soggette a X, in quanto XXX.

# 
