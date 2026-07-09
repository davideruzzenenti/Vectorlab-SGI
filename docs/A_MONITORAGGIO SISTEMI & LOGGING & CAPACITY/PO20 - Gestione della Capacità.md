# PO20 - Gestione della Capacità

**Politica di Gestione della Capacità**

### Revisioni

|          |            |                 |             |               |
| -------- | ---------- | --------------- | ----------- | ------------- |
| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | RSGI        | Amministratore Unico |
|          |            |                 |             |               |
|          |            |                 |             |               |
|          |            |                 |             |               |

# Introduzione

# Scopo

La presente politica ha lo scopo di definire le modalità di gestione
della capacità aziendale, dei servizi e delle risorse tecnologiche di
Vectorlab, in termini operativi e di controllo.

# Campo di applicazione

Questo documento si applica a tutti gli ambiti e ai processi aziendali
coinvolti nell’implementazione della ISO/IEC 27001.

#  Riferimenti e Allegati

> PO27 - Gestione Eventi e Incidenti

> PR19.1 - Gestione del Cambiamento

> PR20.1 - Capacità, Logging e Monitoraggio Tecnico.

# Definizioni, Acronimi, Abbreviazioni

> AdS - Amministratore di Sistema

> CI – Configuration Item

> Hardening – “Rafforzamento” dei sistemi, ovvero l’insieme di
> operazioni
> di [configurazione](https://it.wikipedia.org/wiki/Configurazione_\(informatica\))
> che mirano a minimizzare l'impatto di possibili [attacchi
> informatici](https://it.wikipedia.org/wiki/Attacco_informatico) sugli
> stessi

> IAM – Identity and Access Management

> IoT – Internet of Things

> LAN - Local Area Network

> MFA – Multi Factor Authentication

> VPN - Virtual Private Network

> WAP – Wireless Access Point.

# Responsabilità

RSGI ha la responsabilità di redigere, mantenere aggiornata e comunicare
la presente politica.

Il personale, a qualsiasi livello, e i collaboratori esterni devono
attenersi alle procedure definite dall’Organizzazione per assicurarsi
che la presente Politica sia correttamente applicata.

I responsabili dell’attuazione della presente politica sono:

  - ………..

# Violazione della Politica

Qualsiasi azione non conforme alla politica aziendale di Vectorlab sarà
considerata una violazione della sicurezza e come tale potrà tradursi
nella sospensione dell'accesso alle aree e alle risorse informatiche,
rete e documenti. L'uso improprio degli strumenti aziendali costituisce
una grave violazione del dovere di correttezza e può comportare
l'adozione di provvedimenti disciplinari in conformità alla normativa
vigente.

# Riesame

La revisione di tale politica è effettuata da RSGI almeno una volta
all'anno e prima del riesame della Direzione, e in risposta a
cambiamenti significativi dell'ambiente organizzativo, del business, di
riferimenti normativi o dell’ambiente tecnologico aziendale. Il riesame
è condotto per valutare l'efficienza e l'efficacia del sistema e per
assicurare che siano implementate le azioni necessarie per consentire il
miglioramento continuo secondo i requisiti definiti dai sistemi di
gestione e in tutte le situazioni per le quali è richiesta una modifica
dell'attività aziendale che possa anche avere impatto sulla qualità,
sulla sicurezza delle informazioni o sull'operatività.

# Politica di Gestione della Capacità

Il processo di Gestione della Capacità è incentrato sulle prestazioni e
sulle problematiche di capacità relative alle risorse umane, alle
risorse tecnologiche e alle risorse strumentali impiegate per erogare le
proprie attività di business e i propri servizi.

Le risorse tecnologiche, umane e strutturali devono essere adeguate alle
necessità dell’Azienda e dei clienti e devono soddisfare i requisiti
attuali e futuri in modo tempestivo ed economico.

Devono essere identificati i requisiti di capacità, tenendo conto delle
criticità aziendali relative alle risorse che sono fondamentali per
l’erogazione dei servizi. La messa a punto e il monitoraggio delle
risorse si applicano per garantirne e, ove necessario, migliorarne la
disponibilità e l'efficienza.

I controlli devono essere messi in atto per indicare i problemi a tempo
debito. Le previsioni dei futuri requisiti di capacità devono tenere
conto dei nuovi requisiti aziendali e delle tendenze attuali e previste
nella capacità di elaborazione delle informazioni dell'organizzazione.

Il processo di Capacity Management riguarda i seguenti aspetti:

  - comprensione delle esigenze del servizio e delle capacità di carico
    e piani futuri per la sua crescita o riduzione;

  - analisi delle prestazioni sulla capacità del personale in relazione
    al carico di lavoro e alle competenze necessarie per gestire con
    successo le attività assegnate;

  - analisi delle prestazioni derivante dalla raccolta dei dati di
    misurazione, compresa l’analisi dell’impatto delle nuove versioni di
    software sulla capacità;

  - ottimizzazione delle prestazioni delle attività per garantire l'uso
    più efficiente dell'infrastruttura esistente;

  - trend di utilizzo delle risorse informatiche;

  - pianificazione della capacità di storage, hardware, software e
    risorse dell'infrastruttura di connessione necessarie per un periodo
    di tempo definito (es. annualmente) o in caso di evento
    significativo di change;

  - monitoraggio delle prestazioni e del throughput o del carico su
    server, server farm o cloud;

  - analisi delle prestazioni dei dati di misurazione, compresa
    l’analisi dell’impatto delle nuove versioni di software sulla
    capacità.

Alcuni dei vantaggi del processo di gestione della capacità efficace ed
efficiente sono:

  - garantire che le risorse sia umane sia infrastrutturali siano
    pianificate per soddisfare le esigenze attuali e future;

  - ridurre gli incidenti legati alla capacità attraverso previsioni
    preventive delle prestazioni;

  - garantire che gli aggiornamenti siano pianificati, messi a budget e
    implementati prima della violazione degli SLA (in termini di
    disponibilità o prestazioni);

  - procurare vantaggi finanziari evitando gli acquisti in situazioni di
    emergenza.

Le fasi principali del processo di Capacity Management sono le seguenti:

1)  pianificazione della capacità,

