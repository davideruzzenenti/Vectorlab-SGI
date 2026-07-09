# Vectorlab SGI

Documentazione del Sistema di Gestione Integrato (SGI) di Vectorlab — Qualità (ISO 9001) e Sicurezza delle Informazioni (ISO/IEC 27001) — migrata da Google Drive a Markdown e pubblicata come sito consultabile via browser.

## Cosa contiene questo repository

- **`docs/`** — tutta la documentazione del SGI, organizzata in cartelle per categoria (politiche, procedure, allegati, moduli, registri). Ogni cartella ha un proprio `index.md` con i link a tutti i documenti al suo interno, inclusi quelli non convertiti in Markdown (Excel, PowerPoint, immagini), mantenuti nel loro formato originale accanto alla versione `.md`.
- **`mkdocs.yml`** e **`requirements.txt`** — configurazione di [MkDocs](https://www.mkdocs.org/) (tema Material) usata per generare il sito di navigazione.
- **`.github/workflows/deploy-docs.yml`** — workflow GitHub Actions che ricostruisce e pubblica il sito su GitHub Pages ad ogni push su `main`.

## Consultare la documentazione

Il modo più comodo è tramite il sito pubblicato (menu di navigazione, ricerca full-text):

**https://davideruzzenenti.github.io/Vectorlab-SGI/**

In alternativa si può sfogliare direttamente la cartella `docs/` su GitHub, oppure clonare il repo e avviare il sito in locale:

```bash
pip install -r requirements.txt
mkdocs serve
```

## Stato del progetto

Per la cronologia dettagliata della migrazione (cosa è stato fatto, limiti noti, decisioni prese, revisioni in corso) vedere **[STATO-PROGETTO.md](STATO-PROGETTO.md)**.

## Nota sulla visibilità del repository

Il repository è **pubblico** in questa fase, perché la documentazione contiene ancora bozze e nessun dato reale. È previsto il passaggio a un repository privato (con relativa valutazione di GitHub Pro per mantenere attivo GitHub Pages) quando i documenti conterranno dati aziendali reali.
