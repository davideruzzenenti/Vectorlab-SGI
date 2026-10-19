# PO25 - Sviluppo Sicuro

**Politica Sviluppo Sicuro**

Revisioni

|          |            |                 |             |               |
|----------|------------|-----------------|-------------|---------------|
| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | CTO         | CEO           |
|          |            |                 |             |               |
|          |            |                 |             |               |
|          |            |                 |             |               |

> Indice

# 

#  

# 1. Introduzione

# 1.1. Scopo

La Politica di Sviluppo Sicuro è un documento che fornisce la direzione e il supporto necessari per raggiungere e mantenere la Sicurezza delle Informazioni secondo i requisiti di Business, il cogente e i regolamenti vigenti nel processo di sviluppo software e di sistemi, attraverso la definizione di funzionalità di sicurezza.

Quando un'applicazione è sviluppata indipendentemente dalla sicurezza, può diventare una minaccia per l’ambiente in cui è sviluppata esponendo a rischi sia l’organizzazione che sviluppa che l’utilizzatore finale.

Per rendere quindi sicura l’architettura delle applicazioni è necessario comprendere i requisiti della Politica di Sicurezza in modo che possano essere presi in considerazione insieme ai requisiti funzionali.

Le regole di progettazione e sviluppo di applicazioni sicure sono un attributo importante e necessario di un ambiente informatico sicuro. Applicazioni che proteggono dati da accessi non autorizzati o modifiche che assicurano la sua disponibilità sono vantaggi importanti per le organizzazioni con risorse fisiche e con informazioni che richiedono un tale ambiente.

Applicazioni non sicure contribuiscono ad aumentare interconnessioni di sistemi che forniscono porte aperte a possibili compromissioni di informazioni sensibili e critiche e di sistemi.

Pertanto, al fine di produrre applicazioni robuste e sicure, gli sviluppatori devono conoscere e aderire ad alcuni fondamentali principi di sicurezza in tutte le fasi del Ciclo di Vita del Software, in un’ottica cosiddetta “Secure by Design”.

Obiettivo di questo documento è quindi definire un processo per guidare gli sviluppatori nella definizione e implementazione di applicazioni sicure prendendo in considerazione:

> ● la sicurezza dell’ambiente di sviluppo;
>
> ● una guida sulla sicurezza nel ciclo di vita e nella metodologia di sviluppo del software;
>
> ● requisiti di sicurezza nella fase di design (progettazione);
>
> ● security checkpoints nelle fasi di progetto;
>
> ● repository sicuri;
>
> ● sicurezza nel controllo di versione;
>
> ● capacità degli sviluppatori di evitare, trovare e sistemare eventuali vulnerabilità.

# 1.2. Campo di applicazione

La presente Politica è rivolta al personale di Vectorlab delle aree Digital/SW Development e IT, nonché ai Fornitori esterni che collaborano allo sviluppo.

Maggiore dettaglio sulle attività svolte dalle singole aree è presente nelle procedure “*DIG - PR35.1 - Digital*”, “*IT - PR38.1 - IT*“.

# 1.3. Riferimenti e Allegati

ALPO25.A - Linee guida per lo sviluppo software

MDPR08.1.A - Informazioni Documentate

MDPO25.A - Vectorlab - OWASP ASVS Checklist

MDPO25.B - Definizione dei Requisiti

MDPO25.C - Documentazione Tecnica

MDPO25.G - Piano di Test

PO21 - Gestione dei Backup e Restore

PO26 - Gestione dei Fornitori

PO27 - Gestione Eventi e Incidenti

REG01 - Regolamento di utilizzo degli strumenti aziendali.

# 1.4. Definizioni, Acronimi, Abbreviazioni

CEO - Chief Executive Officer

CISO - Chief Information Security Officer

CTO – Chief Technical Officer

DPIA - Data Protection Impact Assessment

GDPR – General Data Protection Regulation

IT – Information Technology

LTS – Long Time Support

PT – Penetration Test

PM - Project Manager

SGI - Sistema di Gestione Integrato

SO – Sistema Operativo

UI – User Interface

VA – Vulnerability Assessment.

# 1.5. Responsabilità

CTO ha la responsabilità di redigere e mantenere aggiornata la presente politica.

RSGI ha la responsabilità di comunicare la presente politica.

Il personale, a qualsiasi livello, e i collaboratori esterni devono attenersi alle procedure definite dall’Organizzazione per assicurarsi che la presente Politica sia correttamente applicata.

