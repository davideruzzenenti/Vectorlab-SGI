# PO21 - Gestione dei Backup e Restore

**Politica Gestione dei Backup e Restore**

> Revisioni

|          |            |                 |             |               |
| -------- | ---------- | --------------- | ----------- | ------------- |
| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | IT          | CTO           |
|          |            |                 |             |               |
|          |            |                 |             |               |
|          |            |                 |             |               |

> [Revisioni 1](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.gjdgxs)

[1
Introduzione](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.1fob9te)

[1.1
Scopo](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.3znysh7)

[1.2 Campo di
applicazione](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.tyjcwt)

[1.3 Riferimenti e
Allegati](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.1t3h5sf)

[1.4 Definizioni, Acronimi,
Abbreviazioni](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.2s8eyo1)

[1.5
Responsabilità](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.3rdcrjn)

[1.6 Violazione della
Politica 3](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.lnxbz9)

[1.7
Riesame](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.1ksv4uv)

[2 Gestione dei
backup](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.2jxsxqh)

[2.1](https://docs.google.com/document/d/11FXEiVS8h5rjKEWL2k4Nm0YdpfdoAMBG/edit#heading=h.z337ya)

> 222233334Backup 42.2Restore 5

1.  # Introduzione

    1.  # Scopo

Il presente documento definisce la politica di gestione del processo di
Backup e Restore in Vectorlab.

# Campo di applicazione

Il presente documento definisce le attività che afferiscono alla
salvaguardia di tutte le categorie di dati e delle risorse di sistemi,
reti e applicazioni dell’organizzazione. Essa è pertanto rivolta al
personale che nell’ambito delle proprie attività deve individuare,
pianificare e garantire la conservazione e la reperibilità dei dati.

#  Riferimenti e Allegati

> MDPR21.1.A - Piano di Restore

> PR21.1 - Gestione Backup e Restore.

# Definizioni, Acronimi, Abbreviazioni

> CEO - Chief Executive Officer

> CISO - Chief Information Security Officer

> IT - Information Technology

# Responsabilità

IT ha la responsabilità di redigere, mantenere aggiornata e comunicare
la presente politica.

Il personale, a qualsiasi livello, e i collaboratori esterni devono
attenersi alle procedure definite dall’organizzazione per assicurarsi
che la presente Politica sia correttamente applicata.

I responsabili dell’attuazione della presente politica sono:

  - CISO

  - CTO

  - Responsabile IT

  - Staff IT.

    1.  # Violazione della Politica

Qualsiasi azione non conforme alla politica aziendale di Vectorlab sarà
considerata una violazione della sicurezza e come tale potrà tradursi
nella sospensione dell'accesso alle aree e alle risorse informatiche,
rete e documenti. L'uso improprio degli strumenti aziendali costituisce
una grave violazione del dovere di correttezza e può comportare
l'adozione di provvedimenti disciplinari in conformità alla normativa
vigente.

Effettuare i backup di dati/applicazioni/sistemi scaturisce dalla
eventualità di necessità di un possibile ripristino. Per questo motivo
le diverse modalità identificate sono volte, una volta definito quali
componenti sono a rischio, a mitigare efficacemente tale rischio.

#  Riesame

La revisione di tale politica è effettuata da CTO almeno una volta
all'anno e prima del Riesame della direzione. Il riesame è condotto per
valutare l'efficienza e l'efficacia del sistema e per assicurare che
siano implementate le azioni necessarie per consentire il miglioramento
continuo secondo i requisiti definiti dai sistemi di gestione e in tutte
le situazioni per le quali è richiesta una modifica dell'attività
aziendale che possa anche avere impatto sulla sicurezza delle
informazioni o sull'operatività.

# Gestione dei Backup

Ai fini di garantire la disponibilità del dato, nel salvaguardarne la
riservatezza e nel preservarne l’integrità, è necessario definire e
attuare una strategia di sicurezza che includa criteri e modalità per il
salvataggio, l’accesso ai dati di backup, la conservazione e il
ripristino del dato e della funzionalità del software (vanno individuate
le modalità e gli strumenti necessari ad assicurare la disponibilità del
dato e del software sia applicativo che di sistema).

Backup e recovery sono componenti essenziali della pianificazione della
continuità operativa.

# Backup

La politica di backup definisce gli elementi indispensabili per
garantire che le informazioni dell'organizzazione e dei propri clienti
siano protette e che i sistemi informatici e i servizi siano disponibili
secondo quanto previsto e concordato. Il processo di backup ha come
obiettivo di produrre registrazioni accurate e complete delle copie di
backup e delle procedure di ripristino documentate.

In particolare, l’organizzazione ha definito:

  - per quali dati, informazioni, software e sistemi informatici deve
    essere eseguito il backup in modo da riflettere i requisiti
    aziendali dell'organizzazione e dei suoi clienti (RPO – Recovery
    Point Objective), i requisiti di sicurezza delle informazioni
    coinvolte e la criticità delle informazioni oggetto di backup;

  - su quali tipologie di supporti e dove archiviare i backup scegliendo
    un luogo remoto sicuro e protetto, a una distanza sufficiente per
    evitare eventuali danni causati da un disastro nel sito principale.
    È inoltre necessario procurarsi e gestire adeguatamente i supporti
    necessari da utilizzare per i backup, in modo che non vi sia carenza
    di approvvigionamento e che non si verifichino problemi di utilizzo;

  - il tipo di backup (completo, continuo, incrementale) e punti di
    controllo da utilizzare;

  - quante copie di dati devono essere conservate - ciò può variare in
    base al tipo di dati di cui si esegue il backup;

  - le modalità di trasferimento delle copie (ad es. trasferimento di
    file tramite la rete);

  - le modalità di protezione dei backup sia attraverso la gestione
    degli accessi limitati alle copie dei dati sia attraverso uso della
    crittografia in relazione ai rischi identificati sulle informazioni
    oggetto di backup;

  - il tempo di conservazione (retention time);

  - verifica dell’adeguatezza dei backup a seguito di cambiamenti ai
    sistemi informatici;

  - verifiche di correttezza dei backup e periodiche prove di ripristino
    secondo quanto programmato nel piano “*MDPR21.1.A.1 - Piano di
    Restore*”. Anche se non vengono generati codici di errore,
    potrebbero esserci diversi motivi per cui il backup non può essere
    ripristinato o il suo ripristino non sia facile. Una buona strategia
    di backup e procedure operative minimizzeranno il rischio che ciò
    accada. Se vengono rilevati errori di backup, è necessario avviare
    azioni di analisi delle cause e ri-effettuare conseguentemente il
    backup.

