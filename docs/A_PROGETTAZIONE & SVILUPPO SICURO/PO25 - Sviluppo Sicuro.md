# PO25 - Sviluppo Sicuro

**Politica di Sviluppo Sicuro del Software**

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

La presente politica descrive i principi e le regole adottate da
VECTORLAB per garantire che la progettazione, lo sviluppo, il test e il
rilascio del software siano condotti in modo sicuro, riducendo il
rischio che vulnerabilità di sicurezza vengano introdotte nei prodotti e
nei servizi realizzati dall'Azienda.

VECTORLAB sviluppa applicazioni web, desktop, mobile ed embedded,
sistemi 3D/computer graphics, simulatori, soluzioni di realtà
virtuale/aumentata (VR/AR), videogiochi, piattaforme cloud e soluzioni
basate su Intelligenza Artificiale/Large Language Model (LLM). Data la
varietà delle tecnologie e dei contesti di utilizzo, la presente
politica definisce i principi comuni di sicurezza che devono essere
applicati indipendentemente dalla tipologia di prodotto sviluppato,
lasciando ai documenti operativi collegati (allegati e moduli) il
compito di declinare tali principi in regole e strumenti concreti.

Il documento si applica a tutti i progetti di sviluppo software gestiti
da VECTORLAB, sia realizzati per uso interno che per conto di Clienti,
e a tutto il personale (dipendenti e collaboratori esterni) coinvolto
nelle attività di progettazione, sviluppo, test e rilascio del
software.

<span style="color:#B3392A">[DA CONFERMARE: lo sviluppo software è attualmente svolto interamente con personale interno/collaboratori diretti; non risultano ad oggi progetti di sviluppo affidati integralmente in outsourcing a terze parti. Qualora ciò cambiasse, la presente politica dovrà essere estesa con requisiti specifici di supervisione dello sviluppo esternalizzato]</span>.

### 1.2 Riferimenti e Allegati

> ALPO25.A - Regole scrittura codice

> MDPO25.A - OWASP ASVS Checklist

> MDPO25.B - Definizione dei Requisiti \[progetto\]

> MDPO25.C - Documentazione Tecnica \[progetto\]

> PO16 - Gestione degli Accessi

> PO17 - Crittografia

> PO32 – Gestione delle Configurazioni

> PR19.1 - Gestione del Cambiamento

> PR20.1 - Capacità e Monitoraggio Tecnico

> PR33.1 - Processo Analisi del Rischio e Trattamento

> MDPR11.1.C - Piano di Audit Tecnici

> SOA - Statement of Applicability - Dichiarazione di Applicabilità.

### 1.3 Definizioni, Acronimi, Abbreviazioni

> ASVS – Application Security Verification Standard (OWASP)

> CI/CD – Continuous Integration / Continuous Delivery

> CTO – Chief Technical Officer

> DAST – Dynamic Application Security Testing

> LLM – Large Language Model

> OWASP – Open Web Application Security Project

> RSGI – Responsabile del Sistema di Gestione Integrato

> SAST – Static Application Security Testing

> SDLC – Software Development Life Cycle (Ciclo di Vita di Sviluppo del Software)

> SGI – Sistema di Gestione Integrato

> VR/AR – Virtual Reality / Augmented Reality.

## 2 Principi Generali

VECTORLAB adotta un processo strutturato per lo sviluppo del software,
che include attività di progettazione, sviluppo, test e rilascio. Il
codice sorgente di tutti i progetti è gestito tramite sistemi di
versionamento (GitHub) e le modifiche vengono controllate prima della
messa in produzione, in accordo con quanto descritto in "*PR19.1 -
Gestione del Cambiamento*".

I principi fondamentali a cui si ispira la presente politica sono:

  - **Security by design** – i requisiti di sicurezza sono considerati
    fin dalla fase di analisi e progettazione di ciascun progetto, e
    non aggiunti a posteriori;

  - **Riduzione della superficie di attacco** – i sistemi vengono
    progettati minimizzando i componenti, i servizi e le interfacce
    esposte non strettamente necessari;

  - **Difesa in profondità** – i controlli di sicurezza sono applicati
    a più livelli (rete, applicazione, dati, accessi) in modo che il
    fallimento di un singolo controllo non comprometta l'intero
    sistema;

  - **Least privilege** – l'accesso a codice, ambienti e dati è
    concesso secondo il principio del privilegio minimo necessario, in
    coerenza con "*PO16 - Gestione degli Accessi*";

  - **Miglioramento continuo** – le pratiche di sviluppo sicuro sono
    riviste periodicamente alla luce dell'evoluzione delle minacce,
    degli standard di settore (es. OWASP) e delle tecnologie adottate
    dall'Azienda.

## 3 Ciclo di Vita di Sviluppo Sicuro (SDLC)

