# Contoh Terjemahan — Tn. Mustafa (15-06-2026)

## Anamnesis — Input Bahasa Indonesia
```
Tn. Mustafa /09-12-1966/59 tahun/RM 205526

S:
- Pasien masuk dengan keluhan nyeri dada kiri yang sudah dialami sejak jam 1 malam, dengan NRS (8/10), saat tiba di IGD PJT nyeri dada berkurang dengan NRS (5/10). Keluhan nyeri dada kiri tembus belakang dan tidak menjalar, dengan durasi >20 menit. Keluhan tidak disertai keringat dingin, mual dan muntah tidak ada. Riwayat nyeri dada sebelumnya ada namun dirasakan hilang timbul. Keluhan sesak nafas tidak ada, riwayat sesak nafas tidak ada. Dyspneu on Effort tidak ada Paroxysmal Nocturnal Dyspneu tidak ada, orthopneu tidak ada. Pasien dapat berbaring terlentang. Keluhan dan riwayat berdebar sebelumnya tidak ada.
- Keluhan lain berupa : Demam tidak ada, batuk tidak ada, rasa mual dan muntah tidak ada, BAK dan BAB kesan normal.

Pasien Riwayat dilakukan tindakan Angiography tahun 2017, dengan hasil CAD1VD post PCI 1 stent DES di RCA. Pasien tidak rutin kontrol di poli, namun saat ini pasien rutin konsumsi obat Aspilet 80 mg, Ramipril 2.5 mg, Bisoprolol 2.5 mg, Simvastatin 20 mg.

Faktor Risiko Kardiovaskular:
- Riwayat hipertensi tidak ada
- Riwayat diabetes melitus tidak ada
- Riwayat merokok sejak usia remaja, saat ini sehari 1 bungkus
- Riwayat penyakit jantung di keluarga tidak ada
```

## Anamnesis — Output English

```
**Chief complaint:** Chest Pain

The patient presented with left chest pain since 1 AM (June 15, 2026), NRS 8/10. Upon arrival at the PJT Emergency Department, chest pain had decreased, NRS 5/10. The chest pain radiated to the back (-), duration >20 minutes. Diaphoresis (-), nausea (-), vomiting (-). Previous history of chest pain (+) but intermittent. Shortness of breath (-). Dyspnea on exertion (-), paroxysmal nocturnal dyspnea (-), orthopnea (-). Patient can lie flat. Previous history of palpitations (-).

Other complaints: Fever (-), cough (-), nausea (-), vomiting (-), bowel and urinary function within normal limits.

The patient underwent Angiography in 2017: CAD1VD post PCI 1 DES stent in RCA. Patient not routinely attending clinic follow-up; currently routinely taking Aspilet 80 mg, Ramipril 2.5 mg, Bisoprolol 2.5 mg, Simvastatin 20 mg.

**Coronary Risk Factors:**
- History of hypertension (-)
- History of diabetes mellitus (-)
- Smoking history: since adolescence, currently 1 pack/day
- Family history of heart disease (-)
```

---

## Physical Examination — Input Bahasa Indonesia
```
O: Compos mentis
Tensi : 143/115 mmHg
Nadi : 76 x/menit, reguler
Nafas : 20 x /menit
Suhu : 36.5 °C
SpO2 : 99% via Nasal Canul 3 lpm

Anemis tidak ada, ikterus tidak ada
JVP R+2 cmH2O
BJ I/II murni reguler, murmur tidak ada
BP Vesikuler, ronkhi dan wheezing tidak ada
Edema ekstremitas tidak ada, akral teraba hangat.
```

## Physical Examination — Output English
```
Compos mentis (GCS 15; E4M6V5)
Blood Pressure: 143/115 mmHg. Pulse: 76 bpm, regular. Respiratory Rate: 20 breaths/minute. Temperature: 36.5°C. SpO2: 99% on NC 3 lpm
Conjunctiva anemic (-), sclera icteric (-)
JVP R+2 cmH2O
Heart sounds S1/S2 regular, murmur (-)
Lungs: Vesicular breath sound, no rhonchi and no wheezing
Extremities: warm extremities, no edema, CRT <2 seconds
```

## Aturan Kunci dari Contoh Ini

1. TTV **1 baris** dengan titik sebagai pemisah — bukan baris per baris
2. Istilah: "Blood Pressure" (bukan Tensi), "Pulse" (bukan Nadi), "regular" (bukan reguler)
3. NC flow: "on NC 3 lpm" (bukan terjemahan literal "via Nasal Canul")
4. Symptom: "radiated to the back (-)" — pakai (-) karena dalam sumber tertulis "tidak menjalar"
5. Intermittent symptom: "Previous history of chest pain (+) but intermittent"
6. Coronary risk factors: langsung format "History of hypertension (-)" — tanpa kata "There was/were"
