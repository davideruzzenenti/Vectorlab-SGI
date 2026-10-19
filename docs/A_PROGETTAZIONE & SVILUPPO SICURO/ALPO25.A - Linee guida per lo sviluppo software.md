# ALPO25.A - Linee guida per lo sviluppo software

**Linee guida per lo sviluppo software**

### Revisioni

|          |            |                 |                      |               |
|----------|------------|-----------------|----------------------|---------------|
| **Rev.** | **Data**   | **Descrizione** | **Redatto**          | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | Responsabile di Area | CTO           |
|          |            |                 |                      |               |
|          |            |                 |                      |               |
|          |            |                 |                      |               |

# Indice 

# 

#  

# 1. Introduzione 

Il presente documento definisce le linee guida per la scrittura del codice applicativo all’interno dell’area Digital. L’adozione di standard condivisi è essenziale per garantire una gestione efficiente dello sviluppo software, assicurando uniformità e qualità del codice, indipendentemente dagli autori.

L’adozione di regole coerenti facilita il lavoro del team, migliorandone produttività ed efficacia, oltre a semplificare la manutenzione e l’evoluzione del software. Inoltre, un codice strutturato e ben organizzato consente una più agevole integrazione di nuovi membri nel team, rendendo immediatamente comprensibili l’architettura e i blocchi logici del progetto.

Queste linee guida mirano non solo a garantire uniformità stilistica, ma anche a promuovere la scrittura di codice chiaro, scalabile e facilmente manutenibile nel tempo.

# 2. Principi fondamentali

La scrittura di codice pulito e manutenibile è essenziale per garantire efficienza, scalabilità e collaborazione all'interno di un team di sviluppo. I seguenti principi, ispirati al “Clean Code” di Robert C. Martin, rappresentano le linee guida fondamentali per la scrittura del codice, al netto delle regole più specifiche trattate nei capitoli successivi.

# 2.1. Leggibilità e chiarezza

- Il codice deve essere **comprensibile a prima vista**, senza la necessità di commenti eccessivi.

- **Indentazione e formattazione** corrette devono essere applicate sin dalla prima scrittura del codice, anche nei prototipi e nel codice temporaneo.

- Evitare nomi generici e abbreviazioni criptiche: usare **nomi descrittivi e coerenti** per variabili, funzioni e classi.

- Preferire nomi semplici e di lunghezza contenuta (si suggerisce un massimo di 12 caratteri).

- Tutto il codice (nomi di variabili, classi, funzioni, commenti, ecc.) deve essere scritto in **lingua inglese**.

# 2.2. Semplicità e modularità (Keep It Simple - KISS)

- Ogni funzione o metodo deve avere **una sola responsabilità** (principio SRP - **Single Responsibility Principle**).

- Non scrivere funzioni/metodi **troppo lunghi**: preferire la suddivisione in più funzioni più piccole e riutilizzabili.

- Evitare strutture logiche **troppo complesse**: un codice più semplice è più facile da mantenere ed estendere.

# 2.3. Evitare la duplicazione (Don’t Repeat Yourself - DRY)

- Se un blocco di codice viene ripetuto in più punti, deve essere estratto in una funzione o metodo riutilizzabile.

<!-- -->

- Usare **costanti e variabili globali** invece di ripetere valori hardcoded.

- Dichiarare sempre come **costanti** le variabili il cui valore non è destinato a cambiare nel corso del loro ciclo di vita.

# 2.4. Commenti e documentazione essenziali

- Il codice **dovrebbe essere autoesplicativo**, ma quando necessario è opportuno **aggiungere commenti chiari e pertinenti**.

- Evitare commenti inutili o ridondanti.

- Devono chiarire la **logica di business** e non semplicemente descrivere il codice.

- Fornire spiegazioni chiare su metodi e flussi logici, documentando le scelte progettuali per facilitarne la comprensione e manutenzione.

- Documentare **le API e i moduli** utilizzando strumenti adeguati.

# 2.5. Struttura e organizzazione del codice

- Separare il codice in **moduli e file distinti** per migliorarne la manutenibilità.

