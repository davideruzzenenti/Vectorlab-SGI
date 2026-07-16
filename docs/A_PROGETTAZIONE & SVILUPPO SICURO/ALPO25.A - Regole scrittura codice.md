# ALPO25.A - Regole scrittura codice

**Allegato — Linee Guida di Codifica Sicura (Secure Coding Guidelines)**

<div style="border-left:4px solid #2A5C8A;background:#EAF1F7;padding:.75rem 1rem;margin:1rem 0">
<strong>DOCUMENTO IN BOZZA — generato il 16/07/2026</strong> per colmare una lacuna rilevata durante la revisione della documentazione (citato nella SOA ma non ancora creato). Contenuto basato su pratiche reali già note da altri documenti del SGI; le parti evidenziate in rosso sono da confermare prima dell'approvazione formale.
</div>

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.1      | 16/07/2026 | Prima bozza — documento mancante generato per colmare una lacuna rilevata nella SOA | IA          | Da approvare  |
|          |            |                 |             |               |

## 1 Scopo

Il presente allegato a "*PO25 - Sviluppo Sicuro*" raccoglie le regole e
le linee guida di codifica sicura che il personale di VECTORLAB
(dipendenti e collaboratori) coinvolto nello sviluppo software deve
applicare, indipendentemente dal linguaggio di programmazione o dalla
piattaforma target (web, desktop, mobile, embedded, cloud, AI/LLM).

Le regole si basano sui principi generali di secure coding promossi
dall'OWASP (Open Web Application Security Project) e sono da
considerarsi come standard minimo applicabile a tutti i progetti,
fermo restando che ogni progetto può definire, tramite "*MDPO25.B -
Definizione dei Requisiti \[progetto\]*", requisiti aggiuntivi più
stringenti in base al contesto.

## 2 Validazione degli Input

  - Tutti i dati provenienti dall'esterno (input utente, parametri di
    richieste HTTP, file caricati, risposte di API di terze parti,
    messaggi scambiati tra componenti) devono essere considerati non
    fidati e validati prima dell'uso.

  - La validazione deve preferibilmente basarsi su liste di valori
    ammessi (allow-list) piuttosto che su liste di valori da escludere
    (deny-list).

  - Devono essere applicate tecniche di parametrizzazione delle query
    verso i database (es. query parametrizzate/prepared statement) per
    prevenire injection (SQL/NoSQL injection).

  - I dati in output verso l'utente (es. contenuti mostrati in pagine
    web) devono essere opportunamente codificati (output encoding) per
    prevenire attacchi di tipo Cross-Site Scripting (XSS).

  - I file caricati dagli utenti devono essere validati per tipo,
    dimensione e contenuto prima di essere elaborati o memorizzati.

## 3 Autenticazione e Gestione delle Sessioni

  - Le credenziali di autenticazione (password) non devono mai essere
    memorizzate in chiaro; devono essere utilizzate funzioni di hash
    robuste e dedicate alla protezione delle password.

  - I meccanismi di autenticazione devono prevedere protezioni contro
    tentativi ripetuti di accesso (es. blocco temporaneo dopo un numero
    di tentativi falliti), ove tecnicamente possibile.

  - I token e gli identificativi di sessione devono essere generati con
    adeguato livello di casualità, avere una durata di validità limitata
    e essere invalidati al logout o dopo un periodo di inattività.

  - Ove disponibile, deve essere valutato l'utilizzo dell'autenticazione
    a più fattori (MFA) per gli accessi con privilegi elevati.

## 4 Controllo degli Accessi

  - Ogni funzionalità e ogni risorsa esposta dall'applicazione deve
    verificare che l'utente richiedente sia autorizzato ad accedervi,
    applicando il controllo lato server (mai affidandosi al solo
    controllo lato client/interfaccia).

  - Deve essere applicato il principio del privilegio minimo (least
    privilege): ogni componente, utenza di servizio o integrazione deve
    disporre solo dei permessi strettamente necessari al proprio
    funzionamento, in coerenza con "*PO16 - Gestione degli Accessi*".

  - I riferimenti diretti a oggetti (es. ID di record, percorsi di
    file) esposti tramite API o URL devono essere protetti da controlli
    di autorizzazione per prevenire accessi non autorizzati a dati di
    altri utenti (Insecure Direct Object Reference).

