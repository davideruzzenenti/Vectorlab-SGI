# PO30 - Privacy by design e by default

**Politica sui principi di Privacy by Design e by Default**

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

Il presente documento definisce le linee guida adottate da Vectorlab per
l'applicazione dei principi di *Privacy by Design* e *Privacy by Default*
sanciti dall'art. 25 del GDPR, con particolare riferimento alla
progettazione e allo sviluppo dei prodotti e servizi software realizzati da
Vectorlab per conto dei propri clienti.

La politica si applica a tutti i progetti di sviluppo software, interni e
per conto di clienti, e a tutto il personale tecnico (sviluppatori,
architetti) coinvolto nelle fasi di progettazione, sviluppo, test e
rilascio del software.

### 1.2 Riferimenti e Allegati

> REGOLAMENTO (UE) 2016/679 DEL PARLAMENTO EUROPEO E DEL CONSIGLIO del 27
> aprile 2016 relativo alla protezione delle persone fisiche con riguardo
> al trattamento dei dati personali (GDPR) - art. 25

> Linee guida 4/2019 sull'articolo 25 "Protezione dei dati fin dalla
> progettazione e per impostazione predefinita" v.02

> OWASP – Best Practices per lo sviluppo sicuro del software

> PO31 - Misure di sicurezza protezione dati personali

> PR33.2 - Processo Analisi del Rischio Privacy

> PR31.3 - Procedura Valutazione d'impatto sulla protezione dei dati (DPIA)

> MDPR31.4.A - Registro dei Trattamenti Titolare

> MDPR31.4.B - Registro dei Trattamenti Responsabile

### 1.3 Definizioni, Acronimi, Abbreviazioni

> DPIA – Data Protection Impact Assessment

> EDPB – European Data Protection Board

> GDPR – General Data Protection Regulation

> SDLC – Software Development Life Cycle.

## 2 Principi di Privacy by Design e by Default

Vectorlab adotta, per la progettazione e lo sviluppo dei propri prodotti e
servizi software, i principi fondamentali di *Privacy by Design*, in linea
con quanto previsto dall'art. 25 GDPR e dalle Linee guida EDPB 4/2019:

  - **Proattività, non reattività** - i rischi per la protezione dei dati
    devono essere anticipati e prevenuti fin dalle prime fasi di
    progettazione, non affrontati a posteriori;

  - **Privacy come impostazione predefinita** - le impostazioni di
    default di un sistema o servizio devono garantire il massimo livello
    di protezione dei dati personali, senza richiedere un'azione da
    parte dell'utente;

  - **Privacy incorporata nella progettazione** - la protezione dei dati
    deve essere parte integrante dell'architettura dei sistemi e dei
    processi, non un elemento aggiunto successivamente;

  - **Piena funzionalità** - l'adozione di misure di protezione dei dati
    non deve compromettere la funzionalità del prodotto o servizio (logica
    win-win tra esigenze di business e tutela degli interessati);

  - **Sicurezza fin dall'inizio e per l'intero ciclo di vita** - i dati
    devono essere protetti dalla loro raccolta fino alla loro
    cancellazione;

  - **Visibilità e trasparenza** - i componenti e le operazioni relative
    al trattamento dei dati devono restare visibili e verificabili;

  - **Rispetto della privacy dell'utente** - l'interesse dell'interessato
    deve essere posto al centro della progettazione, attraverso misure
    quali informative chiare, impostazioni di privacy facilmente
    accessibili e forme di controllo dell'utente sui propri dati.

## 3 Applicazione nel ciclo di vita di sviluppo software (SDLC)

Vectorlab integra i principi di privacy by design e by default nelle
diverse fasi del proprio ciclo di sviluppo software:

### 3.1 Fase di analisi dei requisiti

In fase di raccolta dei requisiti di un nuovo progetto o di una nuova
funzionalità, il team tecnico individua, con il supporto del Referente
Privacy laddove il progetto preveda il trattamento di dati personali, i
dati necessari al raggiungimento delle finalità del trattamento,
applicando il principio di minimizzazione. Qualora dalla valutazione
preliminare emerga un rischio elevato per i diritti e le libertà degli
interessati, si applica la metodologia di analisi del rischio privacy
descritta in *"PR33.2 - Processo Analisi del Rischio Privacy"*, con
eventuale attivazione della DPIA secondo *"PR31.3 - Procedura Valutazione
d'impatto sulla protezione dei dati (DPIA)"*.

