# MDPO25.A - OWASP ASVS Checklist

**Modulo — Checklist di Verifica basata su OWASP Application Security Verification Standard (ASVS)**

<div style="border-left:4px solid #2A5C8A;background:#EAF1F7;padding:.75rem 1rem;margin:1rem 0">
<strong>DOCUMENTO IN BOZZA — generato il 16/07/2026</strong> per colmare una lacuna rilevata durante la revisione della documentazione (citato nella SOA ma non ancora creato). Contenuto basato su pratiche reali già note da altri documenti del SGI; le parti evidenziate in rosso sono da confermare prima dell'approvazione formale.
</div>

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.1      | 16/07/2026 | Prima bozza — documento mancante generato per colmare una lacuna rilevata nella SOA | IA          | Da approvare  |
|          |            |                 |             |               |

## 1 Scopo

Il presente modulo, allegato a "*PO25 - Sviluppo Sicuro*", fornisce un
template di checklist per la verifica dei requisiti di sicurezza delle
applicazioni sviluppate da VECTORLAB, basato sulle categorie di
controllo dell'OWASP Application Security Verification Standard
(ASVS), standard pubblico di riferimento del settore per la
verifica della sicurezza applicativa.

La checklist deve essere compilata per ciascun progetto (o release
significativa di un progetto) per cui, in base a "*MDPO25.B -
Definizione dei Requisiti \[progetto\]*", sia stato definito un livello
di rischio tale da richiedere una verifica strutturata dei requisiti di
sicurezza applicativa. Non tutte le voci sono applicabili a tutti i
progetti: la colonna "Applicabile" consente di escludere motivatamente
le voci non pertinenti alla tipologia di applicazione in esame (es.
alcuni controlli lato web non sono pertinenti per applicazioni
desktop/embedded standalone).

## 2 Istruzioni per l'uso

  - Duplicare la presente checklist per ogni progetto/release da
    verificare, indicando nome progetto, versione e data di
    compilazione.

  - Per ogni voce, indicare se il requisito è **Applicabile** al
    progetto in esame.

  - Per le voci applicabili, indicare l'**Esito** della verifica
    (Conforme / Non conforme / Parzialmente conforme / Non verificato).

  - Riportare in **Note/Evidenze** eventuali riferimenti a test
    eseguiti, strumenti utilizzati o motivazioni di non applicabilità.

  - Le non conformità rilevate devono essere riportate anche in
    "*MDPO25.C - Documentazione Tecnica \[progetto\]*" e gestite fino
    a risoluzione o accettazione formale del rischio residuo.

## 3 Dati del Progetto

| **Campo**              | **Valore** |
| ----------------------- | ---------- |
| Nome progetto            |            |
| Versione/Release         |            |
| Tipologia applicazione (web/mobile/desktop/embedded/cloud/AI-LLM) |            |
| Data compilazione        |            |
| Compilatore              |            |
| Livello ASVS di riferimento (1/2/3) |            |

