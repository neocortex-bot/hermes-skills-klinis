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

## ⛔ ATURAN WAJIB — BACA SETIAP KALI SEBELUM BUAT SOAP ⛔

### ATURAN PEMBUKA
- **SELALU** "Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *[lokasi]* atas nama:"
- JANGAN pernah pakai "Selamat pagi/siang/sore/malam" kecuali Pakboss secara eksplisit menyuruh
- Format: `Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *[lokasi]* atas nama:`

### ATURAN LAB (KRITIS — SERING SALAH)
- **JANGAN PERNAH mengisi nilai lab fiktif/halusinasi.** Jika data lab tidak diberikan:
  - Tulis header `*Hasil Lab (DD-MM-YYYY):*` dengan tanggal
  - Tulis parameter lab dalam FORMAT GABUNGAN (per baris parameter gabungan, bukan per item):
  ```
  *Hasil Lab (15-06-2026):*
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
  ```
  - **KOSONGKAN NILAINYA** — jangan isi angka fiktif, jangan pakai "—", jangan pakai "..."
  - Biarkan kolom nilai kosong agar Pakboss isi sendiri
- HANYA Echo dan Foto Thorax yang boleh ditulis "Menyusul"

### ATURAN FOTO THORAX
- Format: `*Foto Thorax (DD-MM-YYYY):* Menyusul` (WAJIB sertakan tanggal)

### ATURAN ECHOCARDIOGRAPHY
- Format: `*Echocardiography (DD-MM-YYYY):* Menyusul` (WAJIB sertakan tanggal)

### ATURAN OBAT
- Format penulisan: `[Nama Obat] [dosis] / [frekuensi] / [rute]`
- Contoh BENAR: `Asam Mefenamat 500 mg / 3x1 / oral`
- Contoh SALAH: `Asam Mefenamat 500 mg / 3x1 / oral KP nyeri` (jangan tambah "KP nyeri" di rute)
- Jangan campur indikasi/kepentingan di baris rute

### ATURAN PEMBUKAAN (sekali lagi)
- **Assalamualaikum** — jangan "Selamat pagi"

### ATURAN TTD — JANGAN PERNAH ISI NILAI FIKTIF/LAB HALUSINASI
- Biarkan KOSONG untuk diisi Pakboss

### ATURAN BOLD
- 🟢 PAKAI *...*: lokasi pasien, nama pasien, EKG, Hasil Lab, Foto Thorax, Echocardiography, Mohon izin assess, Mohon izin terapi, Plan
- 🔴 JANGAN PAKAI *...*: S, O, dan semua body/data/lab/TTV/deskripsi/fisis
- SELALU bungkus SOAP di ``` (code block)

### FORMAT EKG
- 1 baris sequential, parameter dipisah koma:
  `Sinus Rhythm, HR [x] bpm, reguler, Normoaxis, P wave [x] sec, PR interval [x] sec, QRS Duration [x] sec, No ST-T changes`
- Untuk AF: irama = `Supraventricular Rhythm` (bukan Atrial Fibrillation)
- Jika belum ada data EKG: tulis EKG normal lengkap (boleh diisi dengan nilai perkiraan, ini satu-satunya yang boleh)

### TOP 10 KESALAHAN FATAL

| # | Kesalahan | Yang BENAR |
|---|---|---|
| 1 | `*S:*` atau `*O:*` pakai bold | `S:` dan `O:` POLOS tanpa asterisk |
| 2 | `*A (Assessment):*` | `*Mohon izin kami assess dengan:*` |
| 3 | `*Terapi:*` | `*Mohon izin kami terapi dengan:*` |
| 4 | TTV berjejer pipe: `TD: 141/88 | Nadi: 100` | Tiap baris baru, nama panjang: `Tekanan Darah:`, `Nadi:`, `Pernapasan:`, `Suhu:`, `Saturasi:` |
| 5 | TTV disingkat: `TD:`, `RR:`, `HR:` | `Tekanan Darah:`, `Pernapasan:`, `Nadi:` |
| 6 | `(-)` / `(+)` / `[-/+]` di fisis | Narasi: `tidak ada` / `ada` |
| 7 | Lab berjejer pipe: `WBC: 10 | Hb: 12` | Tiap parameter baris sendiri, FORMAT GABUNGAN |
| 8 | LAB DIISI NILAI FIKTIF/HALUSINASI | KOSONGKAN nilai lab — biarkan Pakboss isi |
| 9 | EKG cuma 1-2 kata: `SVT, HR 136` | Sequential lengkap: Rhythm, HR, axis, P, PR, QRS, ST, T |
| 10 | Tidak pakai code block | SELALU bungkus SOAP di ``` |

### FORMAT SOAP LENGKAP (WAJIB persis urutan ini)

```
Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *[lokasi]* atas nama:

*[Tn./Ny.] [Nama] / [DD-MM-YYYY] / [Umur] tahun / RM [nomor]*

S:
- [Narasi keluhan utama — onset, karakter, durasi, gejala penyerta. Paragraf kontinu.]
- Riwayat [penyakit] ada/tidak ada
- Riwayat [penyakit lain] ada/tidak ada

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
Sinus Rhythm, HR ... bpm, reguler, Normoaxis, P wave ... sec, PR interval ... sec, QRS Duration ... sec, No ST-T changes

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
- [Diagnosis 1]

*Mohon izin kami terapi dengan:*
- [Obat] [dosis] / [frekuensi] / [rute]

*Plan:*
- [Item plan 1]

Tabe dokter, mohon arahannya dokter, terima kasih dokter.
```

### ATURAN PEMERIKSAAN FISIS
- TIDAK pakai (-)/(+) atau [-/+]
- Narasi: `[temuan] tidak ada` / `[temuan] ada`
- Format baku:
  - Mata: konjungtiva tidak anemis, sklera tidak ikterik
  - Leher: JVP R+2 cmH2O dalam batas normal
  - Thorax: BP vesikuler, ronkhi tidak ada, wheezing tidak ada
  - Jantung: BJ I/II murni reguler, murmur tidak ada
  - Abdomen: datar, supel, hepar dan lien tidak teraba, nyeri tekan tidak ada
  - Ekstremitas: akral teraba hangat, edema tidak ada, CRT < 2 detik

### ATURAN OBAT — FORMAT TEPAT
- `[Nama Obat] [dosis] / [frekuensi] / [rute]`
- Contoh: `Asam Mefenamat 500 mg / 3x1 / oral`
- JANGAN tambah keterangan KP/indikasi di rute
- JANGAN pakai "— sudah diberikan"

### PRINSIP
- 1 sesi = 1 pasien — tidak campur data antar pasien
- Kumulatif — setiap informasi baru ditambahkan ke SOAP yang sudah ada
- Output selalu SOAP lengkap terbaru (bukan hanya delta)
- Initial report = langsung full

### PITFALLS
- Jangan campur template ACS untuk non-ACS
- Jangan singkat nama DPJP
- Jangan pernah isi nilai lab fiktif
- Jangan tanya "mau terapi apa?" — berikan opsi standar
