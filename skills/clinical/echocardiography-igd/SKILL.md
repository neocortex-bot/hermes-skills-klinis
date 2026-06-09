---
name: echocardiography-igd
description: Template Echocardiography Bedside + Echo Hemodinamik untuk pelaporan pasien IGD PJT Jantung. 1 sesi = 1 pasien. Hanya cantumkan parameter yang diisi oleh pakboss.
triggers:
  - pakboss mengirimkan data echo (teks/foto)
  - pakboss meminta format echo untuk SOAP
  - pakboss mengisi form isian echo
---

# Echocardiography IGD PJT

## Prinsip
- **Hanya parameter yang diisi** — bila pakboss kirim data echo, hanya parameter yang disebutkan/diisi yang dicantumkan. Jika cuma "Mild MR" ya tulis Mild MR saja, jangan tambahkan parameter lain.
- **Yang tidak perlu diisi pakboss** (kalkulasi otomatis dari app hemodinamik atau dari TTV):
  - MAP, LV SV, LV CO, eRAP, SVR, BSA, CI, CPO, CPI, Collapsibility Index, Distensibility Index
  - TDS, TDD, HR, Suhu — dari monitor TTV
  - Lung US (A-line, B-line, efusi pleura) — dari app
  - Urine output, fluid balance — dari catatan
- **Yang pakboss isi** — form isian di bawah ini saja.

---

## Form Isian Echo (Yang Perlu Diisi Pakboss)

Kirim nomor dan nilainya saja.

```
Tanggal:
1. LV func: _ | EF TEICH _% | EF Biplane ___%
2. RV func: _ | TAPSE _ | S' Lat ___
3. Mitral: _ | Aorta: _ | Pulmonal: _ | Tricuspid: _

Masalah katup (jabarkan di sini):
- Mitral: _ | MR ERO _ cm² | MR RV _ ml | MR VC _ cm | Regurg Jet Length > _% LA | Carpentier _ | Annulus mitral _ cm | MVA planimetry _ cm² | MVA PHT _ cm² | MS Mean PG _ mmHg | Mean PHT _ ms | Wilkins Score _
- Aorta: _ | AR PHT _ ms | AR ERO _ cm² | AR RV _ ml | AR VC _ cm | Regurg Jet Length > _% LVOT | Holodiastolic Reversal Flow Peak Vel _ cm/s | Aortic annulus _ cm | Sinus valsava _ cm | ST junction _ cm | Ascenden _ cm | AVA planimetry _ cm² | AV Vmax _ m/s | AV mean PG _ mmHg | AV continuity eq _ cm² | SVI _ ml/m² | AV VTI _ cm
- Pulmonal: _ | PR PHT _ ms | Regurg Jet Width > _/_ RVOT | PV AccT _ ms | PASP _ mmHg | mPAP _ mmHg | PV Vmax _ m/s | PV mean PG _ mmHg | PV VTI _ cm
- Tricuspid: _ | TR Jet [Central/Excentric] | Regurg Jet Area > _% RA | TR Vmax _ m/s | TR maxPG _ mmHg | TR VC _ cm | Systolic Reversal Flow Hepatic Vein [Ya/Tidak] | PH Probability [Low/Intermediate/High]

4. LVIDd _ | LA _ / _ | RA _ / _ | RVDB _ | LA/Ao ___
5. LVH: _ | LVMI _ | RWT ___
6. RWMA: ___
7. E/A _ | E' Med _ | E' Lat _ | E/E' _ | Grade ___
8. Perikard: ___
9. Lain: ___

TDS _ | TDD _ | HR _ | LVOT Diam _ | LVOT VTI ___
IVC exp _ | IVC insp _ | BB _ | TB _
```

**Aturan:** Jika pakboss lampirkan nomor 3 (Katup), artinya ada masalah katup — JANGAN tulis "Normal function and movement". Tulis sesuai yang pakboss sebutkan. Jika tidak disebut, jangan sematkan baris katup itu.

---

## Template Output Echo Bedside

Format untuk dimasukkan ke SOAP IGD:

```
*Echocardiography Bedside (tanggal):*
- [temuan LV Function], EF ...% (TEICH), EF ...% (BIPLANE)
- [temuan RV Function], TAPSE ... cm, S' lateral ... cm/s

Cardiac Valves:
- Mitral: ...
- Aorta: ...
- Pulmonal: ...
- Tricuspid: ...

Cardiac Dimensions:
... (LVIDd ... cm, LA Mayor ... cm, LA minor ... cm, RA Mayor ... cm, RA minor ... cm, RVDB ... cm, LA/Ao: ...)

LV Geometry:
[Eccentric/Concentric] LVH (LVMI ... g/m2, RWT ...)

Regional Wall Motion:
[Global Normokinetic / Akinetic/Hypokinetic ...]

eRAP: ... mmHg (IVC exp ... cm, IVC insp ... cm)
[Ini dari app hemodinamik — diisi otomatis]

LV Diastolic Function:
E/A ..., E' Med ... cm/s, E' Lat ... cm/s, E/E' ..., Grade ...

Pericardial Effusion: [ada/tidak]

[Parameter lain jika ada]
```

