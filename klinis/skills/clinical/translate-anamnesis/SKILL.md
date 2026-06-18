---
name: translate-anamnesis
description: "Translate seluruh data pasien IGD PJT Jantung ke Inggris dalam 1 kali prompt. Mencakup identitas, anamnesis, pemeriksaan fisis, assessment, terapi, dan plan. Output berupa 6 section terpisah dalam codeblock, format (+)/(-) untuk efisiensi."
triggers:
  - user meminta translate pasien ke Inggris
  - user meminta English version of all sections
  - user menyebut "translate" dan "anamnesis"
  - user menyebut "translate all" atau "translate semua"
  - user mengirim data pasien dan meminta diterjemahkan
  - setiap kali user mengirim data pasien baru dan berkata "translate"
---

# Translate All Sections -> English

Satu prompt mencakup semua section. Output berupa 6 blok terpisah dengan urutan tetap:

1. **Identitas** (codeblock, Label : Value format)
2. **Anamnesis** (codeblock, narasi dengan (+)/(-))
3. **Physical Examination** (codeblock)
4. **Assessment** (codeblock, tanpa header, tanpa bullet)
5. **Therapy** (codeblock, tanpa header, tanpa bullet)
6. **Plan** (codeblock, tanpa header, tanpa bullet)

Setiap blok dipisah baris kosong. Header bisa ditulis di luar codeblock.

## Urutan Lengkap Output

### Blok 1 - Identitas
(Codeblock — urutan tetap: Name, Age, DOB, Address, MR, Date of Admission, DPJP, baris kosong, lalu Referral narasi)

```
Name    : Mr./Mrs. [Initial]
Age     : [Age] years old
Date of birth : [DD-MM-YYYY]
Address : [City/Domicile]
MR      : [MRN]
Date of Admission : [DD-MM-YYYY]
DPJP    : [dr. Name]

Patient Reffered From [RS] with [diagnosis]
```

- Referral: baris terakhir, 1 baris kosong setelah DPJP, dalam narasi (bukan Label : Value), diawali "Patient Reffered From"
- Jika tidak ada rujukan, SKIP baris Referral dan baris kosong sebelumnya (tidak perlu ditulis)

### Blok 2 - Anamnesis
(Codeblock)

```
Chief complaint: ...

[Paragraf narasi lengkap dengan (+)/(-)]

Coronary Risk Factors:
- History of hypertension: ...
- History of diabetes mellitus: ...
- Smoking history: ...
- Family history of heart disease: ...
```

### Blok 3 - Physical Examination
(Codeblock)

```
Compos mentis (GCS 15; E4M6V5)
Blood Pressure: ... mmHg. Pulse: ... bpm, ... Respiratory Rate: ... breaths/minute. Temperature: ...C. SpO2: ...%
Conjunctiva anemic (-), sclera icteric (-)
JVP R+... cmH2O
Heart sounds S1/S2 regular, murmur (-)
Lungs: Vesicular breath sound, no rhonchi and no wheezing
Extremities: warm extremities, no edema, CRT <2 seconds
```

### Blok 4 - Assessment
(Codeblock, tanpa header, tanpa bullet)

```
STEMI ... KILLIP I (TIMI Score ...)
CAD2VD ...
...
```

### Blok 5 - Therapy
(Codeblock, tanpa header, tanpa bullet)

```
IVFD NaCl 0.9% 500 cc/24h/IV
Aspilet 80 mg/24h/oral
...
```

### Blok 6 - Plan
(Codeblock, tanpa header, tanpa bullet)

```
Monitor vital signs and hemodynamics
Monitor signs of bleeding
...
```

---

## Checklist Master - Semua Section

### A. Identitas
- [ ] Label konsisten: Name, Age, Date of birth, Address, MR, Date of Admission, DPJP
- [ ] Value kosong jika info tidak tersedia (jangan halusinasi)
- [ ] Name: Mr./Mrs. + huruf depan
- [ ] Age: [angka] years old
- [ ] Date of birth: DD-MM-YYYY
- [ ] Address: dari input (kosong jika tidak disebut)
- [ ] MR: nomor RM
- [ ] Date of Admission: DD-MM-YYYY
- [ ] DPJP: sesuai input
- [ ] Referral: baris narasi terakhir — "Patient Reffered From [RS] with [diagnosis]" — 1 baris kosong setelah DPJP, di dalam codeblock yang sama
- [ ] Jika tidak ada rujukan: SKIP baris Referral dan baris kosongnya (jangan tulis kosong)
- [ ] **Identitas di dalam codeblock — bukan plain text**

