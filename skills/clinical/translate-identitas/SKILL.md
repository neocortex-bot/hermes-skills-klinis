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

Output identitas tanpa codeblock -- langsung plain text dengan format:

```
: [Initial]
: [Age] years old
: [DD-MM-YYYY]
: [City/Domicile]
: [MRN]
: [DD-MM-YYYY]
: [dr. Name]
```

- Setiap baris diawali dengan `: ` (colon + space)
- Tidak ada label/key -- cukup nilai langsung setelah `: `
- Baris pertama: Inisial + title (Mr. / Mrs.)
- Tanggal Lahir dan Date of Admission format DD-MM-YYYY
- Info rujukan opsional -- baris terakhir bila ada, dengan format:
  `The patient was referred from [RS] with [diagnosis]`

## Checklist Wajib

### Struktur
- [ ] Format `: [value]` -- colon + space, tanpa label
- [ ] Urutan tetap: Inisial -> Usia -> TTL -> Domisili -> MRN -> Admission -> DPJP -> Rujukan (opsional)
- [ ] Tidak ada codeblock -- plain text
- [ ] Bila info tidak tersedia -- KOSONGKAN barisnya (jangan halusinasi, jangan isi "N/A" atau "--")

### Aturan Per Baris

| Baris | Format | Contoh |
|---|---|---|
| 1 -- Inisial | `: Mr./Mrs. [Huruf depan]` | `: Mr. M` |
| 2 -- Usia | `: [angka] years old` | `: 59 years old` |
| 3 -- Tanggal Lahir | `: [DD-MM-YYYY]` | `: 09-12-1966` |
| 4 -- Domisili | `: [Kota]` (dari input) | `: [kosong bila tidak ada]` |
| 5 -- MRN | `: [nomor RM]` | `: 205526` |
| 6 -- Date of Admission | `: [DD-MM-YYYY]` (tanggal masuk IGD) | `: 15-06-2026` |
| 7 -- DPJP | `: dr. [Nama]` (tanpa gelar Sp, cukup nama) | `: dr. Az Hafid Nashar` |
| 8 -- Rujukan (opsional) | `The patient was referred from [RS] with [diagnosis]` | Hanya bila ada info rujukan |

### Aturan Khusus
- [ ] Inisial: huruf depan nama depan saja. Mr. untuk laki-laki, Mrs. untuk perempuan
- [ ] Usia: dari input -- jika tidak disebut, kosongkan
- [ ] TTL: dari input -- jika tidak disebut, kosongkan
- [ ] Domisili: dari input -- jika tidak disebut, kosongkan (jangan isi tebakan)
- [ ] MRN: nomor RM dari input
- [ ] Date of Admission: tanggal masuk IGD/RS -- dari input atau hari ini
- [ ] DPJP: nama dokter penanggung jawab -- cukup nama tanpa gelar subspesialis, tanpa "Sp."
- [ ] Rujukan: hanya bila ada info "dirujuk dari" -- jika tidak ada, skip baris ini

### Contoh Output -- Tanpa Rujukan

```
: Mr. M
: 59 years old
: 09-12-1966
: 
: 205526
: 15-06-2026
: dr. Az Hafid Nashar
```

### Contoh Output -- Dengan Rujukan

```
: Mrs. S
: 63 years old
: 07-10-1963
: Gowa
: 1630580
: 21-05-2026
: dr. NP

The patient was referred from Syeikh Yusuf Gowa Hospital with STEMI Inferior
```

## Pitfalls
- Jangan tambahkan label seperti "Name:", "Age:" -- cukup `: [value]`
- Jangan inisial pakai dots: "M." -> cukup "M" atau "Mr. M"
- Jangan isi domisili/alamat bila tidak disebut
- DPJP: cukup nama tanpa gelar subspesialis -- simpan untuk SOAP
- Tanggal LAHIR pasien, bukan tanggal visit -- bedakan dengan Date of Admission
- Info rujukan hanya 1 baris terakhir, pisahkan dengan 1 baris kosong dari DPJP
