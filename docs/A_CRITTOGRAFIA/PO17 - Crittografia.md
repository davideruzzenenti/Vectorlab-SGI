# PO17 - Crittografia

**Politica sull'Uso della Crittografia**

<div style="border-left:4px solid #2A5C8A;background:#EAF1F7;padding:.75rem 1rem;margin:1rem 0">
<strong>DOCUMENTO IN BOZZA — generato il 16/07/2026</strong> per colmare una lacuna rilevata durante la revisione della documentazione (citato nella SOA ma non ancora creato). Contenuto basato su pratiche reali già note da altri documenti del SGI; le parti evidenziate in rosso sono da confermare prima dell'approvazione formale.
</div>

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.1      | 16/07/2026 | Prima bozza — documento mancante generato per colmare una lacuna rilevata nella SOA | IA          | Da approvare  |
|          |            |                 |             |               |

## 1 Introduzione

### 1.1 Scopo

La presente politica descrive i principi e le regole adottate da
VECTORLAB per l'utilizzo della crittografia a protezione della
riservatezza, dell'integrità e, ove applicabile, dell'autenticità delle
informazioni trattate durante il loro ciclo di vita (in transito, a
riposo e in uso).

Il documento ha lo scopo di:

- definire quando e come la crittografia deve essere utilizzata a
  protezione delle informazioni aziendali e dei dati personali trattati;

- definire i criteri generali di gestione delle chiavi crittografiche,
  per quanto di competenza di VECTORLAB, tenuto conto che la maggior
  parte dei servizi utilizzati è erogata in modalità cloud/SaaS con
  gestione della crittografia demandata al fornitore;

- assicurare la coerenza tra le misure di cifratura adottate e il
  livello di classificazione delle informazioni definito in "*PO15 -
  Politica Classificazione Informazioni*".

### 1.2 Campo di applicazione

La presente politica si applica a tutti i sistemi, dispositivi,
applicazioni e servizi (inclusi i servizi cloud e SaaS) utilizzati da
VECTORLAB per il trattamento, la trasmissione e la conservazione delle
informazioni aziendali e dei dati personali, nonché a tutto il
personale, dipendente e collaboratore esterno, che ne fa uso.

### 1.3 Riferimenti e Allegati

> PO15 - Politica Classificazione Informazioni

> PO16 - Gestione degli Accessi

> PO32 - Gestione delle Configurazioni

> PR14.1 - Gestione Asset

> PR21.1 - Gestione dei Backup e Restore

> PR32.1 - Gestione delle Configurazioni

> PR33.1 - Processo Analisi del Rischio e Trattamento

> REG01 - Regolamento sull'utilizzo degli strumenti informatici
> aziendali

> SOA - Statement of Applicability - Dichiarazione di Applicabilità.

### 1.4 Definizioni, Acronimi, Abbreviazioni

> AdS - Amministratore di Sistema

> CISO - Chief Information Security Officer

> HTTPS - HyperText Transfer Protocol Secure

> RSGI - Responsabile del Sistema di Gestione Integrato

> SaaS - Software as a Service

> SGI - Sistema di Gestione Integrato

> TLS - Transport Layer Security.

## 2 Responsabilità

