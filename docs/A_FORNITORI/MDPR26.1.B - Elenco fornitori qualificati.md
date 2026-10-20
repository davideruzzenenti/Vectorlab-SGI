# MDPR26.1.B - Elenco fornitori qualificati

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0      | 24/04/2026 | Prima emissione (modello vuoto) | RSGI | Amministratore Unico |
| 0.1      | 20/10/2026 | Prima compilazione: fornitori che svolgono attività e processi per conto di Vectorlab nel campo di applicazione del SGI (elenco delle attività svolte presso terzi), ricavati dall'anagrafica fornitori amministrativa e dall'inventario degli asset. Stato di qualifica e accordi da verificare; voce Aruba aggiornata con le informazioni dell'IT esterno (server dedicato) | RSGI | Da approvare |

## 1 Scopo

Il registro elenca i fornitori ai quali Vectorlab affida attività o
processi che rientrano nel campo di applicazione del Sistema di
Gestione Integrato (attività svolte presso terzi), con la loro
classificazione di criticità secondo PR26.1. Risponde anche alla
richiesta dell'ente di certificazione di un «elenco delle attività
svolte presso terzi».

I servizi applicativi (es. la piattaforma di automazione n8n, asset A0022)
sono installati e gestiti da Vectorlab sul server dedicato Aruba: la
gestione applicativa è interna, l'infrastruttura fisica e il data center
sono del fornitore (voce 1).

Non sono elencati i fornitori senza impatto sul SGI (ristorazione,
viaggi, cancelleria, acquisti occasionali di attrezzature).
L'anagrafica amministrativa completa è tenuta dall'Amministrazione.

Legenda **impatto sulla sicurezza delle informazioni** (PR26.1):

- **A** – accesso diretto alle informazioni di Vectorlab o dei clienti;
- **B** – svolge attività necessarie alla sicurezza delle informazioni senza accedere alle informazioni;
- **C** – non accede alle informazioni ma può introdurre rischi;
- **—** – nessun impatto.

Stato della qualifica: **Q** qualificato, **QR** qualificato con riserva,
**R** respinto, **DV** da valutare. Per i fornitori cloud la qualifica si
basa sulle certificazioni pubbliche del fornitore (es. ISO/IEC 27001) e
sulle condizioni contrattuali standard (DPA), secondo PO40.

## 2 Servizi ICT e cloud

| # | Fornitore | Attività svolta per Vectorlab | Critico 9001 | Critico 27001 | Impatto | Dati personali (art. 28 GDPR) | Qualifica | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Aruba S.p.A. | Server dedicato (bare-metal) in data center Aruba, gestito da Vectorlab: siti web aziendali e Ynsera, API e servizi interni, n8n, gestione credenziali, ambienti di sviluppo e demo per i clienti, game server (asset A0011, A0018, A0020, A0022–A0025) | SI | SI | A | SI | DV | Fornitore più critico: tutta l'infrastruttura applicativa è su questo server |
| 2 | Google (Google Workspace / Google Cloud Italy S.r.l.) | Posta elettronica, archiviazione documentale, collaborazione (A0016; dati amministrativi, contratti, personale) | SI | SI | A | SI | DV | DPA standard Google |
| 3 | GitHub, Inc. | Repository del codice sorgente, anche di proprietà dei clienti (A0039) | SI | SI | A | SI | DV | Asset A0039 a criticità 5; trasferimento USA (Data Privacy Framework) |
| 4 | Mango Technologies, Inc. (ClickUp) | Gestione progetti, ticketing, CRM, promemoria (A0014, A0015) | SI | SI | A | SI | DV | Trasferimento USA |
| 5 | Bitwarden, Inc. | Gestione delle credenziali aziendali | NO | SI | B | NO | DV | |
| 6 | Anthropic, OpenAI | Servizi di intelligenza artificiale usati nel lavoro | NO | SI | A | da verificare | DV | Definire quali dati dei clienti possono essere inseriti (AI Act, PO15) |
| 7 | Discord | Messaggistica interna (A0017) | NO | SI | A | SI | DV | Discord non è accettato dal SGI: da sostituire o limitare al canale di emergenza (vedi task ISO) |
| 8 | Fastweb S.p.A. | Connettività internet e telefonia mobile della sede | NO | SI | C | NO | DV | |
| 9 | Bunny.net, GoDaddy | CDN e registrazione domini | NO | SI | C | NO | DV | |
| 10 | iubenda S.r.l. | Gestione cookie e informative del sito | NO | NO | — | SI | DV | |
| 11 | InfoCert / Tinexta InfoCert S.p.A., Namirial S.p.A., Actalis S.p.A. | Firma digitale, PEC, certificati | NO | SI | B | NO | DV | |
| 12 | BrowserStack, Figma | Test su dispositivi, progettazione interfacce | SI | SI | A | da verificare | DV | Possono contenere materiale dei clienti |

