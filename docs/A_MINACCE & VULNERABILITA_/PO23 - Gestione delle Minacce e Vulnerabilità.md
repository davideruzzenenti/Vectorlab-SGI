# PO23 - Gestione delle Minacce e Vulnerabilità

**Politica di Gestione delle Minacce e Vulnerabilità**

<div style="border-left:4px solid #2A5C8A;background:#EAF1F7;padding:.75rem 1rem;margin:1rem 0">
<strong>DOCUMENTO IN BOZZA — generato il 16/07/2026</strong> per colmare una lacuna rilevata durante la revisione della documentazione (citato nella SOA ma non ancora creato). Contenuto basato su pratiche reali già note da altri documenti del SGI; le parti evidenziate in rosso sono da confermare prima dell'approvazione formale.
</div>

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.1      | 16/07/2026 | Prima bozza — documento mancante generato per colmare una lacuna rilevata nella SOA | IA          | Da approvare  |
|          |            |                 |             |               |

## 1 Introduzione

### 1.1 Scopo / Campo di applicazione

La presente politica definisce i principi e le linee guida con cui
VECTORLAB gestisce le minacce alla sicurezza delle informazioni e le
vulnerabilità tecniche che possono interessare i propri asset,
infrastrutture e software.

Poiché lo sviluppo software (web, mobile, desktop, embedded) costituisce
il core business di VECTORLAB, la gestione delle vulnerabilità non è un
tema periferico ma un elemento centrale della postura di sicurezza
dell'Azienda: riguarda tanto l'infrastruttura tecnologica su cui i
servizi sono erogati quanto il codice sorgente, le librerie e le
dipendenze utilizzate nei progetti realizzati per i Clienti.

Il documento ha lo scopo di:

  - definire l'approccio adottato da VECTORLAB per identificare,
    valutare e trattare le vulnerabilità tecniche presenti sui sistemi
    e sul software di propria gestione;

  - definire le modalità con cui l'Azienda raccoglie e valuta
    informazioni relative a minacce alla sicurezza delle informazioni
    (threat monitoring), al fine di anticipare possibili impatti sugli
    asset aziendali;

  - stabilire ruoli e responsabilità per l'attuazione dei processi di
    gestione delle minacce e delle vulnerabilità;

  - garantire la coerenza di questi processi con la gestione del
    cambiamento, la gestione degli asset e la gestione degli incidenti
    già definite nel SGI.

La presente politica si applica:

  - all'infrastruttura cloud (AWS) e al server Aruba gestito in
    modalità Infrastructure-as-Code;

  - a tutti i software, applicativi e servizi sviluppati o mantenuti da
    VECTORLAB per conto proprio o dei Clienti, incluse le relative
    librerie e dipendenze di terze parti;

  - alle postazioni di lavoro, agli account e ai servizi SaaS aziendali
    (es. Google Workspace, GitHub, strumenti di ticketing);

  - a tutto il personale, interno ed esterno (collaboratori,
    sviluppatori in P.IVA), che opera su tali sistemi.

### 1.2 Riferimenti e Allegati

> MDPR11.1.C - Piano di Audit Tecnici

> PO25 - Sviluppo Sicuro

> PO32 - Gestione delle Configurazioni

> PR14.1 - Gestione Asset

> PR22.1 - Gestione delle Patch

> PR23.1 - Gestione delle Vulnerabilità Tecniche

> PR23.2 - Monitoraggio delle Minacce

> PR27.1 - Gestione Incidenti e Data Breach

> PR33.1 - Processo Analisi del Rischio e Trattamento

> PR19.1 - Gestione del Cambiamento

> ALPR23.2.A - Report Monitoraggio Minacce

> MDPR23.1.A - Piano Gestione delle Vulnerabilità \[progetto\]

> MDPR23.2.A - Monitoraggio Minacce - Template

> SOA - Statement of Applicability - Dichiarazione di Applicabilità.

### 1.3 Definizioni, Acronimi, Abbreviazioni

> CISO - Chief Information Security Officer. In VECTORLAB tale ruolo è
> ricoperto dall'Amministratore Unico, coerentemente con
> l'organizzazione snella dell'Azienda

> CTO - Chief Technology Officer

> CVE - Common Vulnerabilities and Exposures, identificativo standard
> assegnato a una vulnerabilità nota

