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

10. Pianificazione audit interni: `MDPR11.1.A` rev 0.1, programma triennale 2026–2028; audit 2026 completo nella settimana 23–27/11 con auditor esterno (da incaricare; poi fissato al 25–26/11, vedi sotto), Riesame della Direzione entro la prima settimana di dicembre.

**In attesa (20/10/2026)**: risposte di Andrei sull'infrastruttura (il server Vectorlab con n8n gira probabilmente su AWS; AWS non compare nell'anagrafica fornitori). Domande nel task ClickUp «ISO». Bloccano il documento 9 (schema ICT) e il completamento di MDPR26.1.B, PR21.1, PR16.1, PR24.1. Serve anche una planimetria o foto dell'ufficio per ALPR18.1.A.

**Infrastruttura (20/10/2026, pomeriggio)**: l'IT esterno indica un unico server dedicato Aruba (nessun AWS; conferma attesa da Francesco/Amministrazione prima di correggere i documenti che citano AWS). Le debolezze tecniche emerse e le azioni prioritarie prima dell'audit interno sono nel task ClickUp «ISO», volutamente non nel repo finché è pubblico. Lo schema ICT è tenuto fuori dal repo per lo stesso motivo.

**Emerso**: PR34.1/PR35.1/PR36.1 (procedure dei processi principali) citate ma inesistenti; piano di trattamento 2026 con tutti i rischi accettati senza azioni (da discutere con Nextage); nel modulo RINA il civico del sito è «39/2» invece di 39/22.

**Attenzione ai nomi file**: nel terminale Windows le lettere accentate appaiono come «├á»: è solo visualizzazione (`git config core.quotepath false`, `chcp 65001`), i file non vanno rinominati.

## Procedure dei processi principali (21/10/2026)

Metodo: skill `procedura-processo-sgi`, intervista una domanda alla volta (preferenza di Davide).

**PR35.1 Digital** (rev 0.0, da approvare), in `docs/8.2_PRODOTTI & SERVIZI/`. Modello reale: Vectorlab vende un team qualificato inserito nel progetto del cliente, a giornata, dopo uno studio; il team usa strumenti e processo del cliente. Decisioni: offerta firmata = riesame requisiti; task Prospect = scheda commessa (commento di avvio e di chiusura, nuovo stato «finito» da creare); PM = responsabile di commessa; capacity planner per l'allocazione (niente tracciamento ore); regole su dati e codice del cliente: prima NDA e clausole del cliente, poi solo strumenti aziendali approvati; form di fine commessa (da far realizzare ad Andrei). In sospeso: strumenti di IA autorizzati (Claude su piano individuale usato da Davide e Francesco; GitHub Copilot «Copilot Max» su account personale `vectorlab-developer` condiviso dai programmatori). Da riallineare: PO25, che descrive ambienti di quality, team di test e PC Ubuntu non esistenti.

Visura camerale aggiornata (estratta il 09/09/2026) ricevuta: conferma sede 39/22, CAP 16129, piano 8.

## Campo di applicazione e procedura commerciale (22/10/2026)

- **Campo di applicazione**: deciso di certificare solo il servizio della business unit **Ynsera** (team di Vectorlab inseriti nei progetti dei clienti, a giornata). Esclusi la unit Vectorlab (prodotti per aziende, es. Gaia), la partecipazione a bandi e i progetti di ricerca; si potranno aggiungere con un'estensione del certificato. Il testo inviato a RINA resta invariato. Aggiornati PO02 §4.2/§4.4 (rev 0.3), PO01 §3.3/§6 (rev 0.3), PR35.1 (rev 0.1), MDPR11.1.A (rev 0.2).
- **PR09.1 Gestione Commerciale** (rev 0.1): riscritta sul processo reale e limitata a Ynsera; assorbe PR36.1, mai emessa. PR34.1 non serve più.
- **MDPO15.A** (rev 0.1): registro di conservazione compilato per tutti i processi; casella email dei cessati 6 mesi; durata dei backup da decidere con l'IT.
- **ISO 9001**: documenti impostati sulla 2026; indicata la 2015 come norma di certificazione RINA (PO01, PO02, MDPO29.C, MDPR11.1.A).
- **MDPO29.C** (rev 0.1): Cyber Resilience Act da valutare per i prodotti Vectorlab, fuori dal campo ISO.
- Aperti: condizioni generali nel modello di preventivo Ynsera (revisione legale); contratti Ynsera come appalto di servizi; comunicazione a Nextage.

## Obiettivi, rischi, personale (22/10/2026, pomeriggio)

- **MDPO03.A Lista Obiettivi** (rev 0.1): 6 obiettivi 2026–2027 approvati da Davide (certificazione, accessi sicuri, backup, soddisfazione clienti, formazione, processo commerciale).
- **MDPR33.1.B** (rev 0.2): owner di immagine e reputazione = Amministratore Unico; «1.23» → 5.23. Rischio Copilot da inserire in ERA con Nextage.
- **PR05.1** (rev 0.3): gestione della casella email dell'uscente secondo il Garante (04/12/2019).
- **PR13.1** (rev 0.1): registro delle non conformità = lista ClickUp «Non conformità e miglioramento» (creata il 22/10, cartella SGI); stati e campi da configurare a mano.
- **PR11.1** (rev 0.3) e **PR12.1** (rev 0.2): allineate al registro NC in ClickUp, ai codici corretti dei documenti sui rischi e degli obiettivi, al campo di applicazione.
- Utenze: 10 account Google Workspace (verifica in due passaggi: vedi riunione del 18/11); 4 interni in ClickUp con Gmail personale (task di correzione creato in ClickUp, scadenza 30/10).

## Incidenti e prima non conformità (23–24/10/2026)

- Prima NC registrata nella lista ClickUp: certificato SSL *.vectorlab-cg.com scaduto il 21/10 (n8n e sito Ynsera con problemi, nessun cliente coinvolto); causa: mancato passaggio di informazioni tra acquisto (Amministrazione) e installazione (IT esterno).
- **PR27.1** (rev 0.2) e **PR13.1**: segnalazioni a sicurezza@vectorlab-cg.com (gruppo Google da creare); incidenti registrati nella lista NC con Origine = Incidente.
- PO25 in attesa delle risposte del CTO (task ClickUp con 6 domande); sviluppatori su PC personali Windows.
- Informative privacy ALPR31.2.A–G e PR31.1: titolare Vector Lab S.r.l. con P.IVA, privacy@vectorlab-cg.com (gruppo Google), PEC vectorlab@legalmail.it. Gruppo sicurezza@vectorlab-cg.com creato il 24/10.
- Privacy semplificata (24/10, rivista il 26/10): le informative restano solo nel repo SGI; ALPR31.2.A–G (rev 0.1) hanno tabella delle revisioni e riga «Consegna». Le altre informative si consegnano nelle rispettive occasioni.

## Verifica sui testi di norma e NC certificati (26/10/2026)

