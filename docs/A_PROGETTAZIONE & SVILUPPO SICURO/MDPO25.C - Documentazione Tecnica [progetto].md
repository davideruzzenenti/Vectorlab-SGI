# MDPO25.C - Documentazione Tecnica [progetto]

### Revisioni

|          |            |                 |                      |               |
|----------|------------|-----------------|----------------------|---------------|
| **Rev.** | **Data**   | **Descrizione** | **Redatto**          | **Approvato** |
| 0.0      | 24/04/2026 | Prima emissione | Responsabile di Area | CTO           |
|          |            |                 |                      |               |
|          |            |                 |                      |               |
|          |            |                 |                      |               |

# Indice

|                   |                                            |
|-------------------|--------------------------------------------|
| **Approvatore**   | Menzionare la risorsa coinvolta            |
| **Collaboratori** | Menzionare le risorse coinvolte            |
| **Informati**     | Menzionare le risorse coinvolte            |
| **Committente**   | Denominazione del committente del progetto |
| **Progetto**      | Denominazione del progetto                 |

# 1. Introduzione

Cos’è, a cosa serve, cosa fa, dove si colloca.

# 2. Architettura Globale

Come è definita, come è strutturata, su quale stack tecnologico si basa. Schema architetturale generale di riferimento con collegamenti ad altri applicativi esterni e relative modalità di integrazione / comunicazione

# 2.1. Stack tecnologico

…

### 2.1.1. Database

…

### 2.1.2. Backend

…

### 2.1.3. Frontend

…

# 2.2. Schema architetturale \[\<istanza (prod, dev, test, …)\>\]

Riportare uno schema architetturale ed eventuale descrizione a corredo, relativi all’istanza presa in considerazione.

# 3. Architettura Interna

Schema architetturale interno della soluzione sviluppata.

# 3.1. Schema architetturale

Riportare uno schema architetturale interno ed eventuale descrizione a corredo.

# 3.2. Database

Descrizione del database scelto, diagrammi e strutture dati.

# 3.3. Backend

Descrizione architetturale interna dell’applicazione lato BE.

# 3.4. Frontend

Descrizione architetturale interna dell’applicazione lato FE.

# 3.5. Struttura del progetto

Per ogni componente applicativo realizzato, riportarne le dipendenze e l’alberatura.

### 3.5.x. \<Backend/Frontend/Middleware/App/…\>

#### Dipendenze

Si riportano di seguito, le librerie aggiunte per il progetto:

- \<*nome libreria*\> (\<*versione major.minor.patch\>*): *descrizione tecnica*

- *…*

#### Alberatura

Riportare cartelle e file creati specificamente per l’applicazione, secondo il livello di dettaglio e granularità adeguati:

- **\<cartella\>**: descrizione e contenuti;

  - **\<sotto cartella\>**: descrizione e contenuti;

    - \<file\>: descrizione ed eventuale dettaglio implementativo

    - …

  - …

- …

# 4. Flussi applicativi

- schema + descrizione del flusso applicativo globale

- schema + descrizione dei sotto flussi applicativi specifici

- fornire la documentazione del codice (funzioni, metodi, classi, …)

- funzionamento degli eventi (come e quando vengono inviati, come aggiungerne o modificarne uno)

Elencare nel dettaglio i moduli/servizi/componenti/… utilizzati per realizzare i flussi applicativi che necessitano di un approfondimento o che devono essere esplicitati per interesse progettuale.

# 4.x. \<Contesto applicativo (app web, app mobile, …)\>

### \<modulo/servizio/componente/…\>

**\<tipologia\>**

#### Percorso

\<path/to/folder_or_file\>

#### Descrizione

Fornire descrizione tecnica dettagliata.

# 5. Integrazioni

Elencare le integrazioni e descrivere dettagliatamente le procedure previste e le implementazioni adottate per ognuna di esse, ove applicabili.

# 5.x. \<Contesto applicativo (app web, app mobile, …)\>

- link / riferimento documentazione e specifiche finali

- come funziona

  - descrizione del tipo di integrazione

  - quali servizi sono usati / disponibili

  - descrizione dei messaggi di Request e Response:

    - della struttura

    - significato dei campi e tipologia

    - opzionalità/obbligatorietà (in caso anche descrivendo se e quando la condizione di obbligatorietà possa variare)

    - come sono valorizzati

