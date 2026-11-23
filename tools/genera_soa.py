"""Genera la vista leggibile della SOA (riepilogo + dettaglio apribile).

Sorgente: tools/soa/SOA-sorgente.md = conversione della SOA di Nextage
(Excel su Drive). Quando Nextage aggiorna l'Excel, si riconverte la
sorgente e si rilancia lo script:

    python tools/genera_soa.py

Il contenuto dei controlli NON viene modificato. Lo script corregge solo:
- "27002.0" -> "ISO/IEC 27002" (residuo numerico della conversione da Excel);
- l'intestazione della sezione 7 (Controlli fisici), mancante nella sorgente.
Le colonne sempre vuote non vengono mostrate.

La sezione «AGID CSP-SAAS» della sorgente NON viene pubblicata
(INCLUDI_AGID = False): contiene residui di un altro cliente (Nutanix,
«LD in iter di certificazione 2019») e la sua rimozione è stata decisa il
16/11/2026, da far applicare a Nextage anche in ERA.
"""
import html
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "soa" / "SOA-sorgente.md"
DST = ROOT / "docs" / "02_SOA" / "SOA - Statement of Applicability - Dichiarazione di Applicabilità 27001.md"

SEZIONI = {
    "5": "5. Controlli organizzativi (Organizational controls)",
    "6": "6. Controlli relativi alle persone (People controls)",
    "7": "7. Controlli fisici (Physical controls)",
    "8": "8. Controlli tecnologici (Technological controls)",
}
INCLUDI_AGID = False

# Revisioni aggiunte alla vista (la rev. 0.0 viene dalla sorgente)
REVISIONI_EXTRA = [
    ("0.1", "23/11/2026",
     "Nuova vista (riepilogo e dettaglio); corretti il campo Set controlli "
     "e l'intestazione della sezione 7; tolta la sezione AGID CSP-SAAS "
     "(residui di un altro cliente)", "RSGI", "Da approvare", "Interno"),
]
# Indici delle colonne nella tabella Controlli della sorgente
C = dict(id=0, titolo=1, testo=2, set=3, app_si=5, app_no=6, att_si=7, att_no=8,
         mot_escl=9, legale=10, contratto=11, business=12, rischio=13,
         descr=14, rif=15, attr=range(16, 22))
ATTRIBUTI = ["Tipo di controllo", "Proprietà di sicurezza", "Concetti cybersecurity",
             "Capacità operative", "Domini di sicurezza", "Processi"]
MOTIVI = [("legale", "L", "Requisito legale"), ("contratto", "C", "Obbligo contrattuale"),
          ("business", "B", "Requisito business / best practice"),
          ("rischio", "R", "Risultato analisi dei rischi")]


def testo(cella):
    return cella.get_text(" ", strip=True)


def interno(cella):
    return cella.decode_contents().strip()


def x(cella):
    return testo(cella).lower() == "x"


def md_cella(s):
    return s.replace("|", "\\|").replace("\n", " ")


def leggi_controlli(tabella):
    controlli = []
    for tr in tabella.find_all("tr"):
        c = tr.find_all(["td", "th"])
        if len(c) < 22 or not re.fullmatch(r"\d+\.\d+", testo(c[C["id"]])):
            continue  # intestazioni e righe di sezione
        titolo_html = interno(c[C["titolo"]])
        parti = re.split(r"<br\s*/?>", titolo_html, maxsplit=1)
        rif_links = c[C["rif"]].find_all("a")
        controlli.append(dict(
            id=testo(c[C["id"]]),
            titolo_it=BeautifulSoup(parti[0], "html.parser").get_text(" ", strip=True),
            titolo_html=titolo_html,
            testo=interno(c[C["testo"]]),
            set=testo(c[C["set"]]),
            applicabile="Sì" if x(c[C["app_si"]]) else ("No" if x(c[C["app_no"]]) else "—"),
            attuato="Sì" if x(c[C["att_si"]]) else ("No" if x(c[C["att_no"]]) else "—"),
            mot_escl=interno(c[C["mot_escl"]]),
            motivi=[(k, s, n) for k, s, n in MOTIVI if x(c[C[k]])],
            descr=interno(c[C["descr"]]),
            rif_html=interno(c[C["rif"]]),
            rif_brevi=[(a.get("href", ""), testo(a).split(" - ")[0].strip()) for a in rif_links],
            rif_testo=testo(c[C["rif"]]) if not rif_links else "",
            attributi=[(ATTRIBUTI[i], interno(c[j])) for i, j in enumerate(C["attr"]) if testo(c[j])],
        ))
    return controlli


def correggi_set(valore):
    v = re.sub(r"\.0$", "", valore.strip())  # 27002.0 -> 27002
    return f"ISO/IEC {v}" if v.isdigit() else v


def ancora(cid):
    return "c-" + cid.replace(".", "-")


def cover(tabella, n_ctrl):
    righe = [[testo(td) for td in tr.find_all(["td", "th"]) if testo(td)] for tr in tabella.find_all("tr")]
    rev = [r for r in righe[1:] if len(r) >= 6 and re.fullmatch(r"\d+\.\d+", r[1])]
    info = {r[0]: r[1] for r in righe if len(r) == 2}
    revisioni = [tuple(r[1:7]) for r in rev] + REVISIONI_EXTRA
    ultima = revisioni[-1]
    out = ["## Cover", "",
           "| Rev. | Data | Descrizione | Redatto | Approvato | Classificazione |",
           "|---|---|---|---|---|---|"]
    out += ["| " + " | ".join(md_cella(v) for v in r) + " |" for r in revisioni]
    out += ["", "| | |", "|---|---|",
            f"| Data ultima versione | {ultima[1]} |",
            f"| Versione | {ultima[0]} |"]
    for k in ("Set di Controlli inclusi", "Controlli Non Applicabili", "Acronimi Controllo"):
        if k in info:
            out.append(f"| {k} | {md_cella(info[k])} |")
    out.append(f"| Numero controlli | {n_ctrl} |")
    return out


