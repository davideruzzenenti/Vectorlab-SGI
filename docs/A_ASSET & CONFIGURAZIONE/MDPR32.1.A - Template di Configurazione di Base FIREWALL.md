# MDPR32.1.A - Template di Configurazione di Base FIREWALL

**Modulo Template - Configurazione di Base FIREWALL**

<div style="border-left:4px solid #2A5C8A;background:#EAF1F7;padding:.75rem 1rem;margin:1rem 0">
<strong>DOCUMENTO IN BOZZA — generato il 16/07/2026</strong> per colmare una lacuna rilevata durante la revisione della documentazione (citato nella SOA ma non ancora creato). Contenuto basato su pratiche reali già note da altri documenti del SGI; le parti evidenziate in rosso sono da confermare prima dell'approvazione formale.
</div>

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.1      | 16/07/2026 | Prima bozza — documento mancante generato per colmare una lacuna rilevata nella SOA | IA          | Da approvare  |
|          |            |                 |             |               |

## Istruzioni per l'uso del modulo

Il presente modulo è un **template vuoto**, da compilare a cura dell'IT
in occasione della messa in servizio, della sostituzione o della
revisione periodica di un apparato con funzionalità firewall (dedicato
o integrato nel router aziendale), secondo quanto previsto in "*PR32.1
- Gestione delle Configurazioni*".

<span style="color:#B3392A">[DA CONFERMARE: allo stato attuale
VECTORLAB utilizza le funzionalità firewall integrate nel router
aziendale; il presente template si applica quindi alla componente
firewall di tale apparato, salvo diversa indicazione risultante da
future modifiche infrastrutturali]</span>.

**Riferimento asset / CI (CMDB):** _da compilare_

**Data compilazione:** _da compilare_

**Compilato da:** _da compilare_

## Checklist parametri di configurazione

| **Categoria** | **Parametro di configurazione** | **Valore configurato** | **Verificato (Sì/No)** | **Note** |
| -------------- | -------------------------------------------------------- | ----------------------- | ----------------------- | -------- |
| Accesso amministrativo | Credenziali di default sostituite | | | |
| Accesso amministrativo | Accesso amministrativo limitato a rete interna / IP autorizzati | | | |
| Accesso amministrativo | Autenticazione a più fattori abilitata (ove supportata) | | | |
| Firmware | Versione firmware in uso | | | |
| Firmware | Aggiornamenti automatici / periodici abilitati | | | |
| Regole di filtraggio | Politica di default in ingresso (deny by default) | | | |
| Regole di filtraggio | Regole di inoltro porte (port forwarding) documentate | | | |
| Regole di filtraggio | Regole obsolete/non utilizzate rimosse | | | |
| Content / Web filtering | Content filtering verso categorie di siti non pertinenti/malevoli attivo | | | |
| Content / Web filtering | Elenco eccezioni (whitelist) aggiornato | | | |
| VPN | Accesso VPN configurato e limitato agli utenti autorizzati | | | |
| VPN | Protocollo di cifratura VPN in uso | | | |
| Logging | Logging degli eventi di sicurezza abilitato | | | |
| Logging | Conservazione dei log conforme a "*PR20.1 - Capacità e Monitoraggio Tecnico*" | | | |
| Segmentazione | Segregazione rete aziendale / rete Guest (ove presente) | | | |
| Servizi non necessari | Servizi/protocolli di gestione non necessari disabilitati (es. Telnet, UPnP) | | | |

## Note e osservazioni

_Spazio per eventuali osservazioni, eccezioni concordate o motivazioni
di scostamento dalla configurazione di base, da riportare secondo
quanto previsto in "*PR32.1 - Gestione delle Configurazioni*", par.
2.6._
