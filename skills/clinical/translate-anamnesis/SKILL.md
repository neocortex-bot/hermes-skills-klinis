---
name: translate-anamnesis
description: Translate anamnesis pasien IGD PJT Jantung dari Bahasa Indonesia ke Bahasa Inggris dengan format baku, concise, menggunakan (+) dan (-) untuk mempersingkat tanpa kehilangan konteks.
triggers:
  - user meminta translate anamnesis ke bahasa Inggris
  - user menyebut "translate" dan "anamnesis" pasien
  - user meminta Inggris section untuk anamnesis/riwayat
---

# Translate Anamnesis → English

## Format Output

Output diawali dengan judul section, kemudian isi anamnesis dalam Bahasa Inggris dengan format concise.

**Format baku:**
```
**Chief complaint:** [Keluhan utama singkat]

[Paragraf narasi lengkap — pakai (+) dan (-) untuk efisiensi]

**Coronary Risk Factors:**
- History of hypertension: ...
- History of diabetes mellitus: ...
- Smoking history: ...
- Family history of heart disease: ...
```

## ⛔ CHECKLIST WAJIB ⛔

### 1. STRUKTUR
- [ ] Diawali dengan **Chief complaint:** (bold)
- [ ] Baris baru setelah Chief complaint
- [ ] Paragraf narasi berisi semua informasi S (Subjective) dari anamnesis asli
- [ ] **Coronary Risk Factors:** (bold)
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
**Chief complaint:** Chest Pain

The patient presented with chest pain that had worsened over the past 3 hours (May 21, 2026, at 05:00) prior to admission to the Emergency Department of RSUD Gowa, with a pain scale of NRS 8/10. Upon arrival at the PJT Emergency Department, with symptom onset of 8 hours (May 21, 2026, at 10:00), the pain scale was NRS 5/10. The chest pain radiated to the left arm and lasted for more than 20 minutes. Diaphoresis (+) and nausea (+), without vomiting. There was history of chest pain (-). Shortness of breath (-). Dyspnea on exertion (-), paroxysmal nocturnal dyspnea (-), and orthopnea (-). There was no prior history of shortness of breath. Previous history of palpitations (-).

Other complaints included no fever, occasional cough, reddish-colored urine since this morning, and bowel movements within normal limits.

The patient was referred from RSUD Gowa and had already received loading doses of Aspilet 2 tablets, clopidogrel 300 mg, and atorvastatin 40 mg.

**Coronary Risk Factors:**
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
