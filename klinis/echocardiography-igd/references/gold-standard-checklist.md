# Gold Standard Checklist — Echocardiography Lengkap + Hemodinamik

> Berdasarkan input form isian echo Pakboss.
> Interpretasi sendiri — jangan copas mentah.
> Hanya parameter yang diisi yang dicantumkan.
> Format: **Interpretasi dulu, parameter dalam kurung.**

---

## 1. STRUKTUR OUTPUT WAJIB

### Blok Echocardiography Bedside
```
*Echocardiography Bedside (DD-MM-YYYY):*
[PH section jika ada]
[Trombus section jika ada]
- Normal/Depressed LV Systolic Function, EF ...%
- Normal RV systolic function / RV systolic dysfunction, TAPSE ... cm
Cardiac Valves:
- Mitral: ...
- Aorta: 3 cuspis, calcification (-), Normal function and movement [default]
- Pulmonal: ...
- Tricuspid: ...
[RA dilatation, RV dilatation, dll + parameter dalam kurung satu baris]
[Concentric remodeling / LVH jika ada + parameter]
[Regional Wall Motion: ...]
[eRAP: ... mmHg (exp/insp cm)]
[Grade I/II/III LV Diastolic Dysfunction + parameter]
[No pericardial effusion / Pericardial effusion ...]
```

### Blok Echo Hemodinamik
```
*Echo Hemodinamik:*
TD .../... mmHg
MAP ... mmHg
HR ... bpm
LVOT Diam ... cm
LVOT VTI ... cm
LVSV ... ml
LVCO ... L/min
eRAP ... mmHg
PCWP ... mmHg (E/e' avg ...)  — hanya jika data E/A, E Septal, E Lateral tersedia
SVR ... dynes/sec/cm⁻⁵
BSA ... m²
CI ... L/min/m²
CPO ... watt
CPI ... watt/m²
```

### Blok Lung US (WAJIB SELALU ADA)
```
Lung US:
Lung sliding (+), pleural line irregular, A line (+), B line (-), pleural effusion (-)
```
Sesuaikan jika ada temuan.

### Aturan dasar format output:
- **No pipe `|`** di output laporan
- **Interpretasi dulu**, parameter dalam kurung — contoh: "Concentric remodeling (LVMI 70.15 g/m², RWT 0.59)"
- Dimensi + geometri jadi **SATU baris** kalau semuanya normal: "Normal Cardiac Dimensions (LVIDd ...)"
- Jika ada dilatasi → tulis "RA dilatation, RV dilatation with LV-D shaped (parameter...)"
- TAPSE satuan **cm** (bukan cm/s)
- Nama katup di output: **lengkap** (MR→Mitral Regurgitation, AR→Aortic Regurgitation, PR→Pulmonary Regurgitation, MS→Mitral Stenosis, AS→Aortic Stenosis). **TR tetap TR.**

---

## 2. PARAMETER DEMOGRAFI & INPUT

| Parameter | Sumber | Wajib? |
|-----------|--------|--------|
| Tanggal | Input pakboss | ✓ |
| TDS / TDD | Monitor TTV | ✓ |
| HR | Monitor TTV | ✓ |
| BB / TB | Input pakboss atau rekam medis | ✓ untuk BSA |
| LVOT Diam | Input pakboss (dari echo) | ✓ untuk LVSV/CO |

---

## 3. LV FUNCTION (No. 1 input)

### Nilai Normal
| Parameter | Normal | Mild ↓ | Moderate ↓ | Severe ↓ |
|-----------|--------|--------|------------|----------|
| EF TEICH | ≥ 55% | 45-54% | 30-44% | < 30% |
| EF Biplane | ≥ 55% | 45-54% | 30-44% | < 30% |

### Interpretasi Output
- EF ≥ 55% → "Normal LV Systolic Function, EF ...% (TEICH)"
- EF 45-54% → "Mildly Depressed LV Systolic Function, EF ...% (TEICH)"
- EF 30-44% → "Moderately Depressed LV Systolic Function, EF ...% (TEICH)"
- EF < 30% → "Severely Depressed LV Systolic Function, EF ...% (TEICH)"

