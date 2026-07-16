# Stato progetto: migrazione documentazione SGI su GitHub

Nota di lavoro aggiornata al 2026-07-09. Serve come promemoria per riprendere il lavoro da VS Code senza dover ripercorrere tutta la chat.

## Obiettivo

Spostare la documentazione ISO di Vectorlab da Google Drive (Word/Excel, organizzata in sottocartelle di stato Working/Da Approvare/Ultima Versione/Obsolete) a GitHub in formato Markdown, con MkDocs per la navigazione via browser. Motivazione originale (CTO): avere una visione d'insieme e poter usare un LLM per scovare incongruenze tra documenti.

## Repository

`https://github.com/davideruzzenenti/Vectorlab-SGI.git` — **passato a privato il 16/07/2026** (prima era pubblico). Conseguenza: GitHub Pages (piano Free) non funziona più su repo privato — il sito `davideruzzenenti.github.io/Vectorlab-SGI/` risulta 404 finché non si sceglie tra tornare pubblico o passare a GitHub Pro (vedi "Cose da sapere" e "Prossimi passi").

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

**Risultato**: `STATO-DOCUMENTAZIONE.html` (alla root del repo) — dashboard con tabella filtrabile di 114 documenti valutati, i 10 problemi con impatto maggiore, e i 33 documenti citati ma mai creati (in gran parte l'intero blocco tecnologico: gestione accessi, crittografia, minacce/vulnerabilità, sviluppo sicuro, reti, configurazioni, patch). Aprire il file in un browser per consultarla.

**In sintesi**: 24 documenti pronti così come sono, 40 template vuoti normali da popolare, 44 con difetti concreti (placeholder mai risolti, riferimenti incrociati rotti tra documenti, contraddizioni interne), 33 mai creati. I problemi più seri: `PO20` ha l'80% del testo che parla di Gestione delle Configurazioni invece che di Capacità (copia-incolla sbagliato dal template); `PR27.1` e i suoi allegati trattano il DPO come obbligatorio, contraddicendo la revisione già fatta su `PO31`; i moduli di emergenza fisica (`MDPR18.1.F/G/H`) hanno ancora "Nome Cognome" non compilato (gap di conformità D.Lgs 81/08, non solo carta); sospetti residui di un altro cliente del consulente (date "05/2009" e "15/03/2021", "NOME AZIENDA" al posto di Vectorlab in più atti) da verificare.

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
- [ ] Riconciliare le note appena importate nella SOA con i riferimenti documentali già presenti (alcune si contraddicono, es. 5.35, probabilmente 5.12/5.13)
- [x] Repo passato a privato (16/07/2026) — decidere se tornare pubblico o passare a GitHub Pro per riavere Pages attivo (vedi sezione Repository)
- [ ] Consultare `STATO-DOCUMENTAZIONE.html` e decidere l'ordine di lavoro sui 44 documenti da correggere e i 33 mancanti
- [ ] Correggere `PO20` (contenuto sbagliato), `PR27.1`+allegati (DPO trattato come obbligatorio, da allineare a `PO31`), moduli di emergenza fisica (nominativi mancanti)
- [ ] Verificare se ci sono davvero residui di un altro cliente del consulente (date sospette, "NOME AZIENDA" al posto di Vectorlab)
- [ ] Fase 2 (idea originale del CTO, non ancora iniziata): usare un LLM di grosse dimensioni per scandagliare il corpus consolidato e individuare incongruenze tra documenti — ora fattibile perché tutto è in un unico formato strutturato e ragionevolmente pulito
