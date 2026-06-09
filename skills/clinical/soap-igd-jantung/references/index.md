# Indeks Kasus Referensi SOAP IGD PJT

## Format penamaan
Setiap kasus disimpan di `references/kasus-XX.md` dengan XX = nomor urut.
Gunakan kata kunci di bawah untuk mencari kasus yang mirip.

---

| # | Pasien | RM | Bed | DPJP | Diagnosis Utama | Kata Kunci |
|---|---|---|---|---|---|---|
| 01 | Tn. Irwan (51) | 1650487 | Redzone 6 | Dr.dr. Akhtar Fajar Muzakkir, Sp.JP(K) | STEMI Extensive Anterior KILLIP II post Failed Fibrinolytic → CAD 2VD post PCI 1 DES LAD | STEMI, anterior, fibrinolytic failed, PCI, LAD, 2VD, KILLIP II, TIMI 3, AKI, HFmrEF, nefrolithiasis |
| 02 | Ny. Zoar Naim (50) | 0808547 | Bed 1 | dr. Pendrik Tandean, Sp.PD-KKV | Total AV Block with Junctional Escape Rhythm + CAP | TAVB, bradikardi, symptomatic, junctional escape, TPM, sick sinus, pneumonia, CAP |
| 03 | Ny. Salma (57) | 1522083 | Redzone 6 | Dr.dr. Abdul Hakim Alkatiri, Sp.JP(K) | ADHF Wet-Warm + Severe MR/TR/PR + AKI on CKD | ADHF, wet-warm, multivalvular, severe MR, severe TR, ascites, CKD, hyponatremia, hypoalbumin |
| 04 | Tn. Arief Mahrus (52) | 1650126 | Redzone 6 | dr. Pendrik Tandean, Sp.PD-KKV / dr. Muh Asrul Apris Sp.JP(K) | NSTEMI High Risk + post VT + HFrEF + CAP | NSTEMI, GRACE 98, VT, amiodarone, HFrEF, CAP, pleural effusion, invasive strategy, VES bigeminy |

## Template SOAP

| Template | File | Keterangan |
|---|---|---|
| ACS Primary PCI | `template-acs-ppci.md` | ACS kandidat PPCI — S&O identik Non-PPCI, beda di A (STEMI) & Plan |
| ACS Non-PPCI | `template-acs-non-ppci.md` | Pasien ACS bukan kandidat primary PCI |
| Gagal Jantung | `template-gagal-jantung.md` | Pasien dengan keluhan utama sesak nafas/gagal jantung, DPJP tentative dr. Aussie |
| Bradikardia | `template-bradikardia.md` | Pasien dengan keluhan lemas/pingsan, bradikardia simtomatik (TAVB, SND, sinus arrest), DPJP tentative dr. Aussie |
| Acute Pericarditis | `template-acute-pericarditis.md` | Nyeri dada pleuritik, membaik duduk membungkuk, ST elevasi difus + PR depresi, friction rub |

Template berikutnya akan ditambahkan sesuai arahan Dokter.

## Rencana Input Visual
- **Foto rujukan**: difoto → OCR → masuk ke S section (riwayat RS perujuk)
- **Foto barcode pasien**: difoto → model visual → ekstrak Nama, TTL, RM → masuk header SOAP