### B. Anamnesis
- [ ] Chief complaint: (plain text, tanpa bold markdown)
- [ ] Chest pain triple criteria (lokasi, karakter, penjalaran)
- [ ] Onset + durasi + skala nyeri NRS
- [ ] Perubahan skala: "Upon arrival ..."
- [ ] Diaphoresis (+)/(-)
- [ ] Nausea (+)/(-)
- [ ] Vomiting (+)/(-)
- [ ] Shortness of breath (+)/(-)
- [ ] DOE/PND/Orthopnea (+)/(-)
- [ ] Previous chest pain (+)/(-)
- [ ] Palpitations (+)/(-)
- [ ] Other complaints: fever, cough, BAK, BAB (+)/(-)
- [ ] Riwayat PCI/angiografi (tahun, pembuluh, stent)
- [ ] Obat rutin (nama + dosis)
- [ ] Terapi RS rujukan (bila ada)
- [ ] Obat RS rujukan: injeksi dosis/rute, oral cukup sediaan
- [ ] Coronary Risk Factors: (plain text, tanpa bold markdown)
- [ ] Hipertensi (+)/(-) + keterangan
- [ ] DM (+)/(-) + keterangan
- [ ] Merokok (since, jumlah/hari)
- [ ] PJ Keluarga (+)/(-) + siapa

### C. Physical Examination
- [ ] Status kesadaran baris pertama
- [ ] TTV 1 baris -- dipisah titik
- [ ] Blood Pressure, Pulse bpm, Respiratory Rate breaths/minute, Temperature C, SpO2 %
- [ ] Conjunctiva anemic (-), sclera icteric (-)
- [ ] JVP R+... cmH2O
- [ ] Heart sounds S1/S2 regular, murmur (-)
- [ ] Lungs: Vesicular breath sound, no rhonchi and no wheezing
- [ ] Abdomen: (bila ada)
- [ ] Extremities: warm/cold, edema, CRT
- [ ] Semua (+)/(-) bukan "tidak ada"
- [ ] "regular/irregular" bukan "reguler"

### D. Assessment
- [ ] Tanpa header di dalam codeblock
- [ ] Tanpa bullet (-)
- [ ] 1 baris per diagnosis
- [ ] Istilah medis baku (STEMI, CAD, HFmrEF, CCS)
- [ ] TIMI/GRACE/ARC-HBR angka tetap
- [ ] Killip class tetap "KILLIP I/II/III/IV"
- [ ] Semua diagnosis dari input tersampaikan

### E. Therapy
- [ ] Tanpa header di dalam codeblock
- [ ] Tanpa bullet (-)
- [ ] 1 baris per obat
- [ ] IVFD di baris pertama
- [ ] Format: [Obat] [dosis] / [frekuensi] / [rute] — spasi sebelum & sesudah / (contoh: NaCl 0.9% 500 cc / 24h / IV)
- [ ] ISDN khusus: "[dosis]/SL if chest pain" (bukan /sos/SL)
- [ ] /24h/ sekali sehari, /12h/ dua kali sehari
- [ ] /sos untuk (kp)
- [ ] Dosis desimal pakai titik
- [ ] Rehydration: ... untuk rehidrasi

### F. Plan
- [ ] Tanpa header di dalam codeblock
- [ ] Tanpa bullet (-)
- [ ] 1 baris per plan item
- [ ] Istilah teknis dipertahankan (CVCU, DR, UR, Cr)
- [ ] Semua item dari input asli tersampaikan

### G. Bahasa Umum
- [ ] (+) untuk "ada" / (-) untuk "tidak ada"
- [ ] Bukan "denies", bukan "present/absent"
- [ ] Boleh broken English
- [ ] Tidak ada informasi fiktif/halusinasi

# Translate Anamnesis → English

## Format Output

Output diawali dengan judul section, kemudian isi anamnesis dalam Bahasa Inggris dengan format concise.

**Format baku:**
```
Chief complaint: [Keluhan utama singkat]

[Paragraf narasi lengkap — pakai (+) dan (-) untuk efisiensi]

Coronary Risk Factors:
- History of hypertension: ...
- History of diabetes mellitus: ...
- Smoking history: ...
- Family history of heart disease: ...
```