## 3 Servizi professionali

| # | Fornitore | Attività svolta per Vectorlab | Critico 9001 | Critico 27001 | Impatto | Dati personali (art. 28 GDPR) | Qualifica | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | Andrei Apostu (libero professionista) | Amministrazione di sistema e gestione IT | SI | SI | A | SI | DV | Servono incarico, accordo di riservatezza (ALPR26.1.B.3) e nomina ad Amministratore di Sistema (ALPO31.A) |
| 14 | Consulenti tecnici esterni (es. Paolo Macco, Simone Ponte, Zona Web S.r.l., V.B. S.a.s., Lucia Tozzi) | Consulenze tecniche | da verificare | da verificare | da verificare | da verificare | DV | Da chiarire se lavorano su progetti dei clienti: in quel caso lo sviluppo è in parte esternalizzato e il controllo 8.30 della SoA non può essere escluso |
| 15 | ABCD Lavoro S.r.l. – S.T.P. | Elaborazione paghe e consulenza del lavoro | NO | SI | A | SI | DV | Dati dei dipendenti |
| 16 | Commercialista / elaborazione contabile (Cerra Alessandro, SMRTAX S.r.l.) | Contabilità e adempimenti fiscali | NO | SI | A | SI | DV | |
| 17 | Nextage S.r.l. | Consulenza per il Sistema di Gestione Integrato, analisi dei rischi (strumento ERA) | SI | SI | A | SI | DV | |
| 18 | 2 SPAM Sicurezza sul Lavoro S.a.s., Sicurnet Liguria S.r.l., medico competente | Supporto alla sicurezza sul lavoro, formazione, sorveglianza sanitaria | NO | NO | — | SI | DV | D.Lgs. 81/2008 |

## 4 Sede e servizi generali

| # | Fornitore | Attività svolta per Vectorlab | Critico 9001 | Critico 27001 | Impatto | Dati personali (art. 28 GDPR) | Qualifica | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19 | San Giorgio Immobiliare S.r.l. | Locazione della sede | NO | SI | C | NO | DV | Sicurezza fisica dell'edificio (PR18.1) |
| 20 | Splash Service S.r.l. | Pulizia dei locali | NO | SI | C | NO | DV | Accesso ai locali: regole per esterni (PR18.1) |
| 21 | Enel Energia S.p.A. / Fastweb energia | Energia elettrica | NO | SI | C | NO | DV | |

## 5 Da completare

Per ogni fornitore critico (Critico 9001 o 27001 = SI) l'Amministrazione,
con il supporto di RSGI, completa:

- valutazione e stato della qualifica (PR26.1);
- accordo di riservatezza (ALPR26.1.B.3) e comunicazione SGSI
  controfirmata (ALPR26.1.A), dove applicabili;
- nomina a responsabile del trattamento (ALPR26.1.D) o DPA del
  fornitore, per chi tratta dati personali per conto di Vectorlab;
- riferimento interno, contatti, SLA e modalità di fine servizio.

Il registro è riesaminato almeno una volta l'anno e a ogni nuovo
fornitore critico.
