# MDPR26.1.B - Elenco fornitori qualificati

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0 | 17/11/2026 | Emissione | RSGI | Da approvare |

## 1 Scopo

Il registro elenca i fornitori ai quali Vectorlab affida attività o
processi che rientrano nel campo di applicazione del Sistema di
Gestione Integrato (attività svolte presso terzi), con la loro
classificazione di criticità secondo [PR26.1](PR26.1%20-%20Gestione%20dei%20fornitori.md). Risponde anche alla
richiesta dell'ente di certificazione di un «elenco delle attività
svolte presso terzi».

I servizi applicativi (es. la piattaforma di automazione n8n, asset A0022)
sono installati e gestiti da Vectorlab sul server dedicato Aruba: la
gestione applicativa è interna, l'infrastruttura fisica e il data center
sono del fornitore (voce 1).

Non sono elencati i fornitori senza impatto sul SGI (ristorazione,
viaggi, cancelleria, acquisti occasionali di attrezzature).
L'anagrafica amministrativa completa è tenuta dall'Amministrazione.

Legenda **impatto sulla sicurezza delle informazioni** ([PR26.1](PR26.1%20-%20Gestione%20dei%20fornitori.md)):

- **A** – accesso diretto alle informazioni di Vectorlab o dei clienti;
- **B** – svolge attività necessarie alla sicurezza delle informazioni senza accedere alle informazioni;
- **C** – non accede alle informazioni ma può introdurre rischi;
- **—** – nessun impatto.

Stato della qualifica: **Q** qualificato, **QR** qualificato con riserva,
**R** respinto, **DV** da valutare. Per i fornitori cloud la qualifica si
basa sulle certificazioni pubbliche del fornitore (es. ISO/IEC 27001) e
sulle condizioni contrattuali standard (DPA), secondo [PR26.1](PR26.1%20-%20Gestione%20dei%20fornitori.md) §6.

## 2 Servizi ICT e cloud