## ⛔ CHECKLIST WAJIB ⛔

### 1. STRUKTUR
- [ ] Diawali dengan Chief complaint: (plain text, tanpa bold)
- [ ] Baris baru setelah Chief complaint
- [ ] Paragraf narasi berisi semua informasi S (Subjective) dari anamnesis asli
- [ ] Coronary Risk Factors: (plain text, tanpa bold)
- [ ] Setiap faktor risiko di bullet list dengan format "- "

### 2. KONTEN ANAMNESIS
- [ ] **Chest pain triple criteria:** location (left chest/retrosternal), character (heaviness/pressure), radiation (left arm/jaw/back)
- [ ] Pain onset jelas: "since ..." atau "started at ..." dengan tanggal
- [ ] Durasi nyeri: "duration >20 minutes"
- [ ] Pain scale: "NRS [angka]/10"
- [ ] Perubahan skala: "Upon arrival ... pain scale NRS [angka]/10"
- [ ] **Diaphoresis** (+)/(-)
- [ ] **Nausea** (+)/(-)
- [ ] **Vomiting** (+)/(-)
- [ ] **Shortness of breath** (+)/(-)
- [ ] **Dyspnea on exertion / Paroxysmal Nocturnal Dyspnea / Orthopnea** (+)/(-)
- [ ] Previous chest pain history (+)/(-) dan sifatnya
- [ ] **Palpitations** (+)/(-)
- [ ] **Other complaints:** fever, cough, BAK, BAB — (+)/(-)
- [ ] Riwayat PCI/Angiography: year, vessel, stent count — narasi lengkap
- [ ] Riwayat RS rujukan bila ada
- [ ] **Pasien telah mendapat terapi dari RS rujukan** — translated (obat injeksi dosis/rute, oral cukup sediaan)
- [ ] Obat rutin pasien: disebutkan semua dengan dosis

### 3. EFISIENSI BAHASA
- [ ] **(+)** untuk "ada" — bukan "tidak ada" atau "present/absent"
- [ ] **(-)** untuk "tidak ada" — bukan "negative" atau "denies"
- [ ] Boleh broken English — tetap jelas dan tidak menghilangkan konteks
- [ ] TIDAK menggunakan frasa "There was/were history of" — langsung saja "History of ... (+)/(-)" atau narasi langsung
- [ ] TIDAK menggunakan kata "denies" — ganti (-)
- [ ] TIDAK menggunakan "present/absent" — ganti (+)/(-)

### 4. FORMAT CORONARY RISK FACTORS
- [ ] Setiap faktor risiko di bullet: "- [faktor]: ..."
- [ ] Hipertensi: "History of hypertension (+)/(-)"
- [ ] DM: "History of diabetes mellitus (+)/(-)"
- [ ] Merokok: "Smoking history: [ada/tidak], since [usia], [jumlah]/day"
- [ ] PJ Keluarga: "Family history of heart disease (+)/(-)", bila (+) sebut siapa

### 5. PENGGUNAAN (+)/(-) — CONTOH
```
(+) = present/yes/ada
(-) = absent/no/tidak ada
```

**Contoh kalimat:**
```
Diaphoresis (+), nausea (+), vomiting (-).
Shortness of breath (-). Dyspnea on exertion (-), PND (-), orthopnea (-).
History of chest pain (-).
Previous history of palpitations (-).

Other complaints: Fever (+), cough (+), bowel movements within normal limits.
```

### 6. OBAT
- [ ] Obat rutin ditulis dengan dosis: "Aspilet 80 mg, Ramipril 2.5 mg, ..."
- [ ] Obat RS rujukan: "Aspilet 2 tablets, Clopidogrel 300 mg, Atorvastatin 40 mg"

### 7. FINAL CHECK
- [ ] Semua informasi dari anamnesis asli tersampaikan — TIDAK ADA yang terlewat
- [ ] Tidak ada informasi fiktif/halusinasi
- [ ] Format rapi dengan bold section headers
- [ ] Broken English is OK — yang penting semua konteks terjaga

---

## Contoh Output (Gold Standard)

