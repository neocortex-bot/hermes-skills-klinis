---
name: soap-igd-golden-checklist
description: GOLD STANDARD SOAP IGD — dari file dr. Hakim. Pegangan WAJIB.
triggers:
  - user minta buat SOAP IGD
  - user kasih data pasien baru IGD
  - user koreksi SOAP
  - user bilang "HARAMM" atau "jangan ada terlewat"
  - user kirim / refer ke gold-standard-checklist-soap-igd
---

# SEGMENTASI SOAP + CHECKLIST

## 1. PEMBUKA
**Format:**
```
Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *[lokasi]* atas nama:

*[Tn./Ny.] [Nama] / [DD-MM-YYYY] / [Umur] tahun / RM [nomor]*
```

✅ Checklist:
- [ ] "Assalamualaikum dokter" — bukan "Selamat pagi"
- [ ] Lokasi di bold
- [ ] Nama, TTL, umur, RM di bold

## 2. DPJP
**Format:**
```
_DPJP Utama: dr. [Nama], Sp.JP, Subsp. ..._
_DPJP Tindakan: dr. [Nama], Sp.JP, Subsp. ..._
```

✅ Checklist:
- [ ] Baris terpisah
- [ ] Pakai underscore italic
- [ ] DPJP Tindakan hanya jika ada
- [ ] Bisa juga `_DPJP Utama dan Tindakan_` bila disebutkan hanya 1 orang

## 3. RUJUKAN
**Format:**
```
_Pasien dirujuk dari [RS] dengan diagnosis [diagnosis]_
```

✅ Checklist:
- [ ] Nama RS rujukan
- [ ] Diagnosis rujukan harus lengkap dituliskan, tidak disingkat. Bila input singkat, wajib panjangkan.

## 4. SUBJEKTIF [S]
**Format:**
```
S:
- [Keluhan utama: onset, karakter, durasi, lokasi, penjalaran, skala nyeri]
- [Gejala penyerta: keringat dingin, mual/muntah, sesak, berdebar, pusing] — tulis "tidak ada" jika tidak ada
- [Riwayat PCI/operasi jantung: tahun, RS, jumlah stent] (bila ada, narasi lengkap)
- [Riwayat dirujuk: RS, diagnosis, tujuan]
- Pasien telah mendapat terapi dari RS rujukan: [Obat] [dosis] / [frekuensi] / [rute], ...
  contoh: Cefotaxim 1 gr / 12 jam / IV, Ranitidin 1 amp / 12 jam / IV, Furosemide 20 mg / 24 jam / IV, Fondaparinux 2.5 mg / 24 jam / subcutan, ...
  Obat oral cukup sediaannya saja.
- Faktor Risiko Kardiovaskular:
  - Riwayat Hipertensi: sejak kapan, berobat rutin/tidak, obat apa
  - Riwayat DM: sejak kapan, berobat rutin/tidak, obat apa
  - Riwayat merokok: sejak kapan, jumlah, sudah berhenti — berapa lama
  - Riwayat PJ keluarga: siapa (hubungan sedarah)
```

✅ Checklist:
- [ ] **S: — TIDAK bold** (polos)
- [ ] Onset dan durasi jelas
- [ ] Karakter nyeri (tipikal/atipikal) disebut, 3 kriteria dipanjangkan
- [ ] Penjalaran disebut
- [ ] Gejala penyerta LENGKAP: keringat dingin, mual/muntah, sesak, berdebar, pusing — tiap item "ada"/"tidak ada"
- [ ] Riwayat PCI: tahun, RS, jumlah stent
- [ ] Riwayat Hipertensi: sejak kapan, berobat/tidak, obat
- [ ] Riwayat DM: sejak kapan, berobat/tidak, obat
- [ ] Riwayat merokok: durasi, jumlah, sudah berhenti — berapa lama
- [ ] Riwayat PJ keluarga: siapa
- [ ] Riwayat rujukan: RS asal, diagnosis, lama rawat, terapi
- [ ] Terapi RS rujukan: narasi paragraf. Injeksi/subkutan: [dosis]/[berapa jam]/[route]. Oral: cukup sediaan.

