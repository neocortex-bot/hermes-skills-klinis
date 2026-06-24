---
name: cvcu-followup-jantung
category: clinical
description: Format laporan follow up pasien di CVCU (Cardiovascular Care Unit) untuk pelaporan harian multispesialis dengan TS (Tim Spesialis) konsulen. Berbeda dari SOAP IGD — mencakup S/O/Fluid/Glucose/Infection, echo hemodinamik serial, dan TS konsultan.
tags: [cvcu, icu, followup, cardiology, multispecialty]
trigger:
  - user meminta buat follow up pasien CVCU
  - user memberikan data pasien rawat ICU/CVCU
  - user meminta format seperti pasien sebelumnya
  - user memberikan data bed-side echo CVCU + data klinis lengkap
---

# CVCU Follow-Up Report — Format Laporan Harian

Format laporan **follow up pasien di CVCU** untuk pelaporan harian. Berbeda dengan SOAP IGD yang sekali-admit, laporan CVCU bersifat **kumulatif harian** dengan data monitor ketat.

## 1. PEMBUKA

**Format:**
```
Assalamualaikum dokter. Tabe dokter, mohon izin melaporkan follow up pasien di *[Lokasi/Ruangan]* atas nama:

*[Tn./Ny.] [Nama] / [DD-MM-YYYY] / [Umur] tahun / [RM]*

_[DPJP]_
```

✅ Checklist:
- [ ] "Assalamualaikum dokter. Tabe dokter, mohon izin melaporkan follow up pasien" — BUKAN format pasien baru
- [ ] Lokasi di bold: *CVCU bed N*
- [ ] Nama, TTL, umur, RM di bold
- [ ] Semua DPJP di italic underscore — termasuk DPJP Utama, DPJP Tindakan, DPJP Pulmo, DPJP EMD, DPJP GH, DPJP GEH, DPJP Rehab Medik, dll
- [ ] Baris rujukan dengan underscore italic (bila ada)

## 2. DIAGNOSIS LIST

**Format:**
```
*Diagnosis*
- [Diagnosis 1]
- [Diagnosis 2]
- ...
```

✅ Checklist:
- [ ] Bold header *Diagnosis*
- [ ] Semua diagnosis tercantum dengan bullet `-`
- [ ] Termasuk stratifikasi risiko (GRACE, TIMI, CHADS2VASc, HASBLED, SOFA, SCAI) bila ada
- [ ] Trend laboratorium ditulis dalam tanda kurung: (132->151->157->153)

## 3. SUBJEKTIF [S]

**Format:**
```
S :
[Keluhan/subjektif pasien]
- Post [prosedur/tindakan] (Hari, DD-MM-YYYY)
- demam ada/tidak, perdarahan ada/tidak
```

✅ Checklist:
- [ ] **S : — TIDAK bold** (polos)
- [ ] Subjektif singkat — post tindakan apa, demam/perdarahan

## 4. OBJEKTIF [O] — SISTEM PER SISTEM

**Format:**
```
O :
Airway : Patent dengan ETT ukuran [N], kedalaman [N]cm, mucus (-) Pluq (-)

Breathing : On Ventilator Mode [Mode] FiO2 [N]%, RR [N]x/menit, PEEP [N], VT [N]ml, Ps [N], menghasilkan PIP [N] mbar, VT [N] ml, RR [N] kali/menit, MV [N] L/min, Bunyi pernapasan Vesikuler +/+, Rh +/+, Wh -/-, SpO2 [N]%, LUS : Lung sliding (+), regular pleural line, A lines (-), B lines (+) [deskripsi]

Circulation : Tekanan darah [N]/[N] mmHg (MAP [N]), nadi [N] x/menit [reguler/ireguler], didapatkan LV VTI [N] cm, LVSV [N] ml, LVCO [N] L/min, SVR [N] dynes/sec.cm-5, eRAP [N], CI [N], CPO [N], CPI [N], SVV [N]%

Disability : GCS E[N]M[N]Vx tersedasi dengan [obat] [dosis]

Exposure : Suhu [N], Elektrolit (DD-MM-YYYY) [hasil], AGD (DD-MM-YYYY) [kesan], PO2 [N], pCO2 [N], HCO3 [N], laktat [N]; Foto thorax (DD-MM-YYYY) : [kesan]
```

✅ Checklist:
- [ ] **O : — TIDAK bold** (polos)
- [ ] **Airway** — ukuran ETT, kedalaman, mucus, pluq
- [ ] **Breathing** — setting ventilator LENGKAP (mode, FiO2, RR, PEEP, VT set, Ps), hasil aktual (PIP, VT aktual, RR aktual, MV), auskultasi (Vesikuler, Rh, Wh), SpO2, LUS
- [ ] **Circulation** — TD, MAP, nadi, LV VTI, LVSV, LVCO, SVR, eRAP, CI, CPO, CPI, SVV
- [ ] **Disability** — GCS, sedasi
- [ ] **Exposure** — suhu, elektrolit terbaru, AGD terbaru, foto thorax
- [ ] Semua parameter ECHO hemodinamik: LVOT VTI, LVSV, LVCO, SVR, eRAP
- [ ] Parameter LUS: lung sliding, pleural line, A lines, B lines, C lines, effusion

## 5. FLUID (Balance Cairan)

**Format:**
```
Fluid :
Keb. Cairan ([N] ml/kg) [N] ml/24 jam
Intake [N]cc
Output [N] cc
BC [+/-][N] cc
UO : [N]cc/[N]kg/[N]jam = [N] cc/kg/jam
```

