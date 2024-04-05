from .utils import delim, print_events, print_time

TITLE = 'Localisation'

languages = (
    'english',
    'russian',
)


@print_time(TITLE)
def localisation(out: str, cat: str, fi: list[str], c: int):
    files = {}

    with open('../../eawse.mod', 'r', encoding='utf-8') as fm:
        ver = fm.readline().split('=')[1][1:-2]

    for lang in languages:
        with open(f'{out}/localisation/{lang}/eawse_cake_l_{lang}.yml', 'w', encoding='utf-8-sig') as fc:
            fc.write(f'l_{lang}:\n  EAWSE_SETTINGS_CAKE: "EaW SE v.{ver}"\n')
        
    for lang in languages:
        files[lang] = open(
            f'{out}/localisation/{lang}/eawse_{cat}_l_{lang}.yml', 'w', encoding='utf-8-sig'
        )

    def write_all(data: str):
        for file in files.values():
            file.write(data)

    try:
        events = 0
        for lang, file in files.items():
            file.write(f'l_{lang}:\n')

        cat_i = 0
        event = ''
        event_i = 0

        for line in fi:
            if line.startswith('!!'):
                line = line[2:]
                write_all(f'  {line}: ')
                cat_i = 1
            elif line.startswith('!'):
                line = line[1:]
                write_all(f'  # {delim} #\n  {line}: ')
                cat_i = 1
            elif cat_i:
                lang = languages[cat_i - 1]
                files[lang].write(f'"{line}"\n\n')
                if cat_i == len(languages):
                    cat_i = 0
                else:
                    cat_i += 1

            elif not event_i:
                event = line.split()[1]
                event_i = 1
                events += 1
            elif event_i:
                lang = languages[(event_i - 1) // 4]
                match (event_i - 1) % 4:
                    case 0:
                        files[lang].write(f'  {event}_TITLE: "{line}"\n')
                    case 1:
                        files[lang].write(f'  {event}_T: "{line}"\n')
                    case 2:
                        files[lang].write(f'  {event}_A: "{line}"\n')
                    case 3:
                        files[lang].write(f'  {event}_D: "{line}"\n')
                if event_i == len(languages) * 4:
                    if events < c:
                        write_all('\n')
                    event_i = 0
                else:
                    event_i += 1

        print_events(TITLE, events)
    finally:
        for file in files.values():
            file.close()
