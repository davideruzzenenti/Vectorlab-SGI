# MDPO25.G - Piano di Test [progetto]


## Cover

<table>
<tr><td></td><td></td><td rowspan="6" colspan="2"></td><td rowspan="6" colspan="5">Piano di Test</td><td rowspan="3" colspan="2">MDPO25.G</td></tr>
<tr><td></td><td></td></tr>
<tr><td></td><td></td></tr>
<tr><td></td><td></td><td rowspan="3">Rev. 0.0</td><td rowspan="3">24/04/2026</td></tr>
<tr><td></td><td></td></tr>
<tr><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td colspan="3">Cliente</td><td colspan="6">&lt;Cliente&gt;</td></tr>
<tr><td></td><td></td><td colspan="3">Progetto</td><td colspan="6">&lt;Progetto&gt;</td></tr>
<tr><td></td><td></td><td colspan="3">Livello di classificazione</td><td colspan="6">Interno</td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td>Rev.</td><td>Data</td><td colspan="4">Descrizione</td><td>Redatto</td><td>Approvato</td><td>Classificazione</td></tr>
<tr><td></td><td></td><td>0.0</td><td>24/04/2026</td><td colspan="4">Prima emissione</td><td>Resp. Divisione</td><td>CTO</td><td>Interno</td></tr>
</table>


## 1. Ambito e Contesto

<table>
<tr><td colspan="4">1. Ambito e Contesto</td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td colspan="5">Questa sezione descrive il perimetro dei test eseguiti, specificando i dati utilizzati, le modalità di gestione, gli ambienti coinvolti e i soggetti autorizzati al trattamento dei dati.</td></tr>
<tr><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>1.1. Set di dati utilizzati</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Nota di compilazione</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Selezionare le configurazioni opportune che descrivono gli scenari di test previsti dalla sessione, tra quelle proposte nella tabella.</td><td></td><td></td><td></td><td></td></tr>
<tr><td>La tabella propone alcune possibili configurazioni.</td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Tipologia</td><td>Origine</td><td>Anonimizzazione</td><td>Modalità di inserimento</td><td>Finalità</td></tr>
<tr><td>Dati reali anonimizzati</td><td>Forniti dal Cliente (produzione/pre-produzione)</td><td>Effettuata dal Cliente</td><td>Inseriti dal Team di progetto</td><td>Simulare scenari reali senza esposizione di dati sensibili</td></tr>
<tr><td>Dati reali non anonimizzati</td><td>Forniti dal Cliente (produzione/pre-produzione)</td><td>Effettuata dal Team di progetto con tool/script</td><td>Inseriti dal Team di progetto</td><td>Test su dati conformi al reale, previa anonimizzazione</td></tr>
<tr><td>Dati sintetici</td><td>Generati dal Team di progetto o da tool/script</td><td>Non necessaria</td><td>Inseriti dal Team di progetto o generati in automatico</td><td>Simulazione controllata di scenari specifici</td></tr>
<tr><td>Dati inseriti manualmente</td><td>Generati tramite l’applicativo</td><td>Non necessaria</td><td>Inseriti manualmente dai tester</td><td>Verifica dell&#x27;inserimento e della gestione dati dall’interfaccia</td></tr>
<tr><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>1.2. Ambiente di test</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Nota di compilazione</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Selezionare uno o più scenari per descrivere l’ambiente in cui si eseguirà il testing previsto dalla sessione.</td><td></td><td></td><td></td><td></td></tr>
<tr><td>La tabella propone alcuni possibili scenari.</td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Ambiente</td><td>Descrizione</td><td>Scopo</td><td></td><td></td></tr>
<tr><td>Sviluppo</td><td>Ambiente interno agli sviluppatori</td><td>Test unitari e integrazione iniziale</td><td></td><td></td></tr>
<tr><td>Test</td><td>Ambiente separato con dati di test</td><td>Test funzionali e di accettazione</td><td></td><td></td></tr>
<tr><td>Pre-produzione</td><td>Replica dell’ambiente di produzione</td><td>Test di regressione e validazione finale</td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>1.3. Soggetti coinvolti</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Nota di compilazione</td><td></td><td></td><td></td><td></td></tr>
<tr><td>Indicare i soggetti coinvolti per la gestione de idati d itest che verranno utilizzati nella sessione.</td><td></td><td></td><td></td><td></td></tr>
<tr><td>La tabella propone alcuni possibili scenari.</td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Ruolo</td><td>Responsabilità</td><td>Accesso ai dati di test</td><td></td><td></td></tr>
<tr><td>Team di test</td><td>Esecuzione test, verifica risultati</td><td>Sì, secondo policy di accesso</td><td></td><td></td></tr>
<tr><td>Team di sviluppo</td><td>Creazione e gestione ambienti</td><td>Solo su dati anonimi o sintetici</td><td></td><td></td></tr>
<tr><td>Cliente</td><td>Fornitura dati di test</td><td>Accesso completo ai dati di origine</td><td></td><td></td></tr>
<tr><td>CSM / PM / PL</td><td>Supervisione e validazione</td><td>Limitato ai report dei test</td><td></td><td></td></tr>
</table>