- **Testi di norma letti dai PDF UNI** (cartella Drive «NORME ISO»). Edizione da citare per la 27001: **UNI CEI EN ISO/IEC 27001:2024+A1:2024**, recepimento della EN ISO/IEC 27001:2023+A1:2024, ratificata dal Presidente UNI il 07/10/2024 ed entrata nel corpo normativo nazionale il 16/10/2024. In 27001 il punto 10.2 si scrive «Nonconformità e azioni correttive» (una parola); in 9001 «Non conformità e azioni correttive» (due).
- **Attenzione**: «ISO/IEC 27001:2022» non è un errore — è l'edizione ISO originale, di cui la UNI CEI EN è il recepimento italiano. Nel repo convivono le due forme (16 occorrenze della prima su 5 documenti: MDPO03.A, REG01, PR09.1, PR35.1, MDPR11.1.D). Da uniformare per scelta, non per correzione.
- **PR13.1 rev 0.2**: aggiunta la verifica dell'efficacia alle fasi delle NC di produzione-progettazione (§2.1), reclami e segnalazioni clienti (§2.2) e fornitura (§2.3). Prima era prevista solo per le NC di processo, mentre 27001 10.2 e 9001 10.2.1 d) la richiedono per ogni azione correttiva. Stato «Da approvare».
- **PO27**: il rimando rotto a «PR A16.1» risulta già corretto in rev 0.1 (16/07/2026). Il Drive è indietro su questo documento.
- **NC certificati, aggiornamento**: i certificati li ha ricaricati Andrea (Amministratore Unico e CTO) previo confronto con Andrei; servizi ripristinati. La correzione è fatta, l'azione correttiva no. Causa confermata: il passaggio acquisto (Amministrazione) → installazione (IT) non ha proprietario né scadenza presidiata. Registrazione del 23/10 eliminata e ricostruita il 26/10 come NC01 nella lista «Non conformità e miglioramento» (stato «azione in corso»). Azioni: proprietario unico del ciclo di vita (Andrei), task ClickUp al posto dei passaggi su Telegram, rinnovo automatico ACME, allarme a 30 giorni indipendente da n8n, certificati nell'inventario asset. Contesto: ballot CA/Browser Forum SC-081v3, durata massima dei certificati TLS pubblici 200 giorni dal 15/03/2026, 100 dal 15/03/2027, 47 dal 15/03/2029.
- **Da verificare**: organigramma SGI con il doppio ruolo di Andrea (AU e CTO) e, collegata, la separazione dei compiti (27001 5.3) da dichiarare nell'analisi dei rischi con le misure compensative.
- **Fine riga**: i file sul PC Windows sono CRLF, nel repo sono LF (git per Windows converte, l'ambiente Linux no). Chi scrive nel repo da Linux deve salvare in LF, altrimenti il diff mostra l'intero documento riscritto.

## Presa visione e consapevolezza (26/10/2026)

- Scartato il modulo Google per documento e revisione (menu da aggiornare a ogni revisione, non mantenibile). Scelto un **pacchetto unico** `ALPR05.1.H - Documenti per il personale` (PO01, REG01, ALPR31.2.A, PR27.1 segnalazione) confermato in blocco: all'ingresso, ogni anno a gennaio, a ogni revisione sostanziale. La revisione in vigore alla data risulta dalle tabelle delle revisioni e dalla cronologia git.
- Registro: lista ClickUp **«Consapevolezza e formazione»** (cartella SGI). Un task per occasione, un sottotask per persona con due voci (lettura del pacchetto; il proprio portatile Vectorlab rispetta i requisiti di REG01 §3). La persona chiude il proprio sottotask: chi chiude e quando è l'evidenza. Nella stessa lista le sessioni di formazione (obiettivo 5).
- Creato il task «Presa visione documenti per il personale – 2026» con 10 sottotask (6 sviluppatori, Davide, Andrea, Francesco, Andrei), **senza assegnatari**: si assegnano dopo l'approvazione di Andrea.
- Aggiornati PR05.1 (rev 0.4) e PO31 (rev 0.2); ALPR31.2.A rimanda ad ALPR05.1.H.
- **Correzione del 26/10**: i portatili sono **forniti da Vectorlab**, non personali (A0007/A0008 nell'inventario asset sono corretti). Nessuna procedura sui portatili esisteva.
- **REG01 rev 0.1 (27/10)**: riscritto da 1.435 righe di modello a ~200 righe sugli strumenti reali. Portatili con 4 requisiti minimi (disco cifrato con BitLocker o Crittografia dispositivo, password con blocco schermo, aggiornamenti automatici, Defender attivo), confermati da Andrei e Andrea, verificati da ciascuno sul proprio portatile; sviluppatori amministratori del proprio PC come scelta motivata. Account aziendali con verifica in due passaggi, Bitwarden, niente account condivisi, password lunghe senza scadenza fissa (NIST SP 800-63B). Tolti ticketing, firewall con filtri, NAS, VPN, sfondi, KeePass. Casella dell'uscente allineata a PR05.1 (6 mesi, non 60 giorni). Aperti: app di messaggistica ammessa al posto di Discord; rete Wi-Fi e stampante dell'ufficio.
- Controllo dei portatili (27/10): non lo fa Andrei, lo fa **ogni persona in autonomia** e lo registra nel proprio sottotask di presa visione con modello e numero di serie; i sottotask formano l'inventario. Chiave di ripristino BitLocker nel Bitwarden aziendale. Da fare prima dell'audit interno. Poi si possono assegnare i sottotask di presa visione (dopo l'approvazione di Andrea).

- **PR35.1 rev 0.2 (27/10)**: allineata a PR09.1 (offerta firmata dal CTO; le clausole su riservatezza, proprietà intellettuale e dati personali non sono più date per presenti, restano «DA COMPLETARE»), a REG01 (portatili Vectorlab) e a PR27.1 (incidenti a sicurezza@). Resta aperto l'elenco degli strumenti di IA autorizzati (§2.3).

## Triage dei documenti (28/10/2026)

- Verificato sui testi UNI: la 27001 (7.5.1) e la 9001 chiedono pochi documenti obbligatori; il resto è a scelta dell'organizzazione, proporzionato alle dimensioni. Un documento si può ritirare se la SoA viene aggiornata, i rimandi corretti e le registrazioni conservate.
- Triage di tutti i 172 file del repo (documento «Triage documenti SGI» tra gli artifact): 81 tenere, 16 riscrivere, 13 compilare, 25 unire, 31 ritirare (−26% di righe). Ritiri e unioni approvati da Davide il 28/10; Nextage avvisata.
- Esame di verifica: requisiti obbligatori 27001/9001 tutti coperti; 51 controlli SoA da riallineare (+3 errori già presenti: 5.8 senza documenti, 5.31 senza MDPO29.C, 6.6 senza NDA); 34 documenti con rimandi da correggere; nessuna registrazione reale nei documenti da ritirare.
- **Lacuna**: MDPR33.1.D (rischi e opportunità per la qualità, ISO 9001 6.1) è vuoto e non c'è altra analisi: da fare prima dell'audit.
- Da decidere con Nextage: applicabilità di 9001 7.1.5 e 8.3 (PO02 §4.4 dichiara tutto applicabile).

### Ritiri e unioni applicati (28/10/2026)

- Ritirati o uniti **41 documenti** (53 file). Elenco con motivo e documento sostitutivo in `tools/ritirati.csv`; `genera_elenco.py` lo riporta in fondo a MDPR08.1.A («Documenti ritirati o uniti»). Le versioni precedenti restano nella cronologia git (evidenza per 7.5.3).
- Contenuti assorbiti: PR33.1 rev 0.2 (rischi e opportunità ISO 9001, da PR33.1.1); MDPR11.1.A §6 «Verifiche tecniche periodiche» (da MDPR11.1.C); MDPR26.1.B §6 «Valutazione annuale» (da MDPR26.1.A); PO31 privacy by design art. 25 (da PO30); registro chiavi unico MDPR05.1.U (da MDPR05.1.S/T); PR08.1 senza modelli Word/Excel.
- Rimandi corretti in REG01, PR18.1 (rev 0.3), PR11.1, PR12.1, PR08.1, PR27.1, MDPR05.1.V, ALPR26.1.D, MDPO29.C, PO31. I rimandi nei documenti da riscrivere si correggono alla riscrittura.
- **MDPR18.1.D** (registro visitatori) tenuto: l'ipotesi che lo gestisse il condominio non era verificata. Emergenza ed evacuazione: documenti D.Lgs. 81 seguiti dal consulente sicurezza, fuori dal SGI.
- ALPR05.1.E rev 0.1: giornate di lavoro agile non fisse, concordate di settimana in settimana con il PM o la Direzione.
- REG02 e PR04.1 ritirati (deciso 28/10): non richiesti dalle norme e pieni di contenuti da modello. Il processo disciplinare richiesto da 27001 A.6.4 è ora in REG01 §11 (rev 0.2), comunicato con la presa visione di ALPR05.1.H; SoA rev 0.5 (6.4 non più «non formalizzato», tolti i rimandi a REG02 e PR04.1, corretto «REGO01» in 5.4). Il processo Amministrazione resta descritto in PO02. Da verificare con il consulente del lavoro: codice disciplinare del contratto collettivo affisso in ufficio (art. 7 L. 300/1970).
- Dashboard: PO25 e PR20.1 declassati a «da rifare»; righe dei documenti ritirati tolte.
- Prossimo: riscritture P1 (PR16.1, PR32.1, PR26.1, PR10.1, PR05.1, PO25) e compilazione di MDPR33.1.D con Andrea; riallineamento SoA (54 controlli) con Nextage.

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
- [ ] Documenti grafici (21/10/2026): convertire in .md con diagrammi Mermaid ALPO01.A Organigramma, ALPO02.A Contesto e processi, ALPR24.1.A/B Schemi (quando il repo sarà privato), MDPR12.1.A Riesame; piantina ALPR18.1.A come immagine; abilitare Mermaid in `mkdocs.yml`; convertire l'immagine .emf di PR33.1; togliere le 7 immagini inutilizzate di PR08.1; decidere che per i moduli con doppia versione xlsx/md vale il .md
- [ ] Modello di preventivo Ynsera: aggiungere condizioni generali (riservatezza, proprietà intellettuale, organizzazione del lavoro a cura del PM, dati personali) dopo revisione legale
- [ ] MDPO15.A: fissare con l'IT la durata dei backup

## Piano di audit MDPR11.1.B (04/11/2026)

Nextage ha chiesto il «template di piano di audit» per l'audit interno di fine novembre. Il file era ancora il modello generico Nextage (rev 0.0, cartella Drive 0_Working). Portato a rev 0.1 «Da approvare» nel .md:

- una sola modalità, per funzione (tolta quella per processo);
- funzioni reali allineate al programma MDPR11.1.A §3: Direzione, CTO/CISO con IT esterno, RSGI, Business Development, Digital, Amministrazione, HR, Referente Privacy;
- tolti ISO 27017/27018, DPO, PM, «Area XXXX» e i controlli non applicabili da SoA (A.7.12, A.8.11, A.8.30);
- aggiunta la sezione dati dell'audit (obiettivi, campo, criteri, metodo, auditor) e il collegamento dei rilievi alla lista ClickUp NC (PR13.1).

Aperto: il .xlsx accanto è ancora il modello Nextage rev 0.0; date, orari e auditor da compilare con Nextage.

Nota (05/11/2026): modifiche fatte il 04/11 in una seconda copia del repo (`OneDrive\Desktop\Conversione ISO`, altro PC) mai committata; riapplicate qui il 05/11. Quella copia va scartata: lavorare solo in `Desktop\Vectorlab-SGI`.

## Piano dell'audit interno I/2026 (11/11/2026)

Mail di Micaela Leone del 10/11/2026 «Piano audit interno»: piano pronto su Drive (*Master › B_REGISTRAZIONI › Audit Interno › Anno 2026 › MDPR11.1.B*), date spostate al **25–26/11/2026**. Il «template su GITLAB da cambiare» della mail significa: portare il piano compilato nel repo (Nextage lavora solo su Drive).

- Nuova registrazione `docs/B_REGISTRAZIONI/Audit Interno/2026/MDPR11.1.B - Piano di Audit e Report - I-2026.md` (rev 0.0, «Da approvare»): trascrizione fedele del file Drive nel formato del modello VectorLab rev 0.1 (verificati tutti i 157 riferimenti all'Annex A). Il modello in `9.2_AUDIT INTERNO` resta invariato; l'Excel di Nextage non entra nel repo.
- `MDPR11.1.A` rev 0.5: date 25–26/11 e nomi degli auditor (Micaela Leone, Francesca Capuano).
- Indici `B_REGISTRAZIONI` e `Audit Interno/2026` aggiornati per la navigazione.

Punti aperti sul piano, da chiarire con Nextage (non corretti nella trascrizione):

- include controlli non applicabili da SoA: A.7.12 (sessione IT), A.8.11 (Referente Privacy, IT), A.8.30 (Digital, CTO);
- il CISO è attribuito sia al CTO (Amministratore Unico) sia a RSGI: va allineato all'organigramma;
- A.5.1 Politiche per la sicurezza delle informazioni non compare (nel modello VectorLab è nella sessione Direzione);
- nel file Drive la copertina riporta «Approvato: CDA»;
- indipendenza degli auditor: MDPR11.1.A §1 esclude chi ha redatto la documentazione.

Da organizzare: Andrei il 25/11 alle 14:00 e il 26/11 dalle 9:30 alle 11:30; uno sviluppatore il 25/11 alle 11:00; chi sono «Resp. BD» e «Resp HR»; Riesame della Direzione tra il 27/11 e l'11/12 (stage 1 il 15/12).

Nota (11/11/2026): la copia `OneDrive\Desktop\Conversione ISO` è stata riallineata a GitHub (stesso commit `6f77e4e`, contenuto identico a meno dei fine riga) ed è quella collegata a Claude su questo PC: la nota del 05/11 che la dava da scartare non vale più.

## Risposte di Andrea e Francesco (riunione del 04/11/2026), applicate l'11/11/2026

Fonte: documento Claude «ISO – Domande aperte per Andrea e Francesco (riunione 4/11)». Applicate solo le risposte che sono fatti chiari; ogni documento ha una riga di revisione «Da approvare».

- `PO01` rev 0.4: politica non pubblicata sul sito, disponibile su richiesta (dom. 7).
- `PO02` rev 0.5 e `PR18.1` rev 0.4: tolto AWS (dom. 28).
- `REG01` rev 0.3: nessuna app di messaggistica ammessa per il lavoro; nessuna rete Wi-Fi ospiti; nessuna stampante (dom. 11–13).
- `MDPR26.1.B` rev 0.3: accordi con i fornitori, Aruba, certificati Actalis/GoDaddy, consulenti tecnici, Davide e Francesco tra i fornitori critici (dom. 23–31).
- `ALPO01.B` rev 0.3: misure compensative approvate dall'Amministratore Unico (dom. 8).
- `MDPR06.1.C` rev 0.1: piano della formazione 2026–2027 (dom. 20 + obiettivo 5).
- `MDPR06.1.E` rev 0.2: competenze tecniche del team (dom. 21); livelli da assegnare.
- `PR19.1` rev 0.1: change come task ClickUp (dom. 17).
- `PO25` rev 0.1: riscritta in forma breve con le risposte 1–6 del CTO.
- `MDPR31.4.A` rev 0.1 e `MDPR31.4.B` rev 0.1: registro dei trattamenti come titolare (dom. 36, 40); nessun trattamento come responsabile. Telefono (dom. 37) non inserito finché il repo è pubblico.

Decisioni dell'11/11 sui punti aperti: backup (dom. 16) **lasciato aperto** da Davide: A.8.13 e obiettivo 3 di MDPO03.A restano scoperti, probabile NC all'audit. BIA e continuità (dom. 18–19): **rischio accettato** per tutti i servizi, compresa la perdita definitiva dei dati del server Aruba senza backup; `MDPR28.1.A` rev 0.1 in forma minima e `PR28.1` rev 0.1 (applicazione ridotta, evidenze in B_REGISTRAZIONI); accettazione da approvare da Andrea.

Non applicate, da decidere con Davide (risposte in contrasto con le norme o incomplete): backup «di competenza di Aruba» (dom. 16, lasciato aperto); ruolo GDPR di ABCD Lavoro e Google (dom. 39); A.8.30 con i consulenti esterni su progetti dei clienti (dom. 30–31); misura compensativa sui log (nota di Andrea alla dom. 8); i 29 controlli «solo pianificati» (dom. 10, da Davide); AGID da togliere dalla SoA (dom. 9, in ERA con Nextage); evidenze dei casi già avvenuti (dom. 44); KPI con responsabile Andrea (dom. 22).

Altre decisioni dell'11/11: ruolo GDPR di ABCD Lavoro (dom. 39) **in attesa** dei documenti richiesti allo studio. A.8.30 e consulenti esterni (dom. 30–31): **contratto diretto tra consulente e cliente**, Vectorlab fa solo la parte amministrativa e contabile (Davide, 11/11): A.8.30 resta escluso; motivazione in `MDPR26.1.B` e `PO25` §6, da far riportare da Nextage in ERA (la motivazione attuale della SoA è contraddittoria: «applicabile ma non applicato»). Log (dom. 8): misura resa concreta nel `ALPO01.B` §3, log degli accessi degli amministratori al server conservati 6 mesi e **controllati da RSGI una volta l'anno** (minimo del provv. Garante 27/11/2008). Casi già avvenuti (dom. 44): chiavi, **registro MDPR05.1.U da compilare ora** (Francesco); portatili, aperto (sottotask di presa visione da assegnare); visitatori, **nessun registro, rischio accettato** (`PR18.1` rev 0.4, `PO26` rev 0.1); il modulo `MDPR18.1.E` resta nel repo ma non è più usato: da ritirare in `tools/ritirati.csv` e `MDPR08.1.A` al prossimo triage.

## Revisione documenti con Davide (16/11/2026)

Metodo: una domanda alla volta; i documenti si aprono in chat in versione HTML leggibile. Decisioni di Davide valide da ora: **revisioni azzerate a una sola riga «rev 0.0 – Emissione – Da approvare»** per ogni documento che si sistema; **la versione Nextage su Drive è solo un punto di partenza, fa fede il repo**.

- `ALPO01.B` Mansionario rev 0.0: 14 schede sulla realtà Vectorlab. Tolte IT Staff, HR Staff, Innovation & Research (fuori campo), Digital Technical Manager (unita al CTO); HR Director → Risorse Umane (Francesco: selezione, ferie e presenze, consulente del lavoro, formazione e 81/08); aggiunta scheda PM (PR35.1). Tolti anni di esperienza (li decide l'organizzazione; requisito = titolo o esperienza documentata, livelli in MDPR06.1.E), parità di genere, piano carriere, clima, ISTAT, centralino, posta, Confindustria, credito d'imposta, PMI innovativa. Finanza: operativo Francesco, decide Andrea. Andrei: server Aruba, servizi, TLS, rete ufficio (niente backup né PC); PC gestiti da ciascun dipendente; GitHub al CTO. Sviluppatori: competenze dalla griglia, lavoro nel processo del cliente, accettazione del cliente (§3). Business Development (Davide): prospect, offerte, clienti, social e comunicazione. §2.15 tabella «Responsabile di Area». Codici ALPO31.B e ALPO31.C corretti.
- `ALPO01.A` Organigramma rev 0.0: Innovation & Research lasciata con «fuori dal campo di applicazione SGI»; Digital e PM invariati.
- **RLS**: Marco Ottone Casagrande è in organigramma ma **non è stato eletto né ha fatto il corso**. Da decidere con Francesco: elezione interna (verbale, comunicazione INAIL, corso 32 ore) o RLS territoriale (art. 48). Scheda RLS nel Mansionario: «consultato» sulla designazione di addetti e medico competente.
- `PR33.1` rev 0.0: criteri di rischio (6.1.2 a): metodologia ERA, RA = 45 stabilito dall'AU, trattamento sopra soglia, residuo sopra RA solo per eccezione motivata e accettata dall'AU; selezione dei controlli, confronto con Appendice A e SoA (6.1.3 b–d); approvazione di Risk Owner e AU (6.1.3 f); CISO = AU con riesame RSGI. Testo della norma letto da `271_2024_Cesare_3.md` (Drive NORME ISO). I 5 rischi accettati nel piano 2026 hanno residuo 45 = RA: coerenti con il criterio.
- `PO01`, `PR11.1` rev 0.0 (solo revisioni). `PO02` rev 0.0: schede di processo riviste una a una (tolti gare/PA, posta, rendicontazione ricerca, help desk, manutenzione, sviluppo esternalizzato, attività commerciali in Digital, parità di genere, molestie, comitato guida, sindacati, Confindustria, partner); ore in giornate/mezze giornate (Planner, in sviluppo); offerte nella cartella Drive del prospect; Z1 Social Media Manager esterno; 13 codici documento corretti; KPI allineati ai 14 della tabella.
- `MDPR10.1.A` Tabella Indicatori rev 0.0: da 54 KPI mai misurati a 14 (PS5, PS4, GC2, GC3, IN1, IN4, DA1, CN1, SO3, RF6, PS1, PS3, RU1, AR2) con obiettivo, soglia, frequenza, fonte, responsabile, **in bozza**. Tolto dal repo l'Excel di Nextage con i 54 KPI. `PR06.1` rev 0.0: monitoraggio con RU1.
- SoA (in ERA, da chiedere a Nextage dopo il 18/11): A.8.13 backup oggi dichiarato attuato ma assente (sicuro entro il 15/12, probabile entro il 25/11); A.8.30 non applicabile (Vectorlab non affida mai sviluppo a esterni; consulenti con contratto diretto col cliente); A.7.12 non applicabile (solo router e Wi-Fi); togliere sezione AGID; rischio Copilot. Gruppo 1 (comunicare PO01, REG01, PO15, MDPR05.1.H al personale con presa visione) **entro il 25/11**.
- Piano audit I/2026 (Nextage, non modificato): da segnalare a Nextage l'indipendenza di Francesca Capuano sull'analisi dei rischi (ha partecipato alla checklist di agosto) e Andrea in due sessioni parallele il 26/11 ore 9:30. Il resto lo gestisce Nextage.
- Piantina `ALPR18.1.A`: vuota, solo intestazione.

**Riunione di mercoledì 18/11 con Andrea, Andrei e Francesco**:
1. RLS: elezione interna o RLS territoriale.
2. SoA gruppo 2 (screening, formazione sicurezza, verifiche del rispetto delle regole) e gruppo 3 (chiavi e accessi, scrivania pulita, portatili fuori sede, dismissione PC): cosa è già in uso, cosa entro quando.
3. SoA gruppo 4 tecnico con Andrea e Andrei: 8.1 dispositivi, 8.2/8.18 accessi privilegiati, 8.20 rete, 8.23 filtro web, 5.28 raccolta prove, 5.30 continuità ICT, 5.33 protezione registrazioni.
4. Backup: data e prima prova di ripristino.
5. Planimetria o foto dell'ufficio (ALPR18.1.A) e schema ICT.
6. Z1 in MDPR26.1.B: NDA e accessi ai profili social.
7. Consegna di portatili e account con MDPR05.1.V: mai fatta, da avviare (Francesco).
8. PO02 Digital: chi fa progettazione e requisiti; quali test fa il team (codice, prestazioni/carico/stress, VA-PT); strumenti (Andrea).
9. Confermare i 14 KPI di MDPR10.1.A e fare la prima misurazione prima del 25/11.
10. Livelli della griglia competenze MDPR06.1.E (Andrea) prima dell'audit.
11. Mail al team del gruppo 1 entro il 25/11.
Dopo la riunione: un'unica mail a Nextage (SoA + piano audit). Nel Riesame: accettazione di RA = 45 e valutazione dei cambiamenti da settembre (campo ristretto a Ynsera, AWS tolto, NC01 TLS) senza nuova analisi dei rischi.

## Riferimenti rotti e metodologia rischi (17/11/2026)

- Corretti 26 riferimenti con codice sbagliato in 19 documenti (es. PO34 → PO40, ALPR26.1.C → ALPR16.1.C, ALPR26.1.B → ALPR26.1.B.3, MDPO29.D → MDPO29.A, MDPR09.1.* → MDPR33.1.*, MDPR07.A → MDPO07.A, codici con suffisso .1/.2/.3); righe di revisione storiche non toccate.
- Tolti 8 rimandi a documenti mai scritti (PR39.1, MDPR05.1.Q/R, REG03 → PR18.1, PO05 → PO01, ALPR28.1.B Disaster Recovery Plan, MDPR09.1.A Maturity model, template MDPR32.1 → repository Ansible e REG01 §3). MDPO25.F (UI-UX, solo su Drive) non importato.
- Nuovo `ALPR33.1.A – Metodologia di Analisi del Rischio (ERA)` rev 0.0, scritto da Claude dal report 2026 (decisione di Davide): da confermare con Nextage numero dei livelli delle scale e formula di ERA. PR33.1 e PO23 ora rimandano ad ALPR33.1.A.
- Corretti anche i rimandi a documenti ritirati il 28/10 (decisione di Davide, 17/11), con il sostituto di tools/ritirati.csv: MDPR11.1.C → MDPR11.1.A §6, MDPR26.1.A → MDPR26.1.B, PO27 → PR27.1, PO30 → PO31, MDPR05.1.S/T → MDPR05.1.U, MDPR05.1.D → MDPR06.1.E, MDPR06.1.B/D → lista ClickUp «Consapevolezza e formazione», MDPR21.1.B → richiesta via mail o task ClickUp (PR21.1), PR29 → PO29, ALPR24.1.A/B → schema ICT riservato fuori dal repo, MDPR05.1.M → anagrafica tenuta dall'Amministrazione fuori dal repo. Restano solo le citazioni storiche («sostituisce il vecchio…») e le righe di revisione. Tabelle delle revisioni non modificate: sono correzioni di rimandi.
- **SoA**: corretti nel repo 27 link a documenti ritirati (PO27, PO30, MDPR11.1.C, MDPR26.1.A, MDPR21.1.B, MDPR05.1.S/T/D, MDPR06.1.B, ALPR24.1.A/B). **Da comunicare a Nextage** nella mail unica perché allineino ERA.

## Riduzione documenti: nasce PR32.1 Infrastruttura IT (17/11/2026)
- Decisione di Davide (17/11): ridurre i 38 documenti copiati dai modelli Nextage. 14 da tenere e correggere, 21 da unire in 6 documenti, 3 checklist di audit (MDPR11.1.D/L/M) da togliere se Nextage usa le sue.
- Primo gruppo fatto: PR32.1 «Gestione delle Configurazioni e dell'Infrastruttura IT» (rev 0.0, Da approvare) riunisce PO32, PR03.1, PR14.1, PR22.1, PO20, PR20.1, PR24.1, PO17. Gli 8 file sono stati tolti dal repo e registrati in tools/ritirati.csv (esito Unito). Rimandi aggiornati in 11 documenti, SoA compresa; index delle 4 cartelle aggiornati.
- SoA: corretti anche i rimandi a REG03 (→ ALPR05.1.E), MDPR32.1.A (→ PR32.1) e ALPR23.2.A (→ MDPR23.2.A).
- Da confermare con Andrei il 18/11 (segnati [DA CONFERMARE] nel PR32.1): dove sta il repository Ansible, frequenza degli aggiornamenti, strumento di monitoraggio, NTP, chiavi SSH personali e firewall.
- Prossimi gruppi: PR21.1 (+PO21, MDPR21.1.A), PR16.1 (+PO16), PR23.1 (+PO23), PR26.1 (+PO26, PO40, ALPR26.1.E), PR28.1 (+PO28).
- Secondo gruppo fatto (17/11): PR21.1 «Gestione dei Backup e Restore» (rev 0.0, Da approvare) riunisce PO21, ritirata. Decisioni di Davide: AWS non è usato da Vectorlab (tolto); Google Workspace e GitHub non hanno copie esterne (protezione del fornitore, da registrare come rischio accettato); prova di ripristino solo del server Aruba, una volta l'anno, più un recupero di file da Google Workspace; MDPR21.1.A resta come registro in formato md (xlsx tolto il 17/11). Tolti dal PR21.1 i dettagli tecnici dell'infrastruttura (repo pubblico).
- Attenzione audit: nessuna prova di ripristino è ancora stata fatta; la prima entro il 15/12/2026. In ERA il controllo 8.13 risulta «attuato»: va corretto.
- Da decidere il 18/11 con Andrea: copia esterna di GitHub o rischio accettato (registro rischi e Riesame).
- Terzo gruppo fatto (17/11): PR16.1 «Gestione degli Accessi» (rev 0.0, Da approvare) riunisce PO16 e ALPR16.1.A, ritirati. Decisioni di Davide: gli account (Google Workspace, GitHub, ClickUp, Bitwarden) li gestiscono RSGI e Francesco; n8n lo usano solo Davide e Andrei; revisione degli accessi ogni 6 mesi con gli elenchi scaricati dalle console allegati al task ClickUp (niente lista utenze nel repo: dati personali). KPI DA1: obiettivo 2 revisioni l'anno.
- Verifica in due passaggi su Google Workspace: controllata il 17/11 nella console; dettaglio nella checklist privata della riunione. Primo punto della riunione del 18/11 (proposta: obbligo dal 24/11, senza SMS).
- Nomine degli amministratori di sistema (Provv. Garante 27/11/2008): da far firmare ad Andrei (con verifica del contratto art. 28 GDPR) e a Davide; elenco MDPO29.A da compilare (Francesco).
- Quarto gruppo fatto (17/11): PR23.1 «Gestione delle Minacce e delle Vulnerabilità Tecniche» (rev 0.0, Da approvare) riunisce PO23, PR23.2, MDPR23.1.A e MDPR23.2.A, ritirati. Davide (17/11): il foglio Nextage del 27/07 sulle minacce è generico e non adatto a Vectorlab; sostituito da MDPR23.1.B «Monitoraggio delle minacce 2026» (10 minacce riferite a Vectorlab, colonna ERA da completare). Da verificare il 18/11: scansioni del server (Andrei), Dependabot e secret scanning su GitHub (Andrea), regola sui cambi IBAN (Francesco).
- Quinto gruppo fatto (17/11): PR26.1 «Gestione dei fornitori» (rev 0.0, Da approvare) riunisce PO26 e PO40, ritirati; allineato all'Elenco fornitori MDPR26.1.B già compilato. La lettera ALPR26.1.A ora include i requisiti di sicurezza (ALPR26.1.E ritirato). Corretto un errore: ALPR26.1.A ed E dichiaravano un SGSI «certificato ISO/IEC 27001»; ora «in corso di certificazione». Davide (17/11): la lettera non è mai stata inviata. Termine di 24 ore per la notifica degli incidenti dei fornitori: proposta da confermare.
- Sesto gruppo fatto (17/11): PR28.1 «Gestione della continuità operativa» (rev 0.0, Da approvare) riunisce PO28, PR28.2, ALPR28.1.A, MDPR28.1.B e MDPR28.1.C, ritirati. BIA MDPR28.1.A rev 0.2: il server Aruba (e Bitwarden) passa da rischio accettato a trattato, coerente con PR21.1; il piano di ripristino è la copia del server con prova annuale. Aggiunte le regole di sicurezza durante un'interruzione (A.5.29).
- Riepilogo della riduzione del 17/11: 6 gruppi chiusi (PR32.1, PR21.1, PR16.1, PR23.1, PR26.1, PR28.1); ritirati 23 documenti. Restano: correzione dei 14 documenti da tenere; le 3 checklist di audit (MDPR11.1.D/L/M) da ritirare se Nextage usa le sue; verifica di MDPR18.1.D.
- Decisione di Davide (17/11): finché non c'è l'approvazione unica di Andrea, tutti i documenti hanno una sola riga di revisione «0.0 – 17/11/2026 – Emissione – RSGI – Da approvare». Azzerate le tabelle di 92 documenti .md (SoA compresa, anche «Versione» e «Data ultima versione» in copertina); lo storico resta nella cronologia di git. Non toccati i file .xlsx/.pptx e i documenti senza tabella delle revisioni (lettere ALPO31.A/B, ALPR27.1.A, registri MDPR18.1.A/E, checklist MDPR11.1.L/M, asset inventory).
- Decisione di Davide (17/11): eliminati i 26 file Excel (.xlsx/.xlsm) che avevano un gemello .md (SoA, registri, moduli, BIA, elenco fornitori, asset inventory…): nel repo fa fede il .md. Tolti dagli index delle cartelle. Restano i .pptx (organigramma, contesto, riesame, piantina) e il .drawio.
- Rinominati il 17/11 quattro file perché il nome coincida con il titolo: PR32.1 «…e dell'Infrastruttura IT», PR23.1 «Gestione delle Minacce e delle Vulnerabilità Tecniche», PR28.1 «Gestione della continuità operativa», ALPR26.1.A «Comunicazione e requisiti di sicurezza per i fornitori». Link aggiornati; controllo di tutti i 522 link interni del repo: nessuno rotto.
- Documenti da tenere e correggere (14), iniziati il 17/11. 1) PR10.1 riscritto e allineato ai 14 KPI; tolte affermazioni non vere (monitoraggio automatico, audit trail, log digitali degli accessi fisici) e contraddizioni (DPO, obiettivi in MDPR33.1.D). Davide (17/11): questionario di soddisfazione a fine commessa su pagina web preparata da Andrei, non ancora fatto; aggiunto l'invio annuale ai clienti continuativi. KPI SO3 portato ad annuale (coerente con PR21.1); PS5 aggiornato.
- 2) PR19.1 Gestione del cambiamento riscritto: cambiamenti ai sistemi ordinari (già approvati), importanti (approvazione CTO prima) e urgenti (registrati entro 2 giorni), più i cambiamenti al Sistema di Gestione (6.3). Davide (17/11): oggi Andrei registra le modifiche a modo suo; proposta la lista ClickUp «Modifiche ai sistemi», da confermare il 18/11.
- 3) PO25 Sviluppo sicuro: testo già riscritto dopo il 28/10 e buono; il 17/11 segnati 4 punti [DA CONFERMARE] per Andrea (revisione del codice, MDPO25.B/G, strumenti sulle librerie, secondo fattore GitHub). Davide non conosce la pratica del team su questi punti.
- 4) PO29 Gestione della conformità riscritto: tolti DPO, «provider cloud», ticketing; licenze e abbonamenti nell'inventario tenuto dall'Amministrazione (Davide, 17/11). Restano circa 50 citazioni del DPO in altri documenti (privacy): da sistemare con PR31.1.
- 5) PR31.1 Diritti degli interessati riscritto; corretto il caso di Vectorlab responsabile del trattamento (inoltro al titolare, art. 28.3.e). Davide (17/11): le caselle privacy@vectorlab-cg.com (39 citazioni, informative comprese) e sicurezza@vectorlab-cg.com (11 citazioni) NON esistono: da creare come gruppi Google (privacy@ → Francesco; sicurezza@ → RSGI e CISO). Corretto privacy@vectorlab.it in PR08.1. Le citazioni del DPO negli altri documenti sono già condizionate («ove nominato»): coerenti.
- 6) PR05.1 Gestione del personale riscritto (da 1050 righe a 4 pagine) sui requisiti ISO; tolti permessi, congedi, welfare, buste paga (restano all'Amministrazione con il consulente del lavoro). Mantenute le sezioni già adattate (presa visione, casella email all'uscita). Da chiedere a Francesco: dove sta l'archivio del personale.
- 7) ALPR05.1.E Accordo lavoro agile: correzioni mirate (rimando a un piano di continuità inesistente, «incaricato» pre-GDPR, refusi) e regole di sicurezza per il lavoro da remoto (A.6.7). REG01 §9: tolta la descrizione della rete Wi-Fi dell'ufficio (repo pubblico); accesso ospiti da decidere con Andrei.
- 8) MDPO07.A Piano della comunicazione rifatto (canali reali, niente «xxx»); corretto l'errore sulla notifica dei data breach al Garante (art. 33 vs art. 34).
- 9) Contratto di fornitura: rinominato ALPR16.1.C → ALPR26.1.C (allegato di PR26.1); compilati i dati di Vectorlab, campi da compilare in «[…]», allegati senza doppioni; testo giuridico invariato.
- 10) ALPR26.1.B.3 Accordo di riservatezza: compilati i dati di Vectorlab, controparte società o persona fisica (serve per stagisti e professionisti come Andrei), campi «[…]», ambito esteso a fornitura/collaborazione/stage. Testo giuridico invariato.
- 11) MDPR18.1.D e MDPR18.1.G rifatti come moduli puliti; dati da completare con Francesco (impianti presenti, addetti emergenza, condominio). Davide è sicuro solo della cassetta di primo soccorso; l'ultimo elenco del contenuto aveva scadenze 2021–2023: da controllare. Numeri di telefono fuori dal repo.
- 12) MDPR33.1.D Rischi e opportunità (9001, 6.1): era vuoto; prima compilazione in bozza (7 rischi, 3 opportunità) da confermare con Andrea. MDPR33.1.B Piano di trattamento: aggiunte le azioni T1–T13 e la rivalutazione dei rischi accettati (A0017 Discord, A0039 codice clienti). Da segnalare a Nextage: ricalcolo ERA; nella SoA 8.5 (verifica in due passaggi) e 8.13 (backup) risultano «attuati» ma oggi non lo sono.
- Fine dei 14 documenti da tenere e correggere (17/11). Restano: SoA (gruppi 2–4 con Francesco e Andrea), checklist di audit MDPR11.1.D/L/M (in attesa di Nextage), PO02 (rimandi a Jira, «parità di genere», piano di continuità ID-PBC05 da verificare).
- Link ai documenti (17/11, decisione di Davide): ogni codice di documento citato nei testi è ora un link alla pagina del documento sul sito (1108 link in 69 file; relativi, controllati da mkdocs). Esclusi titoli, intestazioni, tabelle delle revisioni, index e codici dei documenti ritirati. Corretto anche un errore di tools/genera_elenco.py: i link dell'elenco MDPR08.1.A puntavano a un livello sbagliato ed erano rotti sul sito. Verifica sul sito costruito in locale: 1621 link, 0 rotti.

