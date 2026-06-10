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

## ⛔ TOP 10 KESALAHAN FATAL — DIBACA SEBELUM BUAT SOAP ⛔

### KONTEKS UMUM — Laporan Kelayakan Tindakan Non-Kardiak
Skill ini juga mencakup **laporan konsul kelayakan tindakan non-kardiak** (bronkoskopi, operasi, dll). Formatnya berbeda dari SOAP IGD biasa:

- **Pembukaan**: "Assalamualaikum dokter. Tabe dok, mohon izin melaporkan pasien konsul dari *[TS/Bagian]* di *@* atas nama:"
- **Header pasien**: `*[Tn./Ny.] [Nama] / [Umur] tahun / [DD-MM-YYYY] / RM [nomor]*`
- **Subtitle**: `_Pasien dikonsulkan untuk kelayakan [tindakan]_` (miring)
- **Body isi** mengikuti template laporan kelayakan di `references/template-kelayakan.md`
- **Tidak ada** bagian "Mohon izin assess/terapi" — penutup langsung: "Mohon arahan selanjutnya dokter. Terima kasih dokter."

> **CACHE CONTEXT**: Kamu sudah berkali-kali salah dan mempermalukan diri. Ini daftar kesalahan yang TIDAK BOLEH diulangi.

| # | Kesalahan | Yang BENAR |
|---|---|---|
| 1 | `*S:*` atau `*O:*` pakai bold | `S:` dan `O:` **POLOS** tanpa asterisk |
| 2 | `*A (Assessment):*` | `*Mohon izin kami assess dengan:*` |
| 3 | `*Terapi:*` | `*Mohon izin kami terapi dengan:*` |
| 4 | TTV berjejer pipe: `TD: 141/88 \| Nadi: 100` | Tiap baris baru, nama panjang: `Tekanan Darah:`, `Nadi:`, `Pernapasan:`, `Suhu:`, `Saturasi:` |
| 5 | TTV disingkat: `TD:`, `RR:`, `HR:` | `Tekanan Darah:`, `Pernapasan:`, `Nadi:` |
| 6 | `(-)` / `(+)` / `[-/+]` di fisis | Narasi: `tidak ada` / `ada` |
| 7 | Lab berjejer pipe: `WBC: 10 \| Hb: 12` | Tiap parameter baris sendiri |
| 8 | **LAB TIDAK DICANTUMKAN** (pakboss: "mana labnya tolol") | SELALU cantumkan `*Hasil Lab:*` meski kosong |
| 9 | EKG cuma 1-2 kata: `SVT, HR 136` | Sequential lengkap: Rhythm, HR, axis, P, PR, QRS, ST, T, kesan |
| 10 | Tidak pakai code block | SELALU bungkus SOAP di \`\`\` |
| **11** | **Meninggalkan '...' (placeholder/ellipsis)** di output — pakboss harus hapus manual | **ISI LANGUNG atau HAPUS**. Lab yang belum keluar: tulis "Hasil lab menyusul" di baris pertama. Lab yang sudah keluar tapi kosong: tulis "[parameter]: —". JANGAN pernah meninggalkan "..." untuk diisi manual |

### ATURAN BOLD SEKALI LAGI:
- 🟢 **PAKAI** `*...*`: lokasi pasien, nama pasien, EKG, Hasil Lab, Mohon izin assess, Mohon izin terapi, Plan
- 🔴 **JANGAN PAKAI** `*...*`: S, O, dan semua body/data/lab/TTV/deskripsi/fisis

### ATURAN OUTPUT:
- SELALU bungkus di \`\`\` (code block) agar asterisk literal saat dicopy ke WhatsApp

### CACHE — CONTOH EMAS (Kasus Ny. Nofri):
Lihat `references/kasus-05.md` untuk contoh format yang SUDAH VALID dan DITERIMA pakboss.

## Prinsip
- **1 sesi = 1 pasien** — tidak campur data antar pasien
- **Kumulatif** — setiap informasi baru ditambahkan ke SOAP yang sudah ada
- **Sumber input**: teks langsung, speech-to-text, foto hasil lab, PDF hasil lab
- Output selalu SOAP lengkap terbaru (bukan hanya delta/incremental)
- **Initial report = langsung full** — saat pakboss minta buatkan initial, buat SOAP lengkap dengan semua section (S, O, EKG, Lab, Foto Thorax, Laporan Tindakan/PCI, Echo Bedside, Echo Hemodinamik, Lung US, Assessment, dan **seluruh daftar terapi yang mungkin diberikan** — jangan cuma 1-2 item placeholder, tulis semua opsi terapi standar untuk diagnosis tersebut)
- **Echocardiography Bedside DIPISAHKAN** dari body Echo — di SKILL.md dan template, `Echocardiography Bedside` adalah heading mandiri (bukan bagian dari Echo section). Echo lengkap (Echo Bedside + Echo Hemodinamik + Lung US) akan dipindahkan ke skill terpisah nanti.
- Daftar terapi harus komprehensif — termasuk obat KP, lini pertama, lini kedua, dan terapi suportif yang relevan

---

## Template SOAP Baku

> **PENTING**: Pilih template spesifik berdasarkan keluhan utama pasien. Template lengkap tersimpan di `references/template-*.md`.
> Template generik di bawah HANYA digunakan sebagai fallback jika tidak ada template spesifik.
> **Initial report = full report** — saat pakboss minta "buatkan initial", outputkan SOAP dengan semua section terisi, termasuk daftar terapi lengkap (bukan placeholder). Jangan tanya "mau terapi apa?" — berikan opsi terapi standar untuk diagnosis tersebut.

### Panduan Memilih Template (Decision Tree)

| Keluhan Utama | DOE | PND/Orthopneu | Nyeri Dada | Kunci Tambahan | Template |
|---|---|---|---|---|---|
| Nyeri dada | (-) | (-) | Dominan, menjalar | ST elevasi regional | **ACS PPCI** |
| Nyeri dada | (-) | (-) | Dominan, menjalar | ST depresi/T inverted/non-diagnostik | **ACS Non-PPCI** |
| Nyeri dada | (+) | (-) | Tajam, pleuritik | Membaik duduk, demam, friction rub, ST difus + PR depresi | **Acute Pericarditis** |
| Sesak nafas | (+) | (+) | Hilang timbul | JVP R+3, ronkhi basal, edema | **Gagal Jantung** |
| Lemas, pingsan | (+) | (-) | Hilang timbul | Pusing, berdebar, nyeri ulu hati, AV block/SND | **Bradikardia** |
| **Berdebar/palpitasi** | *tergantung* | *tergantung* | *mungkin ada saat episode* | Pusing, nyeri ulu hati, mual, sinkop, neck pounding, onset akut/saat istirahat, denyut cepat | **Takiaritmia** |

Template tersedia di `references/`:
| Template | File |
|---|---|
| ACS Primary PCI | `template-acs-ppci.md` |
| ACS Non-PPCI | `template-acs-non-ppci.md` |
| Gagal Jantung | `template-gagal-jantung.md` |
| Bradikardia | `template-bradikardia.md` |
| Acute Pericarditis | `template-acute-pericarditis.md` | Nyeri dada pleuritik, membaik duduk membungkuk, ST elevasi difus + PR depresi, friction rub |
| Takiaritmia / Palpitasi | `template-takiaritmia.md` | Berdebar, SVT, WCT, VT, WPW, AF, Flutter — mencakup AVRT, AVNRT, VT, WPW syndrome |

> ⚠️ TEMPLATE LAMA DI ATAS SUDAH TIDAK DIGUNAKAN — lihat **Alur Kerja** di bawah untuk format SOAP terbaru yang sudah divalidasi.

---

## Pola Penting

### Diagnostik & Skoring
- STEMI: sertakan onset, KILLIP, TIMI risk score, fibrinolytic success/failed
- NSTEMI: sertakan GRACE score (risk %), ARC-HBR
- Heart Failure: klasifikasi (HFrEF/HFmrEF/HFpEF), profil hemodinamik (wet/dry, warm/cold)
- CKD/AKI: staging eGFR

### Terminologi Spesifik
- **KILLIP**: I-IV untuk stratifikasi STEMI
- **TIMI flow**: 0-3 post PCI
- **DOE**: Dyspnea on Effort
- **PND**: Paroxysmal Nocturnal Dyspnea
- **NRS**: Numeric Rating Scale (nyeri)
- **JVP**: Jugular Venous Pressure (R+... cmH2O)
- **CRT**: Capillary Refill Time
- **LVOT VTI**: Left Ventricular Outflow Tract Velocity Time Integral
- **TAPSE**: Tricuspid Annular Plane Systolic Excursion
- **eRAP**: estimated Right Atrial Pressure
- **SVR**: Systemic Vascular Resistance
- **CPO/CPI**: Cardiac Power Output/Index

### Obat & Singkatan
- **SP**: Syringe Pump
- **KP**: Kalau Perlu
- **IVFD**: Intravenous Fluid Drip
- **H-1/H-2/...**: Hari ke-1/2/... terapi

### Urutan Pemeriksaan Fisik
Mata → Leher (JVP) → Thorax (Paru) → Jantung → Abdomen → Ekstremitas

---

## Alur Kerja (WAJIB DIIKUTI SETIAP KALI MEMBUAT SOAP)

### CHECKLIST SEBELUM OUTPUT — Cocokkan dengan contoh kasus yang sudah divalidasi

```
☐ Pembukaan: "Selamat [pagi/siang/sore/malam] dokter. Tabe Dokter, mohon izin melaporkan pasien baru di [lokasi] atas nama:"
☐ Header: *[Tn./Ny.] [Nama] / [DD-MM-YYYY] / [Umur] tahun / RM [nomor]*
☐ S: — narasi paragraf kontinu, tiap item di baris bullet (-)
   ☐ Keluhan utama (onset, karakter, riwayat episode sebelumnya, gejala penyerta)
   ☐ Gejala lain (nyeri dada, sesak, dll — tulis "ada"/"tidak ada")
   ☐ Riwayat penyakit dahulu (HT, DM, merokok, keluarga) — masing-masing baris terpisah