- Strutturare il codice in modo logico, separando le diverse funzionalità per contesto.

- Organizzare le classi in **file separati** (una classe per file, se possibile).

- Limitare la dimensione dei file sorgente; **si consiglia di non superare un** **massimo di 400 righe per file**.

- Evitare metodi eccessivamente lunghi; preferire la suddivisione in funzioni più piccole e leggibili. **Si consiglia di non superare le 75 righe per metodo**.

- Evitare linee di codice troppo lunghe; **si consiglia di non eccedere i 180 caratteri per riga**.

<!-- -->

- Rispettare le convenzioni di denominazione specifiche del linguaggio.

- Attenersi alle regole indicate in questo documento. In caso di dubbi, consultare il proprio referente.

# 3. Impostazione stilistica 

Lo stile di codice utilizzato prevede un'impostazione di partenza sulla base dello stile Stroustrup. Si tratta dell’adattamento di Bjarne Stroustrup dello stile K&R per il C++. In questa versione le parentesi dei flussi di controllo sono indipendenti, ad esempio per l’esempio precedente avremo che la parentesi di chiusura dell’if sarà inserita in una propria linea e non accorpata con l’else successivo come nell’esempio seguente:

if (a \< 0) {

method1("Negativo");

method2(x);

}

else {

method1("Non-negativo");

method3(x);

}

A partire da questo stile seguono una serie di regole specifiche da adottare a livello di tutti gli applicativi prodotti dall'area Digital:

- i nomi dei file sono in stile dash case mentre il codice viene scritto in stile camel case;

- i nomi delle classi hanno sempre il primo carattere maiuscolo:

class MyClass {}

- dichiarazione di funzioni:

  - il nome della funzione ha sempre il primo carattere minuscolo;

  - non devono esserci spazi tra nome del metodo e le parentesi contenenti gli argomenti;

  - gli argomenti sono separati e spaziati tra loro;

  - deve sempre esserci uno spazio tra la fine degli argomenti e la graffa di apertura;

myClassFunction(arg1, arg2) <span class="mark"></span>{

}

function myGenericFunction(arg1, arg2) <span class="mark"></span>{

}

myArrowFunction(arg1, arg2) <span class="mark"></span>=\> <span class="mark"></span>{

}

- i nomi delle costanti applicative sono uppercase secondo la notazione:

const MY_CONST_VARIABLE = 'value';

- l'indentazione è basata su spazi e non su tab;

- l'indentazione per progetti Javascript / Typescript di 2 spazi, mentre per progetti Java è consentita un'indentazione a 4 spazi;

- nei costrutti racchiusi tra parentesi graffe inserire sempre una riga vuota tra riga di espressione o definizione di funzione e la prima istruzione in essa contenuta:

if (a \< 0) {

method1("Negativo");

method2(x);

}

myMethod(arg) {

method1("Negativo");

}

- in caso di costrutti all'interno dei quali è presente una sola istruzione non è richiesto l’uso di parentesi graffe e non si applica di conseguenza la regola precedente:

if (a \< 0)

method1("Negativo");

- inserire uno spazio tra espressione condizionale o iterativa e l'apertura della parentesi tonda successiva:

if <span class="mark"></span>(a \< 0)

for <span class="mark"></span>(let i = 0; i \<= 10; i++)

- inserire sempre le spaziature in caso di assegnazioni e operazioni, anche nel caso in cui siano parte di espressioni condizionali o iterative o argomento di funzione:

method1(var1 <span class="mark"></span>+ <span class="mark"></span>var2);

for (let i <span class="mark"></span>= <span class="mark"></span>0; <span class="mark"></span>i <span class="mark"></span>\<= <span class="mark"></span>(10 <span class="mark"></span>+ <span class="mark"></span>var2); <span class="mark"></span>i++) <span class="mark"></span>{}

let myVar <span class="mark"></span>= <span class="mark"></span>(var1 <span class="mark"></span>+ <span class="mark"></span>var2) <span class="mark"></span>/ <span class="mark"></span>x;

