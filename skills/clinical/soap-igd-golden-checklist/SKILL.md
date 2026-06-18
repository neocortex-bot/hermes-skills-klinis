---
name: soap-igd-golden-checklist
description: GOLDEN CHECKLIST WAJIB — SOAP IGD format baku, tidak boleh ada 1 item pun terlewat. Berlaku untuk semua kasus IGD PJT Jantung. Setiap SOAP WAJIB centang SEMUA item sebelum kirim.
triggers:
  - user minta buat SOAP IGD
  - user kasih data pasien baru IGD
  - user koreksi SOAP
  - user minta golden checklist
  - user bilang "HARAMM!!" atau "jangan ada terlewat"
---

# ⛔ SOAP IGD — GOLDEN CHECKLIST WAJIB ⛔

## ATURAN UTAMA
1. **SETIAP SOAP WAJIB dibungkus dalam ``` code block** — jangan pernah kirim sebagai teks biasa
2. **SETIAP ITEM DI BAWAH INI WAJIB DICENTANG SATU PER SATU** sebelum mengirim
3. **SETIAP ADA KOREKSI/KESALAHAN → CENTANG ULANG SEMUA CHECKLIST**
4. **JANGAN KIRIM SEBAGIAN** — SOAP harus lengkap langsung satu kali kirim
5. **JANGAN KOSONGKAN SECTION** — isi "Menyusul" hanya untuk Echo dan Foto Thorax. Lab dikosongkan (tanpa nilai, tanpa "—", tanpa "...").

---

## ⚡ FORMAT LENGKAP — GOLD STANDARD
```
Assalamualaikum dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *[LOKASI]* atas nama:

*Tn./Ny. [NAMA LENGKAP] / [DD-MM-YYYY] / [UMUR] tahun / RM [NOMOR RM]*

_DPJP Utama: dr. [Nama], Sp.JP, Subsp. ..._
_DPJP Tindakan: dr. [Nama], Sp.JP, Subsp. ..._

_Pasien dirujuk dari [RS ASAL] dengan diagnosis [DIAGNOSIS LENGKAP — dipanjangkan, tidak disingkat]_

*S:*
- [Keluhan utama: onset, lokasi, karakter 3 kriteria tipikal (retrosternal/nyeri dada kiri, terasa berat/ditekan, menjalar ke lengan kiri/rahang/punggung), penjalaran, skala nyeri NRS]
- [Gejala penyerta — WAJIB disebut SATU PER SATU: keringat dingin ada/tidak ada, mual muntah ada/tidak ada, sesak nafas ada/tidak ada, berdebar ada/tidak ada, pusing ada/tidak ada]
- [Riwayat PCI/operasi jantung: tahun, RS, jumlah stent — dengan narasi lengkap bila ada]
- Pasien telah mendapat terapi dari RS rujukan: [Obat injeksi/subkutan dosis / interval jam / route], [Oral cukup sediaan saja]
- Faktor Risiko Kardiovaskular:
  - Riwayat Hipertensi: [sejak kapan, berobat rutin/tidak, obat apa]
  - Riwayat DM: [sejak kapan, berobat rutin/tidak, obat apa]
  - Riwayat merokok: [ada/tidak, sejak berapa tahun, berapa batang/hari, sudah berhenti — berapa lama]
  - Riwayat PJ keluarga: [ada/tidak, sebutkan siapa — hubungan sedarah]

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
[GCS: ... — bila tidak compos mentis]

*EKG [LOKASI] (DD-MM-YYYY):*
[1 baris sequential: Rhythm, HR .. bpm, reguler/ireguler, Axis, P wave .. sec, PR interval .. sec, QRS Duration .. sec, ST segment/T wave changes]

*Laboratorium [LOKASI] (DD-MM-YYYY):*
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
[Bilirubin Total/Direk — bila perlu]
[Albumin — bila perlu]

*Foto Thorax [LOKASI] (DD-MM-YYYY):*
Menyusul

*Echocardiography (DD-MM-YYYY):*
Menyusul

*Mohon izin kami assess dengan:*
- [Diagnosis utama + stratifikasi risiko lengkap]

*Mohon izin kami terapi dengan:*
- [Obat] [dosis]/[frekuensi]/[rute]

*Plan:*
- Monitoring tanda vital dan hemodinamik
- [Pantau urine output dan balance cairan — untuk pasien heart failure]
- [Plan lain sesuai kasus]

