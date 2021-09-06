from typing import Dict, List
import rpx
import ghs_demangle as ghs_demangle
import logging
import json
import pickle

logging.basicConfig(level=logging.INFO)


def get_name(obj: ghs_demangle.Function) -> str:
    if type(obj) == str:
        return obj

    if type(obj.name) == str:
        return obj.name

    return obj.name.name


demangler = ghs_demangle.Demangler()
elf = rpx.Elf("/home/syoch/Documents/reversing/Minecraft.Client.rpx")

table: Dict[str, List[ghs_demangle.Function]] = {}

for func in elf.getFunctions():
    mangled_name = func.name.decode()

    if mangled_name == "__CPR74____ct__Q4_2nn3nex15StepSequenceJJob4StepFMQ3_2nn3nexJ16JFv_vPCw":
        continue

    f = demangler.demangle(mangled_name)
    if isinstance(f, str):
        continue

    if isinstance(f.name, str):
        continue

    if not f.name.namespace.path:
        continue

    path = [
        x.name
        for x in f.name.namespace.path
        if x.name != ""
    ]
    key = "/".join(path)
    if key not in table:
        table[key] = []
    table[key].append(f)

with open("functable.pkl", "wb") as f:
    pickle.dump(table, f)