<span style="color:#B3392A">[DA CONFERMARE: VECTORLAB non ha ad oggi formalizzato quale livello ASVS (1, 2 o 3) debba essere adottato come standard minimo per le diverse tipologie di progetto; si suggerisce, in assenza di indicazioni contrattuali dei Clienti, l'adozione del Livello 1 come base minima]</span>.

## 4 Checklist di Verifica

### 4.1 Architettura, Progettazione e Modellazione delle Minacce

| **#** | **Requisito** | **Applicabile (Si/No)** | **Esito** | **Note/Evidenze** |
| ----- | ------------- | ------------------------ | --------- | ------------------ |
| 1.1   | I componenti dell'applicazione sono segregati tra loro in base alla criticità e alla superficie di attacco. |  |  |  |
| 1.2   | Sono identificati e documentati i requisiti di sicurezza specifici del progetto. |  |  |  |
| 1.3   | L'architettura prevede meccanismi di riduzione della superficie di attacco (servizi/porte/endpoint minimi necessari). |  |  |  |

### 4.2 Autenticazione

| **#** | **Requisito** | **Applicabile (Si/No)** | **Esito** | **Note/Evidenze** |
| ----- | ------------- | ------------------------ | --------- | ------------------ |
| 2.1   | Le password sono memorizzate tramite funzioni di hash dedicate e robuste (mai in chiaro o con hash reversibile). |  |  |  |
| 2.2   | Sono previste protezioni contro attacchi di forza bruta (rate limiting, blocco account). |  |  |  |
| 2.3   | È disponibile/valutata l'autenticazione a più fattori per utenze con privilegi elevati. |  |  |  |
| 2.4   | I meccanismi di recupero password sono sicuri (no invio password in chiaro, token con scadenza). |  |  |  |

### 4.3 Gestione della Sessione

| **#** | **Requisito** | **Applicabile (Si/No)** | **Esito** | **Note/Evidenze** |
| ----- | ------------- | ------------------------ | --------- | ------------------ |
| 3.1   | I token/identificativi di sessione sono generati con adeguata casualità. |  |  |  |
| 3.2   | Le sessioni hanno una durata di validità limitata e vengono invalidate al logout. |  |  |  |
| 3.3   | I cookie di sessione, ove utilizzati, sono configurati con attributi di sicurezza appropriati (Secure, HttpOnly, SameSite). |  |  |  |

### 4.4 Controllo degli Accessi

| **#** | **Requisito** | **Applicabile (Si/No)** | **Esito** | **Note/Evidenze** |
| ----- | ------------- | ------------------------ | --------- | ------------------ |
| 4.1   | Ogni richiesta a funzionalità/risorse protette è verificata lato server. |  |  |  |
| 4.2   | È applicato il principio del privilegio minimo per utenze e componenti di servizio. |  |  |  |
| 4.3   | I riferimenti diretti a oggetti (ID record, path file) sono protetti da controlli di autorizzazione. |  |  |  |

### 4.5 Validazione, Sanitizzazione e Codifica dell'Input/Output

| **#** | **Requisito** | **Applicabile (Si/No)** | **Esito** | **Note/Evidenze** |
| ----- | ------------- | ------------------------ | --------- | ------------------ |
| 5.1   | Gli input provenienti dall'esterno sono validati secondo un approccio allow-list. |  |  |  |
| 5.2   | Le interazioni con database utilizzano query parametrizzate/prepared statement. |  |  |  |
| 5.3   | I dati in output sono correttamente codificati per prevenire XSS. |  |  |  |
| 5.4   | I file caricati dagli utenti sono validati per tipo, dimensione e contenuto. |  |  |  |

### 4.6 Crittografia

| **#** | **Requisito** | **Applicabile (Si/No)** | **Esito** | **Note/Evidenze** |
| ----- | ------------- | ------------------------ | --------- | ------------------ |
| 6.1   | I dati in transito sono protetti tramite protocolli cifrati (HTTPS/TLS). |  |  |  |
| 6.2   | I dati riservati/personali a riposo sono protetti tramite cifratura, ove applicabile. |  |  |  |
| 6.3   | Sono utilizzate esclusivamente librerie crittografiche standard e mantenute (nessun algoritmo custom). |  |  |  |

### 4.7 Gestione degli Errori e Logging

| **#** | **Requisito** | **Applicabile (Si/No)** | **Esito** | **Note/Evidenze** |
| ----- | ------------- | ------------------------ | --------- | ------------------ |
| 7.1   | I messaggi di errore verso l'utente non rivelano dettagli tecnici sensibili. |  |  |  |
| 7.2   | I log applicativi non contengono dati sensibili in chiaro. |  |  |  |
| 7.3   | Sono tracciati eventi rilevanti per la sicurezza (accessi falliti, modifiche permessi). |  |  |  |

### 4.8 Gestione delle Dipendenze e della Configurazione

| **#** | **Requisito** | **Applicabile (Si/No)** | **Esito** | **Note/Evidenze** |
| ----- | ------------- | ------------------------ | --------- | ------------------ |
| 8.1   | Le dipendenze di terze parti sono aggiornate e prive di vulnerabilità note. |  |  |  |
| 8.2   | Segreti e credenziali non sono presenti nel codice sorgente o nei repository. |  |  |  |
| 8.3   | Gli ambienti di sviluppo, test e produzione sono separati e configurati in modo indipendente. |  |  |  |

### 4.9 Comunicazioni e Servizi Esterni/API

| **#** | **Requisito** | **Applicabile (Si/No)** | **Esito** | **Note/Evidenze** |
| ----- | ------------- | ------------------------ | --------- | ------------------ |
| 9.1   | Le API esposte richiedono autenticazione/autorizzazione appropriate. |  |  |  |
| 9.2   | Le API sono state verificate tramite test manuali/automatici (es. Postman). |  |  |  |
| 9.3   | Le integrazioni con servizi di terze parti (incluse soluzioni AI/LLM) sono state valutate per i rischi di esposizione dati. |  |  |  |

## 5 Esito Complessivo e Firma

| **Campo**                         | **Valore** |
| ---------------------------------- | ---------- |
| Numero non conformità rilevate      |            |
| Non conformità critiche/bloccanti   |            |
| Esito complessivo (Approvato / Approvato con riserva / Non approvato) |            |
| Verificato da                       |            |
| Data                                |            |

## 6 Riferimenti

> PO25 - Sviluppo Sicuro

> ALPO25.A - Regole scrittura codice

> MDPO25.B - Definizione dei Requisiti \[progetto\]

> MDPO25.C - Documentazione Tecnica \[progetto\].