L’elenco dei backup previsti per ogni sistema o gruppo di sistemi con le
informazioni relative al tipo di backup, la frequenza, il supporto, la
gestione degli accessi, la retention time e modalità di verifica è
riportato nella “*PR21.1 - Gestione Backup e Restore*” assieme ad
indicazioni operative.

Se i backup vengono automatizzati è necessario considerare le
funzionalità di monitoraggio degli eventi in modo che eventuali guasti
possano essere rilevati in anticipo e risolti prima che possano causare
problemi. In tali casi, le operazioni IT hanno un ruolo da svolgere
nella definizione di avvisi e percorsi di escalation.

# Restore

Un restore può essere effettuato a fronte di diversi eventi che vanno da
operazioni di ricostruzione in seguito a danneggiamento dei dati,
applicazione di piani di continuità fino a una richiesta di servizio di
utente opportunamente registrata nel sistema di ticketing aziendale.

Potrebbe essere necessario un ripristino in caso di:

  - dati corrotti;

  - dati persi;

  - eventi che compromettano la continuità di servizi;

  - richiesta dati storici per le indagini forensi.

I passi da compiere includono:

  - localizzazione dei dati / supporti appropriati;

  - trasferimento nella posizione di ripristino fisica;

  - accordo sul punto di ripristino e posizione specifica in cui
    posizionare i dati recuperati (disco, directory, cartella ecc.);

  - ripristino effettivo del file / dei dati (copia ed eventuale
    rollback / roll-forward necessari per arrivare al punto di
    ripristino concordato;

  - verifica esito del ripristino - con ulteriori azioni di ripristino
    se necessario fino al raggiungimento del successo;

  - approvazione utente / cliente.