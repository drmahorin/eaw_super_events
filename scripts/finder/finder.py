import re
from pathlib import Path

ids = {}
with open('../migrator/old/common/scripted_localisation/EAWSE_scripted_localisation.txt') as f:
    gfx = f.read()
    for hit in re.finditer(r'EAWSE_super_event = ([0-9]*).*\n.*"(.*)_T"', gfx, re.MULTILINE):
        ids[hit[2].split('_', 1)[1]] = hit[1]

files = list(Path('../events').rglob('*.[tT][xX][tT]'))

for file in files:
    cat = file.stem.split('_')[1]
    with file.open(encoding='utf-8') as f:
        lines = f.readlines()

    with file.open('w', encoding='utf-8') as f:
        for line in lines:
            line = line.rstrip()
            flag_1 = line.startswith('SE_') or line.startswith('EAWSE_')
            flag_2 = line.endswith('_T')
            if flag_1 and flag_2:
                print(line)
                line = '_'.join(line.split('_')[1:-1])
                line = f'{ids[line]} EAWSE_{line}'
                print(line)
            f.write(f'{line}\n')
