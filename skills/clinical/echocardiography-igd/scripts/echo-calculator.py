#!/usr/bin/env python3
"""
Echocardiography IGD Calculator — Mini App
Pakboss isi parameter echo, script output format lengkap.
Yang tidak diisi = tidak disematkan.

Cara pakai: python3 echo-calculator.py --date "08-05-2026" --lv-func "Moderately Abnormal" ...
Atau: panggil fungsi calculate() dari Python.
"""

import math
import argparse
import sys


def fmt(n):
    """Format angka: integer tanpa desimal, float dengan 1 desimal"""
    if n is None:
        return ""
    if isinstance(n, int):
        return str(n)
    return f"{n:.1f}"


def calculate(tds=None, tdd=None, hr=None, lvot_diam=None, lvot_vti=None,
              ivc_exp=None, ivc_insp=None, bb=None, tb=None,
              lv_func=None, ef_teich=None, ef_biplane=None,
              rv_func=None, tapse=None, s_lat=None,
              mitral=None, aorta=None, tricuspid=None, pulmonal=None,
              lvidd=None, la_mayor=None, la_minor=None, ra_mayor=None, ra_minor=None,
              rvdb=None, la_ao=None,
              lvh_type=None, lvmi=None, rwt=None,
              rwma=None,
              ea=None, e_med=None, e_lat=None, ee=None, grade=None,
              perikard=None,
              a_line="+", b_line="-", b_line_loc="", c_line="-",
              pleural_effusion="-", pleural_loc="",
              extra_echo=None,
              date="",
              conclusion_lv=None, conclusion_rv=None, conclusion_valves=None,
              conclusion_lvh=None, conclusion_rwma=None, conclusion_diastole=None,
              ):
    
    lines = []
    lines.append(f"*Echocardiography Bedside ({date})*")
    
    # 1. LV Function
    if lv_func:
        line = f"- {lv_func} LV Systolic Function"
        if ef_teich is not None:
            line += f" EF {ef_teich}% (TEICH)"
        if ef_biplane is not None:
            if ef_teich is not None:
                line += f", EF {ef_biplane}% (BIPLANE)"
            else:
                line += f" EF {ef_biplane}% (BIPLANE)"
        lines.append(line)
    
    # 2. RV Function
    if rv_func:
        line = f"- {rv_func} RV systolic function"
        if tapse is not None:
            line += f", TAPSE {tapse} cm/s"
        if s_lat is not None:
            line += f", S' lateral {s_lat} cm/s"
        lines.append(line)
    
    # 3. Valves
    has_valve = any([mitral, aorta, tricuspid, pulmonal])
    if has_valve:
        lines.append("- Cardiac Valves:")
        if aorta:
            lines.append(f"    - Aorta: {aorta}")
        if mitral:
            lines.append(f"    - Mitral: {mitral}")
        if tricuspid:
            lines.append(f"    - Tricuspid: {tricuspid}")
        if pulmonal:
            lines.append(f"    - Pulmonal: {pulmonal}")
    
    # 4. Cardiac Dimensions
    dims = []
    if lvidd is not None: dims.append(f"LVIDd {lvidd} cm")
    if la_mayor is not None: dims.append(f"LA mayor {la_mayor} cm")
    if la_minor is not None: dims.append(f"LA minor {la_minor} cm")
    if ra_mayor is not None: dims.append(f"RA mayor {ra_mayor} cm")
    if ra_minor is not None: dims.append(f"RA minor {ra_minor} cm")
    if rvdb is not None: dims.append(f"RVDB {rvdb} cm")
    if la_ao is not None: dims.append(f"LA/Ao {la_ao}")
    
    if dims:
        # Check if LV dilated
        is_lv_dilated = lvidd is not None and lvidd > 5.5
        is_la_dilated = la_mayor is not None and la_mayor > 4.0
        is_ra_dilated = ra_mayor is not None and ra_mayor > 4.0
        
        if lvh_type and lvh_type.lower() != "normal":
            lvh_str = f" with {lvh_type} LVH"
            if lvmi is not None and rwt is not None:
                lvh_str += f" (LVMI {lvmi} g/m², RWT {rwt})"
            elif lvmi is not None:
                lvh_str += f" (LVMI {lvmi} g/m²)"
            
            prefix = ""
            if is_lv_dilated and is_la_dilated and is_ra_dilated:
                prefix = "All Chambers Dilatation"
            elif is_lv_dilated:
                prefix = "LV Dilatation"
            elif is_la_dilated:
                prefix = "LA Dilatation"
            
            if prefix:
                dims_str = ", ".join([d.split(" cm")[0] + " cm" for d in dims])
                lines.append(f"- {prefix}{lvh_str} ({dims_str})")
            else:
                lines.append(f"- {', '.join(dims)}{lvh_str}")
        else:
            prefix = ""
            if is_lv_dilated and is_la_dilated and is_ra_dilated:
                prefix = "All Chambers Dilatation "
            elif is_lv_dilated:
                prefix = "LV Dilatation "
            elif is_la_dilated:
                prefix = "LA Dilatation "
            lines.append(f"- {prefix}({', '.join(dims)})")
    
    # 5. RWMA
    if rwma:
        lines.append(f"- RMWA: {rwma}")
    
    # 6. eRAP
    if ivc_exp is not None and ivc_insp is not None:
        erap_val = _calc_erap(ivc_exp, ivc_insp)
        lines.append(f"- eRAP: {erap_val} mmHg (IVC exp: {ivc_exp} cm, IVC insp: {ivc_insp} cm)")
    
    # 7. Diastolic Function
    diast_parts = []
    if ea is not None: diast_parts.append(f"E/A {ea}")
    if e_med is not None: diast_parts.append(f"E Sept {e_med} cm")
    if e_lat is not None: diast_parts.append(f"E Lat {e_lat} cm")
    if ee is not None: diast_parts.append(f"E/E' {ee}")
    
    if diast_parts:
        diast_str = ", ".join(diast_parts)
        if grade:
            lines.append(f"- {grade} LV Diastolic Dysfunction ({diast_str})")
        else:
            lines.append(f"- Abnormal LV Diastolic Function ({diast_str})")
    elif grade:
        lines.append(f"- {grade} LV Diastolic Dysfunction")
    
    # 8. Pericardial effusion
    if perikard:
        lines.append(f"- Pericardial Effusion: {perikard}")
    
    # 9. Extra
    if extra_echo:
        lines.append(f"- {extra_echo}")
    
    lines.append("")
    
    # === Echo Hemodinamik ===
    has_hemo = any([tds is not None, tdd is not None, hr is not None,
                    lvot_diam is not None, lvot_vti is not None,
                    ivc_exp is not None, ivc_insp is not None])
    
    if has_hemo:
        lines.append("*Echo Hemodinamik:*")
        
        if tds is not None and tdd is not None:
            map_val = ((2 * tdd) + tds) / 3
            lines.append(f"TD: {tds}/{tdd} mmHg")
            lines.append(f"MAP: {map_val:.0f} mmHg")
        
        if hr is not None:
            lines.append(f"HR: {hr} bpm")
        
        if lvot_diam is not None:
            lines.append(f"LVOT Diam: {lvot_diam} cm")
        if lvot_vti is not None:
            lines.append(f"LVOT VTI: {lvot_vti} cm")
        
        # LV SV = VTI * D^2 * pi/4
        if lvot_vti is not None and lvot_diam is not None:
            lv_sv = lvot_vti * (lvot_diam ** 2) * 0.7854
            lines.append(f"LV SV: {lv_sv:.1f} ml")
            
            if hr is not None:
                lv_co = (lv_sv * hr) / 1000
                lines.append(f"LV CO: {lv_co:.2f} L/min")
        
        if ivc_exp is not None and ivc_insp is not None:
            erap_val = _calc_erap(ivc_exp, ivc_insp)
            lines.append(f"eRAP: {erap_val} mmHg ({ivc_exp}/{ivc_insp} cm)")
        
        # SVR
        if all([tds is not None, tdd is not None, ivc_exp is not None, ivc_insp is not None,
                lvot_vti is not None, lvot_diam is not None, hr is not None]):
            map_val = ((2 * tdd) + tds) / 3
            lv_sv = lvot_vti * (lvot_diam ** 2) * 0.7854
            lv_co = (lv_sv * hr) / 1000
            erap_val = _calc_erap(ivc_exp, ivc_insp)
            svr = ((map_val - erap_val) / lv_co) * 80
            lines.append(f"SVR: {svr:.0f} dynes/sec/cm-5")
        
        # BSA, CI, CPO, CPI
        if all([bb is not None, tb is not None, lvot_vti is not None, lvot_diam is not None,
                hr is not None, tds is not None, tdd is not None]):
            map_val = ((2 * tdd) + tds) / 3
            lv_sv = lvot_vti * (lvot_diam ** 2) * 0.7854
            lv_co = (lv_sv * hr) / 1000
            bsa = math.sqrt((tb * bb) / 3600)
            ci = lv_co / bsa
            cpo = (lv_co * map_val) / 451
            cpi = cpo / bsa
            lines.append(f"BSA: {bsa:.2f} m² | CI: {ci:.2f} L/min/m²")
            lines.append(f"CPO: {cpo:.2f} watt | CPI: {cpi:.2f} watt/m²")
    
    lines.append("")
    
    # === Lung Ultrasound ===
    lines.append("*Lung Ultrasound:*")
    lu_parts = []
    lu_parts.append("Lung sliding (+), pleural line reguler")
    lu_parts.append(f"A line ({a_line})")
    lu_parts.append(f"B line ({b_line})")
    if b_line_loc:
        lu_parts.append(b_line_loc)
    lu_parts.append(f"C line ({c_line})")
    ef_str = f"Plural effusion ({pleural_effusion})"
    if pleural_loc:
        ef_str += f" {pleural_loc}"
    lu_parts.append(ef_str)
    lines.append(", ".join(lu_parts))
    
    lines.append("")
    
    # === Conclusion ===
    if any([conclusion_lv, conclusion_rv, conclusion_valves,
            conclusion_lvh, conclusion_rwma, conclusion_diastole]):
        lines.append("*Conclusion:*")
        if conclusion_lv: lines.append(f"- {conclusion_lv}")
        if conclusion_rv: lines.append(f"- {conclusion_rv}")
        if conclusion_valves: lines.append(f"- {conclusion_valves}")
        if conclusion_lvh: lines.append(f"- {conclusion_lvh}")
        if conclusion_rwma: lines.append(f"- {conclusion_rwma}")
        if conclusion_diastole: lines.append(f"- {conclusion_diastole}")
        lines.append("")
    
    return "\n".join(lines)