- per sviluppi Javascript / Typescript racchiudere sempre le stringe mediante l'uso di apici (') e non virgolette ("). Laddove si voglia creare una stringa lunga e con l'utilizzo di variabili preferire la notazione:

\`il mio testo \${variabile}\`

al posto di:

'il mio testo ' + variabile

- all’interno dei metodi utilizzare i commenti per singola linea // evitando commenti per righe multiple /\* \*/;

- ogni metodo deve essere preceduto da un commento nel seguente formato, salvo notazioni specifiche (eg. typescript che non richiede di esplicitare i tipi degli argomenti nel commento):

/\*\*

\* Method description

\*

\* @param {\*} arg1

\* @param {\*} arg2

\*/

method1(arg1, arg2) {

}

- per sviluppi Javascript / Typescript prediligere l’utilizzo di *arrow function*:

myArr.forEach((elem) =\> {

line1;

line2;

});

Ove il contenuto della funzione sia composto da una sola riga prediligere la notazione compatta:

myArr.forEach((elem) =\> line1);

- allineare sempre le assegnazioni delle variabili, non in modo assoluto ma per sottoblocchi di contesto. Separare blocchi e linee di codice diversi da assegnazione da una linea vuota:

let myVar1 <span class="mark">=</span> 'a';

let mySuperVar2 <span class="mark">=</span> 'b';

let myObject <span class="mark">=</span> {

attr1 <span class="mark">:</span> 123,

myAttr2<span class="mark">:</span> {

subattr1<span class="mark">:</span> { a <span class="mark">:</span> 2, bb<span class="mark">:</span> 34, c <span class="mark">:</span> 5 },

sattr2 <span class="mark">:</span> { aa<span class="mark">:</span> 33, b <span class="mark">:</span> 4, dfd<span class="mark">:</span> 38 }

}

attr3: 'abc'

};  
  
line1;

line2;

let myVar2 <span class="mark">=</span> 'a';

let mySuVar3 <span class="mark">=</span> 'b';

- in caso di strutture dati delimitate da graffe, spaziare sempre ogni attributo e inserire sempre uno spazio tra parentesi graffa e attributo. Non inserire spazi tra nome attributo e “:” se non per motivi di allineamento come rappresentato nell’esempio precedente:

{ <span class="mark"></span>a: <span class="mark"></span>2, <span class="mark"></span>b: <span class="mark"></span>34, <span class="mark"></span>c: <span class="mark"></span>5 <span class="mark"></span>}

- per sviluppi Javascript i metodi privati delle classi iniziano col carattere “\_”:

MyClass {

constructor() { }

/\*\*

\* Private method description

\*

\* @param {\*} arg

\*/

<span class="mark">\_p</span>rivateMethod1(arg) {

...

}

/\*\*

\* Public method description

\*

\* @param {\*} arg

\*/

publicMethod1(arg) {

...

}

}

- non lasciare linee vuote al termine di metodi funzioni o classi:

MyClass {

constructor() { }

/\*\*

\* Private method description

\*

\* @param {\*} arg

\*/

\_privateMethod1(arg) {

line1;

line2;

arr.forEach(elem =\> {

sl1;

<span class="mark">sl2;</span>

<span class="mark">});</span>

<span class="mark">line3;</span>

<span class="mark">}</span>

/\*\*

\* Public method description

\*

\* @param {\*} arg

\*/

publicMethod1(arg) {

...

<span class="mark">}</span>

<span class="mark">}</span>

- in caso di variabili booleane o metodi aventi valore di ritorno booleano non usare il pattern “isQualcosa” ma usare “qualcosa”

~~isEnabled = true;~~ NO

enabled = true; SI

~~isSomethingReady() { }~~ NO

somethingReady() { } SI

# 4. Linguaggi e framework

# 4.1. Angular

Per lo sviluppo front-end basato su **Angular**, si fa esplicito riferimento alle linee guida ufficiali **"Angular Coding Style Guide"**, disponibili al seguente link: [<u>Angular Coding Style Guide</u>](https://angular.io/guide/styleguide).

Per comodità, tali linee guida sono riportate anche nel documento interno **"Angular - Angular Coding Style Guide.pdf"**.

Le regole indicate in tali documenti devono essere considerate **aggiuntive** e non **sostitutive** delle linee guida generali descritte nel presente documento. Pertanto, nello sviluppo di applicazioni Angular, è necessario applicare entrambe le serie di regole in modo complementare, garantendo coerenza e qualità del codice.

# 4.2. Java

Per lo sviluppo back-end basato su **Java**, si devono seguire le **Java Code Conventions** ufficiali, disponibili al seguente link: [<u>Java Code Conventions</u>](https://www.oracle.com/java/technologies/javase/codeconventions-contents.html).

Le seguenti linee guida specifiche devono essere sempre rispettate:

- **Struttura del codice**: mantenere una chiara separazione tra **modelli, servizi e controller**, seguendo l'architettura **MVC (Model-View-Controller)**.

- **Nomenclatura**:

  - I nomi delle classi devono essere in **PascalCase** (es. UserService).

  - I metodi e le variabili devono seguire lo **stile camelCase** (es. calculateTotalAmount).

  - Le costanti devono essere scritte in **MAIUSCOLO_SNAKE_CASE** (es. DEFAULT_TIMEOUT).

- **Uso delle interfacce**: preferire l'uso di interfacce per definire contratti e separare implementazioni concrete.

- **Gestione delle eccezioni:**

  - Evitare **catch generici** (es. catch (Exception e)), specificando sempre il tipo di eccezione.

  - Fornire messaggi chiari per facilitare la diagnostica dei problemi.

- **Commenti e Javadoc**:

  - Ogni classe e metodo pubblico deve essere documentato con **Javadoc**.

  - Utilizzare **TODO** per segnalare miglioramenti futuri, evitando commenti inutili.

# 4.3. Python

Per lo sviluppo in **Python**, è obbligatorio seguire lo standard **PEP 8**, disponibile al seguente link: [<u>PEP 8 – Style Guide for Python Code</u>](https://peps.python.org/pep-0008/).

Le principali regole di stile includono:

- **Indentazione**: utilizzare **4 spazi** per livello di indentazione (evitare tabulazioni).

- **Nomenclatura**:

  - I nomi delle variabili e delle funzioni devono essere in **snake_case** (es. calculate_total_amount).

  - I nomi delle classi devono essere in **PascalCase** (es. DataProcessor).

- **Lunghezza del codice:**

  - Ogni riga di codice non deve superare gli **80 caratteri** (preferibilmente 79).

  <!-- -->

  - Un file Python non dovrebbe superare le **400 righe** per mantenere la leggibilità.

- **Gestione delle eccezioni:**

  - Utilizzare blocchi try/except specifici, evitando except Exception as e generici.

  - Fornire messaggi chiari per debugging e logging.

- **Uso di docstring**: ogni modulo, classe e funzione deve avere una **docstring** che ne descriva lo scopo, secondo il formato **PEP 257**.

- **Tipizzazione opzionale**: utilizzare **type hints** dove possibile per migliorare la leggibilità e la manutenibilità del codice (es. def add(a: int, b: int) -\> int:).

# 7. Documentazione

Una documentazione chiara e ben strutturata è essenziale per garantire la manutenibilità e la scalabilità del codice.

# 7.1. Linee guida

- **Struttura della documentazione:**

  - La documentazione deve coprire tutti gli aspetti fondamentali del progetto, inclusi **obiettivi, architettura, API, flussi operativi e dipendenze**.

  - Ogni modulo deve avere una descrizione chiara della sua funzione e del suo utilizzo.

- **Formato della documentazione:**

  - Prediligere l'uso di **Markdown** (.md), **reStructuredText** o documenti in **HTML/PDF**.

  - Per i progetti di grandi dimensioni, si consiglia l’uso di strumenti come **Sphinx**, **MkDocs**, **Doxygen** o **Swagger** per API documentation.

- **Aggiornamento costante:**

  - La documentazione deve essere **sempre allineata** con lo stato attuale del codice.

  - Qualsiasi modifica sostanziale al codice deve essere accompagnata da un aggiornamento della documentazione corrispondente.

# 7.2. Commenti nel codice

- **Commenti esplicativi:**

  - Devono essere **essenziali e utili**, evitando di spiegare l’ovvio.

  - Devono chiarire la **logica di business** e non semplicemente descrivere il codice.

- **Struttura dei commenti:**

  - Usare **Javadoc** per Java, **docstring** per Python, e commenti inline (// per JavaScript/TypeScript, \# per Python).

  - Evitare commenti obsoleti o ridondanti.

# 8. Sicurezza nel codice

La sicurezza del codice è un aspetto fondamentale dello sviluppo software. Un codice non sicuro può esporre l’applicazione a vulnerabilità critiche come SQL Injection, Cross-Site Scripting (XSS), attacchi Cross-Site Request Forgery (CSRF) e molte altre minacce informatiche.

Di seguito vengono illustrati i principi fondamentali per scrivere codice sicuro, riducendo il rischio di exploit e migliorando la protezione dei dati.

# 8.1. Sanitizzazione e validazione degli input

Uno degli attacchi più comuni sfrutta l’inserimento di dati malevoli nei campi input. Per prevenire tali vulnerabilità, è essenziale:

- **Validare sempre gli input** prima di utilizzarli (verificare tipo, lunghezza, formato, contenuto).

- **Sanitizzare i dati in ingresso** per rimuovere caratteri o codici potenzialmente dannosi.

- **Evitare concatenazioni di stringhe per query SQL**: utilizzare sempre **Prepared Statements** o **ORM**.

# 8.2. Prevenzione di attacchi XSS (Cross-Site Scripting)

L’**XSS** avviene quando un’applicazione permette l’inserimento di codice JavaScript dannoso, che viene poi eseguito dagli utenti. Per evitarlo:

- **Evitare l’inserimento di input utente non filtrato nelle pagine HTML**.

- **Utilizzare escaping per output dinamico** (es. htmlspecialchars() in PHP, escape() in Django, dompurify per JavaScript).

- **Implementare Content Security Policy (CSP)** per limitare l’esecuzione di script dannosi.

# 8.3. Protezione contro attacchi CSRF (Cross-Site Request Forgery)

Il **CSRF** sfrutta l’autenticazione di un utente per eseguire azioni non autorizzate su un sito web. Per mitigarlo:

- **Utilizzare token CSRF per ogni richiesta POST**.

- **Verificare sempre l’origine delle richieste HTTP** (header Referer o Origin).

- **Evitare sessioni troppo lunghe** e implementare timeout di autenticazione.

# 8.4. Gestione sicura delle credenziali e dei dati sensibili

Le credenziali e le informazioni sensibili devono essere **protette e mai hardcodate nel codice sorgente**. Best practices:

- **Utilizzare variabili d’ambiente** per gestire credenziali e chiavi API.

- **Mai salvare password in chiaro**, ma solo versioni **hashed e salate**.

- **Limitare la visibilità dei file di configurazione** e proteggere i dati sensibili.

# 8.5. Principio del minimo privilegio

L’accesso ai dati e alle funzionalità deve essere concesso **solo nella misura strettamente necessaria**. Regole fondamentali:

- **Account con permessi minimi necessari** (evitare root o admin quando non richiesto).

- **Limitare accessi ai database** (uso di ruoli con privilegi minimi).

- **Disabilitare funzioni inutilizzate** per ridurre la superficie di attacco.

- **Loggare le attività sospette** e monitorare accessi non autorizzati.

# 8.6. Logging e monitoraggio delle attività sospette

Il **logging sicuro** è essenziale per identificare e mitigare attacchi. Best practices:

- **Registrare solo dati essenziali**, evitando di salvare informazioni sensibili nei log.

- **Usare strumenti di monitoraggio** per rilevare comportamenti sospetti.

- **Proteggere i log da accessi non autorizzati** e mantenerli per il tempo strettamente necessario.

# 8.7. Configurazioni sicure

Le configurazioni dell’applicazione devono seguire le best practices di sicurezza:

- **Disabilitare errori dettagliati in produzione** (evitare divulgazione di stack trace).

- **Utilizzare protocolli di comunicazione sicuri** (HTTPS invece di HTTP).

- **Limitare l’uso di cookie persistenti** e proteggere le sessioni (Secure, HttpOnly, SameSite).

- **Evitare dipendenze obsolete o vulnerabili**: mantenere le librerie aggiornate.

# 9. Testing e qualità del codice

Oltre alla scrittura del codice, il testing e la revisione della qualità sono elementi fondamentali per garantire un software robusto, efficiente e manutenibile. Un codice non testato o di bassa qualità può portare a bug critici, vulnerabilità di sicurezza e difficoltà nella manutenzione futura.

Questa sezione illustra le migliori pratiche per assicurare la qualità del codice attraverso **test automatizzati**, **revisioni del codice** e **analisi statica**.

# 9.1. Test Unitari (Unit Test)

I test unitari sono essenziali per verificare che ogni unità di codice (funzione, metodo, classe) si comporti correttamente in modo isolato. **Scrivere test unitari permette di rilevare errori precocemente** e semplificare il debugging.

**Best practice per i test unitari:**

- Scrivere test indipendenti tra loro.

- Utilizzare **mock e stub** per isolare il comportamento delle unità testate.

- Assicurarsi che i test siano **veloci ed eseguibili frequentemente**.

- Seguire il principio **AAA (Arrange, Act, Assert)** per strutturare i test.

# 9.2. Test di integrazione

I test di integrazione verificano che diversi moduli o componenti di un’applicazione funzionino correttamente quando combinati. Sono essenziali per individuare problemi di comunicazione tra servizi, database e API.

**Best practice per i test di integrazione:**

- Simulare scenari reali di utilizzo.

- Utilizzare **database di test o mock di API** per evitare modifiche ai dati reali.

- Automatizzare i test di integrazione nei flussi CI/CD.

# 9.3. Code Review e Pair Programming

La revisione del codice è un processo critico per migliorare la qualità e la manutenibilità del software. **Il codice deve essere sempre sottoposto a una revisione prima di essere integrato nel repository principale**.

**Best practice per la code review:**

- Usare strumenti di **version control (Git)** per tracciare le modifiche.

- Seguire una checklist di revisione, valutando leggibilità, sicurezza, performance e aderenza agli standard.

- **Fornire feedback costruttivi** e spiegazioni chiare sulle richieste di modifica.

**Pair Programming** è un’altra tecnica utile in casi di necessità particolari: due sviluppatori scrivono codice insieme, riducendo bug e migliorando la qualità in tempo reale.

# 9.4. Analisi statica del codice

L'analisi statica del codice aiuta a individuare problemi **senza eseguire il programma**, rilevando bug, problemi di sicurezza e violazioni di stile.

**Best practice per l’analisi statica:**

- Integrare l’analisi nei processi CI/CD per una verifica continua.

- Automatizzare l’esecuzione di tool di linting e sicurezza.

- Correggere le segnalazioni critiche prima di ogni rilascio.

# 10. Gestione del versionamento del codice (Git Guideline e Bitbucket)

L’utilizzo corretto di Git è fondamentale per garantire una gestione efficiente del codice sorgente, favorire la collaborazione tra sviluppatori e ridurre i conflitti. In questa sezione vengono illustrate le migliori pratiche per organizzare il repository, definire una strategia di branching chiara e scrivere commit significativi.

# 10.1. Struttura del repository

Un repository Git ben organizzato migliora la leggibilità e la manutenibilità del codice. **Best practices:**

- Mantenere una struttura di cartelle chiara e coerente.

- Separare codice, documentazione e test.

- Ignorare file non necessari con un file **.gitignore** ben configurato.

# 10.2. Strategie di branching

L’adozione di una strategia di branching chiara riduce i conflitti e migliora la collaborazione. Le strategie più utilizzate sono:

- **Git Flow** – Ideale per progetti con rilasci strutturati. Prevede branch separati per sviluppo, feature, bugfix e release.

- **GitHub Flow** – Strategia più semplice, ideale per Continuous Deployment. Tutte le modifiche partono da main e vengono integrate tramite pull request.

- **Trunk-based Development** – Strategia per team agili, con commit frequenti direttamente sulla main branch e feature flags per il rilascio controllato.

# 10.3. Commit messages

Un buon messaggio di commit aiuta a capire **cosa è cambiato e perché**. E’ buona norma scrivere messaggi chiari e significativi:

- Usare **messaggi descrittivi** e al presente es. "Fix bug nel calcolo di…"

- Seguire la convenzione **"Tipo: Descrizione"**

- Separare titolo e descrizione con una riga vuota.

**Esempio di commit message ben strutturato:**

feat: aggiunto supporto per la localizzazione in italiano

\- Aggiunto file di traduzione it.json

\- Modificata configurazione di i18n per supportare più lingue

**Tipologie di commit (convenzionali):**

- **feat:** Nuova funzionalità

- **fix:** Correzione di bug

- **chore:** Modifiche di manutenzione (es. aggiornamenti dipendenze)

- **docs:** Aggiornamento della documentazione

- **test:** Aggiunta/modifica test

- **refactor:** Rifattorizzazione senza cambiare il comportamento

# 10.4. Gestione dei merge e delle Pull Request

Le pull request (PR) sono essenziali per il controllo qualità e il code review prima di integrare il codice nel branch principale. **Best practices per merge e PR:**

- Creare PR con una **descrizione chiara delle modifiche**.

- Assegnare un revisore prima di effettuare il merge.

- Evitare merge diretti su main senza revisione.

- Risolvere i conflitti prima di unire il codice.

# 11. Strumenti adottati

# 11.1. IDE

### 11.1.2. Visual Studio Code

L’IDE di riferimento per lo sviluppo software è **Visual Studio Code** (VS Code). Questo ambiente di sviluppo è adottato per la sua leggerezza, flessibilità ed estensibilità grazie all’ampia disponibilità di estensioni.

**Estensioni consigliate per VS Code**

Per migliorare l’efficienza dello sviluppo, vengono adottati e consigliati i seguenti plugin ufficiali:

- **Supporto AI & Code Assistance**

  - GitHub Copilot e GitHub Copilot Chat (GitHub)

  - IntelliCode e IntelliCode API Usage Examples (Microsoft)

- **Sviluppo Backend**

  - Debugger for Java (Microsoft)

  - Extension Pack for Java (Microsoft)

  - Gradle for Java (Microsoft)

  - Maven for Java (Microsoft)

  - Lombok Annotations Support for Java (Microsoft)

  - Java Server Pages (JSP) Language Support (JohnMilton)

  - Language Support for Java™ (Red Hat)

  - Project Manager for Java (Microsoft)

- **Spring Boot & Spring Framework:**

  - Spring Boot Dashboard (Microsoft)

  - Spring Boot Extension Pack (VMware)

  - Spring Boot Tools (VMware)

  - Spring Initializr Java Support (Microsoft)

- **Sviluppo Frontend & UI/UX**

  - Ionic (Ionic)

  - Live Sass Compiler (Glenn Marks)

  - Live Server (Ritwick Dey)

  - Angular Language Service (Angular)

  - React Native Tools (Microsoft)

  - Stylelint (Stylelint)

- **API & Web Services**

  - Apollo GraphQL (Apollo GraphQL)

  - GraphQL for VSCode (Kumar Harsh)

  - OpenAPI (Swagger) Editor (42Crunch)

  - Postman (Postman)

- **Versioning & Collaboration**

  - Jira and Bitbucket (Atlassian)

  - Docker (Microsoft)

  - DotENV (mikestead)

  - SVN (Chris Johnston)

- **Testing & Debugging**

  - Community Server Connectors (Red Hat)

  - Runtime Server Protocol (Red Hat)

  - Test Runner for Java (Microsoft)

- **Analisi del Codice & Sicurezza**

  - SonarQube for IDE (SonarSource)

- **Gestione Configurazioni & Markup**

  - YAML (Red Hat)

  - XML (Red Hat)

- **Altri strumenti utili**

  - Random Name Generator (Thomas Rayner)

  - Red Hat Commons (Red Hat)

  - PlantUML (jebbs)
