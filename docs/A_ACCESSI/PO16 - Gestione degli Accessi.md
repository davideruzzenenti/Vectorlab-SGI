# PO16 - Gestione degli Accessi

**Politica di Gestione degli Accessi**

<div style="border-left:4px solid #2A5C8A;background:#EAF1F7;padding:.75rem 1rem;margin:1rem 0">
<strong>DOCUMENTO IN BOZZA — generato il 16/07/2026</strong> per colmare una lacuna rilevata durante la revisione della documentazione (citato nella SOA ma non ancora creato). Contenuto basato su pratiche reali già note da altri documenti del SGI; le parti evidenziate in rosso sono da confermare prima dell'approvazione formale.
</div>

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.1      | 16/07/2026 | Prima bozza — documento mancante generato per colmare una lacuna rilevata nella SOA | IA          | Da approvare  |
|          |            |                 |             |               |

## 1 Introduzione

### 1.1 Scopo e Campo di applicazione

La presente politica descrive i principi che VECTORLAB adotta per
governare il ciclo di vita degli accessi logici alle proprie
informazioni, applicazioni, sistemi e infrastrutture, sia on-premise
che in cloud, al fine di garantire che l'accesso a ciascuna risorsa sia
concesso solo a soggetti autorizzati, per le finalità necessarie allo
svolgimento delle proprie mansioni e nel rispetto dei principi di
"need-to-know" e minimo privilegio.

Il documento ha lo scopo di:

- definire i principi generali di gestione delle utenze e dei
  privilegi di accesso ai sistemi informativi aziendali;

- stabilire le responsabilità delle funzioni coinvolte nel processo di
  provisioning, modifica e revoca degli accessi;

