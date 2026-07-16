# PO32 - Gestione delle Configurazioni

**Politica di Gestione delle Configurazioni**

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

La presente politica definisce i principi generali adottati da
VECTORLAB per la gestione delle configurazioni di sicurezza dei
sistemi, dei dispositivi, delle applicazioni e dei servizi di rete
utilizzati dall'Azienda, al fine di:

- assicurare che tutti gli asset siano configurati secondo impostazioni
  di sicurezza note, documentate e riproducibili (baseline di
  configurazione);

- ridurre la superficie di attacco disabilitando funzionalità, servizi
  e account non necessari;

- garantire che le configurazioni di sicurezza siano mantenute nel
  tempo, monitorate e sottoposte a verifica periodica.

Le modalità operative di dettaglio con cui questa politica viene
attuata sono descritte in "*PR32.1 - Gestione delle Configurazioni*".

### 1.2 Campo di applicazione

La presente politica si applica a tutti i sistemi IT, dispositivi
fisici (PC aziendali, apparati di rete), applicazioni e servizi cloud
di proprietà o in uso a VECTORLAB, censiti nel CMDB secondo quanto
descritto in "*PR14.1 - Gestione Asset*".

### 1.3 Riferimenti e Allegati

> MDPR11.1.C - Piano di Audit Tecnici

> MDPR32.1.A - Template di Configurazione di Base FIREWALL

> MDPR32.1.A - Template di Configurazione di Base PC

> MDPR32.1.A - Template di Configurazione di Base ROUTER

> MDPR32.1.A - Template di Configurazione di Base SWITCH

> PO17 - Crittografia

> PR03.1 - IT

> PR14.1 - Gestione Asset

> PR19.1 - Gestione del Cambiamento

> PR22.1 - Gestione delle Patch

> PR32.1 - Gestione delle Configurazioni

> REG01 - Regolamento sull'utilizzo degli strumenti informatici
> aziendali

> SOA - Statement of Applicability - Dichiarazione di Applicabilità.

### 1.4 Definizioni, Acronimi, Abbreviazioni

> Baseline di configurazione - insieme documentato dei parametri di
> configurazione di sicurezza minimi richiesti per una categoria di
> asset

> CI - Configuration Item

> CMDB - Configuration Management System Data Base

> Hardening - insieme di attività volte a ridurre la superficie di
> attacco di un sistema, rimuovendo o disabilitando funzionalità non
> necessarie

> RSGI - Responsabile del Sistema di Gestione Integrato

> SGI - Sistema di Gestione Integrato.

## 2 Responsabilità

RSGI ha la responsabilità di redigere, mantenere aggiornata e
comunicare la presente politica.

L'IT ha la responsabilità di:

- definire, in accordo con CISO (ruolo ricoperto dall'Amministratore
  Unico), le configurazioni di base (baseline) per ciascuna categoria di
  asset;

- applicare le configurazioni di base al momento della messa in
  servizio di un nuovo asset (cfr. "*PR14.1 - Gestione Asset*", par.
  2.3);

- mantenere e verificare periodicamente la conformità delle
  configurazioni in essere rispetto alla baseline definita.

## 3 Principi Generali

VECTORLAB adotta configurazioni sicure per sistemi, dispositivi e
applicazioni utilizzate, basandosi sulle impostazioni di sicurezza
raccomandate dai fornitori. Sono disabilitate funzionalità non
necessarie.

In particolare, i seguenti principi generali guidano la gestione delle
configurazioni:

- **configurazione minima necessaria**: ogni sistema deve essere
  configurato attivando solo i servizi, le porte e le funzionalità
  strettamente necessarie all'operatività;

- **impostazioni raccomandate dal fornitore**: le configurazioni di
  base fanno riferimento, per quanto possibile, alle linee guida di
  hardening pubblicate dai produttori/fornitori dei sistemi, dispositivi
  e servizi in uso;