- dove mettere le mani

- come estenderla

- come svilupparne una nuova

- come verificare / ricercare possibili problematiche

- come testare da dentro l’applicazione

- come testare da fuori

  - quali tool usare

  - come configurarli

  - che servizi

  - esempi di richieste di input da usare in test per ognuno dei servizi

  - risposte previste in caso di successo o errore

  - casistiche

- configurazione

  - dove si trova

  - com’è fatta

  - come e cosa modificare

# 6. Servizi di interfacciamento

- tipologia: REST, GraphQL, gRPC, WebSocket, MQTT, SOAP

- dove sono

- come si estendono

- api sono disponibili

  - url

  - dati input

  - output

- come funziona auth

# 7. Diagnostica

- dove e come sono gestiti i log e come interpretarli, come abilitare diversi livelli di log

- procedure per verificare che sia tutto ok (anche lato DB) o trovare possibili errori

- casi frequenti di possibili errori, descrizione di conseguenze sulla produzione e possibili accorgimenti

# 8. Criteri di sicurezza

- descrivere criteri e requisiti di sicurezza implementati (secure by design, privacy by design, …)

# 9. Installazione e configurazione

…

# 9.1. Repository

Elencare tutti i repository di progetto.

- \<url\>: descrizione

- …

# 9.2. Aspetti sistemistici

Per ogni ambiente, specificare tutte le informazioni in modo dettagliato.

### \<Ambiente dev/test/prod/…\>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><h4 id="sistema">Sistema</h4></td>
</tr>
<tr class="even">
<td><strong>Hostname</strong></td>
<td>&lt;hostname&gt;</td>
</tr>
<tr class="odd">
<td><strong>Proxy</strong></td>
<td>&lt;proxy&gt;</td>
</tr>
<tr class="even">
<td><strong>Conf. di rete</strong></td>
<td><table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>IP</strong></td>
<td>-</td>
</tr>
<tr class="even">
<td><strong>Subnet</strong></td>
<td>-</td>
</tr>
<tr class="odd">
<td><strong>Gateway</strong></td>
<td>-</td>
</tr>
<tr class="even">
<td><strong>DNS1</strong></td>
<td>-</td>
</tr>
<tr class="odd">
<td><strong>DNS2</strong></td>
<td>-</td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="odd">
<td><strong>Ubuntu</strong></td>
<td>&lt;versione&gt;</td>
</tr>
<tr class="even">
<td><strong>Docker</strong></td>
<td>&lt;versione&gt;</td>
</tr>
<tr class="odd">
<td><strong>Docker Compose</strong></td>
<td>&lt;versione&gt;</td>
</tr>
<tr class="even">
<td><strong>MongoDB</strong></td>
<td>&lt;versione&gt;</td>
</tr>
<tr class="odd">
<td><strong>Record DNS</strong></td>
<td>&lt;url&gt;</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><h4 id="composizione-docker-stack">Composizione Docker Stack</h4></td>
</tr>
<tr class="even">
<td><strong>Apache</strong></td>
<td>&lt;nome container&gt;</td>
</tr>
<tr class="odd">
<td><strong>BE</strong></td>
<td>&lt;nome container&gt;</td>
</tr>
<tr class="even">
<td><strong>FE</strong></td>
<td>&lt;nome container&gt;</td>
</tr>
<tr class="odd">
<td><strong>MongoDB</strong></td>
<td>&lt;nome container&gt;</td>
</tr>
<tr class="even">
<td><strong>Portainer</strong></td>
<td>&lt;nome container&gt;</td>
</tr>
<tr class="odd">
<td><strong>Portainer Agent</strong></td>
<td>&lt;nome container&gt;</td>
</tr>
<tr class="even">
<td><strong>&lt;container&gt;</strong></td>
<td>&lt;nome container&gt;</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="vm">VM</h4></td>
</tr>
<tr class="even">
<td>Informazioni di installazione/configurazione VM</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><h4 id="vpn">VPN</h4></td>
</tr>
<tr class="even">
<td><strong>Tipologia/Client</strong></td>
<td>&lt;openvpn/sophos/cisco/fortinet/…&gt;</td>
</tr>
<tr class="odd">
<td><strong>IP/Gateway</strong></td>
<td>-</td>
</tr>
<tr class="even">
<td><strong>Porta</strong></td>
<td>-</td>
</tr>
<tr class="odd">
<td rowspan="2"><strong>Credenziali di accesso</strong></td>
<td>u: &lt;username&gt;<br />
p: &lt;password&gt;</td>
</tr>
<tr class="even">
<td>u: &lt;username&gt;<br />
p: &lt;password&gt;</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><h4 id="servizi-e-accessi">Servizi e accessi</h4></td>
</tr>
<tr class="even">
<td><strong>Mongo</strong></td>
<td><p>u: &lt;username&gt;<br />
p: &lt;password&gt;</p>
<p>DB: &lt;nome db&gt;</p>
<p>grants: &lt;grants&gt;</p></td>
</tr>
<tr class="odd">
<td><strong>Portainer</strong></td>
<td>u: &lt;username&gt;<br />
p: &lt;password&gt;</td>
</tr>
<tr class="even">
<td><strong>Docker</strong></td>
<td>u: &lt;username&gt;<br />
p: &lt;password&gt;</td>
</tr>
<tr class="odd">
<td><strong>&lt;Servizio&gt;</strong></td>
<td>u: &lt;username&gt;<br />
p: &lt;password&gt;</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><h4 id="certificati">Certificati</h4></td>
</tr>
<tr class="even">
<td><strong>Scadenza</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Passphrase</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Common name (CN)</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Rilascio</strong></td>
<td></td>
</tr>
</tbody>
</table>

