---
name: soap-igd-jantung
description: Format SOAP baku pelaporan pasien IGD PJT Jantung. 1 sesi = 1 pasien. Setiap informasi baru memperbarui SOAP secara kumulatif. Mendukung input dari speech, foto hasil lab, dan PDF.
triggers:
  - user melaporkan pasien baru IGD PJT
  - user memberikan update anamnesis/lab/echo/prosedur
  - user meminta perbarui SOAP
  - user memberikan foto hasil lab atau PDF
---

# SOAP IGD PJT Jantung

## ⛔ WAJIB — GOLD STANDARD SEQUENTIAL CHECKLIST ⛔

**SEBELUM MENGIRIM SOAP, WAJIB CENTANG SEMUA ITEM DI BAWAH INI SATU PER SATU**
**SETIAP ADA KESALAHAN/KOREKSI, WAJIB CENTANG ULANG SEMUA CHECKLIST**

---

## SEGMENTASI SOAP + CHECKLIST

### 1. PEMBUKA
**Format:**
```
Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di [lokasi] atas nama:

[Tn./Ny.] [Nama] / [DD-MM-YYYY] / [Umur] tahun / RM [nomor]
```
✅ Checklist:
- [ ] "Assalamualaikum dokter" — bukan "Selamat pagi"
- [ ] Lokasi di bold
- [ ] Nama, TTL, umur, RM di bold

### 2. DPJP
**Format:**
```
DPJP Utama: dr. [Nama], Sp.JP, Subsp. ...
DPJP Tindakan: dr. [Nama], Sp.JP, Subsp. ...
```
✅ Checklist:
- [ ] Baris terpisah
- [ ] Pakai underscore italic
- [ ] DPJP Tindakan hanya jika ada
- [ ] Bisa juga "DPJP Utama dan Tindakan" bila disebutkan hanya 1 orang

### 3. RUJUKAN
**Format:**
```
Pasien dirujuk dari [RS] dengan diagnosis [diagnosis]
```
✅ Checklist:
- [ ] Nama RS rujukan
- [ ] Diagnosis rujukan harus lengkap dituliskan tidak disingkat, bila input singkat maka wajib panjangkan

### 4. SUBJEKTIF [S]
**Format:**
```
S:
[Keluhan utama: onset, karakter, durasi, lokasi, penjalaran, skala nyeri]
[Gejala penyerta: keringat dingin, mual/muntah, sesak, berdebar, pusing] — tulis "tidak ada" jika tidak ada
[Riwayat PCI/operasi jantung: tahun, RS, jumlah stent] (bila ada, informasi narasi harus lengkap)
[Riwayat dirujuk: RS, diagnosis, tujuan]
Pasien telah mendapat terapi dari RS rujukan:
[Obat injeksi/subkutan] [dosis] / [berapa jam] / [route]
[Obat oral cukup ditulis sediaannya saja]
```
✅ Checklist:
- [ ] S: — BOLD (sesuai format baru, S: dan O: sekarang bold)
- [ ] Onset dan durasi jelas
- [ ] Karakter nyeri: 3 kriteria tipikal dipanjangkan — 1) retrosternal/chest Pain kiri, 2) terasa berat/ditekan, 3) menjalar ke lengan kiri/rahang/punggung
- [ ] Penjalaran disebut
- [ ] Gejala penyerta LENGKAP: keringat dingin, mual/muntah, sesak, berdebar, pusing — tiap item ditulis "ada" atau "tidak ada", bukan "tidak disebutkan"
- [ ] Riwayat PCI: sebut tahun, RS, jumlah stent
- [ ] Riwayat Hipertensi: dialami sejak kapan, berobat rutin atau tidak, mendapatkan apa
- [ ] Riwayat DM: dialami sejak kapan, berobat rutin atau tidak, mendapatkan apa
- [ ] Riwayat merokok: bila ada sejak berapa tahun, berapa batang/bungkus per hari, bila sudah berhenti — sudah berapa lama berhenti
- [ ] Riwayat PJ keluarga: bila ada sebutkan siapa dari pasien dengan keluarga yang sedarah
- [ ] Riwayat rujukan: RS asal, dengan diagnosis, dirawat berapa hari di sana, sudah menjalani apa
- [ ] Terapi RS rujukan harus lengkap — narasi memanjang/paragraf. Hanya injeksi/subkutan yang ditulis lengkap [dosis]/[berapa jam]/[route]. Oral cukup sediaan saja

