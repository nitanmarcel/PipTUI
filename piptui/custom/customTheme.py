import curses
import json
from piptui.settings import get_config_value, THEME_FOLDER

from npyscreen import ThemeManager

TRANSPARENT_KEYS = [
    'GREEN_ON_DEFAULT',
    'BLUE_ON_DEFAULT',
    'BLACK_ON_DEFAULT',
    'CYAN_ON_DEFAULT',
    'MAGENTA_ON_DEFAULT',
    'YELLOW_ON_DEFAULT',
    'WHITE_ON_DEFAULT',
    'RED_ON_DEFAULT']
DEFAULT_COLORS = json.load(open(THEME_FOLDER + get_config_value('theme')))
HAS_TRANSPARENT = False


HAS_TRANSPARENT = any(color in DEFAULT_COLORS.values()
                      for color in TRANSPARENT_KEYS)


class PipTuiTheme(ThemeManager):

    default_colors = {
        'DEFAULT': 'WHITE_BLACK',
        'FORMDEFAULT': 'WHITE_BLACK',
        'NO_EDIT': 'BLUE_BLACK',
        'STANDOUT': 'CYAN_BLACK',
        'CURSOR': 'WHITE_BLACK',
        'CURSOR_INVERSE': 'BLACK_WHITE',
        'LABEL': 'GREEN_BLACK',
        'LABELBOLD': 'WHITE_BLACK',
        'CONTROL': 'YELLOW_BLACK',
        'IMPORTANT': 'GREEN_BLACK',
        'SAFE': 'GREEN_BLACK',
        'WARNING': 'YELLOW_BLACK',
        'DANGER': 'RED_BLACK',
        'CRITICAL': 'BLACK_RED',
        'GOOD': 'GREEN_BLACK',
        'GOODHL': 'GREEN_BLACK',
        'VERYGOOD': 'BLACK_GREEN',
        'CAUTION': 'YELLOW_BLACK',
        'CAUTIONHL': 'BLACK_YELLOW',
    }

    _colors_to_define = (
        ('BLACK_WHITE', curses.COLOR_BLACK, curses.COLOR_WHITE),
        ('BLUE_BLACK', curses.COLOR_BLUE, curses.COLOR_BLACK),
        ('CYAN_BLACK', curses.COLOR_CYAN, curses.COLOR_BLACK),
        ('GREEN_BLACK', curses.COLOR_GREEN, curses.COLOR_BLACK),
        ('MAGENTA_BLACK', curses.COLOR_MAGENTA, curses.COLOR_BLACK),
        ('RED_BLACK', curses.COLOR_RED, curses.COLOR_BLACK),
        ('YELLOW_BLACK', curses.COLOR_YELLOW, curses.COLOR_BLACK),
        ('BLACK_RED', curses.COLOR_BLACK, curses.COLOR_RED),
        ('BLACK_GREEN', curses.COLOR_BLACK, curses.COLOR_GREEN),
        ('BLACK_YELLOW', curses.COLOR_BLACK, curses.COLOR_YELLOW),
        ('BLUE_WHITE', curses.COLOR_BLUE, curses.COLOR_WHITE),
        ('CYAN_WHITE', curses.COLOR_CYAN, curses.COLOR_WHITE),
        ('GREEN_WHITE', curses.COLOR_GREEN, curses.COLOR_WHITE),
        ('MAGENTA_WHITE', curses.COLOR_MAGENTA, curses.COLOR_WHITE),
        ('RED_WHITE', curses.COLOR_RED, curses.COLOR_WHITE),
        ('YELLOW_WHITE', curses.COLOR_YELLOW, curses.COLOR_WHITE)
    )

    if HAS_TRANSPARENT is True:
        _colors_to_define = _colors_to_define + (('BLACK_ON_DEFAULT', curses.COLOR_BLACK, -1),
                                                 ('WHITE_ON_DEFAULT', curses.COLOR_WHITE, -1),
                                                 ('BLUE_ON_DEFAULT', curses.COLOR_BLUE, -1),
                                                 ('CYAN_ON_DEFAULT', curses.COLOR_CYAN, -1),
                                                 ('GREEN_ON_DEFAULT', curses.COLOR_GREEN, -1),
                                                 ('MAGENTA_ON_DEFAULT', curses.COLOR_MAGENTA, -1),
                                                 ('RED_ON_DEFAULT', curses.COLOR_RED, -1),
                                                 ('YELLOW_ON_DEFAULT', curses.COLOR_YELLOW, -1))
    default_colors = DEFAULT_COLORS or default_colors

    def __init__(self, *args, **kwargs):
        if HAS_TRANSPARENT is True:
            curses.use_default_colors()
        super(PipTuiTheme, self).__init__(*args, **kwargs)
