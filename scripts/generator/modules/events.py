from .utils import delim, print_events, print_time, read_template

TITLE = 'Events'

te = read_template('./templates/event.txt')


@print_time(TITLE)
def events(out: str, ids_all: dict[str, list[dict[int, str]]], c: int):
    events = 0
    fo = open(f'{out}/events/eawse_events.txt', 'w', encoding='utf-8')

    try:
        fo.write('add_namespace = eaw_superevents\n\n')
        for cat, ids in ids_all.items():
            fo.write(f'# {delim} #\n# {cat}\n# {delim} #\n')
            for i, id in ids.items():
                fo.write(te(i=i, id=id.lower()))
                events += 1
                if events < c:
                    fo.write('\n')
        print_events(TITLE, events)
    finally:
        fo.close()
