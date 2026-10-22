# MDPO29.C - Elenco leggi, regolamenti e norme applicabili

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0      | 20/10/2026 | Prima emissione: sostituisce il foglio «Compliance» del vecchio elenco Excel MDPR08.1.A (riferimenti superati: ISO/IEC 27001:2013, ISO 9001:2015, ISO/IEC 27002:2017); aggiunte le norme su intelligenza artificiale, cybersicurezza dei prodotti, lavoro agile, trasferimenti di dati extra UE | RSGI | Da approvare |
| 0.1      | 22/10/2026 | Cyber Resilience Act: da «non applicabile» a «da valutare» per i prodotti della unit Vectorlab, esclusi dal campo di applicazione; ISO 9001: indicata la 2015 come norma di certificazione RINA | RSGI | Da approvare |

## 1 Scopo e uso

Il presente registro elenca i requisiti cogenti (leggi e regolamenti) e
le norme volontarie che hanno impatto sul Sistema di Gestione Integrato
di Vectorlab, come previsto da PO29 – Gestione della conformità, §2.1.

Per ogni requisito indica se si applica a Vectorlab, con quali documenti
del SGI viene rispettato e chi ne segue gli aggiornamenti.

- **Applicabile**: il requisito si applica oggi a Vectorlab.
- **Da valutare**: l'applicabilità dipende da attività o clienti
  specifici; va verificata caso per caso (anche con consulenza legale).
- **Non applicabile**: valutato e escluso, con la motivazione.

Il registro è riesaminato da RSGI almeno una volta l'anno, prima del
Riesame della Direzione, e ogni volta che entra in vigore una norma
rilevante o cambia l'attività aziendale. I requisiti contrattuali dei
singoli clienti non sono elencati qui: sono gestiti nei contratti e
nell'offerta (PR09.1, PR26.1).

## 2 Protezione dei dati personali

