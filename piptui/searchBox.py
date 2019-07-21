import re

import requests
from npyscreen import BoxTitle, TextCommandBox

from . import INSTALLED
from .run_threaded import threaded


class SearchBox(BoxTitle):
    _contained_widget = TextCommandBox


PYPI = []


@threaded
def get_pypi():
    global PYPI
    request = requests.get('https://pypi.org/simple/')
    if request.status_code == 200:
        data = request.text
        pattern = re.compile(r'    <a href=".+">(.+)</a>')
        PYPI = [pattern.match(line).group(1)
                for line in data.split("\n")[6:-2]]


class QueryPypi:
    def __init__(self):
        get_pypi()

    def process_command_complete(self, value, *args, **kwargs):
        if value.value == '':
            value.parent.PkgBoxObj.values = INSTALLED
            value.parent.PkgBoxObj.update()

    def process_command_live(self, value, **kwargs):
        packages = []
        if not value.value:
            value.parent.PkgBoxObj.values = INSTALLED
            value.parent.PkgBoxObj.update()
        else:
            query_pypi(mainbox=value.parent.PkgBoxObj, to_query=value.value)
            value.parent.PkgBoxObj.value = 0
            value.parent.PkgBoxObj.update()
            value.parent.InfoBoxObj.display_info()


def query_pypi(mainbox, to_query):
    global PYPI
    packages = []
    if not PYPI:
        request = requests.get('https://pypi.org/simple/')
        if request.status_code == 200:
            data = request.text
            pattern = re.compile(r'    <a href=".+">(.+)</a>')
            PYPI = [pattern.match(line).group(1)
                    for line in data.split("\n")[6:-2]]
    for pkg in PYPI:
        if to_query.lower() in pkg.lower():
            packages.append(pkg)
    mainbox.values = packages
    mainbox.update()
