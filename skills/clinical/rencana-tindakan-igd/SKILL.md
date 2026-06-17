---
name: rencana-tindakan-igd
description: Format laporan rencana tindakan dari IGD PJT. DPJP Utama & Tindakan bisa orang yang sama atau berbeda.
triggers:
  - "buatkan rencana tindakan"
  - "format rencana tindakan"
  - "laporkan pasien rencana tindakan"
  - pasien akan dijadwalkan prosedur (PCI, TPM, dll)
---

# Rencana Tindakan IGD PJT

## Format Baku

```
Assalamualaikum dokter. Tabe dok, mohon izin melaporkan pasien rencana tindakan dari *IGD PJT RedZone bed [X]* atas nama: 

*[Tn./Ny.] [Nama]/[DD-MM-YYYY]/[Umur] thn/RM [nomor]*

Diagnosis:
- [Diagnosis 1]
- [Diagnosis 2]

*Rencana tindakan: [Jenis Tindakan] (Hari, DD-MM-YYYY)*

_DPJP Utama dan Tindakan : [Dr./Dr.dr. Nama, Spesialis]_ 
ATAU (jika berbeda):
_DPJP Utama : [Dr./Dr.dr. Nama, Spesialis]_
_DPJP Tindakan : [Dr./Dr.dr. Nama, Spesialis]_

TB: [x] cm
BB: [x] kg
BPJS Kelas [1/2/3]
GDS: [x] mg/dl

Tabe dokter, izin melampirkan hasil pemeriksaan penunjang pasien
```

## Aturan DPJP

**Jika 1 orang (Utama = Tindakan):**
```
_DPJP Utama dan Tindakan : Dr.dr. Akhtar Fajar Muzakkir, Sp.JP, Subsp. IKK(K), KI(K)_
```

**Jika 2 orang berbeda (Utama ≠ Tindakan):**
```
_DPJP Utama : dr. Pendrik Tandean, Sp.PD-KKV_
_DPJP Tindakan : Dr.dr. Akhtar Fajar Muzakkir, Sp.JP(K)_
```

## Variabel

## Variabel

> **DPJP**: Selalu gunakan nama dan gelar lengkap dari `references/daftar-dpjp.md`. JANGAN menyingkat nama (misal: "Akhtar Fajar M" → harus "Akhtar Fajar Muzakkir").

| Variabel | Sumber |
|---|---|
| Nama, TTL, Umur, RM | Dari SOAP pasien di sesi ini / barcode |
| Bed | Dari SOAP / arahan Dokter |
| Diagnosis | Dari SOAP Assessment |
| Jenis Tindakan + tanggal | Arahan Dokter |
| DPJP Utama | Arahan Dokter |
| DPJP Tindakan | Arahan Dokter (konfirmasi: sama atau beda?) |
| TB, BB, BPJS | Dari SOAP |
| GDS | Dari lab terbaru |

## Pitfalls

- **JANGAN singkat nama DPJP**: "Dr.dr. Akhtar Fajar M" ❌ → "Dr.dr. Akhtar Fajar Muzakkir" ✅. Selalu cek `references/daftar-dpjp.md`.
- **JANGAN asumsikan DPJP Utama = Tindakan**: Konfirmasi ke Dokter setiap kali. Format 2 baris berbeda saat beda orang.
- **GDS dari lab terbaru**: Bukan dari anamnesis, pastikan ambil dari data lab SOAP.
- **Umur dihitung dari TTL**: TTL 12-12-1982 di 2026 = 43 thn, bukan 56 thn. Hitung manual, jangan ikut angka lisan.
- Primary PCI
- Implantasi TPM (Temporary Pacemaker)
- Pemasangan IABP
- Perikardiosentesis

## Alur Kerja
1. Dokter: "buatkan rencana tindakan [nama pasien]"
2. Ambil data dari SOAP sesi ini
3. Konfirmasi: DPJP Utama = Tindakan? atau berbeda?
4. Konfirmasi: jenis tindakan + tanggal
5. Isi template → tampilkan
