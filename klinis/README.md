# Hermes Skills — Klinis IGD PJT Jantung

Repository untuk skill Hermes Agent yang digunakan di IGD PJT Jantung.

## Struktur

```
skills/
├── clinical/
│   ├── soap-igd-jantung/
│   │   ├── SKILL.md          — Template SOAP baku + decision tree
│   │   └── references/
│   │       ├── template-acs-ppci.md
│   │       ├── template-acs-non-ppci.md
│   │       ├── template-gagal-jantung.md
│   │       ├── template-bradikardia.md
│   │       ├── template-acute-pericarditis.md
│   │       ├── kasus-01.md s/d kasus-04.md
│   │       └── index.md
│   └── echocardiography-igd/
│       ├── SKILL.md           — Template echo + form isian 9 nomor
│       └── scripts/
│           └── echo-calculator.py  — Mini app kalkulator echo + hemodinamik
```

## Cara Sync ke Hermes

```bash
# Dari repo ke ~/.hermes/skills/
cp -r skills/clinical/* ~/.hermes/skills/clinical/

# Dari ~/.hermes/skills/ ke repo
cp -r ~/.hermes/skills/clinical/* skills/clinical/
```

## Apa yang Ada

- **soap-igd-jantung**: Template SOAP untuk ACS PPCI, ACS Non-PPCI, Gagal Jantung, Bradikardia, Acute Pericarditis
- **echocardiography-igd**: Template echo bedside + kalkulator hemodinamik (MAP, LV SV, LV CO, eRAP, SVR, BSA, CI, CPO, CPI)
