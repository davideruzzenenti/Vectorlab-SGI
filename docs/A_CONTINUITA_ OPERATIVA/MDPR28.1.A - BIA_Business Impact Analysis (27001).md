# MDPR28.1.A - BIA_Business Impact Analysis (27001)

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** | **Classificazione** |
| -------- | ---------- | --------------- | ----------- | ------------- | ------------------- |
| 0.0 | 17/11/2026 | Emissione | RSGI | Da approvare | Interno |

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
| 4 | Bitwarden | Password e chiavi non accessibili | Possibile ritardo sui progetti | Ospitato sul server Aruba: **trattato** con la copia del server e l'esportazione cifrata (PR21.1) |
| 5 | Server dedicato Aruba (n8n, siti, Bitwarden) | Automazioni ferme, siti non raggiungibili (es. NC01, ottobre 2026); senza copia, un guasto grave comporterebbe la perdita di n8n, del vault delle credenziali e della configurazione | Nessuno: il server non ospita servizi o dati dei clienti | **Trattato** (decisione del 17/11/2026): copia completa del server e prova di ripristino una volta l'anno (PR21.1, PR28.1 §7). Copie in attivazione: data da confermare con il System Administrator; prima prova entro il 15/12/2026 |
| 6 | Portatile di uno sviluppatore | Una persona ferma finché non ha un'altra macchina | Ritardo limitato | **Rischio accettato**: si lavora su un altro portatile o sulla macchina del cliente; il codice non sta solo sul portatile |
| 7 | Connessione internet dell'ufficio | Ufficio senza rete | Nessuno | **Rischio accettato**: si lavora da casa (ALPR05.1.E) |

## 4 Conseguenze sulla continuità operativa

- Il server Aruba è l'unico servizio trattato: il suo piano di ripristino
  è la copia completa con prova annuale (PR21.1; PR28.1 §7).
- Per gli altri servizi il rischio è accettato: non ci sono piani di
  ripristino da provare.
- Un'interruzione reale si gestisce secondo PR28.1 §6, si registra nella
  lista ClickUp «Non conformità e miglioramento» (PR13.1) e si riesamina
  qui alla revisione successiva.
- I rischi accettati sono riportati nel Riesame della Direzione (PR12.1).

## 5 Approvazione

L'accettazione dei rischi del §3 è approvata dall'Amministratore Unico
nell'approvazione dei documenti di fine stage 1 (mail di conferma
archiviata in B_REGISTRAZIONI).