| # | Fornitore | Attività svolta per Vectorlab | Critico 9001 | Critico 27001 | Impatto | Dati personali (art. 28 GDPR) | Qualifica | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Aruba S.p.A. | Server dedicato (bare-metal) in data center Aruba, gestito da Vectorlab: siti web aziendali e Ynsera, API e servizi interni, n8n, gestione credenziali, ambienti di sviluppo e demo per i clienti, game server (asset A0011, A0018, A0020, A0022–A0025) | SI | SI | A | SI | DV | Fornitore più critico: tutta l'infrastruttura applicativa è su questo server. Account intestato a Vectorlab e pagato da Vectorlab; credenziali del pannello all'Amministrazione. Accordo: termini di servizio |
| 2 | Google (Google Workspace / Google Cloud Italy S.r.l.) | Posta elettronica, archiviazione documentale, collaborazione (A0016; dati amministrativi, contratti, personale) | SI | SI | A | SI | DV | Accordo: termini di servizio, con DPA standard Google |
| 3 | GitHub, Inc. | Repository del codice sorgente, anche di proprietà dei clienti (A0039) | SI | SI | A | SI | DV | Asset A0039 a criticità 5; trasferimento USA (Data Privacy Framework). Accordo: termini di servizio |
| 4 | Mango Technologies, Inc. (ClickUp) | Gestione progetti, ticketing, CRM, promemoria (A0014, A0015) | SI | SI | A | SI | DV | Trasferimento USA. Accordo: termini di servizio |
| 5 | Bitwarden, Inc. | Gestione delle credenziali aziendali | NO | SI | B | NO | DV | |
| 6 | Anthropic, OpenAI | Servizi di intelligenza artificiale usati nel lavoro | NO | SI | A | da verificare | DV | Definire quali dati dei clienti possono essere inseriti (AI Act, [PO15](../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni.md)) |
| 7 | Discord | Messaggistica interna (A0017) | NO | SI | A | SI | DV | Discord non è accettato dal SGI e per il lavoro non è ammessa nessuna app di messaggistica ([REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §5, decisione del 04/11/2026): da dismettere |
| 8 | Fastweb S.p.A. | Connettività internet e telefonia mobile della sede | NO | SI | C | NO | DV | |
| 9 | Bunny.net, GoDaddy | CDN, registrazione domini e certificati SSL (GoDaddy) | NO | SI | C | NO | DV | |
| 10 | iubenda S.r.l. | Gestione cookie e informative del sito | NO | NO | — | SI | DV | |
| 11 | InfoCert / Tinexta InfoCert S.p.A., Namirial S.p.A., Actalis S.p.A. | Firma digitale, PEC, certificati SSL dei siti (Actalis) | NO | SI | B | NO | DV | Certificati SSL da Actalis e GoDaddy con abbonamento annuale, ancora necessario; rinnovo automatico (ACME) da verificare (NC01) |
| 12 | BrowserStack, Figma | Test su dispositivi, progettazione interfacce | SI | SI | A | da verificare | DV | Possono contenere materiale dei clienti |

## 3 Servizi professionali

| # | Fornitore | Attività svolta per Vectorlab | Critico 9001 | Critico 27001 | Impatto | Dati personali (art. 28 GDPR) | Qualifica | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | Andrei Apostu (libero professionista) | Amministrazione di sistema e gestione IT | SI | SI | A | SI | DV | Incarico, accordo di riservatezza ([ALPR26.1.B.3](ALPR26.1.B.3%20-%20Accordo%20di%20Riservatezza%20con%20le%20Terze%20Parti.md)) e nomina ad Amministratore di Sistema ([ALPO31.A](../A_CONFORMITA_/ALPO31.A%20-%20Lettera%20incarico%20AdS.md)): da fare |
| 14 | Consulenti tecnici esterni (es. Paolo Macco, Simone Ponte, Zona Web S.r.l., V.B. S.a.s., Lucia Tozzi) | Consulenze tecniche | da verificare | da verificare | da verificare | da verificare | DV | Paolo Macco e Simone Ponte lavorano direttamente con clienti per i quali Vectorlab gestisce solo la parte amministrativa e contabile; gli altri svolgono lavori interni che non rientrano nel campo di applicazione del SGI (Amministrazione, 04/11/2026; confermato da RSGI l'11/11/2026). Il contratto con il cliente è del consulente, non di Vectorlab (confermato da RSGI l'11/11/2026): non è sviluppo affidato all'esterno da Vectorlab e il controllo 8.30 della SoA resta escluso, con questa motivazione |
| 15 | ABCD Lavoro S.r.l. – S.T.P. | Elaborazione paghe e consulenza del lavoro | NO | SI | A | SI | DV | Dati dei dipendenti. Contratto firmato. Ruolo GDPR indicato dall'Amministrazione: titolare autonomo [DA VERIFICARE] |
| 16 | Commercialista / elaborazione contabile (Cerra Alessandro, SMRTAX S.r.l.) | Contabilità e adempimenti fiscali | NO | SI | A | SI | DV | Contratto firmato |
| 17 | Nextage S.r.l. | Consulenza per il Sistema di Gestione Integrato, analisi dei rischi (strumento ERA) | SI | SI | A | SI | DV | Contratto firmato |
| 18 | 2 SPAM Sicurezza sul Lavoro S.a.s., Sicurnet Liguria S.r.l., medico competente | Supporto alla sicurezza sul lavoro, formazione, sorveglianza sanitaria | NO | NO | — | SI | DV | D.Lgs. 81/2008 |
| 22 | Davide Ruzzenenti | RSGI, gestione dei progetti e sviluppo commerciale | SI | SI | A | da verificare | DV | Contratto e accordo di riservatezza: da fare |
| 23 | Francesco Cappetti | Amministrazione e Referente Privacy | SI | SI | A | da verificare | DV | Contratto e accordo di riservatezza: da fare |

## 4 Sede e servizi generali

| # | Fornitore | Attività svolta per Vectorlab | Critico 9001 | Critico 27001 | Impatto | Dati personali (art. 28 GDPR) | Qualifica | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19 | San Giorgio Immobiliare S.r.l. | Locazione della sede | NO | SI | C | NO | DV | Sicurezza fisica dell'edificio ([PR18.1](../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale.md)) |
| 20 | Splash Service S.r.l. | Pulizia dei locali | NO | SI | C | NO | DV | Accesso ai locali: regole per esterni ([PR18.1](../A_SICUREZZA%20FISICA%20AMBIENTALE/PR18.1%20-%20Gestione%20sicurezza%20fisica%20e%20ambientale.md)) |
| 21 | Enel Energia S.p.A. / Fastweb energia | Energia elettrica | NO | SI | C | NO | DV | |

## 5 Da completare

Per ogni fornitore critico (Critico 9001 o 27001 = SI) l'Amministrazione,
con il supporto di RSGI, completa:

- valutazione e stato della qualifica ([PR26.1](PR26.1%20-%20Gestione%20dei%20fornitori.md));
- accordo di riservatezza ([ALPR26.1.B.3](ALPR26.1.B.3%20-%20Accordo%20di%20Riservatezza%20con%20le%20Terze%20Parti.md)) e comunicazione SGSI
  controfirmata ([ALPR26.1.A](ALPR26.1.A%20-%20Comunicazione%20e%20requisiti%20di%20sicurezza%20per%20i%20fornitori.md)), dove applicabili;
- nomina a responsabile del trattamento ([ALPR26.1.D](ALPR26.1.D%20-%20Nomina%20Responsabile%20Trattamenti%20Dati%20Personali.md)) o DPA del
  fornitore, per chi tratta dati personali per conto di Vectorlab;
- riferimento interno, contatti, SLA e modalità di fine servizio.

Il registro è riesaminato almeno una volta l'anno e a ogni nuovo
fornitore critico.

## 6 Valutazione annuale

Sostituisce il vecchio modulo MDPR26.1.A. Una volta l'anno, prima del
Riesame della Direzione, l'Amministrazione con RSGI valuta ogni
fornitore critico con tre voti da 1 a 10:

- **Q** – qualità e affidabilità del servizio (disservizi, errori, supporto);
- **T** – rispetto dei tempi e degli impegni;
- **S** – rispetto dei requisiti di sicurezza e, per i responsabili del
  trattamento, degli obblighi dell'art. 28 GDPR (6 se non ci sono
  requisiti di sicurezza da verificare).

Esito sulla media: 7 o più **qualificato**; da 5 a 6,9 **sotto
osservazione**, con un'azione nella lista «Non conformità e
miglioramento»; sotto 5 **non qualificato**, da sostituire o da
gestire come rischio. Un incidente o una NC causata dal fornitore si
annota nella valutazione dell'anno.

| # | Fornitore | Data | Q | T | S | Media | Esito | Note e riferimenti (NC, incidenti) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | |

