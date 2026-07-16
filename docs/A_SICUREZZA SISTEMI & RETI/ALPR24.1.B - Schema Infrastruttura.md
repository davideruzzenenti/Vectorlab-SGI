# ALPR24.1.B - Schema Infrastruttura

**Allegato - Schema Infrastruttura**

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

Il presente allegato descrive, a livello logico e in forma testuale,
l'infrastruttura cloud utilizzata da VECTORLAB per l'erogazione dei
propri servizi e per la gestione delle attività interne. Come indicato
in "*PR18.1 - Gestione Sicurezza Fisica e Ambientale*", VECTORLAB non
dispone di infrastrutture fisiche proprie (CED, sala server, rack): i
sistemi sono interamente ospitati su piattaforme cloud di terze parti.
Non essendo disponibile uno strumento di disegno tecnico validato per
un diagramma grafico, l'infrastruttura viene qui rappresentata come
elenco di componenti e collegamenti, coerentemente con quanto già
descritto in "*PR20.1 - Capacità e Monitoraggio Tecnico*" e "*PR21.1 -
Gestione dei Backup e Restore*".

### 1.2 Riferimenti e Allegati

> PR24.1 - Gestione delle Reti

> ALPR24.1.A - Schema di Rete

> PR18.1 - Gestione Sicurezza Fisica e Ambientale

> PR20.1 - Capacità e Monitoraggio Tecnico

> PR21.1 - Gestione dei Backup e Restore.

### 1.3 Definizioni, Acronimi, Abbreviazioni

> ECR - Elastic Container Registry: Docker registry privato su AWS

> ECS - Elastic Container Service: gestore di container su AWS

> EC2 - Elastic Compute Cloud: servizio di elaborazione virtuale AWS

> EFS - Elastic File System: file system di rete AWS

> IaC - Infrastructure-as-Code

> S3 - Simple Storage Service: servizio di storage a oggetti AWS.

## 2 Componenti dell'infrastruttura

L'infrastruttura tecnologica di VECTORLAB si articola su tre principali
piattaforme cloud, ciascuna dedicata ad ambiti differenti:

### 2.1 Piattaforma AWS (Amazon Web Services)

