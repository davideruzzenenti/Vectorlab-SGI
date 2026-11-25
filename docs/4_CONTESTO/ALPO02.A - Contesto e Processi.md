# ALPO02.A - Contesto e Processi

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0 | 23/11/2026 | Emissione | RSGI | Da approvare |

Rappresenta il contesto dell'organizzazione e i processi del Sistema di Gestione Integrato nel campo di applicazione definito in [PO02](PO02%20-%20Gestione%20del%20Contesto.md) §4 (ISO 9001 4.1–4.4; ISO/IEC 27001:2024+A1:2024, 4.1–4.4). Input, output, responsabilità e indicatori di ogni processo sono descritti nella procedura indicata ([PO02](PO02%20-%20Gestione%20del%20Contesto.md) §5.1). I codici sono link alle procedure.

## Diagramma del contesto

<div class="sgi-contesto">
<div class="sgi-esterni">
<div class="sgi-box est"><strong>Clienti</strong><span>il team lavora nei loro sistemi e strumenti</span></div>
<div class="sgi-box est"><strong>Fornitori</strong><span>IT esterno, consulenti, servizi cloud</span></div>
</div>
<div class="sgi-perimetro">
<p class="sgi-titolo-perimetro">Perimetro SGI: servizio Ynsera</p>
<div class="sgi-box sup"><strong>Sede di Genova</strong><span>Piazza Borgo Pila 39/22, piano 8 (unico sito)</span></div>
<div class="sgi-box sup"><strong>Lavoro agile</strong><span>portatili aziendali con i requisiti di <a href="../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali/">REG01</a> §3</span></div>
<div class="sgi-box sup"><strong>Servizi affidati a terzi</strong><span>server Aruba, Google Workspace, GitHub, ClickUp, Bitwarden (<a href="../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/">PR26.1</a>)</span></div>
</div>
<div class="sgi-esterni">
<div class="sgi-box est"><strong>Enti</strong><span>RINA, Garante privacy, INAIL</span></div>
<div class="sgi-box est"><strong>Proprietà</strong><span>socio unico</span></div>
</div>
</div>
<p class="sgi-nota sgi-esclusi">Esclusi dal campo: prodotti della unit Vectorlab, bandi e progetti di ricerca. Condividono sede, persone e strumenti: i controlli del sistema su queste risorse valgono per tutta l'organizzazione (<a href="../../4_CONTESTO/PO02%20-%20Gestione%20del%20Contesto/">PO02</a> §4.4).</p>

## Mappa dei processi

<div class="sgi-mappa">
<p class="sgi-etichetta">Processi di direzione</p>
<div class="sgi-riga">
<div class="sgi-box dir"><strong>Contesto e rischi</strong><span><a href="../../4_CONTESTO/PO02%20-%20Gestione%20del%20Contesto/">PO02</a> · <a href="../../6.1_ANALISI%20DEI%20RISCHI/PR33.1%20-%20Processo%20Analisi%20del%20Rischio%20e%20Trattamento/">PR33.1</a></span></div>
<div class="sgi-box dir"><strong>Politica e obiettivi</strong><span><a href="../../01_POLITICA%20SISTEMA%20INTEGRATO/PO01%20-%20Sistema%20Integrato-Rev%200.0/">PO01</a> · <a href="../../6.2_OBIETTIVI/MDPO03.A%20-%20Lista%20Obiettivi/">MDPO03.A</a></span></div>
<div class="sgi-box dir"><strong>Riesame della direzione</strong><span><a href="../../9.3_RIESAME%20DIREZIONE/PR12.1%20-%20Riesame%20della%20Direzione/">PR12.1</a></span></div>
</div>
<p class="sgi-etichetta">Processi primari: servizio Ynsera</p>
<div class="sgi-flusso">
<div class="sgi-box est"><strong>Cliente</strong><span>requisiti</span></div><div class="sgi-freccia">→</div>
<div class="sgi-box pri"><strong>Commerciale</strong><span><a href="../../8.2_PRODOTTI%20%26%20SERVIZI/PR09.1%20-%20Gestione%20Commerciale/">PR09.1</a></span><em>lead, offerta, riesame dei requisiti</em></div><div class="sgi-freccia">→</div>
<div class="sgi-box pri"><strong>Commessa</strong><span><a href="../../8.2_PRODOTTI%20%26%20SERVIZI/PR35.1%20-%20Digital/">PR35.1</a></span><em>avvio, esecuzione negli strumenti del cliente, chiusura</em></div><div class="sgi-freccia">→</div>
<div class="sgi-box est"><strong>Cliente</strong><span>soddisfazione</span></div>
</div>
<p class="sgi-etichetta">Processi di supporto</p>
<div class="sgi-riga">
<div class="sgi-box sup"><strong>Personale</strong><span><a href="../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale/">PR05.1</a> · <a href="../../7_GESTIONE%20RISORSE/PR06.1%20-%20Gestione%20delle%20Performance/">PR06.1</a></span></div>
<div class="sgi-box sup"><strong>Fornitori</strong><span><a href="../../A_FORNITORI/PR26.1%20-%20Gestione%20dei%20fornitori/">PR26.1</a></span></div>
<div class="sgi-box sup"><strong>Infrastruttura IT</strong><span><a href="../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT/">PR32.1</a></span></div>
<div class="sgi-box sup"><strong>Accessi e backup</strong><span><a href="../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi/">PR16.1</a> · <a href="../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore/">PR21.1</a></span></div>
<div class="sgi-box sup"><strong>Sicurezza fisica</strong><span><a href="../../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale/">PR18.1</a></span></div>
<div class="sgi-box sup"><strong>Documenti</strong><span><a href="../../7.5_INFORMAZIONI%20DOCUMENTATE/PR08.1%20-%20Gestione%20Informazioni%20Documentate/">PR08.1</a></span></div>
<div class="sgi-box sup"><strong>Comunicazione</strong><span><a href="../../7.4_COMUNICAZIONI/PO07%20-%20Politica%20Gestione%20della%20Comunicazione/">PO07</a></span></div>
<div class="sgi-box sup"><strong>Privacy</strong><span><a href="../../A_CONFORMITA_/PO31%20-%20Misure%20di%20sicurezza%20protezione%20dati%20personali/">PO31</a></span></div>
</div>
<p class="sgi-etichetta">Monitoraggio e miglioramento</p>
<div class="sgi-riga">
<div class="sgi-box dir"><strong>Indicatori</strong><span><a href="../../9.1_MONITORAGGIO%20KPI/MDPR10.1.A%20-%20Tabella%20Indicatori/">MDPR10.1.A</a></span></div>
<div class="sgi-box dir"><strong>Audit interno</strong><span><a href="../../9.2_AUDIT%20INTERNO/PR11.1%20-%20Audit%20Interno/">PR11.1</a></span></div>
<div class="sgi-box dir"><strong>NC e incidenti</strong><span><a href="../../10_GESTIONE%20NON%20CONFORMITA_%20E%20MIGLIORAMENTO/PR13.1%20-%20Gestione%20delle%20Non%20Conformit%C3%A0%20e%20Azioni%20di%20Miglioramento/">PR13.1</a> · <a href="../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach/">PR27.1</a></span></div>
<div class="sgi-box dir"><strong>Cambiamenti e continuità</strong><span><a href="../../A_CAMBIAMENTO/PR19.1%20-%20Gestione%20del%20Cambiamento/">PR19.1</a> · <a href="../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa/">PR28.1</a></span></div>
</div>
<p class="sgi-nota">Fuori dal campo di applicazione: prodotti della unit Vectorlab, bandi e progetti di ricerca.</p>
</div>
