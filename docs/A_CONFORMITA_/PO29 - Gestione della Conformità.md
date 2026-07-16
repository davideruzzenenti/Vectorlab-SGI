# PO29 - Gestione della Conformità

**Politica di Gestione della Conformità**

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

Il presente documento definisce la politica di Vectorlab per l'identificazione, la
gestione e il monitoraggio dei requisiti legali, statutari, regolamentari,
normativi e contrattuali applicabili alle proprie attività, in particolare
per quanto riguarda la sicurezza delle informazioni (cfr. controllo SOA 5.31
- Requisiti legali, statutari, regolamentari e contrattuali).

La politica costituisce inoltre il riferimento generale per gli aspetti di
conformità trattati anche dai controlli SOA 5.32 (Diritti di proprietà
intellettuale), 5.33 (Protezione delle registrazioni), 5.34 (Privacy e
protezione dei dati personali, per la quale sono in essere politiche
specifiche, cfr. §1.2), 5.35 (Riesame indipendente della sicurezza delle
informazioni) e 5.36 (Conformità con le politiche, le regole e le norme di
sicurezza delle informazioni).

La politica si applica a tutte le attività svolte da Vectorlab, a tutto il
personale e ai collaboratori esterni, e viene declinata in requisiti
specifici a seconda dell'ambito (privacy, sicurezza delle informazioni,
proprietà intellettuale, obblighi contrattuali con clienti e fornitori).

### 1.2 Riferimenti e Allegati

> PO30 - Privacy by design e by default

> PO31 - Misure di sicurezza protezione dati personali

> MDPO29.D - Elenco AdS

> MDPR08.1.A - Elenco Informazioni documentate

> PR11.1 - Audit Interno

> PR33.1 - Processo di Analisi del Rischio e Trattamento

> REG01 - Regolamento sull'utilizzo degli strumenti aziendali

> asset_inventory_vectorlab (categoria "Valore": A0045 - D.lgs. 196/03 e
> GDPR; A0046 - D.lgs. 81/08; A0047 - Norme volontarie ISO)

> REGOLAMENTO (UE) 2016/679 (GDPR)

> D.Lgs. 9 aprile 2008, n. 81 (sicurezza sul lavoro)

> ISO/IEC 27001:2022, ISO 9001:2015

### 1.3 Definizioni, Acronimi, Abbreviazioni

> GDPR – General Data Protection Regulation

> RSGI – Responsabile del Sistema di Gestione Integrato

> SGI – Sistema di Gestione Integrato

> SOA – Statement of Applicability / Dichiarazione di Applicabilità.

## 2 Gestione della Conformità

### 2.1 Approccio generale

Vectorlab, in quanto piccola software house che eroga servizi di sviluppo
software e consulenza ICT, opera in un contesto normativo composto
principalmente da: obblighi di legge di carattere generale (fiscali,
societari, lavoristici, sulla protezione dei dati personali), obblighi
contrattuali verso clienti e fornitori, e adesione volontaria a standard
e best practice di settore (norme ISO, linee guida OWASP).

L'identificazione e il presidio di tali requisiti sono organizzati secondo
tre categorie, coerentemente con quanto già mappato tra gli asset di
"Valore" dell'Asset Inventory aziendale (cfr. *"asset_inventory_vectorlab"*,
categoria VALE/VANO):

  - requisiti legali e regolamentari cogenti;

  - requisiti contrattuali;

  - requisiti normativi volontari / best practice di settore.

### 2.2 Requisiti legali e regolamentari cogenti

Tra i principali requisiti legali cogenti applicabili a Vectorlab si
segnalano:

  - la normativa in materia di protezione dei dati personali (Regolamento
    (UE) 2016/679 - GDPR e D.Lgs. 196/2003 e ss.mm.ii.), gestita in modo
    specifico attraverso le politiche e procedure dedicate (cfr. *"PO30 -
    Privacy by design e by default"* e *"PO31 - Misure di sicurezza
    protezione dati personali"* e relative procedure collegate);

  - la normativa in materia di salute e sicurezza sul lavoro (D.Lgs.
    81/2008), <span style="color:#B3392A">[DA CONFERMARE: riferimento al
    documento/i specifico/i di gestione della sicurezza sul lavoro e al
    ruolo di RSPP, non ancora mappato in un documento dedicato del
    presente SGI]</span>;

  - la normativa a tutela del diritto d'autore sul software (L. 633/1941 e
    ss.mm.ii.) e più in generale sulla proprietà intellettuale, rilevante
    per il codice sorgente sviluppato per conto dei clienti (cfr. asset
    A0039 - Codici sorgenti di proprietà dei clienti);

  - <span style="color:#B3392A">[DA CONFERMARE: eventuali ulteriori
    normative settoriali applicabili, ad esempio in tema di responsabilità
    amministrativa degli enti (D.Lgs. 231/2001), la cui applicabilità a
    Vectorlab non risulta ad oggi formalmente valutata]</span>.

