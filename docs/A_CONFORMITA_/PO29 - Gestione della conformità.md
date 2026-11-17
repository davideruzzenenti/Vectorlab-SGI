# PO29 - Gestione della conformità

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0 | 17/11/2026 | Emissione | RSGI | Da approvare |

## 1 Scopo

Stabilisce come Vectorlab individua i requisiti di legge, contrattuali e
volontari che riguardano il Sistema di Gestione Integrato, come li
rispetta e come verifica di rispettarli.

## 2 Campo di applicazione

Tutto il personale e i collaboratori esterni che lavorano nel campo di
applicazione del Sistema di Gestione.

## 3 Riferimenti

- ISO 9001:2026 e ISO/IEC 27001:2024+A1, 4.2 Comprendere le esigenze e
  le aspettative delle parti interessate
- 27001:2024+A1, Allegato A: 5.28 Raccolta di prove, 5.31 Requisiti
  legali, statutari, regolamentari e contrattuali, 5.32 Diritti di
  proprietà intellettuale, 5.33 Protezione delle registrazioni, 5.34
  Privacy e protezione dei dati personali, 5.35 Riesame indipendente della
  sicurezza delle informazioni, 5.36 Conformità alle politiche, alle regole
  e agli standard per la sicurezza delle informazioni
- MDPO29.C – Elenco leggi, regolamenti e norme applicabili
- PO31 – Misure di sicurezza per la protezione dei dati personali e
  procedure PR31.1–PR31.4
- PO15 – Classificazione delle informazioni; MDPO15.A – Data Retention
- PR11.1 – Audit Interno; MDPR11.1.A – Programma Audit
- PR26.1 – Gestione dei fornitori; PR27.1 – Gestione Incidenti e Data
  Breach

## 4 Responsabilità

| Ruolo | Compiti |
| --- | --- |
| Amministratore Unico | Risponde della conformità dell'azienda; firma i contratti; decide se serve una consulenza legale |
| RSGI | Tiene aggiornato il registro MDPO29.C e verifica la conformità con gli audit interni |
| Referente Privacy | Segue gli adempimenti GDPR e i rapporti con il Garante (PO31) |
| Amministrazione | Tiene contratti, accordi di riservatezza e l'inventario delle licenze e degli abbonamenti software |
| Responsabili di Area | Segnalano a RSGI nuovi requisiti di clienti, bandi o progetti |

## 5 Requisiti applicabili

1. Il registro MDPO29.C elenca leggi, regolamenti e norme volontarie che
   riguardano Vectorlab, con i documenti del sistema che li attuano e chi
   ne segue gli aggiornamenti.
2. RSGI lo riesamina una volta l'anno, prima del Riesame della Direzione,
   e quando entra in vigore una norma rilevante o cambia l'attività
   (nuovo tipo di cliente, bando pubblico, nuovo servizio).
3. Per tenersi aggiornati si consultano le fonti ufficiali indicate in
   MDPO29.C (es. Gazzetta Ufficiale, Garante Privacy, EUR-Lex) e, quando
   serve, consulenti legali esterni.
4. I **requisiti contrattuali** di clienti e fornitori (riservatezza,
   sicurezza, trattamento dei dati) si individuano alla firma del
   contratto: il PM li riporta al team e, se richiedono misure nuove, a
   RSGI.

## 6 Proprietà intellettuale e licenze

- Si usa solo software con licenza valida, di origine nota, installato
  secondo REG01 e la Lista software permessi (ALPR05.1.G).
- L'Amministrazione tiene l'inventario delle licenze e degli abbonamenti
  intestati a Vectorlab, con scadenze e assegnatari, e una volta l'anno
  ne verifica l'uso e i rinnovi.
- Codice, documenti e materiali dei clienti restano di proprietà del
  cliente secondo il contratto e si usano solo per il progetto. Il codice
  open source si usa rispettandone la licenza.
- Testi, immagini e video di terzi si usano solo con i diritti necessari.

## 7 Protezione delle registrazioni

Le registrazioni del Sistema di Gestione e quelle richieste dalla legge
(contabili, del personale, privacy) si conservano per i tempi di
MDPO15.A, protette con gli accessi di PR16.1 e i backup di PR21.1. Non si
cancellano prima della scadenza e, alla scadenza, si eliminano in modo
sicuro.

## 8 Dati personali

Vectorlab rispetta il GDPR con le misure di PO31 e le procedure collegate:
registri dei trattamenti (PR31.4), diritti degli interessati (PR31.1),
consensi (PR31.2), valutazione d'impatto quando necessaria (PR31.3),
nomine dei responsabili del trattamento (PR26.1) e gestione dei data
breach (PR27.1). Il Referente Privacy coordina queste attività.

## 9 Crittografia e paesi esteri

In Italia e nell'Unione europea l'uso della crittografia non ha limiti
particolari. Se un progetto comporta l'invio di software o dati cifrati
verso paesi extra UE, il PM verifica con il CTO eventuali limiti
all'esportazione o all'uso della crittografia in quel paese.

## 10 Prove in caso di incidente

Se un incidente può avere conseguenze legali o disciplinari, si
conservano log, mail e file interessati senza modificarli, annotando chi
li ha raccolti e quando, secondo PR27.1. Per i servizi cloud si usano gli
strumenti di esportazione del fornitore (es. console di Google Workspace).

## 11 Verifica della conformità

- **Audit interni** (PR11.1): almeno una volta l'anno verificano il
  rispetto delle norme ISO, delle procedure e dei requisiti di MDPO29.C.
  Sono svolti da auditor indipendenti dalle attività verificate e valgono
  come riesame indipendente della sicurezza delle informazioni (A.5.35).
- **Verifiche tecniche** pianificate in MDPR11.1.A §6: revisione degli
  accessi, operato degli amministratori di sistema, prove di ripristino,
  scansioni delle vulnerabilità.
- **Ente di certificazione**: dopo la certificazione, le verifiche annuali
  dell'ente.
- Le non conformità trovate si gestiscono secondo PR13.1.

## 12 Ispezioni delle autorità

In caso di ispezione (es. Garante Privacy, Ispettorato del lavoro,
Guardia di Finanza) si avvisano subito l'Amministratore Unico e, per la
privacy, il Referente Privacy. Si forniscono i documenti richiesti dopo
averne verificato la richiesta formale; si annota cosa è stato consegnato.

## 13 Registrazioni

| Registrazione | Dove | Chi | Conservazione |
| --- | --- | --- | --- |
| Elenco leggi, regolamenti e norme (MDPO29.C) | Repo SGI | RSGI | Sempre aggiornato; versioni precedenti in git |
| Inventario di licenze e abbonamenti | Archivio dell'Amministrazione | Amministrazione | Durata della licenza + 1 anno |
| Contratti e accordi di riservatezza | Archivio dell'Amministrazione | Amministrazione | 10 anni dalla fine del contratto |
| Rapporti di audit e verifiche tecniche | PR11.1; MDPR11.1.A | RSGI | 3 anni |