I responsabili dell’attuazione della presente politica sono:

- CTO

- CISO

- Responsabile Area Digital

- Staff Digital.

# 1.6. Violazione della Politica

Qualsiasi azione non conforme alla politica aziendale di Vectorlab sarà considerata una violazione della sicurezza e come tale potrà tradursi nella sospensione dell'accesso alle aree e alle risorse informatiche, rete e documenti. L'uso improprio degli strumenti aziendali costituisce una grave violazione del dovere di correttezza e può comportare l'adozione di provvedimenti disciplinari in conformità alla normativa vigente.

I casi gravi saranno segnalati all'autorità competente e potranno essere oggetto di provvedimenti disciplinari o legali.

# 1.7. Riesame

Il riesame della presente politica viene effettuato periodicamente dalla Direzione al fine di valutare l’efficienza e l’efficacia delle misure messe in atto per garantire la Sicurezza delle Informazioni tramite l'adozione di principi di sicurezza all'interno del Ciclo di Vita del Software. Il riesame viene inoltre effettuato in tutte le situazioni per le quali viene richiesta una modifica relativa al business aziendale che può avere impatto anche sulla Sicurezza delle Informazioni.

# 2. Development Environment Security

L’ambiente di sviluppo è costituito da un insieme di componenti hardware e software, utilizzati dai diversi gruppi di sviluppo che ne definiscono le caratteristiche in base alla tipologia / campo di applicazione del prodotto software da sviluppare.

Il gruppo di lavoro (Team di sviluppo) è gestito da una figura responsabile (PM) che ha, tra le proprie mansioni, la responsabilità della gestione dei diversi componenti che costituiscono l’ambiente di sviluppo, definendone la loro costituzione iniziale, l’evoluzione, l’accessibilità, operando per ognuno di questi aspetti in stretta collaborazione con la funzione IT. Ogni variazione nella configurazione deve essere autorizzata dal Responsabile Area Digital o CTO.

L’ambiente di sviluppo di una applicazione utilizza come elementi principali i seguenti componenti:

- Postazioni degli sviluppatori

- Strumenti di sviluppo

- Server di versionamento

- Server di sviluppo – Unit testing

- Ambiente di Quality

- Ambiente di VA/PT

- Server di compilazioni delle build

- Gestione degli incidenti.

# 2.1. Configurazione postazioni degli sviluppatori

<span class="mark">Il PC aziendale in uso da personale Digital è installato di default con SO Linux Ubuntu nella versione LTS corrente e o</span>pportunamente configurato. L’installazione deve essere mantenuta aggiornata tramite i repository ufficiali. Non è consentito aggiornare la versione di SO installata salvo la disponibilità di una nuova versione LTS e previa autorizzazione in modo da evitare rischi per il corretto svolgimento delle attività di sviluppo. Tale aggiornamento dovrà avvenire pertanto in un periodo temporale concordato.

Eccezione a quanto sopra in caso le attività richieste allo sviluppatore richiedano l’utilizzo di una postazione specifica (es. computer Mac per sviluppo di applicazioni iOS).

L’accesso alle postazioni di lavoro è protetto con <span class="mark">password e, indipendentemente dal SO installato, lo storage è criptato; per quanto riguarda le installazioni miste (Linux/Windows) che prevedono *dual boot*, vengono criptate le partizioni contenenti dati sensibili. Per queste</span> macchine l’accesso a Internet è limitato/governato dalle best practice aziendali per la navigazione Internet (vedi “*REG01 - Regolamento di ut<span class="mark">ilizzo degli strumenti aziendali</span>*<span class="mark">”).</span>

<span class="mark">La procedura di prima configurazione della postazione prevede anche l’installazione dei principali strumenti software adottati dall’area e relativa configurazione.</span>

# 2.2. Strumenti di sviluppo

l tool di sviluppo sono nella disponibilità degli sviluppatori in due forme distinte, a seconda delle caratteristiche tecniche dei tool stessi:

- pacchetti installabili mediante i repository ufficiali della distribuzione Linux;

- pacchetti .deb da installare sulle singole macchine degli sviluppatori.

Il download di nuovi componenti (librerie, tools, documentazione, ecc.) deve avvenire attraverso una connessione HTTPS. Una volta acquisiti, i nuovi componenti prima di essere utilizzati devono essere verificati tramite un successivo test di integrazione con gli strumenti già in essere.

