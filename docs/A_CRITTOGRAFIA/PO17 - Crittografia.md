# PO17 - Crittografia

Politica Crittografia

### Revisioni

|          |            |                 |             |               |
|----------|------------|-----------------|-------------|---------------|
| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | CISO        | CDA           |
|          |            |                 |             |               |
|          |            |                 |             |               |
|          |            |                 |             |               |

### Indice 

<span id="_Toc65593031" class="anchor"></span>

# Introduzione

# Scopo

Il presente documento delinea le modalità di uso dei controlli crittografici per la protezione delle informazioni e la gestione delle chiavi crittografiche attraverso tutto il loro ciclo di vita in Vectorlab.

Le tecniche di cifratura devono garantire una o più delle seguenti caratteristiche:

- <u>riservatezza</u>: proprietà per la quale le informazioni sono rese disponibili o divulgate solo ad individui o processi autorizzati;

- <u>integrità</u>: garanzia che le informazioni siano protette da modifiche accidentali o non autorizzate (alterazione, cancellazione o aggiunta) a seguito di errori, malfunzionamenti o di azioni volontarie;

- <u>autenticazione</u>: proprietà per la quale è garantito che l’identità di un soggetto o di una risorsa che richiedono l’accesso o che effettuano una transazione sia quella dichiarata;

- <u>non ripudio</u>: capacità di dimostrare che un’azione o un evento hanno avuto luogo, in modo tale che il soggetto che compie l’azione non possa ripudiarla successivamente.

L’utilizzo della crittografia ha lo scopo di proteggere le informazioni conservate in asset fisici e garantire trasmissioni sicure delle stesse attraverso canali di comunicazione.

È necessario anche tener presente che la crittografia può rallentare l'elaborazione e la trasmissione delle informazioni; pertanto, è importante comprendere i rischi e bilanciare i controlli ad un livello adeguato mantenendo gli obiettivi di protezione.

# Campo di applicazione

La politica di crittografia si applica a tutta l’azienda, nell’implementazione di prodotti e servizi le cui informazioni necessitino di tecniche di cifratura. Inoltre, deve essere tenuta in considerazione nell’ambito della definizione degli accordi con qualsiasi soggetto esterno che debba implementare o utilizzare sistemi crittografici.

#  Riferimenti e Allegati

> MDPR08.1.A – Elenco Informazioni documentate
>
> PO15 - Classificazione delle Informazioni
>
> PO16 - Gestione degli Accessi
>
> PR24.1 - Gestione delle reti.

# Definizioni, Acronimi, Abbreviazioni

> AES – Advanced Encryption Standard
>
> CEO - Chief Executive Officer
>
> CISO - Chief Information Security Officer
>
> HTTP - HyperText Transfer Protocol
>
> HTTPS - HyperText Transfer Protocol over Secure Socket Layer
>
> IT – Information Technology
>
> NIST – National Institute of Standards and Technology
>
> PEC – Posta Elettronica Certificata
>
> SGI - Sistema di Gestione Integrato
>
> SSH – Secure Shell
>
> SSL – Secure Sockets Layer
>
> SW - Software
>
> TLS – Transport Layer Security
>
> VPN – Virtual Private Network
>
> WPA2-PSK – Wi-Fi Protected Access II pre-shared key.

# Responsabilità

CISO ha la responsabilità di redigere, mantenere aggiornata e comunicare la presente politica.

Il personale, a qualsiasi livello, e i collaboratori esterni devono attenersi alle procedure definite dall’Organizzazione per assicurarsi che la presente Politica sia correttamente applicata.

I responsabili dell’attuazione della presente politica sono:

- la Direzione di Vectorlab che stabilisce i criteri di accettazione e i livelli di accettabilità del rischio e fornisce le risorse necessarie per garantire la corretta applicazione

- CISO, come sopra indicato;

- Digital IT, nell’identificare le soluzioni tecniche migliori per applicare la seguente politica;

- Digital – SW Development, nell’identificare le soluzioni tecniche migliori per applicare la seguente politica nell’area di competenza;

- tutto il personale di Vectorlab, come sopra indicato.

Tutto il personale può segnalare eventuali difformità e suggerire potenziali miglioramenti finalizzati ad incrementare l’efficacia di questa politica.

# Violazione della Politica

Qualsiasi azione non conforme alla politica aziendale di Vectorlab sarà considerata una violazione della sicurezza e come tale potrà tradursi nella sospensione dell'accesso alle aree e alle risorse informatiche, rete e documenti. L'uso improprio degli strumenti aziendali costituisce una grave violazione del dovere di correttezza e può comportare l'adozione di provvedimenti disciplinari in conformità alla normativa vigente.

#  Riesame

La revisione di tale politica è effettuata da CISO almeno una volta all'anno e prima del Riesame della direzione. Il riesame è condotto per valutare l'efficienza e l'efficacia del sistema e per assicurare che siano implementate le azioni necessarie per consentire il miglioramento continuo secondo i requisiti definiti dai sistemi di gestione e in tutte le situazioni per le quali è richiesta una modifica dell'attività aziendale che possa anche avere impatto sulla sicurezza delle informazioni o sull'operatività.

