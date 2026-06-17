# ⛔ GOLD STANDARD CHECKLIST — Echocardiography + Hemodinamik

> **SEBELUM MENGIRIM LAPORAN ECHO, WAJIB CENTANG SEMUA ITEM DI BAWAH INI SATU PER SATU**
> **SETIAP ADA KOREKSI, WAJIB CENTANG ULANG SEMUA CHECKLIST**
> Interpretasi sendiri — jangan copas mentah. Hanya parameter yang diisi.

---

## FORMAT ISIAN PAKBOSS (REFERENSI CEPAT)

Kirim nomor dan nilainya saja:
```
Tanggal:
LV func: | EF TEICH % | EF Biplane ___%
RV func: | TAPSE | S' Lat ___
Mitral: | Aorta: | Pulmonal: | Tricuspid:
LVIDd | LA / | RA area | RVDB _ | LA/Ao ___
LVH: | LVMI | RWT ___
RWMA: ___
E value | E/A | E' Med | E' Lat | E/E' _ | Grade ___
Perikard: ___
Lain: ___

TDS | TDD | HR | LVOT Diam | LVOT VTI __
IVC exp | IVC insp | BB | TB _

LUS (isi jika ada temuan, kosongkan jika normal):
B line: | lokasi:
Pleural effusion: cm | lokasi:

Masalah katup (jabarkan di sini):
```

---

## ⛔ CHECKLIST — SEBELUM MENGIRIM ⛔

### A. FORMAT UMUM
- [ ] **No pipe `|`** di output laporan
- [ ] **Laporan dikirim dalam CODE BLOCK** (``` ```) — bukan teks biasa
- [ ] **Tanpa bullet points / list markdown** untuk konten laporan echo — plain text dalam code block
- [ ] **Interpretasi dulu**, parameter dalam kurung — bukan parameter dulu baru interpretasi
- [ ] TAPSE satuannya **cm** (bukan cm/s)
- [ ] S' Lateral satuannya **cm/s**
- [ ] Nama katup di output **lengkap**: MR→Mitral Regurgitation, AR→Aortic Regurgitation, PR→Pulmonary Regurgitation, MS→Mitral Stenosis, AS→Aortic Stenosis. **TR tetap TR**
- [ ] Hanya parameter yang diisi pakboss yang dicantumkan — jangan tambah-tambah
- [ ] Parameter yang wajib ada namun tidak diisi → tetap ditulis, nilai diganti **`...`**

### B. LV FUNCTION (No. 1)
- [ ] **WAJIB:** Jika pakboss memberi EF Biplane, tulis di baris LV Function setelah EF TEICH: `EF 65% (TEICH), EF 64% (Biplane)`
- [ ] EF ≥ 55% → "Normal LV Systolic Function"
- [ ] EF 41-54% → "Mildly Abnormal LV Systolic Function"
- [ ] EF 30-40% → "Moderately Abnormal LV Systolic Function"
- [ ] EF < 30% → "Severely Abnormal LV Systolic Function"
- [ ] Format: `Normal LV Systolic Function, EF 65% (TEICH)`
- [ ] Jika biplane ada: `Normal LV Systolic Function, EF 65% (TEICH), EF 64% (Biplane)`

### C. RV FUNCTION (No. 2)
- [ ] TAPSE ≥ 1.7 cm → "Normal RV systolic function"
- [ ] TAPSE < 1.7 cm → "Decreased RV Systolic function"
- [ ] Format: `Normal RV systolic function, TAPSE 2.8 cm, S' lateral 13 cm/s`

### D. CARDIAC VALVES (No. 3)
- [ ] **Mitral N** → "Mitral: Normal function and movement"
- [ ] **Aorta N** → "Aorta: 3 cuspis, calcification (-), Normal function and movement"
- [ ] **Pulmonal N** → "Pulmonal: Normal function and movement"
- [ ] **Tricuspid N** → "Tricuspid: Normal function and movement"
- [ ] Jika katup tidak disebut → **semua katup harus disebutkan, tidak disebut artinya normal**
- [ ] Jika ada abnormality → lihat bagian **Masalah Katup** (section J)
- [ ] Section header: **"Cardiac Valves:"** tanpa indentasi
- [ ] **Jangan tulis "Normal function and movement" bila ada masalah katup meskipun Mild/ringan**

