# MDPR23.1.B - Monitoraggio delle minacce 2026

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0 | 25/11/2026 | Emissione | RSGI | Da approvare |

Registrazione prevista da [PR23.1](PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche.md) §5. Si aggiorna una volta l'anno, prima
del Riesame della Direzione.

**Fonti consultate**: ACN, sintesi operativa 2026; Clusit, Rapporto 2026;
ENISA, Threat Landscape 2025; MITRE ATT&CK (estrazione maggio 2026).

| # | Minaccia (fonte) | Perché riguarda Vectorlab | Misure in essere | Azione |
| --- | --- | --- | --- | --- |
| 1 | Phishing e furto di credenziali (ACN, ENISA, Clusit) | Tutto il lavoro passa dagli account Google aziendali, che danno accesso anche a GitHub e ClickUp | Password secondo [REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md); verifica in due passaggi obbligatoria su tutti gli account dal 24/11/2026 ([REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §2); formazione | Nessuna |
| 2 | Compromissione della casella di posta e frodi con finte fatture o cambio IBAN (ACN) | L'Amministrazione riceve fatture e richieste di pagamento via mail | Ogni cambio di IBAN di un fornitore si conferma per telefono a un numero già noto (Amministrazione) | Nessuna |
| 3 | Malware e ransomware sui portatili (ACN, Clusit) | Ogni persona lavora su un portatile Windows | Antivirus, aggiornamenti, disco cifrato ([REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §3); dati su cloud ([PR21.1](../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore.md)) | Nessuna |
| 4 | Sfruttamento di falle su servizi esposti su internet (ACN, ENISA, Clusit) | Il server Aruba ospita siti e n8n raggiungibili da internet | Aggiornamenti ([PR32.1](../A_ASSET%20%26%20CONFIGURAZIONE/PR32.1%20-%20Gestione%20delle%20Configurazioni%20e%20dell%27Infrastruttura%20IT.md) §7) | Scansione delle vulnerabilità del server una volta l'anno ([PR23.1](PR23.1%20-%20Gestione%20delle%20Minacce%20e%20delle%20Vulnerabilit%C3%A0%20Tecniche.md) §6) |
| 5 | Librerie open source vulnerabili o compromesse (MITRE, Supply Chain Compromise) | Il team sviluppa software con librerie di terze parti, anche per i clienti | Revisione del codice ([PO25](../A_PROGETTAZIONE%20%26%20SVILUPPO%20SICURO/PO25%20-%20Sviluppo%20Sicuro.md)) | Attivare gli avvisi Dependabot sui repository che usano librerie di terze parti gestite con un package manager |
| 6 | Chiavi e password finite nel codice o in repository pubblici (MITRE, Unsecured Credentials) | I repository GitHub contengono configurazioni; il repo SGI è pubblico | Credenziali in Bitwarden ([REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §2) | Attivare il secret scanning di GitHub; nel repo SGI nessun dettaglio dell'infrastruttura |
| 7 | Errori di configurazione e condivisioni troppo aperte (ACN, Misconfiguration) | Documenti di clienti su Google Drive, condivisibili con link | Classificazione delle informazioni ([PO15](../A_CLASSIFICAZIONE%20INFORMAZIONI/PO15%20-%20Politica%20Classificazione%20Informazioni.md)) | Nella revisione semestrale degli accessi ([PR16.1](../A_ACCESSI/PR16.1%20-%20Gestione%20degli%20Accessi.md) §6) controllare anche i file condivisi con «chiunque abbia il link» |
| 8 | Fuga di dati tramite strumenti di intelligenza artificiale | Il team usa strumenti AI nello sviluppo | Solo strumenti autorizzati ([PR35.1](../8.2_PRODOTTI%20%26%20SERVIZI/PR35.1%20-%20Digital.md) §2.3) | Nessuna |
| 9 | Guasto o indisponibilità di un fornitore (ACN, Guasto) | Il lavoro dipende da Google, GitHub e Aruba | Backup del server ([PR21.1](../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore.md)) | Nessuna: nessuna copia esterna di GitHub, rischio accettato dall'Amministratore Unico il 18/11/2026 |
| 10 | Furto o perdita del portatile | Portatili usati anche fuori sede | Disco cifrato, blocco schermo ([REG01](../7_GESTIONE%20RISORSE/REG01%20-%20Regolamento%20sull%E2%80%99utilizzo%20degli%20strumenti%20aziendali.md) §3) | Nessuna |

**Conclusione per il Riesame della Direzione 2026**: le minacce più
rilevanti per Vectorlab sono quelle legate agli account (1, 2) e al
software sviluppato (5, 6). Le azioni aperte sono la scansione del
server e i controlli automatici su GitHub (Dependabot e secret
scanning).
