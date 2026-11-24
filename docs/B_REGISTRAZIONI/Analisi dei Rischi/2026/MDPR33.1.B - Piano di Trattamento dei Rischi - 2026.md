# MDPR33.1.B - Piano di Trattamento dei Rischi - 2026

**Piano di Trattamento Rischi**

**ISO/IEC 27001**

### Revisioni

|          |            |                 |             |               |
|----------|------------|-----------------|-------------|---------------|
| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| 0.0 | 17/11/2026 | Emissione | RSGI | Da approvare |
| 0.1 | 23/11/2026 | Colonna «Asset ERA ridotti» nelle azioni; T13 suddivisa nelle azioni T13–T27; aggiunte T28–T30 per i controlli 5.3, 8.3, 8.15 passati a «non attuato» nella SoA rev. 0.2; colonna «Esito» | RSGI | Da approvare |

### Indice 

# 1 Introduzione

A fronte dell’Analisi dei Rischi sulla Sicurezza delle Informazioni di Vectorlab, effettuata ai sensi della norma ISO/IEC 27001 relativa all’ambito di certificazione ***“Progettazione, sviluppo software e consulenza in particolare in ambito deep tech” - “Design, software development and consultancy primarily in deep tech”*** di Vectorlab è stato predisposto un piano di trattamento dei rischi evidenziati dall’analisi.

# 2 Piano di trattamento

|                                              |                                               |
|----------------------------------------------|-----------------------------------------------|
| **Dati in ingresso al Piano di trattamento** |                                               |
| Data effettuazione Analisi del Rischio       | Agosto – Settembre 2026                       |
| Report di analisi                            | [MDPR33.1.A](MDPR33.1.A%20-%20Report%20Analisi%20dei%20Rischi%20-%202026.md) – Report Analisi dei Rischi - 2026 |

|                                                       |        |     |
|-------------------------------------------------------|--------|-----|
| **Rischio accettabile definito dalla organizzazione** |        |     |
| **Versione del rischio accettabile**                  | **45** |     |

