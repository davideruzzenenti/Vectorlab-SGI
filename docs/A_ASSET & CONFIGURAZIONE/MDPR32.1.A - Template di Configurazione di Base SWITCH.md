# MDPR32.1.A - Template di Configurazione di Base SWITCH

**Modulo Template - Configurazione di Base SWITCH**

<div style="border-left:4px solid #2A5C8A;background:#EAF1F7;padding:.75rem 1rem;margin:1rem 0">
<strong>DOCUMENTO IN BOZZA — generato il 16/07/2026</strong> per colmare una lacuna rilevata durante la revisione della documentazione (citato nella SOA ma non ancora creato). Contenuto basato su pratiche reali già note da altri documenti del SGI; le parti evidenziate in rosso sono da confermare prima dell'approvazione formale.
</div>

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.1      | 16/07/2026 | Prima bozza — documento mancante generato per colmare una lacuna rilevata nella SOA | IA          | Da approvare  |
|          |            |                 |             |               |

## Istruzioni per l'uso del modulo

Il presente modulo è un **template vuoto**, predisposto per la
configurazione di base di apparati switch di rete, in coerenza con
quanto elencato in "*PR32.1 - Gestione delle Configurazioni*" e con i
riferimenti già presenti nella SOA per il controllo 8.9 (Gestione delle
configurazioni sicure e dell'hardening).

<span style="color:#B3392A">[DA CONFERMARE - APPLICABILITA': in base
alle informazioni ad oggi disponibili, l'infrastruttura di rete di
VECTORLAB è costituita da un'unica sede a Genova con un router dotato di
firewall integrato e rete Wi-Fi protetta con WPA2, senza switch gestiti
o apparati di rete di livello 2 dedicati. Questo template potrebbe
quindi non essere applicabile nel contesto attuale e viene mantenuto
come modulo vuoto disponibile per eventuali future evoluzioni
dell'infrastruttura di rete (es. introduzione di switch gestiti in
sede). Si raccomanda di confermare l'applicabilità o l'esclusione di
questo modulo in sede di prima revisione del documento]</span>.

**Riferimento asset / CI (CMDB):** _da compilare_

**Data compilazione:** _da compilare_

**Compilato da:** _da compilare_

## Checklist parametri di configurazione

| **Categoria** | **Parametro di configurazione** | **Valore configurato** | **Verificato (Sì/No)** | **Note** |
| -------------- | -------------------------------------------------------- | ----------------------- | ----------------------- | -------- |
| Accesso amministrativo | Credenziali di default sostituite | | | |
| Accesso amministrativo | Interfaccia di gestione accessibile solo da rete/host autorizzati | | | |
| Firmware | Versione firmware in uso | | | |
| Firmware | Aggiornamenti di sicurezza applicati | | | |
| Porte non utilizzate | Porte fisiche non utilizzate disabilitate | | | |
| Segmentazione | VLAN configurate secondo segregazione prevista | | | |
| Servizi non necessari | Protocolli di gestione non necessari disabilitati (es. Telnet, servizi legacy) | | | |
| Logging | Logging degli eventi di configurazione/accesso abilitato | | | |

## Note e osservazioni

_Spazio per eventuali osservazioni, eccezioni concordate o motivazioni
di scostamento dalla configurazione di base, da riportare secondo
quanto previsto in "*PR32.1 - Gestione delle Configurazioni*", par.
2.6._
