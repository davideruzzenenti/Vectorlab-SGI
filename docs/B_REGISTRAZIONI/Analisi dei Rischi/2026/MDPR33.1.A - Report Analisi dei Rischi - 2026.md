# MDPR33.1.A - Report Analisi dei Rischi - 2026

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
<td>Aprile 2026</td>
</tr>
<tr class="even">
<td><strong>Numero di Asset</strong></td>
<td>49</td>
</tr>
<tr class="odd">
<td><strong>Rischio Accettabile</strong></td>
<td>45</td>
</tr>
<tr class="even">
<td><strong>Tool Analisi del rischio e relativa versione</strong></td>
<td>ERA v2.0</td>
</tr>
<tr class="odd">
<td><strong>Data effettuazione Analisi del Rischio</strong></td>
<td>Agosto – Settembre 2026</td>
</tr>
<tr class="even">
<td><strong>Codice Analisi del rischio</strong></td>
<td>Agosto 2026</td>
</tr>
<tr class="odd">
<td><strong>Data compilazione Checklist</strong></td>
<td>Agosto 2026</td>
</tr>
<tr class="even">
<td><strong>Team di compilazione Analisi del Rischio</strong></td>
<td><p>1) <u>Asset Inventory e AR</u>:</p>
<p>Andrea Ruzzenenti, Davide Ruzzenenti, Francesco Cappetti.</p>
<p>Con il supporto di: Alberto Vaglio (Nextage), Ilir Perez (Nextage)</p>
<p>2) <u>Checklist</u>:</p>
<p>Andrea Ruzzenenti, Davide Ruzzenenti. Con il supporto di:</p>
<p>Francesca Capuano (Nextage)</p></td>
</tr>
<tr class="odd">
<td><strong>Prossima data di revisione/compilazione</strong></td>
<td>Settembre 2027</td>
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

RIDA - Proprietà di Riservatezza, Integrità, Disponibilità, Autenticità di una Informazione

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

| **Processo**         | **Tipo** | **Codice** |
|----------------------|----------|------------|
| IT                   | Supporto | P001       |
| Software Development | Primario | P002       |
| Amministrazione      | Supporto | P003       |
| Risorse Umane        | Supporto | P004       |
| Business Development | Primario | P005       |
| Direzione            | Supporto | P006       |

Tabella 2 – Processi primari e a supporto

In fase di analisi del rischio ogni asset è stato messo in relazione con i processi aziendali.

# 2.2 Asset Inventory

L’Asset Inventory è uno degli input all’analisi del rischio ed è essenziale nel determinare l’output finale in quanto i valori di rischio vengono rappresentati suddivisi per singolo asset.

Questo elenco contiene tutti gli asset informativi che afferiscono all’ambito di certificazione del sistema di gestione SGSI.

L’asset inventory contiene esattamente 49 asset.

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

<img src="MDPR33.1.A - Report Analisi dei Rischi - 2026/media/image1.png" style="width:6.6in;height:4.73472in" />

Figura - Esempio di asset e relative informazioni

# 2.3 Assegnazione Rischio Accettabile

A seguito di una precedente analisi su un sub-set di asset ritenuti sicuri in termini di RIDA, è stato identificato il valore di rischio accettabile, al di sopra del quale l’Organizzazione ritiene necessario definire i trattamenti di riduzione del rischio.

Il rischio accettabile della presente analisi è riportato nella Tabella 1 e viene riportato nel piano di Trattamento dei Rischi dove viene espressamente accettato dalla Direzione (Tabella 3).

<img src="MDPR33.1.A - Report Analisi dei Rischi - 2026/media/image2.png" style="width:5.30879in;height:2.72524in" />

Figura - Valore RA

Il valore di RA viene stabilito dalla Direzione in fase di analisi di rischio e durante il Riesame della Direzione viene proposto un “Piano di rischio accettabile” (Figura 3) in cui si dà evidenza del valore in essere e del valore proposto per la successiva analisi di rischio, la data del Riesame, le funzioni che hanno approvato tale piano ed eventuali Note.

| **Piano di Rischio accettabile** |                                         |                             |                             |                  |          |
|----------------------------------|-----------------------------------------|-----------------------------|-----------------------------|------------------|----------|
| **Anno**                         | **Soglia rischio accettabile definita** | **Proposta futuro RA**      | **Data Riesame**            | **Accettazione** | **Note** |
| 2026                             | 45                                      | <span class="mark">-</span> | <span class="mark">-</span> | C.D.A.           |          |
|                                  |                                         |                             |                             |                  |          |
|                                  |                                         |                             |                             |                  |          |
|                                  |                                         |                             |                             |                  |          |

Tabella 3 – Piano di rischio accettabile