## Riunione del 18/11/2026 (Andrea, Andrei, Francesco)
- Decisioni dell'Amministratore Unico: Discord resta in uso con regole d'uso (REG01 §5: niente dati o codice dei clienti, niente credenziali; senza obbligo di verifica in due passaggi), rischio accettato: supera la decisione del 04/11 «nessuna app di messaggistica». GitHub senza copia esterna: rischio accettato. Codice dei clienti: rischio ridotto (pull request rivista a ogni funzionalità e rilascio, controllo password nel codice). Tolto da MDPR33.1.D il rischio R5 «Mercato del lavoro». sicurezza@ → Andrea, Davide, Andrei; privacy@ → Francesco (riserva Davide). Verifica in due passaggi obbligatoria dal 24/11/2026, solo passkey o token.
- Andrei: backup settimanale automatico; prima prova di ripristino il 18/11 (da registrare in MDPR21.1.A); aggiornamenti automatici del server; avvisi del monitoraggio a sicurezza@; registro modifiche = lista ClickUp «Modifiche ai sistemi»; ospiti senza Wi-Fi aziendale (telefono o hotspot). Dettagli tecnici fuori dal repo.
- Francesco: niente registro visitatori (MDPR18.1.E ritirato, rischio accettato); RLS: candidato Marco Ottone Casagrande, votazione da fare; addetti antincendio e primo soccorso: Andrea; contratto di Andrei (incarico, riservatezza, art. 28, nomina AdS) da fare la settimana del 23/11.
- Campo di applicazione: resta quello del 16–17/11 (servizio Ynsera, esclusi prodotti, bandi e ricerca). Lo stash locale «campo esteso PO01/PO02 14/11» non va applicato.
- Da fare lunedì 23/11: domande aperte di Andrea (a3, a4, a12, a17–a20), di Andrei (b13 schema ICT, b16 CSIRT), sezioni sopralluogo, documenti ed evidenze, comunicazioni ai dipendenti; c17 da riformulare.
- 19/11/2026: verifica in due passaggi obbligatoria impostata dal 24/11 (ammessi tutti i metodi, anche SMS: modifica la decisione del 18/11) e personale avvisato; creati i gruppi privacy@ e sicurezza@ (T8); chiavi BitLocker in Bitwarden, accessibili solo a System Administrator e Amministrazione. Da fare: indirizzo privacy@ nell'informativa Iubenda del sito.
- 19/11/2026: presa visione dei documenti per il personale nella lista ClickUp «Consapevolezza e formazione» (cartella Evidenze): un sottotask per i 5 dipendenti e Andrei, conferma con il commento «Letto, il portatile è a posto». Da avviare dopo l'approvazione unica di Andrea (dopo il 27/11), scadenza 12/12. REG01 §3: blocco schermo a cura della persona (Windows + L), non automatico.

