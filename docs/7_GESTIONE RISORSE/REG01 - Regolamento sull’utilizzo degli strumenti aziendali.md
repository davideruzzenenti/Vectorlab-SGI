# REG01 - Regolamento sull’utilizzo degli strumenti aziendali

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0      | 24/04/2026 | Prima emissione (modello) | CISO | CEO |
| 0.1      | 27/10/2026 | Riscritto sugli strumenti reali: portatili forniti da Vectorlab con 4 requisiti minimi verificati da ciascuno in autonomia, account aziendali con verifica in due passaggi, Bitwarden, regole su dati e codice dei clienti, segnalazioni a sicurezza@. Tolti i riferimenti a strumenti inesistenti (ticketing, firewall con filtri, NAS, VPN, sfondi); uscita allineata a PR05.1 (casella 6 mesi) | RSGI | Da approvare |

## 1 Scopo e destinatari

Il regolamento dice come si usano gli strumenti di lavoro di Vectorlab
per proteggere le informazioni dell'azienda e dei clienti. Vale per
dipendenti e collaboratori, compreso l'IT esterno, e per ogni
strumento usato per lavoro: portatili forniti da Vectorlab, account
aziendali, smartphone personali usati per la posta, macchine e
strumenti dei clienti.

È parte del pacchetto *ALPR05.1.H - Documenti per il personale*:
ognuno ne conferma la lettura all'ingresso e ogni anno (PR05.1).

Per i dettagli tecnici si rimanda a PO16 e PR16.1 (accessi), PO17
(crittografia), PR27.1 (incidenti), PR35.1 (lavoro presso i clienti).

## 2 Account e credenziali

1. Per lavoro si usa solo l'account aziendale **@vectorlab-cg.com**,
   anche per accedere a ClickUp, GitHub e agli altri servizi. Non si
   usano caselle personali per lavoro.
2. La **verifica in due passaggi** è obbligatoria sull'account Google
   aziendale e, dove disponibile, su GitHub e sugli altri servizi.
3. Le credenziali di lavoro (anche quelle ricevute dai clienti) si
   custodiscono in **Bitwarden**. Non si scrivono su file, note o
   messaggi.
4. Password: lunghe (almeno 12 caratteri, meglio una frase), diverse
   per ogni servizio, mai riusate da account personali. Non serve
   cambiarle a scadenza fissa: si cambiano subito se c'è il sospetto
   che qualcuno le conosca.
5. Le credenziali sono personali: **non si condividono account**.
   Un account condiviso esistente va segnalato a RSGI, che lo
   gestisce come rischio fino alla sua eliminazione.

## 3 Portatili forniti da Vectorlab

Ogni persona lavora su un portatile fornito da Vectorlab e ne è
responsabile. Il portatile deve avere sempre:

1. **disco cifrato** (BitLocker o «Crittografia dispositivo» di
   Windows); la chiave di ripristino si salva nel Bitwarden aziendale,
   così l'azienda può recuperare i dati se serve;
2. **password o PIN** all'accesso e **blocco automatico dello
   schermo**;
3. **aggiornamenti automatici** di Windows attivi;
4. **antivirus attivo** (Microsoft Defender è sufficiente).

**Controllo.** Ogni persona verifica da sola i 4 requisiti
all'assegnazione del portatile e poi una volta l'anno, e lo registra
nel proprio sottotask di presa visione (lista ClickUp «Consapevolezza e
formazione», PR05.1) indicando modello e numero di serie del portatile.
Questi sottotask formano l'inventario dei portatili. RSGI può
verificare a campione.

Regole d'uso:

- il portatile è personale: non si presta e non si usa con account
  condivisi;
- gli sviluppatori sono amministratori del proprio portatile perché
  devono installare strumenti di sviluppo; installano solo software da
  fonti ufficiali e con licenza valida (ALPR05.1.G - Lista software
  permessi), mai software pirata, e non disattivano i 4 requisiti;
- si blocca lo schermo (Windows + L) ogni volta che ci si allontana;
- fuori sede il portatile non si lascia incustodito, né in auto in
  vista.

All'uscita dall'azienda il portatile si restituisce; l'IT cancella i
dati prima di riassegnarlo o dismetterlo (PR05.1).

## 4 Smartphone personali

È possibile usare il proprio smartphone per posta, calendario e
ClickUp aziendali se ha:

- blocco con PIN, password o biometria;
- sistema operativo aggiornato;
- app solo dagli store ufficiali.

Non si salvano sul telefono allegati con dati dei clienti o dati
personali. In caso di perdita o furto si segnala subito (§8): l'IT
disconnette l'account aziendale dal telefono dalla console di Google.

## 5 Strumenti ammessi

| Uso | Strumento |
| --- | --- |
| Posta, calendario, documenti, videochiamate | Google Workspace (account aziendale) |
| Codice | GitHub, organizzazione Vectorlab; o repository del cliente |
| Attività, commesse, non conformità | ClickUp |
| Credenziali | Bitwarden |
| Intelligenza artificiale | Solo gli strumenti autorizzati in PR35.1 §2.3 |

Un nuovo servizio che tratta informazioni aziendali o dei clienti si
attiva solo con l'accordo del CTO, che lo fa registrare
nell'inventario degli asset e, se serve, tra i fornitori (PR26.1).