---

## Template Echo Hemodinamik

Diisi otomatis dari app hemodinamik + input pakboss (LVOT Diam, LVOT VTI, IVC). Tidak perlu diisi manual, tinggal copy dari app.

```
Echo Hemodinamik:
TD: .../... mmHg | MAP: ... mmHg | HR: ... bpm
LVOT Diam: ... cm | LVOT VTI: ... cm
LVSV: ... ml | LVCO: ... L/min
eRAP: ... mmHg (IVC exp ... cm, IVC insp ... cm)
SVR: ... dynes/sec/cm-5
BSA: ... m2 | CI: ... L/min/m2
CPO: ... watt | CPI: ... watt/m2
```

---

## Contoh Output Sesuai Data Riil

**Contoh dari Kasus 01 — Tn. Irwan (STEMI Anterior):**

*Kalau pakboss isi:*
1. Mildly abnormal | 42.6 / 41.7
2. Normal / 2.1 / 12.1
3. Mitral: Trivial MR | Aorta: Normal | Pulmonal: Mild PR | Tricuspid: Normal
4. 5.8 / 4.7 / 4.2 / 4.7 / 3.4 / 2.5 / 0.78
5. Eccentric / 143 / 0.36
6. Hypokinetic BM anterior, BM anteroseptal, BM anterolateral, Apicoseptal, apicolateral. Akinetic Apicoanterior
7. 0.6 / 6.07 / 4.2 / 7.7 / Grade I
8. Tidak
9. —

*Output:*
```
*Echocardiography Bedside (09-06-2026):*
- Mildly Abnormal LV Systolic Function, EF 42.6% (TEICH), EF 41.7% (BIPLANE)
- Normal RV systolic function, TAPSE 2.1 cm, S' lateral 12.1 cm/s

Cardiac Valves:
- Mitral: Trivial MR
- Aorta: 3 cuspis, Normal
- Pulmonal: Mild PR (jet < 1/3 RVOT, PR PHT 399 ms, PV AccT 171 ms)
- Tricuspid: Normal

Cardiac Dimensions:
LV dilatation (LA mayor 4.7, LA minor 4.2, RA mayor 4.7, RA minor 3.4, LVIDd 5.8, RVDB 2.5, LA/Ao 0.78)

LV Geometry:
Eccentric LVH (LVMI 143 g/m2, RWT 0.36)

Regional Wall Motion:
Hypokinetic BM anterior, BM anteroseptal, BM anterolateral, Apicoseptal, apicolateral. Akinetic Apicoanterior

eRAP: 8 mmHg (IVC exp 1.8, IVC insp 1.3)

LV Diastolic Function:
E/A 0.6, E' Med 6.07 cm/s, E' Lat 4.2 cm/s, E/E' 7.7, Grade I LV Diastolic Dysfunction

No pericardial effusion
```

---

## Cara Pakai Kalkulator Echo

Script di `scripts/echo-calculator.py`. Tinggal isi parameternya. Contoh panggilan dari terminal:

```bash
python3 ~/.hermes/skills/clinical/echocardiography-igd/scripts/echo-calculator.py \
  --date "08-05-2026" \
  --lv-func "Moderately Abnormal" --ef-teich 37.1 --ef-biplane 33.2 \
  --rv-func "Normal" --tapse 1.7 --s-lat 15.5 \
  --aorta "3 cuspis, calcification (-), Normal" \
  --mitral "Normal" \
  --tricuspid "Normal" \
  --pulmonal "Normal" \
  --lvidd 6.71 --la-mayor 4.20 --la-minor 3.37 --ra-mayor 2.97 --ra-minor 2.40 --rvdb 2.84 \
  --lvh-type Eccentric --lvmi 166 --rwt 0.17 \
  --rwma "Akinetic Apicoanterior, Badal Mid Anteroseptal, Hypokinetic Basal Mid Anterolateral" \
  --ivc-exp 1.22 --ivc-insp 0.6 \
  --ea 1.13 --e-med 9.0 --e-lat 13.3 --grade "Grade I" \
  --tds 105 --tdd 70 --hr 108 --lvot-diam 1.7 --lvot-vti 17.7 --bb 65 --tb 165
```

Atau pakboss kirim form isian 9 nomor ke saya, saya yang proses.
