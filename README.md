# Vectorlab SGI

**Stato documentazione:** https://davideruzzenenti.github.io/Vectorlab-SGI/STATO-DOCUMENTAZIONE.html

**Consulta la documentazione:** https://davideruzzenenti.github.io/Vectorlab-SGI/

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

Per lo stato di completezza dei singoli documenti del SGI (cosa è pronto, cosa è ancora un template da compilare, cosa va corretto, cosa manca del tutto, e chi deve intervenire) vedere la dashboard **[STATO-DOCUMENTAZIONE.html](https://davideruzzenenti.github.io/Vectorlab-SGI/STATO-DOCUMENTAZIONE.html)**.

## Nota sulla visibilità del repository

Il repository è **pubblico**: su piano GitHub Free, Pages (il sito di consultazione) funziona solo con repo pubblici — passare a privato richiederebbe GitHub Pro o un'organizzazione Enterprise Cloud per mantenere il sito attivo. Vedere `STATO-PROGETTO.md` per i dettagli di questa scelta.
