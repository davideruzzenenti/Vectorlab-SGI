# PO40 - Gestione Sicurezza nell_uso dei Servizi Cloud

Politica Gestione Sicurezza nell’uso dei Servizi Cloud

### Revisioni

|          |            |                 |             |               |
| -------- | ---------- | --------------- | ----------- | ------------- |
| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | CISO        | Amministratore Unico |
|          |            |                 |             |               |
|          |            |                 |             |               |
|          |            |                 |             |               |
|          |            |                 |             |               |

# Introduzione

# Scopo

Il presente documento definisce i principi generali per l’utilizzo in
sicurezza dei servizi cloud in Vectorlab, siano essi di tipo SaaS, PaaS
e/o IaaS.

# Campo di applicazione

Questa politica si applica a tutti i servizi che Vectorlab gestisce in
cloud, incluse tutte le informazioni (anche dati personali) relative
agli utenti, sia interni che clienti, di tali servizi.

In particolare, si concentra nell’indirizzare gli aspetti di sicurezza
pertinenti a:

  - modalità di conservazione e localizzazione dei dati,

  - modalità di fruizione dei servizi cloud,

  - gestione degli accessi,

  - gestione degli asset,

  - gestione degli ambienti multi-tenant,

  - gestione degli account amministrativi.

# Riferimenti e Allegati

> MDPR26.1.A – Monitoraggio fornitori

> PO15 – Classificazione delle Informazioni

> PR.26.1 – Gestione dei Fornitori

> REG01 – Regolamento di utilizzo degli strumenti informatici aziendali.

# Definizioni, Acronimi, Abbreviazioni

> CSP – Cloud Service Provider

> IaaS – Infrastructure-as-a-Service. Servizio di cloud computing che
> eroga risorse di virtualizzazione, memorizzazione, rete e server.

> PaaS – Platform-as-a-Service. Servizio di cloud computing che
> fornisce, oltre a quanto previsto da IaaS, risorse come sistema
> operativo, database, piattaforma di sviluppo, server Web ecc.

> SaaS – Software-as-a-Service. Servizio di cloud computing che offre
> agli utenti finali un’applicazione cloud, munita di piattaforme e
> dell’infrastruttura cloud che la supporta, generalmente fruibile
> tramite browser web.

# Responsabilità

Il CISO ha la responsabilità di redigere, mantenere aggiornata e
comunicare la presente politica.

Il personale, a qualsiasi livello, e i collaboratori esterni devono
attenersi alle procedure definite dall’Organizzazione per assicurarsi
che la presente politica sia correttamente applicata.

I responsabili dell’attuazione della presente politica sono:

  - Il CISO che determina le direttive presenti nel documento e
    indirizza la loro applicazione,

  - RSGI, che facilita l’attuazione della presente politica attraverso
    norme e procedure appropriate,

  - IT che opera secondo le direttive presenti nel documento,

  - tutto il personale di Vectorlab, a cui sono assegnati precisi ruoli
    e responsabilità in materia di sicurezza delle informazioni.

# Violazione della Politica

Qualsiasi azione non conforme alla politica aziendale
dell’Organizzazione sarà considerata una violazione della sicurezza e
come tale si tradurrà nella revoca dell'accesso alle aree e alle risorse
informatiche, rete e documenti. L'uso improprio degli strumenti
aziendali costituisce una grave violazione del dovere di correttezza e
può comportare l'adozione di provvedimenti disciplinari in conformità
alla normativa vigente.

I casi gravi saranno segnalati all'autorità competente e potranno essere
oggetto di provvedimenti disciplinari o legali.

#  Riesame

La revisione di tale politica è effettuata dalla Direzione almeno una
volta all'anno e prima del riesame della Direzione, e in risposta a
cambiamenti significativi dell'ambiente organizzativo, del business, di
riferimenti normativi o dell’ambiente tecnologico aziendale. Il riesame
è condotto per valutare l'efficienza e l'efficacia del sistema e per
assicurare che siano implementate le azioni necessarie per consentire il
miglioramento continuo secondo i requisiti definiti dai sistemi di
gestione e in tutte le situazioni per le quali è richiesta una modifica
dell'attività aziendale che possa anche avere impatto sulla qualità e
sulla sicurezza delle informazioni o sull'operatività.