✅ Checklist:
- [ ] Keb. Cairan: hitung 30 ml/kgBB
- [ ] Intake total
- [ ] Output total (termasuk urine + IWL)
- [ ] Balance cairan (BC)
- [ ] Urine output dalam cc/kg/jam

## 6. GLUCOSE & GUT

**Format:**
```
Glucose & Gut :
Enteral : - [Makanan] [kkal] ([frekuensi] x [porsi])
- [ONS/Supplement] [kkal] ([frekuensi] x [dosis])
Total kebutuhan kalori = [N] kkal
GDP [N]
HbA1C [N]
Plan :
- Cek GDS/6 jam
- GDS target [range]
- GDP target [range]
Rectal Toucher : mucosa [deskripsi], sphicter [deskripsi], massa (-), darah (-), feses (-)
```

✅ Checklist:
- [ ] Rincian enteral: makanan + ONS + suplemen
- [ ] Hitung total kalori
- [ ] GDP dan HbA1C
- [ ] Plan GDS/GDP target
- [ ] Rectal Toucher bila ada data

## 7. HYPO/HYPERTHERMIA & HAEMATOLOGY

**Format:**
```
Hypo/Hyperthermia and Haematology
T [N]
*Laboratorium PJT (DD-MM-YYYY)*
*WBC : [N]*; *HB : [N]* N/L [N]/[N]; Ur/Cr : *[N]/[N]* *eGFR [N]*
SGOT/SGPT : *[N]/[N]*; Albumin *[N]*
Plan:
[Antibiotik regimen]
```

✅ Checklist:
- [ ] Bold header
- [ ] Lab terbaru WBC, HB, N/L, Ur/Cr, eGFR, SGOT/SGPT, Albumin
- [ ] Antibiotik plan dengan durasi (H-N)

## 8. INFECTION

**Format:**
```
Infection
*Laboratorium PJT (DD-MM-YYYY)*
CRP [N] -> [N]
*Prokalsitonin [N] -> [N] -> [N]*
*Urinalisis (DD-MM-YYYY)*
Kesan : [temuan]

*Biakan sputum ETT evaluasi (DD-MM-YYYY):* [hasil]
*Kultur spesimen darah:* [hasil]
*Smear gram sputum:* [hasil]
```

✅ Checklist:
- [ ] CRP trend
- [ ] Prokalsitonin trend
- [ ] Urinalisis
- [ ] Kultur biakan (sputum, darah)
- [ ] Smear gram

## 9. ASSESSMENT (Mohon izin assess dengan)

**Format:**
```
*Mohon izin kami assess dengan*
- [Diagnosis + stratifikasi]
```

✅ Checklist:
- [ ] Bold header
- [ ] Semua diagnosis diulang dari atas (redudansi sengaja — untuk ronde)

## 10. TERAPI (Mohon izin kami terapi dengan)

**Format:**
```
Mohon izin kami terapi dengan
- [Obat] [dosis]/[frekuensi]/[rute]
```

✅ Checklist:
- [ ] Bold header
- [ ] IVFD di baris pertama
- [ ] Format per baris: `- [Obat] [dosis]/[frekuensi]/[rute]`
- [ ] Termasuk "Selesai diberikan:" untuk obat yang sudah STOP

## 11. PLAN

**Format:**
```
Plan:
- Monitoring tanda vital dan hemodinamik
- Monitoring urine output dan balance cairan
- [Plan lain]
```

## 12. TS (TIM SPESIALIS) KONSULTAN

Setiap TS memiliki format sendiri:

**Format:**
```
*TS [Nama Spesialisasi]*
Assessment :
- [Diagnosis]

Terapi :
- [Obat] [dosis]/[frekuensi]/[rute] (DD-MM-YYYY) [keterangan]

[Plan:]
- [Item plan]
```

✅ Checklist:
- [ ] Bold header per TS
- [ ] Assessment diagnosis
- [ ] Terapi dengan tanggal mulai + keterangan (STOP/Selesai/TAO)
- [ ] Plan diagnostik bila ada

**TS yang sering muncul:**
- TS Pulmonologi — gagal napas, pneumonia, antibiotik
- TS Anestesi — ventilator, sedasi, fentanyl/midazolam
- TS EMD — DM, insulin basal-koreksi, GDS
- TS Gizi — malnutrisi, suplemen, zinc, thiamin
- TS GH — AKI/CKD, nephrosteril, resfar, hindari nefrotoksik
- TS GEH — hepatitis iskemik, SNMC, hepatoprotektor
- TS Rehab Medik — immobilisasi, FT, safemob, positioning, precaution hemodinamik

## 13. PENUTUP

```
Selanjutnya mohon arahan dokter. Terima kasih Dokter.
```

## ⛔ PITFALLS

1. ❌ **S: dan O: bold** — Format CVCU beda dari SOAP IGD, S: dan O: **TIDAK bold**
2. ❌ **Lupa echo hemodinamik** — parameter LV VTI, LVSV, LVCO, SVR, eRAP WAJIB ada
3. ❌ **TS konsulen tidak lengkap** — setiap TS harus ada Assessment + Terapi
4. ❌ **Terapi tanpa tanggal** — antibiotik dan obat lain perlu tanggal mulai + status (STOP/Selesai/TAO)
5. ❌ **Format TS tidak konsisten** — setiap TS punya format sendiri, lihat template
6. ❌ **Bingung dengan SOAP IGD** — ini adalah laporan **CVCU follow up**, bukan pasien baru IGD. Gunakan format ini, BUKAN soap-igd-golden-checklist.
