# Stato progetto: migrazione documentazione SGI su GitHub

Nota di lavoro aggiornata al 2026-07-09. Serve come promemoria per riprendere il lavoro da VS Code senza dover ripercorrere tutta la chat.

## Obiettivo

Spostare la documentazione ISO di Vectorlab da Google Drive (Word/Excel, organizzata in sottocartelle di stato Working/Da Approvare/Ultima Versione/Obsolete) a GitHub in formato Markdown, con MkDocs per la navigazione via browser. Motivazione originale (CTO): avere una visione d'insieme e poter usare un LLM per scovare incongruenze tra documenti.

## Repository

`https://github.com/davideruzzenenti/Vectorlab-SGI.git` — passato a privato il 16/07/2026, poi **tornato pubblico lo stesso giorno** per riavere GitHub Pages attivo (il piano Free non pubblica Pages su repo privati). Sito di nuovo raggiungibile su `davideruzzenenti.github.io/Vectorlab-SGI/`.

## Cosa è stato fatto

1. **Estrazione e consolidamento struttura**: dall'archivio Google Drive (141 file: 91 docx, 34 xlsx, 6 pptx, 2 xlsm, 6 png, 1 file diagrams.net) sono stati eliminati i due alberi paralleli "Master" e "Pubblicato". "Pubblicato" conteneva solo 9 file, tutti copie identiche o più vecchie di quelli in "Master" — scartato, decisione tracciata in `docs/index.md`. Le sottocartelle di stato (Working/Da Approvare/ecc.) sono state eliminate: ora un solo documento per categoria, lo stato/versioning è gestito da Git.

2. **Conversione documenti Word → Markdown** (pandoc): 91 docx + 1 doc legacy (via LibreOffice) convertiti. Problema riscontrato e risolto: 39/92 documenti (42%) usavano in Word liste numerate manuali invece di stili Titolo 1/2/3 veri, quindi pandoc non li riconosceva come intestazioni. Scritto uno script di normalizzazione che usa il sommario automatico di Word (che contiene la numerazione corretta) per ricostruire heading Markdown reali (`## 2.1 Nome sezione`). Ripuliti anche i blocchi di ancore/TOC residui di Word.

3. **File Excel**: tutti e 34 gli xlsx/xlsm convertiti in Markdown (tabelle HTML con `rowspan`/`colspan` per preservare le celle unite — una tabella piatta li avrebbe resi illeggibili, specialmente la SOA). Gli originali xlsx/xlsm sono stati mantenuti accanto ai .md, nessun dato perso.

4. **File non testuali**: pptx, png (inclusi i loghi in `D_GESTIONE PROGETTO/logokit vectorlab`) e i documenti di certificazione RINA mantenuti nativi, non convertiti.

5. **File senza estensione**: `ALPO02.A - Contesto e Processi` era in realtà un diagramma diagrams.net — rinominato con estensione `.drawio`.

6. **Navigazione**: creato un `index.md` per ogni cartella di categoria (26 in totale) con link a tutti i documenti e file della cartella (compresi Excel/PowerPoint/immagini), così tutto è raggiungibile dal menu del sito MkDocs e non solo i file .md.

7. **MkDocs + GitHub Pages**: `mkdocs.yml` (tema material), `requirements.txt`, workflow GitHub Actions (`.github/workflows/deploy-docs.yml`) che builda e pubblica automaticamente su Pages ad ogni push su `main`. Pages configurato su Settings → Pages, sorgente branch `gh-pages`. Sito raggiungibile su `davideruzzenenti.github.io/Vectorlab-SGI/`.

8. **Push**: eseguito dal PC locale di Davide (non dal sandbox — git si è rivelato inaffidabile dentro la cartella OneDrive montata nel sandbox di lavoro, corrompeva `.git/config`; nessun problema previsto lavorando in locale/VS Code).

9. **README.md**: aggiunto un README di repository che spiega cos'è il progetto, come consultare il sito pubblicato e dove trovare lo stato dettagliato (questo file).

## Revisione IA (09/07/2026)

Prima passata di revisione della documentazione assistita da IA (Claude), su richiesta di Davide, con due obiettivi: (a) verificare la coerenza tra la descrizione aziendale di Vectorlab e la reale struttura organizzativa (una realtà di piccole dimensioni, con più ruoli concentrati sulle stesse persone), e (b) individuare incongruenze/problematiche interne alla documentazione ISO in vista dell'audit di certificazione. Le modifiche sono state discusse e approvate da Davide prima di essere applicate.

