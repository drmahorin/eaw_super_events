import os
from pathlib import Path

import modules

out = '../../eawse'
dirs = (
    'common/scripted_effects',
    'common/scripted_guis',
    'common/scripted_localisation',
    'events',
    'interface/eawse_gfx',
    'interface/eawse_settings',
    'localisation/english',
    'localisation/russian',
    'music',
)
for dir in dirs:
    os.makedirs(f'{out}/{dir}', exist_ok=True)

ids_all = {}
count_all = 0

cats = {}

files = list(Path('../events').rglob('*.[tT][xX][tT]'))
for file in files:
    cat_i, cat = file.stem.split('_', 1)
    cat_i = int(cat_i)
    cats[cat_i] = cat
    print(f'{cat.capitalize()} id = {cat_i}:')
    fi = []
    with file.open(encoding='utf-8') as f:
        fi_raw = f.readlines()
        for line in fi_raw:
            line = line.strip()
            if not line:
                continue
            if line.startswith('#'):
                continue
            fi.append(line)

    ids_all[cat] = (ids := modules.id_grabber(fi))
    sub_ids = modules.subid_grabber(fi)
    anim_ids = modules.anim_grabber(fi)
    count_all += (count := len(ids))
    print(f'Found {count} events...')
    print(ids)

    modules.gfx(out, cat, ids, anim_ids, count)

    steps = (
        modules.localisation,
    )
    for step in steps:
        step(out, cat, fi, count)
    
    print(sub_ids)
    modules.gui(out, (cat_i, cat), sub_ids, count)
    print('')

print('Wrapping some things up...')
steps_all = (
    modules.events,
    modules.music,
    modules.scripted_effects,
    modules.scripted_localisation,
)
for step in steps_all:
    step(out, ids_all, count_all)

modules.category_window(out, len(cats))
