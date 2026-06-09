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

```
[Assalamualaikum wr wb./Selamat malam dokter,] tabe Dokter, mohon izin melaporkan pasien [baru/lanjutan] di *IGD PJT [Redzone bed X/...]* atas nama:

*[Tn./Ny.] [Nama]/[DD-MM-YYYY]/[Umur] tahun/RM [nomor]*

_DPJP Utama [dan Tindakan]: [dr./Dr.dr. Nama, Spesialis]_
_[asal rujukan + diagnosis rujukan jika ada]_

*S:*
- [Keluhan utama]: [onset], [memberat sejak], [karakteristik detail]
  - Nyeri dada: [lokasi], [onset], [kualitas], [penjalaran], [NRS], [faktor pencetus/peredah], [riwayat]
  - Sesak: [onset], DOE [ada/tidak], PND [ada/tidak], orthopneu [ada/tidak], [riwayat]
  - Berdebar: [ada/tidak], [riwayat]
- [Keluhan lain]: [batuk], [demam], [mual/muntah], [BAB/BAK], [keluhan spesifik lain]
- [Riwayat rawat di RS perujuk] — WAJIB jika pasien rujukan:
  - Diagnosis di RS perujuk: [apa]
  - Lama rawat: [X hari]
  - Terapi yang diberikan: [daftar obat + dosis + rute]
- [Riwayat kontrol di poli/RS sebelumnya — jika ada]

Faktor Risiko Kardiovaskular
- Riwayat Hipertensi: [ada/tidak, onset, keteraturan minum obat]
- Riwayat Diabetes Mellitus: [ada/tidak]
- Riwayat Merokok: [ada/tidak, durasi, jumlah, status berhenti]
- Riwayat Penyakit Jantung dalam keluarga: [ada/tidak, detail]

*O:*
[GCS/Kesadaran]
Tekanan Darah: [sistol/diastol] mmHg
Nadi: [x]/menit, [reguler/ireguler]
Nafas: [x]/menit
Suhu: [x.x]°C
SpO2: [x]% [room air/dengan O2] → [x]% [NRM/NC x lpm]

BB: [x] kg | TB: [x] cm
[BPJS kelas: X — jika ada]

Pemeriksaan Fisik
Mata: konjungtiva pucat tidak ada, sklera ikterik tidak ada
Leher: JVP (tidak disebutkan / R+... cmH2O)
Thorax: BP vesikuler, ronkhi tidak ada, wheezing tidak ada
Jantung: BJ I/II murni, reguler/ireguler, murmur tidak ada, gallop tidak ada
Abdomen: datar, supel, hepar/lien tidak teraba, nyeri tekan tidak ada
Ekstremitas: edema tidak ada, akral hangat, CRT <2 detik

*EKG [lokasi] ([tanggal]):*
Sinus Rhythm, HR [x] bpm, reguler, Normoaxis, P wave 0.06 S, PR interval 0.18 S, QRS Duration 0.06 S, [isi kesan Dokter sesuai arahan — format teks panjang kontinu, BUKAN bullet point]

*Laboratorium [lokasi] ([tanggal]):*
WBC: [x] | Hb: [x] | PLT: [x]
Neut/Lymph: [x]/[x]
[PT/INR/APTT: ...]
GDS: [x]
Na/K/Cl: [x]/[x]/[x]
Ureum/Kreatinin: [x]/[x] (eGFR [x])
SGOT/SGPT: [x]/[x]
HbsAg/Anti HCV: [reaktif/nonreaktif]
Hs Trop I: [x]
[Albumin: ...]
[AGD: pH, pO2, pCO2, HCO3, Laktat]
Kesan: [normal/abnormal...]

*Foto Thorax [lokasi] ([tanggal]):*
[Temuan]

*USG Abdomen [lokasi] ([tanggal]):*
[Temuan]

*Echocardiography [lokasi] ([tanggal]):*
1. LV Systolic Function: [Normal/Mildly/Moderately/Severely Abnormal], EF [x]% (TEICH), EF [x]% (BIPLANE)
2. RV Systolic Function: [Normal/Reduced], TAPSE [x] cm, S' lateral [x] cm/s
3. Cardiac Valves:
   - Mitral: [temuan]
   - Aorta: [temuan]
   - Tricuspid: [temuan]
   - Pulmonal: [temuan]
4. Cardiac Dimension: [deskripsi chamber] (LA mayor [x], LA minor [x], RA mayor [x], RA minor [x], LVIDd [x], RVDB [x], LA/Ao [x])
5. LV Geometry: [Normal/Concentric/Eccentric] LVH (LVMI [x] g/m2, RWT [x])
6. Regional Wall Motion: [Normokinetic/Hypokinetic/Akinetic/Dyskinetic] [segmen]
7. eRAP: [x] mmHg (IVC exp [x] cm, IVC insp [x] cm)
8. LV Diastolic Function: [Grade I/II/III, E/A, E', E/E']
9. Pericardial Effusion: [-/+]
10. [LV SEC, thrombus, dll...]

Conclusion:
[Ringkasan temuan echo]

Echo Hemodinamik:
TD: [x/x] mmHg | MAP: [x] mmHg | HR: [x] bpm
LVOT Diam: [x] cm | LVOT VTI: [x] cm
LVSV: [x] ml | LVCO: [x] L/min
eRAP: [x] mmHg | SVR: [x] dynes/sec/cm-5
BSA: [x] m2 | CI: [x] L/min/m2
CPO: [x] watt | CPI: [x] watt/m2

Lung Ultrasound:
Lung sliding (+), pleural line reguler, A-line well visualized, B-line (-), Regular and no thickening of pleural line, C-line (-). Pleural effusion (-), Pericardial effusion (-).

*Laporan PCI/Tindakan ([tanggal]):*
[Dominance, temuan per vessel, kesimpulan, hasil]

*Mohon izin kami assess dengan:*
- [Diagnosis 1] [skor/scoring relevan]
- [Diagnosis 2]
- [...]

*Mohon izin kami terapi dengan:*
- [Nama obat] [dosis]/[frekuensi]/[rute] [(KP/Tunda/...)]
- [...]

*Plan:*
- [Monitoring...]
- [Pemeriksaan...]
- [Konsul...]
- [Rencana rawat/pindah...]
- [...]

[Selanjutnya mohon arahan Dokter. Terima kasih Dokter. / Tabe dokter, mohon arahannya dokter, terima kasih dokter.]
```