<table style="width:100%;">
<colgroup>
<col style="width: 5%" />
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="8"><strong>Definizione del Piano di trattamento</strong></td>
</tr>
<tr class="even">
<td colspan="4">Azioni definite</td>
<td colspan="2">Rischio residuo</td>
<td colspan="2">Risultati</td>
</tr>
<tr class="odd">
<td><em><strong>N°</strong></em></td>
<td><em><strong>Proposta Azione</strong></em></td>
<td><em><strong>Obiettivo di controllo</strong></em></td>
<td><p><em><strong>Asset Owner</strong></em></p>
<p><em><strong>-</strong></em></p>
<p><em><strong>Risk Owner</strong></em></p></td>
<td><em><strong>Valore</strong></em></td>
<td><em><strong>Impatto Contromis. (RID / Prob / Vuln)</strong></em></td>
<td><em><strong>Termine previsto</strong></em></td>
<td><em><strong>Esito</strong></em><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
</tr>
<tr class="even">
<td><em><strong>1)</strong></em></td>
<td><p>A002 - Software Firma Digitale</p>
<p>L’organizzazione intende <strong>ACCETTARE</strong> le minacce di <em>Obsolescenza, Errore del Personale, Inosservanza delle politiche di sicurezza aziendali, Malfunzionamento Software Applicativo/SO, Malfunzionamento Software di base</em> a causa del <em>Mancato processo di gestione delle configurazioni;</em></p>
<p>In quanto l’organizzazione valuta:</p>
<ul>
<li><p>Che le configurazioni di base per i sistemi in mano ai fornitori, siano conformi agli standard di sicurezza</p></li>
<li><p>I limiti operativi che potrebbero impattare su esigenze organizzative tenuto anche conto della bassa numerosità del personale.</p></li>
</ul></td>
<td><p>5.37</p>
<p>8.09</p></td>
<td><em>Andrea Ruzzenenti (CTO) – Andrea Ruzzenenti (CEO)</em></td>
<td>45</td>
<td>N.A.</td>
<td>N.A.</td>
<td>N.A.</td>
</tr>
<tr class="odd">
<td>2)</td>
<td><p>A0017 – Software di Messaggistica</p>
<p>L’organizzazione intende <strong>ACCETTARE</strong> le minacce di <em>Malfunzionamento Software Applicativo/SO, Malfunzionamento Software di base, Accesso non autorizzato alla rete, sw di base, applicazioni</em> a causa del <em>Mancato processo di gestione delle configurazioni;<br />
</em>L’organizzazione intende inoltre <strong>ACCETTARE</strong> la minaccia di <em>Inadeguate misure di protezione dei dati</em> a causa della <em>Mancanza di tracciabilità delle operazioni eseguite sulle applicazioni;<br />
<br />
</em>In quanto l’organizzazione valuta:</p>
<ul>
<li><p>Che le configurazioni di base per i sistemi in mano ai fornitori, siano conformi agli standard di sicurezza</p></li>
<li><p>che eventuali blocchi sarebbero troppo costosi rispetto al valore effettivo delle informazioni</p></li>
<li><p>I limiti operativi che potrebbero impattare su esigenze organizzative tenuto anche conto della bassa numerosità del personale.</p></li>
</ul></td>
<td><p>5.37</p>
<p>8.03</p>
<p>8.09</p>
<p>8.15</p>
<p>5.23</p></td>
<td><em>Andrea Ruzzenenti (CTO) – Andrea Ruzzenenti (CEO)</em></td>
<td>45</td>
<td>N.A.</td>
<td>N.A.</td>
<td>N.A.</td>
</tr>
<tr class="even">
<td>3)</td>
<td><p>A0039 – Codici Sorgenti di proprietà dei clienti</p>
<p>L’organizzazione intende <strong><mark>ACCETTARE</mark></strong> le minacce di <em>Errore del Personale, Malfunzionamento Software Applicativo/SO, Malfunzionamento Software di base, Accesso non autorizzato alla rete, sw di base, applicazioni, Inosservanza delle politiche di sicurezza aziendali</em> a causa del <em>Mancato processo di gestione delle configurazioni;<br />
</em><br />
In quanto l’organizzazione valuta:</p>
<ul>
<li><p>Che le configurazioni di base per i sistemi in mano ai fornitori, siano conformi agli standard di sicurezza</p></li>
<li><p>che eventuali blocchi sarebbero troppo costosi rispetto al valore delle informazioni che diventano obsolete in brevissimo tempo</p></li>
<li><p>I limiti operativi che potrebbero impattare su esigenze organizzative tenuto anche conto della bassa numerosità del personale.</p></li>
</ul></td>
<td>5.37, 8.09</td>
<td><em>Andrea Ruzzenenti (CTO) – Andrea Ruzzenenti (CEO)</em></td>
<td>45</td>
<td>N.A.</td>
<td>N.A.</td>
<td>N.A.</td>
</tr>
<tr class="odd">
<td>4)</td>
<td><p>A0048 – Immagine dell’azienda – Affidabilità</p>
<p>L’organizzazione intende <strong>ACCETTARE</strong> le minacce di <em>Errore del Personale, Malfunzionamento Software Applicativo/SO, Malfunzionamento Software di base, Inosservanza delle politiche di sicurezza aziendali</em> a causa del <em>Mancato processo di gestione delle configurazioni;<br />
</em><br />
In quanto l’organizzazione valuta:</p>
<ul>
<li><p>Che le configurazioni di base per i sistemi in mano ai fornitori, siano conformi agli standard di sicurezza</p></li>
<li><p>che eventuali blocchi sarebbero troppo costosi rispetto al valore effettivo delle informazioni</p></li>
<li><p>I limiti operativi che potrebbero impattare su esigenze organizzative tenuto anche conto della bassa numerosità del personale.</p></li>
</ul></td>
<td>5.37, 8.09</td>
<td>Andrea Ruzzenenti (Amministratore Unico)</td>
<td>45</td>
<td>N.A.</td>
<td>N.A.</td>
<td>N.A.</td>
</tr>
<tr class="even">
<td>5)</td>
<td><p>A0049 – Reputazione dell’azienda – Fiducia</p>
<p>L’organizzazione intende <strong>ACCETTARE</strong> le minacce di <em>Errore del Personale, Malfunzionamento Software Applicativo/SO, Malfunzionamento Software di base, Inosservanza delle politiche di sicurezza aziendali</em> a causa del <em>Mancato processo di gestione delle configurazioni;<br />
</em><br />
In quanto l’organizzazione valuta:</p>
<ul>
<li><p>Che le configurazioni di base per i sistemi in mano ai fornitori, siano conformi agli standard di sicurezza</p></li>
<li><p>che eventuali blocchi sarebbero troppo costosi rispetto al valore effettivo delle informazioni</p></li>
<li><p>I limiti operativi che potrebbero impattare su esigenze organizzative tenuto anche conto della bassa numerosità del personale.</p></li>
</ul></td>
<td>5.37, 8.09</td>
<td>Andrea Ruzzenenti (Amministratore Unico)</td>
<td>45</td>
<td>N.A.</td>
<td>N.A.</td>
<td>N.A.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>Considerazioni</strong></td>
</tr>
<tr class="even">
<td colspan="8">Data ultimo aggiornamento 22/10/2026</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Inserire informazioni sull'esito. Ad esempio: positivo, negativo, parziale, si ripropone, ecc.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

