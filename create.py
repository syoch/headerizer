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

    ident = "MC_" + key.replace("/", "_").upper() + "_H_"

    path = ("hpp/"+key).rpartition("/")[0]
    os.makedirs(path, exist_ok=True)

    namespace_head = ""
    namespace_tail = ""

    namespace_head += "namespace mc {\n"
    namespace_tail += "}  // namespace mc\n"

    for part in key.split("/"):
        namespace_head = namespace_head + "namespace " + part + " {\n"
        namespace_tail = "}  // namespace " + part + "\n"+namespace_tail

    with open("hpp/"+key+".hpp", "w+") as f:
        f.writelines([
            f'#ifndef {ident}\n',
            f'#define {ident}\n',
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
            namespace_head,
            f'\n',
            f'class KEY : public UseInternalAllocator {{\n',
            f' public:\n',
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
            namespace_tail,
            f'\n',
            f'#endif  // {ident}\n'
        ])
    break