☐ O:
   ☐ Tekanan Darah: ... mmHg
   ☐ Nadi: ... kali/menit [reguler/ireguler]
   ☐ Pernapasan: ... kali/menit
   ☐ Suhu: ...°C
   ☐ Saturasi: ...% [room air / on NC ... lpm]
   ☐ Pemeriksaan Fisis — TANPA judul "Pemeriksaan Fisis", langsung nama organ
      - Mata, Leher, Thorax, Jantung, Abdomen, Ekstremitas
      - TIDAK pakai (-)/(+), tulis "[temuan] tidak ada" / "[temuan] ada"
☐ EKG — TULIS LENGKAP sequential dalam 1 paragraf:
   ☐ Rhythm, HR, regular/ireguler, axis, P wave, PR interval, QRS duration, ST segment, T wave, kesan
   ☐ Kesan ada di baris terakhir
   ☐ Jika ada EKG sebelum dan sesudah (IGD + CVCU) — tulis keduanya
☐ Lab — WAJIB disertakan. Jika data belum ada, tulis "*Hasil Lab:* Hasil lab menyusul" sebagai satu baris. JANGAN buat daftar parameter dengan "..." — tidak ada effort untuk pakboss hapus manual.
☐ Foto Thorax — jika belum ada tulis "*(menunggu hasil)*"
☐ Echocardiography — jika belum ada tulis "*Echocardiography:* Menyusul"
☐ Mohon izin kami assess dengan: — tiap diagnosis di baris bullet
☐ Mohon izin kami terapi dengan: — tiap obat di baris bullet
   ☐ Format: [Obat] [dosis]/[frekuensi]/[rute]
   ☐ Obat yang sudah diberikan: tulis "— sudah diberikan"
