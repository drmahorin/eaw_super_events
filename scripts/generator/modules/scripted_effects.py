from .utils import delim, print_events, print_time

TITLE = 'Scripted effects'


@print_time(TITLE)
def scripted_effects(out: str, ids_all: dict[str, list[dict[int, str]]], c: int):
    events = 0
    fo = open(f'{out}/common/scripted_effects/eawse_effect.txt', 'w', encoding='utf-8')

    try:
        fo.write('EAWSE_show_super_event = {\n')
        fo.write('\tset_variable = { EAWSE_super_event = EAWSE_temp_super_event }\n')
        for cat, ids in ids_all.items():
            fo.write(f'\t# {delim} #\n\t# {cat}\n\t# {delim} #\n')
            for i, id in ids.items():
                if events:
                    fo.write('\telse_if = {\n')
                else:
                    fo.write('\tif = {\n')
                fo.write(f'\t\tlimit = {{ check_variable = {{ EAWSE_temp_super_event = {i} }} }}\n')
                fo.write(f'\t\tplay_song = "{id.lower()}"\n\t}}\n')
                events += 1
        print_events(TITLE, events)
        fo.write('}\n')
    finally:
        fo.close()