Per ciascun requisito identificato, Vectorlab individua il documento o i
documenti del SGI che ne garantiscono il presidio, mantenendo tale mappatura
aggiornata nel documento *"MDPR08.1.A - Elenco Informazioni documentate"*.

### 2.3 Requisiti contrattuali

Vectorlab assume, nell'ambito dei contratti stipulati con clienti e
fornitori, obblighi specifici in materia di riservatezza, protezione dei
dati, livelli di servizio (SLA) e proprietà intellettuale, tra cui, a
titolo esemplificativo:

  - accordi di riservatezza (NDA) con clienti, fornitori e collaboratori;

  - clausole contrattuali relative alla proprietà del codice sorgente e
    del know-how sviluppato nell'ambito dei progetti;

  - condizioni contrattuali e SLA dei fornitori di servizi cloud e
    infrastrutturali utilizzati (AWS, Aruba, Google Workspace, GitHub)
    <span style="color:#B3392A">[DA CONFERMARE: elenco puntuale degli SLA
    e delle clausole contrattuali rilevanti per ciascun fornitore
    critico]</span>;

  - eventuali requisiti di conformità richiesti contrattualmente dai
    singoli clienti (es. requisiti di sicurezza specifici, certificazioni
    richieste).

La verifica del rispetto di tali obblighi è in capo alla Direzione e ai
responsabili dei singoli progetti/rapporti contrattuali, con il supporto,
per gli aspetti privacy, del Referente Privacy.

### 2.4 Requisiti normativi volontari e best practice

Vectorlab ha scelto di adottare, su base volontaria, i seguenti riferimenti
normativi e best practice, quale ulteriore garanzia di qualità e sicurezza
dei propri servizi (cfr. asset A0047 - Norme volontarie ISO):

  - ISO 9001:2015 - Sistemi di gestione per la qualità;

  - ISO/IEC 27001:2022 - Sistemi di gestione della sicurezza delle
    informazioni;

  - OWASP - Best Practices per lo sviluppo sicuro del software (già
    richiamate in *"PO31 - Misure di sicurezza protezione dati
    personali"*).

### 2.5 Registro degli obblighi di conformità

La mappatura tra i requisiti identificati e i documenti del SGI che ne
garantiscono il presidio è mantenuta all'interno del documento *"MDPR08.1.A
- Elenco Informazioni documentate"*. Per gli aspetti relativi agli
Amministratori di Sistema, si fa inoltre riferimento al registro *"MDPO29.D
- Elenco AdS"*.

### 2.6 Verifica della conformità

La verifica del rispetto dei requisiti legali, contrattuali e normativi
individuati è svolta nell'ambito del programma di audit interno definito in
*"PR11.1 - Audit Interno"*, con cadenza almeno annuale e in occasione di
modifiche normative o organizzative significative
<span style="color:#B3392A">[DA CONFERMARE: periodicità puntuale delle
verifiche di conformità legale, non ancora formalizzata in un piano
dedicato]</span>.

Le eventuali non conformità riscontrate sono gestite secondo il processo
generale di gestione delle non conformità e delle azioni di miglioramento
del SGI.

### 2.7 Ruoli e responsabilità

  - l'Amministratore Unico, quale Titolare e responsabile ultimo della
    conformità di Vectorlab, approva la presente politica e le eventuali
    azioni correttive rilevanti;

  - il RSGI presidia il mantenimento aggiornato dell'elenco dei requisiti
    applicabili e ne verifica il rispetto in sede di riesame e di audit;

  - il Referente Privacy presidia i requisiti specifici in materia di
    protezione dei dati personali;

  - tutto il personale è tenuto a segnalare eventuali situazioni di
    potenziale non conformità rilevate nello svolgimento delle proprie
    attività.

### 2.8 Violazione della Politica

Qualsiasi azione non conforme alla politica aziendale di Vectorlab sarà
considerata una violazione della sicurezza e come tale potrà tradursi
nella sospensione dell'accesso alle aree e alle risorse informatiche, rete
e documenti. L'uso improprio degli strumenti aziendali costituisce una
grave violazione del dovere di correttezza e può comportare l'adozione di
provvedimenti disciplinari in conformità alla normativa vigente.

I casi gravi saranno segnalati all'autorità competente e potranno essere
oggetto di provvedimenti disciplinari o legali.

### 2.9 Riesame

La revisione della presente politica è effettuata dalla Direzione almeno
una volta all'anno e prima del Riesame della Direzione, nonché in risposta
a cambiamenti significativi del contesto normativo, contrattuale o
organizzativo. Il riesame è condotto per valutare l'efficienza e
l'efficacia del sistema e per assicurare che siano implementate le azioni
necessarie a consentire il miglioramento continuo secondo i requisiti
definiti dai sistemi di gestione.