Tabe dokter, selanjutnya mohon arahannya dokter, terima kasih dokter.
```

---

## 📋 GOLDEN CHECKLIST — 100 ITEM

### A. PEMBUKA — 6 ITEM
- [ ] **CODE BLOCK**: Seluruh SOAP dibungkus ``` code block
- [ ] **Pembukaan**: "Assalamualaikum dokter" (BUKAN "Selamat pagi/siang/malam")
- [ ] **Lokasi bold**: *[Lokasi]* di bold — contoh *IGD PJT Redzone*
- [ ] **Nama bold**: Nama pasien di bold
- [ ] **TTL bold**: Tanggal lahir DD-MM-YYYY di bold
- [ ] **RM bold**: Nomor RM di bold

### B. DPJP — 4 ITEM
- [ ] **DPJP Utama**: Baris terpisah dengan _underscore italic_
- [ ] **Nama lengkap DPJP**: Tidak disingkat, gelar lengkap
- [ ] **DPJP Tindakan**: Baris terpisah bila beda orang dengan DPJP Utama
- [ ] **Singkat jika 1 orang**: "DPJP Utama dan Tindakan: dr. ..." bila 1 orang saja

### C. RUJUKAN — 3 ITEM
- [ ] **Header rujukan**: _Pasien dirujuk dari [RS] dengan diagnosis [diagnosis]_
- [ ] **Nama RS rujukan**: Jelas
- [ ] **Diagnosis rujukan DIPANJANGKAN**: Tidak disingkat dari input user

### D. SUBJEKTIF [S] — 15 ITEM
- [ ] **S: bold**: *S:* — format bold
- [ ] **Keluhan utama**: Onset JELAS (berapa jam/hari sebelum masuk)
- [ ] **Karakter nyeri TIPIKAL**: 3 kriteria dipanjangkan — retrosternal/nyeri dada kiri, terasa berat/ditekan, menjalar
- [ ] **Penjalaran**: Disebut (lengan kiri/rahang/punggung/tidak menjalar)
- [ ] **Skala nyeri**: NRS (0-10)
- [ ] **Keringat dingin**: Ada/tidak ada — HARUS disebut, TIDAK BOLEH DILEWATKAN
- [ ] **Mual/muntah**: Ada/tidak ada — HARUS disebut
- [ ] **Sesak nafas**: Ada/tidak ada, DOE/PND/Orthopneu — HARUS disebut
- [ ] **Berdebar**: Ada/tidak ada — HARUS disebut
- [ ] **Pusing**: Ada/tidak ada — HARUS disebut
- [ ] **Riwayat PCI/operasi jantung**: Tahun, RS, jumlah stent — narasi lengkap bila ada. Bila tidak ada, tulis "tidak ada"
- [ ] **Terapi RS rujukan**: Injeksi/subkutan [dosis]/[interval jam]/[route]. Oral cukup sediaan. Bila tidak ada rujukan → tulis "Pasien datang langsung"
- [ ] **Riwayat Hipertensi**: Sejak kapan, berobat rutin/tidak, obat apa. Bila tidak ada → tulis "tidak ada"
- [ ] **Riwayat DM**: Sejak kapan, berobat rutin/tidak, obat apa. Bila tidak ada → tulis "tidak ada"
- [ ] **Riwayat merokok/PJ keluarga**: Merokok: ada/tidak, sejak kapan, berapa btg/hari, sudah berhenti — berapa lama. PJ keluarga: ada/tidak, siapa. Bila tidak ada → tulis "tidak ada"

### E. TTV — 8 ITEM
- [ ] **O: bold**: *O:* — format bold
- [ ] **Tekanan Darah**: ... mmHg (BUKAN "TD")
- [ ] **Nadi**: ... kali/menit + [reguler/ireguler] (BUKAN "HR" atau "N")
- [ ] **Pernapasan**: ... kali/menit (BUKAN "RR")
- [ ] **Suhu**: ...°C (BUKAN "S")
- [ ] **Saturasi**: ...% + [room air / on NC ... lpm] (BUKAN "SpO2")
- [ ] **Format per baris**: Masing-masing TTV di baris sendiri
- [ ] **Hanya data yang disebut**: Jangan isi nilai fiktif

### F. PEMERIKSAAN FISIS — 9 ITEM
- [ ] **Mata**: konjungtiva tidak anemis, sklera tidak ikterik (BUKAN (-)/(+))
- [ ] **Leher**: JVP R+2 cmH2O dalam batas normal (BUKAN (-)/(+))
- [ ] **Thorax paru**: BP vesikuler, ronkhi tidak ada, wheezing tidak ada (BUKAN (-)/(+))
- [ ] **Jantung**: BJ I/II murni reguler, murmur tidak ada (BUKAN (-)/(+))
- [ ] **Abdomen**: datar, supel, hepar dan lien tidak teraba, nyeri tekan tidak ada (BUKAN (-)/(+))
- [ ] **Ekstremitas**: akral teraba hangat, edema tidak ada, CRT < 2 detik (BUKAN (-)/(+))
- [ ] **GCS**: Bila tidak compos mentis — sebutkan E4V5M6 atau nilai aktual
- [ ] **Semua "tidak ada"/"ada"**: BUKAN simbol (-) atau (+)
- [ ] **Tidak ada kata "tidak disebutkan"**: Asumsikan normal jika tidak diinput abnormal