def _calc_erap(ivc_exp, ivc_insp):
    """Hitung eRAP dari IVC — berdasarkan tabel standar"""
    collaps = ((ivc_exp - ivc_insp) / ivc_exp) * 100
    if ivc_exp < 2.1 and collaps > 50:
        return 3
    elif ivc_exp < 2.1 and collaps <= 50:
        return 8
    elif ivc_exp >= 2.1 and collaps > 50:
        return 8
    else:
        return 15


def parse_arg(v):
    """Parse CLI arg: int, float, atau string"""
    if v is None or v == "":
        return None
    v = v.strip()
    # Try int
    try:
        return int(v)
    except ValueError:
        pass
    # Try float (handle comma as decimal)
    try:
        return float(v.replace(",", "."))
    except ValueError:
        pass
    return v


def main():
    parser = argparse.ArgumentParser(description="Echocardiography IGD Calculator")
    
    # Date
    parser.add_argument("--date", default="")
    
    # Echo params
    parser.add_argument("--lv-func", default=None)
    parser.add_argument("--ef-teich", type=parse_arg, default=None)
    parser.add_argument("--ef-biplane", type=parse_arg, default=None)
    parser.add_argument("--rv-func", default=None)
    parser.add_argument("--tapse", type=parse_arg, default=None)
    parser.add_argument("--s-lat", type=parse_arg, default=None)
    parser.add_argument("--mitral", default=None)
    parser.add_argument("--aorta", default=None)
    parser.add_argument("--tricuspid", default=None)
    parser.add_argument("--pulmonal", default=None)
    parser.add_argument("--lvidd", type=parse_arg, default=None)
    parser.add_argument("--la-mayor", type=parse_arg, default=None)
    parser.add_argument("--la-minor", type=parse_arg, default=None)
    parser.add_argument("--ra-mayor", type=parse_arg, default=None)
    parser.add_argument("--ra-minor", type=parse_arg, default=None)
    parser.add_argument("--rvdb", type=parse_arg, default=None)
    parser.add_argument("--la-ao", type=parse_arg, default=None)
    parser.add_argument("--lvh-type", default=None)
    parser.add_argument("--lvmi", type=parse_arg, default=None)
    parser.add_argument("--rwt", type=parse_arg, default=None)
    parser.add_argument("--rwma", default=None)
    parser.add_argument("--ea", type=parse_arg, default=None)
    parser.add_argument("--e-med", type=parse_arg, default=None)
    parser.add_argument("--e-lat", type=parse_arg, default=None)
    parser.add_argument("--ee", type=parse_arg, default=None)
    parser.add_argument("--grade", default=None)
    parser.add_argument("--perikard", default=None)
    parser.add_argument("--extra-echo", default=None)
    
    # Hemodinamik
    parser.add_argument("--tds", type=parse_arg, default=None)
    parser.add_argument("--tdd", type=parse_arg, default=None)
    parser.add_argument("--hr", type=parse_arg, default=None)
    parser.add_argument("--lvot-diam", type=parse_arg, default=None)
    parser.add_argument("--lvot-vti", type=parse_arg, default=None)
    parser.add_argument("--ivc-exp", type=parse_arg, default=None)
    parser.add_argument("--ivc-insp", type=parse_arg, default=None)
    parser.add_argument("--bb", type=parse_arg, default=None)
    parser.add_argument("--tb", type=parse_arg, default=None)
    
    # Lung US
    parser.add_argument("--a-line", default="+")
    parser.add_argument("--b-line", default="-")
    parser.add_argument("--b-line-loc", default="")
    parser.add_argument("--c-line", default="-")
    parser.add_argument("--pleural-effusion", default="-")
    parser.add_argument("--pleural-loc", default="")
    
    # Conclusion
    parser.add_argument("--conclusion-lv", default=None)
    parser.add_argument("--conclusion-rv", default=None)
    parser.add_argument("--conclusion-valves", default=None)
    parser.add_argument("--conclusion-lvh", default=None)
    parser.add_argument("--conclusion-rwma", default=None)
    parser.add_argument("--conclusion-diastole", default=None)
    
    args = parser.parse_args()
    
    result = calculate(
        date=args.date,
        lv_func=args.lv_func, ef_teich=args.ef_teich, ef_biplane=args.ef_biplane,
        rv_func=args.rv_func, tapse=args.tapse, s_lat=args.s_lat,
        mitral=args.mitral, aorta=args.aorta, tricuspid=args.tricuspid, pulmonal=args.pulmonal,
        lvidd=args.lvidd, la_mayor=args.la_mayor, la_minor=args.la_minor,
        ra_mayor=args.ra_mayor, ra_minor=args.ra_minor, rvdb=args.rvdb, la_ao=args.la_ao,
        lvh_type=args.lvh_type, lvmi=args.lvmi, rwt=args.rwt,
        rwma=args.rwma,
        ea=args.ea, e_med=args.e_med, e_lat=args.e_lat, ee=args.ee, grade=args.grade,
        perikard=args.perikard,
        a_line=args.a_line, b_line=args.b_line, b_line_loc=args.b_line_loc,
        c_line=args.c_line, pleural_effusion=args.pleural_effusion, pleural_loc=args.pleural_loc,
        extra_echo=args.extra_echo,
        tds=args.tds, tdd=args.tdd, hr=args.hr,
        lvot_diam=args.lvot_diam, lvot_vti=args.lvot_vti,
        ivc_exp=args.ivc_exp, ivc_insp=args.ivc_insp, bb=args.bb, tb=args.tb,
        conclusion_lv=args.conclusion_lv, conclusion_rv=args.conclusion_rv,
        conclusion_valves=args.conclusion_valves, conclusion_lvh=args.conclusion_lvh,
        conclusion_rwma=args.conclusion_rwma, conclusion_diastole=args.conclusion_diastole,
    )
    print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        # Test dengan data riil pakboss
        result = calculate(
            date="08-05-2026",
            lv_func="Moderately Abnormal", ef_teich=37.1, ef_biplane=33.2,
            rv_func="Normal", tapse=1.7, s_lat=15.5,
            aorta="3 cuspis, calcification (-), Normal",
            tricuspid="Normal Function and Movement",
            pulmonal="Normal Function and Movement",
            mitral="Normal Function and Movement",
            lvidd=6.71, la_mayor=4.20, la_minor=3.37, ra_mayor=2.97, ra_minor=2.40,
            rvdb=2.84, lvh_type="Eccentric", lvmi=166, rwt=0.17,
            rwma="Akinetic Apicoanterior, Badal Mid Anteroseptal, Hypokinetic Basal Mid Anterolateral",
            ivc_exp=1.22, ivc_insp=0.6,
            ea=1.13, e_med=9.0, e_lat=13.3, grade="Grade I",
            tds=105, tdd=70, hr=108,
            lvot_diam=1.7, lvot_vti=17.7, bb=65, tb=165,
            conclusion_lv="Moderately Abnormal LV Systolic Function EF 37.1% (TEICH), EF 33.2% (BIPLANE)",
            conclusion_rv="Normal RV systolic function, TAPSE 1.7 cm/s, S' lateral 15.5 cm/s",
            conclusion_valves="Normal Cardiac Valves",
            conclusion_lvh="LV Dilatation with Eccentric LVH",
            conclusion_rwma="Akinetic and Hypokinetic Segmental",
            conclusion_diastole="Grade I LV Diastolic Dysfunction",
        )
        print(result)
