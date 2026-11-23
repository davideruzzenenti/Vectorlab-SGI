# PO25 - Sviluppo Sicuro

**Politica Sviluppo Sicuro**

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0 | 17/11/2026 | Emissione | RSGI | Da approvare |
| 0.1 | 23/11/2026 | Requisiti, documentazione tecnica e test negli strumenti del cliente; ritirati i modelli MDPO25.A–G | RSGI | Da approvare |

## 1 Scopo e campo di applicazione

La politica dice come il team di Vectorlab sviluppa software in modo
sicuro nei progetti dei clienti, in cui è inserito con il servizio della
business unit Ynsera ([PO02](../4_CONTESTO/PO02%20-%20Gestione%20del%20Contesto.md) §4). Vale per gli sviluppatori dipendenti,
per il PM della commessa e per chiunque collabori allo sviluppo,
compresi i fornitori esterni (§6).

Nei progetti dei clienti il team usa gli strumenti, i repository e gli
ambienti del cliente e ne segue le regole: quando le regole del cliente
sono più severe di questa politica, valgono quelle del cliente. Questa
politica fissa il minimo che Vectorlab garantisce comunque.

Il processo di commessa (offerta, avvio, erogazione, chiusura) è
descritto in [PR35.1](../8.2_PRODOTTI%20%26%20SERVIZI/PR35.1%20-%20Digital.md) - Digital.

## 2 Riferimenti

- ISO/IEC 27001 (UNI CEI EN ISO/IEC 27001:2024+A1:2024), Annex A:
  A.5.8, A.8.4, A.8.8, A.8.25, A.8.26, A.8.27, A.8.28, A.8.29, A.8.31,
  A.8.33; A.8.30 per lo sviluppo affidato all'esterno (§6)
- ISO 9001:2026, 8.3 Progettazione e sviluppo di prodotti e servizi
- [PR35.1](../8.2_PRODOTTI%20%26%20SERVIZI/PR35.1%20-%20Digital.md) - Digital; [PR16.1](../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md) - Gestione degli Accessi; [PR27.1](../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach.md) -
  Eventi e incidenti; [PR26.1](../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori.md) - Fornitori; [REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) - Regolamento
  sull'utilizzo degli strumenti aziendali
- [ALPO25.A](ALPO25.A%20-%20Linee%20guida%20per%20lo%20sviluppo%20software.md) - Linee guida per lo sviluppo software

## 3 Responsabilità

- **CTO**: mantiene la politica, decide gli strumenti di sviluppo
  ammessi, gestisce l'organizzazione GitHub vectorlab-cg e i suoi
  accessi.
- **PM della commessa**: concorda con il cliente regole, strumenti e
  ambienti del progetto e verifica che il team li rispetti.
- **Sviluppatori**: applicano la politica e segnalano subito problemi
  di sicurezza (§5.6).
- **CISO**: verifica l'applicazione della politica, anche con l'audit
  interno.

## 4 Ambiente di sviluppo

### 4.1 Postazioni