**CONTOH TERAPI RUJUKAN:**
```
Pasien telah mendapat terapi dari RS rujukan: Cefotaxim 1 gr / 12 jam / IV, Ranitidin 1 amp / 12 jam / IV, Furosemide 20 mg / 24 jam / IV, Fondaparinux 2,5 mg / 24 jam / subcutan, Santagesik 1 amp / 12 jam / IV, Clopidogrel 75 mg, Atorvastatin 40 mg, Bisoprolol 1,25 mg, Fasorbid 10 mg, Betahistin 6 mg, Dimenhidrinat 2x1, ISDN 5 mg / sublingual
```
Obat oral cukup ditulis sediaannya saja. Sebisa mungkin sebutkan isi obatnya dibandingkan nama brand obatnya.

**Faktor Risiko Kardiovaskular:**
```
Riwayat Hipertensi: ... (dialami sejak kapan, berobat rutin atau tidak, mendapatkan apa)
Riwayat DM: ... (dialami sejak kapan, berobat rutin atau tidak, mendapatkan apa)
Riwayat merokok: ... (bila ada sejak berapa tahun, berapa batang/bungkus per hari, bila sudah berhenti — sudah berapa lama berhenti)
Riwayat PJ keluarga: ... (bila ada sebutkan siapa dari pasien dengan keluarga yang sedarah)
```

### 5. OBJEKTIF [O]

**a. TTV — Checklist:**
- [ ] O: — BOLD (sesuai format baru)
- [ ] Tekanan Darah (bukan TD)
- [ ] Nadi (bukan HR/N)
- [ ] Pernapasan (bukan RR)
- [ ] Suhu pakai °C (bukan S)
- [ ] Saturasi (bukan SpO2)
- [ ] Nadi: reguler/ireguler

**Format:**
```
Tekanan Darah: ... mmHg
Nadi: ... kali/menit [reguler/ireguler]
Pernapasan: ... kali/menit
Suhu: ...°C
Saturasi: ...% [room air / on NC ... lpm]
```

**b. Pemeriksaan Fisis — Checklist:**
- [ ] Semua "tidak ada" / "ada" — BUKAN (-)/(+)
- [ ] Bila abnormal maka ubah yang normal itu
- [ ] Selama tidak diberikan input abnormal, maka asumsikan saja normal. Tidak boleh kata-kata "tidak disebutkan"

**Format:**
```
Mata: konjungtiva tidak anemis, sklera tidak ikterik
Leher: JVP R+2 cmH2O dalam batas normal
Thorax: BP vesikuler, ronkhi tidak ada, wheezing tidak ada
Jantung: BJ I/II murni reguler, murmur tidak ada
Abdomen: datar, supel, hepar dan lien tidak teraba, nyeri tekan tidak ada
Ekstremitas: akral teraba hangat, edema tidak ada, CRT < 2 detik
```

**c. EKG — Checklist KRITIS:**
```
*EKG [lokasi] (DD-MM-YYYY):*
[1 baris sequential lengkap]
```
- [ ] Bold header: *EKG ...*
- [ ] Format: Rhythm, HR, reguler/ireguler, Axis, P wave ... ms, PR interval ... ms, QRS Duration ... ms, ST segment/ T wave abnormality (bila ada)
- [ ] JANGAN menyalin singkat dari user
- [ ] Parameter tak diketahui: isi default P 0,08, PR 0,16, QRS 0,08
- [ ] **KONSISTENSI ST-T**: jika T inverted atau ST elevasi/depresi → ST segment TIDAK "no significant changes"

**CONTOH EKG:**
`*EKG IGD PJT (13-06-2026):*`
`Sinus Bradi, HR 55 bpm, reguler, Normoaxis, P wave 0,08 sec, PR interval 0,16 sec, QRS Duration 0,08 sec, T inverted V1-V6, I, avL`

**d. Lab — Checklist:**
- [ ] Bold header: *Laboratorium [lokasi] (DD-MM-YYYY):*
- [ ] Sebutkan lokasinya, secara default "IGD PJT"
- [ ] Format gabungan per baris
- [ ] SEMUA KOSONG — jangan isi fiktif, jangan "—", jangan "..."