2)  dimensionamento delle risorse,

3)  monitoraggio dell'utilizzo e delle prestazioni delle risorse,

4)  reportistica e gestione delle azioni correttive.

Il processo di Capacity Management deve essere condotto da tre diverse
prospettive, per questo motivo si articola in tre sottoprocessi
paralleli che includono tutte le 4 fasi appena indicate e che di seguito
elenchiamo:

  - gestione della capacità aziendale;

  - gestione della capacità del servizio;

gestione della capacità delle risorse tecnologiche.

# Principi

L’implementazione del processo di gestione della configurazione prevede
il rispetto dei seguenti principi di sicurezza:

  - per tutto l’hardware, il software, i servizi e le reti di Vectorlab
    devono essere applicate le configurazioni standard definite, incluse
    le configurazioni di sicurezza o “hardening”, prima della loro
    implementazione nell’ambiente ICT aziendale;

  - il deployment di nuovi sistemi, pc, apparati, ecc. deve tenere conto
    dell'esistenza di configurazioni standard, le quali devono essere
    sempre usate come base di partenza a garanzia di sicurezza;

  - eventuali eccezioni devono essere documentate, motivate,
    autorizzate, tracciate nel tempo e riesaminate a cadenza regolare
    per verificare nel tempo la loro validità;

  - tutte le configurazioni standard devono essere sempre disponibili e
    riviste periodicamente per garantire che soddisfino i requisiti
    stabiliti dalla presente politica;

  - laddove possibile, devono essere utilizzati modelli standard per
    documentare la corretta configurazione (incluse le impostazioni
    sicurezza necessarie) di ogni componente ICT (come “*MDPR23.1-*
    *Piano di Gestione delle Vulnerabilità \[progetto\]*”). Questi
    stessi modelli sono soggetti a modifiche e controllo delle versioni,
    al netto di cambiamenti nel panorama delle minacce e vulnerabilità e
    di aggiornamenti hardware e software;

  - i dettagli delle configurazioni di base devono essere considerati
    informazioni riservate e, pertanto, devono essere protette da
    accessi e modifiche non autorizzate;

  - nel caso in cui il monitoraggio delle configurazioni evidenzi
    scostamenti dalla baseline, essi devono essere analizzati e, se
    necessario, corretti;

  - possono essere utilizzati strumenti automatizzati per
    l’identificazione, la documentazione e il monitoraggio delle
    modifiche, affinché vi sia la sicurezza di tenere traccia di ogni
    cambiamento e segnalare e correggere le non conformità;

  - affinché sia garantita l’integrità delle informazioni di
    configurazione, l’ambiente di gestione delle configurazioni
    dovrebbe:

<!-- end list -->

  - essere dimensionato per la mole di documenti da gestire (hardware,
    software, dati, documenti),

  - garantire adeguata protezione da corruzione e modifiche non
    autorizzate,

  - garantire il recupero in caso di disastro.

# Fasi della Gestione della Configurazione

Il processo di gestione della configurazione prevede lo svolgimento
delle seguenti attività:

1.  **Identificazione** - Si definisce un inventario degli elementi da
    gestire, come hardware, software, firmware e documentazione.

2.  **Configurazione standard** - Si stabiliscono e documentano
    configurazioni standard approvate per ogni elemento, incluse le
    specifiche ed i requisiti di funzionalità e sicurezza e le relazioni
    con altri elementi. Tali standard diverranno il punto di riferimento
    per apportare ulteriori ottimizzazioni rispetto a specifiche
    esigenze aziendali e per gestire tutte le successive modifiche.

3.  **Controllo delle modifiche** - La fase di controllo delle modifiche
    assicura che siano opportunamente richiesti, valutati, approvati e
    documentati tutti i cambiamenti alle configurazioni standard. Un
    aspetto importante è la capacità di identificare le relazioni
    intercorrenti fra gli elementi della configurazione, poiché un
    cambiamento potrebbe avere impatto sugli elementi della
    configurazione interconnessi. Il controllo delle modifiche avviene
    in conformità a quanto definito nel documento “*PR19.1 - Gestione
    del Cambiamento*”.

4.  **Monitoraggio dello status** - Si monitora continuamente lo stato
    degli elementi per identificare eventuali problemi o deviazioni
    dagli standard definiti nelle baseline. Una volta implementate le
    modifiche, la registrazione del nuovo status permette di individuare
    come le modifiche hanno influenzato o alterato quello esistente,
    rendendo tracciabili gli elementi della configurazione durante tutto
    il corso del loro sviluppo e operatività. In pratica, si dovrebbe
    essere in grado di conoscere su quale versione si trova la
    configurazione ed avere un record storico delle vecchie versioni.

5.  **Verifica e auditing** - Si eseguono regolarmente verifiche per
    assicurarsi che le modifiche siano state applicate correttamente e
    che le configurazioni degli elementi siano conformi alle politiche
    di sicurezza ed agli standard aziendalmente definiti, ossia ai
    requisiti ed alle informazioni di configurazione iniziali. Questo
    può includere audit tecnici e scansioni di sicurezza.

Maggiori dettagli sulla gestione della configurazione sono presenti
nella procedura “*PR32.1 - Gestione delle Configurazioni*”.

# Interazioni ***con gli altri processi aziendali***

Il processo di gestione della configurazione, nell’applicazione delle
sue varie fasi, interagisce con altri processi del Sistema di Gestione
Integrato, i quali garantiscono l’implementazione di ulteriori attività
parallele e conseguenti alla gestione della configurazione.

  - <span class="underline">Gestione delle vulnerabilità
    tecniche</span>: identificare e correggere le vulnerabilità
    derivanti da configurazioni errate o non aggiornate. Ciò si realizza
    tramite la tempestiva applicazione di patch e aggiornamenti.
    Maggiori dettagli sono riportati nei documenti “*PR23.1 - Gestione
    delle Vulnerabilità Tecniche*” e “*PR22.1 - Gestione delle Patch*”.

  - <span class="underline">Gestione dei backup:</span> creare e
    mantenere un repository centralizzato e un backup delle
    configurazioni critiche per garantirne la disponibilità ed il rapido
    ripristino in caso di guasti o attacchi informatici. Il processo è
    descritto nel documento “*PR21.1 - Gestione dei Backup e Restore”.*

  - <span class="underline">Monitoraggio e logging</span>: implementare
    sistemi di monitoraggio e logging sul repository centralizzato in
    modo da tracciare le modifiche alle configurazioni e rilevare
    eventuali attività sospette o non autorizzate. Tali attività sono
    riportate nel documento “*PR20.1 - Capacità, Logging e Monitoraggio
    Tecnico”.*

  - <span class="underline">Formazione e consapevolezza</span>: educare
    il personale del reparto IT e gli utenti finali sull'importanza
    della gestione delle configurazioni e su come contribuire a
    mantenere un ambiente sicuro. Una procedura ben definita di gestione
    delle configurazioni aiuta a prevenire incidenti di sicurezza,
    riduce i tempi di risposta agli incidenti (poiché è più rapido
    ripristinare i sistemi partendo da una configurazione sicura) e
    garantisce che i sistemi siano sempre allineati con le best
    practices di sicurezza e le normative di settore.