### E. DIMENSI RUANG JANTUNG (No. 4)
- [ ] LVIDd 3.5-5.4 cm → normal
- [ ] **LA mayor** normal: **< 6.1 cm** (bukan 4.5!) → jika ≥ 6.1 tulis **LA dilatation**
- [ ] **LA minor** normal: **< 4.5 cm** → jika ≥ 4.5 tulis **LA dilatation**
- [ ] **WAJIB:** LA mayor dan LA minor HARUS selalu ditulis di parameter, meskipun normal. Jika LA minor tidak disebut pakboss → tulis `LA minor ... cm`
- [ ] RA area < 18 cm² → normal; ≥ 18 → **RA dilatation**
- [ ] RVDB < 4.2 cm → normal; ≥ 4.2 → **RV dilatation**
- [ ] Semua normal → `Normal Cardiac Dimensions`
- [ ] Ada dilatasi → tulis kelainan dulu baru parameter dlm kurung: `LA dilatation, RV dilatation (LVIDd ..., ...)`
- [ ] Jika RV dilatasi + D-shaped LV → `RV dilatation with LV-D shaped`
- [ ] **Dimensi + geometri jadi SATU baris** kalau semuanya normal. Tulis di laporan = `Normal Cardiac Dimensions`
- [ ] **LA mayor < 6.1 cm → BUKAN LA dilatation.** Jangan pernah bilang LA dilatation untuk LA mayor 5.6 cm.

### F. LV GEOMETRY (No. 5)
- [ ] **Tidak tulis "LV Geometry:"** — bila semua normal tulis saja `Normal Cardiac Dimensions`
- [ ] Kecuali ada LVH → `Normal Cardiac Dimensions with Concentric LVH`
- [ ] RWT normal + LVMI normal → masukkan dan ikutkan parameter ini di **Cardiac Dimensions**
- [ ] RWT > 0.42 + LVMI normal → **Concentric remodeling**
- [ ] RWT ≤ 0.42 + LVMI ↑ → **Eccentric LVH**
- [ ] RWT > 0.42 + LVMI ↑ → **Concentric LVH**
- [ ] Format: `Concentric remodeling (LVMI ... g/m², RWT ...)` — jangan pisah baris
- [ ] Format: `Concentric LVH (LVMI ... g/m², RWT ...)` — jangan pisah baris
- [ ] Format: `Eccentric LVH (LVMI ... g/m², RWT ...)` — jangan pisah baris

### G. REGIONAL WALL MOTION (No. 6)
- [ ] Normal / Tidak ada → `Regional Wall Motion: Global normokinetic`
- [ ] Ada segment → `Regional Wall Motion: Hypokinesis segment ..., Akinetic segment ...`

### H. LV DIASTOLIC FUNCTION (No. 7)
- [ ] E/A, E' Med, E' Lat semua normal → **jangan skip baris** — tulis ulang semuanya dengan parameter normal
- [ ] E/A < 0.8 + E' Med/Lat ↓ → **Grade I LV Diastolic Dysfunction**
- [ ] E/A 0.8-2.0 + E' ↓ + E/e' 8-14 → **Grade II LV Diastolic Dysfunction**
- [ ] E/A > 2.0 + E' ↓ + E/e' > 14 → **Grade III LV Diastolic Dysfunction**
- [ ] Format: `Grade I LV Diastolic Dysfunction (E/A ..., E' Med ..., E' Lat ...)` — **interpretasi dulu**
- [ ] **E/e' avg hanya disebut jika ada kalkulasi PCWP** — tidak perlu di baris diastolik
- [ ] Jika E value disebut tapi E/A tidak → tulis `E value ... m/s` saja

