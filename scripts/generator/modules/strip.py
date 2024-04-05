from .utils import print_events, print_time


@print_time('IDs')
def id_grabber(fi: list[str]) -> dict[int, str]:
    events = {}
    skip = 0
    for line in fi:
        if skip:
            skip -= 1
            continue

        if line.startswith('!!'):
            skip = 2
        elif line.startswith('!'):
            skip = 2
        else:
            line = line.split()
            events[int(line[0])] = line[1]
            skip = 8

    print_events('IDs', len(events))
    return dict(sorted(events.items()))


@print_time('SubIDs')
def subid_grabber(fi: list[str]) -> dict[str, dict[int, str]]:
    events = {}
    subid = ''
    skip = 0
    for line in fi:
        if skip:
            skip -= 1
            continue

        if line.startswith('!!'):
            skip = 2
        elif line.startswith('!'):
            # events[subid] = dict(sorted(events[subid].items()))
            subid = line[1:].strip()
            events[subid] = {}
            skip = 2
        else:
            line = line.split()
            if subid:
                events[subid][int(line[0])] = line[1]
            skip = 8

    print_events('SubIDs', len(events))
    return events


@print_time('AnimIDs')
def anim_grabber(fi: list[str]) -> dict[str, dict[int, str]]:
    events = {}
    skip = 0
    for line in fi:
        if skip:
            skip -= 1
            continue

        if line.startswith('!!'):
            skip = 2
        elif line.startswith('!'):
            skip = 2
        else:
            line = line.split()
            if len(line) == 3:
                events[int(line[0])] = int(line[2])
            skip = 8

    print_events('AnimIDs', len(events))
    return dict(sorted(events.items()))
