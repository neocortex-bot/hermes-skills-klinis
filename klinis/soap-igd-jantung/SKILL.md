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

## ⛔ WAJIB — VALIDASI GOLD STANDARD SEQUENTIAL CHECKLIST ⛔

**SEBELUM MENGIRIM SOAP, WAJIB CEK SEMUA ITEM DI BAWAH INI SATU PER SATU — TIDAK BOLEH LOMBAT**

---

### CHECKLIST SEGMEN [S] — SUBJEKTIF
- [ ] Pembukaan: "Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *[lokasi]* atas nama:" — SELALU Assalamualaikum, JANGAN "Selamat pagi/siang/sore/malam" kecuali user explicit
- [ ] Identitas: *[Tn./Ny.] [Nama] / [DD-MM-YYYY] / [Umur] tahun / RM [nomor]*
- [ ] DPJP Utama dan DPJP Tindakan (jika ada) di baris terpisah pakai underscore italic
- [ ] Kalimat rujukan: _Pasien dirujuk dari [RS] dengan diagnosis [diagnosis]_
- [ ] Keluhan utama: onset, karakter, durasi, lokasi, penjalaran, skala nyeri
- [ ] Gejala penyerta: keringat dingin, mual/muntah, sesak napas, berdebar — tulis "tidak ada" jika memang tidak ada, JANGAN "tidak disebutkan"
- [ ] Riwayat penyakit dahulu: riwayat PCI/operasi jantung (tahun, RS), HT, DM, merokok, PJ keluarga
- [ ] Riwayat rujukan: dari RS mana, diagnosis rujukan, tujuan rujuk
- [ ] Terapi RS rujukan: tulis per baris format "[Obat] [dosis] / [frekuensi] / [rute]" — pisahkan IV dan oral rapi
- [ ] FRK (Faktor Risiko Kardiovaskular): bullet point rapi
- [ ] ANAMNESIS LENGKAP — checklist isi minimal:
  - [ ] Onset dan durasi nyeri
  - [ ] Karakter nyeri (tipikal/atipikal)
  - [ ] Penjalaran
  - [ ] Gejala penyerta (keringat dingin, mual, muntah, pusing, sesak, berdebar)
  - [ ] Riwayat PCI/stenting (tahun, RS, jumlah stent)
  - [ ] Riwayat HT — sejak kapan, berobat teratur/tidak
  - [ ] Riwayat DM — ada/tidak
  - [ ] Riwayat merokok — ada/tidak
  - [ ] Riwayat PJ keluarga — ada/tidak
  - [ ] Riwayat rujukan — dari RS mana, diagnosis rujukan, tujuan

---

### CHECKLIST SEGMEN [O] — OBJEKTIF
#### TTV
- [ ] Tekanan Darah: ... mmHg (bukan TD)
- [ ] Nadi: ... kali/menit [reguler/ireguler] (bukan HR, bukan N)
- [ ] Pernapasan: ... kali/menit (bukan RR)
- [ ] Suhu: ...°C (bukan S, pakai derajat)
- [ ] Saturasi: ...% [room air / on NC ... lpm] (bukan SpO2)

#### Pemeriksaan Fisis
- [ ] Mata: konjungtiva tidak anemis, sklera tidak ikterik
- [ ] Leher: JVP R+2 cmH2O dalam batas normal
- [ ] Thorax: BP vesikuler, ronkhi tidak ada, wheezing tidak ada
- [ ] Jantung: BJ I/II murni reguler, murmur tidak ada
- [ ] Abdomen: datar, supel, hepar dan lien tidak teraba, nyeri tekan tidak ada
- [ ] Ekstremitas: akral teraba hangat, edema tidak ada, CRT < 2 detik
- [ ] Fis PAKAI narasi "tidak ada" / "ada" — JANGAN pakai (-)/(+)/[-/+]