**Analisi**: due sub-agent di sola lettura hanno esaminato l'intero mansionario, le politiche di sistema, i documenti privacy/GDPR, la procedura di audit interno e l'organigramma (estratto da `ALPO01.A - Organigramma.pptx`), individuando diverse incongruenze tra la documentazione (impostata su un modello di governance da azienda strutturata: CDA collegiale, ruoli distinti, segregazione formale dei compiti) e la realtà effettiva (azienda a socio unico e amministratore unico, con ruoli molto concentrati).

**Modifiche applicate** (tutte in Rev. 0.1 dei documenti toccati, con relativa riga di storico revisione):

- **CDA → Amministratore Unico**: corretta la definizione dell'acronimo "CDA" in `PO01` e nel `Mansionario` (`ALPO01.B`), chiarendo che le funzioni attribuite a questo organo sono in realtà esercitate dall'Amministratore Unico, coerentemente con la forma societaria dichiarata — evita che un audit richieda verbali di un consiglio collegiale che non esiste.
- **Descrizione aziendale** (`PO01`, Sez. 3 "Vectorlab"): arricchita con settori, tecnologie e approccio operativo, aggiunto un paragrafo che descrive la struttura organizzativa come volutamente snella e orizzontale, per allinearla al linguaggio già usato altrove nel SGI (PO02, Mansionario) a giustificazione della concentrazione dei ruoli.
- **RSPP**: allineato come ruolo interno (coerente con l'organigramma) in `REG02` e in `PR20.1`; prima veniva descritto in alcuni punti come consulente esterno, in contraddizione con l'organigramma stesso.
- **DPO vs Referente Privacy**: chiarito in `PO31`, `PR31.4` e `ALPO31.D` che Vectorlab non rientra nei casi di designazione obbligatoria del DPO (art. 37 GDPR) e che il Referente Privacy opera in autonomia, con il DPO coinvolto solo se e quando eventualmente nominato.
- **Audit interno** (`PR11.1`): reso obbligatorio, non solo raccomandato, il ricorso a un auditor esterno per le aree di cui RSGI è anche responsabile operativo (Business Development, Innovation & Research Projects), per evitare l'auto-audit vietato dalla procedura stessa.
- **Riferimento dimensionale** (`PO02`): rimosso il numero esplicito di persone del team (generalizzato in "struttura snella e compatta"), risolvendo anche una discrepanza numerica con l'organigramma.
- **Mansionario**: aggiunte le schede mancanti per RSPP e Referente Privacy (citati altrove ma senza scheda propria) e una nota di chiarimento su "Responsabile di Area" come termine trasversale, non ruolo distinto.
- **Pulizia placeholder**: corretto un dominio email residuo di un altro template ("nextage-on.com" → "vectorlab.it") in `REG02` e `PR20.1`; risolto un riferimento di ruolo non deciso ("RSGI/CISO???XXXXXX") in `PR05.1`; compilata una data di revisione mancante in `PR31.3`; corretto un indirizzo PEC con nome di un'altra azienda in `ALPR26.1.B.3` (**da verificare**: l'indirizzo PEC reale di Vectorlab non era noto, inserito un placeholder plausibile da confermare).

**Punti aperti non toccati in questa passata**:

- La nota "È UN ESEMPIO va FATTO AD HOC" nello slide di `ALPO02.A - Contesto e Processi.pptx` non è stata rimossa (file PowerPoint, modifica non affidabile in questa sede).
- Diversi placeholder "XXX"/"Area XXXX" in moduli/piani (`MDPR11.1.A/B/C`, Piano della Comunicazione, Piano di Capacità, contratti/NDA fornitori) sono stati lasciati intenzionalmente: sono campi di template da compilare caso per caso, non errori.
- Le nuove righe di revisione (0.1) riportano "Approvato: Amministratore Unico" in modo formale/documentale; l'approvazione sostanziale da parte di Davide/Andrea resta comunque da dare a mente fredda leggendo i diff.

## Integrazione SOA con export ERA (16/07/2026)

Luca Corradi ha condiviso un export CSV (`era-control-vect.csv`, salvato in `docs/02_SOA/` come riferimento) dallo strumento "ERA" usato dal team per compilare la Dichiarazione di Applicabilità ISO 27001/27002, con l'obiettivo di far coincidere questo lavoro con la SOA già presente nel repo (`docs/02_SOA/SOA - Statement of Applicability...md`).

