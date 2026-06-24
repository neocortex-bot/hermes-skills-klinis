---
name: abcde-intensive-care
category: clinical
description: Konversi SOAP konvensional (IGD/rawat) ke format ABCDE-Intensive-Care untuk follow up harian di ICU/CVCU. Dipanggil setiap hari untuk transformasi data SOAP biasa ke struktur Airway-Breathing-Circulation-Disability-Exposure + Fluid-Glucose-Infection + TS konsulen.
tags: [abcde, icu, cvcu, konversi, followup, harian, cardiology]
trigger:
  - user meminta "konversi ke ABCDE" atau "ubah ke format ABCDE"
  - user memberikan SOAP konvensional dan meminta dibuatkan follow up CVCU/ICU
  - user berkata "buatkan follow up CVCU seperti biasa"
  - user memberikan data pasien rawat + data klinis untuk dijadikan format ABCDE
  - "konversi dari SOAP konvensional ke SOAP ABCDE"
  - user memberikan data mentalah (TTV, lab, hasil echo) untuk dijadikan laporan harian
---

# ABCDE-Intensive-Care — Konversi SOAP Konvensional → ABCDE

## Tujuan

Skill ini mengkonversi **SOAP konvensional** (format IGD/rawat biasa — S/O/A/P) menjadi **format ABCDE-Intensive-Care** untuk follow up harian di ICU/CVCU.

**Sumber data:** SOAP konvensional (dari skill `soap-igd-jantung` atau input manual user)
**Target:** Format ABCDE-FGI (Airway, Breathing, Circulation, Disability, Exposure, Fluid, Glucose & Gut, Infection) + TS konsulen

---

## 1. POLA TRANSFORMASI

### Header (Pembuka)

| SOAP Konvensional | ABCDE Output |
|---|---|
| Hanya "DPJP Utama" dan "DPJP Tindakan" | Tambah DPJP Pulmonologi, EMD, GH, GEH, Rehab Medik bila user beri atau kosongkan |
| Format pasien baru | Format follow up: "mohon izin melaporkan **follow up** pasien di *CVCU bed N*" |
| Diagnosis di Assessment saja | Diagnosis List di header + diulang di Assessment |

### Subjektif → S:
- Dari S: SOAP konvensional → S: di ABCDE (singkat, fokus post-prosedur, demam, perdarahan)
- Keluhan utama baru → S: (onset, karakter)
- "Tidak ada keluhan" → tulis "tidak ada keluhan baru"

### Objektif → Transformasi ke ABCDE

| SOAP Konvensional | ABCDE Output |
|---|---|
| TTV lepas per baris | **Circulation:** TD, MAP, nadi — ditambah echo hemodinamik (LV VTI, LVSV, LVCO, SVR, eRAP, CI, CPO, CPI, SVV) — pakai data echo bila ada |
| — | **Breathing:** RR, SpO2, auskultasi ditambah setting ventilator bila intubasi + LUS |
| — | **Airway:** Patent/ETT — hanya jika pasien intubasi |
| — | **Disability:** GCS, sedasi |
| Suhu, lab, AGD, foto thorax | **Exposure:** Suhu, elektrolit, AGD, laktat, foto thorax |

### Pemeriksaan Fisis
- Thorax: vesikuler/ronkhi/wheezing → masuk **Breathing**
- Jantung: BJ/murmur → masuk **Circulation**
- Abdomen → masuk **Glucose & Gut** (rectal toucher)
- Ekstremitas/edema → masuk **Circulation** atau **Exposure**
- JVP → masuk **Circulation**

### EKG
- Dari SOAP: EKG paragraph → tetap di **Exposure** setelah AGD
- Atau dibuat section terpisah *(EKG ...)* jika serial

### Lab
- Dari SOAP: Hematologi + Kimia → **Hypo/Hyperthermia and Haematology** (WBC, HB, N/L, Ur/Cr, eGFR, SGOT/SGPT, Albumin)
- CRP, PCT → **Infection**
- GDS, HbA1C → **Glucose & Gut**
- Urinalisis → **Infection**

### Fluid (Balance Cairan)
- **TIDAK ada** di SOAP konvensional → WAJIB hitung:
  - Keb. Cairan = 30 ml/kg × BB
  - Intake total (infus + oral + obat)
  - Output total (urine + IWL jika dihitung)
  - BC = Intake − Output
  - UO dalam cc/kg/jam
- Jika user tidak memberi data lengkap: tulis "Data balance cairan: [yang diketahui]" dan kosongkan sisanya