**Messaggistica.** Le decisioni e i passaggi di lavoro (per esempio
«ho acquistato il certificato, va installato») si registrano in un
task ClickUp o per mail, non in chat. Le app di messaggistica servono
solo per comunicazioni veloci e non devono contenere credenziali, dati
personali o informazioni dei clienti. [DA DECIDERE: quale app di
messaggistica è ammessa; Discord non è accettato dal sistema di
gestione.]

## 6 Posta elettronica

- La casella aziendale si usa per lavoro; l'uso personale è
  occasionale.
- Prima di inviare si controllano i destinatari. Una mail ricevuta per
  errore si segnala al mittente e si cancella.
- Documenti con dati personali o informazioni riservate si
  condividono con un link Drive con accesso limitato alle persone
  necessarie, non come allegato aperto.
- Mail sospette (link o allegati inattesi, richieste urgenti di
  pagamenti o credenziali): non si aprono, si inoltrano a
  sicurezza@vectorlab-cg.com.
- Assenze programmate: risposta automatica con data di rientro e un
  contatto alternativo.
- Firma: nome, ruolo, Vector Lab S.r.l., sito.

## 7 Dati dell'azienda e dei clienti

1. Le informazioni aziendali si salvano su Google Drive o GitHub
   dell'organizzazione, non solo sul portatile. Copie locali solo per
   il tempo necessario.
2. Per dati e codice dei clienti valgono prima di tutto le regole del
   cliente (offerta, NDA, istruzioni): se il cliente vieta di portarli
   fuori dai suoi strumenti, si lavora solo lì (PR35.1 §2.3).
3. Sulle macchine e sugli strumenti del cliente si seguono le regole
   del cliente.
4. Mai dati personali o codice dei clienti in strumenti di IA non
   autorizzati o in account personali.
5. La condivisione dei file su Drive va tenuta aggiornata: si tolgono
   gli accessi quando non servono più.
6. A fine commessa si cancellano copie locali, ambienti e demo con
   dati del cliente, salvo diverso accordo (PR35.1 §2.5).

## 8 Incidenti, perdita o furto

Si segnala **subito** a **sicurezza@vectorlab-cg.com** (per le urgenze
si telefona all'IT esterno o al CISO):

- perdita o furto di portatile o smartphone;
- credenziali esposte o sospetto accesso al proprio account;
- mail sospetta aperta, comportamento anomalo del PC;
- dati inviati alla persona sbagliata.

In caso di furto si fa anche denuncia e se ne invia copia al CISO. Si
cambiano subito le password dei servizi usati da quel dispositivo. La
gestione segue PR27.1.

## 9 Ufficio

- Scrivania e schermo puliti: documenti riservati non lasciati in
  vista, schermo bloccato quando ci si allontana.
- Gli ospiti sono accompagnati e non usano i portatili aziendali.
- Le chiavi della sede sono personali; consegna e restituzione
  nel registro MDPR05.1.U.
- I documenti cartacei riservati si distruggono, non si buttano interi.
- [DA CONFERMARE con l'IT: rete Wi-Fi dell'ufficio (rete ospiti
  separata o no) e stampante.]

## 10 Controlli della Società

Gli strumenti descritti sono strumenti di lavoro. Vectorlab non usa
strumenti di controllo a distanza dell'attività delle persone e non
legge il contenuto della posta o dei file.

Gli amministratori possono vedere, per sicurezza e gestione: gli
accessi e le attività registrate dalla console di Google Workspace,
dagli strumenti di ClickUp e GitHub, lo stato dei portatili (cifratura,
aggiornamenti) durante i controlli dell'IT. Questi dati si usano solo
per sicurezza, gestione degli incidenti e degli accessi, nel rispetto
dell'art. 4 della L. 300/1970 e del Regolamento UE 2016/679;
l'informativa ai dipendenti è *ALPR31.2.A*.

L'accesso alla casella di una persona assente o uscita segue PR05.1
(«Casella email e account Google Workspace»).

Le violazioni del regolamento possono avere conseguenze disciplinari
secondo il contratto collettivo applicato (REG02).

## 11 Riferimenti alle norme

| Requisito | Dove nel regolamento |
| --- | --- |
| ISO/IEC 27001:2022, A.5.10 Utilizzo accettabile delle informazioni e degli altri asset associati | §5, §6, §7 |
| ISO/IEC 27001:2022, A.5.17 Informazioni di autenticazione | §2 |
| ISO/IEC 27001:2022, A.6.7 Lavoro da remoto | §3, §4 |
| ISO/IEC 27001:2022, A.6.8 Segnalazione degli eventi relativi alla sicurezza delle informazioni | §8 |
| ISO/IEC 27001:2022, A.7.7 Scrivania pulita e schermo pulito | §3, §9 |
| ISO/IEC 27001:2022, A.7.9 Sicurezza degli asset all'esterno delle sedi | §3 |
| ISO/IEC 27001:2022, A.8.1 Dispositivi terminali degli utenti | §3, §4 |
| ISO/IEC 27001:2022, A.8.7 Protezione contro il malware | §3 |
| L. 300/1970, art. 4; Regolamento UE 2016/679 | §10 |

I titoli dei controlli sono da verificare sul testo UNI CEI EN ISO/IEC
27001:2024+A1:2024.