### 3.2 Fase di progettazione

In fase di progettazione dell'architettura si privilegiano, ove
applicabili:

  - la minimizzazione dei dati raccolti e trattati, limitandoli a quanto
    strettamente necessario alla finalità del trattamento;

  - la pseudonimizzazione e, ove opportuno, l'anonimizzazione dei dati
    personali;

  - la cifratura dei dati personali in transito e a riposo;

  - un controllo degli accessi granulare, basato sul principio del
    minimo privilegio;

  - la definizione di politiche di conservazione (retention) e
    cancellazione dei dati coerenti con le finalità dichiarate;

  - impostazioni di default orientate alla protezione dell'utente (es.
    opt-in anziché opt-out per il trattamento di dati non strettamente
    necessari, visibilità minima dei dati personali nelle interfacce
    utente).

### 3.3 Fase di sviluppo

Lo sviluppo del software segue le pratiche di *secure coding* richiamate
nelle linee guida OWASP (cfr. *"PO31 - Misure di sicurezza protezione dati
personali"*). La revisione tra pari (*peer review*) del codice costituisce,
in coerenza con l'organizzazione snella di Vectorlab, una misura
compensativa per la verifica dell'applicazione dei principi di privacy by
design, in assenza di una funzione di revisione indipendente dedicata
<span style="color:#B3392A">[DA CONFERMARE: eventuale checklist privacy
by design formalizzata da integrare nel processo di code review, non
ancora presente come documento a sé stante]</span>.

### 3.4 Fase di test e rilascio

In fase di test si verifica che le impostazioni di default del prodotto
software siano effettivamente privacy-friendly e che siano rispettati i
requisiti di minimizzazione definiti in fase di progettazione. Prima del
rilascio, si verifica che il Registro dei Trattamenti (cfr. *"MDPR31.4.A -
Registro dei Trattamenti Titolare"* e *"MDPR31.4.B - Registro dei
Trattamenti Responsabile"*) e le informative agli interessati siano
aggiornati rispetto al nuovo trattamento introdotto.

### 3.5 Fase di manutenzione

Durante la manutenzione ordinaria e straordinaria del software (patch,
aggiornamenti, nuove funzionalità), viene rivalutata l'applicazione dei
principi di privacy by design qualora le modifiche comportino un impatto
sui dati personali trattati o sulle misure di sicurezza esistenti.

## 4 Privacy by default nei prodotti sviluppati per i clienti

Nell'ambito dei progetti di sviluppo software svolti per conto dei propri
clienti, Vectorlab opera tipicamente in qualità di fornitore/Responsabile
del trattamento. In tale contesto, Vectorlab garantisce che i prodotti
software siano progettati con impostazioni predefinite orientate alla
minimizzazione della raccolta e conservazione dei dati personali, salvo
diversa e consapevole configurazione da parte del cliente Titolare del
trattamento, il quale rimane responsabile delle finalità e delle modalità
complessive del trattamento.

## 5 Ruoli e responsabilità

  - il team tecnico (sviluppatori e architetti software) applica i
    principi di privacy by design e by default nelle attività di
    progettazione e sviluppo;

  - il Referente Privacy supporta il team tecnico nella valutazione dei
    rischi privacy e nell'individuazione delle misure adeguate;

  - l'Amministratore Unico approva la presente politica e le eventuali
    deroghe motivate.

## 6 Violazione della Politica

Qualsiasi azione non conforme alla politica aziendale di Vectorlab sarà
considerata una violazione della sicurezza e come tale potrà tradursi
nella sospensione dell'accesso alle aree e alle risorse informatiche, rete
e documenti. L'uso improprio degli strumenti aziendali costituisce una
grave violazione del dovere di correttezza e può comportare l'adozione di
provvedimenti disciplinari in conformità alla normativa vigente.

## 7 Riesame

La revisione della presente politica è effettuata dalla Direzione almeno
una volta all'anno e prima del Riesame della Direzione, e in risposta a
cambiamenti significativi del contesto normativo o tecnologico. Il
riesame è condotto per valutare l'efficienza e l'efficacia del sistema e
per assicurare che siano implementate le azioni necessarie a consentire il
miglioramento continuo.
