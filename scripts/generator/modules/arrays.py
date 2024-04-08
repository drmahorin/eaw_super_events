from .utils import print_events, print_time, read_template

TITLE = 'Arrays'

ta = read_template('./templates/arrays.txt')


@print_time(TITLE)
def arrays(out: str, subids_all: dict[str, list[dict[int, str]]], c: int):
    events = 0
    cats = 0
    subcats = 0
    fo = open(f'{out}/common/scripted_effects/eawse_arrays.txt', 'w', encoding='utf-8')

    with open('../../eawse.mod', 'r', encoding='utf-8') as fm:
        ver = fm.readline().split('=')[1][1:-2]
    ver = int(ver.replace('.', ''))

    setup = []
    for cat, subs in subids_all.items():
        cat_length = 0
        for ids in subs.values():
            cat_length += len(ids)
        setup.append(f'### {cat} ###')
        setup.append('for_loop_effect = {')
        setup.append(f'\tend = {cat_length}')
        setup.append('\tvalue = i')
        setup.append(f'\tadd_to_array = {{ global.eawse_events_categories = {cats} }}')
        setup.append('}')
        setup.append(f'add_to_array = {{ global.eawse_categories_bounds = {events} }}')
        for sub, ids in subs.items():
            setup.append(f'# {sub.lower()} #')
            setup.append('for_loop_effect = {')
            setup.append(f'\tend = {len(ids)}')
            setup.append('\tvalue = i')
            setup.append(f'\tadd_to_array = {{ global.eawse_events_subcategories = {subcats} }}')
            setup.append('}')
            for i, _ in ids.items():
                setup.append(f'add_to_array = {{ global.eawse_events_all = {i} }}')
                events += 1
            subcats += 1
        cats += 1
    setup.append('')
    setup.append(f'add_to_array = {{ global.eawse_categories_bounds = {events} }}')
    try:
        fo.write(ta(cats_size=len(subids_all), events=events, data='\n\t\t'.join(setup), ver=ver))
        print_events(TITLE, events)
    finally:
        fo.close()
