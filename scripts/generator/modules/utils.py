import time

delim = '-' * 40

def print_events(title: str, events: int):
    print(f'{title}: {events} events')

def print_time(title: str) -> int:
    def decorator(func):
        def wrapper(*args, **kwargs):
            stime = time.time()
            value = func(*args, **kwargs)
            ttime = time.time() - stime
            print("%s: %.3f ms" % (title, ttime * 1000))
            return value
        return wrapper
    return decorator

def read_template(fn: str) -> callable:
    data = ''
    with open(fn, 'r', encoding='utf-8') as f:
        data = f.read()
    return data.format