> <span style="color:#B3392A">\[DA CONFERMARE: VECTORLAB non utilizza
> attualmente un punteggio CVSS formalizzato; la severità viene stimata
> qualitativamente da IT sulla base delle informazioni disponibili
> (fonte, criticità dell'asset coinvolto, sfruttabilità nota)\]</span>

> Minaccia - Causa potenziale di un incidente indesiderato, che può
> provocare un danno a un sistema o all'Organizzazione

> RID - Riservatezza, Integrità, Disponibilità

> RSGI - Responsabile del Sistema di Gestione Integrato

> SGI - Sistema di Gestione Integrato

> VA - Vulnerability Assessment

> Vulnerabilità - Debolezza di un asset o di un controllo che può
> essere sfruttata da una o più minacce.

## 2 Politica di Gestione delle Minacce e Vulnerabilità

### 2.1 Principi generali

VECTORLAB adotta un approccio proattivo alla gestione delle minacce e
delle vulnerabilità, coerente con quanto già dichiarato nella SOA per i
controlli 5.7 (Monitoraggio delle minacce) e 8.8 (Gestione delle
vulnerabilità tecniche): l'Azienda mantiene aggiornati i propri sistemi
operativi e software, monitora le vulnerabilità note attraverso fonti
pubbliche e gli aggiornamenti dei fornitori, e applica le patch
tempestivamente, compatibilmente con il contesto operativo e la
continuità dei servizi erogati.

I principi che guidano questo approccio sono:

  - **prevenzione**: ridurre la superficie di attacco attraverso
    l'aggiornamento regolare di sistemi, software e dipendenze
    (cfr. "*PR22.1 - Gestione delle Patch*") e attraverso pratiche di
    sviluppo sicuro (cfr. "*PO25 - Sviluppo Sicuro*");

  - **identificazione tempestiva**: individuare le vulnerabilità
    tecniche non appena rese note, attraverso attività di Vulnerability
    Assessment periodico e monitoraggio continuo delle fonti
    informative rilevanti;

  - **valutazione basata sul rischio**: prioritizzare il trattamento
    delle vulnerabilità in base alla criticità dell'asset coinvolto
    (secondo la classificazione dell'Asset Inventory, cfr. "*PR14.1 -
    Gestione Asset*") e alla gravità della vulnerabilità stessa;

  - **trattamento tempestivo e tracciato**: gestire la remediation
    attraverso i canali già previsti dal SGI (change management,
    ticketing) in modo da garantire tracciabilità e verificabilità
    delle azioni intraprese;

  - **proporzionalità**: le misure adottate sono commisurate alle
    dimensioni e alle risorse di VECTORLAB, che non dispone di un CED
    fisico proprio (infrastruttura cloud-first) né di un team di
    sicurezza dedicato a tempo pieno.

### 2.2 Ambiti di applicazione

La gestione delle minacce e delle vulnerabilità in VECTORLAB si
articola su due ambiti complementari, descritti nel dettaglio dalle
rispettive procedure:

  - **Gestione delle Vulnerabilità Tecniche** (cfr. "*PR23.1 - Gestione
    delle Vulnerabilità Tecniche*"): riguarda l'identificazione, la
    valutazione e il trattamento delle vulnerabilità note che
    interessano l'infrastruttura (AWS, server Aruba), i sistemi
    operativi, le postazioni di lavoro e, in ragione del core business
    di sviluppo software, il codice sorgente e le dipendenze/librerie
    di terze parti utilizzate nei progetti;

  - **Monitoraggio delle Minacce** (cfr. "*PR23.2 - Monitoraggio delle
    Minacce*"): riguarda la raccolta e l'analisi di informazioni
    relative a minacce alla sicurezza delle informazioni provenienti da
    fonti pubbliche, dai fornitori di servizi cloud/software e dalle
    community tecniche, al fine di anticipare possibili impatti sugli
    asset aziendali, in coerenza con quanto già dichiarato nella SOA per
    il controllo 5.7.

Entrambi gli ambiti sono strettamente collegati al processo di
"*PR19.1 - Gestione del Cambiamento*", in particolare per quanto
riguarda le change di tipo emergenza, che possono essere attivate a
seguito della rilevazione di una vulnerabilità grave o di una minaccia
imminente.

### 2.3 Ruoli e responsabilità

Il CISO ha la responsabilità di redigere, mantenere aggiornata e
comunicare la presente politica, con il supporto del CTO per gli
aspetti tecnici.

I responsabili dell'attuazione della presente politica sono:

  - la **Direzione** di VECTORLAB, che fornisce le risorse necessarie
    per garantire la corretta applicazione della politica;

  - il **CISO**, che indirizza le priorità di trattamento delle
    minacce e delle vulnerabilità più rilevanti e ne riferisce alla
    Direzione;

  - il **CTO** e il reparto **IT**, che eseguono operativamente le
    attività di identificazione, valutazione, monitoraggio e
    remediation delle vulnerabilità tecniche, sia a livello
    infrastrutturale sia a livello di codice/dipendenze dei progetti
    software;

  - tutto il **personale tecnico**, che ha la responsabilità di
    segnalare tempestivamente al CISO o al CTO qualsiasi vulnerabilità
    o indicatore di minaccia rilevato nell'ambito della propria
    attività, incluse le segnalazioni provenienti da fornitori,
    Clienti o community tecniche;

  - i **collaboratori esterni e fornitori** coinvolti nello sviluppo o
    nella gestione dei sistemi, tenuti al rispetto delle medesime
    regole in base agli accordi contrattuali sottoscritti.

### 2.4 Violazione della Politica

Qualsiasi azione non conforme alla presente politica, inclusa la
mancata segnalazione di una vulnerabilità nota o l'omessa applicazione
di aggiornamenti di sicurezza senza giustificato motivo, sarà
considerata una violazione della sicurezza e potrà comportare
l'adozione di provvedimenti disciplinari in conformità alla normativa
vigente, oltre alla sospensione dell'accesso alle risorse informatiche
interessate.

### 2.5 Riesame

La revisione della presente politica, e delle procedure ad essa
afferenti, è effettuata dal CISO almeno una volta all'anno e prima del
Riesame della Direzione, e in risposta a cambiamenti significativi
dell'ambiente organizzativo, del business, di riferimenti normativi o
dell'ambiente tecnologico aziendale (ad esempio l'adozione di nuovi
strumenti di sviluppo o l'evoluzione dell'infrastruttura cloud). Il
riesame è condotto per valutare l'efficacia del sistema e assicurare il
miglioramento continuo dei processi di gestione delle minacce e delle
vulnerabilità.