# 2.3. Server di versionamento

La storicizzazione e l'archiviazione dei file che formano i sorgenti di ogni applicazione avviene attraverso appositi tool di controllo delle versioni, differenziati a seconda del gruppo di utilizzo/applicazione da sviluppare.

<span class="mark">L’area IT, coordinandosi con i responsabili dei gruppi di lavoro, mantiene un inventario dei repository ufficiali per i diversi progetti. È responsabilità della funzione IT garantire il backup (vedasi “*PO21 - Gestione dei Backup e Restore*”).</span>

Ogni gruppo di lavoro deve archiviare i sorgenti sul repository aziendale di riferimento per il proprio progetto.

Viene usato lo strumento aziendale di versionamento (vedasi “*MDPR08.1.A - Informazioni Documentate/Tools*”), opportunamente configurato per consentire ai soli utenti censiti e autorizzati l’accesso ai sorgenti di competenza.

I sorgenti delle applicazioni sono ivi catalogate mediante la strutturazione opportuna di progetti e repository dedicati e suddivisi per Cliente.

La notifica all’area IT della necessità di attivare / disattivare accessi logici ai repository per i membri del gruppo di lavoro è a carico dei referenti dei gruppi, con particolare attenzione posta agli accessi dati a fornitori e collaboratori esterni.

# 2.4. Server di Sviluppo – Unit testing

Durante la fase di sviluppo, le attività di test in-progress (derivanti dal consolidamento dei codici sorgenti sviluppati e testati dai singoli programmatori) avvengono su una o più macchine dedicate (che possono coincidere con quelle di sviluppo) dove è presente un ambiente (file di configurazione, database, ecc.) il più possibile significativo per la verifica di quanto implementato.

L’accesso a tali macchine deve essere limitato agli sviluppatori e tester, ed eventualmente, ma solo a livello di accesso alla UI degli applicativi, ad altri utenti.

Le evidenze relative ai piani di test eseguiti per ogni progetto, sono raccolte nel documento “*MDPO25.G - Piano di Test*”.

# 2.5. Ambiente di Quality

Con lo scopo di consentire ai gruppi di tester (Team di test) di effettuare un test funzionale degli elementi rilasciati in-progress a seguito della fase di sviluppo, una o più macchine server dedicate sono destinate ad ospitare questi ambienti di lavoro.

È alimentato dai Team di sviluppo e successivamente configurato in collaborazione con i Team di test per rappresentare (a livello di file di configurazione, database, ecc.) nel modo più significativo possibile il campo di applicazione target.

Le evidenze relative ai test eseguiti per ogni progetto, sono raccolte nel documento “*MDPO25.G - Piano di Test*”.

# 2.6. Ambiente di VA/PT

Con lo scopo di consentire opportune verifiche di sicurezza e consentire test di VA/PT degli elementi rilasciati in-progress o finali, una o più macchine server dedicate sono destinate ad ospitare questi ambienti di lavoro. Può coincidere con ambiente di Quality.

Ambiente alimentato dai Team di sviluppo e successivamente configurati in collaborazione con i Team di test per rappresentare (a livello di file di configurazione, database, ecc.) nel modo più significativo possibile il campo di applicazione target.

# 2.7. Server di compilazione delle build

La compilazione per rilascio delle varie applicazioni avviene accedendo al repository del tool di versionamento utilizzato, così da poter selezionare <span class="mark">le versioni corrette ed aggiornare i sorgenti.</span>

<span class="mark">Per ogni progetto, la procedura di build (manuale o automatica) è documentata nella documentazione di progetto (vedasi “*MDPO25.C - Documentazione Tecnica*”).</span>

# 2.8. Gestione degli incidenti

Ogni evento che determina una possibile “incidente di sicurezza” per questi componenti (es. perdita di un portatile di uno sviluppatore, mancata riservatezza delle credenziali di accesso di uno sviluppatore, penetrazione di un virus su un PC di una risorsa di sviluppo, fail di un backup di un server di sviluppo ecc.) non appena nella visibilità dell’area IT, prevede il coinvolgimento del Responsabile Area Digital o CTO in modo che possa concorrere nel definire congiuntamente le azioni correttive immediate, nonché valutare comportamenti azioni atte a prevenire il ripetersi di analoghe situazione di rischio.

