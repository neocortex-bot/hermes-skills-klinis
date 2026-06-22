---
name: translate-identitas
description: "Translate identitas pasien IGD PJT Jantung ke Inggris. Format baku: Inisial, Usia, TTL, Domisili, MRN, Date of Admission, DPJP, dan info rujukan (opsional)."
triggers:
  - user meminta translate identitas pasien ke Inggris
  - user meminta English version of patient identity/header
  - user menyebut "translate identitas" atau "identity"
---

# Translate Identitas Pasien -> English

## Format Output

Output identitas di dalam codeblock dengan format:

```
Name    : [Initial]
Age     : [Age] years old
Date of birth : [DD-MM-YYYY]
Address : [City/Domicile]
MR      : [MRN]
Date of Admission : [DD-MM-YYYY]
DPJP    : [dr. Name]

Patient Reffered From [RS] with [diagnosis]
```

- Setiap baris berisi label + colon + value, rata kiri
- Label: Name, Age, Date of birth, Address, MR, Date of Admission, DPJP
- Referral: baris narasi terakhir, 1 baris kosong setelah DPJP, diawali "Patient Reffered From"
- Jika tidak ada rujukan, SKIP baris Referral dan baris kosongnya

## Checklist Wajib

### Struktur
- [ ] Format `Label : [value]` -- rata kiri, colon + space
- [ ] Urutan tetap: Name -> Age -> DOB -> Address -> MR -> Date of Admission -> DPJP
- [ ] Referral: baris narasi terakhir, 1 baris kosong setelah DPJP
- [ ] **Di dalam codeblock — bukan plain text**
- [ ] Bila info tidak tersedia -- KOSONGKAN value-nya (jangan halusinasi, jangan isi "N/A")
- [ ] Label konsisten: persis Name, Age, Date of birth, Address, MR, Date of Admission, DPJP

### Aturan Per Baris

| Label | Format | Contoh |
|---|---|---|
| Name | `Name    : Mr./Mrs. [Huruf depan]` | `Name    : Mr. M` |
| Age | `Age     : [angka] years old` | `Age     : 59 years old` |
| Date of birth | `Date of birth : [DD-MM-YYYY]` | `Date of birth : 09-12-1966` |
| Address | `Address : [Kota]` (dari input) | `Address : Gowa` (kosong jika tidak ada) |
| MR | `MR      : [nomor RM]` | `MR      : 205526` |
| Date of Admission | `Date of Admission : [DD-MM-YYYY]` | `Date of Admission : 15-06-2026` |
| DPJP | `DPJP    : [Nama]` (tanpa "dr." jika tidak disebut, cukup nama) | `DPJP    : dr. Az Hafid Nashar` |

Referral (opsional): baris narasi setelah 1 baris kosong dari DPJP, diawali "Patient Reffered From [RS] with [diagnosis]"

### Aturan Khusus
- [ ] Name: Mr. untuk laki-laki, Mrs. untuk perempuan, diikuti huruf depan nama
- [ ] Age: dari input -- jika tidak disebut, kosongkan
- [ ] Date of birth: dari input -- jika tidak disebut, kosongkan
- [ ] Address: dari input -- jika tidak disebut, kosongkan (jangan isi tebakan)
- [ ] MR: nomor RM dari input
- [ ] Date of Admission: tanggal masuk IGD/RS -- dari input
- [ ] DPJP: nama dokter penanggung jawab sesuai input -- dengan gelar "dr." bila disebut
- [ ] Referral: hanya bila ada info "dirujuk dari" -- 1 baris kosong setelah DPJP, lalu "Patient Reffered From [RS] with [diagnosis]"
- [ ] Jika tidak ada rujukan: SKIP baris Referral dan baris kosongnya

### Contoh Output -- Tanpa Rujukan

```
Name    : Mr. M
Age     : 59 years old
Date of birth : 09-12-1966
Address : 
MR      : 205526
Date of Admission : 15-06-2026
DPJP    : dr. Az Hafid Nashar
```

### Contoh Output -- Dengan Rujukan

```
Name    : Mrs. S
Age     : 63 years old
Date of birth : 07-10-1963
Address : Gowa
MR      : 1630580
Date of Admission : 21-05-2026
DPJP    : dr. NP

Patient Reffered From Syeikh Yusuf Gowa Hospital with STEMI Inferior
```

## Pitfalls
- Jangan tambahkan label seperti "Name:", "Age:" -- cukup `: [value]`
- Jangan inisial pakai dots: "M." -> cukup "M" atau "Mr. M"
- Jangan isi domisili/alamat bila tidak disebut
- DPJP: cukup nama tanpa gelar subspesialis -- simpan untuk SOAP
- Tanggal LAHIR pasien, bukan tanggal visit -- bedakan dengan Date of Admission
- Referral: baris NARASI (bukan Label : Value), diawali "Patient Reffered From"
- Referral: 1 baris kosong setelah DPJP, bukan langsung setelah Address
- Jika tidak ada rujukan, SKIP baris Referral dan baris kosongnya