# 4 Compilazione analisi del rischio

Sulla base degli input definiti al punto 4 è stata definita una istanza di analisi del rischio identificata dal codice “**Agosto 2026**”.

<img src="MDPR33.1.A - Report Analisi dei Rischi - 2026/media/image3.png" style="width:6.6in;height:0.44722in" />

Figura - Istanza di Analisi di Rischio

Il concetto di record è alla base della logica del tool Analisi del Rischio.

Il singolo record è espressione del rischio sull’asset dovuto all’impatto di una minaccia (modulato sulla probabilità di accadimento) che sfrutta una vulnerabilità dell’asset.

Ogni record rappresenta quindi il valore di rischio associato a una terna univoca rappresentata da:

**asset-minaccia-vulnerabilità**

Tale valore è l’espressione del rischio calcolato su di un asset ed è determinato dall’impatto, modulato sulla probabilità di accadimento, che una minaccia sfrutti una vulnerabilità nota dell’asset stesso.

Nella pagina di configurazione di ogni asset, ed in funzione delle minacce associate elencate, sono inserite le seguenti informazioni:

- *<u>Probabilità di accadimento</u> – È la probabilità che si presenti la minaccia derivante da valori storicamente stimati o semplicemente ipotizzata*

- *<u>RID dell’Informazione</u> - Rappresentano il valore dell’impatto che la minaccia considerata ha sulla classe di asset considerata in termini di riservatezza, integrità e disponibilità dell’informazione. E’ assegnato di default dal sistema.*

  - *Vulnerabilità, Vulnerabilità associate all'asset. Il “Livello di vulnerabilità” valore scelto dal Process Owner in base a quanto tale vulnerabilità risulta insita nell'asset, al netto di eventuali contromisure già in atto per mitigare il rischio.*

<img src="MDPR33.1.A - Report Analisi dei Rischi - 2026/media/image4.png" style="width:6.6in;height:3.09792in" />

Figura - Esempio Asset-Minaccia-Vulnerabilità

Le informazioni inserite riportano automaticamente il livello di rischio associato alla terna.

<img src="MDPR33.1.A - Report Analisi dei Rischi - 2026/media/image5.png" style="width:3.8917in;height:3.54873in" />

Figura - Livello rischio

# 5 Risultato dell’analisi del rischio

Sulla base degli input utilizzati, sono stati effettuati i calcoli per determinare i valori di rischio visualizzabili in maniera interattiva direttamente sullo strumento all’indirizzo indicato nella Tabella 1.

I risultati sono rappresentati in un grafico a barre contenente:

- la distribuzione dei record (minaccia-asset-vulnerabilità) per fasce di rischio;

- la numerosità di record contenuti in ogni fascia di rischio;

- la suddivisione dei record in tre zone di compliance rispetto alla soglia di rischio accettabile:

  - valori accettabili -\> valore rischio basso

  - valori limite -\> valore rischio medio

  - superiori al rischio accettabile -\> valore rischio alto.

<img src="MDPR33.1.A - Report Analisi dei Rischi - 2026/media/image6.png" style="width:6.6in;height:1.75556in" />

Figura - Distribuzione rischio

E in un grafico a torta contenente:

- La distribuzione degli asset secondo i livelli di rischio basso-medio-alto

- La distribuzione dei record secondo i livelli di rischio basso-medio-alto.

<img src="MDPR33.1.A - Report Analisi dei Rischi - 2026/media/image7.png" style="width:6.6in;height:1.75556in" />

Figura - Distribuzione rilievi e asset

È possibile visualizzare per ogni fascia di rischio le vulnerabilità e minacce coinvolte ordinate per asset.

Similmente per ogni per ogni asset è rappresentato il colore della fascia più alta in cui si esso colloca (Figura 10)

- Rosso: valore non accettabile;

- Giallo: valore limite;

- Verde: valore accettabile;

<img src="MDPR33.1.A - Report Analisi dei Rischi - 2026/media/image8.png" style="width:4.72541in;height:0.98342in" />

Figura - Colore rischio asset

**Il risultato dell’analisi del rischio evidenzia che TUTTI gli asset sono sotto la soglia di rischio accettabile e quindi nessun asset con rischio ALTO.**

**Tuttavia l’organizzazione prende in considerazione i record sul valore di soglia di rischio accettabile, pari a 22 record relativi a 5 asset.**

Di seguito verranno analizzati:

- Gli asset con valore di rischio pari alla soglia di rischio accettabile e ritenuti necessari di successivo trattamento per ridurre il rischio da parte dell’azienda.

1)  **valore di rischio nell’intervallo 41 – 45 coinvolti 5 Asset**

**Livello di Rischio: 41 - 45**

