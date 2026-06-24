---
name: soap-igd-jantung
description: Format SOAP baku pelaporan pasien IGD PJT Jantung. 1 sesi = 1 pasien. Setiap informasi baru memperbarui SOAP secara kumulatif.
triggers:
  - user melaporkan pasien baru IGD PJT
  - user memberikan update anamnesis/lab/echo/prosedur
  - user meminta perbarui SOAP
  - user memberikan foto hasil lab atau PDF
---

# SOAP IGD PJT Jantung

> ⚠️ FORMAT SOAP: Gunakan skill_view('soap-igd-golden-checklist') sebagai sumber format TERKINI.
> Skill ini menyimpan template kasus spesifik (ACS, HF, dll) dan image routing.
>
> Perbedaan kunci gold standard vs isi lama skill ini:
> - S: dan O: TIDAK bold (polos), bukan bold
> - Frekuensi obat format JAM (24 jam, 12 jam, 8 jam) — bukan "1x sehari"
> - Obat rutin ditulis (obat di pasien)
> - JVP: BACA dari input dokter — bukan asumsi R+2
> - TTV tidak disebut → isi dummy normal (120/80, 80x/mnt, 20x/mnt, 36.5°C, 98%)
> - EKG/Lab/Foto/Echo tanpa data → LEWATKAN section

## WAJIB — CHECKLIST

SEBELUM KIRIM CENTANG SEMUA. SETIAP KOREKSI CENTANG ULANG.

### CODE BLOCK
- [ ] Seluruh SOAP dalam ``` code block. Jangan tanya — langsung kirim.

### PEMBUKA
- [ ] "Assalamualaikum dokter" bukan "Selamat pagi"
- [ ] *Lokasi* bold, *Nama/TTL/umur/RM* bold

### DPJP
- [ ] DPJP italic underscore

### SUBJEKTIF [S] — WAJIB
- [ ] *S:* bold
- [ ] Keluhan utama + onset
- [ ] Keringat dingin, mual/muntah, sesak, berdebar, pusing — SATU PER SATU "ada"/"tidak ada"
- [ ] Obat rutin: "(obat di pasien): [daftar]"
- [ ] Faktor risiko: HT, DM, merokok, PJ keluarga — disebut satu per satu

### TTV [O]
- [ ] *O:* bold
- [ ] **Nadi tanpa [reguler/ireguler] jika dokter tidak menyebut**
- [ ] **DUMMY NORMAL (120/80, 80x/mnt, 20x/mnt, 36.5°C, 98%) jika TTV tidak disebut**
- [ ] PAKAI NILAI USER jika user beri data

### FISIS
- [ ] "tidak ada" bukan (-)/(+). Jangan "tidak disebutkan"
- [ ] **JVP: BACA INPUT DOKTER** — jangan asumsi R+2
- [ ] 6 sistem lengkap

### EKG
- [ ] **HANYA jika ada data/indikasi ACS. LEWATKAN jika tidak.**
- [ ] **Jangan "belum dikerjakan"**
- [ ] 1 baris sequential. AF → "Supraventricular Rhythm"

### LAB
- [ ] **HANYA jika ada data. LEWATKAN jika tidak.**
- [ ] **Jangan "belum dikerjakan"**
- [ ] Semua KOSONG. Jangan fiktif/—/...

### FOTO THORAX & ECHO
- [ ] **HANYA jika user menyebut. LEWATKAN jika tidak.**
- [ ] Jangan "belum dikerjakan"

### ASSESSMENT
- [ ] *Mohon izin kami assess dengan:* bold
- [ ] Diagnosis dipanjangkan

### TERAPI — KRITIS
- [ ] *Mohon izin kami terapi dengan:* bold
- [ ] IVFD BARIS PERTAMA
- [ ] **DILARANG MENGARANG FREKUENSI/DOSIS** — hanya data dokter
- [ ] Obat baru: [obat] [dosis]/[frekuensi]/[rute]
- [ ] Obat rutin: [obat] [dosis]/[rute] (obat di pasien)
- [ ] Dosis desimal pakai TITIK

### PLAN
- [ ] *Plan:* bold. Monitoring TTV baris pertama

### PENUTUP
Tabe dokter, selanjutnya mohon arahannya dokter, terima kasih dokter.

---

## PITFALLS UTAMA
1. CODE BLOCK terlewat
2. "Selamat pagi" / TD/HR/RR/S/SpO2
3. (-)/(+) → "tidak ada"
4. Lab diisi fiktif
5. EKG singkat
6. AF = Atrial Fibrillation → Supraventricular Rhythm
7. Singkatan diagnosis
8. ❌ **MENGARANG FREKUENSI/DOSIS OBAT**
9. ❌ **"tidak disebutkan"** — asumsi normal
10. ❌ **Header EKG/Lab/Foto/Echo kosong** — LEWATKAN
11. ❌ **JVP asumsi R+2** — baca input dokter
12. ❌ **Nadi [reguler/ireguler] karangan**
13. ❌ Obat tanpa (obat di pasien)
14. Soap sepotong-potong

## IMAGE INPUT
Gunakan mimo-vision.py untuk semua foto. Jangan pakai default model.