**Scoperta importante**: la SOA nel repo non era un template vuoto (come inizialmente ipotizzato) — ha già per ogni controllo i riferimenti ai documenti, una tassonomia di attributi ISO 27002:2022 (tipo di controllo, proprietà CIA, concetti Cybersecurity, domini di sicurezza, mappatura ai processi) e un'intera sezione aggiuntiva "AGID CSP-SAAS" (requisiti di qualificazione cloud per la PA) assenti dal CSV. Il CSV, al contrario, non ha riferimenti a documenti né tassonomia, ma aveva note testuali compilate per **tutti** i 93 controlli, mentre la SOA le aveva solo per ~20 controlli (soprattutto nella sezione tecnologica, con note operative dirette tipo "Francesco gestisce tutti i profili").

**Integrazione fatta** (via script Python, poi rimosso, non uno strumento permanente): per ogni controllo con nota vuota nella SOA, importata la nota del CSV (usando il campo giusto a seconda che il controllo fosse marcato applicabile o meno), senza toccare le note già presenti, i riferimenti documentali, gli attributi o la sezione AGID. Puliti anche i problemi di codifica (mojibake) presenti nel CSV originale. Per i 3 controlli che il CSV segna come non applicabili (7.12 Cablaggi, 8.11 Mascheramento dati, 8.30 Sviluppo esterno) è stata compilata anche la colonna "Motivo Esclusione".

**Non ancora fatto (prossimo passo)**: alcune note appena importate sono in contraddizione con i riferimenti documentali già presenti nella stessa riga della SOA — es. il controllo 5.35 "Riesame indipendente" dice ancora "non è ancora formalizzato" pur citando `PR11.1 - Audit Interno`, che è invece una procedura già matura; probabile anche per 5.12/5.13 (Classificazione) rispetto a `PO15`. Vanno riconciliati controllo per controllo, verificando il contenuto reale dei documenti citati (non solo la loro esistenza — es. i moduli "MD" sono spesso form vuoti, mentre le "PO"/"PR" sono policy sostanziali).

## Revisione completa di maturità documentale (16/07/2026)

Su richiesta di Davide, revisione dell'intero corpus (non solo i file già toccati in precedenza): per ogni documento esistente, valutazione se è contenuto reale compilato da Vectorlab, un template ancora vuoto (normale prima del primo uso), un boilerplate generico mai adattato dal consulente, o un documento con difetti concreti da correggere. Confrontato anche l'elenco "Riferimenti a Informazioni Documentate" della SOA con i file realmente presenti, per capire quali documenti sono citati ma non sono mai stati creati.

