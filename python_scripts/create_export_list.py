import sys
import os
import subprocess

try:
    import pefile
except ImportError as e:
    print("To run this script, please install the 'pefile' package: 'pip install pefile'.")
    sys.exit(1)

if len(sys.argv) != 2:
    print("Argument error")
    print("Usage: python create_export_list.py <dllfile>")
    sys.exit(1)

dllpath = sys.argv[1]
if not os.path.exists(dllpath):
    print("DLL not found:", dllpath)
    sys.exit(1)

d = [pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_EXPORT"]]
pe = pefile.PE(dllpath, fast_load=True)
pe.parse_data_directories(directories=d)

exports = [[e.ordinal, e.name] for e in pe.DIRECTORY_ENTRY_EXPORT.symbols]
exports.sort(key=lambda e: e[0]) # Sort by ordinal

export_names = []
for export in exports:
    if export[1] is None: # Ignore exports without names
        continue
    export_names.append(export[1])

num_columns = 50
result_file_name = os.path.basename(dllpath).replace(".dll", "") + "_export_list.txt"
with open(result_file_name, "w") as file:
    index = 0
    for export_name in export_names:
        if type(export_name) is not int:
            file.write("Export(" + str(index) + ", " + export_name.decode("utf-8") + ") ")
            index += 1
            if index % num_columns == 0:
                file.write("\n")