### G. EKG — 8 ITEM
- [ ] **Header bold**: *EKG [LOKASI] (DD-MM-YYYY):* — di bold, tanggal sesuai hari SOAP
- [ ] **1 baris SEQUENTIAL**: Satu baris panjang, bukan bullet
- [ ] **Rhythm**: Disebut (Sinus/Atrial Fibrilasi/Supraventricular Rhythm/dll)
- [ ] **HR**: .. bpm
- [ ] **Reguler/ireguler**: Jelas
- [ ] **Axis**: Normoaxis/Left Axis Deviation/Right Axis Deviation
- [ ] **P wave, PR interval, QRS Duration**: Default 0.08, 0.16, 0.08 sec bila tidak diketahui
- [ ] **KONSISTENSI ST-T**: Jika T inverted / ST elevasi/depresi → ST segment BUKAN "no significant changes"
- [ ] **Catatan AF**: Irama ditulis "Supraventricular Rhythm" (BUKAN Atrial Fibrillation)

### H. LABORATORIUM — 13 ITEM
- [ ] **Header bold**: *Laboratorium [LOKASI] (DD-MM-YYYY):* — di bold, tanggal sesuai hari SOAP
- [ ] **Hemoglobin**: KOSONGKAN (jangan isi fiktif)
- [ ] **Leukosit**: KOSONGKAN
- [ ] **Trombosit**: KOSONGKAN
- [ ] **Neut/Lymp**: KOSONGKAN
- [ ] **PT/INR/APTT**: KOSONGKAN
- [ ] **Glukosa Darah Sewaktu**: KOSONGKAN
- [ ] **Ureum/Kreatinin**: KOSONGKAN
- [ ] **GOT/GPT**: KOSONGKAN
- [ ] **Na/K/Cl**: KOSONGKAN
- [ ] **Troponin I**: KOSONGKAN
- [ ] **HBsAg/Anti HCV**: KOSONGKAN
- [ ] **TAMBAHAN**: Bilirubin, Albumin bila perlu — KOSONGKAN
- [ ] **LARANGAN**: Jangan isi "—", jangan "..." , jangan isi nilai palsu. KOSONGKAN total kolom nilainya

### I. FOTO THORAX — 2 ITEM
- [ ] **Header bold**: *Foto Thorax [LOKASI] (DD-MM-YYYY):*
- [ ] **Isi**: "Menyusul" (kecuali hasil sudah ada)

### J. ECHOCARDIOGRAPHY — 3 ITEM
- [ ] **Header bold**: *Echocardiography (DD-MM-YYYY):*
- [ ] **Isi**: "Menyusul" atau output skill echocardiography-igd (tanpa asterisk/bold, tanpa bullet "-")
- [ ] **Tanggal**: Sesuai hari SOAP (kecuali user beri tanggal berbeda)

### K. ASSESSMENT [A] — 5 ITEM
- [ ] **Header bold**: *Mohon izin kami assess dengan:* — di bold
- [ ] **STEMI**: [Regio wall] + [Onset] + [KILLIP I-IV] + (TIMI Score .. Estimated 30 day mortality ..%, ARC HBR .. Major .. Minor)
- [ ] **NSTEMI**: NSTEMI [risk] (GRACE Score .. point ..% probability of death, ARC-HBR .. mayor .. minor)
- [ ] **Diagnosis tambahan**: Sebutkan bila ada (HHD, CAD, DM, dll)
- [ ] **Singkatan dipanjangkan**: Semua diagnosis ditulis LENGKAP

### L. TERAPI [P1] — 6 ITEM
- [ ] **Header bold**: *Mohon izin kami terapi dengan:* — di bold
- [ ] **IVFD di baris PERTAMA**: Baris terapi paling pertama
- [ ] **Format OBAT**: `[Obat] [dosis]/[frekuensi]/[rute]` — KONSISTEN semua baris dengan slash
- [ ] **Dosis desimal pakai TITIK**: 1.25 mg (BUKAN 1,25 mg)
- [ ] **Jangan tambahan**: "(lanjut)", "(selesai)", "(KP)", atau keterangan lain di belakang obat
- [ ] **Pisah baris per obat**: Setiap obat di baris terpisah dengan "-" bullet