# Configurazione sicura

L’Azienda definisce le configurazioni di base dei seguenti CI:

  - dispositivi endpoint (desktop, laptop, telefoni cellulari, ecc.)

  - reti e dispositivi di rete fisici (router, switch, firewall, ecc.)

  - server fisici e/o virtuali (sistemi operativi, database, web server,
    ecc.)

  - infrastruttura cloud (reti, storage, ecc.)

  - dispositivi IoT.

Per ogni categoria sopra elencata, è importante definire la
configurazione sicura degli elementi che dovrebbe declinare, per quanto
applicabile in base alla tipologia di CI, i seguenti elementi:

  - bloccare l’installazione di software da parte degli utenti,

  - bloccare le connessioni non sicure, per esempio quelle basate su
    protocolli non cifrati,

  - installare, mantenere aggiornato e attivo un software anti-malware,

  - installare, mantenere aggiornato e attivo un personal firewall,

  - configurare la connessione con un sistema di backup,

  - sconnettere automaticamente le sessioni non usate dopo un certo
    periodo di tempo,

  - concedere l’accesso al sistema solo con un sistema di
    autenticazione,

  - bloccare l’accesso dopo un certo periodo di inattività e concederlo
    solo con un sistema di autenticazione,

  - cifrare il disco,

  - eliminare le utenze standard (root e admin),

  - cambiare le password di default,

  - eliminare i servizi e software non necessari,

  - sincronizzare gli orologi con un server NTP unico per tutta
    l’Organizzazione,

  - installare strumenti per la cancellazione sicura,

  - installare un sistema per la cancellazione da remoto dei dati
    (remote wiping),

  - bloccare le porte USB e SD.

Tutte le informazioni sulla configurazione sicura devono essere parte
integrante della configurazione standard definita.

# Configurazione dei Dispositivi Endpoint

### Gestione per la Connessione dei Dispositivi 

I dispositivi endpoint che si connettono alla rete interna di Vectorlab
devono essere configurati in modo sicuro, in particolare le password e
gli utenti di default (escluse quelle necessarie ad operazioni dell’AdS)
devono essere disattivati e appropriati criteri per la gestione delle
password devono essere adottati. Ulteriori dettagli sono riportati in
“*PO16 - Gestione degli Accessi*”.

### Sincronizzazione degli Orologi

Tutti i computer che hanno un sistema operativo desktop installato (i.e.
Windows, Ubuntu), devono essere configurati in modo da avere la
sincronizzazione degli orologi automatica da parte del sistema
operativo.

# Configurazione della Rete Interna

La configurazione della rete interna di Vectorlab deve assicurare
un'adeguata segregazione degli accessi tra le aree di gestione delle
informazioni protette e le aree destinate alla navigazione esterna.

Vengono applicate regole per la gestione dei seguenti aspetti:

  - la sicurezza perimetrale, con definizione dei "confini" della rete
    interna;

  - la difesa in profondità, con l'utilizzo di dispositivi di sicurezza
    di vario tipo e a diversi livelli all'interno del sistema
    informativo aziendale.

### Gestione della LAN