### I. PERIKARDIUM & LAIN-LAIN (No. 8-9)
- [ ] N / Normal / — → `No pericardial effusion`
- [ ] Ada pericardial effusion → format lengkap:
```
Moderate to Large Pericardial Effusion without sign of cardiac tamponade:
- PLAX View: Posterior ... cm, Anterior ... cm
- PSAX view: Anterior ... cm, Posterior ... cm, lateral sinistra ... cm
- Apical 4 Chambers: Basal ... cm, Apical ... cm, Lateral LV ... cm
- Subcostal View: Anterior ... cm, Posterior ... cm
- RA Collapse (-), RV Collapse (-), swinging Heart (-), Mitral Inflow Respiratory Variability ...%, Tricuspid Inflow Respiratory Variability ...%
```
- [ ] Jika ada trombus → `Trombus seen at [lokasi] (ukuran)` — taruh di paling atas echo bedside
- [ ] Jika ada PFO/ASD/VSD → sebutkan

### J. MASALAH KATUP — WAJIB DIJABARKAN

**Aturan umum:**
- [ ] Jika pakboss tulis grade tanpa angka parameter → tulis grade + lampirkan semua parameter yang ada tanpa isian, cukup pakai `"..."`, nanti diisi manual
- [ ] Jika tidak disebut sama sekali → jangan cantumkan sebagai masalah. Artinya katup tersebut "Normal function and movement"
- [ ] **Jangan tulis "Normal function and movement" bila ada masalah katup meskipun Mild/ringan**

#### Mitral Regurgitation (MR)
- [ ] Ditulis lengkap: **Mitral Regurgitation**
- [ ] Mild MR: ERO < 0.20 / RV < 30 / VC < 0.3
- [ ] Moderate MR: ERO 0.20-0.39 / RV 30-59 / VC 0.3-0.69
- [ ] Severe MR: ERO ≥ 0.40 / RV ≥ 60 / VC ≥ 0.7
- [ ] Format: `Moderate Functional Mitral Regurgitation (ERO 0.28 cm², RV 45 ml, VC 0.4 cm) with Central Jet due to MV Annular Dilatation`
- [ ] More than Moderate dan Severe → tuliskan `"Moderate Mitral Regurgitation due to ..."` — tulis titik-titik bila ada
- [ ] **Jabarkan Carpentier berapa, arah jet, primary/secondary**

#### Mitral Stenosis (MS)
- [ ] Ditulis lengkap: **Mitral Stenosis**
- [ ] Mild MS: MVA > 1.5 / Mean PG < 5
- [ ] Moderate MS: MVA 1.0-1.5 / Mean PG 5-10
- [ ] Severe MS: MVA < 1.0 / Mean PG > 10
- [ ] Format: `Severe Mitral Stenosis due to ... (MVA planimetry 1.2 cm², MVA PHT 1.1 cm², Mean PG 8 mmHg, Wilkins Score 7)`
- [ ] **Wilkins Score disebutkan.** Contoh: `Wilkins score 7 (2-2-2-1)`
- [ ] More than Moderate dan Severe → tuliskan `"Moderate Mitral Stenosis due to ..."` — tulis titik-titik bila ada

#### Aortic Regurgitation (AR)
- [ ] Ditulis lengkap: **Aortic Regurgitation**
- [ ] Mild AR: PHT > 500 / ERO < 0.10 / VC < 0.3
- [ ] Moderate AR: PHT 200-500 / ERO 0.10-0.29 / VC 0.3-0.59
- [ ] Severe AR: PHT < 200 / ERO ≥ 0.30 / VC ≥ 0.6
- [ ] Format: `Moderate Aortic Regurgitation due to ... (PHT 340 ms, ERO 0.18 cm², RV 42 ml, VC 0.4 cm, Holodiastolic Reversal Flow Peak Vel 15 cm/s)`
- [ ] More than Moderate dan Severe → tuliskan `"Moderate Aortic Regurgitation due to ..."` — tulis titik-titik bila ada

#### Aortic Stenosis (AS)
- [ ] Ditulis lengkap: **Aortic Stenosis**
- [ ] **Semua parameter isian exact dari pengukuran, bukan rentang**
- [ ] Mild AS: Vmax 2.0-2.9 / Mean PG < 20 / AVA Cont. eq > 1.5 / AVA planimetri > 1.5
- [ ] Moderate AS: Vmax 3.0-3.9 / Mean PG 20-39 / AVA planimetri > 1.0-1.5 / AVA continuity eq > 1.0-1.5
- [ ] Severe AS: Vmax ≥ 4.0 / Mean PG ≥ 40 / AVA < 1.0
- [ ] Format: `Moderate Aortic Stenosis due to ... (AV Vmax 3.5 m/s, mean PG 30 mmHg, AVA continuity eq 1.15 cm², AVA Planimetri 1.09 cm²)`
- [ ] Data aorta: annulus, sinus valsava, ST junction, ascenden — sebut jika ada dilatasi
- [ ] Aortic annulus > 2.6 cm / Sinus > 4.0 cm (pria) / Ascenden ≥ 4.0 cm → sebutkan dilatasi
- [ ] More than Moderate dan Severe → tuliskan `"Moderate Aortic Stenosis due to ..."` — tulis titik-titik bila ada

#### Pulmonal Regurgitation (PR)
- [ ] Ditulis lengkap: **Pulmonal Regurgitation**
- [ ] Mild PR: `Mild Pulmonal Regurgitation (PR Regurgitant Jet < 1/3 RVOT)`
- [ ] Moderate PR: `Moderate Pulmonal Regurgitation (Regurg Jet Width > 1/3 RVOT)`
- [ ] Jika MPA dilatasi: tambahkan `, MPA Dilatation (... cm)`

#### Tricuspid Regurgitation (TR) + PH
- [ ] Ditulis lengkap: **Tricuspid Regurgitation**
- [ ] Mild TR → `Mild Tricuspid Regurgitation (Vmax ... m/s, MaxPG ... mmHg)` — tanpa PH probability
- [ ] Moderate TR → `Moderate Tricuspid Regurgitation (Vmax ... m/s, MaxPG ... mmHg)` + PH Probability
- [ ] Severe TR → `Severe Tricuspid Regurgitation (Vmax ... m/s, MaxPG ... mmHg)` + PH Probability

**PH Probability Rules:**
- [ ] TR Vmax ≤ 2.8 + tanpa RV overload → **Low Probability of PH**
- [ ] TR Vmax ≤ 2.8 + ada RV overload → **Intermediate Probability of PH**
- [ ] TR Vmax 2.8-3.4 + tanpa RV overload → **Intermediate Probability of PH**
- [ ] TR Vmax 2.8-3.4 + ada RV overload → **High Probability of PH**
- [ ] TR Vmax > 3.4 → langsung **High Probability of PH**

*RV overload = D-shaped LV, RV dilatasi, RA dilatasi (area > 18), RVOT AccT < 105 ms*

### K. eRAP
- [ ] IVC < 2.1 + collapse > 50% → eRAP 3 mmHg
- [ ] IVC < 2.1 + collapse < 50% → eRAP 8 mmHg
- [ ] IVC ≥ 2.1 + collapse > 50% → eRAP 8 mmHg
- [ ] IVC ≥ 2.1 + collapse < 50% → eRAP 15 mmHg
- [ ] Format: `eRAP: ... mmHg (.../... cm)`
- [ ] IVC CI = (exp - insp) / exp × 100%

### L. ECHO HEMODINAMIK — KALKULASI
- [ ] MAP = TDD + ⅓(TDS - TDD)
- [ ] LVOT CSA = 0.785 × (LVOT Diam)²
- [ ] LVSV = CSA × LVOT VTI
- [ ] LVCO = LVSV × HR / 1000
- [ ] BSA = √[(BB × TB)/3600] (Mosteller)
- [ ] CI = LVCO / BSA
- [ ] SVR = 80 × (MAP - eRAP) / LVCO
- [ ] PCWP = 1.24 × (E/e' avg) + 1.9 — **hanya jika E/A, E Septal, E Lateral tersedia**
- [ ] CPO = MAP × LVCO / 451
- [ ] CPI = MAP × CI / 451
- [ ] Format tiap parameter: baris sendiri, tanpa pipe, tanpa label tebal
- [ ] Header: `*Echo Hemodinamik:` — tanpa asterisk di output (cukup `Echo Hemodinamik:`)

### N. LUNG US — WAJIB SELALU
- [ ] LUS selalu dicantumkan di baris **paling akhir** setelah Echo Hemodinamik
- [ ] Jika pakboss kosong → `Lung sliding (+), pleural line irregular, A line (+), B line (-), pleural effusion (-)`
- [ ] Jika ada B line → `B line > 3 (+) pada hemithorax bilateral` — sebut jumlah/lokasi
- [ ] Jika ada efusi → `pleural effusion (+) ... cm [lokasi]` — hitung berapa cc
- [ ] Header: `Lung US:` tanpa tanda bintang

### O. URUTAN OUTPUT — FINAL CHECK
- [ ] Baris 1: `Echocardiography Bedside (DD-MM-YYYY):`
- [ ] Jika ada PH → "Pulmonary Hypertension" setelah header (sebagai section)
- [ ] Jika ada trombus → baris sendiri interpretasi tambahan terpisah
- [ ] LV Function → baris sendiri tanpa bullet: `Normal LV Systolic Function, EF ...% (TEICH)`
- [ ] RV Function → baris sendiri tanpa bullet: `Normal RV systolic function, TAPSE ... cm, S' lateral ... cm/s`
- [ ] **Cardiac Valves:** → section header tanpa indentasi
- [ ] Tiap katup → `Mitral: Normal function and movement` — tanpa indentasi, tanpa bullet
- [ ] Baris dimensi (dan geometri jika ada)
- [ ] Baris RWMA (jika ada)
- [ ] Baris eRAP
- [ ] Baris diastolik (jika ada)
- [ ] Baris perikard
- [ ] **Baris kosong**
- [ ] `Echo Hemodinamik:` — tanpa asterisk (disesuaikan dengan format baru)
- [ ] Parameter hemodinamik → tiap baris sendiri tanpa indentasi
- [ ] **Baris kosong**
- [ ] `Lung US:`
- [ ] Deskripsi LUS

---

## CONTOH OUTPUT GOLD STANDARD

```
Echocardiography Bedside (10-06-2026):
Normal LV Systolic Function, EF 62% (TEICH)
Normal RV systolic function, TAPSE 2.8 cm, S' lateral 13 cm/s

Cardiac Valves:
Mitral: Normal function and movement
Aorta: 3 cuspis, calcification (-), Normal function and movement
Pulmonal: Normal function and movement
Tricuspid: Normal function and movement

Normal Cardiac Dimensions (LVIDd 3.9 cm, LA mayor 4.3 cm, LA minor 2.9 cm, RA area 11.3 cm², RVDB 2.6 cm)
Concentric remodeling (LVMI 70.15 g/m², RWT 0.59)
Regional Wall Motion: Global normokinetic
eRAP: 8 mmHg (1.1/0.9 cm)
Grade I LV Diastolic Dysfunction (E/A 0.86, E' Med 11 cm/s, E' Lat 8 cm/s)
No pericardial effusion

Echo Hemodinamik:
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

## ⛔ PITFALLS — JANGAN PERNAH

- [ ] Jangan pipe `|` di output
- [ ] **Jangan kirim laporan echo tanpa code block** — WAJIB dikirim dalam ``` ```
- [ ] **Jangan pakai bullet points / list markdown** untuk konten laporan echo
- [ ] Jangan tulis parameter dulu baru interpretasi — **interpretasi dulu**
- [ ] Jangan tulis "tidak ada" untuk parameter yang tidak disebut — **jangan cantumkan sama sekali**
- [ ] Jangan pisah dimensi dan geometri jadi baris terpisah — jadi **satu baris**
- [ ] Jangan lupa LUS — **WAJIB selalu ada**
- [ ] Jangan lupa tambahkan "3 cuspis, calcification (-)" untuk **Aorta** walaupun normal
- [ ] Jangan tulis "—" atau "..." untuk yang tidak disebut
- [ ] Setiap ada koreksi → **CENTANG ULANG SEMUA CHECKLIST**