---

## Pola Penting

### Diagnostik & Skoring
- STEMI: sertakan onset, KILLIP, fibrinolytic success/failed, TIMI score
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
☐ Lab — WAJIB disertakan sebagai template kosong jika data belum ada (tiap parameter baris baru):
   WBC: ...
   Hb: ...
   PLT: ...
   Neut/Lymph: .../...
   GDS: ...
   PT/INR/APTT: ...
   Na/K/Cl: ...
   Ureum/Kreatinin: .../...
   SGOT/SGPT: ...
   Hs Troponin I: ...
   (sesuaikan dengan layanan — selalu tuliskan lab yang belum diisi)
☐ Foto Thorax — jika belum ada tulis "(menunggu hasil)"
☐ Echocardiography — jika belum ada tulis kalau akan dilakukan
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
- Riwayat [penyakit lain] ada/tidak ada ...
- ... 

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
WBC: ...
Hb: ...
PLT: ...
Neut/Lymph: .../...
GDS: ...
PT/INR/APTT: ...
Na/K/Cl: ...
Ureum/Kreatinin: .../...
SGOT/SGPT: ...
Hs Troponin I: ...

*Mohon izin kami assess dengan:*
- [Diagnosis 1]
- [Diagnosis 2]
- [...]

*Mohon izin kami terapi dengan:*
- [Obat] [dosis]/[frekuensi]/[rute] — [sudah diberikan / ...]
- [Obat] [dosis]/[frekuensi]/[rute]
- [...]

*Plan:*
- [...]
- [...]
- [...]

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
- Lab ditulis dalam 1-3 baris dengan pipe separator
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