### Glucose & Gut
- Dari data GDS/GDP/HbA1C + data enteral/nutrisi
- Jika tidak ada data: tulis "Data nutrisi menyusul"

### TS Konsulen
- **TIDAK ada** di SOAP konvensional → output dikosongkan dengan header saja
- Jika user menyebut TS: tulis Assessment + Terapi sesuai format TS

---

## 2. FORMAT OUTPUT LENGKAP

```
Assalamualaikum dokter. Tabe dokter, mohon izin melaporkan follow up pasien di *[CVCU bed N]* atas nama:

*[Tn./Ny.] [Nama] / [DD-MM-YYYY] / [Umur] tahun / [RM]*

_[DPJP Utama : dr. ..., Sp. ...]_
_[DPJP Tindakan : Dr. dr. ..., Sp. ...]_
_[DPJP Pulmonologi : Dr. dr. ..., Sp.P(K), Sp.PD-KP]_
_[DPJP EMD : Prof. Dr. dr. ..., Sp.PD, KEMD (K)]_
_[DPJP GH : Dr. dr. ..., Sp.PD, KGH]_

*Perawatan CVCU H-[N]*

*Diagnosis*
- [Diagnosis 1]
- [Diagnosis 2]

S :
[Subjektif singkat — post tindakan, demam, perdarahan, keluhan baru]

O :
Airway : Patent dengan ETT ukuran [N], kedalaman [N]cm, mucus (-) Pluq (-) [— atau "Patent, self breathing" bila sadar]

Breathing : On Ventilator Mode [Mode] FiO2 [N]%, RR [N]x/menit, PEEP [N], VT [N]ml, Ps [N], menghasilkan PIP [N] mbar, VT [N] ml, RR [N] kali/menit, MV [N] L/min, Bunyi pernapasan Vesikuler +/+, Rh +/+, Wh -/-, SpO2 [N]%, LUS : Lung sliding (+), regular pleural line, A lines (-), B lines (+) [deskripsi]

[— atau bila spontaneous: Bunyi pernapasan Vesikuler +/+, Rh -/-, Wh -/-, SpO2 [N]% [NC ... lpm / room air]]

Circulation : Tekanan darah [N]/[N] mmHg (MAP [N]), nadi [N] x/menit [reguler/ireguler], didapatkan LV VTI [N] cm, LVSV [N] ml, LVCO [N] L/min, SVR [N] dynes/sec.cm-5, eRAP [N], CI [N], CPO [N], CPI [N], SVV [N]% [— atau tanpa echo: BJ I/II murni reguler, murmur -/-, CRT < 2 detik, akral hangat]

Disability : GCS E[N]M[N]Vx tersedasi dengan [obat] [dosis] [— atau GCS E4M6V5 compos mentis bila sadar]

Exposure : Suhu [N]°C, Elektrolit (DD-MM-YYYY) [hasil], AGD (DD-MM-YYYY) : pH [N], PO2 [N], pCO2 [N], HCO3 [N], laktat [N], BE [N]; Foto thorax (DD-MM-YYYY) : [kesan]

Fluid :
Keb. Cairan (30 ml/kg) [N] ml/24 jam
Intake [N]cc
Output [N] cc
BC [+/-][N] cc
UO : [N]cc/[N]kg/[N]jam = [N] cc/kg/jam

Glucose & Gut :
Enteral : - [Makanan] [kkal] ([frekuensi] x [porsi])
- [ONS/Supplement] [kkal] ([frekuensi])
Total kebutuhan kalori = [N] kkal
GDP [N]
HbA1C [N]
Plan :
- Cek GDS/6 jam
- GDS target [range]
- GDP target [range]
Rectal Toucher : mucosa [deskripsi], sphicter [deskripsi], massa (-), darah (-), feses (-)

Hypo/Hyperthermia and Haematology
T [N]
*Laboratorium PJT (DD-MM-YYYY)*
*WBC : [N]*; *HB : [N]* N/L [N]/[N]; Ur/Cr : *[N]/[N]* *eGFR [N]*
SGOT/SGPT : *[N]/[N]*; Albumin *[N]*
Plan:
[Antibiotik regimen bila ada]

Infection
*Laboratorium PJT (DD-MM-YYYY)*
CRP [N] -> [N]
*Prokalsitonin [N] -> [N] -> [N]*
*Urinalisis (DD-MM-YYYY)*
Kesan : [temuan]
*Biakan sputum ETT evaluasi (DD-MM-YYYY):* [hasil]
*Kultur spesimen darah:* [hasil]
*Smear gram sputum:* [hasil]

*Mohon izin kami assess dengan*
- [Diagnosis lengkap]

Mohon izin kami terapi dengan
- IVFD [cairan] [dosis]/[frekuensi]/[rute]
- [Obat] [dosis]/[frekuensi]/[rute]

Plan:
- Monitoring tanda vital dan hemodinamik
- Monitoring urine output dan balance cairan
- [Plan lain — dari Plan SOAP konvensional]

*TS Pulmonologi*
Assessment :
- [Diagnosis]

Terapi :
- [Antibiotik] [dosis]/[frekuensi]/[rute]

*TS EMD*
Assessment :
- [Diagnosis]

Terapi :
- [Insulin regimen]

*TS GH*
Assessment :
- [Diagnosis]

Terapi :
- [Terapi]

*TS GEH*
Assessment :
- [Diagnosis]

Terapi :
- [Obat]

*TS Rehab Medik*
A/ :
[Diagnosis immobilisasi]

I/ :
- FT di Tempat
- [Latihan progresif]

Selanjutnya mohon arahan dokter. Terima kasih Dokter.
```