```
Chief complaint: Chest Pain

The patient presented with chest pain that had worsened over the past 3 hours (May 21, 2026, at 05:00) prior to admission to the Emergency Department of RSUD Gowa, with a pain scale of NRS 8/10. Upon arrival at the PJT Emergency Department, with symptom onset of 8 hours (May 21, 2026, at 10:00), the pain scale was NRS 5/10. The chest pain radiated to the left arm and lasted for more than 20 minutes. Diaphoresis (+) and nausea (+), without vomiting. There was history of chest pain (-). Shortness of breath (-). Dyspnea on exertion (-), paroxysmal nocturnal dyspnea (-), and orthopnea (-). There was no prior history of shortness of breath. Previous history of palpitations (-).

Other complaints included no fever, occasional cough, reddish-colored urine since this morning, and bowel movements within normal limits.

The patient was referred from RSUD Gowa and had already received loading doses of Aspilet 2 tablets, clopidogrel 300 mg, and atorvastatin 40 mg.

Coronary Risk Factors:
- History of hypertension, not routinely taking medicine
- No history of diabetes mellitus
- No history of smoking
- No family history of heart disease
```

---

## Physical Examination Translation

Section ini untuk menterjemahkan pemeriksaan fisis (O — Objective) dari Bahasa Indonesia ke Bahasa Inggris.

**Format baku:**
```
[Compos mentis atau status kesadaran]

Blood Pressure: ... mmHg. Pulse: ... bpm, [reguler/ireguler]. Respiratory Rate: ... breaths/minute. Temperature: ...°C. SpO2: ...% [Room Air / on NC ... lpm]

[Conjunctiva anemic/sclera icteric — (+) atau (-)]
JVP R+... cmH2O
Heart sounds S1/S2 [murni reguler/murmur], [murmur (+) atau (-)]
Lungs: [Vesicular/Bronchial/etc] breath sound, rhonchi [description], wheezing [description]
Abdomen: [description]
Extremities: [akral hangat/dingin], edema [ada/tidak], CRT [... seconds]
```

### ⛔ CHECKLIST PEMERIKSAAN FISIS

- [ ] Status kesadaran di baris pertama — "Compos mentis (GCS 15; E4M6V5)" atau sesuai input
- [ ] **TTV di 1 baris** — dipisah titik. Format: "Blood Pressure: ... mmHg. Pulse: ... bpm, ... . Respiratory Rate: ... . Temperature: ...°C. SpO2: ...% ..."
- [ ] Mata: "Conjunctiva anemic (-), sclera icteric (-)" — pakai (-)/(+), bukan "tidak ada"
- [ ] JVP: "JVP R+... cmH2O"
- [ ] Jantung: "Heart sounds S1/S2 regular, murmur (-)" — bunyi murmur: (+) bila ada disebut, (-) bila tidak ada
- [ ] Paru: "Lungs: Vesicular breath sound, no rhonchi and no wheezing"
- [ ] Abdomen: bila ada — "Abdomen: flat, soft, no tenderness"
- [ ] Ekstremitas: "Extremities: warm extremities, no edema, CRT <2 seconds"
- [ ] Semua **(+)/(-)** bukan "ada/tidak ada", bukan "anemic present"
- [ ] Keep it literal — terjemahkan langsung dari bahasa Indonesia ke Inggris tanpa menambah/mengurangi informasi
- [ ] TTV per baris: semua di 1 baris dengan titik sebagai pemisah antar parameter

### Contoh Output Physical Examination

**Input (Bahasa Indonesia):**
```
Compos mentis
Tensi : 153/79 mmHg
Nadi : 47 x/menit, reguler
Nafas : 20 x /menit
Suhu : 36.5°C
SpO2 : 99% Room Air

Mata: konjungtiva tidak anemis, sklera tidak ikterik
JVP R+2 cmH2O
Jantung: BJ I/II murni reguler, murmur tidak ada
Paru: BP vesikuler, ronkhi tidak ada, wheezing tidak ada
Ekstremitas: akral teraba hangat, edema tidak ada, CRT < 2 detik
```

**Output (English):**
```
Compos mentis (GCS 15; E4M6V5)
Blood Pressure: 153/79 mmHg. Pulse: 47 bpm, regular. Respiratory Rate: 20 breaths/minute. Temperature: 36.5°C. SpO2: 99% Room Air
Conjunctiva anemic (-), sclera icteric (-)
JVP R+2 cmH2O
Heart sounds S1/S2 regular, murmur (-)
Lungs: Vesicular breath sound, no rhonchi and no wheezing
Extremities: warm extremities, no edema, CRT <2 seconds
```

