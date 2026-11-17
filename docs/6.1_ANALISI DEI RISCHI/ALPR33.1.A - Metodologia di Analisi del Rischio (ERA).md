# ALPR33.1.A - Metodologia di Analisi del Rischio (ERA)

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.0      | 17/11/2026 | Emissione       | RSGI        | Da approvare  |

## 1 Scopo

Descrive il metodo con cui Vectorlab valuta i rischi per la sicurezza
delle informazioni con lo strumento ERA (Environmental Risk Analysis,
servizio cloud di Nextage), in modo che valutazioni ripetute diano
risultati coerenti, validi e confrontabili (ISO/IEC 27001, 6.1.2 b).
Il processo complessivo (ruoli, trattamento, approvazione) è descritto
in *PR33.1 – Processo Analisi del Rischio e Trattamento*; questo allegato
descrive solo come si calcola il rischio.

## 2 Campo di applicazione

Tutti gli asset nel campo di applicazione del Sistema di Gestione
Integrato (PO02 §4).

## 3 Riferimenti

- PR33.1 – Processo Analisi del Rischio e Trattamento
- MDPR33.1.A – Report Analisi dei Rischi
- MDPR33.1.B – Piano di Trattamento dei Rischi
- asset_inventory_vectorlab – Inventario degli asset
- SOA – Dichiarazione di Applicabilità (gestita in ERA)
- ISO/IEC 27001:2024+A1:2024, 6.1.2 e 6.1.3; ISO/IEC 27005 (linee guida)

## 4 Responsabilità

| Ruolo | Compito |
| --- | --- |
| CISO (Amministratore Unico) | Conduce l'analisi in ERA, prepara report e piano di trattamento |
| Asset Owner | Assegna la criticità dell'asset |
| Process Owner | Valuta il livello delle vulnerabilità dell'asset |
| Risk Owner | Decide il trattamento dei rischi del proprio asset |
| Amministratore Unico | Stabilisce il rischio accettabile (RA), approva report e piano, accetta il rischio residuo |
| RSGI | Riesamina report e piano prima dell'approvazione (misura compensativa, ALPO01.B §3) |
| Nextage | Supporto metodologico e gestione dello strumento ERA |

## 5 Metodo

L'analisi si svolge in ERA in sei passi. Ogni analisi è un'istanza con
un codice (es. «Agosto 2026») e si conserva nello strumento.

1. **Processi**: si elencano i processi primari e di supporto con il
   loro Process Owner (es. Software Development, Business Development,
   IT, Amministrazione, Risorse Umane, Direzione).
2. **Inventario degli asset**: per ogni asset si registrano codice,
   nome, stato (attivo o dismesso), classe, criticità, Asset Owner,
   Risk Owner, sede e processi su cui impatta. La criticità esprime il
   valore delle informazioni dell'asset in termini di riservatezza,
   integrità e disponibilità (scala qualitativa, da «Molto bassa» in su),
   e la assegna l'Asset Owner.
3. **Minacce**: per ogni asset ERA propone le minacce tipiche della sua
   classe (es. incendio, malware, errore del personale). Per ciascuna si
   indica la **probabilità di accadimento** (scala qualitativa, da
   «Improbabile» in su), in base agli eventi già accaduti a Vectorlab o
   ad aziende simili.
4. **Impatto**: per ogni minaccia si indica l'impatto su riservatezza,
   integrità e disponibilità (Basso, Medio, Alto). ERA propone un valore
   predefinito per la classe di asset, che si può correggere.
5. **Vulnerabilità**: per ogni asset si valutano le vulnerabilità
   associate e il loro livello (scala a tre livelli), tenendo conto dei
   controlli già in atto. Le vulnerabilità comprendono anche i controlli
   dell'Allegato A non attuati, ricavati dalla checklist dei controlli.
6. **Calcolo**: ERA calcola un valore di rischio per ogni «record», cioè
   ogni combinazione asset + minaccia + vulnerabilità, combinando
   criticità, probabilità, impatto e livello di vulnerabilità.

## 6 Rischio accettabile e fasce

Il **rischio accettabile (RA)** è il valore al di sopra del quale un
rischio va trattato. Lo stabilisce l'Amministratore Unico a ogni
analisi, prendendo come riferimento il valore di rischio di un gruppo
di asset ritenuti sicuri, e lo riesamina nel Riesame della Direzione
(«Piano di rischio accettabile» nel report). Per l'analisi 2026 RA = 45.

ERA divide i record in tre fasce rispetto a RA:

| Fascia | Colore | Significato |
| --- | --- | --- |
| Rischio basso | Verde | Sotto RA: accettabile |
| Rischio medio | Giallo | Valore limite, vicino o pari a RA: si valuta il trattamento |
| Rischio alto | Rosso | Sopra RA: da trattare (PR33.1) |

## 7 Uscite e registrazioni

| Registrazione | Dove si conserva | Chi |
| --- | --- | --- |
| Istanza di analisi (asset, minacce, vulnerabilità, valori) | ERA | CISO |
| Report di analisi (MDPR33.1.A) | B_REGISTRAZIONI/Analisi dei Rischi/<anno> | CISO |
| Piano di trattamento (MDPR33.1.B) | B_REGISTRAZIONI/Analisi dei Rischi/<anno> | CISO |
| Accettazione di RA e dei rischi residui | Verbale del Riesame della Direzione (PR12.1) | Amministratore Unico |

## 8 Frequenza

Almeno una volta l'anno e in caso di cambiamenti significativi
(organizzativi, tecnologici, di contesto o dopo incidenti rilevanti),
come previsto da PR33.1.

<span style="color:#B3392A">[DA CONFERMARE con Nextage: numero dei
livelli di ciascuna scala e formula di calcolo usata da ERA.]</span>
