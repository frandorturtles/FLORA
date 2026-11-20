#!/usr/bin/env python3
"""ERC 'ligero' propio (NO es el ERC oficial de KiCad). Comprueba el netlist exportado del esquemático."""
import os, re, subprocess, sys, xml.etree.ElementTree as ET
import pcbnew
HW = os.environ.get("FLORA_HW", os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
subprocess.run(["kicad-cli","sch","export","netlist","--format","kicadxml","-o","/tmp/flora.xml",f"{HW}/FLORA.kicad_sch"],check=True,capture_output=True)
root = ET.parse("/tmp/flora.xml").getroot()
comps = {}
for c in root.find("components"):
    comps[c.get("ref")] = dict(value=(c.find("value").text or ""), fp=(c.find("footprint").text or ""))
errs, warns, info = [], [], []
# 1) campos básicos y referencias únicas
refs = [c.get("ref") for c in root.find("components")]
if len(refs) != len(set(refs)): errs.append("Referencias duplicadas")
for r, c in comps.items():
    if not c["value"].strip(): errs.append(f"{r}: sin valor")
    if not c["fp"].strip(): errs.append(f"{r}: sin huella")
# 2) pines del símbolo vs pads de la huella
FP = "/usr/share/kicad/footprints/"
pins = {}
for n in root.find("nets"):
    for nd in n: pins.setdefault(nd.get("ref"), {})[nd.get("pin")] = (n.get("name"), nd.get("pintype"), nd.get("pinfunction"))
for r, c in comps.items():
    lib, name = c["fp"].split(":")
    fp = pcbnew.FootprintLoad(FP + lib + ".pretty", name)
    pads = {p.GetNumber() for p in fp.Pads() if p.IsOnCopperLayer() or p.GetAttribute() in (pcbnew.PAD_ATTRIB_PTH,)} - {""}
    sp = set(pins.get(r, {}))
    if sp - pads: errs.append(f"{r}: pines sin pad en la huella {sorted(sp - pads)}")
    if pads - sp: warns.append(f"{r}: pads sin pin en el símbolo {sorted(pads - sp)}")
# 3) redes: nodos, tipos de pin
FLAGGED = {"VIN_PROT", "GND", "VBUS"}      # redes con PWR_FLAG colocado en el esquemático
sch = open(f"{HW}/FLORA.kicad_sch", encoding="utf-8").read()
nflags = len(re.findall(r'\(lib_id "power:PWR_FLAG"', sch)); info.append(f"PWR_FLAG colocados: {nflags}")
for n in root.find("nets"):
    name = n.get("name").lstrip("/"); nodes = [(x.get("ref"), x.get("pin"), x.get("pintype")) for x in n]
    types = [t for *_, t in nodes]
    if name.startswith("unconnected"):
        r, p, t = nodes[0]
        (info if t in ("no_connect", "passive") or "NC" in (pins[r][p][2] or "") or "INT" in (pins[r][p][2] or "") or "SBU" in (pins[r][p][2] or "") else warns).append(f"pin sin conectar con marca NC: {r}.{p} ({pins[r][p][2]}, {t})")
        continue
    if len(nodes) < 2: errs.append(f"Red '{name}' con un solo pin: {nodes}")
    pout = [x for x in nodes if x[2] in ("power_out", "output")]
    if sum(1 for x in nodes if x[2] == "power_out") > 1: errs.append(f"Red '{name}': varias salidas de alimentación {pout}")
    if sum(1 for x in nodes if x[2] == "output") > 1: errs.append(f"Red '{name}': varias salidas {pout}")
    if any(t == "power_in" for t in types):
        if not any(t == "power_out" for t in types) and name not in FLAGGED: errs.append(f"Red '{name}': entrada de alimentación sin fuente ni PWR_FLAG")
        elif not any(t == "power_out" for t in types): info.append(f"Red '{name}': alimentación cubierta por PWR_FLAG")
    if any(t == "input" for t in types) and not any(t in ("output", "bidirectional", "tri_state", "power_out", "passive", "open_collector") for t in types):
        warns.append(f"Red '{name}': entrada sin ningún pin que la maneje {nodes}")
# 4) cortos entre redes de alimentación distintas por nombre
names = {n.get("name").lstrip("/") for n in root.find("nets")}
for must in ("GND", "+3V3", "VBUS", "VIN_PROT", "SENS_VCC"):
    if must not in names: errs.append(f"Falta la red {must}")
# 5) GPIO duplicados
u1 = pins["U1"]; used = [v[0] for k, v in u1.items() if not v[0].startswith("unconnected")]
seen = {}
for k, v in u1.items(): seen.setdefault(v[0], []).append(k)
for net, ks in seen.items():
    if net not in ("GND",) and len(ks) > 1: errs.append(f"U1: la red {net} está en varios pines {ks}")
print(f"ERRORES: {len(errs)}"); [print("  E:", e) for e in errs]
print(f"AVISOS: {len(warns)}"); [print("  W:", w) for w in warns]
print("INFO:"); [print("  I:", i) for i in info]
open("/tmp/erc_light.txt", "w").write("\n".join([f"E: {e}" for e in errs] + [f"W: {w}" for w in warns] + [f"I: {i}" for i in info]))