**Format:**
```
*Laboratorium IGD PJT (DD-MM-YYYY):*
Hemoglobin:
Leukosit:
Trombosit:
Neut/Lymp:
PT/INR/APTT:
Glukosa Darah Sewaktu:
Ureum/Kreatinin:
GOT/GPT:
Na/K/Cl:
Troponin I:
HBsAg/Anti HCV:
```

**e. Foto Thorax — Checklist:**
- [ ] Bold header: *Foto Thorax [lokasi] (DD-MM-YYYY):*
- [ ] Isi: Menyusul

**f. Echocardiography — Checklist:**
- [ ] Bold header: *Echocardiography (DD-MM-YYYY):*
- [ ] Isi: Menyusul

### 6. ASSESSMENT [A] — Checklist:
- [ ] Bold header: *Mohon izin kami assess dengan:*
- [ ] Format stratifikasi risiko lengkap sesuai template

**CONTOH NSTEMI:**
```
- NSTEMI Very high risk (GRACE Score .. point ..% probability of death, ARC-HBR .. mayor .. minor)
```

**CONTOH STEMI:**
```
- STEMI [regio wall] + [onset berapa jam] + KILLIP [berapa] + (TIMI Score .. Estimated 30 day mortality ..%, ARC HBR .. Major .. Minor)
```

**CONTOH DIAGNOSIS TAMBAHAN:**
```
- Hipertensive Heart Disease
```

### 7. TERAPI [P1] — Checklist:
- [ ] Bold header: *Mohon izin kami terapi dengan:*
- [ ] Format: `[Obat] [dosis]/[frekuensi]/[rute]` — KONSISTEN semua baris (pakai slash rapat, spasi setelah dosis)
- [ ] IVFD di baris PERTAMA
- [ ] JANGAN "(lanjut)", "(selesai diberikan)", atau keterangan lain
- [ ] Dosis desimal pakai TITIK: 1.25 mg (bukan 1,25)

**Format:**
```
*Mohon izin kami terapi dengan:*
- IVFD NaCl 0.9% 500 cc / 24 jam / IV
- Aspilet 80 mg / 24 jam / oral
- Clopidogrel 75 mg / 24 jam / oral
- ...
```

### 8. PLAN [P2] — Checklist:
- [ ] Bold header: *Plan:*
- [ ] Monitoring tanda vital dan hemodinamik (BARIS PERTAMA)
- [ ] Pantau urine output dan balance cairan (BARIS KEDUA untuk pasien heart failure)
- [ ] Sematkan plan lain yang diperlukan

### 9. PENUTUP
```
Tabe dokter, selanjutnya mohon arahannya dokter, terima kasih dokter.
```

### 10. FORMAT UMUM — FINAL CHECK
- [ ] Seluruh SOAP dibungkus ``` code block
- [ ] Bold (*...*) untuk: lokasi, nama pasien, EKG, Laboratorium, Foto Thorax, Echocardiography, Mohon izin assess, Mohon izin terapi, Plan, **S:**, **O:**
- [ ] Body/data/TTV/deskripsi/fisis TIDAK bold

---

## FORMAT SOAP LENGKAP (GOLD STANDARD)

```
Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *[lokasi]* atas nama:

*[Tn./Ny.] [Nama] / [DD-MM-YYYY] / [Umur] tahun / RM [nomor]*

_DPJP Utama: dr. [Nama], Sp.JP, Subsp. ..._
_DPJP Tindakan: dr. [Nama], Sp.JP, Subsp. ..._

_Pasien dirujuk dari [RS] dengan diagnosis [diagnosis lengkap]_