Il ciclo di vita di sviluppo del software adottato da VECTORLAB prevede
le seguenti fasi principali, applicate in modo proporzionato alla
dimensione e criticità di ciascun progetto:

1.  **Analisi e definizione dei requisiti** – vengono raccolti i
    requisiti funzionali e non funzionali del progetto, inclusi i
    requisiti di sicurezza applicabili (vedere "*MDPO25.B - Definizione
    dei Requisiti \[progetto\]*");

2.  **Progettazione (design)** – viene definita l'architettura della
    soluzione applicando i principi di architettura sicura descritti
    al capitolo 4;

3.  **Sviluppo** – il codice viene realizzato secondo le linee guida di
    codifica sicura definite in "*ALPO25.A - Regole scrittura
    codice*" e gestito tramite repository GitHub con controllo delle
    versioni;

4.  **Test** – vengono eseguiti test funzionali e verifiche di
    sicurezza di base, secondo quanto descritto al capitolo 6;

5.  **Rilascio (release)** – il software viene rilasciato in ambiente
    di produzione solo a seguito del superamento delle attività di
    test e dell'approvazione delle modifiche, secondo quanto descritto
    in "*PR19.1 - Gestione del Cambiamento*";

6.  **Manutenzione** – successivamente al rilascio, il software viene
    mantenuto e aggiornato, incluse le attività di gestione delle
    vulnerabilità individuate.

<span style="color:#B3392A">[DA CONFERMARE: le fasi del ciclo di vita non sono ad oggi supportate da un template/workflow formale unico e uniforme per tutti i progetti; la modalità di applicazione pratica (es. metodologia Agile/Scrum, cadenza degli sprint, strumenti di project management) può variare da progetto a progetto]</span>.

## 4 Requisiti di Sicurezza delle Applicazioni

Per ciascun progetto di sviluppo, i requisiti di sicurezza applicabili
vengono identificati, specificati e approvati in fase di analisi,
tenendo conto della tipologia di applicazione (web, mobile, desktop,
embedded, cloud, basata su AI/LLM, ecc.), dei dati trattati e del
contesto di utilizzo (interno o per conto di Clienti).

I requisiti di sicurezza individuati vengono documentati utilizzando il
modulo "*MDPO25.B - Definizione dei Requisiti \[progetto\]*" e, per i
progetti di maggiore complessità o esposizione, verificati anche
tramite la checklist "*MDPO25.A - OWASP ASVS Checklist*", basata
sull'OWASP Application Security Verification Standard.

## 5 Principi di Architettura e Ingegnerizzazione Sicura

Durante la progettazione dei sistemi e delle applicazioni vengono
adottati principi di architettura sicura, tra cui:

  - **isolamento dei componenti**, per limitare l'impatto di un'eventuale
    compromissione di un singolo modulo/servizio sul resto del sistema;

  - **gestione degli accessi**, applicando autenticazione, autorizzazione
    e segregazione dei ruoli in coerenza con "*PO16 - Gestione degli
    Accessi*";

  - **protezione dei dati**, sia in transito che a riposo, tramite
    l'uso di meccanismi crittografici in coerenza con "*PO17 -
    Crittografia*";

  - **riduzione delle superfici di attacco**, limitando servizi,
    porte, dipendenze e componenti esposti al minimo necessario per il
    funzionamento dell'applicazione.

Le soluzioni sono progettate considerando i rischi di sicurezza propri
del contesto operativo (applicazioni web e cloud esposte su Internet,
applicazioni mobile distribuite su store pubblici, sistemi embedded con
vincoli di aggiornamento, soluzioni basate su LLM con rischi specifici
di prompt injection e gestione dei dati in input/output) e applicando
misure adeguate a mitigarli.

<span style="color:#B3392A">[DA CONFERMARE: non risulta un documento di architettura di riferimento unico e trasversale a tutti i progetti; le scelte architetturali (es. pattern di isolamento, uso di container, API gateway) sono valutate progetto per progetto]</span>.

## 6 Codifica Sicura

Durante lo sviluppo del software vengono adottate pratiche di codifica
sicura, includendo la validazione degli input, la gestione corretta
degli accessi e la protezione dei dati, in coerenza con i principi
generali dell'OWASP (Open Web Application Security Project).

Le regole operative di codifica sicura, comprensive di indicazioni su
validazione input, gestione di segreti e credenziali nel codice e
gestione delle dipendenze di terze parti, sono riportate nell'allegato
"*ALPO25.A - Regole scrittura codice*".

## 7 Test di Sicurezza e Accettazione

Durante lo sviluppo delle applicazioni vengono eseguiti test funzionali
e verifiche di sicurezza di base, al fine di identificare e correggere
eventuali vulnerabilità prima del rilascio. Le attività di test sono
proporzionate al contesto operativo e ai rischi associati al singolo
progetto, e comprendono di norma:

  - test funzionali, per verificare la corrispondenza tra il software
    realizzato e i requisiti definiti;

  - verifiche di sicurezza di base sulle funzionalità critiche (es.
    autenticazione, gestione sessione, controllo accessi, validazione
    input), supportate, ove applicabile, dalla checklist "*MDPO25.A -
    OWASP ASVS Checklist*";

  - test manuali con strumenti quali Postman per la verifica delle API
    esposte dalle applicazioni.

Le evidenze delle attività di analisi, test e verifica svolte per
ciascun progetto vengono raccolte nel modulo "*MDPO25.C -
Documentazione Tecnica \[progetto\]*".

<span style="color:#B3392A">[DA CONFERMARE: non risultano ad oggi in uso strumenti automatizzati di SAST/DAST/scansione delle dipendenze integrati stabilmente nella pipeline CI/CD; le verifiche di sicurezza sono allo stato attuale prevalentemente manuali]</span>.

## 8 Separazione degli Ambienti

Gli ambienti di sviluppo, test e produzione sono logicamente separati.
L'accesso agli ambienti è controllato e limitato in base ai ruoli, in
coerenza con "*PO16 - Gestione degli Accessi*". Le modifiche vengono
testate in ambienti dedicati prima del rilascio in produzione e non è
consentito effettuare sviluppo direttamente in ambiente di produzione.

Data la natura cloud-first dell'infrastruttura di VECTORLAB (assenza di
un CED fisico), la separazione degli ambienti è realizzata tramite
piattaforme e servizi cloud, con configurazioni e credenziali di
accesso distinte per ciascun ambiente.