### Aturan Terjemahan Istilah

| Indonesia | Inggris |
|---|---|
| Compos mentis | Compos mentis (GCS 15; E4M6V5) |
| Tensi | Blood Pressure |
| Nadi ... x/menit | Pulse ... bpm |
| Nafas ... x/menit | Respiratory Rate ... breaths/minute |
| Suhu | Temperature |
| Saturasi | SpO2 |
| konjungtiva tidak anemis | Conjunctiva anemic (-) |
| sklera tidak ikterik | sclera icteric (-) |
| BJ I/II murni reguler | Heart sounds S1/S2 regular |
| murmur tidak ada | murmur (-) |
| BP vesikuler | Vesicular breath sound |
| ronkhi tidak ada | no rhonchi |
| wheezing tidak ada | no wheezing |
| akral teraba hangat | warm extremities |
| edema tidak ada | no edema |
| CRT < 2 detik | CRT <2 seconds |
| tidak ada | (-) |
| ada | (+) |

---

---

## Assessment Translation

Section ini untuk menterjemahkan assessment / diagnosis dari Bahasa Indonesia ke Bahasa Inggris.

### ⛔ CHECKLIST ASSESSMENT

- [ ] Diawali header: `**Assessment (English):**`
- [ ] Format bullet/bulet sesuai aslinya, hanya diterjemahkan ke Inggris
- [ ] Diagnosis seperti "STEMI Anteroseptal Wall" tetap dipertahankan istilah medisnya
- [ ] Stratifikasi risiko: TIMI Score, GRACE Score, ARC-HBR — diterjemahkan labelnya saja, angkanya tetap
- [ ] Killip class: tetap "KILLIP I/II/III/IV"
- [ ] CAD/CCS/HF: tetap istilah medis baku
- [ ] Hypertensive Heart Disease, Heart Failure dst — terjemahkan narasinya

### Aturan Terjemahan Istilah Assessment

| Indonesia | Inggris |
|---|---|
| Assess dengan | Assessment |
| STEMI [regio] Wall Onset [jam] KILLIP [kelas] | STEMI [region] Wall, Onset [hours], KILLIP [class] |
| TIMI Score [angka] point [persen]% risk of All-Cause Mortality at 30 days | TIMI Score [angka], [persen]% estimated 30-day mortality |
| ARC-HBR Scorex Major [angka] poin, Minor [angka] Point | ARC-HBR Score: Major [angka], Minor [angka] |
| CAD2VD post pPCI 1 stent DES di [pembuluh] | CAD2VD, post pPCI 1 DES stent in [vessel] |
| Heart Failure mildy reduce Ejection Fraction | Heart Failure with mildly reduced Ejection Fraction (HFmrEF) |
| Chronic Coronary Syndrome clinical scenario type [angka] | Chronic Coronary Syndrome, clinical scenario type [angka] |
| Hypertensive Heart Disease | Hypertensive Heart Disease |

---

## Therapy Translation

Section ini untuk menterjemahkan terapi / rencana terapi dari Bahasa Indonesia ke Bahasa Inggris.

### ⛔ CHECKLIST THERAPY

- [ ] Header di luar codeblock — tidak ada di dalam codeblock
- [ ] Format per baris: `[Medication] [dose] / [frequency] / [route]` — tanpa bullet `-`
- [ ] IVFD di baris pertama
- [ ] Dosis desimal pakai titik
- [ ] Setiap obat 1 baris, tanpa bullet list

### Aturan Terjemahan Nama Obat

| Indonesia | Inggris |
|---|---|
| Aspilet | Aspilet (Acetylsalicylic Acid) — atau langsung "Aspilet 80 mg" |
| Clopidogrel | Clopidogrel |
| Ranitidin | Ranitidine |
| NTG | NTG (Nitroglycerin) |
| Atorvastatin | Atorvastatin |
| Bisoprolol | Bisoprolol |
| Ramipril | Ramipril |
| Furosemide | Furosemide |
| ISDN | ISDN (Isosorbide Dinitrate) |
| Heparin | Heparin |
| Laxadyn Syr | Laxadyn Syrup (Lactulose) |
| Simvastatin | Simvastatin |
| NaCl 0.9% | NaCl 0.9% |
| Rehidrasi NaCl 0.9% .../SP | Rehydration: NaCl 0.9% .../SP |
| maintenance | maintenance |
| /oral | /oral |
| /IV | /IV |
| /SP | /SP (syringe pump) |
| /SL | /SL (sublingual) |
| /kp | /sos (as needed) |
| (kp) | (sos) |
| 24 jam | /24h |
| /24 jam/ | /24h/ |
| H-1 | H-1 (unfractionated heparin protocol) |

