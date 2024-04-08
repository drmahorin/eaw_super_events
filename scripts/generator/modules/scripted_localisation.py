from .utils import delim, print_events, print_time

TITLE = 'Scripted localisation'


@print_time(TITLE)
def scripted_localisation(out: str, subids_all: dict[str, list[dict[int, str]]], c: int):
    events = 0
    cats = 0
    subcats = 0
    fi = open(f'{out}/common/scripted_localisation/eawse_sloc_i.txt', 'w', encoding='utf-8')
    ft = open(f'{out}/common/scripted_localisation/eawse_sloc_t.txt', 'w', encoding='utf-8')
    fa = open(f'{out}/common/scripted_localisation/eawse_sloc_a.txt', 'w', encoding='utf-8')
    fd = open(f'{out}/common/scripted_localisation/eawse_sloc_d.txt', 'w', encoding='utf-8')
    fe = open(f'{out}/common/scripted_localisation/eawse_sloc_e.txt', 'w', encoding='utf-8')
    fc = open(f'{out}/common/scripted_localisation/eawse_sloc_c.txt', 'w', encoding='utf-8')
    fs = open(f'{out}/common/scripted_localisation/eawse_sloc_s.txt', 'w', encoding='utf-8')

    def write_all(data: str):
        for f in (fi, ft, fa, fd):
            f.write(data)

    try:
        write_all('defined_text = {\n')
        fe.write('defined_text = {\n')
        fc.write('defined_text = {\n')
        fs.write('defined_text = {\n')

        fi.write('\tname = EAWSEGetEventImage\n')
        ft.write('\tname = EAWSEGetEventTitle\n')
        fa.write('\tname = EAWSEGetEventAnswer\n')
        fd.write('\tname = EAWSEGetEventDescription\n')
        fe.write('\tname = EAWSEGetEventEntry\n')
        fc.write('\tname = EAWSEGetEventCategoryImage\n')
        fs.write('\tname = EAWSEGetEventSubcategory\n')

        for cat, subs in subids_all.items():
            write_all(f'\t# {delim} #\n\t# {cat}\n\t# {delim} #\n')
            fe.write(f'\t# {delim} #\n\t# {cat}\n\t# {delim} #\n')
            fs.write(f'\t# {delim} #\n\t# {cat}\n\t# {delim} #\n')

            fc.write('\ttext = {\n')
            fc.write(f'\t\ttrigger = {{ check_variable = {{ eawse_category_id = {cats} }} }}\n')
            fc.write(f'\t\tlocalization_key = "GFX_EAWSE_{cat.upper()}"\n')
            fc.write('\t}\n')
            for sub, ids in subs.items():
                fs.write('\ttext = {\n')
                fs.write(f'\t\ttrigger = {{ check_variable = {{ eawse_subcategory_id = {subcats} }} }}\n')
                fs.write(f'\t\tlocalization_key = "{sub}"\n')
                fs.write('\t}\n')
                for i, id in ids.items():
                    write_all('\ttext = {\n')
                    fe.write('\ttext = {\n')

                    write_all(f'\t\ttrigger = {{ check_variable = {{ eawse_id = {i} }} }}\n')
                    fe.write(f'\t\ttrigger = {{ check_variable = {{ eawse_linear_id = {events} }} }}\n')

                    fi.write(f'\t\tlocalization_key = "GFX_{id}"\n')
                    ft.write(f'\t\tlocalization_key = "{id}_T"\n')
                    fa.write(f'\t\tlocalization_key = "{id}_A"\n')
                    fd.write(f'\t\tlocalization_key = "{id}_D"\n')
                    fe.write(f'\t\tlocalization_key = "{id}_TITLE"\n')

                    write_all('\t}\n')
                    fe.write('\t}\n')
                    events += 1
                subcats += 1
            cats += 1
        write_all('}\n')
        fe.write('}\n')
        fc.write('}\n')
        fs.write('}\n')
        print_events(TITLE, events)
    finally:
        fi.close()
        ft.close()
        fa.close()
        fd.close()
        fe.close()
        fc.close()
        fs.close()