Ospita i servizi applicativi erogati ai clienti e i dati associati:

  - **EC2** - istanze virtuali con ruolo di "Bastion host", utilizzate
    per montare e accedere ai volumi EFS impiegati dai servizi
    containerizzati;

  - **ECS** - contiene i container Docker in cui sono eseguiti i vari
    servizi back-end applicativi erogati dall'Azienda;

  - **ECR** - registry privato dove sono conservate le immagini dei
    container utilizzati su ECS;

  - **S3** - storage a oggetti utilizzato per la conservazione di file
    di varia natura (inclusi file di sistema, configurazione e
    sicurezza dell'infrastruttura, backup dei database);

  - **EFS** - file system collegato alle istanze EC2, utilizzato dai
    servizi containerizzati;

  - **CloudWatch** - raccoglie log e alert dei container ECS e fornisce
    dashboard per il monitoraggio in tempo reale dell'utilizzo delle
    risorse; notifica automaticamente IT in caso di indisponibilità dei
    servizi;

  - **CloudFront** - espone le nuove versioni dei frontend dei progetti
    verso l'esterno;

  - **Parameter Store** - conserva in modo cifrato i parametri di
    configurazione e i segreti applicativi (es. stringhe di
    connessione, password di servizio).

<span style="color:#B3392A">[DA CONFERMARE: region/e AWS utilizzate, nomi e struttura delle VPC/subnet, elenco puntuale delle istanze EC2/servizi ECS attivi e relativi identificativi — dettagli tecnici non documentati altrove nel SGI]</span>

### 2.2 Server Aruba (Infrastructure-as-Code)

Infrastruttura dedicata agli ambienti di test e agli asset
infrastrutturali specifici di VECTORLAB, gestita in modalità
Infrastructure-as-Code: container e immagini sono definiti in codice
versionato su GitHub, senza una piattaforma di virtualizzazione
on-premise dedicata. Ospita inoltre Bitwarden, il gestore delle
credenziali/segreti aziendali.

<span style="color:#B3392A">[DA CONFERMARE: data center Aruba/regione di erogazione, caratteristiche tecniche del server (tipologia, dimensionamento) — dettagli non documentati]</span>

### 2.3 Google Workspace

Piattaforma SaaS utilizzata per posta elettronica, collaborazione
documentale (Google Drive) e strumenti d'ufficio; gestita interamente
dal fornitore (Google), inclusa la sicurezza di rete sottostante.

### 2.4 GitHub

Piattaforma di versionamento che ospita il codice sorgente sviluppato
da VECTORLAB e la documentazione del SGI; costituisce inoltre il
riferimento per la configurazione IaC del server Aruba e per le
immagini dei container.

## 3 Collegamenti tra i componenti

  - **Sviluppo → GitHub**: il codice sorgente e le configurazioni IaC
    sono versionati su GitHub;

  - **GitHub → ECR/ECS**: le immagini dei container costruite a partire
    dal codice versionato vengono pubblicate su ECR e distribuite come
    servizi su ECS;

  - **GitHub → Server Aruba**: la configurazione del server Aruba viene
    applicata (redeploy) a partire dal codice IaC versionato;

  - **ECS ↔ EFS**: i container montano, tramite le istanze EC2 con
    ruolo di bastion host, i volumi EFS per l'accesso ai file
    applicativi;

  - **ECS/EC2 → S3**: i servizi applicativi e gli script schedulati
    salvano su S3 i backup dei database e altri file di sistema;

  - **ECS → CloudWatch**: i container inviano log e metriche a
    CloudWatch, che genera alert automatici verso IT in caso di
    anomalie;

  - **CloudFront → Utenti finali/Internet**: espone pubblicamente le
    versioni più recenti dei frontend applicativi;

  - **Parameter Store ↔ ECS**: i servizi containerizzati recuperano in
    modo sicuro segreti e parametri di configurazione al bisogno;

  - **Postazioni di lavoro / rete di ufficio → tutte le piattaforme**:
    l'accesso alle console di gestione (AWS, Aruba, Google Workspace,
    GitHub) avviene via Internet in HTTPS/TLS dalla rete di ufficio o da
    reti private del personale in smart working (cfr. "*ALPR24.1.A -
    Schema di Rete*"), con autenticazione secondo quanto descritto in
    "*PO16 - Gestione degli Accessi*".

## 4 Rappresentazione sintetica

```
                         Internet / Utenti finali
                                   |
                             [ CloudFront ]
                                   |
   +-------------------------- AWS -----------------------------+
   |                                                             |
   |   [ EC2 - bastion host ] ---- monta ----> [ EFS ]           |
   |            |                                                |
   |   [ ECS - container backend ] ---- log/alert ---> [ CloudWatch ]
   |            |                                                |
   |            +---- backup/file ----> [ S3 ]                   |
   |            |                                                |
   |            +---- config/secrets ----> [ Parameter Store ]   |
   |                                                             |
   |   [ ECR - registry immagini container ]                     |
   +-------------------------------------------------------------+
                                   ^
                                   | deploy/redeploy da codice IaC
                                   |
                          [ GitHub - codice e IaC ]
                                   |
                                   v
              [ Server Aruba - IaC: test, Bitwarden (segreti) ]

   [ Google Workspace - email, Drive, collaborazione ] (SaaS, gestione
     fornitore indipendente dagli altri componenti)

   Accesso alle console/servizi: postazioni di lavoro (ufficio o smart
   working) via Internet, HTTPS/TLS, con autenticazione
   (cfr. ALPR24.1.A - Schema di Rete; PO16 - Gestione degli Accessi)
```

La sicurezza di rete relativa a ciascuna delle piattaforme sopra
descritte (segregazione, filtraggio, protezione perimetrale) è di
competenza dei rispettivi fornitori cloud, come indicato in "*PR24.1 -
Gestione delle Reti*".