# Gestione Sicurezza nell’uso dei Servizi Cloud

L'uso dei servizi cloud in qualità di *customer* comporta una
responsabilità condivisa e una collaborazione tra il fornitore di
servizi cloud e l’Organizzazione, al fine di garantire che la protezione
della riservatezza, integrità e disponibilità delle informazioni in
cloud avvenga in conformità ai requisiti di sicurezza sanciti
dall’Organizzazione stessa, in linea con le principali best practices
e normative in materia.

È fondamentale che la selezione e gestione dei servizi cloud avvenga in
modo che i dati siano adeguatamente protetti in base al loro valore
aziendale e alla loro classificazione. Da ciò si desume che le
responsabilità di entrambe le parti devono essere chiaramente
identificate ed implementate in modo appropriato in tutte le fasi del
rapporto (acquisizione, implementazione, uso, gestione e uscita dal
servizio cloud).

Vectorlab indirizza tutti gli aspetti di sicurezza negli accordi
stabiliti con i CSP e ne dà evidenza del loro periodico monitoraggio
nell’ambito della gestione e controllo dei rapporti con i fornitori,
all’interno del documento *“MDPR26.1.A – Monitoraggio fornitori”.*

Tutti gli asset in cloud di Vectorlab sono censiti nell’inventario degli
asset e sottoposti ad analisi del rischio in ambito ISO/IEC 27001,
relativo alla sicurezza delle informazioni, al fine di identificare i
rischi associati all'utilizzo dei servizi cloud.

Inoltre, molti servizi cloud sono basati e offerti su un'architettura
“multi-tenant”, dove l’infrastruttura è condivisa tra tutti i clienti
usufruenti del CSP, garantendo un’efficace separazione e indipendenza
reciproca.

# Fase di acquisizione dei servizi cloud

### Definizione dei requisiti

Prima di acquistare un servizio cloud è necessario definire chiaramente
quali sono i requisiti che devono essere soddisfatti dal punto di vista
commerciale, funzionale (in particolare, nel caso del SaaS) ma,
soprattutto, di sicurezza delle informazioni e protezione dei dati
personali.

Le aree in cui devono essere definiti i requisiti di sicurezza delle
informazioni possono includere:

  - le modalità di conservazione e accesso alle informazioni in cloud da
    parte del CSP;

  - la localizzazione geografica del CSP e i paesi in cui può conservare
    i dati di Vectorlab, anche temporaneamente, al fine di soddisfare
    gli obblighi di privacy. Devono essere stabilite anche eventuali
    note legali da applicare ai contratti in base alla legislazione
    attiva sul territorio;

  - come il CSP gestisce e mantiene gli asset di Vectorlab in cloud;

  - come il CSP classifica ed etichetta le informazioni;

  - se e come viene effettuato il mantenimento in ambienti cloud
    multi-tenant;

  - la creazione e gestione degli utenti comuni che fruiscono dei
    servizi cloud e il contesto in cui li usano;

  - la creazione e gestione degli utenti amministratori dei servizi
    cloud fruiti in modalità *customer*, dotati di accessi privilegiati;

  - la definizione di ruoli e responsabilità tra CSP e Organizzazione
    per lo svolgimento di attività operative quali:

      - crittografia dei dati, a riposo e in transito. Ove possibile, le
        chiavi di decifratura saranno in possesso dell’Organizzazione,
        anziché del CSP;

      - procedure di backup e ripristino;

      - gestione delle change, aggiornamenti e applicazione delle patch
        di sicurezza;

      - gestione delle configurazioni;

      - monitoraggio della capacity;

      - controlli anti-malware;

      - gestione delle vulnerabilità;

      - raccolta dei log di sicurezza;

  - controllo degli accessi, inclusa la disponibilità
    dell'autenticazione a più fattori (MFA);

  - le modalità di supporto da parte del CSP in caso di incidente
    relativo alla sicurezza delle informazioni e le modalità e
    tempistiche di notifica delle violazioni e di raccolta delle prove,
    anche utilizzabili per indagini forensi;

  - la gestione di eventuali sub-fornitori (sub-responsabili del
    trattamento) da parte del CSP;

  - le modalità di supporto da parte del CSP in caso di fuoriuscita dal
    servizio cloud;

  - la condivisione e restituzione di informazioni quali file di
    configurazione, codice sorgente e dati di proprietà di Vectorlab, in
    qualità di cliente del servizio cloud, quando richiesto durante la
    fornitura del servizio o al termine del servizio.

