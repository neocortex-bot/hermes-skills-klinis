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
1. LV func: ___ | EF TEICH ___% | EF Biplane ___%
2. RV func: ___ | TAPSE ___ | S' Lat ___
3. Mitral: ___ | Aorta: ___ | Pulmonal: ___ | Tricuspid: ___
4. LVIDd ___ | LA ___ / ___ | RA ___ / ___ | RVDB ___ | LA/Ao ___
5. LVH: ___ | LVMI ___ | RWT ___
6. RWMA: ___
7. E/A ___ | E' Med ___ | E' Lat ___ | E/E' ___ | Grade ___
8. Perikard: ___
9. Lain: ___

TDS ___ | TDD ___ | HR ___ | LVOT Diam ___ | LVOT VTI ___
IVC exp ___ | IVC insp ___ | BB ___ | TB ___
```

**Aturan:** Jika pakboss lampirkan nomor 3 (Katup), artinya ada masalah katup — JANGAN tulis "Normal function and movement". Tulis sesuai yang pakboss sebutkan. Jika tidak disebut, jangan sematkan baris katup itu.

**Parameter katup severe — referensi bila ada masalah katup (hanya yang disebut):**

| Katup | Kondisi | Parameter |
|-------|---------|-----------|
| Mitral | Severe MR | MR ERO ... cm2, MR RV ... ml, MR VC ... cm, Regurgitant Jet Length > 50% LA, Carpentier ... Annulus mitral ... cm |
| Mitral | Severe MS | MVA planimetry: ... cm2, MVA by PHT: ... cm2, MS Mean PG: ... mmHg, Mean PHT: ... ms, Wilkins Score: ... |
| Aorta | Severe AR | AR PHT ... ms, AR ERO ... cm2, AR RV ... ml, AR VC ... cm, Regurgitant Jet Length > 65% LVOT; Holodiastolic Reversal Flow Peak Velocity ... cm/s; Aortic root: annulus ... cm, sinus valsava ... cm, sinotubular junction ... cm, ascenden ... cm |
| Aorta | Severe AS | AVA planimetry ... cm2, AV Vmax ... m/s, AV mean PG ... mmHg, AV continuity equation ... cm2, SVI ... ml/m2, AV VTI ... mmHg |
| Tricuspid | Severe TR | Severe TR with [Central/Excentric] Jet (Regurgitant Jet Area > 35% RA, TR Vmax ... m/s, TR maxPG ... mmHg, TR VC ... cm, Systolic Reversal Flow on Hepatic Vein) with [Low/Intermediate/High] Probability of PH |
| Pulmonal | Mod-Sev PR | PR PHT ... ms, Regurgitant Jet Width > 2/3 RVOT, PV AccT ... ms, PASP ... mmHg, mPAP ... mmHg |

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

## Template Parameter Katup

Hanya cantumkan katup yang disebutkan dan parameternya.

**MR:** Mild MR / Moderate MR (MR ERO ... cm2, MR RV ... ml, MR VC ... cm, Jet ...% LA) / Severe MR (...)
**MS:** MVA planimetry ... cm2, MVA by PHT ... cm2, MS Mean PG ... mmHg, Wilkins Score: ...
**AR:** Mild/Moderate/Severe AR (AR PHT ... ms, AR ERO ... cm2, AR VC ... cm, Jet ...% LVOT)
**AS:** AVA planimetry ... cm2, AV Vmax ... m/s, AV mean PG ... mmHg, SVI ... ml/m2
**TR:** Mild/Moderate/Severe TR (TR Vmax ... m/s, TR maxPG ... mmHg, TR VC ... cm)
**PR:** Mild/Moderate/Severe PR (PR PHT ... ms, Jet Width ...% RVOT), PV AccT ... ms

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
- Aorta: 3 cuspis, Normal function and movement
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
  --aorta "3 cuspis, calcification (-), Normal Function and Movement" \
  --mitral "Normal Function and Movement" \
  --tricuspid "Normal Function and Movement" \
  --pulmonal "Normal Function and Movement" \
  --lvidd 6.71 --la-mayor 4.20 --la-minor 3.37 --ra-mayor 2.97 --ra-minor 2.40 --rvdb 2.84 \
  --lvh-type Eccentric --lvmi 166 --rwt 0.17 \
  --rwma "Akinetic Apicoanterior, Badal Mid Anteroseptal, Hypokinetic Basal Mid Anterolateral" \
  --ivc-exp 1.22 --ivc-insp 0.6 \
  --ea 1.13 --e-med 9.0 --e-lat 13.3 --grade "Grade I" \
  --tds 105 --tdd 70 --hr 108 --lvot-diam 1.7 --lvot-vti 17.7 --bb 65 --tb 165
```

Atau pakboss kirim form isian 9 nomor ke saya, saya yang proses.