☐ Plan: — tiap item di baris bullet
☐ Penutup: "Tabe dokter, mohon arahannya dokter, terima kasih dokter."
```

### 1. Pilih template yang sesuai
Gunakan decision tree di atas. Cek `references/index.md` untuk template yang tersedia.

### 2. Format Output SOAP IGD — WAJIB persis seperti ini urutannya (contoh validasi terbaru):

OUTPUT DI CODE BLOCK (\`\`\`) agar asterisk literal dan aman dicopy ke WA:

```
Selamat [pagi/siang/sore/malam] dokter. Tabe Dokter, mohon izin melaporkan pasien baru di *[lokasi] [bed/ruang]* atas nama:

*[Tn./Ny.] [Nama] / [DD-MM-YYYY] / [Umur] tahun / RM [nomor]*

S:
- [Narasi keluhan utama — onset, karakter, durasi, riwayat episode sebelumnya, gejala penyerta. Paragraf kontinu.]
[Gejala lain jika ada]
- Riwayat [penyakit] ada/tidak ada sejak ...
- Riwayat [penyakit lain] ada/tidak ada 

O:
Tekanan Darah: ... mmHg
Nadi: ... kali/menit [reguler/ireguler]
Pernapasan: ... kali/menit
Suhu: ...°C
Saturasi: ...% [room air / on NC ... lpm]