# 3 Azioni di trattamento 2026

<span style="color:#B3392A">**Aggiunta del 17/11/2026 (bozza RSGI).** Le
azioni derivano dalle procedure riscritte il 16–17/11/2026 e dai controlli
che la SoA indica come applicabili ma non ancora attuati. Responsabili e
scadenze vanno confermati dall'Amministratore Unico; i valori di rischio
residuo vanno ricalcolati in ERA [DA RIPORTARE IN ERA con Nextage].</span>

## 3.1 Rischi accettati da rivalutare

| Rischio | Motivo della rivalutazione | Trattamento proposto |
| --- | --- | --- |
| 2) A0017 – Software di messaggistica | La decisione del 04/11/2026 (dismettere Discord) è superata | Accettare (Amministratore Unico, 18/11/2026): Discord resta in uso con le regole di [REG01](../../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §5, senza dati dei clienti né credenziali |
| 3) A0039 – Codici sorgenti dei clienti | La motivazione «mancato processo di gestione delle configurazioni» non vale più: c'è [PR32.1](../../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT.md) | Ridurre (Amministratore Unico, 18/11/2026): pull request rivista a ogni funzionalità e rilascio, con controllo che nel codice non ci siano password; Dependabot e secret scanning attivi; accessi personali con verifica in due passaggi e revisione semestrale ([PR16.1](../../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md)), revisione del codice e controlli automatici ([PO25](../../../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro.md), [PR23.1](../../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche.md)) |
| Codice e documentazione su GitHub | Nessuna copia esterna al fornitore | Accettare (Amministratore Unico, 18/11/2026): ci si affida alla protezione di GitHub ([PR21.1](../../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore.md) §5) |
| 1), 4), 5) | Stessa motivazione superata | Rivalutare in ERA con le misure di [PR32.1](../../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT.md), [PR19.1](../../../A_CAMBIAMENTO/PR19.1%20-%20Gestione%20del%20Cambiamento.md), [PR21.1](../../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore.md) |

## 3.2 Azioni