Il CISO (ruolo ricoperto dall'Amministratore Unico) è responsabile
della definizione delle regole di utilizzo della crittografia e della
loro comunicazione al personale.

L'IT è responsabile dell'applicazione tecnica delle misure di cifratura
sui dispositivi e sistemi sotto la propria gestione, nonché della
verifica, ove tecnicamente possibile, che i servizi cloud/SaaS
utilizzati adottino protocolli di trasmissione sicuri.

Ogni Owner di asset o di informazione (cfr. "*PR14.1 - Gestione Asset*"
e "*PO15 - Politica Classificazione Informazioni*") è responsabile di
verificare che il livello di protezione crittografica applicato sia
adeguato alla classificazione dell'informazione trattata.

## 3 Principi Generali di Utilizzo della Crittografia

VECTORLAB adotta la crittografia come misura di sicurezza tecnica
principalmente orientata alla protezione dei dati in transito, in
coerenza con il modello operativo dell'Azienda, fortemente basato su
infrastrutture e servizi cloud/SaaS di terze parti (AWS, Google
Workspace, GitHub, server Aruba gestito in modalità
Infrastructure-as-Code) piuttosto che su un'infrastruttura on-premise
proprietaria.

La necessità di utilizzo della crittografia e il livello di protezione
richiesto sono determinati in base a:

- il livello di classificazione dell'informazione trattata (cfr. "*PO15
  - Politica Classificazione Informazioni*");

- gli esiti del processo di analisi del rischio (cfr. "*PR33.1 -
  Processo Analisi del Rischio e Trattamento*");

- eventuali obblighi contrattuali o normativi (es. GDPR) applicabili al
  trattamento.

Per prassi, tutte le informazioni classificate come "Confidenziale" e i
dati personali oggetto di trasmissione o conservazione elettronica
devono essere protetti mediante crittografia, salvo che ciò non sia
tecnicamente possibile.

## 4 Crittografia dei Dati in Transito

VECTORLAB utilizza meccanismi di crittografia per proteggere i dati
durante la trasmissione, in particolare tramite l'utilizzo di protocolli
sicuri (HTTPS/TLS) nei servizi cloud e SaaS adottati. I dati sono
protetti mediante le misure di sicurezza implementate dai fornitori dei
servizi.

In particolare:

- l'accesso a tutte le piattaforme cloud e SaaS aziendali (AWS, Google
  Workspace, GitHub) avviene esclusivamente tramite connessioni cifrate
  HTTPS/TLS;

- l'accesso da remoto alla rete aziendale, ove necessario, avviene
  tramite VPN aziendale (cfr. "*REG01 - Regolamento sull'utilizzo degli
  strumenti informatici aziendali*");

- è vietato l'utilizzo di strumenti di comunicazione (es. instant
  messaging, SMS, social network, file sharing) che non garantiscano la
  crittografia per lo scambio di informazioni classificate come
  "Confidenziale" (cfr. "*PO15 - Politica Classificazione
  Informazioni*").

<span style="color:#B3392A">[DA CONFERMARE: versione minima di TLS
richiesta/accettata (es. TLS 1.2 o superiore) e relativa modalità di
verifica periodica, poiché non risultano attualmente definite in modo
esplicito in alcun documento del SGI]</span>.

## 5 Crittografia dei Dati a Riposo

I dati conservati sui servizi cloud utilizzati da VECTORLAB (es. AWS S3,
AWS EFS) sono protetti secondo le misure di sicurezza rese disponibili
dai relativi fornitori. In particolare, i parametri di configurazione e
i segreti applicativi (es. credenziali, stringhe di connessione) sono
conservati in forma cifrata all'interno di AWS Parameter Store.

Per quanto riguarda i dispositivi aziendali (PC portatili e fissi):

- i dispositivi di archiviazione rimovibili (chiavette USB, hard disk
  esterni, schede SD) contenenti dati aziendali classificati come
  "riservati/confidenziali" devono essere protetti con crittografia
  (cfr. "*PR14.1 - Gestione Asset*", par. 2.6);

- <span style="color:#B3392A">[DA CONFERMARE: se sia attiva la
  cifratura dell'intero disco (full disk encryption, es. BitLocker su
  Windows o FileVault su macOS) su tutti i PC aziendali in dotazione, o
  se tale misura sia limitata ad alcuni dispositivi/categorie di dati]
  </span>.

I backup aziendali, gestiti tramite strumenti cloud secondo quanto
descritto in "*PR21.1 - Gestione dei Backup e Restore*", ereditano le
misure di cifratura messe a disposizione dal fornitore del servizio
cloud utilizzato.

## 6 Gestione delle Chiavi Crittografiche

Data la scelta architetturale di VECTORLAB di appoggiarsi
prevalentemente a servizi cloud/SaaS di terze parti, la generazione, la
custodia e la rotazione delle chiavi crittografiche utilizzate per
proteggere i dati in transito e a riposo sono, nella maggior parte dei
casi, demandate ai fornitori dei servizi stessi, nell'ambito delle
misure di sicurezza da essi implementate.

Per i segreti e i parametri applicativi gestiti direttamente
dall'Azienda (es. credenziali di servizio, stringhe di connessione), la
custodia in forma cifrata avviene tramite AWS Parameter Store, con
accesso limitato al personale IT autorizzato.

<span style="color:#B3392A">[DA CONFERMARE: esistenza di una procedura
formale di rotazione periodica delle chiavi/credenziali applicative e
di un processo strutturato di revoca in caso di compromissione, non
risultando ad oggi documentati in modo specifico]</span>.

VECTORLAB richiede che, per i servizi Cloud che trattano informazioni
classificate come "Confidenziale" o "Interno", i dati archiviati siano
cifrati e che, ove contrattualmente possibile, le chiavi rimangano nella
disponibilità di VECTORLAB (cfr. "*PO15 - Politica Classificazione
Informazioni*").

## 7 Violazione della Politica

Qualsiasi azione non conforme alla presente politica sarà considerata
una violazione della sicurezza e come tale potrà tradursi nella
sospensione dell'accesso alle risorse informatiche, rete e documenti,
oltre a eventuali provvedimenti disciplinari in conformità alla
normativa vigente.

## 8 Riesame

La revisione della presente politica è effettuata da RSGI almeno una
volta all'anno e prima del riesame della Direzione, e in risposta a
cambiamenti significativi dell'ambiente organizzativo, tecnologico o
normativo (es. deprecazione di protocolli o algoritmi crittografici).
