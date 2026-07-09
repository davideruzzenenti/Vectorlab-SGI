# ALPO20.A - Piano di Capacità

**Piano di Capacità**

### Revisioni

|          |            |                 |             |               |
| -------- | ---------- | --------------- | ----------- | ------------- |
| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | RSGI        | Amministratore Unico |
| 0.1      | 09/07/2026 | Revisione assistita da IA: adattamento del template al contesto cloud-first (risorse AWS/Aruba/Google Workspace, valori in EUR); rimozione di esempi server-room e placeholder | RSGI | Amministratore Unico |
|          |            |                 |             |               |

# 

# Introduzione 

Il presente Piano di Capacità soddisfa le esigenze di capacità di
Vectorlab e l’effettiva capacità delle attuali risorse di soddisfarle.
Inoltre, fornisce raccomandazioni per l'adeguamento della capacità
attuale in linea con i requisiti futuri prima che vengano raggiunte le
soglie e il servizio ne risenta.

# Scopo

Questo documento rappresenta il Piano di Capacità per il servizio
erogato da Vectorlab nel periodo di 12 mesi a partire dalla data di
emissione. Esso
tiene conto delle richieste future dei Clienti e le bilancia con
l'attuale utilizzo dei vari componenti del servizio, al fine di arrivare
a un piano di azione consigliato per garantire che il servizio sia
mantenuto in maniera efficiente. Inoltre, ha lo scopo di sviluppare gli
strumenti e i metodi utilizzati per consentire una registrazione più
accurata dell'utilizzo corrente e la previsione delle esigenze future.

# Metodi utilizzati per la stesura del Piano di Capacità

Le informazioni sull'utilizzo futuro dei servizi chiave vengono raccolte
nell'ambito del normale processo di Gestione del Servizio (RIF.
DOCUMENTO); ai Clienti del servizio è richiesto di evidenziare eventuali
aumenti o diminuzioni noti nell'utilizzo dei servizi esistenti e
qualsiasi altro evento aziendale che possa avere un impatto
sull'effettiva fornitura del servizio.

I dati relativi all'utilizzo corrente delle risorse tecniche vengono
raccolti tramite diversi strumenti di monitoraggio e vengono analizzati
trimestralmente per identificare le tendenze.

Nella redazione del presente Piano sono state fatte le seguenti
assunzioni:

  - le previsioni sull'utilizzo futuro sono accurate, sia in termini di
    tempo che di grado di cambiamento,

  - le misurazioni dell'attuale utilizzo della capacità sono
    rappresentative della domanda.

Queste ipotesi saranno riesaminate su base regolare per valutare la loro
continua validità.

# Domanda di servizi attuale e prevista

Diversi sono gli aspetti commerciali, tecnici, statutari, normativi e
contrattuali che potrebbero potenzialmente avere un impatto sulla
capacità del servizio nel periodo considerato.

1.  1.  # Modifiche che incidono sui requisiti di capacità

Si prevede che le seguenti modifiche avranno un impatto sulla capacità
da fornire nei prossimi 12 mesi:

  - avvio di nuovi progetti/commesse con nuovi ambienti applicativi su
    AWS;

  - crescita del numero di servizi/container in produzione;

  - variazioni dell’organico (nuove assunzioni) con impatto su licenze
    Google Workspace e postazioni;

  - sviluppo di prodotti proprietari e attività di R\&S ad alto uso di
    risorse di calcolo (es. workload AI/GPU).

Ciascuno di questi elementi può avere un impatto sulla capacità delle
risorse cloud e sui relativi costi.

# Tendenze

Alcune delle tendenze generali che avranno un impatto sulla capacità
sono:

  - Tassi di registrazione e fidelizzazione di nuovi Clienti

  - Aumento dell'utilizzo del sito web da parte dei Clienti

  - Utilizzo dello smart working

  - Utilizzo del BYOD

  - XXXX

Queste aree saranno monitorate nel tempo per vedere come si sviluppano.

# Riepilogo e raccomandazioni sui servizi e sulle risorse

