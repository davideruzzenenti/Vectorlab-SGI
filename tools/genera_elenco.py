#!/usr/bin/env python3
"""Genera MDPR08.1.A - Elenco Informazioni documentate a partire dai file del repository.

Per ogni documento legge codice e titolo dal nome del file e l'ultima riga
compilata della tabella «Revisioni» (Rev., Data, Redatto, Approvato).
Uso: python tools/genera_elenco.py   (dalla radice del repository)
Gira anche in automatico nella pipeline prima della pubblicazione del sito.
"""
import html
import re
from datetime import date
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
OUT = DOCS / "7.5_INFORMAZIONI DOCUMENTATE" / "MDPR08.1.A - Elenco Informazioni documentate.md"
SKIP_DIRS = {"stylesheets", "logokit vectorlab", "media"}
EXT_OK = {".md", ".pptx", ".xlsx", ".xlsm", ".drawio", ".pdf"}
TIPI = [("SOA", "Dichiarazione di applicabilità"), ("REG", "Regolamento"), ("ALPO", "Allegato"),
        ("ALPR", "Allegato"), ("MDPO", "Modulo"), ("MDPR", "Modulo"), ("PO", "Politica"), ("PR", "Procedura")]
CODE_RE = re.compile(r"^((?:SOA|REG\d+|ALP[OR][\d.]+[A-Z](?:\.\d+)?|MDP[OR][\d.]+[A-Z]?|PO\d+|PR\d+(?:\.\d+)*))\s*[-–]?\s*(.*)$")


def tipo(code):
    for pref, nome in TIPI:
        if code.startswith(pref):
            return nome
    return "Altro"


def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s).replace("*", "")
    return re.sub(r"\s+", " ", s).strip()


def ultima_revisione(text):
    """Restituisce (rev, data, redatto, approvato) dell'ultima riga compilata della tabella revisioni."""
    head = text[:15000]
    rows = []
    # tabelle markdown
    for line in head.splitlines():
        if line.strip().startswith("|"):
            cells = [clean(c) for c in line.strip().strip("|").split("|")]
            rows.append(cells)
    # tabelle html
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", head, flags=re.S):
        rows.append([clean(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, flags=re.S)])
    best = None
    for cells in rows:
        cells = [c for c in cells if c != ""]
        if len(cells) >= 3 and re.fullmatch(r"\d{1,2}(\.\d+)?", cells[0]) and re.fullmatch(r"\d{2}/\d{2}/\d{4}", cells[1]):
            redatto = cells[-2] if len(cells) >= 5 else ""
            approvato = cells[-1] if len(cells) >= 5 else ""
            if approvato.lower() in ("interno", "pubblico", "riservato"):
                redatto, approvato = cells[-3], cells[-2]
            best = (cells[0], cells[1], redatto, approvato)
    return best


def main():
    voci = {}
    for f in sorted(DOCS.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in EXT_OK or f.name == "index.md":
            continue
        if any(p in SKIP_DIRS for p in f.relative_to(DOCS).parts) or f == OUT or f.name.startswith("STATO-"):
            continue
        stem = f.stem
        m = CODE_RE.match(stem)
        if not m:
            continue
        code, title = m.group(1).rstrip("."), m.group(2)
        title = re.sub(r"-?Rev \d+\.\d+$", "", title).strip(" -")
        cartella = f.relative_to(DOCS).parent.as_posix()
        registrazione = cartella.startswith("B_REGISTRAZIONI")
        key = (cartella, stem)
        v = voci.setdefault(key, {"code": code, "title": title, "cartella": cartella, "formati": set(),
                                   "rev": None, "registrazione": registrazione, "md": None})
        v["formati"].add(f.suffix.lower().lstrip("."))
        if f.suffix.lower() == ".md":
            v["md"] = f
            v["rev"] = ultima_revisione(f.read_text(encoding="utf-8", errors="replace"))

    def riga(v):
        rev, data, redatto, approvato = v["rev"] or ("n.d.", "", "", "")
        link = ""
        if v["md"] is not None:
            rel = Path("../") / v["md"].relative_to(DOCS)
            link = "<a href=\"" + html.escape(rel.with_suffix("").as_posix() + "/") + "\">" + html.escape(v["code"]) + "</a>"
        else:
            link = html.escape(v["code"])
        return (f"<tr><td>{tipo(v['code'])}</td><td>{link}</td><td>{html.escape(v['title'])}</td>"
                f"<td>{html.escape(rev)}</td><td>{html.escape(data)}</td><td>{html.escape(redatto)}</td>"
                f"<td>{html.escape(approvato)}</td><td>{html.escape(', '.join(sorted(v['formati'])))}</td>"
                f"<td>{html.escape(v['cartella'])}</td></tr>")

    ordine = lambda v: (v["cartella"], v["code"])
    docs = sorted((v for v in voci.values() if not v["registrazione"]), key=ordine)
    regs = sorted((v for v in voci.values() if v["registrazione"]), key=ordine)
    head = ("<table>\n<tr><th>Tipo</th><th>Codice</th><th>Titolo</th><th>Rev.</th><th>Data rev.</th>"
            "<th>Redatto</th><th>Approvato</th><th>Formato</th><th>Cartella</th></tr>\n")
    out = [
        "# MDPR08.1.A - Elenco Informazioni documentate",
        "",
        "Elenco generato automaticamente dal repository del Sistema di Gestione Integrato "
        f"(script `tools/genera_elenco.py`, PR08.1 §2.9). Ultima generazione: {date.today():%d/%m/%Y}.",
        "",
        "Per ogni documento sono riportati i dati dell'ultima riga della tabella «Revisioni». "
        "«Da approvare» indica una revisione non ancora approvata dalla Direzione; «n.d.» indica un documento senza tabella «Revisioni» (allegato o modulo). "
        "Lo storico completo di ogni documento è nella cronologia del repository.",
        "",
        f"## Documenti del Sistema di Gestione ({len(docs)})",
        "",
        head + "\n".join(riga(v) for v in docs) + "\n</table>",
        "",
        f"## Registrazioni ({len(regs)})",
        "",
        head + "\n".join(riga(v) for v in regs) + "\n</table>",
        "",
    ]
    rit = DOCS.parent / "tools" / "ritirati.csv"
    if rit.exists():
        import csv
        with open(rit, encoding="utf-8") as f:
            righe = list(csv.DictReader(f))
        out += [
            f"## Documenti ritirati o uniti ({len(righe)})",
            "",
            "Documenti tolti dal Sistema di Gestione (PR08.1, conservazione e successive disposizioni). "
            "Il testo resta nella cronologia del repository; l'elenco è in `tools/ritirati.csv`.",
            "",
            "<table>\n<tr><th>Codice</th><th>Titolo</th><th>Data</th><th>Esito</th><th>Sostituito da</th><th>Motivo</th></tr>\n"
            + "\n".join(
                "<tr>" + "".join(f"<td>{html.escape(r[k])}</td>" for k in ("codice", "titolo", "data", "esito", "sostituito_da", "motivo")) + "</tr>"
                for r in righe)
            + "\n</table>",
            "",
        ]
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"Generato {OUT.relative_to(DOCS.parent)}: {len(docs)} documenti, {len(regs)} registrazioni")


if __name__ == "__main__":
    main()