## 5 Gestione di Segreti e Credenziali

  - Password, chiavi API, token di accesso, stringhe di connessione a
    database e altri segreti non devono mai essere inseriti in chiaro
    nel codice sorgente né commit-ati nei repository GitHub, nemmeno in
    repository privati.

  - I segreti devono essere gestiti tramite variabili d'ambiente,
    meccanismi di secret management dedicati o funzionalità sicure
    messe a disposizione dalla piattaforma di CI/CD (es. GitHub
    Actions secrets), evitando la loro esposizione nei log applicativi.

  - Qualora un segreto venga accidentalmente esposto in un repository
    (es. tramite commit errato), esso deve essere considerato compromesso,
    revocato/ruotato immediatamente e sostituito.

  - <span style="color:#B3392A">[DA CONFERMARE: non risulta ad oggi in uso un tool dedicato di secret-scanning automatico sui repository GitHub; l'adozione di funzionalità come GitHub secret scanning/push protection è da valutare e formalizzare]</span>.

## 6 Gestione delle Dipendenze di Terze Parti

  - Le librerie, i framework e i pacchetti di terze parti utilizzati nei
    progetti devono provenire da fonti ufficiali e affidabili (es.
    registri pubblici ufficiali dei rispettivi ecosistemi).

  - Le versioni delle dipendenze utilizzate devono essere tenute
    aggiornate, con particolare attenzione alle versioni che
    correggono vulnerabilità di sicurezza note.

  - Prima di introdurre una nuova dipendenza in un progetto, va
    valutata la sua reale necessità, la sua manutenzione nel tempo
    (community/vendor attivi) e l'eventuale presenza di vulnerabilità
    note.

  - <span style="color:#B3392A">[DA CONFERMARE: non risulta ad oggi uno strumento automatizzato di dependency scanning (es. Dependabot o equivalente) attivato stabilmente su tutti i repository GitHub aziendali; l'adozione è da valutare e formalizzare]</span>.

## 7 Gestione degli Errori e Logging

  - I messaggi di errore mostrati all'utente non devono rivelare
    dettagli tecnici sensibili (es. stack trace, query eseguite,
    struttura interna del database o del sistema).

  - Gli errori e le eccezioni devono essere opportunamente gestiti nel
    codice (try/catch o equivalente) per evitare comportamenti
    imprevisti o l'interruzione non controllata dei servizi.

  - I log applicativi non devono contenere dati sensibili in chiaro
    (password, token, dati personali non necessari), in coerenza con
    "*PO15 - Politica Classificazione Informazioni*".

  - Eventi rilevanti per la sicurezza (es. tentativi di accesso falliti,
    modifiche a permessi) dovrebbero essere tracciati per supportare le
    attività di monitoraggio descritte in "*PR20.1 - Capacità e
    Monitoraggio Tecnico*".

## 8 Crittografia

  - I dati classificati come riservati o contenenti dati personali
    devono essere protetti in transito tramite protocolli cifrati (es.
    HTTPS/TLS) e, ove applicabile, a riposo, in coerenza con "*PO17 -
    Crittografia*".

  - Non devono essere implementati algoritmi crittografici "custom":
    devono essere utilizzate esclusivamente librerie crittografiche
    standard, mantenute e riconosciute dalla comunità di riferimento.

## 9 Considerazioni Specifiche per Soluzioni basate su AI/LLM

  - Gli input forniti a modelli linguistici (LLM) integrati nelle
    soluzioni sviluppate devono essere trattati come dati non fidati,
    valutando i rischi di prompt injection e di divulgazione impropria
    di informazioni riservate tramite i prompt o le risposte generate.

  - I dati riservati o personali non devono essere inclusi nei prompt
    inviati a servizi/modelli di terze parti se non nel rispetto delle
    condizioni contrattuali e delle valutazioni sulla protezione dei
    dati previste per il fornitore del servizio (cfr. "*PR26.1 -
    Gestione dei fornitori*").

  - <span style="color:#B3392A">[DA CONFERMARE: non risultano ad oggi linee guida interne più dettagliate e specifiche sull'uso sicuro di servizi di Intelligenza Artificiale generativa/LLM nello sviluppo software; da valutare l'opportunità di un documento dedicato]</span>.

## 10 Revisione del Codice e Versionamento

  - Tutto il codice sorgente è gestito tramite repository GitHub, con
    storico delle modifiche tracciato tramite commit.

  - Le modifiche al codice destinato alla produzione dovrebbero essere
    sottoposte a revisione (code review, anche tra pari) prima
    dell'integrazione nel ramo principale, in coerenza con i principi di
    controllo delle modifiche descritti in "*PR19.1 - Gestione del
    Cambiamento*".

  - <span style="color:#B3392A">[DA CONFERMARE: non risulta ad oggi formalizzata una regola obbligatoria di revisione tramite pull request con approvazione di un secondo revisore su tutti i repository; la pratica può variare in base alla dimensione del team di progetto]</span>.

## 11 Riferimenti

> PO25 - Sviluppo Sicuro

> MDPO25.A - OWASP ASVS Checklist

> MDPO25.B - Definizione dei Requisiti \[progetto\]

> PO16 - Gestione degli Accessi

> PO17 - Crittografia

> PR19.1 - Gestione del Cambiamento

> PR20.1 - Capacità e Monitoraggio Tecnico.
