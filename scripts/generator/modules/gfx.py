from .utils import print_events, print_time, read_template

TITLE = 'GFX'

tg = read_template('./templates/gfx.txt')
ta = read_template('./templates/gfx_animated.txt')


@print_time(TITLE)
def gfx(out: str, cat: str, ids: dict[int, str], anim_ids: dict[int, int], c: int):
    fo = open(f'{out}/interface/eawse_gfx/eawse_{cat}.gfx', 'w', encoding='utf-8')

    try:
        cat_id = f'eawse_category_{cat}'
        events = 0
        fo.write('spriteTypes = {\n')
        fo.write(tg(id=f'{cat_id}', fn=f'interface/topbar/superevents/{cat_id}'))
        fo.write('\n')
        for i, id in ids.items():
            if i in anim_ids:
                fo.write(ta(id=id.lower(), fn=f'eawse/{id.lower()}', frames=anim_ids[i]))
            else:
                fo.write(tg(id=id.lower(), fn=f'eawse/{id.lower()}'))
            events += 1
            if events < c:
                fo.write('\n')
        fo.write('}\n')
        print_events(TITLE, events)
    finally:
        fo.close()
