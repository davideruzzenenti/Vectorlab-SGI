# MDPO03.A - Lista Obiettivi

## Cover

<table>
<tr><th>Rev.</th><th>Data</th><th colspan="4">Descrizione</th><th>Redatto</th><th>Approvato</th><th>Classificazione</th></tr>
<tr><td>0.0</td><td>17/11/2026</td><td colspan="4">Emissione</td><td>RSGI</td><td>Da approvare</td><td>Interno</td></tr>
<tr><td>0.1</td><td>23/11/2026</td><td colspan="4">Aggiunte le regole per la gestione degli obiettivi, prima in PO03 (ritirato)</td><td>RSGI</td><td>Da approvare</td><td>Interno</td></tr>
</table>

## Regole per la gestione degli obiettivi

- **Origine**: gli obiettivi nascono dalla politica ([PO01](../01_POLITICA%20SISTEMA%20INTEGRATO/PO01%20-%20Sistema%20Integrato-Rev%200.0.md)), dal piano di trattamento dei rischi ([MDPR33.1.B](../B_REGISTRAZIONI/Analisi%20dei%20Rischi/2026/MDPR33.1.B%20-%20Piano%20di%20Trattamento%20dei%20Rischi%20-%202026.md)), dagli indicatori ([MDPR10.1.A](../9.1_MONITORAGGIO%20KPI/MDPR10.1.A%20-%20Tabella%20Indicatori.md)) e dai risultati di audit, non conformità e incidenti.
- **Contenuto**: per ogni obiettivo si indicano cosa fare, risorse, responsabile (owner), scadenza e come si verifica il risultato, con indicatore e traguardo quando è misurabile (colonne della tabella).
- **Responsabilità**: l'Amministratore Unico approva gli obiettivi; l'owner li porta avanti; RSGI aggiorna lo stato almeno prima di ogni Riesame della Direzione ([PR12.1](../9.3_RIESAME%20DIREZIONE/PR12.1%20-%20Riesame%20della%20Direzione.md)), che valuta i risultati e fissa i nuovi obiettivi.
- **Comunicazione e aggiornamento**: gli obiettivi si comunicano alle persone coinvolte e si aggiornano quando cambiano le condizioni.
- **Esito**: completato secondo quanto pianificato; completato ma non secondo quanto pianificato; non completato. Per gli obiettivi con un indicatore si riporta anche il valore raggiunto rispetto al traguardo.

## Obiettivi 2026–2027

| # | Obiettivo | Origine | Owner | Indicatore e traguardo | Scadenza | Risorse | Come si verifica | Stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Certificazione ISO/IEC 27001 e ISO 9001 del servizio Ynsera | Politica [PO01](../01_POLITICA%20SISTEMA%20INTEGRATO/PO01%20-%20Sistema%20Integrato-Rev%200.0.md); decisione della Direzione | RSGI | Stage 1 RINA superato; stage 2 senza non conformità maggiori | Dicembre 2026 (stage 1); T1 2027 (stage 2) | Consulenza Nextage, tempo RSGI | Esito degli audit RINA; Riesame della Direzione | Aperto |
| 2 | Accessi sicuri agli strumenti aziendali | Verifica utenze del 22/10/2026 (27001 A.5.16–A.5.18, A.8.5) | CTO | Verifica in due passaggi attiva sul 100% degli account Google Workspace; 100% degli interni in ClickUp con indirizzo aziendale | 30/11/2026 | Console Google Workspace; nessun costo | Rapporto utenti della console Google; elenco membri ClickUp | Aperto |
| 3 | Continuità dei dati del server | Situazione infrastruttura del 20/10/2026 (27001 A.8.13; [PR21.1](../A_BACKUP%20%26%20RESTORE/PR21.1%20-%20Gestione%20dei%20Backup%20e%20Restore.md)) | CTO, con l'IT esterno | Backup automatico fuori dal server attivo; prova di ripristino superata, poi ripetuta ogni 3 mesi | 30/11/2026 | Spazio di backup esterno; ore dell'IT esterno | Registro delle prove di ripristino ([MDPR21.1.A](../A_BACKUP%20%26%20RESTORE/MDPR21.1.A%20-%20Piano%20di%20Restore.md)) | Aperto |
| 4 | Soddisfazione dei clienti Ynsera | [PR35.1](../8.2_PRODOTTI%20%26%20SERVIZI/PR35.1%20-%20Digital.md) §2.5; 9001 sull'ascolto del cliente | PM; RSGI per l'analisi | Form di fine commessa raccolto sul 100% delle commesse chiuse; voto medio ≥ 4 su 5 | Dal 01/12/2026; analisi annuale | Form di fine commessa (IT esterno) | Form allegati ai task Prospect; [MDPR10.1.B](../9.1_MONITORAGGIO%20KPI/MDPR10.1.B%20%20-%20Analisi%20Soddisfazione%20Cliente.md) | Aperto |
| 5 | Consapevolezza del personale su sicurezza e privacy | 27001 7.3; [PR05.1](../7_GESTIONE%20RISORSE/PR05.1%20-%20Gestione%20del%20personale.md) (Consapevolezza) | HR | 100% del team Ynsera formato con una sessione annuale su sicurezza delle informazioni e privacy | 31/03/2027 | Mezza giornata di formazione interna | Registro presenze; lista ClickUp «Consapevolezza e formazione» | Aperto |
| 6 | Qualità del processo commerciale | [PR09.1](../8.2_PRODOTTI%20%26%20SERVIZI/PR09.1%20-%20Gestione%20Commerciale.md) §2.6 e §2.8 | Business Development | Motivo registrato sul 100% delle offerte perse; tasso di conversione delle offerte misurato (valore di partenza 2027) | 31/12/2027 | Nessuna risorsa aggiuntiva (lista Prospect in ClickUp) | Lista Prospect; analisi annuale ([PR09.1](../8.2_PRODOTTI%20%26%20SERVIZI/PR09.1%20-%20Gestione%20Commerciale.md) §2.8) | Aperto |

## Riferimenti

- ISO/IEC 27001:2022, 6.2 Obiettivi per la sicurezza delle informazioni e pianificazione per conseguirli
- ISO 9001:2026, 6.2 Obiettivi per la qualità e pianificazione per il loro raggiungimento (certificazione sulla ISO 9001:2015, stesso punto; numerazione 2026 da verificare sul testo UNI)