Se sono in uso più servizi cloud, Vectorlab può prendere in
considerazione ulteriori requisiti per gestirli in modo coordinato.

È importante che siano indirizzati controlli specifici che garantiscano
la corretta implementazione dei criteri di sicurezza per la protezione
dei dati personali in linea con la legislazione sulla privacy in vigore;
in caso di mancata coerenza, sarà necessario fornire un documento
ulteriore sulle modalità di utilizzo di tali dati.

Sulla base dell'elenco dei requisiti sopra identificati e dei criteri di
selezione, secondo quanto riportato nella procedura *“PR.26.1 – Gestione
dei Fornitori”*, sono valutati i potenziali fornitori di servizi cloud.

Generalmente, per assicurare una diligente applicazione dei controlli di
sicurezza delle informazioni, verranno privilegiati fornitori
certificati con lo standard internazionale ISO/IEC 27001 e,
eventualmente, anche conformi ai principi degli standard ISO/IEC 27017 e
ISO/IEC 27018, linee guida per i servizi in cloud.

# Fase di implementazione dei servizi cloud 

Una volta raggiunto l'accordo con il CSP prescelto, potrà iniziare
l'implementazione del servizio. A seconda della tipologia di servizio
coinvolto (SaaS, PaaS o IaaS), ciò può consistere in attività come la
configurazione (ad esempio la creazione di server virtuali),
l'installazione di software e il caricamento di dati, o la fruizione di
un’applicazione web.

Verrà effettuato il testing dei servizi cloud e la formazione sul loro
utilizzo e verrà verificato, almeno annualmente, il rispetto dei
requisiti di sicurezza e privacy delle informazioni, in linea con la
ripartizione concordata di ruoli e responsabilità tra Vectorlab e CSP.

# Fase di utilizzo e gestione dei servizi cloud

I servizi cloud verranno utilizzati come qualunque altro servizio e
asset aziendale, in conformità a quanto definito nel *“REG01 -
Regolamento di utilizzo degli strumenti informatici aziendali”* e in
base ai risultati del monitoraggio periodico del CSP. Tale monitoraggio
dovrebbe confermare che tutti i requisiti specificati nelle fasi
precedenti del processo siano stati soddisfatti e che, in caso
contrario, vengano intraprese azioni.

Le modifiche rilevanti ai servizi cloud avviate dal CSP (come il
trasferimento o la riconfigurazione del servizio o le modifiche ai
sub-responsabili del trattamento) devono essere comunicate a Vectorlab,
secondo quanto specificato negli accordi contrattuali.

# Fase di uscita dai servizi cloud

Nel caso in cui i servizi cloud non siano più utilizzati da Vectorlab,
dovranno essere rispettati i termini contrattuali stabiliti in fase di
definizione dei requisiti. A seconda della natura e dell’entità del
servizio, ciò potrebbe comportare la definizione di un vero e proprio
progetto al fine di:

  - estrarre i dati aziendali e, eventualmente, migrarli verso un
    servizio alternativo,

  - eliminare i dati dal CSP, in conformità con la politica *“PO15 –
    Classificazione delle Informazioni”*.