- assicurare che l'accesso alle informazioni sia coerente con il
  livello di classificazione delle stesse (cfr. "*PO15 - Politica
  Classificazione Informazioni*");

- ridurre il rischio di accessi non autorizzati, abuso di privilegi e
  perdita di riservatezza, integrità e disponibilità delle
  informazioni.

Il presente documento si applica a tutto il personale di VECTORLAB
(dipendenti e collaboratori), ai collaboratori esterni e alle terze
parti che, a qualunque titolo, necessitano di accedere a sistemi,
applicazioni, reti o informazioni di proprietà di VECTORLAB o dei suoi
Clienti. Si applica sia agli accessi verso l'infrastruttura cloud
(AWS, server Aruba gestito in modalità Infrastructure-as-Code, Google
Workspace) sia agli strumenti applicativi e di collaborazione in uso
in Azienda.

Le modalità operative di attuazione della presente politica sono
descritte in "*PR16.1 - Gestione degli Accessi*".

### 1.2 Riferimenti e Allegati

> ALPO31.A - Lettera incarico AdS

> ALPR16.1.A - Lista utenze

> MDPR05.1.A - Checklist Documenti per Inserimento Personale

> MDPR05.1.L - Checklist documenti per uscita personale

> MDPR05.1.V - Modulo_consegna_riconsegna_HW_utenze

> PO15 - Politica Classificazione Informazioni

> PO17 - Crittografia

> PO32 - Gestione delle Configurazioni

> PR14.1 - Gestione Asset

> PR16.1 - Gestione degli Accessi

> PR18.1 - Gestione sicurezza fisica e ambientale

> PR24.1 - Gestione delle Reti

> PR27.1 - Gestione degli incidenti e dei data breach

> PR33.1 - Processo Analisi del Rischio e Trattamento

> REG01 - Regolamento sull'utilizzo degli strumenti aziendali

> SOA - Statement of Applicability - Dichiarazione di Applicabilità.

### 1.3 Definizioni, Acronimi, Abbreviazioni

> AdS - Amministratore di Sistema

> IAM - Identity and Access Management

> MFA - Multi-Factor Authentication

> RSGI - Responsabile del Sistema di Gestione Integrato

> SGI - Sistema di Gestione Integrato

> SSO - Single Sign-On.

## 2 Principi Generali di Gestione degli Accessi

### 2.1 Need-to-know e minimo privilegio

L'accesso a informazioni, applicazioni e sistemi è concesso
esclusivamente sulla base dell'effettiva necessità operativa legata al
ruolo ricoperto (principio del "need-to-know") e limitato al minimo
insieme di privilegi necessario per svolgere le proprie mansioni
(principio del "minimo privilegio"). L'attribuzione di privilegi
estesi o amministrativi (es. accesso amministrativo alla console AWS,
ai repository GitHub dell'organizzazione, ai database di produzione)
è riservata a un numero ristretto di persone e motivata da specifiche
esigenze di ruolo (System Administrator, CTO/Amministratore Unico).

### 2.2 Account nominali e responsabilità individuale

Ogni accesso ai sistemi aziendali avviene tramite account nominali e
individuali, non condivisi tra più persone, in modo da garantire la
tracciabilità e la responsabilità individuale delle azioni compiute.
L'uso di account generici o condivisi è vietato, salvo eccezioni
tecniche debitamente motivate e approvate (es. account di servizio
utilizzati da automazioni), che devono comunque essere censite e
avere un Owner responsabile della loro gestione.

Ogni persona autorizzata è responsabile della riservatezza delle
proprie credenziali e di qualunque azione compiuta con il proprio
account, in coerenza con quanto previsto da "*REG01 - Regolamento
sull'utilizzo degli strumenti aziendali*".

### 2.3 Autenticazione e MFA

L'accesso ai servizi aziendali richiede un meccanismo di
autenticazione (tipicamente user id e password), integrato ove
disponibile da un secondo fattore di autenticazione (MFA), in
particolare per i servizi cloud principali (AWS, Google Workspace,
GitHub). L'attivazione della MFA è fortemente raccomandata per tutti
gli account con accesso a informazioni classificate come
"Confidenziale" (cfr. "*PO15 - Politica Classificazione
Informazioni*") e per tutti gli account con privilegi amministrativi.

I requisiti di complessità, storicità e durata delle password sono
definiti in "*REG01 - Regolamento sull'utilizzo degli strumenti
aziendali*" e si applicano a tutte le utenze aziendali, salvo
meccanismi di autenticazione più stringenti già previsti dal singolo
servizio (es. SSO federato).

Tutti i servizi web aziendali sono acceduti tramite connessioni
cifrate (HTTPS/TLS), in coerenza con quanto descritto in "*PO17 -
Crittografia*".

### 2.4 Segregazione dei ruoli e Amministratore di Sistema

La gestione tecnica delle utenze (creazione, modifica, disattivazione)
è affidata al System Administrator, che opera secondo il profilo di
Amministratore di Sistema (AdS) formalmente designato ai sensi della
normativa privacy applicabile (cfr. "*ALPO31.A - Lettera incarico
AdS*"). In coerenza con tale designazione:

- gli accessi logici effettuati dagli AdS sui sistemi di elaborazione
  e sugli archivi elettronici sono registrati (access log), con
  riferimenti temporali e descrizione dell'evento;

- tali registrazioni sono conservate per un periodo minimo di sei
  mesi e non possono essere modificate, cancellate o alterate;

- l'operato degli AdS è oggetto di verifica periodica, con cadenza
  almeno annuale, da parte del Titolare (Amministratore Unico), anche
  attraverso il controllo dei log di accesso, disconnessione ed
  errore di autenticazione.

L'approvazione delle richieste di accesso e la definizione dei
profili autorizzativi (chi può accedere a cosa) resta in capo al
responsabile della funzione richiedente e, per gli accessi più
critici, al RSGI o al CTO/Amministratore Unico, secondo quanto
descritto in "*PR16.1 - Gestione degli Accessi*", in modo da separare
la funzione di autorizzazione da quella di esecuzione tecnica.

## 3 Ciclo di Vita delle Utenze

### 3.1 Provisioning (assunzione/onboarding)

All'atto dell'inserimento di una nuova risorsa (dipendente o
collaboratore), a fronte della checklist di onboarding "*MDPR05.1.A -
Checklist Documenti per Inserimento Personale*", vengono create le
utenze nominali necessarie per lo svolgimento delle mansioni previste,
secondo il principio del minimo privilegio. Le utenze e i relativi
strumenti/dispositivi assegnati sono tracciati tramite "*MDPR05.1.V -
Modulo_consegna_riconsegna_HW_utenze*".

### 3.2 Modifica dei privilegi (cambio ruolo)

In caso di cambio di ruolo, mansione o responsabilità, i privilegi di
accesso vengono rivisti e adeguati alle nuove esigenze, rimuovendo gli
accessi non più necessari e assegnando i nuovi, secondo le medesime
modalità di richiesta e approvazione previste per il provisioning
iniziale.

### 3.3 Revoca (cessazione/offboarding)

Alla cessazione del rapporto di lavoro o collaborazione, tutte le
utenze assegnate vengono disattivate secondo quanto previsto dalla
checklist di uscita "*MDPR05.1.L - Checklist documenti per uscita
personale*" e dalla restituzione degli strumenti aziendali tramite
"*MDPR05.1.V - Modulo_consegna_riconsegna_HW_utenze*". Per l'account
di posta elettronica si applica in aggiunta la procedura specifica
descritta in "*REG01 - Regolamento sull'utilizzo degli strumenti
aziendali*" (disattivazione delle credenziali, risponditore
automatico per un periodo definito, rimozione definitiva dell'account
al termine del periodo).

Coerentemente con quanto previsto per gli Amministratori di Sistema
(cfr. "*ALPO31.A - Lettera incarico AdS*"), le credenziali di accesso
non utilizzate per un periodo superiore a sei mesi vengono
disattivate anche in assenza di una cessazione formale del rapporto.

### 3.4 Riesame periodico degli accessi

<span style="color:#B3392A">[DA CONFERMARE: con cadenza almeno annuale (o secondo diversa periodicità da definire), il RSGI e il System Administrator effettuano un riesame delle utenze attive e dei relativi privilegi, censiti in "ALPR16.1.A - Lista utenze", per verificare la coerenza tra ruoli assegnati e accessi concessi ed eventualmente disattivare utenze non più necessarie]</span>.

## 4 Accesso ai Sistemi e alle Infrastrutture Critiche

### 4.1 Ambienti Cloud (AWS, server Aruba)

L'infrastruttura di produzione di VECTORLAB è ospitata su Amazon Web
Services (EC2, ECS, S3, EFS, CloudWatch, CloudFront, Parameter Store)
e su un server Aruba gestito in modalità Infrastructure-as-Code.
L'accesso alla console e alle risorse AWS è regolato tramite utenze
nominali con privilegi assegnati in base al ruolo (IAM), riservando i
privilegi amministrativi al System Administrator e al CTO/
Amministratore Unico. I parametri e i segreti applicativi sono
gestiti tramite AWS Parameter Store, limitando la loro visibilità al
personale e ai sistemi effettivamente autorizzati.

### 4.2 Google Workspace

L'intero personale VECTORLAB dispone di un account nominale
Google Workspace (email, drive, calendar), utilizzato anche come
identità per l'accesso ad altri strumenti aziendali. La gestione di
tali account (creazione, modifica dei permessi di condivisione,
revoca) segue i medesimi principi descritti al capitolo 3.

### 4.3 Repository di codice (GitHub)

L'accesso ai repository di codice sorgente e alle pipeline di CI/CD
(GitHub Actions) è concesso su base nominale e per il tempo/progetto
di effettiva necessità, secondo il principio del minimo privilegio
(es. permessi di sola lettura, scrittura o amministrazione a livello
di singolo repository o team). L'accesso ai repository da parte di
collaboratori esterni e sviluppatori in P.IVA è subordinato alla
sottoscrizione di accordi di riservatezza (NDA), coerentemente con
quanto previsto in "*PR14.1 - Gestione Asset*".

### 4.4 Strumenti di produttività, tracciamento e automazione

Le medesime regole si applicano agli altri strumenti in uso in
Azienda, tra cui, a titolo esemplificativo: ClickUp e Jira
(ticketing/project tracking), Postman (test e documentazione API),
MongoDB (base dati applicativa), N8N (automazioni), Discord
(comunicazione interna/di team) e Bitwarden (gestione centralizzata di
password e segreti). L'accesso a ciascuno di questi strumenti è
concesso su base nominale e limitato al personale che ne necessita per
lo svolgimento delle proprie attività.

## 5 Gestione delle Credenziali e dei Segreti

Le credenziali e i segreti applicativi (chiavi API, token, password di
servizio) sono gestiti attraverso strumenti dedicati (Bitwarden per le
credenziali condivise di team; AWS Parameter Store per i parametri e
segreti applicativi in produzione), evitando la loro conservazione in
chiaro nel codice sorgente, in ticket, in chat o in altri strumenti non
dedicati.

Ulteriori dettagli sulle modalità di gestione delle password personali
(complessità, durata, custodia) sono definiti in "*REG01 - Regolamento
sull'utilizzo degli strumenti aziendali*".

## 6 Accesso di Terze Parti

L'accesso di fornitori, consulenti e altre terze parti ai sistemi e
alle informazioni di VECTORLAB è concesso solo previa valutazione
della necessità, sottoscrizione di accordi di riservatezza (NDA) e,
ove applicabile, di specifiche clausole contrattuali in materia di
sicurezza delle informazioni. Gli accessi fisici di terze parti alla
sede sono regolati da "*PR18.1 - Gestione sicurezza fisica e
ambientale*".

## 7 Responsabilità

RSGI ha la responsabilità di redigere, mantenere aggiornata e
comunicare la presente politica.

Il System Administrator è responsabile dell'esecuzione tecnica delle
attività di provisioning, modifica e revoca degli accessi, secondo le
autorizzazioni ricevute.

Il personale, a qualsiasi livello, e i collaboratori esterni devono
attenersi alla presente politica e alla procedura "*PR16.1 - Gestione
degli Accessi*" e sono responsabili della corretta custodia delle
proprie credenziali.

## 8 Violazione della Politica

Qualsiasi azione non conforme alla presente politica sarà considerata
una violazione della sicurezza e come tale potrà tradursi nella
sospensione dell'accesso ai sistemi e alle risorse informatiche.
L'uso improprio degli strumenti aziendali costituisce una grave
violazione del dovere di correttezza e può comportare l'adozione di
provvedimenti disciplinari in conformità alla normativa vigente. I
casi gravi saranno segnalati all'autorità competente e potranno essere
oggetto di provvedimenti disciplinari o legali.

## 9 Riesame

La revisione della presente politica è effettuata da RSGI almeno una
volta all'anno e prima del riesame della Direzione, e in risposta a
cambiamenti significativi dell'ambiente organizzativo, del business, di
riferimenti normativi o dell'ambiente tecnologico aziendale.