### Format
```
- Normal LV Systolic Function, EF 62% (TEICH)
```
Jika biplane juga ada: `EF 62% (TEICH), EF 60% (Biplane)`

---

## 4. RV FUNCTION (No. 2 input)

### Nilai Normal
| Parameter | Normal | Abnormal |
|-----------|--------|----------|
| TAPSE | ≥ 1.7 cm | < 1.7 cm |
| S' Lateral | ≥ 9.5 cm/s | < 9.5 cm/s |

### Interpretasi
- TAPSE ≥ 1.7 cm → "Normal RV systolic function"
- TAPSE 1.5-1.6 cm → "Borderline RV systolic function"
- TAPSE < 1.5 cm → "RV Systolic Dysfunction"

### Format
```
- Normal RV systolic function, TAPSE 2.8 cm, S' lateral 13 cm/s
```

---

## 5. CARDIAC VALVES (No. 3 input — bare code)

| Input code | Arti | Kode lain |
|------------|------|-----------|
| N / Norm / Normal | Normal function and movement | "N" |
| Mild MR | Mitral Regurgitation grade mild | MR, Moderate MR, Severe MR |
| Mild AR | Aortic Regurgitation grade mild | AR, Moderate AR, Severe AR |
| Mild PR | Pulmonary Regurgitation grade mild | PR |
| Mild TR | Tricuspid Regurgitation grade mild | TR, Moderate TR, Severe TR |
| MS | Mitral Stenosis | MS |
| AS | Aortic Stenosis | AS |
| — / blank | **Jangan cantumkan baris katup itu** | |

### Default output per katup

**Mitral (jika N):**
```
- Mitral: Normal function and movement
```

**Aorta (jika N — SELALU tambahkan detail cuspis):**
```
- Aorta: 3 cuspis, calcification (-), Normal function and movement
```

**Pulmonal (jika N):**
```
- Pulmonal: Normal function and movement
```

**Tricuspid (jika N):**
```
- Tricuspid: Normal function and movement
```

### Jika ada abnormality — lihat Bagian Masalah Katup (no. 10)

---

## 6. DIMENSI KAMAR JANTUNG (No. 4 input)

### Nilai Normal & Interpretasi

| Parameter | Normal | Dilatasi |
|-----------|--------|----------|
| LVIDd | 3.5-5.7 cm (wanita), 3.9-5.3 cm (pria) | > normal |
| LA mayor | < 4.0 cm | ≥ 4.0 cm → LA dilatation |
| LA minor | < 3.0 cm | ≥ 3.0 cm |
| RA area | < 18 cm² | ≥ 18 cm² → RA dilatation |
| RVDB (RV basal) | < 4.2 cm | ≥ 4.2 cm → RV dilatation |
| LA/Ao | < 1.5 | ≥ 1.5 |

### Format Output

**Semua normal:**
```
Normal Cardiac Dimensions (LVIDd 3.9 cm, LA mayor 4.3 cm, LA minor 2.9 cm, RA area 11.3 cm², RVDB 2.6 cm)
```

**Ada dilatasi — tulis kelainan dulu, baru parameter:**
```
LA dilatation, RA dilatation (LVIDd 3.9 cm, LA mayor 4.3 cm, LA minor 2.9 cm, RA area 21.3 cm², RVDB 2.6 cm)
```

**Jika ada LV-D shaped + RV dilatasi:**
```
RA dilatation, RV dilatation with LV-D shaped (RA area 21.3 cm², RVDB 4.5 cm, LA mayor 3.6 cm, LA minor 2.5 cm, LVMI 70.15 g/m², RWT 0.59)
```

---

## 7. LV GEOMETRY — LVH & RWT (No. 5 input)