Il rispetto dei seguenti aspetti, attraverso l'utilizzo di adeguata
strumentazione hardware e software, permette di gestire correttamente la
LAN, garantendone la protezione:

  - **sicurezza di rete**, ottenuta mediante l'utilizzo di firewall,
    antivirus, antispam, controllo accessi, segregazione, pronta
    installazione di patch atte a risolvere problematiche esistenti;

  - **prestazioni di rete**, ottenute gestendo la larghezza di banda
    disponibile e controllando l'accesso alle connessioni WiFi;

  - **accessibilità alla rete**, ottenuta limitando e controllando le
    connessioni remote;

  - **monitoraggio della rete**, realizzato attraverso il controllo dei
    log, apparato per apparato, di tutte le apparecchiature di rete.

### Gestione della Rete Wireless 

L'installazione della rete wireless aziendale deve essere effettuata a
valle dello studio di un appropriato posizionamento dei punti di accesso
e dei vincoli strutturali, al fine di evitare fenomeni di "sniffing"
all'esterno dell’edificio.

I WAP, dispositivi collegati alla rete cablata che permettono la
fruizione della rete wireless da parte dei dispositivi che vi si
connettono, devono essere posizionati in punti non facilmente
accessibili dell’ufficio per ridurre le probabilità di danni accidentali
da parte di personale e visitatori, e utilizzare i più aggiornati
protocolli crittografici di sicurezza per proteggere le reti di computer
wireless.

### Segregazione delle Reti 

L’Azienda definisce, sia nel caso di LAN che di rete wireless, una
segregazione delle reti in modo da garantire la sicurezza nelle
comunicazioni e scambio di informazioni all’interno delle varie
sottoreti (ad esempio una sottorete wireless “guest” per gli ospiti che
possa soltanto navigare verso l’esterno ma che non abbia accessi
interni) e ridurre le possibilità di intercettazione di informazioni da
parte di interni malintenzionati o di esterni che hanno ottenuto accesso
ad una parte della rete.

### Gestione del Firewall

Per garantire un adeguato livello di sicurezza della rete interna, sono
messe in atto regole appropriate per limitare il traffico in entrata e
in uscita tra segmenti di rete, in particolare:

  - vengono utilizzati filtri per bloccare la trasmissione di tutti i
    dati e i pacchetti di controllo non necessari;

  - i segmenti della rete interna sono isolati secondo lo schema di rete
    “*ALPR24.1.A - Schema di Rete*”;

  - eventuali regole contrarie e cambiamenti devono essere chiaramente
    tracciate come modifiche alla configurazione nel sistema di
    ticketing aziendale.

# Configurazione della Rete Esterna

La protezione perimetrale deve garantire adeguati livelli di sicurezza
contro le minacce su Internet e gli attori ostili. Il traffico esterno
deve essere limitato in misura sufficiente a ciò che è necessario per
svolgere le funzioni aziendali. Il firewall deve essere configurato per
garantire un’adeguata protezione.

### Restrizioni nell’uso di Internet 

Le connessioni ad Internet devono essere adeguatamente protette da
controlli che consentano l’identificazione di attori ostili e che
impediscano possibili intrusioni sui sistemi informatici.

### Crittografia delle Connessioni di Rete

Le connessioni da client remoti devono essere sicure e avvenire
attraverso l’uso di meccanismi di protezione, quali:

  - crittografia durante le transazioni con protocolli sicuri e testati
    sul campo, frequentemente rivisti;

  - protocolli di autenticazione sicuri.

### Gestione della Virtual Private Network – VPN

Le connessioni VPN garantiscono una connessione sicura tra due punti
dislocati geograficamente.

Il personale all’esterno della sede aziendale deve connettersi via VPN
al fine di essere sotto la protezione del firewall aziendale per
navigare e per accedere ai dati presenti nei server aziendali interni.

# Configurazione di Server Fisici e Software di Sistema

La configurazione dei server fisici e del software di sistema
all'interno dell'Organizzazione deve garantire la sicurezza,
l'affidabilità e l'efficienza operativa delle risorse IT.

### Gestione dei Server Fisici