### M. PLAN [P2] — 3 ITEM
- [ ] **Header bold**: *Plan:* — di bold
- [ ] **Monitoring TTV**: "Monitoring tanda vital dan hemodinamik" — baris pertama plan
- [ ] **Plan tambahan**: Sesuai kasus (EKG per hari, cek APTT, cek lab, konsul, pindah rawat, dll)

### N. PENUTUP — 1 ITEM
- [ ] **Penutup**: "Tabe dokter, selanjutnya mohon arahannya dokter, terima kasih dokter."

---

## 🎯 TEMPLATE ASSESSMENT PER KASUS

### STEMI — kandidat PPCI
```
- STEMI [Anteroseptal/Anterior/Inferior/dll] wall, onset [X] jam, KILLIP [I-IV] (TIMI Score .. Estimated 30 day mortality ..%, ARC HBR .. Major .. Minor)
- CAD
- [Diagnosis tambahan]
```

### NSTEMI
```
- NSTEMI [Very high risk / High risk / Intermediate risk] (GRACE Score .. point ..% probability of death, ARC-HBR .. mayor .. minor)
- CAD
- [Diagnosis tambahan]
```

### UAP (Unstable Angina Pectoris)
```
- UAP [Very high risk / High risk / Intermediate risk] (GRACE Score .. point ..% probability of death, ARC-HBR .. mayor .. minor)
- CAD
- [Diagnosis tambahan]
```

### Acute Heart Failure
```
- Acute Heart Failure [tipe: ADHF/De novo/ACS related] + [NYHA III/IV] + (EF: ...%)
- [Etiologi: CAD/HHD/CM dll]
- [Diagnosis tambahan]
```

---

## ⛔ PITFALLS FATAL — JANGAN PERNAH

1. **❌ CODE BLOCK TERLUPA** — Hukuman: user akan koreksi "mana code block"
2. **❌ "Selamat pagi"** — WAJIB "Assalamualaikum dokter"
3. **❌ TTV pakai "TD", "HR", "RR", "S", "SpO2"** — WAJIB "Tekanan Darah", "Nadi", "Pernapasan", "Suhu", "Saturasi"
4. **❌ Fisis pakai (-)/(+)** — WAJIB "tidak ada"/"ada"
5. **❌ Nilai fiktif/halusinasi lab** — Lab WAJIB KOSONG jika belum ada hasil
6. **❌ EKG dari user ditulis singkat** — WAJIB dipanjangkan ke format sequential 1 baris
7. **❌ ST-T inconsistency** — T inverted → ST segment BUKAN "no significant changes"
8. **❌ AF ditulis "Atrial Fibrillation"** — WAJIB "Supraventricular Rhythm"
9. **❌ Singkatan di diagnosis rujukan** — WAJIB dipanjangkan
10. **❌ Format obat pakai koma desimal** — WAJIB 1.25 mg (bukan 1,25)
11. **❌ Obat ditulis "(lanjut)"** — Hanya format [dosis]/[frekuensi]/[rute]
12. **❌ "tidak disebutkan" di fisis** — WAJIB asumsikan normal
13. **❌ Dosis pakai spasi berantakan** — Konsisten: [obat] [dosis]/[frekuensi]/[rute]
14. **❌ Tanggal EKG/Lab pakai tanggal lama** — WAJIB tanggal hari SOAP dibuat, kecuali user tentukan lain
15. **❌ Kirim SOAP sebagian** — WAJIB lengkap dalam 1 kali kirim

---

## ✅ VERIFIKASI AKHIR (SEBELUM KIRIM)

Baca ulang SOAP dan pastikan:
1. ✅ Pembukaan "Assalamualaikum dokter"
2. ✅ Lokasi di bold
3. ✅ Nama/umur/RM di bold
4. ✅ DPJP italic underscore
5. ✅ Rujukan: nama RS + diagnosis panjang
6. ✅ *S:* bold — semua gejala penyerta disebut satu per satu
7. ✅ *O:* bold — TTV per baris, fisis "tidak ada"
8. ✅ EKG: 1 baris sequential lengkap + konsistensi ST-T
9. ✅ Lab: **KOSONG** — jangan isi nilai
10. ✅ Echo/Foto Thorax: "Menyusul"
11. ✅ *Mohon izin kami assess dengan:* bold — stratifikasi risiko lengkap
12. ✅ *Mohon izin kami terapi dengan:* bold — IVFD baris pertama
13. ✅ *Plan:* bold — Monitoring TTV baris pertama
14. ✅ Penutup sesuai
15. ✅ **CODE BLOCK ```** — WAJIB