La tabella seguente riassume l'attuale utilizzo della capacità dei
servizi di Vectorlab con indicazione delle modifiche previste per l'anno
finanziario in corso e delle raccomandazioni per le modifiche apportate,
al fine di garantire che venga fornita una capacità sufficiente per far
fronte ai cambiamenti previsti.

<table>
<tbody>
<tr class="odd">
<td><p><strong>RISORSA</strong></p>
<p><strong>(tecnologica, umana, finanziaria)</strong></p></td>
<td><strong>DESCRIZIONE</strong></td>
<td><strong>SERVIZIO(I)</strong></td>
<td><strong>UTILIZZO ATTUALE</strong></td>
<td><strong>PREVISIONALE</strong></td>
<td><strong>PROPOSTE</strong></td>
<td><strong>PRIORITÀ</strong></td>
</tr>
<tr class="even">
<td>AWS (ECS/EC2)</td>
<td>Ambiente di produzione container applicativi</td>
<td>Servizi back-end erogati ai clienti</td>
<td>da compilare</td>
<td>da compilare</td>
<td>Scale-up/scale-out del servizio (tier successivo)</td>
<td>da compilare</td>
</tr>
<tr class="odd">
<td>AWS (S3/EFS)</td>
<td>Storage dati applicativi e backup</td>
<td>Conservazione dati e backup</td>
<td>da compilare</td>
<td>da compilare</td>
<td>Adeguamento dello spazio/tier</td>
<td>da compilare</td>
</tr>
<tr class="even">
<td>Server Aruba</td>
<td>Infrastruttura specifica gestita in IaC (incl. Bitwarden)</td>
<td>Servizi interni</td>
<td>da compilare</td>
<td>da compilare</td>
<td>Adeguamento risorse del server</td>
<td>da compilare</td>
</tr>
<tr class="odd">
<td>Google Workspace</td>
<td>Postazioni/licenze utente</td>
<td>Collaborazione e posta</td>
<td>da compilare</td>
<td>Variabile con l’organico</td>
<td>Adeguamento numero licenze</td>
<td>da compilare</td>
</tr>
</tbody>
</table>

2.  1.  # Aggiornamenti del servizio richiesti

Nell'arco di tempo coperto dal presente Piano di Capacità sono stati
individuati i seguenti potenziamenti del servizio.

<table>
<tbody>
<tr class="odd">
<td><p><strong>RISORSA</strong></p>
<p><strong>(tecnologica, umana, finanziaria)</strong></p></td>
<td><strong>AGGIORNAMENTO RICHIESTO</strong></td>
<td><strong>SOGLIA</strong></td>
<td><strong>TEMPISTICA</strong></td>
<td><strong>COSTI</strong></td>
</tr>
<tr class="even">
<td>AWS (servizio applicativo)</td>
<td>Passaggio al tier successivo</td>
<td>da compilare</td>
<td>da compilare</td>
<td>€ da compilare</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Impatto delle nuove tecnologie

L’adozione di servizi cloud gestiti e di container (AWS, server Aruba in
IaC) consente di adeguare dinamicamente le risorse in funzione della
domanda, riducendo la necessità di sovradimensionamento. L’eventuale
introduzione di workload ad alto uso di calcolo (es. GPU per attività
AI/computer graphics) richiederà un’attenta valutazione delle
implicazioni in termini di capacità e costi.

# Altre raccomandazioni

A seguito di questa revisione vengono formulate le seguenti
raccomandazioni aggiuntive:

1.  Gli aggiornamenti elencati nella Tabella 2 devono essere acquistati
    nei tempi indicati

2.  Dovrebbe essere mantenuto il monitoraggio dei consumi delle risorse
    cloud (dashboard AWS CloudWatch e console Aruba/Google Workspace)
    per individuare tempestivamente scostamenti e ottimizzare i costi

3.  I servizi aggiuntivi dovrebbero essere incorporati in questo piano
    il prima possibile (ad esempio nuovi servizi cloud attivati)