### Rumus
- **RWT** = (2 × Posterior Wall Thickness) / LVIDd
  - Atau RWT = (IVSd + PWd) / LVIDd
- **LVMI** = LV Mass / BSA
  - LV Mass = 0.8 × {1.04 × [(LVIDd + IVSd + PWd)³ - LVIDd³]} + 0.6
- Normal LVMI: wanita ≤ 95 g/m², pria ≤ 115 g/m²

### Interpretasi
| RWT | LVMI | Klasifikasi |
|-----|------|-------------|
| ≤ 0.42 | Normal | Normal geometry (skip baris) |
| > 0.42 | Normal | **Concentric remodeling** |
| ≤ 0.42 | ↑ | **Eccentric LVH** |
| > 0.42 | ↑ | **Concentric LVH** |

### Format
```
Concentric remodeling (LVMI 70.15 g/m², RWT 0.59)
```
Langung tulis klasifikasi + parameter — jangan "LV Geometry: ..." pisah baris.

---

## 8. REGIONAL WALL MOTION — RWMA (No. 6 input)

| Input | Output |
|-------|--------|
| No / Normal / — | Regional Wall Motion: Global normokinetic |
| ADA sebut segment | Regional Wall Motion: Hypokinesis/Akinesis segment [sebut] |

### Format
```
Regional Wall Motion: Global normokinetic
```
atau
```
Regional Wall Motion: Hypokinesis segment anterior wall (mid-distal) & apex
```

---

## 9. LV DIASTOLIC FUNCTION (No. 7 input)

### Parameter Kunci
| Parameter | Makna |
|-----------|-------|
| E wave | Peak early filling velocity (m/s) |
| A wave | Peak late filling velocity (m/s) |
| E/A ratio | Grade: > 0.8 → normal/grade I (tergantung umur) |
| E' Med (septal e') | Normal ≥ 7 cm/s |
| E' Lat (lateral e') | Normal ≥ 10 cm/s |
| E/e' avg | PCWP prediktor: < 8 → normal filling, 8-14 → gray zone, > 14 → ↑ filling pressure |

### Grade Diastolic Dysfunction
| Grade | E/A | E' Med | E' Lat | E/e' avg | Interpretasi |
|-------|-----|--------|--------|----------|-------------|
| Normal | > 0.8 | ≥ 7 | ≥ 10 | < 8 | Normal diastolic function |
| I | < 0.8 | < 7 | < 10 | < 8 | Grade I (Impaired Relaxation) |
| II | 0.8-2.0 | < 7 | < 10 | 8-14 | Grade II (Pseudonormal) |
| III | > 2.0 | < 7 | < 10 | > 14 | Grade III (Restrictive) |

### Format
```
Grade I LV Diastolic Dysfunction (E/A 0.86, E' Med 11 cm/s, E' Lat 8 cm/s)
```
**Catatan:** Jika E/A, E' Med, E' Lat semua normal → "Normal diastolic function" — jangan pakai grade.

---

## 10. PERIKARDIUM (No. 8 input)

| Input | Output |
|-------|--------|
| N / Normal / — / No | No pericardial effusion |
| Ada jumlah | Pericardial effusion [jumlah] |

### Format
```
No pericardial effusion
```
atau
```
Pericardial effusion moderate (1.5 cm circumferential)
```

---

## 11. LAIN-LAIN (No. 9 input)

Input bebas. Jika ada trombus:
```
Trombus seen at LV apex (2.1 × 1.5 cm)
```
Jika ada PFO, ASD, VSD, PDA, dll:
```
PFO with left-to-right shunt
```

---

## 12. HEMODINAMIK — ECHO KALKULASI OTOMATIS

### Inputan Pakboss
- TDS, TDD, HR — dari monitor
- LVOT Diam — dari echo
- LVOT VTI — dari echo (PW Doppler di LVOT)
- IVC exp / IVC insp — dari echo
- BB, TB — untuk BSA

### Kalkulasi (script echo-calculator.py)