# 9.3. Ambienti

###  \<Ambiente dev/test/prod/…\>

- struttura cartelle applicative / servizi (BE/FE)

- dove trovarle

- procedura di installazione

- procedure di aggiornamento

- procedure di stop / start servizi

- log

# 9.4. Procedure di deploy

- Documentare procedure di deploy (Jenkins, Store, …)

# 9.5. Procedure di collaudo

- Riferimento documenti procedure.

<!-- -->

- Descrizione dei servizi di test da utilizzare e come usarli.

- Quali punti di collaudo effettuare e come affrontarli in fase di collaudo, input e risultati attesi.

# 10. Manutenzione

Riportare di seguito tutte le attività di manutenzione.

# 10.1. Manutenzione non pianificabile

Include la manutenzione Correttiva e di Emergenza.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 42%" />
<col style="width: 15%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Codice</strong></td>
<td>&lt;codice progressivo&gt;</td>
<td><strong>Tipologia</strong></td>
<td>Emergenza</td>
</tr>
<tr class="even">
<td><strong>Data segnalazione</strong></td>
<td>5 apr 2023</td>
<td><strong>Data risoluzione</strong></td>
<td>5 apr 2023</td>
</tr>
<tr class="odd">
<td><strong>Descrizione intervento</strong></td>
<td colspan="3"><strong>Analisi</strong>: ...<br />
<strong>Attuazione</strong>: ...<br />
<strong>Verifica</strong>: ...<br />
<strong>Rilascio</strong>: ...</td>
</tr>
<tr class="even">
<td><strong>Rif. ticket/source</strong></td>
<td>&lt;rif. ticket/source&gt;</td>
<td><strong>Rif. commit</strong></td>
<td>&lt;rif. commit&gt;</td>
</tr>
</tbody>
</table>

# 10.2. Manutenzione pianificabile

Include la manutenzione Preventiva, Migliorativa, Adeguativa, Evolutiva.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 42%" />
<col style="width: 15%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Codice</strong></td>
<td>&lt;codice progressivo&gt;</td>
<td><strong>Tipologia</strong></td>
<td>Preventiva</td>
</tr>
<tr class="even">
<td><strong>Data segnalazione</strong></td>
<td>5 apr 2023</td>
<td><strong>Data risoluzione</strong></td>
<td>5 apr 2023</td>
</tr>
<tr class="odd">
<td><strong>Descrizione intervento</strong></td>
<td colspan="3"><strong>Analisi</strong>: ...<br />
<strong>Attuazione</strong>: ...<br />
<strong>Verifica</strong>: ...<br />
<strong>Rilascio</strong>: ...</td>
</tr>
<tr class="even">
<td><strong>Rif. ticket/source</strong></td>
<td>&lt;rif. ticket/source&gt;</td>
<td><strong>Rif. commit</strong></td>
<td>&lt;rif. commit&gt;</td>
</tr>
</tbody>
</table>
