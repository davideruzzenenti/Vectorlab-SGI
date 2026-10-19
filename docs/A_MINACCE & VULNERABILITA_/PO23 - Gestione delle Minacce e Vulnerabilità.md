# PO23 - Gestione delle Minacce e Vulnerabilità

**Politica Gestione delle Minacce e Vulnerabilità**

### Revisioni

|          |            |                 |             |               |
|----------|------------|-----------------|-------------|---------------|
| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | CISO        | CDA           |
|          |            |                 |             |               |
|          |            |                 |             |               |
|          |            |                 |             |               |

### Indice 

[Revisioni [1](#revisioni)](#revisioni)

[Indice [2](#indice)](#indice)

[1 Introduzione [3](#introduzione)](#introduzione)

[1.1 Scopo [3](#scopo)](#scopo)

[1.2 Campo di applicazione [3](#campo-di-applicazione)](#campo-di-applicazione)

[1.3 Riferimenti e Allegati [3](#riferimenti-e-allegati)](#riferimenti-e-allegati)

[1.4 Definizioni, Acronimi, Abbreviazioni [3](#definizioni-acronimi-abbreviazioni)](#definizioni-acronimi-abbreviazioni)

[1.5 Responsabilità [4](#responsabilità)](#responsabilità)

[1.6 Violazione della Politica [4](#violazione-della-politica)](#violazione-della-politica)

[1.7 Riesame [4](#riesame)](#riesame)

[2 Gestione delle Minacce e delle Vulnerabilità [5](#gestione-delle-minacce-e-delle-vulnerabilità)](#gestione-delle-minacce-e-delle-vulnerabilità)

[2.1 Monitoraggio delle minacce [5](#monitoraggio-delle-minacce)](#monitoraggio-delle-minacce)

[2.1.1 Livello strategico [6](#livello-strategico)](#livello-strategico)

[2.1.2 Livello tattico [6](#livello-tattico)](#livello-tattico)

[2.1.3 Livello operativo [7](#livello-operativo)](#livello-operativo)

[2.2 Rilevamento e Trattamento delle Vulnerabilità [7](#rilevamento-e-trattamento-delle-vulnerabilità)](#rilevamento-e-trattamento-delle-vulnerabilità)

[2.2.1 Cosa è una vulnerabilità tecnica [7](#cosa-è-una-vulnerabilità-tecnica)](#cosa-è-una-vulnerabilità-tecnica)

[2.2.2 Vulnerability Assessment e Penetration Test [8](#vulnerability-assessment-e-penetration-test)](#vulnerability-assessment-e-penetration-test)

[2.3 Analisi del Rischio alla Sicurezza delle Informazioni [9](#analisi-del-rischio-alla-sicurezza-delle-informazioni)](#analisi-del-rischio-alla-sicurezza-delle-informazioni)

[2.4 Condivisione e Diffusione delle Informazioni sui rischi [10](#condivisione-e-diffusione-delle-informazioni-sui-rischi)](#condivisione-e-diffusione-delle-informazioni-sui-rischi)

[2.5 Formazione [10](#formazione)](#formazione)

# Introduzione

# Scopo

Lo scopo di questa politica è duplice e si riferisce ai due elementi fondamentali che contribuiscono alla definizione del rischio che può incombere sugli asset dell’Organizzazione: le minacce e le vulnerabilità.

Da un lato, la presente politica definisce l’approccio che Vectorlab adotta per il monitoraggio delle minacce alla sicurezza informatica a cui l’Azienda stessa è oggettivamente esposta in base alle caratteristiche del proprio business; dall’altro, descrive i criteri in base ai quali l'Organizzazione svolge attività di individuazione e gestione delle vulnerabilità che caratterizzano i propri asset, tecnologici e no, con l’obiettivo di valutare accuratamente i rischi, gestire gli incidenti e implementare i controlli in modo appropriato.

# Campo di applicazione

La presente politica si applica a tutto il personale IT, al personale che si occupa di gestire la sicurezza delle informazioni, al personale afferente all’area di sviluppo del software e al personale che implementa e mantiene la sicurezza dell'organizzazione.

# Riferimenti e Allegati

> PO27 – Gestione degli Incidenti
>
> PR23.1 – Gestione delle Vulnerabilità Tecniche
>
> PR23.2 – Monitoraggio delle Minacce
>
> PR27.1 – Gestione degli Incidenti e dei Data Breach
>
> PR33.1 – Processo Analisi del Rischio e Trattamento
>
> MDPR33.1.A – Report Analisi dei Rischi
>
> MDPR33.1.B – Piano di Trattamento dei Rischi
>
> MDPR23.1.A - Piano di Gestione delle Vulnerabilità Tecniche \[progetto\]
>
> MDPR23.2.A - Monitoraggio delle minacce

# Definizioni, Acronimi, Abbreviazioni

> Black Box – Modalità di test “a scatola chiusa” dove il tester non ha alcuna informazione sul sistema che sta testando, a parte l’indirizzo IP o l’URL
>
> CISO – Chief Information Security Officer
>
> CVSS - Common Vulnerability Scoring System
>
> DAST - Dynamic Application Security Testing
>
> IOC – Indicatori di compromissione
>
> OWASP – Open Web Application Security Project
>
> PT – Penetration Test
>
> RSGI – Responsabile del Sistema di Gestione Integrato
>
> SGI – Sistema di Gestione Integrato
>
> SIEM – Security Information and Event Management
>
> SSL – Secure Sockets Layer
>
> VA – Vulnerability Assessment
>
> White Box – Modalità di test invasivo dove il tester ha accesso completo al codice sorgente e all’architettura del sistema

# Responsabilità

Il CISO ha la responsabilità di redigere, mantenere aggiornata e comunicare la presente politica.

Il personale, a qualsiasi livello, e i collaboratori esterni devono attenersi alle procedure definite dall’Organizzazione per assicurarsi che la presente politica sia correttamente applicata.

I responsabili dell’attuazione della presente politica sono:

- CISO, che monitora la gestione di minacce e vulnerabilità e garantisce la corretta implementazione della attività di trattamento delle stesse;

- RSGI, che facilita l’attuazione della presente politica attraverso norme e procedure appropriate;

- IT, che effettua le attività di monitoraggio delle minacce e VA/PT;

- tutto il personale di Vectorlab, a cui sono assegnati precisi ruoli e responsabilità in materia di sicurezza delle informazioni.

# Violazione della Politica

Qualsiasi azione non conforme alla politica aziendale dell’Organizzazione sarà considerata una violazione della sicurezza e come tale si tradurrà nella revoca dell'accesso alle aree e alle risorse informatiche, rete e documenti. L'uso improprio degli strumenti aziendali costituisce una grave violazione del dovere di correttezza e può comportare l'adozione di provvedimenti disciplinari in conformità alla normativa vigente.

I casi gravi saranno segnalati all'autorità competente e potranno essere oggetto di provvedimenti disciplinari o legali.

#  Riesame

La revisione di tale politica è effettuata dalla Direzione almeno una volta all'anno e prima del riesame della Direzione, e in risposta a cambiamenti significativi dell'ambiente organizzativo, del business, di riferimenti normativi o dell’ambiente tecnologico aziendale. Il riesame è condotto per valutare l'efficienza e l'efficacia del sistema e per assicurare che siano implementate le azioni necessarie per consentire il miglioramento continuo secondo i requisiti definiti dai sistemi di gestione e in tutte le situazioni per le quali è richiesta una modifica dell'attività aziendale che possa anche avere impatto sulla qualità e sulla sicurezza delle informazioni o sull'operatività.

# Gestione delle Minacce e delle Vulnerabilità

Vectorlab ha definito ed attua un processo per la gestione delle minacce e delle vulnerabilità che include varie attività, complementari tra di loro:

1)  Il monitoraggio periodico delle minacce (la c.d. “threat intelligence”), con lo scopo di raccogliere e analizzare, in maniera sistematica, le informazioni sulle minacce rilevanti per l’Azienda, provenienti da canali ufficiali appropriatamente individuati.

2)  La pianificazione ed esecuzione di attività di Vulnerability Assessment e Penetration Test (quest’ultimo quando necessario) per l’individuazione e trattamento delle vulnerabilità tecniche, di due tipi:

- **applicativo** riguardano tutte le verifiche effettuate sulle applicazioni ed effettuato se necessario come elemento di analisi e di supporto alla politica di sviluppo sicuro.

- **infrastrutturale** riguardano tutte le verifiche a livello di configurazione della rete, dei server ed eventualmente dei client pianificato ad intervalli regolari.

3)  L’analisi del rischio, nell’ambito della quale sono mappate le minacce e le vulnerabilità (non solo di tipo tecnico) afferenti agli asset oggetto dell’analisi.

4)  Il mantenimento di canali di comunicazione attivi tra le parti interessate, al fine di garantire lo scambio tempestivo di notizie in merito a minacce e vulnerabilità riscontrate nei propri prodotti e servizi e alle possibili soluzioni disponibili. Tali segnalazioni vengono gestisce dall’Organizzazione come incidenti secondo quanto descritto nella “*PO27 - Gestione degli Incidenti*”.

5)  Le campagne di formazione e le iniziative di sensibilizzazione del personale dell’Organizzazione, al fine di aumentarne la consapevolezza.

# Monitoraggio delle minacce

La conoscenza dei gruppi che sono attivi negli attacchi, dei loro obiettivi, delle loro motivazioni, tecnologie e tecniche è essenziale per garantire che la propria posizione di sicurezza rimanga pertinente alle minacce da affrontare e che si adatti all'evoluzione delle stesse.

La politica di Vectorlab prevede la raccolta e l’analisi delle minacce rilevanti per il settore e mercato di appartenenza e per il tipo di tecnologia o servizio che l’Azienda offre, da fonti autorevoli ed in maniera sistematica, secondo le attività descritte in “*PR23.2 – Monitoraggio delle Minacce*”.

La sistematicità che richiede questo tipo di attività permette al personale interno di essere sempre aggiornato sull’evoluzione delle cyberminacce e sulle principali tecniche di attacco utilizzate e, conseguentemente, di intraprendere, in maniera proattiva e grazie ad informazioni accurate e dettagliate, le opportune azioni di mitigazione. Pertanto, sono definiti e documentati processi e procedure per garantire che le attività di monitoraggio delle minacce siano strutturate e misurabili e che i risultati prodotti soddisfino gli standard richiesti.

Il monitoraggio delle minacce può essere svolto su tre livelli differenti, a scelta dell’Azienda a seconda delle parti interessate coinvolte, dei requisiti e degli obiettivi prefissati: strategico, tattico e operativo.

### Livello strategico

A livello strategico, l’attività di monitoraggio fornisce informazioni generali sul panorama globale delle minacce e su dove si colloca l’Azienda in tale scenario.

Sono raccolte e analizzate informazioni di alto livello riguardanti gruppi di attaccanti, le loro motivazioni, gli obiettivi tipici, i tipi di attacco e i correnti livelli di attività. È probabile che ciò includa la valutazione del livello di minaccia da parte di stati nazionali, bande criminali in paesi specifici, gruppi politicamente motivati e da specifici tipi di attacco come, ad esempio, il ransomware.

Le fonti di informazioni possono includere: agenzie governative, notizie e rapporti di alto livello di organizzazioni commerciali.

I dati emersi dall’analisi sono presentati annualmente dal CISO alla Direzione in occasione del Riesame sotto forma di trend e grafici che illustrano le tendenze delle minacce e dei vari attacchi nel settore di appartenenza e le motivazioni che espongono maggiormente alcuni asset dell’Organizzazione a determinate minacce. Questo consente alla Direzione di avere una visione complessiva delle minacce in un determinato momento, che può influire sul processo di valutazione del rischio, e di indirizzare le strategie e gli investimenti in materia di sicurezza allineandoli con le reali necessità di protezione dei sistemi aziendali.

### Livello tattico

A livello tattico, l’attività di monitoraggio fornisce informazioni circa le modalità in cui sono perpetrate le minacce, inclusi i vettori di attacco, gli strumenti e le tecnologie utilizzati dagli hacker, le tipologie di azienda o sistema presi di mira e le relative difese e strategie di elusione.

Le informazioni, a questo livello, sono raccolte più regolarmente e, in genere, devono essere comunicate più rapidamente all'interno dell'Organizzazione.

Le fonti di informazione possono includere: agenzie governative, blog e feed di notizie di organizzazioni commerciali, principali framework proposti da aziende e associazioni del settore.

I dati sono analizzati ed elaborati all’interno del team di sicurezza aziendale e verso il CISO, per individuare le specifiche aree di intervento ed i controlli di sicurezza da implementare.

### Livello operativo

A livello operativo, l’attività di monitoraggio fornisce informazioni che IT può utilizzare attivamente per contrastare un attacco specifico, anche in corso.

Infatti, le informazioni sono raccolte ed elaborate in molti casi in tempo reale e riguardano attacchi specifici e potenzialmente in corso.

A questo livello c'è un forte legame con il processo di gestione degli incidenti di sicurezza delle informazioni (descritto in “*PR27.1 - Gestione degli Incidenti e dei Data Breach*”), che consente di reagire a una compromissione effettiva o sospetta dei sistemi, e con il processo di gestione delle vulnerabilità (descritto in “*PR23.1 - Gestione delle vulnerabilità*”), che si occupa di applicare patch e trattare i punti deboli.

Le fonti di informazione possono includere: sistemi e strumenti di monitoraggio, le iscrizioni a gruppi di discussione governativi, industriali o locali e gli avvisi emessi da terze parti.

# Rilevamento e Trattamento delle Vulnerabilità

L’identificazione delle vulnerabilità consente di evidenziare quali sono gli elementi di criticità specifici, sui quali si può verificare una situazione di rischio.

Le vulnerabilità si possono considerare come:

- una caratteristica intrinseca all’asset o al servizio considerato,

- la mancata applicazione di un controllo (contromisura) previsto dallo schema di riferimento.

Pertanto, è possibile affermare che nessun asset è completamente immune da vulnerabilità: esse possono essere identificate nei sistemi informatici (sviluppati internamente o acquisiti da terze parti), nell’ambito della scurezza fisica, nelle procedure e anche nei processi dell’Organizzazione.

Attraverso l’identificazione ed il trattamento delle vulnerabilità e, parallelamente, il monitoraggio delle minacce, l’Azienda è in grado di evidenziare quelli che sono i maggiori rischi che incombono sulla propria Organizzazione ed il conseguente livello di protezione dei propri sistemi.

### Cosa è una vulnerabilità tecnica

Una vulnerabilità è comunemente definita come "*una debolezza intrinseca in un sistema informativo, nelle procedure di sicurezza, in controlli interni o in una implementazione che potrebbe essere sfruttata da una minaccia*".

Il processo di sviluppo del software, per esempio, è complicato e il suo output sotto forma di programmi software è raramente privo di bug. La maggior parte di questi bug influisce sulla funzionalità del software in modo che non funzioni come previsto. Inoltre, se manipolati nel modo corretto, alcuni di essi possono consentire a un utente malintenzionato di ottenere una qualche forma di vantaggio o accesso che non era previsto dallo sviluppatore. Questo tipo di bug è considerato una vulnerabilità del software.

Queste vulnerabilità vengono costantemente individuate e corrette tramite aggiornamenti software o patch. La politica di Vectorlab, in relazione alle vulnerabilità tecniche, è di esserne a conoscenza e di chiuderle ove possibile, direttamente o con altri mezzi. Maggiori dettagli sono riportati nella “*PR23.1 – Gestione delle vulnerabilità tecniche*”.

### Vulnerability Assessment e Penetration Test

Il **Vulnerability Assessment (VA)** esterno/interno prevede l’esecuzione di scansioni non invasive, condotte attraverso l’utilizzo di specifici strumenti (leader di mercato) accuratamente selezionati, al fine di rilevare la presenza di vulnerabilità note. Il VA si propone di enumerare il maggior numero di *security issue* presenti sui target senza concentrarsi su un particolare scenario di sfruttamento e attacco.

Tali scansioni sono successivamente integrate da verifiche manuali, volte ad eliminare i falsi positivi e negativi eventualmente introdotti dagli strumenti di analisi automatica.

L’attività di **Penetration Test (PT)** ha l’obiettivo di simulare le operazioni eseguite da un agente di minaccia (hacket) che miri a compromettere i requisiti di sicurezza associati all’infrastruttura informatica oggetto di analisi. Il test consiste in un tentativo di penetrazione dall’esterno della rete del cliente finalizzato al prendere il controllo di target di più alto valore (per esempio il Domain Controller) e a recuperare informazioni relative all’organizzazione.

Il test ha lo scopo di ottenere privilegi di accesso alla rete interna o al controllo totale della stessa.

Queste verifiche sono finalizzate a controllare la configurazione dei server e della rete ospitante al fine di evidenziare gli aspetti legati alla sicurezza quali:

- livello di hardening della infrastruttura,

- livello di patching dei sistemi operativi e relativi middleware,

- presenza di applicazioni e servizi vulnerabili, pericolosi o non necessari,

- corretta implementazione delle credenziali di sicurezza,

- modalità di comunicazione tra servizi e da/verso l’esterno,

- ecc.

L’attività di **Web Application Penetration Test** ha lo scopo di sfruttare le vulnerabilità delle applicazioni web che sempre più spesso rappresentano un veicolo per penetrare in un'azienda, arrecarle danni o sfruttarla per portare attacchi verso terzi.

A livello applicativo, si provvede ad analizzare nel dettaglio i meccanismi di controllo implementati nell’applicazione oggetto di analisi per garantire la sicurezza.

In particolare, secondo quanto previsto dalle linee guida OWASP (Open Web Application Security Project) si provvede a verificare la corretta gestione dei meccanismi di autenticazione, la capacità di gestire correttamente gli input utente e tutte quelle situazioni che possono portare l’applicazione ad avere comportamenti difformi da quanto originariamente previsto.

Il test è volto ad evidenziare se l’applicazione è vulnerabile, a titolo di esempio, alle seguenti famiglie di tecniche di attacco:

- Sql Injection

- Frame Injection

- Cross Site Scripting

- Buffer Overflow

- Attacco ai protocolli di sicurezza (SSL, ecc.)

- Man-in-the middle

- ecc.

In particolare, vengono testati tutti i meccanismi inerenti alla gestione delle sessioni, all’autenticazione, a meccanismi di encryption, error handling, ecc.

Viene prevista un’attività di tipo Black Box, finalizzata alla verifica della resistenza dell’applicazione a tentativi di attacco senza il possesso di credenziali legittime rilasciate dal cliente.

Il test viene poi esteso alla modalità White Box, ossia utilizzando credenziali valide con differenti livelli di autorizzazione, se disponibili.

Il test viene effettuato con tecniche prevalentemente manuali.

# Analisi del Rischio alla Sicurezza delle Informazioni

A seconda del perimetro di riferimento, la mappatura delle principali minacce che possono incombere sugli asset e delle relative vulnerabilità consente a Vectorlab di calcolare, attraverso l’ausilio di uno strumento software, i rischi a cui sono esposte le informazioni e gli asset aziendali.

Le valutazioni vengono fatte in termini qualitativi, da un punto di vista soggettivo e tradotte poi, dallo strumento stesso, in numeri per una più facile elaborazione dei risultati.

Le vulnerabilità considerate nell’ambito dell’analisi di rischio sono di tipo tecnico ma anche ambientale, organizzativo ed operativo in quanto relazionate a differenti tipologie di asset e di minacce che includono sia la parte tecnologica che quella gestionale del sistema informativo.

Ogni vulnerabilità viene associata alla minaccia (o minacce) in grado di sfruttarla e la coppia è valorizzata sulla base delle caratteristiche intrinseche dell’asset sul quale incombe e/o sulla presenza/efficacia di contromisure implementate per la protezione dell’asset stesso.

Per maggiori dettagli sulla metodologia utilizzata per lo svolgimento dell’analisi del rischio e della mappatura di minacce e vulnerabilità, si veda il documento “*ALPR09.1.A - Metodologia Analisi del Rischio”*.

Le evidenze di tale attività vengono riportate in un report di analisi del rischio, secondo il modello “*MDPR09.1.C - Report analisi dei rischi*” e trattate attraverso un piano, secondo il modello “*MDPR09.1.D - Piano di trattamento dei rischi*”.

# Condivisione e Diffusione delle Informazioni sui rischi

La condivisione e diffusione delle informazioni relative alle minacce e alle vulnerabilità tra le Organizzazioni, specie se appartenenti allo stesso settore di business, consente di definire politiche collettive di prevenzione, individuazione, valutazione e monitoraggio dei rischi informatici al fine di contenerne più rapidamente la diffusione e, allo stesso tempo, impedire il potenziale rispettivo contagio.

La politica di Vectorlab è quella di stabilire relazioni con altre organizzazioni per consentire di acquisire e condividere informazioni circa il diffondersi delle minacce informatiche, ad esempio nello stesso settore, nello stesso luogo o utilizzando la stessa tecnologia, e le relative vulnerabilità (virus, attacchi ecc.). Ciò può includere anche la partecipazione attiva a forum di condivisione delle informazioni, ma è necessario prestare attenzione che le informazioni fornite dai dipendenti rimangano conformi alle procedure interne di gestione degli incidenti (ad esempio durante una violazione attiva).

# Formazione

Con il costante aumento delle minacce e la forte dipendenza dalle nuove tecnologie, saper comprendere e gestire correttamente i rischi cyber è diventato essenziale: la formazione in materia di cybersecurity è uno strumento fondamentale per trasformare la percezione del rischio in consapevolezza che il rischio è reale e che occorre adottare e mantenere comportamenti più prudenti.

La politica di Vectorlab garantisce un aggiornamento costante del personale sulle minacce attuali, compresi gli attacchi più recenti, le vulnerabilità comuni e le tattiche degli aggressori; la pianificazione della formazione può includere dimostrazioni pratiche su come avvengono gli attacchi e come possono essere prevenuti o mitigati e simulazioni di attacco che aiutano a comprendere meglio i pericoli reali e le conseguenze potenziali degli attacchi informatici.

La formazione deve essere periodica e sempre allineata al panorama in continua evoluzione delle minacce e delle vulnerabilità.
