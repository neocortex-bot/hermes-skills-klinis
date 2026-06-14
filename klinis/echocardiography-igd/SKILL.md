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
- **Parameter wajib yang tidak diisi → tulis `...`** — contoh: `Mild Tricuspid Regurgitation (Vmax ... m/s, MaxPG ... mmHg)` — nanti diisi manual
- **JANGAN pakai pipe `|`** di output laporan.
- **Interpretasi sendiri** — jangan copas mentah dari data pakboss. Contoh: LVIDd 3.9 cm itu normal → tulis "Normal Cardiac Dimensions". LA 4.3 cm itu dilatasi → tulis "LA dilatation". Dll.
- **Yang tidak perlu diisi pakboss** (kalkulasi otomatis dari app hemodinamik atau dari TTV):
  - MAP, LV SV, LV CO, eRAP, SVR, BSA, CI, CPO, CPI, Collapsibility Index, Distensibility Index
  - PCWP (kalkulasi otomatis jika E/A, E Septal, dan E Lateral tersedia — rumus Nagueh)
  - TDS, TDD, HR, Suhu — dari monitor TTV
  - Lung US (A-line, B-line, efusi pleura) — dari app
  - Urine output, fluid balance — dari catatan
- **Yang pakboss isi** — form isian di bawah ini saja.

---

## Form Isian Echo (Yang Perlu Diisi Pakboss)

Kirim nomor dan nilainya saja.

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

**Aturan Katup:**
- Jika pakboss tulis "N" (Normal) atau tidak disebut masalah — tulis **"Normal function and movement"** untuk Mitral, Aorta, Pulmonal, Tricuspid.
- **Semua katup harus disebutkan** — tidak disebut artinya normal, tetap tulis "Normal function and movement".
- Untuk **Aorta** — selalu tulis **"3 cuspis, calcification (-), Normal function and movement"** kecuali pakboss sebut ada abnormality (stenosis/regurg/kalsifikasi).
- Jika pakboss sebut ada abnormality (Mild MR, Moderate AS, dll) — tulis sesuai yang pakboss sebutkan, jangan "Normal function and movement".
- **Jangan tulis "Normal function and movement" bila ada masalah katup meskipun Mild/ringan** — tulis grade abnormality-nya.

**Aturan Pelebaran Katup (WAJIB):**
Saat pakboss menyebut grade katup (Mild/Moderate/Severe MR/AR/PR/TR), jabarkan dengan parameter berikut. Jangan tulis cuma "Mild PR" saja — harus diperluas dengan template di bawah:

| Katup | Jika pakboss sebut | Format output yang dijabarkan |
|-------|-------------------|-------------------------------|
| Tricuspid | Mild/Moderate/Severe TR | `Mild/Moderate/Severe Tricuspid Regurgitation (Vmax ... m/s, MaxPG ... mmHg)` + PH Probability (kecuali Mild) |
| Pulmonal | Mild/Moderate PR | `Mild Pulmonal Regurgitation (PR Regurgitant Jet < 1/3 RVOT)` — untuk Mild. `Moderate Pulmonal Regurgitation (Regurg Jet Width > 1/3 RVOT)` — untuk Moderate. Jika ada MPA dilatasi, tambahkan koma lalu `MPA Dilatation (... cm)`. |
| Mitral | MR | `[Grade] Mitral Regurgitation (ERO ... cm², RV ... ml, VC ... cm)` — jika ERO/RV/VC tidak disebut, tulis sesuai grade saja. Jabarkan Carpentier, arah jet, primary/secondary. More than Moderate/Severe: `Moderate Mitral Regurgitation due to ...` |
| Aorta | AR | `[Grade] Aortic Regurgitation (PHT ... ms, ERO ... cm², RV ... ml, VC ... cm, Holodiastolic Reversal Flow Peak Vel ... cm/s)` — More than Moderate/Severe: `Moderate Aortic Regurgitation due to ...` |
| Mitral | MS | `[Grade] Mitral Stenosis due to ... (MVA planimetry ... cm², MVA PHT ... cm², Mean PG ... mmHg, Wilkins Score ...)` — Wilkins disebutkan (cth 2-2-2-1) |
| Aorta | AS | `[Grade] Aortic Stenosis due to ... (AV Vmax ... m/s, mean PG ... mmHg, AVA continuity eq ... cm², AVA Planimetri ... cm²)` — parameter exact bukan rentang |

**Pengecualian:** Jika pakboss hanya kirim grade tanpa angka parameter, tulis grade + jelaskan dari parameter yang ada saja.

**Aturan TR + PH Probability:**
- TR Mild → `Mild Tricuspid Regurgitation (Vmax ... m/s, MaxPG ... mmHg)` — tanpa PH probability
- TR Moderate → `Moderate Tricuspid Regurgitation (Vmax ... m/s, MaxPG ... mmHg)` + PH Probability
- TR Severe → `Severe Tricuspid Regurgitation (Vmax ... m/s, MaxPG ... mmHg)` + PH Probability
- PH Probability:
  - TR Vmax ≤ 2.8 + tanda RV overload lain (D-shaped LV, RV dilatasi, RA dilatasi, RVOT AccT < 105ms) → "Intermediate Probability of PH"
  - TR Vmax > 2.8 → lihat tanda RV overload: jika ada tanda RV overload → "High Probability of PH"; jika tanpa tanda → "Intermediate Probability of PH"
  - TR Vmax > 3.4 → langsung "High Probability of PH"

**Aturan TAPSE:**
- TAPSE ≥ 1.7 cm → "Normal RV systolic function"
- TAPSE < 1.7 cm → "Decreased RV Systolic function"

---

## Interpretasi Parameter Echo

### Dimensi Jantung (interpretasi otomatis) — WAJIB DIBACA TANPA TERKECUALI
- LVIDd normal: 3.5-5.4 cm → jika dalam rentang tulis di parameter tanpa label dilatasi.
- **LA mayor** normal: **< 6.1 cm** (bukan 4.5!) → jika ≥ 6.1 tulis "LA dilatation". Jika < 6.1 → **BUKAN dilatasi**.
- **LA minor** normal: **< 4.5 cm** → jika ≥ 4.5 tulis "LA dilatation".
- **WAJIB:** LA mayor dan LA minor HARUS selalu ditulis di parameter, meskipun normal. Format: `LA mayor ... cm, LA minor ... cm`
- RA area normal: < 18 cm² → jika ≥ 18 tulis "RA dilatation".
- RVDB normal: < 4.2 cm → jika ≥ 4.2 tulis "RV dilatation".
- Jika semua dimensi dalam batas normal: **"Normal Cardiac Dimensions"** — tanpa parameter dalam kurung.

### LV Geometry
- **Tidak tulis "LV Geometry:"** — bila semua normal tulis saja `Normal Cardiac Dimensions`
- RWT > 0.42 + LVMI normal → "Concentric remodeling"
- RWT ≤ 0.42 + LVMI ↑ → "Eccentric LVH"
- RWT > 0.42 + LVMI ↑ → "Concentric LVH"
- RWT normal + LVMI normal → skip baris

### LV Diastolic Function — dengan Grade
- Grade I: "Grade I LV Diastolic Dysfunction:" lalu E/A, E' Med, E' Lat
- Grade II/III: sesuai

### eRAP
- "eRAP: ... mmHg (IVC exp/IVC insp)"
- Interpretasi: IVC < 2.1 cm + collapse > 50% → eRAP 3 mmHg (normal); < 2.1 + < 50% → 8 mmHg; ≥ 2.1 + > 50% → 8 mmHg; ≥ 2.1 + < 50% → 15 mmHg

---

## Template Output Echo Bedside — FORMAT PASTI

**Aturan struktur output (WAJIB):**
1. **Pulmonary Hypertension** — section header jika ada PH (TR Severe + PASP ↑ atau tanda RV overload)
2. **Trombus/temuan lain** — baris sendiri interpretasi tambahan terpisah
3. **LV & RV function** — baris sendiri tanpa bullet: `Normal LV Systolic Function, EF ...% (TEICH)`
4. **Cardiac Valves** — section tanpa indentasi, tiap katup baris sendiri tanpa bullet
5. **Dimensi + Geometri jadi SATU baris** — tulis `RA dilatation, RV dilatation with LV-D shaped (RA area ... cm², RVDB ... cm, LA mayor ... cm, LA minor ... cm, LVMI ... g/m², RWT ...)` — jangan pisah dimensi dan geometri. Bila semua normal tulis `Normal Cardiac Dimensions` saja tanpa parameter kurung. **WAJIB:** LA mayor dan LA minor selalu ditulis di parameter terlepas normal atau tidak. Jika LA minor tidak disebut pakboss, tulis `LA minor ... cm`
6. **Pericardial effusion** — `No pericardial effusion` atau format efusi lengkap (PLAX/PSAX/Apical/Subcostal + tamponade signs)

**Template output:**
```
Echocardiography Bedside (tanggal):

Pulmonary Hypertension

Trombus seen at [lokasi] (ukuran)

Normal LV Systolic Function, EF ...% (TEICH)

Normal RV systolic function, TAPSE ... cm, S' lateral ... cm/s

Cardiac Valves:
Mitral: Normal function and movement
Aorta: 3 cuspis, calcification (-), Normal function and movement
Pulmonal: ...
Tricuspid: ...

RA dilatation, RV dilatation with LV-D shaped (RA area ... cm², RVDB ... cm, LA mayor ... cm, LA minor ... cm, LVMI ... g/m², RWT ...)

No pericardial effusion
```

### LUS (Lung Ultrasound) — WAJIB selalu dicantumkan

**Prinsip:** LUS selalu ada di laporan echo, **di bawah Echo Hemodinamik** (bukan di antara Bedside dan Hemodinamik).
- Jika pakboss **tidak menyebut** B line / efusi pleura → artinya normal: A line (+), B line (-), pleural effusion (-)
- Jika pakboss sebut "efusi 2 cm", "B line +" dll → tulis sesuai
- Lung sliding biasanya (+), pleural line irregular jika ada inflamasi

**Format selalu:**
```
Lung US:
Lung sliding (+), pleural line irregular, A line (+), B line (-), pleural effusion (-)
```
Sesuaikan jika pakboss sebut temuan.

### Echo Hemodinamik — Format output
```
Echo Hemodinamik:
TD .../... mmHg
MAP ... mmHg
HR ... bpm
LVOT Diam ... cm
LVOT VTI ... cm
LVSV ... ml
LVCO ... L/min
eRAP ... mmHg
PCWP ... mmHg (E/e' avg ...)  — hanya jika E/A (E wave), E Septal, E Lateral tersedia
SVR ... dynes/sec/cm⁻⁵
BSA ... m²
CI ... L/min/m²
CPO ... watt
CPI ... watt/m²
```

**PENTING — Format interpretasi:** tulis kelainan/kondisi DULU, lalu parameter dalam kurung. Contoh:
- "Concentric remodeling (LVMI 70.15 g/m², RWT 0.59)" — bukan "LV Geometry: Concentric remodeling\n(LVMI..."
- "Grade I LV Diastolic Dysfunction (E/A 0.86, E' Med 11 cm/s, E' Lat 8 cm/s)" — bukan pakai titik dua baris baru
- "Normal Cardiac Dimensions (LVIDd 3.9 cm, LA mayor 4.3 cm, ...)"

**Aturan format:**
- Baris kosong antara blok Echo Bedside dan blok Echo Hemodinamik
- Kalimat terpadu (jangan bullet untuk interpretasi dimensi, geometri, RWMA, eRAP, diastolik, perikard)
- Di Echo Hemodinamik: tiap parameter baris sendiri, tanpa pipe, tanpa label tebal.
- TAPSE satuannya **cm** (bukan cm/s)
- **Header Echo Bedside dan Echo Hemodinamik tanpa asterisk/bold markdown**

---

## Contoh Output

**Data dari Tn. Nofri (10-06-2026):**
1. Norm | 62%
2. Norm | 2.8 | 13
3. N | N | N | N
4. 3.9 | 4.3/2.9 | RA area 11.3 | 2.6
5. concentric remodeling | 70.15 | 0.59
6. No
7. 0.86 | 11 | 8 | — | I
8. N
9. —
TDS 145 | TDD 90 | HR 92 | LVOT Diam 1.9 | LVOT VTI 16.9
IVC exp 1.1 | IVC insp 0.9 | BB 79 | TB 160

**Output:**
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

## ⛔ GOLD STANDARD CHECKLIST

**Sebelum mengirim laporan echo, buka dan centang:**
```
skill_view(name='echocardiography-igd', file_path='references/gold-standard-checklist.md')
```
Centang semua item A-O satu per satu. Setiap ada koreksi → centang ulang semua.

## Cara Pakai Kalkulator Echo

Script di `scripts/echo-calculator.py`. Tinggal isi parameternya.

Atau pakboss kirim form isian 9 nomor ke saya, saya yang proses.
