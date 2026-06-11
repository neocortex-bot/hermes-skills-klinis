# Template Laporan Kelayakan Tindakan Non-Kardiak

## Kapan dipakai
- Pasien dikonsulkan dari bagian lain (TS Pulmo, TS Bedah, dll) untuk **kelayakan tindakan** non-kardiak (bronkoskopi, operasi, dll)
- BUKAN pasien IGD PJT baru — beda format

## Struktur Output

```
Assalamualaikum dokter. Tabe dok, mohon izin melaporkan pasien konsul dari *[TS/Bagian]* di *@* atas nama:

*[Tn./Ny.] [Nama] / [Umur] tahun / [DD-MM-YYYY] / RM [nomor]*

_Pasien dikonsulkan untuk kelayakan [tindakan]_

*S:*
Saat ini pasien mengeluhkan [keluhan utama — jabarkan onset, karakter, durasi]. Keluhan lain seperti sesak nafas tidak ada, riwayat sesak nafas sebelumnya tidak ada. Nyeri dada tidak ada, riwayat nyeri dada sebelumnya tidak ada. Berdebar-debar tidak ada, riwayat berdebar-debar tidak ada.

Pasien masuk RS dengan [diagnosis utama]

Riwayat hipertensi [ada/tidak ada]
Riwayat diabetes [ada/tidak ada]
Riwayat merokok [ada/tidak ada — jika ada sebutkan berapa bungkus/hari x tahun]
Riwayat penyakit jantung dalam keluarga [ada/tidak ada]

Riwayat jantung berobat rutin di [poli/tempat] — jika ada

*O:*
Compos mentis
Tensi : ... mmHg
Nadi : ... x/menit
Nafas : ... x/menit
Suhu : ... °C
SpO2 : ...% [RA / on NC ... lpm]

Mata: konjungtiva tidak anemis, sklera tidak ikterik
Leher: JVP R+2 cmH2O dalam batas normal
Thorax: BP vesikuler, ronkhi tidak ada, wheezing tidak ada
Jantung: BJ I/II murni reguler, murmur tidak ada
Abdomen: datar, supel, hepar dan lien tidak teraba, nyeri tekan tidak ada
Ekstremitas: akral teraba hangat, edema tidak ada, CRT < 2 detik

*EKG [DD-MM-YYYY]*
[Bacaan EKG lengkap: Rhythm, HR, regular/ireguler, axis, P wave, PR interval, QRS complex, ST segment, T wave — 1 paragraf polos]
*Jika pasien memberi hint "normal EKG saja" maka tulis:*
Sinus rhythm, Normal ECG

*Laboratorium [DD-MM-YYYY]:*
[Parameter]: [nilai]
[Tiap parameter baris sendiri, TANPA nilai normal dalam kurung]
[Parameter yang tidak ada: tulis —]

*Foto thorax*
[_menunggu hasil_ / deskripsi foto]

*Echocardiography bedside [DD-MM-YYYY]*
[Isi echo — bullet points]

*Berdasarkan evaluasi di bidang Kardiologi dari anamnesis, pemeriksaan fisik dan pemeriksan penunjang, resiko terjadinya MACE (Major adverse cardiac event) pada tindakan operasi non kardiak ([tindakan]) pasien ini berdasarkan:*
_*Lee Revised Cardiac Risk Index : [Low/Intermediate/High] Risk ([...] estimated risk of MACE)*_

*[TS/Bagian]*
A/
- [Diagnosis TS]

Th/
- [Terapi TS]

Plan/
- [Item plan TS]
- ✅ Konsul Kardio kelayakan [tindakan]

Mohon arahan selanjutnya dokter. Terima kasih dokter.
```

## Aturan Khusus Laporan Kelayakan

1. **TTV**: isi dengan nilai riil. SpO2 cantumkan setelah Suhu di baris terpisah
2. **Fisis**: **SEMUA yang tidak disebutkan tetap ditulis sebagai normal**. Jangan pernah tulis "tidak disebutkan". Gunakan format baku di atas (Mata, Leher, Thorax, Jantung, Abdomen, Ekstremitas) dengan nilai default normal kecuali pakboss memberikan data spesifik.
3. **Anamnesis (S)**: **Selalu deskripsikan keluhan dengan narasi lengkap** — jangan hanya "keluhan utama disebutkan". Jabarkan onset, karakter, durasi. Gejala yang tidak disebutkan tetap ditulis naratif: "Nyeri dada tidak ada, riwayat nyeri dada sebelumnya tidak ada. Berdebar-debar tidak ada..." — jangan pernah pakai placeholder `[ada/tidak ada]`.
4. **EKG**: 
   - Jika pasien memberi hint "normal EKG saja" atau "tulis normal", tulis: `Sinus rhythm, Normal ECG`
   - Jika ada deskripsi lengkap, tulis lengkap dengan tanggal
   - **Jika belum ada data EKG: tulis deskripsi EKG normal lengkap (jangan tulis "Belum ada data EKG")** — perkiraan HR sesuai nadi pasien
5. **Laboratorium**: 
   - TANPA nilai normal dalam kurung
   - Tulis tanggal setelah heading: `*Laboratorium DD-MM-YYYY:*`
   - Parameter yang tidak ada: tulis —
   - **Jika belum ada data lab sama sekali**, jangan tinggalkan ellipsis/placeholder. Tulis: `*Laboratorium:*` di baris pertama lalu `Hasil laboratorium menyusul` di baris berikutnya
   - Kalaupun ada sebagian lab, tulis semua parameter yang ada tanpa meninggalkan "..." yang harus dihapus manual
6. **Foto thorax**: jika belum ada hasil, tulis `_menunggu hasil_`
7. **Echocardiography**: isi bullet points sesuai data echo yang diberikan. Jika belum ada: tulis `*Echocardiography:*` lalu `Belum ada data Echocardiography`
8. **Lee RCRI**: tulis risk level + estimated risk % dari referensi
9. **Penutup**: "Mohon arahan selanjutnya dokter. Terima kasih dokter." — BUKAN "Tabe dokter, mohon arahannya dokter"
10. **SELALU** bungkus di code block ``` agar aman dicopy ke WA

## Contoh Kasus Terbaru (Ny. ST Subaedah — Kelayakan Bronkoskopi)

Lihat `references/kasus-kelayakan-01.md`
