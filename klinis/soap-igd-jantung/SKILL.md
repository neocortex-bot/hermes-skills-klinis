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

### ⛔ CHECKLIST 0 — KIRIM WAJIB CODE BLOCK
- [ ] **Seluruh SOAP WAJIB dibungkus dalam \`\`\` code block** — jangan kirim sebagai teks biasa
- [ ] Jangan tanya/konfirmasi dulu ke user — langsung kirim dalam code block
- [ ] Jika lupa, user akan koreksi "mana code block" — ini PITFALL berat

---

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

<<<<<<< HEAD
### FOTO THORAX & ECHO
- [ ] **HANYA jika user menyebut. LEWATKAN jika tidak.**
- [ ] Jangan "belum dikerjakan"
=======
### PITFALLS
- Jangan campur template ACS untuk non-ACS
- Jangan singkat nama DPJP
- Diagnosis rujukan harus dipanjangkan
- Setiap ada koreksi/kesalahan → CENTANG ULANG SEMUA CHECKLIST
- **WAJIB CODE BLOCK** — selalu kirim SOAP dalam \`\`\` code block, jangan teks biasa
- **Tanggal EKG/lab = hari ini** — tanggal pemeriksaan di header EKG dan lab adalah tanggal SOAP dibuat (hari ini, 18-06-2026 dst), bukan tanggal hasil ditulis/dicetak. Koreksi jika user beri tanggal berbeda.
- **Soap lama → tanggal baru** — saat membuat SOAP baru dari data soap lama, update semua tanggal ke hari ini kecuali user menentukan sendiri
>>>>>>> b308db8 (sync: update skills klinis 2026-06-25)

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