## 5. OBJEKTIF [O]

### a. TTV
**Format:**
```
O:
Compos Mentis
Tekanan Darah: ... mmHg
Nadi: ... kali/menit [reguler/ireguler]
Pernapasan: ... kali/menit
Suhu: ...°C
Saturasi: ...% [room air / on NC ... lpm]
```

✅ Checklist:
- [ ] **O: — TIDAK bold** (polos)
- [ ] **Compos Mentis** — WAJIB selalu ada di baris PERTAMA TTV, di atas Tekanan Darah
- [ ] Cocokkan dari input dokter: compos mentis, somnolen, sopor, soporokoma, koma, dll
- [ ] Jika dokter tulis "Compos mentis selalu di atas tensi" — tulis "Compos Mentis" saja
- [ ] Tekanan Darah (bukan TD)
- [ ] Nadi (bukan HR/N)
- [ ] Pernapasan (bukan RR)
- [ ] Suhu pakai °C (bukan S)
- [ ] Saturasi (bukan SpO2)
- [ ] Nadi: [reguler/ireguler] jika dokter sebut
- [ ] **TTV tidak disebut dokter → isi dummy normal** (120/80, 80x/mnt, 20x/mnt, 36.5°C, 98% room air)
- [ ] **DILARANG** tulis "tidak disebutkan"

### b. Pemeriksaan Fisis
**Format:**
```
Mata: konjungtiva tidak anemis, sklera tidak ikterik
Leher: JVP ... cmH2O
Thorax: BP vesikuler, ronkhi tidak ada, wheezing tidak ada
Jantung: BJ I/II murni, murmur tidak ada
Abdomen: datar, supel, hepar dan lien tidak teraba, nyeri tekan tidak ada
Ekstremitas: akral teraba hangat, edema tidak ada, CRT < 2 detik
```

✅ Checklist:
- [ ] "tidak ada"/"ada" — BUKAN (-)/(+)
- [ ] Bila abnormal, ubah deskripsi yang normal itu
- [ ] Asumsikan normal jika tidak disebut abnormal
- [ ] **DILARANG** kata "tidak disebutkan"
- [ ] **JVP: BACA input dokter** — pakai nilai dokter, bukan asumsi R+2
- [ ] **Nadi: tanpa [reguler/ireguler]** jika dokter tidak sebut

### c. EKG
**Format:**
```
*EKG [lokasi] (DD-MM-YYYY):*
[1 baris sequential lengkap]
```

✅ Checklist:
- [ ] Bold header dengan `* *` (bintang)
- [ ] Format: Rhythm, HR, reguler/ireguler, Axis, P wave, PR interval, QRS Duration, ST segment/T wave abnormality
- [ ] JANGAN menyalin singkat dari user
- [ ] Parameter tak diketahui: default P 0.08, PR 0.16, QRS 0.08
- [ ] **KONSISTENSI ST-T**: T inverted/ST elevasi → ST segment BUKAN "no significant changes"
- [ ] AF → tulis "Supraventricular Rhythm"
- [ ] **Hanya jika ada data/indikasi ACS** — jika tidak, LEWATKAN
- [ ] **JANGAN** tulis "belum dikerjakan"

### d. Laboratorium
**Format:**
```
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
```

✅ Checklist:
- [ ] Bold header
- [ ] Lokasi default: IGD PJT
- [ ] **SEMUA KOSONG** — jangan isi fiktif, jangan "—", jangan "..."
- [ ] **Hanya jika ada ≥ 1 hasil lab** — jika tidak, LEWATKAN
- [ ] **JANGAN** tulis "belum dikerjakan"

### e. Foto Thorax
**Format:**
```
*Foto Thorax [lokasi] (DD-MM-YYYY):*
Menyusul
```

✅ Checklist:
- [ ] **Hanya jika user sebut foto thorax** — jika tidak, LEWATKAN
- [ ] **JANGAN** tulis "belum dikerjakan"

### f. Echocardiography
**Format:**
```
*Echocardiography (DD-MM-YYYY):*
Menyusul
```

✅ Checklist:
- [ ] **Hanya jika user sebut echo** — jika tidak, LEWATKAN
- [ ] **JANGAN** tulis "belum dikerjakan"