*S:*
- [Keluhan utama lengkap — onset, karakter 3 kriteria tipikal, lokasi, penjalaran]
- [Gejala penyerta: keringat dingin ..., mual muntah ..., sesak ..., berdebar ..., pusing ...]
- [Riwayat PCI/operasi — tahun, RS, jumlah stent, informasi narasi lengkap]
- [Riwayat dirujuk — RS asal, diagnosis, dirawat berapa hari, tindakan yang sudah dilakukan, tujuan]
- Pasien telah mendapat terapi dari RS rujukan: [obat injeksi] [dosis]/[jam]/[rute], [obat oral cukup sediaan]
- Faktor Risiko Kardiovaskular:
  - Riwayat Hipertensi: [sejak kapan, berobat rutin/tidak, dapat obat apa]
  - Riwayat DM: [sejak kapan, berobat rutin/tidak, dapat obat apa]
  - Riwayat merokok: [ada/tidak, sejak kapan, berapa batang/hari, sudah berhenti — berapa lama]
  - Riwayat PJ keluarga: [ada/tidak, sebutkan siapa]

*O:*
Tekanan Darah: ... mmHg
Nadi: ... kali/menit [reguler/ireguler]
Pernapasan: ... kali/menit
Suhu: ...°C
Saturasi: ...% [room air / on NC ... lpm]

Mata: konjungtiva tidak anemis, sklera tidak ikterik
Leher: JVP R+2 cmH2O dalam batas normal
Thorax: BP vesikuler, ronkhi tidak ada, wheezing tidak ada
Jantung: BJ I/II murni reguler, murmur tidak ada
Abdomen: datar, supel, hepar dan lien tidak teraba, nyeri tekan tidak ada
Ekstremitas: akral teraba hangat, edema tidak ada, CRT < 2 detik

*EKG [lokasi] (DD-MM-YYYY):*
[Panjang sequential — Rhythm, HR, reguler, Axis, P wave, PR, QRS Dur, ST/T abnormality]

*Laboratorium [lokasi] (DD-MM-YYYY):*
Hemoglobin:
Leukosit:
Trombosit:
Neut/Lymp:
PT/INR/APTT:
Glukosa Darah Sewaktu:
Ureum/Kreatinin:
GOT/GPT:
Na/K/Cl:
Troponin I:
HBsAg/Anti HCV:

*Foto Thorax [lokasi] (DD-MM-YYYY):*
Menyusul

*Echocardiography (DD-MM-YYYY):*
Menyusul

*Mohon izin kami assess dengan:*
- [Diagnosis + stratifikasi risiko lengkap]

*Mohon izin kami terapi dengan:*
- [Obat] [dosis]/[frekuensi]/[rute]

*Plan:*
- Monitoring tanda vital dan hemodinamik
- [Pantau urine output dan balance cairan — untuk pasien heart failure]
- [Plan lain]

Tabe dokter, selanjutnya mohon arahannya dokter, terima kasih dokter.
```

---

## ⛔ ATURAN WAJIB — REFERENSI CEPAT ⛔

### PEMBUKA
- "Assalamualaikum dokter" — jangan "Selamat pagi"

### LAB
- JANGAN PERNAH isi nilai fiktif/halusinasi
- KOSONGKAN semua — jangan "—", jangan "..."
- HANYA Echo dan Foto Thorax yang boleh "Menyusul"

### OBAT
- Format: `[Obat] [dosis]/[frekuensi]/[rute]`
- Dosis desimal pakai TITIK: 1.25 mg
- Jangan "(lanjut)", "(selesai diberikan)"
- Oral: cukup sediaan saja
- IVFD di baris pertama

### TTV
- Tekanan Darah, Nadi, Pernapasan, Suhu, Saturasi

### FISIS
- "tidak ada" / "ada" — BUKAN (-)/(+)
- Asumsikan normal, jangan "tidak disebutkan"

### EKG
- Sequential lengkap: Rhythm, HR, reguler, Axis, P wave, PR, QRS Dur, ST/T
- Parameter tak diketahui: P 0,08, PR 0,16, QRS 0,08
- KONSISTENSI: T inverted/ST elevasi → ST segment bukan "no significant changes"

### BOLD
- BOLD (*...*) untuk: lokasi, nama pasien, EKG, Laboratorium, Foto Thorax, Echocardiography, Mohon izin assess, Mohon izin terapi, Plan, **S:**, **O:**
- Body/TTV/deskripsi/fisis TIDAK bold

### PITFALLS
- Jangan campur template ACS untuk non-ACS
- Jangan singkat nama DPJP
- Diagnosis rujukan harus dipanjangkan
- Setiap ada koreksi/kesalahan → CENTANG ULANG SEMUA CHECKLIST