## 2. Risultati

<table>
<tr><td colspan="8">2. Risultati</td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td colspan="8">Nota di compilazione</td><td></td><td></td></tr>
<tr><td colspan="8">Al termine della sessione per il piano di test, compilare e aggiornare le tabelle sottostanti sulla base degli esiti risultanti.<br><br>Copertura dei Requisiti<br><br>Verificare che tutti i requisiti siano stati testati.<br>Si basa sulla tracciabilità tra test case e requisiti (matrice di tracciabilità).<br><br>Obiettivo: Nessun requisito deve rimanere non testato.<br><br>Tutti i TC previsti sono stati superati → [verde] completa<br>Non tutti i TC previsti sono stati superati → [giallo] parziale<br>Nessun TC previsto è stato superato → [rosso] assente</td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td colspan="8">Matrice di tracciabilità</td><td></td><td></td></tr>
<tr><td rowspan="2">Requisito</td><td colspan="2">TC Funzionali [TF]</td><td colspan="2">TC Non funzionali [TNF]</td><td colspan="2">TC Interfaccia esterna [TIE]</td><td rowspan="2">Copertura</td><td></td><td></td></tr>
<tr><td>Superati</td><td>Previsti</td><td>Superati</td><td>Previsti</td><td>Superati</td><td>Previsti</td><td></td><td></td></tr>
<tr><td>Riferimento codice requisito</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>completa / parziale / assente</td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>SESSIONE </td><td>&lt;ID Sessione&gt;</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Funzionali [TF]</td><td>2</td><td>0.4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Interfaccia esterna [TIE]</td><td>2</td><td>0.4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Non funzionali [TNF]</td><td>1</td><td>0.2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Test case totali</td><td>5</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Superati</td><td>2</td><td>0.4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Bloccati</td><td>1</td><td>0.2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Falliti</td><td>1</td><td>0.2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>In sospeso</td><td>1</td><td>0.2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>Test Case Totali</td><td>5</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</table>


## 3. Sessione

<table>
<tr><td colspan="3">REQUISITI</td><td colspan="7">TEST CASE</td><td></td></tr>
<tr><td>Codice</td><td>Area di riferimento</td><td>Titolo</td><td>Codice</td><td>Tipologia</td><td>Descrizione</td><td>Data</td><td>Esecutore</td><td>Esito</td><td>Note</td><td></td></tr>
<tr><td>REQ01</td><td>AREA RIFERIMENTO ESEMPIO</td><td>REQUISITO ESEMPIO 1</td><td>TF01</td><td>Funzionale</td><td>- PRIMO STEP TEST<br>- SECONDO STEP TEST<br>- TERZO STEP TEST</td><td>10/02/2020</td><td>NOME ESECUTORE</td><td>Superato</td><td>NESSUNA EVIDENZA</td><td></td></tr>
<tr><td>REQ02</td><td>AREA RIFERIMENTO ESEMPIO</td><td>REQUISITO ESEMPIO 2</td><td>TIE01</td><td>UI/UX</td><td>- PRIMO STEP TEST<br>- SECONDO STEP TEST<br>- TERZO STEP TEST</td><td>11/02/2020</td><td>NOME ESECUTORE</td><td>Bloccato</td><td>EVIDENZA 1</td><td></td></tr>
<tr><td>REQ03</td><td>AREA RIFERIMENTO ESEMPIO</td><td>REQUISITO ESEMPIO 3</td><td>TNF01</td><td>Prestazionale</td><td rowspan="2">- PRIMO STEP TEST<br>- SECONDO STEP TEST<br>- TERZO STEP TEST</td><td rowspan="2">12/02/2020</td><td rowspan="2">NOME ESECUTORE</td><td>Fallito</td><td rowspan="2">NESSUNA EVIDENZA </td><td></td></tr>
<tr><td>REQ04</td><td>AREA RIFERIMENTO ESEMPIO</td><td>REQUISITO ESEMPIO 4</td><td>TF01</td><td>Funzionale</td><td>In sospeso</td><td></td></tr>
<tr><td>REQ05</td><td>AREA RIFERIMENTO ESEMPIO TEST NF</td><td>REQUISITO PRESTAZIONALE</td><td>TIE01</td><td>Comunicazione</td><td>- PRIMO STEP TEST<br>- SECONDO STEP TEST<br>- TERZO STEP TEST<br></td><td>12/02/2020</td><td>NOME ESECUTORE</td><td>Superato</td><td>EVIDENZA 2</td><td></td></tr>
</table>