| Parameter | Rumus | Satuan |
|-----------|-------|--------|
| MAP | TDD + 1/3(TDS - TDD) | mmHg |
| LVOT Area (CSA) | 0.785 × (LVOT Diam)² | cm² |
| LVSV (Stroke Volume) | CSA × LVOT VTI | ml |
| LVCO (Cardiac Output) | LVSV × HR / 1000 | L/min |
| eRAP | Dari IVC (lihat tabel) | mmHg |

### eRAP Table (IVC)

| IVC Diameter (exp) | Collapsibility | eRAP |
|--------------------|----------------|------|
| < 2.1 cm | > 50% | 3 mmHg |
| < 2.1 cm | < 50% | 8 mmHg |
| ≥ 2.1 cm | > 50% | 8 mmHg |
| ≥ 2.1 cm | < 50% | 15 mmHg |

IVC CI = Collapsibility Index = (IVC exp - IVC insp) / IVC exp × 100%

### Parameter Tambahan (kalkulasi)

| Parameter | Rumus | Satuan |
|-----------|-------|--------|
| BSA | Mosteller: √[(BB × TB)/3600] | m² |
| CI (Cardiac Index) | LVCO / BSA | L/min/m² |
| SVR | 80 × (MAP - RAP) / LVCO | dynes/sec/cm⁻⁵ |
| PCWP | Jika E/e' avg ada: 1.24 × (E/e' avg) + 1.9 (Nagueh formula) | mmHg |
| CPO (Cardiac Power Output) | MAP × LVCO / 451 | watt |
| CPI (Cardiac Power Index) | MAP × CI / 451 | watt/m² |
| SVRI | 80 × (MAP - RAP) / CI | dynes/sec/cm⁻⁵·m² |

### Normal Values Hemodinamik
| Parameter | Normal |
|-----------|--------|
| LVSV | 60-120 ml |
| LVCO | 4-8 L/min |
| CI | 2.5-4.0 L/min/m² |
| SVR | 800-1200 dynes/sec/cm⁻⁵ |
| PCWP | 8-12 mmHg |
| eRAP (CVP) | 2-6 mmHg |
| CPO | > 1.0 watt |
| MAP | 70-100 mmHg |

### Format Output Hemodinamik
```
*Echo Hemodinamik:*
TD 145/90 mmHg
MAP 108 mmHg
HR 92 bpm
LVOT Diam 1.9 cm
LVOT VTI 16.9 cm
LVSV 47.9 ml
LVCO 4.41 L/min
eRAP 8 mmHg
PCWP 12.5 mmHg (E/e' avg 9.1)
SVR 1821 dynes/sec/cm⁻⁵
BSA 1.87 m²
CI 2.35 L/min/m²
CPO 1.06 watt
CPI 0.57 watt/m²
```

---

## 13. MASALAH KATUP (jabaran lengkap)

### Mitral Regurgitation (MR)

| Grade | ERO (cm²) | RV (ml) | VC (cm) | Regurg Jet Length |
|-------|-----------|---------|---------|-------------------|
| Mild | < 0.20 | < 30 | < 0.3 | < 20% LA |
| Moderate | 0.20-0.39 | 30-59 | 0.3-0.69 | 20-40% LA |
| Severe | ≥ 0.40 | ≥ 60 | ≥ 0.7 | > 40% LA |

**Format:**
```
Mild MR (ERO 0.15 cm², RV 22 ml, VC 0.25 cm)
Moderate MR (ERO 0.28 cm², RV 45 ml, VC 0.4 cm, Regurg Jet Length > 25% LA)
```

### Mitral Stenosis (MS)

| Grade | MVA planimetry | MVA PHT | Mean PG | Mean PHT |
|-------|---------------|---------|---------|----------|
| Mild | > 1.5 cm² | > 1.5 cm² | < 5 mmHg | |
| Moderate | 1.0-1.5 cm² | 1.0-1.5 cm² | 5-10 mmHg | |
| Severe | < 1.0 cm² | < 1.0 cm² | > 10 mmHg | > 220 ms |

