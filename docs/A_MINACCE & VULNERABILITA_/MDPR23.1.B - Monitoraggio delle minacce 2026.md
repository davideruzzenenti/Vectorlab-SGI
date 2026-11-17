# MDPR23.1.B - Monitoraggio delle minacce 2026

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0 | 17/11/2026 | Emissione | RSGI | Da approvare |

Registrazione prevista da PR23.1 §5. Si aggiorna una volta l'anno, prima
del Riesame della Direzione.

**Fonti consultate**: ACN, sintesi operativa 2026; Clusit, Rapporto 2026;
ENISA, Threat Landscape 2025; MITRE ATT&CK (estrazione maggio 2026).

<span style="color:#B3392A">**Bozza.** La colonna «Rischio in ERA» va
completata confrontando la tabella con l'analisi dei rischi 2026
[DA VERIFICARE con Nextage].</span>

| # | Minaccia (fonte) | Perché riguarda Vectorlab | Misure in essere | Rischio in ERA | Azione |
| --- | --- | --- | --- | --- | --- |
| 1 | Phishing e furto di credenziali (ACN, ENISA, Clusit) | Tutto il lavoro passa dagli account Google aziendali, che danno accesso anche a GitHub e ClickUp | Password secondo REG01; formazione | [DA VERIFICARE] | Verifica in due passaggi obbligatoria (al 17/11 nessun account la usa): decisione del 18/11 |
| 2 | Compromissione della casella di posta e frodi con finte fatture o cambio IBAN (ACN) | L'Amministrazione riceve fatture e richieste di pagamento via mail | — | [DA VERIFICARE] | Regola: ogni cambio di IBAN di un fornitore si conferma per telefono a un numero già noto [DA CONFERMARE con Francesco] |
| 3 | Malware e ransomware sui portatili (ACN, Clusit) | Ogni persona lavora su un portatile Windows | Antivirus, aggiornamenti, disco cifrato (REG01 §3); dati su cloud (PR21.1) | [DA VERIFICARE] | Nessuna |
| 4 | Sfruttamento di falle su servizi esposti su internet (ACN, ENISA, Clusit) | Il server Aruba ospita siti, n8n e Bitwarden raggiungibili da internet | Aggiornamenti (PR32.1 §7) | [DA VERIFICARE] | Scansione annuale del server (PR23.1 §6) [DA CONFERMARE con Andrei] |
| 5 | Librerie open source vulnerabili o compromesse (MITRE, Supply Chain Compromise) | Il team sviluppa software con librerie di terze parti, anche per i clienti | Revisione del codice (PO25) | [DA VERIFICARE] | Attivare gli avvisi Dependabot sui repository [DA CONFERMARE con Andrea] |
| 6 | Chiavi e password finite nel codice o in repository pubblici (MITRE, Unsecured Credentials) | I repository GitHub contengono configurazioni; il repo SGI è pubblico | Credenziali in Bitwarden (REG01 §2) | [DA VERIFICARE] | Attivare il secret scanning di GitHub; nel repo SGI nessun dettaglio dell'infrastruttura |
| 7 | Errori di configurazione e condivisioni troppo aperte (ACN, Misconfiguration) | Documenti di clienti su Google Drive, condivisibili con link | Classificazione delle informazioni (PO15) | [DA VERIFICARE] | Nella revisione semestrale degli accessi (PR16.1 §6) controllare anche i file condivisi con «chiunque abbia il link» |
| 8 | Fuga di dati tramite strumenti di intelligenza artificiale | Il team usa strumenti AI nello sviluppo | Solo strumenti autorizzati (PR35.1 §2.3) | [DA VERIFICARE] | Nessuna |
| 9 | Guasto o indisponibilità di un fornitore (ACN, Guasto) | Il lavoro dipende da Google, GitHub e Aruba | Backup del server (PR21.1) | [DA VERIFICARE] | Decisione su copia esterna di GitHub (18/11) |
| 10 | Furto o perdita del portatile | Portatili usati anche fuori sede | Disco cifrato, blocco schermo (REG01 §3) | [DA VERIFICARE] | Nessuna |

**Conclusione per il Riesame della Direzione 2026**: le minacce più
rilevanti per Vectorlab sono quelle legate agli account (1, 2) e al
software sviluppato (5, 6). Le azioni aperte sono la verifica in due
passaggi, la scansione del server e i controlli automatici su GitHub.
