import npyscreen
import requests

from .run_threaded import threaded


class PkgInfoBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

    def create(self):
        self.display()

    @threaded
    def display_pkg_info(self):
        self.value = "Loading package description!"
        self.update()
        current_selection = self.parent.parentApp.MainForm.PkgBoxObj.value
        pkg = self.parent.parentApp.MainForm.PkgBoxObj.values[current_selection].split()[0]
        data = requests.get('https://pypi.org/pypi/{}/json'.format(pkg))
        if data.status_code == 200:
            js_data = data.json()
            info = js_data.get('info')
            description = info.get('description')
            summary = info.get('summary')
            self.value = description or summary or "Package description unavailable"
        elif data.status_code == 404:
            self.value = "Couldn't find this package on pypi.org!"
        self.update()
