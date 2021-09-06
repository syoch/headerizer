import pickle
from typing import List, Dict
import ghs_demangle
import os

# with open("functable.pkl", "rb") as f:
#     functable: Dict[str, List[ghs_demangle.Function]] = pickle.load(f)

functable: Dict[str, List[ghs_demangle.Function]] = {
    "a/b": []
}


for key in functable:
    lst = functable[key]
    ident = key.replace("/", "_")

    key = "hpp/"+key

    path = key.rpartition("/")[0]
    os.makedirs(path, exist_ok=True)

    with open(key+".hpp", "w+") as f:
        f.writelines([
            f'#ifndef MC_{ident}_H_\n',
            f'#define MC_{ident}_H_\n',
            f'\n',
            f'//! include some headers\n',
            f'\n',
            # f'// forward declaration\n',
            # f'namespace mc {{\n',
            # f'    //! forward declaration\n',
            # f'}}\n',
            f'\n',
            f'// linking for minecraft internal functions\n',
            f'namespace mc_link {{\n',
            f'    //! "MC_LINK", type, name, ";"\n',
            f'}}\n',
            f'\n',
            f'namespace mc {{\n',
            f'\n',
            f'class KEY : public UseInternalAllocator {{\n',
            f'public:\n',
            # f'    //! "enum class"?\n',
            # f'\n',
            # f'    //! type name;\n',
            # f'\n',
            # "static"?, type, name, args, "\n{"
            # "  return mc_link::", name, args, "\n;"
            # "\n}"
            f'}};\n',
            # f'MC_CHECK_SIZE(KEY, SIZE);\n',
            f'\n',
            f'}}\n',
            f'\n',
            f'#endif\n'
        ])
    break
