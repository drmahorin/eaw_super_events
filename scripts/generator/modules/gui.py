from .utils import print_events, print_time, read_template

TITLE = 'GUI'

tceg = read_template('./templates/superevent_category_entry.txt')
tces = read_template('./templates/superevent_category_entry_sg.txt')

tcg = read_template('./templates/superevent_category.txt')
tcs = read_template('./templates/superevent_category_sg.txt')

tsg = read_template('./templates/superevent_entry.txt')
tss = read_template('./templates/superevent_entry_sg.txt')

tsl = read_template('./templates/scripted_localisation.txt')

ci = 0

@print_time(TITLE)
def gui(out: str, cat: tuple[int, str], sub_ids: dict[str, dict[int, str]], c: int):
    global ci
    cat_i, cat = cat
    cat_cap = cat.upper()
    fg = open(f'{out}/interface/eawse_settings/eawse_{cat}.gui', 'w', encoding='utf-8')
    fs = open(f'{out}/common/scripted_guis/eawse_{cat}.txt', 'w', encoding='utf-8')
    fl = open(f'{out}/common/scripted_localisation/eawse_sloc_c_{cat}.txt', 'w', encoding='utf-8')

    try:
        events = 0
        fg.write('guiTypes = {\n')
        fs.write('scripted_gui = {\n')

        fg.write(tceg(cat = cat, cat_cap = cat_cap, cat_i = cat_i, y = 120 * ci + 3))
        fs.write(tces(cat = cat, cat_i = cat_i))

        ci += 1

        fg.write(tcg(cat = cat, y = c * 30))
        fs.write(tcs(cat = cat, cat_i = cat_i))
        for sub_id, ids in sub_ids.items():
            for i, id in ids.items():
                fg.write(tsg(i = i, id = id, sub = sub_id, y = events * 30))
                fs.write(tss(cat = cat, i = i, id = id.lower()))
                fl.write(tsl(id = id))
                events += 1
                if events < c:
                    fg.write('\n')
                    fs.write('\n')
        fg.write('}\n')
        fs.write('}\n')
        print_events(TITLE, events)
    finally:
        fg.close()
        fs.close()
        fl.close()