---

## 3. ATURAN TRANSFORMASI KRITIS

### 3.1 Yang TIDAK Berubah dari SOAP Konvensional
- **Diagnosis** — tetap sama, hanya diformat ulang di header + Assessment
- **Obat/terapi** — semua obat tetap di "Mohon izin kami terapi dengan..."
- **Plan** — dari Plan SOAP konvensional jadi Plan di ABCDE

### 3.2 Yang BERUBAH dari SOAP Konvensional
- **TTV → Circulation + Breathing** — TD, Nadi → Circulation; RR, SpO2 → Breathing
- **EKG → Exposure** — setelah AGD
- **Fisis thorax/jantung** → Breathing / Circulation
- **Abdomen** → Glucose & Gut (rectal toucher)
- **Lab hematologi** → Hypo/Hyperthermia
- **CRP/PCT/urinalisis/kultur** → Infection
- **GDS/GDP/HbA1C** → Glucose & Gut

### 3.3 Default (Jika Data Tidak Tersedia)
- **Airway:** "Patent, self breathing" (bila sadar) atau "Patent dengan ETT..." (bila intubasi)
- **Breathing:** On Ventilator — hanya jika user beri data ventilator. Default: "Bunyi pernapasan Vesikuler +/+, Rh -/-, Wh -/-, SpO2 [N]%"
- **Circulation:** echo hemodinamik — hanya jika user beri data echo. Default: "BJ I/II murni reguler, murmur tidak ada, CRT < 2 detik, akral hangat"
- **Disability:** Default compos mentis bila sadar
- **LUS:** Kosongkan — "LUS: —" jika tidak ada data
- **Fluid:** Hitung dari BB. Kosongkan intake/output bila tidak ada data
- **Glucose & Gut:** Kosongkan enteral bila tidak ada data. Tulis "Data nutrisi menyusul" jika user belum beri
- **TS konsulen:** Tulis header saja tanpa konten — "Data TS menyusul"
- **Rectal Toucher:** Kosongkan — hanya isi bila user beri data

### 3.4 Penanganan Pasien Sadar (Non-Intubasi / Non-Ventilator)
Gunakan baris-baris alternatif berikut:

```
Airway : Patent, self breathing
Breathing : Bunyi pernapasan Vesikuler +/+, Rh -/-, Wh -/-, SpO2 [N]% [room air / on NC ... lpm]
Disability : GCS E4M6V5, compos mentis
```

### 3.5 Echo Hemodinamik — Hanya jika ada data echo
```
Circulation : Tekanan darah [N]/[N] mmHg (MAP [N]), nadi [N] x/menit [reguler], [tanpa echo: BJ I/II murni, CRT < 2dtk, akral hangat]
```

Jika user beri data echo hemodinamik (LV VTI, LVSV, LVCO, dll), masukkan semua parameter di Circulation.

---

## 4. CONTOH KONVERSI