> Gli asset riportati di seguito presentano un rischio compreso tra 41 e 45: 5 asset per un totale di 22 record.

| ID Asset                                         | Valore di rischio MAX |
|--------------------------------------------------|-----------------------|
| A002 - Software Firma Digitale                   | 45                    |
| A0017 - Software di Messaggistica                | 45                    |
| A0039 - Codici sorgenti di proprietà dei clienti | 45                    |
| A0049 - Reputazione dell’azienda – Fiducia       | 45                    |
| A0048 - Immagine dell’azienda - Affidabilità     | 45                    |

| **ID Asset**                                                                               | **Descrizione** | **Classe Asset**                                                           | **Criticità** | **Minaccia**                                                | **Livello Impatto Minaccia** | **Vulnerabilità**                                                      | **Livello Impatto Vulnerabilità** | **Valore di Rischio** |
|--------------------------------------------------------------------------------------------|-----------------|----------------------------------------------------------------------------|---------------|-------------------------------------------------------------|------------------------------|------------------------------------------------------------------------|-----------------------------------|-----------------------|
| A002 – Software Firma Digitale                                                             | \-              | Dispositivi Crittografici                                                  | 5             | Obsolescenza                                                | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A002 – Software Firma Digitale                                                             | \-              | Dispositivi Crittografici                                                  | 5             | Errore del Personale                                        | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A002 – Software Firma Digitale                                                             | \-              | Dispositivi Crittografici                                                  | 5             | Inosservanza delle politiche di sicurezza aziendali         | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A002 – Software Firma Digitale                                                             | \-              | Dispositivi Crittografici                                                  | 5             | Malfunzionamento Software Applicativo/SO                    | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A002 – Software Firma Digitale                                                             | \-              | Dispositivi Crittografici                                                  | 5             | Malfunzionamento Software di base                           | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0017 – Software di Messaggistica                                                          | \-              | Applicazioni Commerciali                                                   | 5             | Malfunzionamento Software Applicativo/SO                    | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0017 – Software di Messaggistica                                                          | \-              | Applicazioni Commerciali                                                   | 5             | Accesso non autorizzato alla rete, sw di base, applicazioni | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0017 – Software di Messaggistica                                                          | \-              | Applicazioni Commerciali                                                   | 5             | Malfunzionamento Software di Base                           | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0017 – Software di Messaggistica                                                          | \-              | Applicazioni Commerciali                                                   | 5             | Inadeguate misure di protezione dei dati                    | 3                            | Mancanza di tracciabilità delle operazioni eseguite sulle applicazioni | 3                                 | 45                    |
| A0039 – Codici sorgenti di proprietà dei clienti                                           | \-              | Codici sorgente                                                            | 5             | Errore del personale                                        | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0039 – Codici sorgenti di proprietà dei clienti                                           | \-              | Codici sorgente                                                            | 5             | Inosservanza delle politiche di sicurezza aziendali         | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0039 – Codici sorgenti di proprietà dei clienti                                           | \-              | Codici sorgente                                                            | 5             | Malfunzionamento Software Applicativo/SO                    | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0039 – Codici sorgenti di proprietà dei clienti                                           | \-              | Codici sorgente                                                            | 5             | Accesso non autorizzato alla rete, sw di base, applicazioni | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0039 – Codici sorgenti di proprietà dei clienti                                           | \-              | Codici sorgente                                                            | 5             | Malfunzionamento Software di Base                           | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0049 – Reputazione dell’azienda – Fiducia && A0048 – Immagine dell’azienda – Affidabilità | \-              | Reputazione dell’azienda – Fiducia && Immagine dell’azienda - Affidabilità | 5             | Errore del personale                                        | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0049 – Reputazione dell’azienda – Fiducia && A48 – Immagine dell’azienda – Affidabilità   | \-              | Reputazione dell’azienda – Fiducia && Immagine dell’azienda - Affidabilità | 5             | Inosservanza delle politiche di sicurezza aziendali         | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0049 – Reputazione dell’azienda – Fiducia && A48 – Immagine dell’azienda – Affidabilità   | \-              | Reputazione dell’azienda – Fiducia && Immagine dell’azienda - Affidabilità | 5             | Malfunzionamento Software Applicativo/SO                    | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |
| A0049 – Reputazione dell’azienda – Fiducia && A48 – Immagine dell’azienda – Affidabilità   | \-              | Reputazione dell’azienda – Fiducia && Immagine dell’azienda - Affidabilità | 5             | Malfunzionamento Software di base                           | 3                            | Mancato processo di gestione delle configurazioni                      | 3                                 | 45                    |

La tabella sopra riportata evidenzia le minacce e le vulnerabilità a cui sono esposti gli asset.  
  
Data ultimo aggiornamento 24/09/2026
