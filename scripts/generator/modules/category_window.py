from .utils import read_template

tcw = read_template('./templates/superevent_category_window.txt')

def category_window(out: str, cat_count: int):
    with open(f'{out}/interface/eawse_settings/eawse_category_window.gui', 'w', encoding='utf-8') as fo:
        fo.write(tcw(y = 120 * cat_count))