## Sito compilato e SoA leggibile (23/11/2026)
- Sito: tema scuro (`palette: slate` in `mkdocs.yml`, da aggiungere a mano: il file è protetto per gli strumenti remoti), colonna centrale più larga, barre laterali più strette, tabelle senza tagli (tolto `width: max-content`, che impediva di andare a capo), registri larghi con intestazione e prima colonna fisse. Tutto in `docs/stylesheets/extra.css`.
- SoA rev 0.1 (Da approvare): nuova vista **generata** da `tools/genera_soa.py` a partire da `tools/soa/SOA-sorgente.md` (copia della SoA rev 0.0 del 17/11). Riepilogo per sezione (ID, controllo, applicabile, attuato, motivo L/C/B/R, riferimenti) e dettaglio apribile per controllo; link diretti ai controlli (`#c-5-1`). Contenuto dei 93 controlli invariato (verificate 1023 celle). Correzioni: «27002.0» → «ISO/IEC 27002», aggiunta l'intestazione della sezione 7, colonne sempre vuote non mostrate, **tolta la sezione AGID CSP-SAAS** (residui di un altro cliente, rimozione decisa il 16/11; resta nella sorgente).
- Regola: la SoA nel sito non si modifica a mano. Si aggiorna la sorgente e si rilancia lo script (`pip install beautifulsoup4`).
- Restano aperti, già noti e da chiedere a Nextage in ERA: 7.12 e 8.30 segnati «non applicabili» ma motivati come «applicabili ma non applicati»; 5.1 Politiche segnato «non attuato»; nessun controllo con motivo «Risultato analisi dei rischi» (colonna sempre vuota, l'auditor può chiedere il legame SoA ↔ trattamento dei rischi, 27001 6.1.3); i 29 controlli non attuati da collegare al piano MDPR33.1.B.

## Ritiro di 11 documenti e inventario asset (23/11/2026)
- Conteggio: 102 documenti del sistema prima del ritiro (101 nell'elenco + l'elenco stesso, che `tools/genera_elenco.py` escludeva: corretto, ora si include e segnala i file senza codice). Dopo il ritiro: **91 documenti** e 4 registrazioni.
- Ritirati (decisioni di Davide del 23/11, in `tools/ritirati.csv`): MDPR11.1.M checklist AdS (basata sull'Allegato B D.Lgs. 196/2003, abrogato dal D.Lgs. 101/2018); MDPO25.A OWASP ASVS (non usata); MDPO25.B, C, D, E, G modelli di progetto (nei progetti Ynsera requisiti, documentazione tecnica, test e changelog sono del cliente); ALPR27.1.B lessons learned (ora nel task ClickUp dell'incidente); ALPO31.C addendum AdS per i clienti (la nomina la fa il cliente); MDPR18.1.A registro presenze cartaceo (le presenze sono registrate nel software interno Planner, PR18.1); ALPR31.2.H registro consensi (unici consensi: liberatorie foto/video firmate).
- Rimandi corretti con riga di revisione 0.1 «Da approvare»: PR11.1, PO25 (risolto il DA CONFERMARE sui requisiti: li scrive il cliente), PR27.1, MDPO29.C (OWASP ASVS «non adottato»), PR18.1, PR31.2, ALPO01.B, PR32.1, ALPR33.1.A; index delle cartelle; SoA (10 rimandi tolti nella sorgente, vista rigenerata).
- Inventario degli asset: `asset_inventory_vectorlab` diventa **MDPR32.1.B - Inventario degli asset - 2026** in B_REGISTRAZIONI/Analisi dei Rischi/2026 (MDPR32.1.A non riusato: era un codice ritirato il 28/10). Criticità senza «.0».
- I file vanno tolti con git: `git --literal-pathspecs rm --pathspec-from-file=_ritira.txt`, poi `del _ritira.txt`.
- Da chiedere a Nextage (mail unica): togliere in ERA i rimandi della SoA a MDPO25.A/B/C, ALPR27.1.B, ALPO31.C, MDPR18.1.A. Da decidere: MDPR11.1.D e MDPR11.1.L (se all'audit Nextage usa le sue checklist); MDPR05.1.H (chiedere a Francesco chi prepara le contestazioni disciplinari). Resta il problema già noto del controllo 5.8 senza documenti nella SoA.

## Organigramma e Contesto e processi sul sito (23/11/2026)
- ALPO01.A Organigramma: pagina Markdown con l'immagine ricavata dal PowerPoint (che resta l'originale). Da chiarire: nel team Digital compare Tommaso Ramella, che non è tra le persone Ynsera del 22/10.
- ALPO02.A Contesto e processi rev 0.1 (Da approvare): riscritto in Markdown sul solo servizio Ynsera (diagramma del contesto e mappa dei processi in HTML, con link alle procedure; stile in extra.css §6). Il modello Nextage in PowerPoint conteneva «E' UN ESEMPIO va FATTO AD HOC», segnaposto «XXXXX» e processi fuori campo. PowerPoint, draw.io e immagini da togliere con `git --literal-pathspecs rm --pathspec-from-file=_ritira.txt`.
- Da sistemare: PO02 §5 ha residui del modello («Jira e pipeline CI/CD», «Parità di Genere»); PO02 §4.4 dichiara applicabile la 9001 8.3 mentre requisiti e progettazione li scrive il cliente (da rivedere con Nextage); Discord: decisione AU «resta in uso con regole» in contrasto con il vincolo «Discord non accettato».
- 23/11 pomeriggio: ALPO01.A Organigramma rev 0.1 (Da approvare) convertito in Markdown con schema ad albero in SVG (stessi contenuti, ruoli collegati al Mansionario; stile in extra.css §7); PowerPoint e immagine tolti con `_ritira.txt`; rimandi al PowerPoint aggiornati in PR05.1, PR06.1, MDPO07.A, ALPO01.B, PO01, PR09.1 (la SoA era già stata corretta).
- 23/11 sera: PO03 Gestione Obiettivi unito a MDPO03.A rev 0.1 (Da approvare): le regole (origine, contenuto, responsabilità, comunicazione, esito) sono in testa alla Lista Obiettivi; tolti i residui del modello (parità di genere, ticketing). Rimandi aggiornati in PO01, index e SoA 5.1 (sorgente e vista rigenerata; da chiedere a Nextage anche in ERA). Avviato il riesame uno per uno dei documenti facoltativi.
- 23/11 sera: PR08.1 rev 0.2 (Da approvare) accorciata da ~3.650 a ~1.270 parole sul modo di lavoro reale. Aperto: VectorLab oggi non segue fonti di aggiornamento (controllo 5.6, ex foglio FORUM); proposta 3 fonti (Dependabot, avvisi fornitori cloud, CSIRT Italia, seguite da Andrei), Davide non ha ancora deciso.
- 23/11 sera: PR10.1 unita a MDPR10.1.A rev 0.1 (regole del monitoraggio e della soddisfazione del cliente in testa alla Tabella Indicatori) e ritirata; rimandi aggiornati in PO01, PR11.1, PR35.1, MDPO07.A, MDPR33.1.D, ALPO02.A, index e SoA 5.37 (da allineare anche in ERA).

## SoA collegata all'analisi dei rischi e piano di trattamento (23/11/2026, sera)
- Fonte: due export dell'analisi ERA «Agosto 2026» (pagina risk-analysis/6a902f03cc23128bf9be9efc) fatti da Davide con Claude Desktop: controlli ↔ asset e record asset × controllo (stato Plan/Do/nessuna). Minacce, vulnerabilità, probabilità e owner non visibili nell'export; manca l'asset A0031. I due CSV sono salvati in `docs/B_REGISTRAZIONI/Analisi dei Rischi/2026/` (ERA-controlli-vs-asset-Agosto-2026.csv, ERA-record-Agosto-2026.csv) e collegati dall'index della cartella.
- **SoA rev 0.2** (Da approvare): «X» nella colonna Rischio della sorgente per i **77 controlli** collegati ad almeno un asset in ERA (motivo R); 5.3 (ERA Plan), 8.3 (ERA nessuna), 8.5 (T1), 8.9 (ERA nessuna: è la vulnerabilità dei 5 asset a 45), 8.13 (T2), 8.15 (ERA Do solo su 4 asset su 40) passati a «non attuato», con motivazione in testa alla descrizione. Ora 55 attuati, 35 non attuati, 3 esclusi. Riga di revisione in `tools/genera_soa.py`, vista rigenerata.
- Senza asset collegati in ERA, quindi senza R: 5.5, 5.6, 5.7, 6.2, 6.5, 6.7, 8.13, 8.17, 8.25, 8.28, 8.31, 8.33, 8.34 (più i 3 esclusi). 8.13 e i controlli di sviluppo sicuro sono probabilmente una lacuna del collegamento in ERA.
- Non allineati e lasciati come sono: 5.1, 5.12, 5.13 «non attuati» nella SoA ma «Do» in ERA; 7.13, 8.18, 8.20, 8.23 «non attuati» e «nessuna» in ERA (coperti dal piano).
- **MDPR33.1.B rev 0.1** (Da approvare): colonne «Asset ERA ridotti (rischio)» (asset a 45 e numero di asset sotto soglia) ed «Esito» (T8 fatto, T1 in corso, le altre aperte); T13 generica suddivisa in T13–T27 (5.28, 5.33, 5.35, 5.36, 6.1, 6.4, 7.2, 7.3, 7.4, 7.6, 7.8, 7.9, 7.10, 7.14, 8.23); aggiunte T28–T30 (5.3, 8.3, 8.15). Tutti i 35 controlli non attuati hanno un'azione. Responsabili e scadenze di T13–T30 «da confermare AU» (proposta 12/12/2026). Sezioni di Nextage (§2, §3.1) invariate.
- Le azioni che toccano tutti e 5 gli asset a 45 sono T1, T3, T4, T5, T7, T9, T11, T12, T14, T19, T29, T30; le più rilevanti per abbassarli sono T5 e T7 (5.37, 8.9: gestione delle configurazioni).