Gli sviluppatori lavorano su portatili Windows forniti da Vectorlab
con i requisiti di [REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §3 (disco cifrato, blocco dello schermo,
aggiornamenti automatici, antivirus attivo) e, quando il cliente lo
richiede, su macchine del cliente. Si installano solo strumenti
ammessi ([ALPR05.1.G](../7_GESTIONE%20RISORSE/ALPR05.1.G%20-%20Lista%20software%20permessi.md)); gli strumenti di intelligenza artificiale sono
quelli autorizzati in [PR35.1](../8.2_PRODOTTI%20%26%20SERVIZI/PR35.1%20-%20Digital.md) §2.3.

### 4.2 Codice sorgente e repository

Il codice dei progetti sta nei repository del cliente e, quando serve,
nell'organizzazione GitHub di Vectorlab **vectorlab-cg**.

- Nell'organizzazione vectorlab-cg ogni persona entra con il proprio
  account nominativo e con la **verifica in due passaggi obbligatoria**.
  [DA CONFERMARE con il CTO: se il secondo fattore si gestisce in
  Bitwarden o sull'app del telefono personale.]
- Gli accessi ai repository sono dati solo a chi lavora sul progetto e
  tolti a fine progetto o all'uscita della persona ([PR16.1](../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md)). Il PM
  segnala al CTO gli ingressi e le uscite dal team.
- Il codice dei clienti non si copia su servizi o account diversi da
  quelli concordati con il cliente.

### 4.3 Ambienti di test

Gli ambienti di test sono sempre del cliente: Vectorlab non gestisce
ambienti di test propri per i progetti dei clienti. Il PM concorda con
il cliente chi vi accede e con quali dati; nei test non si usano dati
personali reali, salvo accordo scritto con il cliente.

### 4.4 Password, chiavi e token

Password, chiavi e token di progetto si conservano nel **Bitwarden
aziendale** e non si scrivono mai nel codice, nei commit, nei task o
nelle mail. Un segreto finito per errore in un repository si considera
compromesso: si cambia subito e si segnala come evento di sicurezza
([PR27.1](../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach.md)).

## 5 Ciclo di sviluppo

### 5.1 Requisiti

All'avvio della commessa il PM raccoglie con il cliente i requisiti,
compresi quelli di sicurezza e privacy (ISO 9001 8.3; A.8.26).
Requisiti, documentazione tecnica e piano di test li scrive il cliente
nei propri strumenti; il team lavora su quella documentazione (deciso
il 23/11/2026). Se il software tratta dati personali, i requisiti di privacy
by design li indica il cliente, che è titolare del trattamento.

### 5.2 Scrittura del codice

Il team segue le linee guida [ALPO25.A](ALPO25.A%20-%20Linee%20guida%20per%20lo%20sviluppo%20software.md) (A.8.27, A.8.28).

### 5.3 Revisione del codice

Ogni modifica è rivista prima del rilascio da un **collega Vectorlab**
e, quando il cliente la prevede, dal **cliente sulle pull request**.
La revisione resta tracciata nella pull request (A.8.25, A.8.29).
[DA CONFERMARE con il CTO: se la revisione di un collega avviene
sempre o solo dove la prevede il cliente.]

### 5.4 Librerie e vulnerabilità

Le vulnerabilità delle librerie usate sono controllate dal team con
strumenti automatici (per esempio Dependabot, npm audit o simili) e,
quando previsto, dal cliente [DA CONFERMARE con il CTO: strumenti
attivi oggi; vedi [PR23.1](../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche.md) §6]. Le vulnerabilità gravi si correggono
prima del rilascio o si segnalano al cliente (A.8.8).

### 5.5 Test e rilascio

I test si svolgono negli ambienti del cliente, secondo il piano di test
del cliente. Il rilascio in produzione lo decide il cliente.
Ambienti di sviluppo, test e produzione restano separati come previsto
dal cliente (A.8.31).

### 5.6 Problemi di sicurezza

Chi scopre un problema di sicurezza (una vulnerabilità, un segreto
esposto, un accesso anomalo) lo segnala subito al PM e a
sicurezza@vectorlab-cg.com; il PM informa il cliente. Si segue [PR27.1](../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach.md).

## 6 Sviluppo affidato all'esterno

Se una parte dello sviluppo è affidata a un fornitore esterno, il
fornitore firma un accordo di riservatezza ([ALPR26.1.B.3](../A_FORNITORI/ALPR26.1.B.3%20-%20Accordo%20di%20Riservatezza%20con%20le%20Terze%20Parti.md)), riceve
questa politica e le regole del progetto, lavora con account nominativi
e il suo lavoro passa dalla stessa revisione del §5.3 (A.8.30;
[PR26.1](../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori.md)).

Oggi Vectorlab non affida a terzi lo sviluppo nei progetti dei clienti:
i consulenti tecnici esterni che lavorano per clienti hanno un contratto
diretto con il cliente, e Vectorlab ne cura solo la parte amministrativa
e contabile. Per questo il controllo A.8.30 è escluso nella SoA; questa
sezione si applica se in futuro Vectorlab affiderà a un fornitore una
parte dello sviluppo che vende al cliente.

## 7 Riesame

La politica si riesamina una volta l'anno, prima del Riesame della
Direzione, e quando cambiano gli strumenti o il modo di lavorare con i
clienti.

## 8 Registrazioni

| Registrazione | Dove | Conservazione |
| --- | --- | --- |
| Pull request con revisione del codice | Repository del cliente o di vectorlab-cg | Secondo il repository |
| Requisiti e piano di test di progetto | Strumenti del cliente | Secondo [MDPO15.A](../A_CLASSIFICAZIONE%20INFORMAZIONI/MDPO15.A%20-%20Data%20Retention%20informazioni%20aziendali.md) |
| Accessi all'organizzazione vectorlab-cg | GitHub; revisione semestrale [PR16.1](../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md) §6 | Secondo [MDPO15.A](../A_CLASSIFICAZIONE%20INFORMAZIONI/MDPO15.A%20-%20Data%20Retention%20informazioni%20aziendali.md) |
| Segnalazioni di problemi di sicurezza | Lista ClickUp «Non conformità e miglioramento» ([PR27.1](../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach.md)) | Secondo [PR13.1](../10_GESTIONE%20NON%20CONFORMITA_%20E%20MIGLIORAMENTO/PR13.1%20-%20Gestione%20delle%20Non%20Conformit%C3%A0%20e%20Azioni%20di%20Miglioramento.md) |