| Riferimento | Contenuto in breve | Applicabilità | Come lo rispettiamo | Owner |
| --- | --- | --- | --- | --- |
| [Reg. (UE) 2016/679 – GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Regolamento generale sulla protezione dei dati personali | Applicabile: Vectorlab è titolare (personale, clienti, fornitori) e responsabile del trattamento (dati dei clienti nei progetti) | PO30, PO31, PR31.1–PR31.4, MDPR31.4.A/B, informative ALPR31.2.*, PR27.1 (data breach), PR33.2 | Referente Privacy |
| [D.Lgs. 196/2003 – Codice privacy](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196), come modificato dal D.Lgs. 101/2018 | Norme nazionali di adeguamento al GDPR | Applicabile | Come GDPR | Referente Privacy |
| Provvedimento del Garante privacy del 27/11/2008 sugli Amministratori di Sistema, modificato il 25/06/2009 | Nomina, elenco e verifica degli amministratori di sistema; registrazione degli accessi | Applicabile (amministratore di sistema interno ed esterno) | ALPO31.A, ALPO31.C, MDPO29.A, PR16.1, MDPR11.1.M | CTO |
| Linee guida del Garante privacy su cookie e altri strumenti di tracciamento (10/06/2021) | Consenso e informativa per cookie e tracciamento sui siti web | Applicabile (sito aziendale) | ALPR31.2.F | Referente Privacy |
| [Decisione di esecuzione (UE) 2023/1795 – EU-US Data Privacy Framework](https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj) | Trasferimento di dati personali verso organizzazioni certificate negli USA | Applicabile (fornitori cloud con sede o infrastrutture negli USA) | PO40, PR26.1, ALPR26.1.D, registro dei trattamenti | Referente Privacy |
| Linee guida e raccomandazioni EDPB | Interpretazione del GDPR a livello europeo | Riferimento interpretativo | Consultate in caso di nuovi trattamenti o DPIA (PR31.3) | Referente Privacy |

## 3 Lavoro, salute e sicurezza

| Riferimento | Contenuto in breve | Applicabilità | Come lo rispettiamo | Owner |
| --- | --- | --- | --- | --- |
| [D.Lgs. 81/2008 – Testo unico salute e sicurezza](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2008-04-09;81) | Valutazione dei rischi, RSPP, RLS, formazione, emergenze | Applicabile | DVR (gestito da RSPP), PR18.1, MDPR18.1.*, ALPR05.1.A–D | RSPP |
| [L. 300/1970 – Statuto dei lavoratori](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1970-05-20;300), in particolare art. 4 | Limiti ai controlli a distanza sui lavoratori tramite strumenti informatici | Applicabile | REG01, REG02, ALPR31.2.A | HR |
| [L. 81/2017 – Lavoro agile](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2017-05-22;81) | Accordo individuale e sicurezza nel lavoro agile | Applicabile | ALPR05.1.E, ALPR05.1.F | HR |
| [D.Lgs. 24/2023 – Whistleblowing](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-03-10;24) | Canali di segnalazione degli illeciti | Non applicabile: meno di 50 lavoratori e nessun modello 231 adottato | — | HR |

## 4 Cybersicurezza

| Riferimento | Contenuto in breve | Applicabilità | Come lo rispettiamo | Owner |
| --- | --- | --- | --- | --- |
| [D.Lgs. 138/2024 – recepimento direttiva NIS2](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-09-04;138) | Obblighi di sicurezza e notifica per soggetti essenziali e importanti | Non applicabile direttamente: Vectorlab è una piccola impresa, sotto le soglie di dimensione. Clienti soggetti a NIS2 possono imporre requisiti nella catena di fornitura, gestiti come requisiti contrattuali | PR26.1 (lato fornitore), PR27.1 | CISO |
| [Reg. (UE) 2024/2847 – Cyber Resilience Act](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) | Requisiti di sicurezza per prodotti hardware e software con elementi digitali immessi sul mercato UE; segnalazione di vulnerabilità sfruttate e incidenti dal 11/09/2026, applicazione piena dal 11/12/2027 | Non applicabile al servizio nel campo di applicazione (team Ynsera presso i clienti). **Da valutare** per i prodotti della unit Vectorlab (es. Gaia), esclusi dal campo di applicazione ma soggetti all'obbligo di legge se immessi sul mercato UE (rettifica del 22/10/2026) | Valutazione per prodotto, fuori dal SGI | CTO |

## 5 Intelligenza artificiale

| Riferimento | Contenuto in breve | Applicabilità | Come lo rispettiamo | Owner |
| --- | --- | --- | --- | --- |
| [Reg. (UE) 2024/1689 – AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), come modificato dal Reg. (UE) 2026/1744 (Digital Omnibus) | Pratiche vietate e alfabetizzazione del personale (già in vigore); trasparenza art. 50 dal 02/08/2026; sistemi ad alto rischio dell'Allegato III dal 02/12/2027 | Applicabile: Vectorlab sviluppa (fornitore) e usa (deployer) sistemi di IA. Gli obblighi per l'alto rischio vanno valutati per ogni progetto | PO25 (requisiti di progetto), MDPO25.B, formazione MDPR06.1.C | CTO |
| [L. 132/2025 – Disposizioni sull'intelligenza artificiale](https://www.normattiva.it/eli/id/2025/09/25/25G00143/CONSOLIDATED) | Norme nazionali sull'uso dell'IA, anche nel lavoro e nelle professioni | Applicabile | Come AI Act; informativa ai lavoratori sull'uso di sistemi di IA (ALPR31.2.A) | CTO |

## 6 Proprietà intellettuale, servizi digitali, documenti

| Riferimento | Contenuto in breve | Applicabilità | Come lo rispettiamo | Owner |
| --- | --- | --- | --- | --- |
| [L. 633/1941 – Diritto d'autore](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1941-04-22;633) | Tutela del software e dei contenuti; uso di licenze | Applicabile (sviluppo software, uso di librerie e software di terzi) | ALPR05.1.G, PO29 §2.2 (licenze), contratti con clienti (PR09.1) | CTO |
| Codice civile, artt. 2214–2220 | Tenuta e conservazione delle scritture contabili (10 anni) | Applicabile | PR04.1, MDPO15.A | Resp. Amministrazione |
| [D.Lgs. 82/2022 – Accessibilità di prodotti e servizi (European Accessibility Act)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2022-05-27;82) e [L. 4/2004](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2004-01-09;4) | Requisiti di accessibilità per servizi digitali al consumatore e siti della PA | Da valutare: si applica ai prodotti e servizi digitali realizzati per clienti che ricadono nel campo di applicazione (es. e-commerce, PA) | Requisiti di progetto (MDPO25.B) | CTO |
| [Reg. (UE) 2023/2854 – Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj) | Accesso ai dati dei prodotti connessi; passaggio tra fornitori di servizi cloud | Da valutare: solo se Vectorlab fornisce servizi cloud o prodotti connessi | PO40 | CTO |

## 7 Norme volontarie

| Riferimento | Contenuto in breve | Applicabilità | Come lo rispettiamo | Owner |
| --- | --- | --- | --- | --- |
| UNI CEI EN ISO/IEC 27001:2024 + A1:2024 | Sistema di gestione per la sicurezza delle informazioni | Applicabile (certificazione) | Intero SGI, SoA | RSGI |
| ISO 9001:2026 (certificazione RINA sulla ISO 9001:2015, transizione alla prima ricertificazione) | Sistema di gestione per la qualità | Applicabile (certificazione) | Intero SGI | RSGI |
| ISO/IEC 27002:2022 | Linee guida per i controlli di sicurezza | Riferimento per i controlli dell'Annex A | SoA | CISO |
| ISO/IEC 27005:2022 e ISO 31000:2018 | Gestione del rischio | Riferimento per la metodologia | PR33.1, PR33.1.1 | CISO |
| ISO 19011:2018 | Linee guida per gli audit dei sistemi di gestione | Riferimento per gli audit interni | PR11.1 | RSGI |
| OWASP ASVS | Requisiti di verifica della sicurezza delle applicazioni | Riferimento per lo sviluppo sicuro | PO25, MDPO25.A | CTO |
