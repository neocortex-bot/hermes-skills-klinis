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
- **JANGAN pakai pipe `|`** di output laporan.
- **Interpretasi sendiri** — jangan copas mentah dari data pakboss. Contoh: LVIDd 3.9 cm itu normal → tulis "Normal Cardiac Dimensions". LA 4.3 cm itu dilatasi → tulis "LA dilatation". Dll.
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
4. LVIDd _ | LA _ / _ | RA area _ | RVDB _ | LA/Ao ___
5. LVH: _ | LVMI _ | RWT ___
6. RWMA: ___
7. E/A _ | E' Med _ | E' Lat _ | E/E' _ | Grade ___
8. Perikard: ___
9. Lain: ___

TDS _ | TDD _ | HR _ | LVOT Diam _ | LVOT VTI ___
IVC exp _ | IVC insp _ | BB _ | TB _

LUS (isi jika ada temuan, kosongkan jika normal):
B line: _ | lokasi: _
Pleural effusion: _ cm | lokasi: _

Masalah katup (jabarkan di sini):
- Mitral:
_ | MR ERO _ cm² | MR RV _ ml | MR VC _ cm | Regurg Jet Length > _% LA | Carpentier _ | Annulus mitral _ cm |
MVA planimetry _ cm² | MVA PHT _ cm² | MS Mean PG _ mmHg | Mean PHT _ ms | Wilkins Score _

- Aorta:
_ | AR PHT _ ms | AR ERO _ cm² | AR RV _ ml | AR VC _ cm | Regurg Jet Length > _% LVOT | Holodiastolic Reversal Flow Peak Vel _ cm/s | Aortic annulus _ cm | Sinus valsava _ cm | ST junction _ cm | Ascenden _ cm |
AVA planimetry _ cm² | AV Vmax _ m/s | AV mean PG _ mmHg | AV continuity eq _ cm² | SVI _ ml/m² | AV VTI _ cm

- Pulmonal:
_ | PR PHT _ ms | Regurg Jet Width > _/_ RVOT | PV AccT _ ms | PASP _ mmHg | mPAP _ mmHg

- Tricuspid:
_ | TR Jet [Central/Excentric] | Regurg Jet Area > _% RA | TR Vmax _ m/s | TR maxPG _ mmHg | TR VC _ cm | Systolic Reversal Flow Hepatic Vein [Ya/Tidak] | PH Probability [Low/Intermediate/High]
```

**Aturan Katup:**
- Jika pakboss tulis "N" (Normal) atau tidak disebut masalah — tulis **"Normal function and movement"** untuk Mitral, Pulmonal, Tricuspid.
- Untuk **Aorta** — selalu tulis **"3 cuspis, calcification (-), Normal function and movement"** kecuali pakboss sebut ada abnormality (stenosis/regurg/kalsifikasi).
- Jika pakboss sebut ada abnormality (Mild MR, Moderate AS, dll) — tulis sesuai yang pakboss sebutkan, jangan "Normal function and movement".
- Jika katup tidak disebut sama sekali, jangan sematkan baris katup itu.

---

## Interpretasi Parameter Echo

### Dimensi Jantung (interpretasi otomatis)
- LVIDd normal: 3.5-5.7 cm (wanita), 3.9-5.3 cm (pria) → tulis "Normal Cardiac Dimensions" jika dalam rentang.
- LA mayor normal: < 4.0 cm → jika ≥ 4.0 tulis "LA dilatation".
- RA area normal: < 18 cm² → jika ≥ 18 tulis "RA dilatation".
- RVDB normal: < 4.2 cm → jika ≥ 4.2 tulis "RV dilatation".
- Jika semua dimensi dalam batas normal: **"Normal Cardiac Dimensions (parameter...)"**

### LV Geometry
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

```
*Echocardiography Bedside (tanggal):*
- [temuan LV Function], EF ...% (TEICH)
- [temuan RV Function], TAPSE ... cm, S' lateral ... cm/s
Cardiac Valves:
- Mitral: Normal function and movement
- Aorta: 3 cuspis, calcification (-), Normal function and movement
- Pulmonal: Normal function and movement
- Tricuspid: Normal function and movement
[Interpretasi Dimensi] (LVIDd ... cm, LA mayor ... cm, LA minor ... cm, RA area ... cm², RVDB ... cm)
LV Geometry: [kelainan] (LVMI ... g/m², RWT ...)
Regional Wall Motion: [Global normokinetic / ...]
eRAP: ... mmHg (exp/insp)
[Grade] LV Diastolic Dysfunction (E/A ..., E' Med ... cm/s, E' Lat ... cm/s)
[Pericardial effusion / No pericardial effusion]

## LUS (Lung Ultrasound) — WAJIB selalu dicantumkan

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

**PENTING — Format interpretasi:** tulis kelainan/kondisi DULU, lalu parameter dalam kurung. Contoh:
- "Concentric remodeling (LVMI 70.15 g/m², RWT 0.59)" — bukan "LV Geometry: Concentric remodeling\n(LVMI..."
- "Grade I LV Diastolic Dysfunction (E/A 0.86, E' Med 11 cm/s, E' Lat 8 cm/s)" — bukan pakai titik dua baris baru
- "Normal Cardiac Dimensions (LVIDd 3.9 cm, LA mayor 4.3 cm, ...)"

*Echo Hemodinamik:*
TD .../... mmHg
MAP ... mmHg
HR ... bpm
LVOT Diam ... cm
LVOT VTI ... cm
LVSV ... ml
LVCO ... L/min
eRAP ... mmHg
SVR ... dynes/sec/cm⁻⁵
BSA ... m²
CI ... L/min/m²
CPO ... watt
CPI ... watt/m²

Lung US:
Lung sliding (+), pleural line irregular, A line (+), B line (-), pleural effusion (-)
```

**Aturan format:**
- Baris kosong antara blok Echo Bedside dan blok Echo Hemodinamik
- Kalimat terpadu (jangan bullet untuk interpretasi dimensi, geometri, RWMA, eRAP, diastolik, perikard)
- Di Echo Hemodinamik: tiap parameter baris sendiri, tanpa pipe, tanpa label tebal.
- TAPSE satuannya **cm** (bukan cm/s)

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
*Echocardiography Bedside (10-06-2026):*
- Normal LV Systolic Function, EF 62% (TEICH)
- Normal RV systolic function, TAPSE 2.8 cm, S' lateral 13 cm/s
Cardiac Valves:
- Mitral: Normal function and movement
- Aorta: 3 cuspis, calcification (-), Normal function and movement
- Pulmonal: Normal function and movement
- Tricuspid: Normal function and movement
Normal Cardiac Dimensions (LVIDd 3.9 cm, LA mayor 4.3 cm, LA minor 2.9 cm, RA area 11.3 cm², RVDB 2.6 cm)
LV Geometry: Concentric remodeling (LVMI 70.15 g/m², RWT 0.59)
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
SVR 1821 dynes/sec/cm⁻⁵
BSA 1.87 m²
CI 2.35 L/min/m²
CPO 1.06 watt
CPI 0.57 watt/m²

Lung US:
Lung sliding (+), pleural line irregular, A line (+), B line (-), pleural effusion (-)
```

---

## Cara Pakai Kalkulator Echo

Script di `scripts/echo-calculator.py`. Tinggal isi parameternya.

Atau pakboss kirim form isian 9 nomor ke saya, saya yang proses.