#### EKG — CHECKLIST KRITISS
- [ ] Format: 1 baris sequential, parameter dipisah koma
- [ ] Rhythm: Sinus Rhythm / Sinus Bradi / SVT / AF (jika AF → "Supraventricular Rhythm" bukan Atrial Fibrillation)
- [ ] HR: ... bpm
- [ ] Reguler/ireguler
- [ ] Axis: Normoaxis / Left Axis / Right Axis
- [ ] P wave: ... sec (default 0,08 sec jika tidak diketahui)
- [ ] PR interval: ... sec (default 0,16 sec jika tidak diketahui)
- [ ] QRS Duration: ... sec (default 0,08 sec jika tidak diketahui)
- [ ] ST segment: TULIS SESUAI KONDISI — JANGAN "no significant changes" jika ada T inverted/ST elevasi/depresi
- [ ] T wave: normal / inverted [lead] / elevated [lead] / depressed [lead]
- [ ] JANGAN menyalin singkat dari data mentah user
- [ ] **KONSISTENSI ST-T**: Cek apakah T inverted/ST elevasi ada. Jika ada → ST segment TIDAK "no significant changes"
- [ ] Contoh benar T inverted saja: "ST segment no significant changes, T inverted V1-V6, I, avL"
- [ ] Contoh benar ST elevasi + T inverted: "ST segment elevated V1-V4, T wave inverted V1-V6"
- [ ] Contoh benar ST depresi: "ST segment depressed V5-V6, T wave inverted V5-V6"
- [ ] Jika tidak ada data EKG sama sekali → tulis lengkap dengan nilai perkiraan normal (boleh)

#### Lab
- [ ] Header: *Hasil Lab (DD-MM-YYYY):*
- [ ] Format gabungan per baris (Hb/Leuko/Trombo, PT/INR/APTT, GDS, Ureum/Kreatinin, GOT/GPT, Na/K/Cl, Troponin I, HBsAg/Anti HCV)
- [ ] **KOSONGKAN SEMUA NILAI** — jangan isi fiktif, jangan "—", jangan "..."
- [ ] Jangan pakai pipe untuk lab

#### Foto Thorax
- [ ] Format: *Foto Thorax (DD-MM-YYYY):* Menyusul

#### Echocardiography
- [ ] Format: *Echocardiography (DD-MM-YYYY):* Menyusul

---

### CHECKLIST SEGMEN [A] — ASSESSMENT
- [ ] Diawali bold: *Mohon izin kami assess dengan:*
- [ ] Diagnosis utama dengan stratifikasi risiko lengkap (sesuai template spesifik)
- [ ] Contoh NSTEMI: `- NSTEMI High risk (GRACE Score  points, % probability of death, ARC-HBR )`
- [ ] Diagnosis tambahan di baris berikut

---

### CHECKLIST SEGMEN [P] — TERAPI & PLAN
#### Terapi
- [ ] Diawali bold: *Mohon izin kami terapi dengan:*
- [ ] Format SETIAP baris: `- [Nama Obat] [dosis] / [frekuensi] / [rute]`
- [ ] IVFD di baris PERTAMA
- [ ] JANGAN pakai "(lanjut)", "(selesai diberikan)" atau keterangan tambahan di rute
- [ ] JANGAN pakai "— sudah diberikan"
- [ ] JANGAN campur indikasi di rute (misal "KP nyeri")
- [ ] Dosis angka desimal pakai koma: 1,25 mg — BUKAN 1.25 mg

#### Plan
- [ ] Diawali bold: *Plan:*
- [ ] Minimal: monitoring, plan lanjutan, konsul jika perlu
- [ ] Penutup: `Tabe dokter, mohon arahannya dokter, terima kasih dokter.`

---