**Wilkins Score** (per skor 1-4):
- Leaflet mobility
- Leaflet thickening
- Subvalvular thickening
- Calcification
- Total score 1-16

**Format:**
```
MS (MVA planimetry 1.2 cm², MVA PHT 1.1 cm², Mean PG 8 mmHg, Wilkins Score 7)

**Tambahan:** Annulus mitral ... cm — jika annulus dilatasi ≥ 3.5 cm: "Mitral Annular Dilatation"
```

### Aortic Regurgitation (AR)

| Grade | PHT (ms) | ERO (cm²) | RV (ml) | VC (cm) | Holodiastolic Reversal Flow |
|-------|---------|-----------|---------|---------|---------------------------|
| Mild | > 500 | < 0.10 | < 30 | < 0.3 | Tidak ada / hanya di awal |
| Moderate | 200-500 | 0.10-0.29 | 30-59 | 0.3-0.59 | Ada di desendens |
| Severe | < 200 | ≥ 0.30 | ≥ 60 | ≥ 0.6 | Holodiastolic reversal seluruh |

**Format:**
```
Mild AR (PHT 560 ms)
Moderate AR (PHT 340 ms, ERO 0.18 cm², RV 42 ml, VC 0.4 cm, Holodiastolic Reversal Flow Peak Vel 15 cm/s)
Severe AR (PHT 180 ms, ERO 0.35 cm², RV 65 ml, VC 0.7 cm, Holodiastolic Reversal Flow Peak Vel 22 cm/s)
```

### Aortic Stenosis (AS)

| Grade | AV Vmax (m/s) | Mean PG (mmHg) | AVA continuity eq (cm²) | AVA planimetry (cm²) | SVI (ml/m²) |
|-------|--------------|----------------|------------------------|---------------------|-------------|
| Mild | 2.0-2.9 | < 20 | > 1.5 | > 1.5 | |
| Moderate | 3.0-3.9 | 20-39 | 1.0-1.5 | 1.0-1.5 | |
| Severe | ≥ 4.0 | ≥ 40 | < 1.0 | < 1.0 | < 35 (low-flow) |

**Continuity equation:** AVA = (CSA_LVOT × LVOT VTI) / AV VTI

**Format:**
```
Moderate AS (AV Vmax 3.5 m/s, mean PG 30 mmHg, AVA continuity eq 1.15 cm², SVI 38 ml/m²)
```

**Data tambahan Aorta (ukuran):**
| Level | Normal | Dilatasi |
|-------|--------|----------|
| Aortic annulus | 2.0-2.6 cm | > 2.6 cm |
| Sinus valsava | 2.9-4.5 cm | > 4.0 cm (pria) / > 3.6 cm (wanita) |
| ST junction | 2.2-3.6 cm | > 3.6 cm |
| Ascending aorta | < 3.7 cm | ≥ 4.0 cm → Aortic root dilatation |

### Pulmonal Regurgitation (PR)

| Grade | PHT (ms) | Regurg Jet Width | PV AccT | PASP |
|-------|---------|-----------------|---------|------|
| Mild | > 200 | < 1/3 RVOT | — | — |
| Moderate | — | > 1/3 RVOT | — | — |

**Format:**
```
Mild PR (PR Regurgitant Jet < 1/3 RVOT)
Moderate PR (Regurg Jet Width > 1/3 RVOT)

Jika MPA dilatasi: , MPA Dilatation (3.8 cm)
```

**PV Accelerated Time (PV AccT):**
- Normal > 130 ms
- 90-130 ms → Intermediate probability PH
- < 90 ms → High probability PH

**Format PASP / mPAP jika ada:**
```
Mild PR, mPAP 25 mmHg
```

**mPAP formulas:**
- mPAP = 79 - (0.45 × PV AccT) — jika AccT tersedia
- mPAP = 4 × TR Vmax² + eRAP — jika TR jet tersedia