def riepilogo(controlli):
    tot = len(controlli)
    app = sum(c["applicabile"] == "Sì" for c in controlli)
    att = sum(c["attuato"] == "Sì" for c in controlli)
    non_att = sum(c["applicabile"] == "Sì" and c["attuato"] != "Sì" for c in controlli)
    non_app = sum(c["applicabile"] == "No" for c in controlli)
    out = ["## Riepilogo", "",
           f"**{tot} controlli**: {app} applicabili, di cui {att} attuati e {non_att} non ancora "
           f"attuati; {non_app} non applicabili.", "",
           "Motivo di inclusione: " + " · ".join(f"**{s}** = {n}" for _, s, n in MOTIVI) + ".",
           "Clic sull'ID per aprire il dettaglio del controllo.", ""]
    for sez, nome in SEZIONI.items():
        gruppo = [c for c in controlli if c["id"].split(".")[0] == sez]
        if not gruppo:
            continue
        out += [f"### {nome}", "",
                "| ID | Controllo | Applicabile | Attuato | Motivo | Riferimenti |",
                "|---|---|---|---|---|---|"]
        for c in gruppo:
            rif = ", ".join(f"[{md_cella(t)}]({h})" for h, t in c["rif_brevi"]) or md_cella(c["rif_testo"])
            mot = " ".join(s for _, s, _ in c["motivi"]) or "—"
            out.append(f"| [{c['id']}](#{ancora(c['id'])}) | {md_cella(c['titolo_it'])} | "
                       f"{c['applicabile']} | {c['attuato']} | {mot} | {rif} |")
        out.append("")
    return out


def dettaglio(controlli):
    out = ["## Dettaglio dei controlli", ""]
    for sez, nome in SEZIONI.items():
        gruppo = [c for c in controlli if c["id"].split(".")[0] == sez]
        if not gruppo:
            continue
        out += [f"### {nome}", ""]
        for c in gruppo:
            stato = f"Applicabile: {c['applicabile']} · Attuato: {c['attuato']}"
            righe = [f"<tr><th>Controllo</th><td>{c['titolo_html']}<br><em>{c['testo']}</em></td></tr>",
                     f"<tr><th>Set di controlli</th><td>{html.escape(correggi_set(c['set']))}</td></tr>",
                     f"<tr><th>Applicabile / Attuato</th><td>{c['applicabile']} / {c['attuato']}</td></tr>"]
            if c["motivi"]:
                righe.append("<tr><th>Motivo di inclusione</th><td>"
                             + ", ".join(n for _, _, n in c["motivi"]) + "</td></tr>")
            if c["mot_escl"]:
                righe.append(f"<tr><th>Motivo di esclusione</th><td>{c['mot_escl']}</td></tr>")
            if c["descr"]:
                righe.append(f"<tr><th>Descrizione dell'attuazione</th><td>{c['descr']}</td></tr>")
            if c["rif_html"]:
                righe.append(f"<tr><th>Riferimenti documentali</th><td>{c['rif_html']}</td></tr>")
            if c["attributi"]:
                righe.append("<tr><th>Attributi ISO/IEC 27002</th><td>"
                             + "<br>".join(f"{k}: {v}" for k, v in c["attributi"]) + "</td></tr>")
            out += [f'<details class="soa-ctrl" id="{ancora(c["id"])}">',
                    f"<summary><strong>{c['id']}</strong> {html.escape(c['titolo_it'])} "
                    f'<span class="soa-stato">{stato}</span></summary>',
                    '<table class="soa-scheda">', *righe, "</table>", "</details>", ""]
    return out


SCRIPT_ANCORE = """<script>
/* Apre il dettaglio del controllo quando si arriva da un link #c-x-y */
(function () {
  function apri() {
    var el = location.hash && document.getElementById(location.hash.slice(1));
    if (el && el.tagName === "DETAILS") { el.open = true; el.scrollIntoView(); }
  }
  window.addEventListener("hashchange", apri);
  document.addEventListener("DOMContentLoaded", apri);
  if (typeof document$ !== "undefined") { document$.subscribe(apri); }
})();
</script>"""


def main():
    src = SRC.read_text(encoding="utf-8")
    soup = BeautifulSoup(src, "html.parser")
    t_cover, t_ctrl, t_agid = soup.find_all("table")[:3]
    controlli = leggi_controlli(t_ctrl)
    if len(controlli) != 93:
        sys.exit(f"Attesi 93 controlli ISO/IEC 27002, trovati {len(controlli)}: controllare la sorgente.")
    agid = re.search(r"## AGID CSP-SAAS\s*(<table>.*?</table>)", src, re.S).group(1)
    out = ["<!-- File GENERATO da tools/genera_soa.py: non modificarlo a mano. "
           "Le modifiche vanno nella sorgente tools/soa/SOA-sorgente.md -->", "",
           "# SOA - Statement of Applicability - Dichiarazione di Applicabilità 27001", ""]
    out += cover(t_cover, len(controlli)) + [""]
    out += riepilogo(controlli)
    out += dettaglio(controlli)
    if INCLUDI_AGID:
        out += ["## AGID CSP-SAAS", "", agid, ""]
    out += [SCRIPT_ANCORE, ""]
    DST.write_text("\n".join(out), encoding="utf-8")
    print(f"Scritto {DST.relative_to(ROOT)}: {len(controlli)} controlli")


if __name__ == "__main__":
    main()