### CHECKLIST FORMAT UMUM
- [ ] SELALU bungkus seluruh SOAP di ``` (code block)
- [ ] BOLD (*...*) hanya untuk: lokasi, nama pasien, EKG, Hasil Lab, Foto Thorax, Echocardiography, Mohon izin assess, Mohon izin terapi, Plan
- [ ] JANGAN bold S:, O: atau body/data/TTV/deskripsi/fisis
- [ ] DPJP Utama dan DPJP Tindakan di baris TERPISAH pakai underscore italic (_..._)
- [ ] TTV nama PANJANG: Tekanan Darah, Nadi, Pernapasan, Suhu, Saturasi
- [ ] Obat format KONSISTEN semua: `[Obat] [dosis] / [frekuensi] / [rute]`

---

## ⛔ ATURAN WAJIB — REFERENSI CEPAT ⛔

### ATURAN PEMBUKA
- **SELALU** "Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *[lokasi]* atas nama:"
- JANGAN pernah pakai "Selamat pagi/siang/sore/malam"

### ATURAN LAB
- **JANGAN PERNAH mengisi nilai lab fiktif/halusinasi.**
- KOSONGKAN semua nilai — jangan "—", jangan "..."
- HANYA Echo dan Foto Thorax yang boleh "Menyusul"

### ATURAN OBAT
- Format baku: `[Nama Obat] [dosis] / [frekuensi] / [rute]`
- Contoh BENAR: `Aspilet 80 mg / 24 jam / oral`
- Contoh SALAH: `Aspilet 80 mg / 24 jam / oral (lanjut)`
- Contoh SALAH: `Aspilet 80 mg / 24 jam / oral KP`
- Jangan tambah "(lanjut)", "(selesai diberikan)", atau keterangan apapun di rute

### ATURAN TTV
- Nama PANJANG: Tekanan Darah, Nadi, Pernapasan, Suhu, Saturasi
- BUKAN: TD, HR, RR, S, SpO2

### ATURAN FISIS
- Narasi: `tidak ada` / `ada` — BUKAN (-)/(+)/[-/+]

### ATURAN EKG — RINGKASAN
- Sequential lengkap: Rhythm, HR, reguler/ireguler, Axis, P wave, PR interval, QRS Duration, ST segment, T wave
- Jangan menyalin singkat dari user — tulis PANJANG
- Parameter tak diketahui: isi default P 0,08, PR 0,16, QRS 0,08
- **KONSISTENSI**: Jika T inverted / ST elevasi/depresi → ST segment TIDAK "no significant changes"

### PRINSIP
- 1 sesi = 1 pasien
- Kumulatif — setiap update perbarui SOAP lengkap
- Output selalu SOAP lengkap (bukan delta)

### PITFALLS
- Jangan campur template ACS untuk non-ACS
- Jangan singkat nama DPJP
- Jangan isi lab fiktif

### FORMAT SOAP LENGKAP

```
Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *[lokasi]* atas nama:

*[Tn./Ny.] [Nama] / [DD-MM-YYYY] / [Umur] tahun / RM [nomor]*

_DPJP Utama: dr. [Nama], Sp.JP, Subsp. ..._
_DPJP Tindakan: dr. [Nama], Sp.JP(K)_

_Pasien dirujuk dari [RS] dengan diagnosis [diagnosis]_

S:
- [Keluhan utama — onset, karakter, durasi, penjalaran, gejala penyerta]
- [Riwayat PCI/operasi jantung — tahun, RS]
- [Riwayat dirujuk — RS, diagnosis, tujuan]
- [Terapi RS rujukan per baris]
- Faktor Risiko Kardiovaskular:
  - Riwayat HT ...
  - Riwayat DM ...
  - Riwayat merokok ...
  - Riwayat PJ keluarga ...

O:
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
[Panjang sequential]

*Hasil Lab (DD-MM-YYYY):*
Hemoglobin:
Leukosit:
Trombosit:
PT/INR/APTT:
Glukosa Darah Sewaktu:
Ureum/Kreatinin:
GOT/GPT:
Na/K/Cl:
Troponin I:
HBsAg/Anti HCV:

*Foto Thorax (DD-MM-YYYY):*
Menyusul

*Echocardiography (DD-MM-YYYY):*
Menyusul

*Mohon izin kami assess dengan:*
- [Diagnosis 1 (dengan stratifikasi risiko lengkap)]

*Mohon izin kami terapi dengan:*
- [Obat] [dosis] / [frekuensi] / [rute]

*Plan:*
- [Item plan 1]

Tabe dokter, mohon arahannya dokter, terima kasih dokter.
```