Alcune regole per la configurazione dei server fisici:

  - devono essere scelti in base alle esigenze specifiche del carico di
    lavoro, alla scalabilità e alle performance richieste assieme ad una
    valutazione dei requisiti di alimentazione e raffreddamento;

  - devono essere acquistati da fornitori selezionati;

  - devono essere installati in un ambiente sicuro, preferibilmente in
    un data center con controllo di accesso fisico, con cablaggio e
    connettività di rete sicure;

  - devono avere a corredo una documentazione completa che includa la
    configurazione hardware, il numero di serie, la posizione fisica e
    il contatto per il supporto.

### Gestione del Software di Sistema:

Per quanto riguarda la configurazione del software di sistema:

  - deve essere scelto in base alle esigenze operative e di sicurezza
    dell'Organizzazione, tenendo in considerazione le licenze, il
    supporto del fornitore e la compatibilità con l'hardware;

  - deve essere installato seguendo le linee guida del fornitore,
    modificando secondo le proprie baseline le configurazioni
    predefinite per migliorarne la sicurezza e le performance;

  - devono essere installati regolarmente aggiornamenti di sicurezza e
    patch per mantenere il software aggiornato e sicuro. Gli
    aggiornamenti devono essere testati in un ambiente di test prima
    della distribuzione in produzione;

  - gli account utente devono essere gestiti con criteri di password
    robusti e privilegi minimi e quelli inutilizzati devono essere
    disattivati o rimossi;

  - devono essere implementati regolari backup dei dati e delle
    configurazioni di sistema. I piani di ripristino devono essere
    testati periodicamente per garantire la continuità operativa.

# Configurazione dell’Infrastruttura Cloud

La configurazione di un’infrastruttura cloud deve seguire alcune
indicazioni:

1)  **Configurazione delle risorse**

<!-- end list -->

  - Provisioning delle risorse di calcolo:

      - configurare le macchine virtuali (VM) o i container necessari
        per i carichi di lavoro,

      - scegliere le dimensioni delle VM o i tipi di istanze in base
        alle esigenze di performance e scalabilità.

<!-- end list -->

2)  **Impostazione dello storage**

<!-- end list -->

  - Selezionare i tipi di storage appropriati (SSD, HDD, ecc.)

  - Configurare le politiche di backup e recupero dei dati

<!-- end list -->

3)  **Configurazione della rete**

<!-- end list -->

  - Creare reti virtuali per isolare le risorse

  - Configurare subnet, gateway di rete, firewall e gruppi di sicurezza

  - Implementare VPN o connessioni dirette per l'accesso sicuro alla
    rete

<!-- end list -->

4)  **Gestione delle identità e degli accessi (IAM):**

<!-- end list -->

  - Configurare ruoli e politiche IAM per gestire l'accesso e i permessi
    degli utenti

  - Implementare l'autenticazione multifattore (MFA) per aumentare la
    sicurezza degli accessi

<!-- end list -->

5)  **Crittografia:**

<!-- end list -->

  - Abilitare la crittografia dei dati a riposo e in transito

  - Utilizzare servizi di gestione delle chiavi per la gestione sicura
    delle chiavi di crittografia

<!-- end list -->

6)  **Monitoraggio e logging:**

<!-- end list -->

  - Configurare i servizi di monitoraggio per monitorare le risorse e le
    performance

  - Abilitare il logging delle attività e delle configurazioni

<!-- end list -->

7)  **Gestione delle vulnerabilità**:

<!-- end list -->

  - Eseguire regolari vulnerability assessment e penetration test

  - Applicare tempestivamente patch di sicurezza e aggiornamenti del
    software.

# Configurazione dei dispositivi IoT

Nel seguito, si riportano alcune regole generali per la configurazione
sicura dei dispositivi IoT:

  - scegliere produttori affidabili che garantiscano l’implementazione
    di adeguate misure di sicurezza in fase di setup dei dispositivi e
    che offrano un supporto costante e regolare degli aggiornamenti di
    sicurezza;

  - installare regolarmente tali aggiornamenti.

  - aggiornare regolarmente il firmware dei dispositivi per garantire
    che siano protetti dalle ultime minacce informatiche;

  - impostare password complesse per l’accesso ai dispositivi e
    cambiarle regolarmente;

  - utilizzare i dispositivi su VPN;

  - utilizzare tecniche di crittografia nella trasmissione delle
    informazioni.