È responsabilità di ogni membro del Team di sviluppo di segnalare tempestivamente al proprio responsabile e alla funzione IT qualsiasi anomalia alla propria postazione di lavoro o agli ambienti di sviluppo condiviso, tramite mail.

Maggiore dettaglio sul flusso della gestione degli incidenti da seguire è descritto nella politica “*PO27 - Gestione Eventi e Incidenti*”.

# 3. Ciclo di Sviluppo Sicuro

Il raggiungimento di un efficace livello di sicurezza richiede attenzione a tutte le fasi del processo di progettazione e sviluppo del software.

A titolo esplicativo, la seguente matrice riporta un indice quantitativo di effort in termini di costi necessario nella risoluzione delle problematiche di sicurezza applicativa:

|                     |                     |                                                 |                              |                                  |                              |                               |
|---------------------|---------------------|-------------------------------------------------|------------------------------|----------------------------------|------------------------------|-------------------------------|
|                     |                     | **PROBLEMATICHE DI SICUREZZA (VULNERABILITA')** |                              |                                  |                              |                               |
|                     |                     | Scoperte in fase di progettazione e design      | Scoperte in fase di sviluppo | Scoperte in fase di integrazione | Scoperte in fase di collaudo | Scoperte in fase di esercizio |
| **DOVUTE A ERRORI** | **Architetturali**  | 1x                                              | 5x                           | 10x                              | 20x                          | 30x                           |
|                     | **Di codifica**     | \-                                              | 1x                           | 10x                              | 20x                          | 30x                           |
|                     | **Di integrazione** | \-                                              | \-                           | 1x                               | 10x                          | 15x                           |

*Tabella 1 - Vulnerabilità dovute a errori*

Un ciclo di sviluppo sicuro considera e implementa opportune attività di sicurezza nel corso di tutte le fasi del processo.

Al fine di ottemperare al concetto di *Privacy by design* e *Privacy by default*, il ciclo di vita dei nostri software deve tenere conto dei <span class="mark">risultati di un’eventuale valutazione della DPIA, per cui viene utilizzato lo strumento indicato in “*MDPR08.1.A - Informazioni Documentate/Tools*”.</span>

Gli step del processo che sono coinvolti dall’applicazione di misure di sicurezza, a cui concorrono per la definizione le aree Digital e Governance, sono:

- **Requisiti**: in questa fase vengono effettuate le analisi dei requisiti di sicurezza, dei rischi, delle probabilità di impatto delle minacce. Si considerano inoltre le best practice di carattere generale nella definizione dei requisiti di sicurezza (vedi capp. 3.1.2 e 3.1.3);

- **Progettazione**: in questa fase si esamina il sistema in divenire con l’ausilio di tecniche di analisi e modellazione delle minacce, producendo requisiti di sicurezza di dettaglio che si aggiungono a quelli prodotti dalla precedente fase;

- **Implementazione**: in questa fase si realizza il sistema attraverso la programmazione di codice sicuro, test di sicurezza basati sull'analisi delle minacce e analisi statica del codice sorgente. Quest’ultima può produrre nuovi requisiti di sicurezza che indirizzano la revisione del codice;

- **Verifica**: in questa fase si analizzano gli aspetti di sicurezza del sistema in esecuzione in un ambiente controllato impiegando tecniche e strumenti di analisi dinamica;

- **Validazione**: è la fase immediatamente prima del rilascio, viene effettuata una *final security review* per verifica del rispetto dei requisiti dati;

- **Miglioramento continuo**: il processo viene periodicamente sottoposto a revisione da parte dei soggetti coinvolti, adeguandolo alle rinnovate necessità tecniche e/o di business, ai mutati scenari sistemistici/architetturali, e tarandolo sulle skill acquisite dalle figure coinvolte.

Le principali azioni di sicurezza da attuare sono:

- Definizione degli elementi di sicurezza applicativa, finalizzata alla valutazione dei requisiti relativamente a:

<!-- -->

- Integrità

- Autenticità

- Riservatezza.

<!-- -->

- Definizione dei requisiti di privacy, attraverso la raccolta strutturata delle seguenti categorie di informazioni:

<!-- -->

- Dati personali

- Servizi di terze parti

- Policy.

<!-- -->

- Risk Assessment, finalizzato alla valutazione del rischio.

Ogni fase è caratterizzata dall'adozione di opportuni strumenti software a supporto delle operazioni.

# 3.1 Requisiti

### 3.1.1. Valutazione Rischio e Minacce

L'analisi viene eseguita in maniera qualitativa suddividendo l’attività di sviluppo in task su cui dovrà essere decretato il livello di rischio in una scala che prevede i valori: *assente*, *basso*, *medio*, *alto*. In assenza di strumenti a supporto, l’analisi sarà eseguita dal progettista di maggior esperienza. L’attività è effettuata mediante il documento “*MDPO25.B - Definizione dei Requisiti*”.

Nel caso di rischio *assente*, si procede come da flusso standard, senza più alcun rilievo inerente alla sicurezza.

Nel caso di rischio *basso*, ci si limita ad inserire una segnalazione di attenzione all’interno della specifica, ma per il resto si procede come da flusso standard, senza più alcun rilievo inerente alla sicurezza.

Nel caso di rischio *medio* o *alto*, oltre a inserire una segnalazione di attenzione all’interno della specifica, si procede con la stesura dei requisiti di sicurezza tecnici e di business, come descritto ai capp. 3.1.2 e 3.1.3.

### 3.1.2. Definizione dei Requisiti di sicurezza a livello di business

Qualora possibile, i requisiti di sicurezza a livello di business saranno dettagliati in una sezione dedicata della specifica funzionale, in modo da accrescere l’evidenza a tutti gli stakeholder del processo. Nei casi in cui tali requisiti siano fortemente compenetrati con l'argomento stesso della segnalazione, ne definiscono il vero e proprio contenuto e saranno piuttosto annegati nelle varie parti della specifica.

### 3.1.3. Definizione dei Requisiti di sicurezza tecnici

<span class="mark">Nel documento “*MDPO25.B - Definizione dei Requisiti*” vengono descritti i requisiti di sicurezza a livello di business; devono altresì dettagliarsi le soluzioni tecniche necessarie da implementare per garantire i requisiti tecnici di sicurezza identificati.</span>

Il dettaglio e la completezza della descrizione dei requisiti devono essere tali da consentire all’incaricato alla progettazione di scegliere una soluzione di dettaglio idonea ai requisiti, e al personale destinato al test di verificare i casi d’uso necessari alla validazione di tutti i requisiti.

<span class="mark">I</span> punti di attenzione di sicurezza, descritti in dettaglio nella specifica funzionale, sono elencati in “*MDPO25.B - Definizione dei Requisiti*” e “*MDPO25.A - Vectorlab – OWASP ASVS Checklist*” assieme alla soluzione implementativa identificata. Ciò rende evidente, sia allo sviluppatore incaricato dell’implementazione che all’assegnatario del test, che la specifica funzionale deve contenere indicazioni dettagliate relative a ciascuno dei topic indicati.

Poiché vi sono requisiti tecnici di sicurezza che sono nativamente gestiti dal framework, di essi non è necessario dettagliare su ogni task le modalità di implementazione. In tali casi, tuttavia, la specifica funzionale deve indicare esplicitamente che il requisito non è oggetto di una specifica implementazione poiché già soddisfatto da meccanismi nativi del framework, limitandosi a citarli. In tal caso, anche le note di sicurezza nella checklist OWASP citeranno, per ogni requisito, l’eventuale riferimento alla feature di framework che lo implementa.

Qualora l’implementazione di un requisito di sicurezza, sia esso di business o tecnico, non venga assolto dalla sola implementazione tecnica di sviluppo, ma richieda una specifica configurazione dell'ambiente di installazione, la specifica funzionale deve indicare le configurazioni necessarie e le implicazioni nel caso queste non fossero implementate. In tal caso, le note di sicurezza della checklist OWASP devono indicare che esiste un rischio legato alla mancata implementazione delle configurazioni indicate in specifica.

# 3.2. Progettazione

Le azioni di sicurezza attuabili in questa fase possono essere così sintetizzate:

- analisi e modellazione delle minacce, attraverso l’identificazione dei componenti applicativi coinvolti, delle interfacce e degli agenti che potrebbero minacciare il sistema;

- analisi della superficie d’attacco e della finestra di opportunità, allo scopo di individuare le parti del sistema che possono essere esposte ad attacchi e pertanto lo rendono vulnerabile;

- piano di mitigazione, attraverso l’identificazione delle contromisure da adottare in questa fase al fine di mitigare le potenziali minacce individuate (utilizzando anche tool automatici e semiautomatici);

- Secure Design Refactoring, revisione progettuale che attua le contromisure individuate; produzione di un High Level Design conforme ai principi del Secure by Design.

<span class="mark">Questa fa</span>se produce le specifiche funzionali e applicative, che tengono in considerazione i requisiti, tramite “*MDPO25.B - Definizione dei Requisiti*”.

La progettazione del software è ispirata, entro i vincoli tecnologici e di progetto, ai principi di sicurezza by design OWASP, di cui si tiene conto tramite “*MDPO25.A - Vectorlab – OWASP ASVS Checklist*”.

Il flusso di attività relativo alla privacy in ambito progettazione in questa fase può essere schematizzato come:

- **Input**: requisiti di privacy di base e test; Standard, cogente, best practice e procedure applicabili sulla privacy, requisiti funzionali, Profili di rischio per la privacy;

- **Attività**: nel caso ne sia stata riscontrata la necessità, svolgere una Data Protection Impact Assessment parametrata sugli obiettivi di protezione individuati;

- **Output**: requisiti di protezione per la privacy specifici per il software.

### 3.2.1. Privacy by design e by default

Il concetto di *Privacy by Design* consiste nel considerare l’interessato al centro del sistema di protezione dei dati personali, progettando un'applicazione che segue i requisiti di sicurezza sin da subito garantendo i diritti e le libertà dell’interessato.

La progettazione di qualsiasi software che coinvolga il trattamento dei dati personali deve essere preceduta da un'identificazione dei requisiti di protezione per la privacy, in quanto dal trattamento o dall’elaborazione dei dati personali potrebbero derivare dei rischi e delle minacce ai diritti e alla libertà dell’interessato. I rischi per la privacy negli applicativi software che comportano il trattamento dei dati personali, dovrebbero essere trattati prima della loro implementazione, ossia sin dalla fase di progettazione (Engineering Privacy by Design). Dovranno quindi essere analizzati i rischi collegati alle applicazioni software.

In linea con i requisiti di attuazione previsti dal GDPR, qualora un trattamento dei dati personali possa presentare un rischio elevato per i diritti e le libertà delle persone fisiche, i titolari di quest’ultimo dovranno effettuare una valutazione dell’impatto del trattamento sulla protezione dei dati personali o Data Protection Impact Assessment (DPIA); quest’obbligo è applicabile anche al ciclo di vita del software.

Per quanto riguarda il concetto di *Privacy by Default*, si può definire come: qualunque applicazione deve garantire che ogni accesso a un dato sensibile sia sempre mediato dall’applicazione di una policy di sicurezza.

Le policy di sicurezza devono sempre integrare:

- autorizzazioni legate ai ruoli degli utenti;

- autorizzazioni legate ai consensi espressi dall’interessato;

- tracciamento delle operazioni di accesso ai dati.

# 3.3. Implementazione

Le azioni di sicurezza attuabili in questa fase possono essere così sintetizzate:

- **Regole di scrittura**: scrivere codice secondo le guideline aziendali sulla strutturazione e scrittura formale del codice, presenti nell’allegato tecnico “*ALPO25.A - Linee guida per lo sviluppo software*”;

- **Regole implementative**: produrre software secondo le regole di base aziendale definite per la gestione di macro-tematiche di interesse, sempre in riferimento all’allegato tecnico “*ALPO25.A - Linee guida per lo sviluppo software*”;

- **Code review**: il codice deve essere sottoposto periodicamente dal Responsabile Area Digital a controlli di aderenza alle guideline sopra riportate. In caso alcune parti non soddisfino i requisiti di cui sopra la porzione di codice deve essere sottoposta a revisione;

- **Data Validation**: verificare la presenza di vulnerabilità che possono riguardare eventuali dati corrotti in ingresso e che possono portare a un comportamento anomalo dell’applicazione;

- **Control Flow**: verificare i rischi collegati all’assenza di specifiche sequenze di operazioni che, se non eseguite nel corretto ordine, possono portare a violazioni sulla memoria o sull’uso scorretto di determinati componenti;

- **Controllo Configurazioni**: verificare i parametri intrinseci di configurazione dell’applicazione.

Il flusso di attività relativo alla privacy in ambito implementazione può essere schematizzato come:

- **Input**: requisiti architetturali e funzionali specifici per la privacy;

- **Attività**: implementare i requisiti di protezione della privacy definiti nella fase di progettazione;

- **Output**: componenti del software implementati; Mitigazione dei rischi accettabili per la privacy residua.

L'implementazione del software è ispirata, entro i vincoli tecnologici e di progetto, ai principi di Secure Coding OWASP integrati con le best practice e guideline specifiche per le singole tecnologie di sviluppo in uso.

# 3.4. Verifica della sicurezza delle applicazioni

Le azioni di sicurezza attuabili in questa fase possono essere così sintetizzate:

- **Penetration Test**: attraverso l’esecuzione di scansioni ed analisi della superficie di attacco;

- **Test di autenticazione multilivello**: attraverso la verifica delle modalità di gestione dell'accesso degli utenti;

- **Business Logic test**: attraverso l’esecuzione di test manuali sulle applicazioni in fase di esecuzione;

- **Analisi dei risultati**: attraverso l’individuazione e la rimozione dei falsi positivi;

- **Remediation Plan**: attraverso la definizione del piano di rientro e la produzione di reportistica di sintesi e di dettaglio;

- **Proof of Concept**: per le vulnerabilità riscontrate, comprensiva di azioni per la riduzione della superficie d’attacco.

Il flusso di attività relativo a privacy in ambito verifica e validazione può essere schematizzato come:

- **Input**: componenti del software implementati; Requisiti di privacy specifici del sistema e test; Politiche e procedure di privacy applicabili;

- **Attività**: sviluppare / perfezionare dei test sulla privacy; Eseguire delle verifiche sulla privacy; Verificare il comportamento operativo rispetto alle politiche e alle procedure sulla privacy applicabili;

- **Output**: risultati dei test di privacy; Documentazione delle incoerenze sulla privacy documentate; Descrizione del piano di trattamento della privacy.

L’esame delle applicazioni in esecuzione in ambiente di test può avvenire tramite VA, portando alla produzione delle seguenti tipologie di documenti:

- **Vulnerability Assessment**: report di dettaglio delle vulnerabilità riscontrate nella fase di analisi dinamica dell’applicazione tramite gli strumenti a supporto;

- **Remediation Plan**: report che analizza i falsi positivi ed indirizza la risoluzione delle problematiche riscontrate nell’analisi stessa.

<span class="mark">Per lo svolgimento di VA e PT Vectorlab può appoggiarsi a fornitori esterni.</span>

# 3.5. Supporto per la manutenzione di applicazioni sicure

L’obiettivo di questa fase è mantenere un prodotto sicuro, a partire dagli ultimi trend sugli attacchi/minacce. Il team deve quindi analizzare le nuove minacce e individuare le contromisure necessarie rilasciando nuovi aggiornamenti/patch laddove necessario attraverso un processo di *Continuous Security*.

# 4. Sviluppo in Outsourcing

I fornitori esterni che collaborano allo sviluppo ottemperano alla presente Policy nella stessa misura delle risorse interne, e vengono consegnate loro la Policy e tutti i documenti a cui essa fa riferimento.

Ogni fornitore, prima di essere abilitato ad accedere alle risorse aziendali, oltre ad un accordo di riservatezza, sottoscrive una dichiarazione con cui conferma la presa visione delle procedure in essa elencate e ne garantisce l’applicazione.

Viene fornito un estratto della documentazione al fornitore atta a garantire la piena conformità ai requisiti di sicurezza che vengono adottati dall’Azienda, che può includere il presente documento o un suo estratto, “*MDPO25.B - Definizione dei Requisiti*”, “*MDPO25.A - Vectorlab OWASP ASVS Checklist*” e “*MDPO25.C - Documentazione Tecnica*”.

Inoltre, nella contrattualizzazione dell’accordo possono essere indirizzati anche i seguenti punti:

- requisiti per lo sviluppo sicuro in progettazione, codifica e test;

- fornitura di evidenze per la conformità del prodotto software sviluppato ai requisiti di sviluppo sicuro;

- fornitura di evidenze dell’applicazione di test sufficienti a garantire l'assenza di contenuti dannosi sia intenzionali che non intenzionali al momento della consegna;

- accordi di deposito a garanzia (“source escrow”), per evitare l’indisponibilità del codice sorgente;

- possibilità di effettuare audit tecnici di seconda parte;

- documentazione efficace del prodotto sviluppato;

- accordi di licenza, proprietà del codice e diritti di proprietà intellettuale relativi al progetto software sviluppato.

La gestione del fornitore e requisiti di sicurezza sono descritti nella politica “*PO26 - Gestione dei Fornitori*”.