# Crittografia

La presente politica definisce l’utilizzo della crittografia applicata alla gestione delle informazioni e in particolare ai dati personali, in accordo con il sistema di gestione integrato e con i requisiti cogenti in ambito di protezione dei dati, dei servizi e delle strutture.

Vengono gestiti i seguenti aspetti di sicurezza:

- controlli crittografici applicati a differenti categorie di asset logici e fisici e le modalità di applicazione, il cui dettaglio viene definito da procedure o specifiche progettuali;

- modalità con cui vengono generate, conservate, gestite, recuperate ed eliminate le chiavi crittografiche, interne ed esterne;

- algoritmi e corrispondenti livelli minimi di crittografia ammessi.

# Categorie di applicazioni della crittografia

La gestione della cifratura relativa ai sistemi aziendali è applicata alle seguenti categorie:

- asset fisici o fisicamente disponibili;

- asset logici, accessi e protocolli di rete.

Sono di seguito indicate le norme generali da rispettare in caso di utilizzo della crittografia.

### Asset fisici

Di seguito viene data evidenza degli asset fisici a cui può essere applicata la crittografia:

1.  Dispositivi fisici dotati di software di gestione dei dati:

    - <u>Server, laptop e PC fissi</u>: protezione attraverso software di cifratura dei dischi (Bitlocker o analoghi) qualora siano archiviati dati che necessitino di cifratura al fine di garantire particolari requisiti di riservatezza. Il software utilizzato deve consentire la gestione centralizzata delle chiavi di cifratura.

    - <u>Macchine virtuali</u>: sono considerate analogamente a server, laptop e PC fissi. Le eventuali macchine virtuali che contengono dati personali verranno protette mediante crittografia di uno o più dei seguenti metodi:

      - Crittografia totale del disco;

      - Crittografia della partizione;

      - Crittografia della home directory.

2.  Dispositivi fisici per la conservazione dei dati:

    - <u>Chiavette USB e altri dispositivi di archiviazione esterna</u>: protezione attraverso software di cifratura qualora contengano dati che necessitino di cifratura al fine di garantire particolari requisiti di riservatezza. Questa valutazione viene effettuata in fase di assegnazione dell’asset alla risorsa o qualora emergano rischi in momenti successivi.

> Il software utilizzato deve garantire la gestione centralizzata delle chiavi di cifratura.

- <u>Dischi utilizzati per il backup sicuro di dati personali e particolari, archivi di e-mail ed altri dati</u>: le procedure di backup devono garantire che i dati con particolari requisiti di riservatezza vengano crittografati in accordo con le normative che lo prevedono. I dispositivi che effettuano il salvataggio di dati e le memorie utilizzate sono accessibili solo dal personale autorizzato.

3.  Dispositivi per la gestione di chiavi crittografiche

    - Dispositivi per la firma digitale.

La scelta di utilizzare la crittografia nei dispositivi sopra elencati viene effettuata in fase di setup dell’asset e prima di un eventuale assegnazione alle risorse o in momenti successivi qualora si evidenziassero nuovi rischi e sempre in relazione alla classificazione delle informazioni in esso contenute nel rispetto della politica “*PO15 - Classificazione delle Informazioni*”.

Le chiavi crittografiche utilizzate devono, ove possibile, essere gestite centralmente ed archiviate in luogo sicuro. Le eventuali chiavi o password non gestite centralmente devono garantire, oltre ad un analogo livello di sicurezza, un adeguato sistema di ripristino dei dati in caso di perdita o smarrimento della chiave da parte dell’utilizzatore.

### Asset Logici, accessi e protocolli di rete

Rientrano in questa categoria tutti quegli asset che hanno natura puramente logica senza dimensione materiale, ad esclusione delle macchine virtuali: ad esempio canali sicuri di comunicazione, e-mail, protocolli di autenticazione, certificati di firma, transazioni web, password etc.

**Protocolli di crittografia applicati a canali protetti di comunicazione**:

- <u>Amministrazione remota dei sistemi</u>: tutti i sistemi devono essere amministrati attraverso connessioni crittografate (SSH, HTTPS, etc.) considerate sicure.

- <u>Collegamenti dall’esterno della sede aziendale verso la rete interna</u>: tutti i collegamenti dall’esterno verso le reti gestite da Vectorlab devono essere crittografati, in particolare:

  - Collegamenti VPN che transitano da rete esterna: rientrano in questa tipologia le connessioni VPN di dipendenti, collaboratori esterni e fornitori. Tali connessioni devono obbligatoriamente rientrare nella gestione centralizzata di apparati di rete che garantiscano adeguata crittografia del collegamento. La gestione è in carico al fornitore del servizio.

  - Collegamenti VPN da clienti o da fornitori dall’esterno delle sedi aziendali verso macchine situate in data center: tali connessioni devono obbligatoriamente rientrare nella gestione centralizzata di apparati di rete che garantiscano adeguata crittografia del collegamento, vedi punto precedente.

  - Collegamenti Wi-Fi:

    - Collegamenti wireless su rete interna: utilizzo di protocolli sicuri per l’accesso alla rete (WPA2-PSK).

    - Wi-Fi rete Guest: Connessione tramite voucher (cfr. “*PR24.1 - Gestione delle reti*”).

