# PCWP Calculation (Nagueh Formula)

## Rumus

```
PCWP (mmHg) = 2 + 1.16 × (E / e')
```

Dimana:
- **E** = Mitral inflow E wave velocity (m/s) — parameter `ea` di form echo
- **e'** = Average of septal and lateral mitral annular early diastolic velocity (m/s)
  - `e' = (E' Med + E' Lat) / 2`

## Unit konversi

Parameter dari form echo:
- `ea` (E/A) = **E wave velocity** dalam **m/s** → langsung pakai
- `e_med` (E' Med) = **cm/s** → bagi 100 → **m/s**
- `e_lat` (E' Lat) = **cm/s** → bagi 100 → **m/s**

## Syarat kalkulasi

PCWP hanya dihitung jika **ketiga parameter tersedia**:
1. `ea` (E wave, m/s)
2. `e_med` (E' Septal, cm/s)
3. `e_lat` (E' Lateral, cm/s)

Jika salah satu tidak ada, PCWP dilewati (tidak dicantumkan).

## Contoh

| E (m/s) | E' Med (cm/s) | E' Lat (cm/s) | e' avg (m/s) | E/e' | PCWP (mmHg) |
|---------|---------------|---------------|--------------|------|-------------|
| 0.86    | 11            | 8             | 0.095        | 9.1  | 12.5        |
| 1.13    | 9.0           | 13.3          | 0.112        | 10.1 | 13.8        |

## Referensi

Nagueh SF, Smiseth OA, Appleton CP, et al. Recommendations for the Evaluation of Left Ventricular Diastolic Function by Echocardiography: An Update from the ASE and the EACVI. *J Am Soc Echocardiogr.* 2016;29(4):277-314.
