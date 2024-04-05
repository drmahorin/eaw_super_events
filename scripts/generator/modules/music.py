from .utils import delim, print_events, print_time, read_template

TITLE = 'Music'

ta = read_template('./templates/music_asset.txt')
tt = read_template('./templates/music_txt.txt')


@print_time(TITLE)
def music(out: str, ids_all: dict[str, list[dict[int, str]]], c: int):
    events = 0
    credits = {}
    with open(f'../../eawse/music_credits.txt', encoding='utf-8') as fc:
        for line in fc:
            line = line.strip()
            if not line:
                continue
            line = line.split(' - ', 1)
            credits[line[0]] = line[1]

    fa = open(f'{out}/music/eawse/eawse_sounds.asset', 'w', encoding='utf-8')
    ft = open(f'{out}/music/eawse/eawse_sounds.txt', 'w', encoding='utf-8')
    fe = open(f'{out}/localisation/english/eawse_music_l_english.yml', 'w', encoding='utf-8-sig')
    fr = open(f'{out}/localisation/russian/eawse_music_l_russian.yml', 'w', encoding='utf-8-sig')

    try:
        ft.write('music_station = "eawse"\n\n')
        fe.write('l_english:\n')
        fr.write('l_english:\n')
        for cat, ids in ids_all.items():
            fa.write(f'# {delim} #\n# {cat}\n# {delim} #\n\n')
            ft.write(f'# {delim} #\n# {cat}\n# {delim} #\n\n')
            fe.write(f'  # {delim} #\n  # {cat}\n  # {delim} #\n')
            fr.write(f'  # {delim} #\n  # {cat}\n  # {delim} #\n')

            for id in ids.values():
                id = id.lower()
                fa.write(ta(id=id))
                ft.write(tt(id=id))
                fe.write(f'  {id}: "{credits[id]}"\n')
                fr.write(f'  {id}: "{credits[id]}"\n')

                events += 1
                if events < c:
                    fa.write('\n')
                    ft.write('\n')
        print_events(TITLE, events)
    finally:
        fa.close()
        ft.close()
        fe.close()
        fr.close()