<span style="color:#B3392A">[DA CONFERMARE: le modalità tecniche esatte di separazione degli ambienti (es. progetti/istanze cloud distinti, branching model su GitHub, naming convention degli ambienti) possono variare da progetto a progetto e non sono ad oggi standardizzate in un unico documento]</span>.

## 9 Gestione dei Cambiamenti

Le modifiche al codice e ai sistemi in produzione sono gestite in modo
controllato: prima dell'introduzione in produzione, i cambiamenti
vengono valutati, testati e approvati, e sono tracciati e documentati
tramite il sistema di versionamento (storico delle revisioni e delle
modifiche su GitHub), con possibilità di ripristino in caso di
problemi. Il processo di gestione del cambiamento è descritto in
dettaglio in "*PR19.1 - Gestione del Cambiamento*".

## 10 Dati di Test

I dati utilizzati nelle attività di test e sviluppo non devono
contenere dati reali sensibili o dati personali di Clienti, salvo
laddove opportunamente mascherati, anonimizzati o pseudonimizzati.
L'accesso ai dati e ai report di test è riservato al personale
autorizzato.

## 11 Sviluppo Affidato all'Esterno

Lo sviluppo software di VECTORLAB non è ad oggi affidato a fornitori
esterni ma è gestito internamente. Qualora in futuro si ricorresse a
sviluppo esternalizzato, dovranno essere definiti requisiti specifici
di supervisione, monitoraggio e revisione delle attività affidate a
terze parti, in coerenza con "*PR26.1 - Gestione dei fornitori*".

## 12 Protezione dei Sistemi durante Audit e Test

Le attività di test, audit e verifica sui sistemi informativi sono
pianificate e controllate per evitare impatti negativi sull'operatività
dei sistemi in uso, in coerenza con "*MDPR11.1.C - Piano di Audit
Tecnici*". Gli accessi concessi per finalità di audit e test sono
limitati, monitorati e autorizzati.

## 13 Responsabilità

RSGI ha la responsabilità di redigere, mantenere aggiornata e comunicare
la presente politica.

Il personale coinvolto nelle attività di sviluppo, a qualsiasi livello,
e i collaboratori esterni devono attenersi alle regole definite dalla
presente politica e dai relativi allegati e moduli operativi.

<span style="color:#B3392A">[DA CONFERMARE: dato il contesto organizzativo snello di VECTORLAB (Amministratore Unico che ricopre anche il ruolo di CTO), la responsabilità di approvazione tecnica finale dei rilasci e di supervisione dell'applicazione della presente politica è verosimilmente in capo al CTO; da confermare formalmente l'assegnazione dei ruoli operativi (es. revisione del codice, gestione della checklist ASVS) tra le risorse coinvolte nello sviluppo]</span>.

## 14 Riesame

La revisione della presente politica è effettuata da RSGI almeno una
volta all'anno e prima del riesame della Direzione, e in risposta a
cambiamenti significativi delle tecnologie di sviluppo adottate, degli
standard di sicurezza di riferimento (es. evoluzione dell'OWASP ASVS) o
del contesto organizzativo e di business di VECTORLAB.
