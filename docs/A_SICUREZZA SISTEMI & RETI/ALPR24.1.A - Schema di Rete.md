# ALPR24.1.A - Schema di Rete

**Allegato - Schema di Rete**

<div style="border-left:4px solid #2A5C8A;background:#EAF1F7;padding:.75rem 1rem;margin:1rem 0">
<strong>DOCUMENTO IN BOZZA — generato il 16/07/2026</strong> per colmare una lacuna rilevata durante la revisione della documentazione (citato nella SOA ma non ancora creato). Contenuto basato su pratiche reali già note da altri documenti del SGI; le parti evidenziate in rosso sono da confermare prima dell'approvazione formale.
</div>

### Revisioni

| **Rev.** | **Data**   | **Descrizione** | **Redatto** | **Approvato** |
| -------- | ---------- | --------------- | ----------- | ------------- |
| 0.1      | 16/07/2026 | Prima bozza — documento mancante generato per colmare una lacuna rilevata nella SOA | IA          | Da approvare  |
|          |            |                 |             |               |

## 1 Introduzione

### 1.1 Scopo

Il presente allegato descrive, in forma testuale, la rete locale
presente presso la sede di VECTORLAB (Piazza Borgo Pila 39, Genova).
Come indicato in "*PR24.1 - Gestione delle Reti*", si tratta di una rete
volutamente semplice: l'Azienda non dispone di un CED, di una sala
server né di apparati di rete critici propri (cfr. "*PR18.1 - Gestione
Sicurezza Fisica e Ambientale*"). Non essendo disponibile uno strumento
di disegno tecnico validato per la produzione di un diagramma grafico,
la rete viene qui rappresentata come elenco di componenti e
collegamenti.

### 1.2 Riferimenti e Allegati

> PR24.1 - Gestione delle Reti

> ALPR24.1.B - Schema Infrastruttura

> PR18.1 - Gestione Sicurezza Fisica e Ambientale.

## 2 Componenti della rete di ufficio

  - **Connessione Internet** in ingresso presso la sede, fornita
    dall'operatore di connettività <span style="color:#B3392A">[DA CONFERMARE: nome dell'operatore/ISP e tipologia di linea (fibra/FTTC/altro) — non documentati]</span>.

  - **Router/Firewall di ufficio** — unico apparato di rete presente in
    sede:

      - fornisce indirizzamento e instradamento (NAT) verso Internet;

      - espone la rete Wi-Fi aziendale con autenticazione WPA2;

      - integra funzionalità di firewall (incluso filtro dei contenuti
        web e rilevamento delle intrusioni - IDS), come descritto in
        "*PR24.1 - Gestione delle Reti*";

      - <span style="color:#B3392A">[DA CONFERMARE: marca/modello dell'apparato]</span>;

      - <span style="color:#B3392A">[DA CONFERMARE: indirizzo IP pubblico, range di indirizzamento privato/subnet interna e configurazione DHCP]</span>.

  - **Postazioni di lavoro** (PC fissi e portatili del personale) —
    collegate al router via cavo Ethernet o Wi-Fi (WPA2). Non è presente
    una segmentazione interna (VLAN) dedicata per le postazioni di
    lavoro del personale.

  - <span style="color:#B3392A">[DA CONFERMARE: rete Wi-Fi guest per i visitatori, eventualmente segregata su VLAN dedicata, come indicato in REG01 — da verificare se attualmente attiva]</span>.

  - **Dispositivi mobili aziendali** (smartphone, tablet, dispositivi di
    test) — si collegano alla rete Wi-Fi di ufficio quando presenti in
    sede, oppure utilizzano la rete dati mobile/reti terze quando in
    mobilità.

Non sono presenti, presso la sede, switch gestiti, ulteriori access
point, VPN concentrator, rack o altri apparati di rete oltre al
router/firewall sopra descritto.

## 3 Collegamenti verso l'esterno

  - **Router di ufficio → Internet**: unico punto di uscita della rete
    di ufficio verso la rete pubblica, protetto dal firewall integrato
    nel router.

  - **Postazioni di lavoro → servizi cloud aziendali**: l'accesso a
    Google Workspace, GitHub, AWS (console e servizi applicativi),
    server Aruba e agli altri strumenti aziendali in cloud avviene
    tramite Internet, in HTTPS/TLS, attraverso il router di ufficio o
    tramite le reti utilizzate in modalità smart working (reti
    domestiche del personale, non gestite da VECTORLAB).

  - <span style="color:#B3392A">[DA CONFERMARE: eventuale accesso VPN dedicato per il personale verso risorse aziendali, come indicato in REG01 — da verificare l'effettivo utilizzo e le relative caratteristiche tecniche]</span>.

Il collegamento tra la rete di ufficio e l'infrastruttura cloud
aziendale (descritta in dettaglio in "*ALPR24.1.B - Schema
Infrastruttura*") non prevede canali dedicati (es. VPN site-to-site o
linee dirette): l'accesso avviene come un qualsiasi accesso Internet
autenticato, in linea con il modello cloud-first adottato
dall'Azienda.

## 4 Rappresentazione sintetica

```
Internet
   |
   |  (connessione fornita dall'operatore di connettività)
   |
[ Router / Firewall di ufficio ]
   - NAT / firewall integrato
   - Wi-Fi aziendale (WPA2)
   - filtro contenuti web + IDS
   |
   |------ (cavo Ethernet) ------ [ Postazioni di lavoro fisse ]
   |
   |------ (Wi-Fi WPA2) ---------- [ Portatili / dispositivi mobili aziendali ]
   |
   +------ (DA CONFERMARE: Wi-Fi guest / VLAN dedicata) ---- [ Dispositivi visitatori ]

Tutte le postazioni raggiungono via Internet (HTTPS/TLS) i servizi
cloud aziendali: AWS, server Aruba, Google Workspace, GitHub
(cfr. ALPR24.1.B - Schema Infrastruttura)
```

Non essendo la rete di ufficio dotata di segmentazione interna
significativa né di apparati aggiuntivi, lo schema sopra riportato
esaurisce la rappresentazione della rete fisica di VECTORLAB.