### Tricuspid Regurgitation (TR)

| Grade | VC (cm) | Regurg Jet Area | Hepatic Vein Flow |
|-------|---------|----------------|-------------------|
| Mild | < 0.3 | < 20% RA | Normal |
| Moderate | 0.3-0.69 | 20-40% RA | Normal/blunted |
| Severe | ≥ 0.7 | > 40% RA | Systolic reversal |

**Format:**
```
Mild TR
Moderate TR (Vmax 3.2 m/s, MaxPG 41 mmHg), Intermediate Probability of PH
Severe TR (Vmax 4.1 m/s, MaxPG 67 mmHg), High Probability of PH
```

**TR + PH Probability Rules:**

| TR Vmax | Tanda RV Overload* | PH Probability |
|---------|-------------------|----------------|
| ≤ 2.8 | Tidak ada | Low |
| ≤ 2.8 | Ada | Intermediate |
| 2.8-3.4 | Tidak ada | Intermediate |
| 2.8-3.4 | Ada | High |
| > 3.4 | — | High |

*\*Tanda RV overload: D-shaped LV, RV dilatasi, RA dilatasi (area > 18 cm²), RVOT AccT < 105 ms*

**Format PH:**
- Low → cantumkan setelah grade: `, Low Probability of Pulmonary Hypertension`
- Intermediate: `, Intermediate Probability of Pulmonary Hypertension`
- High: `, High Probability of Pulmonary Hypertension`

**Note:** Untuk TR Mild → cukup tulis "Mild TR" saja (tanpa PH probability) — hanya Moderate/Severe yang perlu PH probability.

---

## 14. LUNG ULTRASOUND (LUS) — WAJIB

**Prinsip:**
- LUS selalu ada di laporan echo, **di bawah Echo Hemodinamik**
- Jika pakboss **kosong/tidak menyebut** → artinya normal: A line (+), B line (-), pleural effusion (-)
- Lung sliding (+) bila normal

### B Line
- Fokal (1-2 intercostal) → bisa normal/pathologi
- Multiple (≥ 3) → interstitial syndrome (edema paru, fibrosis, pneumonia)
- Lokasi: Apical, mid, basal; anterior/lateral/posterior

### Pleural Effusion
- Kuantifikasi: jarak dari paru ke diafragma
- Minimal: < 2 cm (non-drainable)
- Moderate: 2-5 cm
- Large: > 5 cm

### Format
```
Lung US:
Lung sliding (+), pleural line irregular, A line (+), B line (-), pleural effusion (-)
```

**Jika ada temuan:**
```
Lung US:
Lung sliding (+), pleural line irregular, A line (+), B line (+) multiple bilateral basal, pleural effusion (-)
```

```
Lung US:
Lung sliding (+), pleural line irregular, A line (-), B line (+) multiple bilateral, pleural effusion (+) 3.2 cm right basal
```

---

## 15. COMPLETE OUTPUT TEMPLATE — GOLD STANDARD

```
*Echocardiography Bedside (10-06-2026):*
- Normal LV Systolic Function, EF 62% (TEICH)
- Normal RV systolic function, TAPSE 2.8 cm, S' lateral 13 cm/s

Cardiac Valves:
- Mitral: Normal function and movement
- Aorta: 3 cuspis, calcification (-), Normal function and movement
- Pulmonal: Normal function and movement
- Tricuspid: Normal function and movement

Normal Cardiac Dimensions (LVIDd 3.9 cm, LA mayor 4.3 cm, LA minor 2.9 cm, RA area 11.3 cm², RVDB 2.6 cm)
Concentric remodeling (LVMI 70.15 g/m², RWT 0.59)
Regional Wall Motion: Global normokinetic
eRAP: 8 mmHg (1.1/0.9 cm)
Grade I LV Diastolic Dysfunction (E/A 0.86, E' Med 11 cm/s, E' Lat 8 cm/s)
No pericardial effusion

*Echo Hemodinamik:*
TD 145/90 mmHg
MAP 108 mmHg
HR 92 bpm
LVOT Diam 1.9 cm
LVOT VTI 16.9 cm
LVSV 47.9 ml
LVCO 4.41 L/min
eRAP 8 mmHg
PCWP 12.5 mmHg (E/e' avg 9.1)
SVR 1821 dynes/sec/cm⁻⁵
BSA 1.87 m²
CI 2.35 L/min/m²
CPO 1.06 watt
CPI 0.57 watt/m²

Lung US:
Lung sliding (+), pleural line irregular, A line (+), B line (-), pleural effusion (-)
```