**Protocolli di sicurezza applicati alla posta elettronica**:

- <u>Crittografia delle email</u>: quando è necessario inviare e-mail con particolari requisiti di sicurezza l’azienda fa uso della PEC seguendo le regole tecniche di AGID.

> Tale sistema garantisce integrità dei messaggi in transito, non ripudio e marca temporale. Le chiavi crittografiche sono a carico del fornitore del servizio.

- <u>Invio e ricezione di file e documenti crittografati e/o firmati</u>: in caso di necessità di sicurezza nel trasferimento di file da e verso l’esterno dell’azienda debbono essere utilizzati sistemi crittografici. In particolare:

  - Invio puntuale di file crittografati e/o firmati verso l’esterno dell’azienda: Utilizzo strumenti per la crittografia di file e cartelle che utilizzino protocolli crittografici come AES-256 o livelli crittografici equivalenti eventualmente accoppiati con protocolli di compressione (es. zip, rar). Risulta necessaria la comunicazione della chiave privata (es. password) su canale sicuro. Le chiavi private sono a carico dell’utente.

  - Certificati e chiavi di firma: utilizzo di strumenti e certificati per la firma digitale acquisiti dal fornitore di PEC aziendale (cfr. “*MDPR08.1.A – Elenco Informazioni documentate/Tools*”). La gestione delle chiavi risulta a carico dell’utente.

**Protezione dei servizi web e altre applicazioni**:

- <u>Protezione del protocollo HTTP</u>: per tutte le pagine che necessitano di transazioni sicure e/o autenticazione viene utilizzato il protocollo HTTPS. I certificati utilizzati vengono acquisiti ed emessi da autorità certificatrici verificate o, in alcuni casi, generati internamente (a carico IT).

**Gestione delle password**:

- <u>Conservazione delle password</u>: le password di accesso ai sistemi sono crittografate tramite metodi di hashing (es. KeePass) ed accessibili solo al personale autorizzato.

# Gestione delle chiavi

La gestione, la protezione e l'uso di chiavi crittografiche durante l'intero ciclo di vita prevedono:

- acquisizione dall’esterno;

- generazione attraverso apparati interni e gestione sicura degli stessi;

- gestione, distribuzione e conservazione;

- recupero;

- revoca e cancellazione.

Vengono dettagliate le modalità a seconda che le chiavi siano generate internamente o esternamente.

### Chiavi generate internamente

Le chiavi originate internamente su dispositivi fisici, ove necessario, sono le seguenti:

- password di dispositivi;

- password del software di cifratura dei dischi (es. <span class="mark">Bitlocker</span>);

- certificati autogenerati dai singoli sistemi e/o applicazioni per protezione SSL/TLS di siti web e servizi ad uso interno.

Tutti i dispositivi che generano le chiavi sono accessibili unicamente al personale autorizzato.

Le chiavi, non divulgate, devono essere protette da un utilizzo non autorizzato e mantenute in appositi repository sotto la gestione degli aventi diritto.

Nel caso di chiavi autogenerate risulta invece necessaria la sostituzione puntuale.

Al fine di gestire eventuali problematiche di recupero, le chiavi <span class="mark">Bitlocker</span> sono site in una chiavetta USB e conservata nella cassaforte Vectorlab la cui gestione delle chiavi fisiche è descritta nella politica “*PO16 - Gestione degli Accessi*”.

### Chiavi generate esternamente

Le chiavi di origine esterna sono le seguenti:

- la firma digitale;

- certificati per protezione HTTPS di siti web acquisiti da Certification Authority riconosciuta.

La loro acquisizione dall’esterno, attraverso canali sicuri e doppia autenticazione dell’autorità emittente, avviene secondo procedura dettata dal fornitore. Esse possono essere salvate in appositi repository protetti o password manager, sotto la gestione degli aventi diritto, es. amministratori di sistema, secondo procedure apposite. Nel caso di revoca di chiavi (es. firme digitali, chiave per crittografia e-mail, ...) vengono utilizzati i processi definiti dal fornitore.

# Algoritmi crittografici e livelli minimi ammessi

È necessario utilizzare servizi, funzioni e algoritmi crittografici la cui robustezza sia comprovata da certificazioni e standard riconosciuti a livello internazionale e che risultino esenti da vulnerabilità note.

Viene quindi aggiornato da CISO con il supporto di reparto IT l’elenco dei protocolli crittografici considerati come sicuri seguendo i più diffusi standard di sicurezza (es. NIST).

Tali protocolli (o suite di protocolli) / algoritmi / best practices sono gli unici ad essere utilizzati all’interno di procedure tecniche o di progetti di Vectorlab.
