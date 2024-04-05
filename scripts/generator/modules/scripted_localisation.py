from .utils import delim, print_events, print_time

TITLE = 'Scripted localisation'


@print_time(TITLE)
def scripted_localisation(out: str, ids_all: dict[str, list[dict[int, str]]], c: int):
    events = 0
    fi = open(f'{out}/common/scripted_localisation/eawse_sloc_i.txt', 'w', encoding='utf-8')
    ft = open(f'{out}/common/scripted_localisation/eawse_sloc_t.txt', 'w', encoding='utf-8')
    fa = open(f'{out}/common/scripted_localisation/eawse_sloc_a.txt', 'w', encoding='utf-8')
    fd = open(f'{out}/common/scripted_localisation/eawse_sloc_d.txt', 'w', encoding='utf-8')

    def write_all(data: str):
        for f in (fi, ft, fa, fd):
            f.write(data)

    try:
        write_all('defined_text = {\n')
        fi.write('\tname = EAWSEGetEventImage\n')
        ft.write('\tname = EAWSEGetEventTitle\n')
        fa.write('\tname = EAWSEGetEventAnswer\n')
        fd.write('\tname = EAWSEGetEventDescription\n')

        for cat, ids in ids_all.items():
            write_all(f'\t# {delim} #\n\t# {cat}\n\t# {delim} #\n')
            for i, id in ids.items():
                write_all('\ttext = {\n')
                write_all(f'\t\ttrigger = {{ check_variable = {{ EAWSE_super_event = {i} }} }}\n')
                fi.write(f'\t\tlocalization_key = "GFX_{id.lower()}"\n')
                ft.write(f'\t\tlocalization_key = "{id}_T"\n')
                fa.write(f'\t\tlocalization_key = "{id}_A"\n')
                fd.write(f'\t\tlocalization_key = "{id}_D"\n')
                write_all('\t}\n')

                events += 1
        write_all('}\n')
        print_events(TITLE, events)
    finally:
        fi.close()
        ft.close()
        fa.close()
        fd.close()