**Format penulisan obat — rapat tanpa spasi sekitar `/`:**

```
Contoh BENAR:
IVFD NaCl 0.9% 500 cc/24h/IV
Aspilet 80 mg/24h/oral
Heparin 7 IU/kgBB bolus IV then 12 IU/kgBB/h/SP
ISDN 5 mg/SL if chest pain     ← khusus ISDN: "/SL if chest pain" (bukan /sos/)
Laxadin 30 cc/24h/oral

Contoh SALAH (jangan):
IVFD NaCl 0.9% 500 cc / 24h / IV
Aspilet 80 mg / 24h / oral
ISDN 5 mg / sos / SL
```

- Spasi hanya antara nama obat dan dosis, lalu rapat sampai akhir
- Format: `[Obat] [dosis]/[frekuensi]/[rute]`
- `/24h/` sekali sehari, `/12h/` dua kali sehari, `/8h/` tiga kali sehari, `/6h/` empat kali sehari
- ISDN khusus: `[dosis]/SL if chest pain` (bukan /sos/)

---

## Plan Translation

Section ini untuk menterjemahkan rencana / plan dari Bahasa Indonesia ke Bahasa Inggris.

### ⛔ CHECKLIST PLAN

- [ ] Header di luar codeblock — tidak ada di dalam codeblock
- [ ] Format per baris tanpa bullet `-`, 1 baris per plan item
- [ ] "Konsul TS [Spesialisasi]" → "Consult to [Specialization] Subdivision" — lowercase subdivision name (e.g. Endocrinology, Cardiology)

### Aturan Terjemahan Istilah Plan

| Indonesia | Inggris |
|---|---|---|
| Monitoring Tanda vital dan hemodinamik | Monitor vital signs and hemodynamics |
| Monitoring tanda-tanda perdarahan | Monitor signs of bleeding |
| Cek DR, UR, Cr post rehidrasi | Check DR, UR, Cr post rehydration |
| Cek Profil Lipid | Check Lipid Profile |
| Pindah Perawatan CVCU | Transfer to CVCU for further care |
| Konsul TS [Spesialisasi] | Consult to [Specialization] Subdivision |

---

## Complete Output Format — 3 Codeblocks

Ketika user meminta translate semua (assessment + terapi + plan), output berupa **3 codeblock terpisah**. Tidak ada header dan tidak ada bullet `-` di dalam codeblock.

````
```

STEMI [region] Wall, Onset [hours], KILLIP [class] (TIMI Score ...)
CAD2VD, post pPCI ...

```


```

IVFD NaCl 0.9% 500 cc / 24h / IV
Aspilet 80 mg / 24h / oral
...

```


```

Monitor vital signs and hemodynamics
Monitor signs of bleeding
Check DR, UR, Cr post rehydration
...

```
````

Setiap codeblock dipisah baris kosong agar rapi. Header seperti "**Assessment (English):**" ditulis di luar codeblock jika perlu.

---

## Pitfalls
- Jangan gunakan kata "denies" — ganti (-)
- Jangan gunakan "present/absent" — ganti (+)/(-)
- Jangan terjemahkan kata per kata — tangkap konteks medisnya
- Jangan buat kalimat terlalu formal/panjang — concise & broken English OK
- Pastikan semua gejala penyerta disebutkan explicit — jangan skip yang "tidak ada"
- Untuk pasien STEMI/UAP, pastikan triple criteria chest pain disebutkan
- Format **Chief complaint:** satu kata/dua kata singkat: "Chest Pain", "Shortness of Breath", "Palpitations"
- Riwayat PCI: sebut tahun dan pembuluh yang distent
- **Pemeriksaan Fisis:** TTV dalam 1 baris dipisah titik — jangan baris per baris
- **Pemeriksaan Fisis:** Gunakan istilah literal "Blood Pressure" (bukan "Tensi"), "breaths/minute" (bukan "/min")
- **Pemeriksaan Fisis:** Istilah "regular"/"irregular" untuk nadi — bukan "reguler"