[Langsung nama organ tanpa judul — body polos]
Mata: konjungtiva pucat [tidak ada/ada], sklera ikterik [tidak ada/ada]
Leher: JVP [tidak disebutkan / R+... cmH2O]
Thorax: BP [vesikuler/...], ronkhi [tidak ada/ada], wheezing [tidak ada/ada]
Jantung: BJ I/II [murni/...], [reguler/ireguler], murmur [tidak ada/ada]
Abdomen: [datar/cembung], [supel/tegang], hepar/lien [tidak teraba/teraba], nyeri tekan [tidak ada/ada]
Ekstremitas: akral [hangat/dingin], edema [tidak ada/ada], CRT [<2/>2] detik

*EKG [lokasi] [tanggal]*
[Bacaan EKG sequential — 1 paragraf polos]

*EKG [lokasi lanjutan] [tanggal]* — jika ada
[Bacaan EKG kedua — polos]
Kesan: ... — polos

*Hasil Lab [tanggal/lokasi]:*
Hasil lab menyusul

*Mohon izin kami assess dengan:*
- [Diagnosis 1]
- [Diagnosis 2]

*Mohon izin kami terapi dengan:*
- [Obat] [dosis]/[frekuensi]/[rute] — sudah diberikan
- [Obat] [dosis]/[frekuensi]/[rute]

*Plan:*
- [Item plan 1]
- [Item plan 2]

Tabe dokter, mohon arahannya dokter, terima kasih dokter.
```

ATURAN BOLD:
- PAKAI asterisk (*): lokasi pasien, nama pasien, EKG, Hasil Lab, Mohon izin assess, Mohon izin terapi, Plan
- TANPA asterisk: S, O, dan semua body/data/lab/deskripsi
- WRAP DALAM CODE BLOCK: selalu bungkus SOAP di ``` agar asterisk literal saat dicopy ke WA

### 3. Aturan MENULIS EKG — WAJIB sequential, jangan diringkas:
Tulis seperti contoh: `Sinus Rhythm HR 53 bpm, regular, normoaksis, P wave 0.06 sec, PR Interval 0.16 sec, QRS Duration 0.10 sec, [temuan gelombang Q patologis], [ST segment], [T wave inversi], [aritmia/extra beat].` — dalam SATU PARAGRAF kontinu. Jangan dibuat per baris/bullet terpisah.

### 4. Aturan Pemeriksaan Fisis — TIDAK pakai (-)/(+) atau [-/+]
Gunakan narasi teks: "[temuan] tidak ada" / "[temuan] ada". Contoh: "ronkhi tidak ada", "edema tidak ada", "murmur tidak ada". Ikuti format contoh kasus 04 yang sudah divalidasi.

### 5. Format Assessment
Pakai `*Mohon izin kami assess dengan:*` — BUKAN `*A (Assessment):*`

### 6. Format Terapi
Pakai `*Mohon izin kami terapi dengan:*` — BUKAN `*Terapi:*`

### 7. Prinsip teks kontinu
- S adalah narasi paragraf kontinu per item (bukan data terstruktur)
- Lab ditulis tiap parameter baris baru (bukan pipe-separated `|`)
- EKG 1 paragraf kontinu

---

## Pitfalls

- **Jangan campur template**: Jangan gunakan kalimat dari template ACS untuk pasien gagal jantung (misal: "DOE (-), PND (-)" pada pasien HF yang seharusnya "(+)").
- **Jangan gunakan template generik kalau ada template spesifik**: Decision tree di atas wajib dicek dulu sebelum fallback.
- **S pasien rujukan wajib lengkap**: Diagnosis RS perujuk + lama rawat + terapi yang diberikan. Jangan skip ini.
- **Echo valves urutan baku**: Aorta → Mitral → Tricuspid → Pulmonal di template user. Ikuti urutan template user.
- **Jangan singkat nama DPJP**: Tulis nama lengkap sesuai `daftar-dpjp.md`. Contoh: "Dr.dr. Akhtar Fajar Muzakkir" BUKAN "Dr.dr. Akhtar Fajar M". Gelar subspesialis wajib lengkap (IKKV, EKO, dll).
- **Konsistensi format**: Nyeri dada pakai NRS (.../10). Echo selalu sertakan TEICH DAN BIPLANE. JVP selalu format "R+X cmH2O".
- **Echocardiography Bedside terpisah**: Echo Bedside, Echo Hemodinamik, dan Lung US tulis sebagai `[Menyusul — menggunakan skill Echocardiography terpisah]` di SOAP IGD. Isi echo detail akan dibuat menggunakan skill Echocardiography yang terpisah (belum dibuat).
- **Initial report jangan tanya "mau terapi apa?"**: Langsung berikan semua opsi terapi standar yang relevan. Termasuk obat KP, lini pertama, lini kedua, dosis, dan rute.