**Risultato**: `docs/STATO-DOCUMENTAZIONE.html` — dashboard con tabella filtrabile di 114 documenti valutati, i 10 problemi con impatto maggiore, i 33 documenti citati ma mai creati (in gran parte l'intero blocco tecnologico: gestione accessi, crittografia, minacce/vulnerabilità, sviluppo sicuro, reti, configurazioni, patch), e per ogni voce chi deve intervenire (IA in autonomia / misto / serve input umano). Spostato dentro `docs/` (e non alla root) apposta perché MkDocs/Pages lo includano nel sito pubblicato: raggiungibile su `davideruzzenenti.github.io/Vectorlab-SGI/STATO-DOCUMENTAZIONE.html` (non compare nel menu di navigazione, solo via link diretto).

**In sintesi**: 24 documenti pronti così come sono, 40 template vuoti normali da popolare, 44 con difetti concreti (placeholder mai risolti, riferimenti incrociati rotti tra documenti, contraddizioni interne), 33 mai creati. I problemi più seri: `PO20` ha l'80% del testo che parla di Gestione delle Configurazioni invece che di Capacità (copia-incolla sbagliato dal template); `PR27.1` e i suoi allegati trattano il DPO come obbligatorio, contraddicendo la revisione già fatta su `PO31`; i moduli di emergenza fisica (`MDPR18.1.F/G/H`) hanno ancora "Nome Cognome" non compilato (gap di conformità D.Lgs 81/08, non solo carta); sospetti residui di un altro cliente del consulente (date "05/2009" e "15/03/2021", "NOME AZIENDA" al posto di Vectorlab in più atti) da verificare.

## Generazione bozze documenti mancanti e correzioni (16/07/2026, stessa giornata)

Su richiesta di Davide, dopo aver discusso l'approccio: generate le bozze di tutti i documenti risultati mancanti nella revisione precedente, corrette le contraddizioni già identificate, aggiornato l'elenco documenti e la dashboard.

**Standard adottato per le bozze**: niente lorem ipsum. Contenuto reale e verosimile basato sui fatti già noti nel repository (stack AWS/Aruba/Google Workspace/GitHub, testo già reale della SOA, documenti "fratelli" già maturi), con un banner blu "DOCUMENTO IN BOZZA" in cima a ogni file generato e le frasi/parametri assunti evidenziati con `<span style="color:#B3392A">[DA CONFERMARE: ...]</span>` nel testo. Tutti i documenti generati sono in Rev. 0.1, "Redatto: IA", "Approvato: Da approvare".

**Esecuzione**: 7 sub-agent in parallelo (uno per gruppo tematico), ciascuno con lo stesso standard di marcatura e un elenco di fatti verificati da cui partire, per mantenere coerenza senza dover rileggere tutto a mano. Generati 36 documenti (contando anche i 4 template Firewall/PC/Router/Switch di MDPR32.1.A come file separati). Non generato solo REG03 (vedi sotto, chiarimento inatteso).

**Correzione importante prima di generare**: confrontando i codici mancanti con `MDPR08.1.A - Elenco Informazioni documentate` (che aveva già righe segnaposto per quasi tutti questi documenti, con la cartella "ufficiale" prevista dal consulente), sono emerse cartelle diverse da quelle inizialmente create. Rinominate per coerenza:
- `A_CONTROLLO ACCESSI` → `A_ACCESSI`
- PO17 spostato dalla cartella Asset&Configurazione in una cartella propria `A_CRITTOGRAFIA`
- `A_MINACCE E VULNERABILITA` → `A_MINACCE & VULNERABILITA_`
- `A_PROGETTAZIONE E SVILUPPO SICURO` → `A_PROGETTAZIONE & SVILUPPO SICURO`
- `A_SICUREZZA SISTEMI E RETI` → `A_SICUREZZA SISTEMI & RETI`
- `A_GESTIONE COMMERCIALE` → `8.2_PRODOTTI & SERVIZI`

**Scoperta inattesa**: REG03, che si ipotizzava riguardasse il lavoro agile, secondo l'elenco documenti è in realtà un "Regolamento accesso esterni" (processo Sicurezza Fisica e Ambientale). Non generato: da decidere con la Direzione se serve, dato che il lavoro agile è già coperto da `ALPR05.1.E/F`.

**Altra scoperta**: l'elenco documenti cita `PR33.1` due volte, con due metodologie diverse (analisi rischio SGSI/SGCO/SGS completa, e una versione HLS semplificata) — è stato generato un solo documento con la metodologia principale; da verificare se ne serve un secondo.

**Correzioni applicate ai documenti esistenti** (13 punti, tutti in nuova riga di revisione): riferimenti a documenti inesistenti corretti in `PR12.1`, `PO27`, `PR27.1` (MDPR10.1.C→MDPR10.1.B, PR A16.1→PR27.1, MDPR31.5.A→MDPR27.1.A); chiarito che il DPO non è obbligatorio (coerente con `PO31`) in `PR27.1`, `ALPR27.1.B`, `MDPR27.1.A`; corretto "NOME AZIENDA"→Vectorlab in `ALPO31.A`; aggiunta tabella Revisioni mancante in `ALPO31.D`; sistemati riferimenti incrociati invertiti in `MDPR05.1.V`; rimossi placeholder residui in `MDPR06.1.E`, `MDPR11.1.N` (errore Excel `#DIV/0!`), `PO15`; aggiunta l'introduzione mancante in `PR11.1`; segnalato come non applicabile (non più orfano) il registro CED in `MDPR18.1.B`; riconciliate le note della SOA sui controlli 5.12 e 5.35 (ora rimandano a `PO15`/`PR11.1` invece di contraddirli) e compilato il campo "Controlli Non Applicabili" in copertina.

**Elenco documenti** (`MDPR08.1.A`): compilate le colonne Rev./Data/Cartella per tutti i documenti generati, aggiunte 4 righe che mancavano del tutto (MDPR23.1.A, PR06.1, MDPO29.D, PR28.2).

**Dashboard**: `docs/STATO-DOCUMENTAZIONE.html` aggiornata — i 36 documenti generati sono ora tracciati con stato "Nuovo (bozza IA)" invece che "mancante"; le 13 righe corrette aggiornate; KPI ricalcolati (150 documenti totali, 32 pronti, 44 template vuoti, 32 da correggere, 36 nuovi, 1 ancora da creare/decidere: REG03).

**Non ancora fatto**: `PO20` (contenuto sbagliato, parla di Configurazioni invece che Capacità) e `REG01` (5 codici diversi per lo stesso regolamento) restano da correggere — erano marcati "misto" (serve una decisione, non solo una correzione meccanica), non toccati in questa passata.

**Correzione dashboard (stesso giorno, dopo un feedback di Davide)**: la colonna "Cosa serve" (rinominata "Domanda aperta") e la sezione "Chi deve fare cosa" erano scritte in forma dichiarativa invece che come vere domande — non risultavano riconoscibili come tali. Riscritte tutte le 88 righe della tabella che richiedono un input umano/misto come domande esplicite (es. "Qual è l'indirizzo PEC reale...?"), oltre ai 4 punti della sezione "Umano" in alto. Verificato con `node --check` e un `eval` con DOM stubbato che l'array JS resti valido e che ogni riga non-IA abbia una domanda con punto interrogativo.

## Allineamento con Drive (19/10/2026)

Decisione di Davide: il repo è la destinazione finale del SGI; Drive serve solo finché Nextage ci lavora e poi verrà eliminato. Sul contenuto vince la versione più recente di Nextage su Drive.

**Inventario** della cartella "Vectorlab SGI - Master" (166 file) confrontata con il repo per codice documento. Confronto completo in `confronto-drive-repo-2026-10-19.csv` (consegnato a Davide in chat, non nel repo).

**Importati in questo ramo** (`allineamento-drive-2026-10-19`), convertiti da Word/Excel con pandoc e openpyxl:
- 27 documenti per cui Drive aveva una versione Nextage successiva a luglio: sostituiscono le bozze IA del 16/07 (blocco accessi, crittografia, minacce e vulnerabilità, sviluppo sicuro, configurazioni, patch, reti, conformità, PR33.1, PR03.1, PR04.1, PR09.1, MDPR08.1.A).
- 13 documenti presenti solo su Drive: PR29, PR33.1.1, MDPR33.1.A/B/D (modelli), MDPO25.D/E/G, MDPO29.A (sostituisce la bozza IA MDPO29.D, stesso documento), MDPR23.2.A (modello e registrazione del 27/07), modulo RINA firmato (PDF) e versione corretta.
- Nuova cartella `B_REGISTRAZIONI/Analisi dei Rischi/2026`: report analisi dei rischi e piano di trattamento 2026 (Nextage, 25-29/09).
- Aggiornati i 23 link della SOA verso documenti che hanno cambiato nome.

**Non importato**: MDPO25.F - Definizione UI-UX [progetto] (16 MB, oltre il limite di download del connettore Drive): da copiare a mano.

**Rilevato durante l'inventario**: su Drive 164 file su 166 sono in "0_Working"; "Da Approvare" e "Ultima Versione" sono vuote, quindi nessun documento risulta formalmente approvato. 12 documenti importati riportano ancora "Approvato: CDA" invece di Amministratore Unico.

**Non toccati** (decisione rinviata): le 27 correzioni IA di luglio su documenti che Drive non ha più modificato restano nel repo, da approvare; PR06.1, PR28.2, ALPR26.1.D e ALPR23.2.A sono bozze IA senza corrispettivo su Drive.

**Dashboard aggiornata** (stesso giorno): `STATO-DOCUMENTAZIONE.html` ora traccia le versioni Nextage al posto delle bozze IA (161 documenti: 37 pronti, 62 template, 51 da correggere, 5 boilerplate, 4 bozze IA, 2 mancanti). Aggiunto il valore "Nextage" nella colonna "Chi agisce" per le correzioni da chiedere a Nextage su Drive (es. «Approvato: CDA»), e lo stato "Mancante" per MDPO25.F. Le righe importate sono state valutate da tabella revisioni, segnaposto e inizio del testo, non da una rilettura integrale. Emersi: la PEC reale vectorlab@legalmail.it dal modulo RINA firmato (da confermare per ALPR26.1.B.3); PR33.1.1 è la metodologia HLS semplificata, quindi non serve un secondo PR33.1; report e piano di trattamento dei rischi 2026 riportano una revisione 0.0 del 24/04/2026, precedente all'analisi stessa.

## Revisione dei documenti dello stage 1 (20/10/2026)

Metodo deciso da Davide: un documento alla volta, nell'ordine della lista stage 1 di Nextage (mail del 07/10/2026). Claude scrive le modifiche direttamente nella copia del repo sul Desktop di Davide; Davide fa commit e push. Ogni sessione aggiorna anche `docs/STATO-DOCUMENTAZIONE.html` (sezione «Avanzamento stage 1») e il task ClickUp «ISO» nella lista Task Davide, che raccoglie le cose da fare. Tutto ciò che è corretto resta «Da approvare»: l'approvazione dell'Amministratore Unico è prevista in un'unica sessione a fine stage 1, con mail di conferma come evidenza.

**Dati confermati**: sede Piazza Borgo Pila 39/22, piano 8, 16129 Genova (dati comunicati a Innovares per il bando SPAIC, settembre 2026; CAP corretto in CCIAA con variazione anagrafica). Visura su Drive del 26/06/2025, superata: richiesta una nuova a Francesco (Backlog Amministrazione). Andrei Apostu (IT) è libero professionista esterno; Francesco Cappetti è Referente Privacy; i 7 sviluppatori sono dipendenti; i progetti di ricerca rientrano nel campo di applicazione.

**Fatto**:
1. Campo di applicazione: PO02 §4 riscritto (9001:2026 + 27001:2024+A1:2024, testo uguale alla domanda RINA, sede, aree, confini cloud, esclusioni); PO01 §6 allineato; indirizzo completato in ALPR05.1.A, MDPR05.1.S/T, PR18.1.
2. Politica PO01 (rev 0.2): impegni su obiettivi, requisiti applicabili e miglioramento; comunicazione della politica; DPO allineato a PO31.
3. Organigramma ALPO01.A (rev 0.1) e Mansionario ALPO01.B (rev 0.2): Amministratore Unico, IT esterno, Referente Privacy, misure compensative per i ruoli concentrati.
4. PR33.1 (rev 0.1), report e piano rischi 2026 (rev 0.1): archivio, approvazione, frequenza annuale, date di emissione, campo, owner.

5. SoA (rev 0.4–0.5): compilati Applicabile/Applicato e motivi di inclusione per i 93 controlli dall'export ERA (`docs/02_SOA/era-control-vect.csv`, verificato con screenshot ERA del 20/10: Plan/Do/Check invariati); rimossa la sezione AGID CSP-SAAS (residui di un altro cliente). La SoA è gestita da Nextage in ERA: il repo ne è una copia.
6. Elenco informazioni documentate: generato in automatico dal repo con `tools/genera_elenco.py` (anche nella pipeline prima della pubblicazione); PR08.1 rev 0.2 adeguata a repository privato sul server aziendale e approvazione tramite tabella Revisioni (decisione Davide: il repo resta pubblico per ora, ma i documenti si scrivono come se fosse già spostato e privato).

7. Elenco leggi e regolamenti: nuovo registro `MDPO29.C` (27 riferimenti, verificati il 20/10/2026: AI Act come modificato dal Reg. UE 2026/1744, L. 132/2025, Cyber Resilience Act con segnalazioni dal 11/09/2026, NIS2 non applicabile direttamente per dimensione); PO29 rimanda al registro; corretti i codici sbagliati in PR05.1 (MDPO29.B → MDPR31.4.A) e PR18.1 (MDPO29.D → MDPO29.A).

8. Attività svolte presso terzi: compilato `MDPR26.1.B - Elenco fornitori qualificati` (21 voci dai fornitori del foglio «Elenco Fornitori» del Resoconto Finanziario 2026 e dall'inventario asset), che PR26.1 rev 0.1 indica anche come elenco delle attività presso terzi. Cyber Resilience Act dichiarato non applicabile in MDPO29.C: Vectorlab fa solo consulenza e sviluppo software B2B, non vende prodotti software (Davide, 20/10/2026).

10. Pianificazione audit interni: `MDPR11.1.A` rev 0.1, programma triennale 2026–2028; audit 2026 completo nella settimana 23–27/11 con auditor esterno (da incaricare), Riesame della Direzione entro la prima settimana di dicembre.

**In attesa (20/10/2026)**: risposte di Andrei sull'infrastruttura (il server Vectorlab con n8n gira probabilmente su AWS; AWS non compare nell'anagrafica fornitori). Domande nel task ClickUp «ISO». Bloccano il documento 9 (schema ICT) e il completamento di MDPR26.1.B, PR21.1, PR16.1, PR24.1. Serve anche una planimetria o foto dell'ufficio per ALPR18.1.A.

**Infrastruttura (20/10/2026, pomeriggio)**: l'IT esterno indica un unico server dedicato Aruba (nessun AWS; conferma attesa da Francesco/Amministrazione prima di correggere i documenti che citano AWS). Le debolezze tecniche emerse e le azioni prioritarie prima dell'audit interno sono nel task ClickUp «ISO», volutamente non nel repo finché è pubblico. Lo schema ICT è tenuto fuori dal repo per lo stesso motivo.

**Emerso**: PR34.1/PR35.1/PR36.1 (procedure dei processi principali) citate ma inesistenti; piano di trattamento 2026 con tutti i rischi accettati senza azioni (da discutere con Nextage); nel modulo RINA il civico del sito è «39/2» invece di 39/22.

**Attenzione ai nomi file**: nel terminale Windows le lettere accentate appaiono come «├á»: è solo visualizzazione (`git config core.quotepath false`, `chcp 65001`), i file non vanno rinominati.

## Cose da sapere / limiti noti

- **Qualità conversione Excel**: fogli semplici (liste, registri) vengono puliti; fogli con layout complesso (es. copertina della SOA) restano leggibili ma non identici all'originale — limite fisiologico di qualunque conversione tabella libera → tabella strutturata. Originali sempre disponibili come fallback.
- **GitHub Pages su repo privato**: richiede piano GitHub Pro (a pagamento) o organizzazione Enterprise Cloud — su piano Free personale Pages funziona solo su repo pubblici. Da tenere a mente quando si passa al repo aziendale privato.
- **Stili Word**: se il CTO continua a revisionare/creare documenti, conviene usare gli stili Titolo 1/2/3 nativi di Word (non liste numerate manuali) così le prossime conversioni avranno heading puliti senza bisogno di normalizzazione a posteriori.

## Prossimi passi

- [x] Push finale delle conversioni Excel
- [ ] Rileggere con calma le modifiche della "Revisione IA (09/07/2026)" e confermarle (o correggerle) come vere e proprie approvazioni documentali
- [ ] Verificare l'indirizzo PEC reale di Vectorlab da inserire in `ALPR26.1.B.3` al posto del placeholder
- [ ] CTO prosegue la revisione dei documenti mancanti (era arrivato a "A_Asset e configurazione")
- [x] Integrare l'export CSV di ERA nella SOA del repo (fatto il 16/07/2026, vedi sezione dedicata sopra)
- [x] Riconciliare le note appena importate nella SOA con i riferimenti documentali già presenti (fatto il 16/07/2026: 5.12 e 5.35 corretti, vedi sezione dedicata sopra)
- [x] Repo tornato pubblico (16/07/2026) per riavere Pages attivo, dopo una breve parentesi privata
- [x] Generare le bozze dei 33 documenti mancanti citati nella SOA/Elenco (fatto il 16/07/2026: 36 file generati, solo REG03 lasciato in sospeso — vedi sezione dedicata sopra)
- [ ] Rivedere una per una le 36 bozze generate dalla IA e confermarle/correggerle (contenuti evidenziati in rosso "DA CONFERMARE" da verificare, poi passare lo stato revisione da "Da approvare" a una revisione formale)
- [ ] Decidere se serve davvero `REG03` ("Regolamento accesso esterni", non generato) dato che `ALPR05.1.E/F` coprono già il lavoro agile
- [ ] Decidere se serve un secondo `PR33.1` per la metodologia "HLS semplificata" citata nell'Elenco, o se è solo una nota interna al documento esistente
- [ ] Correggere `PO20` (contenuto sbagliato, parla di Capacity Management ma tratta Configuration Management)
- [ ] Correggere `REG01` (citato con 5 codici diversi e tutti inesistenti nell'Elenco, da uniformare)
- [ ] Verificare se ci sono davvero residui di un altro cliente del consulente (date sospette, "NOME AZIENDA" al posto di Vectorlab)
- [ ] Fase 2 (idea originale del CTO, non ancora iniziata): usare un LLM di grosse dimensioni per scandagliare il corpus consolidato e individuare incongruenze tra documenti — ora fattibile perché tutto è in un unico formato strutturato e ragionevolmente pulito
