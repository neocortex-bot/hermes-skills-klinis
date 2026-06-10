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
Saat ini memiliki keluhan berupa sesak nafas [ada/tidak ada], riwayat sesak nafas [ada/tidak ada]
Nyeri dada [ada/tidak ada], riwayat nyeri dada sebelumnya [ada/tidak ada]. 
Berdebar-debar [ada/tidak ada], riwayat berdebar-debar [ada/tidak ada]. 

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

Anemis [tidak ada/ada], ikterus [tidak ada/ada]
JVP [R+... cmH2O / tidak disebutkan]
BJ I/II murni reguler, murmur [tidak ada/ada]
BP Vesikuler, ronkhi [tidak ada/ada], wheezing [tidak ada/ada]
Edema ekstremitas inferior [tidak ada/ada], akral teraba [hangat/dingin]

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
2. **EKG**: 
   - Jika pasien memberi hint "normal EKG saja" atau "tulis normal", tulis: `Sinus rhythm, Normal ECG`
   - Jika ada deskripsi lengkap, tulis lengkap dengan tanggal
3. **Laboratorium**: 
   - TANPA nilai normal dalam kurung
   - Tulis tanggal setelah heading: `*Laboratorium DD-MM-YYYY:*`
   - Parameter menyusul / tidak ada: tulis —
4. **Foto thorax**: jika belum ada hasil, tulis `_menunggu hasil_`
5. **Echocardiography**: isi bullet points sesuai data echo yang diberikan
6. **Lee RCRI**: tulis risk level + estimated risk % dari referensi
7. **Penutup**: "Mohon arahan selanjutnya dokter. Terima kasih dokter." — BUKAN "Tabe dokter, mohon arahannya dokter"
8. **SELALU** bungkus di code block ``` agar aman dicopy ke WA

## Contoh Kasus Terbaru (Ny. ST Subaedah — Kelayakan Bronkoskopi)

Lihat `references/kasus-kelayakan-01.md`