---

## 16. QUICK REFERENCE — Nilai Normal Satu Tampilan

| Parameter | Normal | Batas |
|-----------|--------|-------|
| EF TEICH | ≥ 55% | 45-54% (mild), 30-44% (mod), <30% (severe) |
| TAPSE | ≥ 1.7 cm | 1.5-1.6 (borderline), <1.5 (dysfunction) |
| S' Lateral | ≥ 9.5 cm/s | < 9.5 (abnormal) |
| LVIDd | 3.5-5.7 cm | > batas = dilatasi |
| LA mayor | < 4.0 cm | ≥ 4.0 = dilatasi |
| RA area | < 18 cm² | ≥ 18 = dilatasi |
| RVDB | < 4.2 cm | ≥ 4.2 = dilatasi |
| RWT | ≤ 0.42 | > 0.42 = concentric |
| LVMI | Pria ≤ 115, Wanita ≤ 95 | ↑ = LVH |
| E/A | > 0.8 | < 0.8 = Grade I |
| E' Med | ≥ 7 cm/s | < 7 = abnormal diastolik |
| E' Lat | ≥ 10 cm/s | < 10 = abnormal diastolik |
| E/e' avg | < 8 | > 14 = ↑ filling pressure |
| LVSV | 60-120 ml | |
| LVCO | 4-8 L/min | |
| CI | 2.5-4.0 L/min/m² | |
| SVR | 800-1200 dynes | |
| PCWP | 5-12 mmHg | |
| eRAP | 2-6 mmHg | |
| MAP | 70-100 mmHg | |
| CPO | > 1.0 watt | |
| IVC exp | < 2.1 cm | ≥ 2.1 = dilated |

---

## 17. QUICK REFERENCE — Grade Katup Satu Tampilan

### Regurgitasi

| Katup | Mild | Moderate | Severe |
|-------|------|----------|--------|
| MR - ERO | < 0.20 | 0.20-0.39 | ≥ 0.40 |
| MR - RV | < 30 | 30-59 | ≥ 60 |
| MR - VC | < 0.3 | 0.3-0.69 | ≥ 0.7 |
| AR - PHT | > 500 | 200-500 | < 200 |
| AR - ERO | < 0.10 | 0.10-0.29 | ≥ 0.30 |
| AR - VC | < 0.3 | 0.3-0.59 | ≥ 0.6 |
| PR - Jet | < 1/3 RVOT | > 1/3 RVOT | — |
| TR - VC | < 0.3 | 0.3-0.69 | ≥ 0.7 |

### Stenosis

| Katup | Mild | Moderate | Severe |
|-------|------|----------|--------|
| MS - MVA | > 1.5 | 1.0-1.5 | < 1.0 |
| MS - Mean PG | < 5 | 5-10 | > 10 |
| AS - Vmax | 2.0-2.9 | 3.0-3.9 | ≥ 4.0 |
| AS - Mean PG | < 20 | 20-39 | ≥ 40 |
| AS - AVA | > 1.5 | 1.0-1.5 | < 1.0 |

---

> **Format file ini:** gold standard reference. Baca sebelum menulis laporan echo untuk memastikan semua parameter terisi dengan interpretasi yang benar. Jangan copy-paste form isian — interpretasi sendiri.