| # | Azione | Controlli (Allegato A) | Asset ERA ridotti (rischio) | Documento | Responsabile | Entro | Esito |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | Verifica in due passaggi obbligatoria su Google Workspace e GitHub | 5.17, 8.5 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 32 asset | [REG01](../../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §2, [PR16.1](../../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md) §5 | Amministratore Unico / System Administrator | 24/11/2026 | In corso: obbligo impostato e personale avvisato il 19/11/2026 |
| T2 | Backup del server Aruba e prima prova di ripristino (prova del 18/11/2026 da registrare in MDPR21.1.A) | 8.13, 5.30 | **a 45:** A0002, A0017, A0048, A0049 · sotto soglia: 25 asset | [PR21.1](../../../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore.md), [PR28.1](../../../A_CONTINUITA_%20OPERATIVA/PR28.1%20-%20Gestione%20della%20continuit%C3%A0%20operativa.md) | System Administrator | 15/12/2026 | Aperta |
| T3 | Nomina scritta degli amministratori di sistema ed elenco aggiornato; verifica annuale del loro operato | 8.2, 8.18 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 33 asset | [PR16.1](../../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md) §7 | Referente Privacy / RSGI | 25/11/2026 | Aperta |
| T4 | Prima revisione semestrale degli accessi con gli elenchi delle console | 5.18, 8.2 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 34 asset | [PR16.1](../../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md) §6 | RSGI e Amministrazione | 25/11/2026 | Aperta |
| T5 | Registro delle modifiche ai sistemi: lista ClickUp «Modifiche ai sistemi» (decisione del 18/11/2026) | 8.32, 5.37 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 43 asset | [PR19.1](../../../A_CAMBIAMENTO/PR19.1%20-%20Gestione%20del%20Cambiamento.md) | System Administrator | 30/11/2026 | Aperta |
| T6 | Scansione delle vulnerabilità del server [DA DECIDERE: data]; iscrizione ai bollettini CSIRT. Dependabot e secret scanning su GitHub: attivi (18/11/2026) | 8.8, 5.7 | **a 45:** A0039, A0048, A0049 · sotto soglia: 18 asset | [PR23.1](../../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche.md) | System Administrator / CTO | 15/12/2026 | Aperta |
| T7 | Aggiornamenti di sicurezza automatici sul server; monitoraggio con avvisi via mail a sicurezza@ (anche per i backup falliti) | 8.9, 8.20, 8.1 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 38 asset | [PR32.1](../../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT.md) | System Administrator | 15/12/2026 | Aperta |
| T8 | Caselle privacy@ (Referente Privacy, riserva RSGI) e sicurezza@ (Amministratore Unico, RSGI, System Administrator) attive | 5.24, 5.34, 6.8 | **a 45:** A0017, A0039, A0048, A0049 · sotto soglia: 28 asset | [PR31.1](../../../A_CONFORMITA_/PR31.1%20-%20Gestione%20dei%20Diritti%20degli%20Interessati.md), [PR27.1](../../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach.md) | Amministratore Unico | 19/11/2026 | Fatto il 19/11/2026 |
| T9 | Presa visione dei documenti per il personale e sessione di sensibilizzazione | 6.3, 5.1, 7.7 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 43 asset | [PR05.1](../../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale.md) §8 | RSGI | 12/12/2026 (dopo l'approvazione unica dei documenti) | Aperta |
| T10 | Controlli della sede: cassetta di primo soccorso, estintori, addetti all'emergenza, contatti | 7.5, 7.11, 7.13 | **a 45:** A0002, A0017, A0048, A0049 · sotto soglia: 35 asset | [MDPR18.1.D](../../../A_SICUREZZA%20FISICA%20AMBIENTALE/MDPR18.1.D%20-%20Registri%20interventi%20ambientali.md), [MDPR18.1.G](../../../A_SICUREZZA%20FISICA%20AMBIENTALE/MDPR18.1.G%20-%20Contatti%20di%20emergenza.md) | Amministrazione | 15/12/2026 | Aperta |
| T11 | Regole d'uso di Discord comunicate al personale | 5.14, 8.3 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 37 asset | [REG01](../../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §5 | RSGI | 25/11/2026 | Aperta |
| T12 | Classificazione ed etichettatura delle informazioni applicate nei documenti e nelle cartelle | 5.12, 5.13 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 18 asset | [PO15](../../../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni.md) | RSGI | 31/03/2027 | Aperta |
| T13 | Paragrafo in PR27.1 su come conservare le prove di un incidente (log, screenshot, export): chi le raccoglie e dove si archiviano | 5.28 | **a 45:** A0017, A0039, A0048 · sotto soglia: 21 asset | [PR27.1](../../../A_EVENTI%20%26%20INCIDENTI/PR27.1%20-%20Gestione%20Incidenti%20e%20Data%20Breach.md) | RSGI [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T14 | Per ogni registrazione indicare dove è conservata, chi può modificarla e per quanto tempo si tiene | 5.33 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 34 asset | [MDPR08.1.A](../../../7.5_INFORMAZIONI%20DOCUMENTATE/MDPR08.1.A%20-%20Elenco%20Informazioni%20documentate.md) | RSGI [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T15 | Audit interno svolto da Nextage (consulente esterno) come riesame indipendente; rapporto conservato | 5.35 | **a 45:** A0048, A0049 · sotto soglia: 10 asset | Rapporto di audit interno 2026 | RSGI [DA CONFERMARE: Amministratore Unico] | Data dell'audit interno (fine novembre 2026) | Aperta |
| T16 | Verifica della conformità alle politiche nell'audit interno e verifica annuale a campione dei portatili sui 4 requisiti di REG01 | 5.36 | **a 45:** A0017, A0039, A0048, A0049 · sotto soglia: 29 asset | [REG01](../../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) | RSGI [DA CONFERMARE: Amministratore Unico] | Audit interno 2026; poi annuale | Aperta |
| T17 | Verifica del CV e dei titoli dichiarati all'assunzione, entro i limiti di legge, registrata nella checklist di inserimento | 6.1 | **a 45:** A0048, A0049 · sotto soglia: 11 asset | [MDPR05.1.A](../../../7_GESTIONE%20RISORSE/MDPR05.1.A%20-%20Checklist%20Documenti%20per%20Inserimento%20Personale.md) | Amministrazione [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T18 | Richiamo del codice disciplinare del CCNL in REG01 e PR05.1 e sua affissione in luogo accessibile a tutti (art. 7 L. 300/1970) | 6.4 | **a 45:** A0002, A0017, A0048, A0049 · sotto soglia: 30 asset | [REG01](../../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md), [PR05.1](../../../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale.md) | Amministrazione [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T19 | Elenco di chi ha chiavi o badge dell'ufficio; visitatori sempre accompagnati | 7.2 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 39 asset | Elenco chiavi/badge [DA CREARE] | Amministrazione [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T20 | Regola: l'ultimo che esce chiude a chiave; nessun documento dei clienti lasciato sulle scrivanie | 7.3 | **a 45:** A0002 · sotto soglia: 23 asset | [REG01](../../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) | RSGI [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T21 | Verificare i servizi di sicurezza dell'edificio (portineria, videosorveglianza); se assenti, accettare il rischio con motivazione | 7.4 | **a 45:** A0002 · sotto soglia: 15 asset | Esito della verifica | Amministrazione [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T22 | Valutare se il controllo è non applicabile (unico ufficio, nessuna area riservata) e aggiornare SoA ed ERA | 7.6 | **a 45:** A0002, A0017, A0048, A0049 · sotto soglia: 36 asset | [SoA](../../../02_SOA/SOA%20-%20Statement%20of%20Applicability%20-%20Dichiarazione%20di%20Applicabilit%C3%A0%2027001.md) | RSGI con Amministratore Unico [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T23 | Router e apparati di rete in un punto chiuso; schermi non visibili dall'ingresso | 7.8 | **a 45:** A0002, A0017, A0049 · sotto soglia: 31 asset | [PR32.1](../../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT.md) | System Administrator [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T24 | Registrare la verifica dei 4 requisiti di REG01 sui portatili (disco cifrato, blocco schermo, aggiornamenti, Defender); poi «Attuato» nella SoA | 7.9 | **a 45:** A0002 · sotto soglia: 16 asset | [REG01](../../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) | System Administrator [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T25 | Regola su chiavette e dischi esterni (cifrati, o vietati per i dati dei clienti) | 7.10 | **a 45:** A0002, A0048 · sotto soglia: 17 asset | [REG01](../../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) | RSGI [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T26 | Cancellazione sicura prima di dismettere o riassegnare un dispositivo, registrata | 7.14 | **a 45:** A0002, A0017 · sotto soglia: 29 asset | [MDPR05.1.V](../../../7_GESTIONE%20RISORSE/MDPR05.1.V%20-%20Modulo_consegna_riconsegna_HW_utenze.md), [MDPR32.1.B](../../../B_REGISTRAZIONI/Analisi%20dei%20Rischi/2026/MDPR32.1.B%20-%20Inventario%20degli%20asset%20-%202026.md) | System Administrator [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T27 | Filtro web minimo con Defender SmartScreen sui PC, oppure accettazione del rischio motivata | 8.23 | **a 45:** A0017, A0049 · sotto soglia: 13 asset | [REG01](../../../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) | System Administrator [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T28 | Verificare nel mansionario le attività incompatibili (chi chiede e chi approva accessi e modifiche); dove le persone non bastano, controllo dell'Amministratore Unico | 5.3 | **a 45:** A0002, A0039, A0048, A0049 · sotto soglia: 24 asset | [ALPO01.B](../../../01_POLITICA%20SISTEMA%20INTEGRATO/ALPO01.B%20-%20Mansionario-Rev%200.0.md) | RSGI [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T29 | Nella revisione degli accessi (T4) verificare che i permessi su Drive e GitHub siano limitati ai progetti di ciascuno | 8.3 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 30 asset | [PR16.1](../../../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md) | RSGI e Amministrazione [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |
| T30 | Definire quali log si conservano (Google Workspace, GitHub, server Aruba), per quanto tempo e chi li controlla | 8.15 | **a 45:** A0002, A0017, A0039, A0048, A0049 · sotto soglia: 35 asset | [PR32.1](../../../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT.md), [PR23.1](../../../A_MINACCE%20%26%20VULNERABILITA_/PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche.md) | System Administrator [DA CONFERMARE: Amministratore Unico] | 12/12/2026 | Aperta |

La colonna «Asset ERA ridotti» viene dall'analisi ERA «Agosto 2026»
(collegamento controllo ↔ asset): indica gli asset al rischio limite
(45) e il numero di asset sotto soglia su cui agiscono i controlli
dell'azione. Le azioni T13–T30 (aggiunte il 23/11/2026) coprono i
controlli che la SoA rev. 0.2 indica come applicabili ma non attuati.
La colonna «Esito» registra il risultato di ogni azione (data ed
evidenza) quando viene chiusa (ISO/IEC 27001:2022, 8.3).

Lo stato delle azioni si segue nella lista ClickUp «Non conformità e
miglioramento» e si riporta nel Riesame della Direzione ([PR12.1](../../../9.3_RIESAME%20DIREZIONE/PR12.1%20-%20Riesame%20della%20Direzione.md)). A
ogni azione completata si aggiorna la colonna «Applicato» della SoA.