- **credenziali non di default**: le credenziali di accesso
  predefinite (default) di qualsiasi dispositivo o applicazione devono
  essere sostituite prima della messa in servizio;

- **documentazione e riproducibilità**: le configurazioni di base sono
  documentate tramite appositi template (cfr. "*MDPR32.1.A - Template di
  Configurazione di Base*", declinati per categoria di asset), in modo
  da rendere la configurazione riproducibile e verificabile;

- **coerenza con la classificazione degli asset**: il livello di
  hardening richiesto è proporzionato alla criticità dell'asset, così
  come definita nell'Asset Inventory (cfr. "*PO15 - Politica
  Classificazione Informazioni*");

- **tracciabilità delle modifiche**: ogni modifica alle configurazioni
  di sicurezza di un asset è soggetta al processo di gestione del
  cambiamento (cfr. "*PR19.1 - Gestione del Cambiamento*").

## 4 Configurazioni di Base per Categoria di Asset

VECTORLAB definisce configurazioni di base (baseline) per le seguenti
categorie di asset, per le quali sono predisposti appositi moduli
template:

- **PC aziendali** (cfr. "*MDPR32.1.A - Template di Configurazione di
  Base PC*");

- **Router/apparato di connessione perimetrale** (cfr. "*MDPR32.1.A -
  Template di Configurazione di Base ROUTER*");

- **Firewall** (cfr. "*MDPR32.1.A - Template di Configurazione di Base
  FIREWALL*");

- **Switch**, ove presenti (cfr. "*MDPR32.1.A - Template di
  Configurazione di Base SWITCH*").

<span style="color:#B3392A">[DA CONFERMARE: allo stato attuale
l'infrastruttura di rete di VECTORLAB risulta composta da un unico
router con firewall integrato e funzionalità WPA2 per la rete Wi-Fi
aziendale; non risultano presenti switch gestiti né altri apparati di
rete complessi. Il template SWITCH viene comunque predisposto per
completezza documentale rispetto a quanto indicato nella SOA, ma la sua
applicabilità concreta è da confermare]</span>.

Per i sistemi applicativi e i servizi erogati in cloud (AWS, server
Aruba in Infrastructure-as-Code, Google Workspace), la configurazione
sicura è gestita secondo le modalità descritte in "*PR32.1 - Gestione
delle Configurazioni*" e, per la componente infrastrutturale versionata
come codice, tramite gli stessi meccanismi di controllo delle modifiche
adottati per il codice sorgente applicativo.

## 5 Gestione delle Modifiche alle Configurazioni

Ogni modifica ad una configurazione di sicurezza già in essere
(baseline) deve essere valutata, testata ove possibile e approvata
prima dell'implementazione, in coerenza con quanto previsto da "*PR19.1
- Gestione del Cambiamento*". Le modifiche vengono tracciate e, se
rilevanti, riportate nel CMDB a cura dell'IT (cfr. "*PR14.1 - Gestione
Asset*").

## 6 Verifica Periodica

La conformità delle configurazioni in essere rispetto alla baseline
definita è verificata periodicamente dall'IT, anche nell'ambito delle
attività di audit tecnico pianificate in "*MDPR11.1.C - Piano di Audit
Tecnici*". Eventuali scostamenti rilevati sono corretti o, se
giustificati da esigenze operative, formalmente accettati come
eccezione documentata.

## 7 Violazione della Politica

Qualsiasi azione non conforme alla presente politica sarà considerata
una violazione della sicurezza e come tale potrà tradursi nella
sospensione dell'accesso alle risorse informatiche, oltre a eventuali
provvedimenti disciplinari in conformità alla normativa vigente.

## 8 Riesame

La revisione della presente politica è effettuata da RSGI almeno una
volta all'anno e prima del riesame della Direzione, e in risposta a
cambiamenti significativi dell'infrastruttura tecnologica o
organizzativa di VECTORLAB.