### Input (SOAP Konvensional):
```
Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *CVCU bed 6* atas nama:

*Tn. Ibrahim / 05-04-1971 / 55 tahun / 1650197*

_DPJP Utama: dr. Andi Renata Bastario, Sp.JP (K)_
_DPJP Tindakan: Dr. dr. Az Hafid Nashar, Sp.JP (K)_

*S:*
Post primary PCI hari ini. Keluhan nyeri dada sudah hilang. Demam tidak ada.

*O:*
Tekanan Darah: 110/70 mmHg
Nadi: 85 kali/menit reguler
Pernapasan: 20 kali/menit
Suhu: 36.7°C
Saturasi: 98% room air

Thorax: BP vesikuler, ronkhi tidak ada, wheezing tidak ada
Jantung: BJ I/II murni reguler, murmur tidak ada

*Mohon izin kami assess dengan:*
- STEMI Anterior

*Mohon izin kami terapi dengan:*
- IVFD NaCl 0.9% 500 cc/24 jam/IV
- Aspilet 80 mg/24 jam/oral
- Ticagrelor 90 mg/12 jam/oral

*Plan:*
- Monitoring tanda vital dan hemodinamik
- Rawat CVCU
```

### Output (ABCDE):
```
Assalamualaikum dokter. Tabe dokter, mohon izin melaporkan follow up pasien di *CVCU bed 6* atas nama:

*Tn. Ibrahim / 05-04-1971 / 55 tahun / 1650197*

_[DPJP Utama : dr. Andi Renata Bastario, Sp.JP (K)]_
_[DPJP Tindakan : Dr. dr. Az Hafid Nashar, Sp.JP (K)]_

*Perawatan CVCU H-1*

*Diagnosis*
- STEMI Anterior

S :
Post primary PCI hari ini, nyeri dada hilang, demam tidak ada

O :
Airway : Patent, self breathing

Breathing : Bunyi pernapasan Vesikuler +/+, Rh -/-, Wh -/-, SpO2 98% room air

Circulation : Tekanan darah 110/70 mmHg (MAP 83), nadi 85 x/menit reguler, BJ I/II murni reguler, murmur tidak ada, CRT < 2 detik, akral hangat

Disability : GCS E4M6V5, compos mentis

Exposure : Suhu 36.7°C, AGD dan elektrolit: —

Fluid :
Keb. Cairan (30 ml/kg) [N] ml/24 jam
Intake [N] cc
Output [N] cc
BC [N] cc
UO : [N] cc/kg/jam

Glucose & Gut :
Data nutrisi menyusul

Hypo/Hyperthermia and Haematology
T 36.7°C
*Laboratorium PJT :*
*WBC : —*; *HB : —* N/L —/—; Ur/Cr : *—/—* *eGFR —*

Infection
CRP —, PCT —

*Mohon izin kami assess dengan*
- STEMI Anterior

Mohon izin kami terapi dengan
- IVFD NaCl 0.9% 500 cc/24 jam/IV
- Aspilet 80 mg/24 jam/oral
- Ticagrelor 90 mg/12 jam/oral

Plan:
- Monitoring tanda vital dan hemodinamik
- Rawat CVCU

*TS Pulmonologi*
Assessment :
—
Terapi :
—

*TS EMD*
Assessment :
—
Terapi :
—

*TS GH*
Assessment :
—
Terapi :
—

Selanjutnya mohon arahan dokter. Terima kasih Dokter.
```

---

## 5. PITFALLS

1. ❌ **Lupa mengganti "pasien baru" → "follow up"** — SOAP konvensional pakai "melaporkan pasien baru", ABCDE pakai "melaporkan follow up pasien"
2. ❌ **S: tetap bold** — Di ABCDE, **S: dan O: TIDAK bold** (beda dari SOAP IGD)
3. ❌ **TTV masih per baris** — TTV harus sudah dipisah ke Circulation (TD, nadi) dan Breathing (RR, SpO2)
4. ❌ **Fisis thorax/jantung tidak dipisah** — thorax → Breathing, jantung → Circulation
5. ❌ **Tidak menambah DPJP konsulen** — CVCU biasanya punya Pulmo, EMD, GH, GEH, Rehab
6. ❌ **Lupa Fluid section** — balance cairan WAJIB ada di laporan ICU/CVCU
7. ❌ **Echo hemodinamik tidak diisi** — jika user beri data echo, WAJIB semua parameter (LV VTI, LVSV, dll)
8. ❌ **TS konsulen dikosongkan total** — tulis header TS dengan isi "—" agar user bisa isi
9. ❌ **Data fiktif** — JANGAN isi data lab/nutrisi/AGD yang tidak user berikan. Tanda "—" atau "menyusul" lebih baik
10. ❌ **Lupa hitung MAP** — MAP = (2×diastol + sistol)/3, hitung selalu
11. ❌ **Lupa menambahkan LUS** — LUS adalah bagian standar Breathing di CVCU. Tulis "LUS : —" jika tidak ada data
