# MDPR28.1.A - BIA_Business Impact Analysis (27001)

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** | **Classificazione** |
| -------- | ---------- | --------------- | ----------- | ------------- | ------------------- |
| 0.0      | 24/04/2026 | Prima emissione (modello) | | | Interno |
| 0.1      | 11/11/2026 | Prima compilazione in forma minima, proporzionata a Vectorlab: servizi da cui dipende il lavoro, impatto di un'interruzione e decisione. Per tutti i servizi si accetta il rischio (proposta di RSGI dell'11/11/2026, da approvare dall'Amministratore Unico); per il server Aruba, oggi senza backup, l'accettazione riguarda anche la perdita definitiva dei dati. Tolte le tabelle del modello (scale RTO/MTPD per processo), non usate | RSGI | Da approvare (Amministratore Unico) | Interno |

## 1 Scopo e metodo

La BIA (analisi dell'impatto di un'interruzione) individua i servizi da
cui dipende il lavoro di Vectorlab, cosa succede se si fermano e cosa
decide la Direzione. Risponde a ISO/IEC 27001 A.5.29 (Sicurezza delle
informazioni durante un'interruzione) e A.5.30 (Preparazione dell'ICT per
la continuità operativa) e alimenta la valutazione dei rischi (PR33.1).

Vectorlab è una piccola azienda che lavora inserita nei progetti dei
clienti, con gli strumenti e gli ambienti dei clienti (PO02 §4, PR35.1):
un'interruzione dei servizi interni rallenta il lavoro di Vectorlab ma
non ferma i servizi dei clienti. Per questo la BIA non usa scale
temporali per processo (RTO, MTPD), ma una valutazione qualitativa per
servizio, fatta dalla Direzione con RSGI.

## 2 Dati della BIA

| Voce | Contenuto |
| --- | --- |
| Ambito | Servizi e strumenti usati da Vectorlab nel campo di applicazione del SGI (PO02 §4) |
| Data di compilazione | 11/11/2026 |
| Redattore | RSGI (Davide Ruzzenenti) |
| Decisione | Amministratore Unico (Andrea Ruzzenenti) |
| Prossima revisione | Prima del Riesame della Direzione 2027, o prima se cambiano servizi o modo di lavorare |

## 3 Servizi, impatto e decisione

| # | Servizio | Impatto se si interrompe | Impatto sui clienti | Decisione |
| --- | --- | --- | --- | --- |
| 1 | Google Workspace (posta, Drive) | Mail e documenti di commessa non raggiungibili; lavoro rallentato | Nessuno diretto: il team lavora negli strumenti del cliente | **Rischio accettato**: il servizio dipende interamente dal fornitore e Vectorlab non ha leve per ridurlo |
| 2 | GitHub (organizzazione vectorlab-cg) | Codice su vectorlab-cg non raggiungibile | Nessuno diretto: il codice principale sta nei repository dei clienti | **Rischio accettato**, come sopra |
| 3 | ClickUp | CRM, task, commesse e registro NC non raggiungibili | Nessuno | **Rischio accettato**, come sopra |
| 4 | Bitwarden | Password e chiavi non accessibili | Possibile ritardo sui progetti | **Rischio accettato**, come sopra |
| 5 | Server dedicato Aruba (n8n, siti, gestione delle credenziali) | Automazioni ferme, siti non raggiungibili (es. NC01, ottobre 2026). **Oggi non ci sono backup: un guasto grave comporta la perdita definitiva di n8n, del vault delle credenziali e della configurazione** | Nessuno: il server non ospita servizi o dati dei clienti | **Rischio accettato, compresa la perdita definitiva dei dati**. Da riesaminare se il server inizia a ospitare servizi o dati dei clienti |
| 6 | Portatile di uno sviluppatore | Una persona ferma finché non ha un'altra macchina | Ritardo limitato | **Rischio accettato**: si lavora su un altro portatile o sulla macchina del cliente; il codice non sta solo sul portatile |
| 7 | Connessione internet dell'ufficio | Ufficio senza rete | Nessuno | **Rischio accettato**: si lavora da casa (ALPR05.1.E) |

## 4 Conseguenze sulla continuità operativa

- Non sono previsti piani di continuità specifici (ALPR28.1.A) né test
  periodici (MDPR28.1.B), perché per nessun servizio è stato deciso un
  trattamento: non c'è una soluzione di ripristino da provare.
- Un'interruzione reale si registra come evento nella lista ClickUp
  «Non conformità e miglioramento» (PR27.1, PR13.1) e si riesamina qui
  alla revisione successiva.
- I rischi accettati sono riportati nel Riesame della Direzione (PR12.1).

## 5 Approvazione

L'accettazione dei rischi del §3 è approvata dall'Amministratore Unico
nell'approvazione dei documenti di fine stage 1 (mail di conferma
archiviata in B_REGISTRAZIONI).
