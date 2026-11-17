# MDPR23.1.B - Monitoraggio delle minacce 2026

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0 | 17/11/2026 | Emissione | RSGI | Da approvare |

Registrazione prevista da [PR23.1](PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche.md) §5. Si aggiorna una volta l'anno, prima
del Riesame della Direzione.

**Fonti consultate**: ACN, sintesi operativa 2026; Clusit, Rapporto 2026;
ENISA, Threat Landscape 2025; MITRE ATT&CK (estrazione maggio 2026).

<span style="color:#B3392A">**Bozza.** La colonna «Rischio in ERA» va
completata confrontando la tabella con l'analisi dei rischi 2026
[DA VERIFICARE con Nextage].</span>

| # | Minaccia (fonte) | Perché riguarda Vectorlab | Misure in essere | Rischio in ERA | Azione |
| --- | --- | --- | --- | --- | --- |
| 1 | Phishing e furto di credenziali (ACN, ENISA, Clusit) | Tutto il lavoro passa dagli account Google aziendali, che danno accesso anche a GitHub e ClickUp | Password secondo [REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md); formazione | [DA VERIFICARE] | Verifica in due passaggi obbligatoria su tutti gli account ([REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §2) |
| 2 | Compromissione della casella di posta e frodi con finte fatture o cambio IBAN (ACN) | L'Amministrazione riceve fatture e richieste di pagamento via mail | — | [DA VERIFICARE] | Regola: ogni cambio di IBAN di un fornitore si conferma per telefono a un numero già noto [DA CONFERMARE con Francesco] |
| 3 | Malware e ransomware sui portatili (ACN, Clusit) | Ogni persona lavora su un portatile Windows | Antivirus, aggiornamenti, disco cifrato ([REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §3); dati su cloud ([PR21.1](../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore.md)) | [DA VERIFICARE] | Nessuna |
| 4 | Sfruttamento di falle su servizi esposti su internet (ACN, ENISA, Clusit) | Il server Aruba ospita siti, n8n e Bitwarden raggiungibili da internet | Aggiornamenti ([PR32.1](../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT.md) §7) | [DA VERIFICARE] | Scansione annuale del server ([PR23.1](PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche.md) §6) [DA CONFERMARE con Andrei] |
| 5 | Librerie open source vulnerabili o compromesse (MITRE, Supply Chain Compromise) | Il team sviluppa software con librerie di terze parti, anche per i clienti | Revisione del codice ([PO25](../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro.md)) | [DA VERIFICARE] | Attivare gli avvisi Dependabot sui repository [DA CONFERMARE con Andrea] |
| 6 | Chiavi e password finite nel codice o in repository pubblici (MITRE, Unsecured Credentials) | I repository GitHub contengono configurazioni; il repo SGI è pubblico | Credenziali in Bitwarden ([REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §2) | [DA VERIFICARE] | Attivare il secret scanning di GitHub; nel repo SGI nessun dettaglio dell'infrastruttura |
| 7 | Errori di configurazione e condivisioni troppo aperte (ACN, Misconfiguration) | Documenti di clienti su Google Drive, condivisibili con link | Classificazione delle informazioni ([PO15](../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni.md)) | [DA VERIFICARE] | Nella revisione semestrale degli accessi ([PR16.1](../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md) §6) controllare anche i file condivisi con «chiunque abbia il link» |
| 8 | Fuga di dati tramite strumenti di intelligenza artificiale | Il team usa strumenti AI nello sviluppo | Solo strumenti autorizzati ([PR35.1](../8.2_PRODOTTI%20%26%20SERVIZI/PR35.1%20-%20Digital.md) §2.3) | [DA VERIFICARE] | Nessuna |
| 9 | Guasto o indisponibilità di un fornitore (ACN, Guasto) | Il lavoro dipende da Google, GitHub e Aruba | Backup del server ([PR21.1](../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore.md)) | [DA VERIFICARE] | Decisione su copia esterna di GitHub (18/11) |
| 10 | Furto o perdita del portatile | Portatili usati anche fuori sede | Disco cifrato, blocco schermo ([REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §3) | [DA VERIFICARE] | Nessuna |

**Conclusione per il Riesame della Direzione 2026**: le minacce più
rilevanti per Vectorlab sono quelle legate agli account (1, 2) e al
software sviluppato (5, 6). Le azioni aperte sono la verifica in due
passaggi, la scansione del server e i controlli automatici su GitHub.