## 6. ASSESSMENT [A]
**Format:**
```
*Mohon izin kami assess dengan:*
- [Diagnosis 1 (stratifikasi risiko)]
- [Diagnosis tambahan]
```

✅ Checklist:
- [ ] Bold header
- [ ] NSTEMI: NSTEMI Very high risk (GRACE Score .. point ..% probability of death, ARC-HBR .. mayor .. minor)
- [ ] STEMI: STEMI [regio wall] onset [jam] KILLIP [I-IV] (TIMI Score .. Estimated 30 day mortality ..%, ARC HBR .. Major .. Minor)
- [ ] Diagnosis dipanjangkan (tidak disingkat)

## 7. TERAPI [P1]
**Format:**
```
*Mohon izin kami terapi dengan:*
- [Obat] [dosis] / [frekuensi] / [rute]
```

✅ Checklist:
- [ ] Bold header
- [ ] Format `[Obat] [dosis] / [frekuensi] / [rute]` — KONSISTEN
- [ ] IVFD di baris PERTAMA
- [ ] **Frekuensi WAJIB format JAM**: 24 jam, 12 jam, 8 jam, 6 jam — **BUKAN "1x sehari"**, **BUKAN "0-0-1"**, **BUKAN "1x"**
- [ ] JANGAN "(lanjut)", "(selesai)"
- [ ] Dosis desimal pakai titik: 1.25 mg (bukan 1,25)
- [ ] **Obat rutin**: tulis `(obat di pasien)` setelah dosis/frekuensi/rute
- [ ] **Terapi baru**: tanpa `(obat di pasien)`
- [ ] **DILARANG mengarang frekuensi/dosis** — hanya data dokter
- [ ] Per baris per obat dengan "-" bullet

## 8. PLAN [P2]
**Format:**
```
*Plan:*
- [Item plan]
```

✅ Checklist:
- [ ] Bold header
- [ ] "Monitoring tanda vital dan hemodinamik" — baris PERTAMA
- [ ] "Pantau urine output dan balance cairan" — baris KEDUA (pasien heart failure)
- [ ] Plan tambahan sesuai kebutuhan

## 9. PENUTUP
```
Tabe dokter, selanjutnya mohon arahannya dokter, terima kasih dokter.
```

## 10. FORMAT UMUM — FINAL CHECK
- [ ] Seluruh SOAP dibungkus ``` code block
- [ ] **Bold hanya untuk**: lokasi, nama pasien, EKG, Laboratorium, Foto Thorax, Echocardiography, *Mohon izin assess*, *Mohon izin terapi*, *Plan*
- [ ] **S: dan O: — TIDAK bold** (polos) — lihat referensi gold-standard-checklist-soap-igd.md item 63 dan 88
- [ ] Body/data/TTV/deskripsi/fisis **TIDAK bold**

REFERENSI: File asli gold standard dari dr. Hakim ada di references/gold-standard-checklist-soap-igd.md. Baca itu untuk verifikasi format persisnya.

## ⛔ PITFALLS FATAL
1. ❌ BUKAN code block
2. ❌ "Selamat pagi" — WAJIB "Assalamualaikum dokter"
3. ❌ TTV pakai TD/HR/RR/S/SpO2
4. ❌ (-)/(+) di fisis — WAJIB "tidak ada"
5. ❌ **Mengarang frekuensi/dosis obat — DILARANG**
6. ❌ **"tidak disebutkan"** di TTV/fisis
7. ❌ Header EKG/Lab/Foto/Echo kosong — LEWATKAN
8. ❌ **JVP asumsi R+2** — BACA input dokter
9. ❌ Nadi ditambah [reguler/ireguler] tanpa data
10. ❌ AF ditulis "Atrial Fibrillation" — tulis "Supraventricular Rhythm"
11. ❌ **Format obat "1x sehari"/"0-0-1"** — WAJIB format JAM
12. ❌ Obat rutin tanpa (obat di pasien)
13. ❌ Kirim SOAP sebagian
14. ❌ Body/fisis/data di-bold — hanya header yang bold
