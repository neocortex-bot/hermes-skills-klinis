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
- Mata: konjungtiva pucat [-/+], sklera ikterik [-/+]
- Leher: JVP R+[x] cmH2O
- Thorax: BP [vesikuler/...], ronkhi [lokasi] [-/+], wheezing [-/+]
- Jantung: BJ I/II [murni/...] [reguler/ireguler], murmur [-/+], [gallop]
- Abdomen: [datar/cembung], [supel/tegang], hepar/lien [teraba/tidak], nyeri tekan [-/+], BU [normal/...]
- Ekstremitas: edema [-/+], akral [hangat/dingin], CRT [<2/>2] detik

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

## Alur Kerja
1. User memberikan informasi pasien (bisa berupa teks, foto lab, PDF)
2. **Tentukan tipe/jenis pasien** — cek `references/index.md` untuk template yang tersedia
3. **Pilih template yang sesuai** dari `references/template-*.md`
4. Jika sesi baru (pasien baru): buat SOAP dari template yang sesuai
5. Jika pasien yang sama: **perbarui** SOAP dengan data baru, pertahankan data lama
6. Selalu tampilkan **SOAP LENGKAP terbaru** setelah setiap update
7. Data lab/echo/prosedur yang baru menggantikan/melengkapi yang lama
8. Jika ada data yang bertentangan, gunakan yang terbaru dan beri catatan perubahan
9. Untuk mencari referensi kasus sebelumnya: cocokkan dengan kata kunci di `references/index.md`

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
