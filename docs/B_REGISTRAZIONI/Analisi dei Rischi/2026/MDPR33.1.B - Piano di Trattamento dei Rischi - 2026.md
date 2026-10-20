# MDPR33.1.B - Piano di Trattamento dei Rischi - 2026

**Piano di Trattamento Rischi**

**ISO/IEC 27001**

### Revisioni

|          |            |                 |             |               |
|----------|------------|-----------------|-------------|---------------|
| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| 0.0      | 29/09/2026 | Prima emissione: piano di trattamento dei rischi 2026 | CISO        | Da approvare (Amministratore Unico) |
| 0.1      | 20/10/2026 | Corretta la data di emissione (riportava quella del modello); campo di applicazione allineato a PO02; ruolo «IT» dell'owner corretto in «CTO» (la funzione IT è esterna) | RSGI        | Da approvare  |
|          |            |                 |             |               |

### Indice 

# 1 Introduzione

A fronte dell’Analisi dei Rischi sulla Sicurezza delle Informazioni di Vectorlab, effettuata ai sensi della norma ISO/IEC 27001 relativa all’ambito di certificazione ***“Progettazione, sviluppo software e consulenza in particolare in ambito deep tech” - “Design, software development and consultancy primarily in deep tech”*** di Vectorlab è stato predisposto un piano di trattamento dei rischi evidenziati dall’analisi.

# 2 Piano di trattamento

|                                              |                                               |
|----------------------------------------------|-----------------------------------------------|
| **Dati in ingresso al Piano di trattamento** |                                               |
| Data effettuazione Analisi del Rischio       | Agosto – Settembre 2026                       |
| Report di analisi                            | MDPR33.1.A – Report Analisi dei Rischi - 2026 |

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
<p>1.23</p></td>
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
<td>Andrea Ruzzenenti (BD) – Andrea Ruzzenenti (CEO)</td>
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
<td>Andrea Ruzzenenti (BD) – Andrea Ruzzenenti (CEO)</td>
<td>45</td>
<td>N.A.</td>
<td>N.A.</td>
<td>N.A.</td>
</tr>
<tr class="odd">
<td colspan="8"><strong>Considerazioni</strong></td>
</tr>
<tr class="even">
<td colspan="8">Data ultimo aggiornamento 29/09/2026</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Inserire informazioni sull'esito. Ad esempio: positivo, negativo, parziale, si ripropone, ecc.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>
