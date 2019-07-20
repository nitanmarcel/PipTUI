import requests
from npyscreen import BoxTitle, MultiLineEdit

from .run_threaded import threaded


class InfoBox(BoxTitle):
    _contained_widget = MultiLineEdit

    def create(self):
        self.display()

    @threaded
    def display_info(self):
        self.value = 'Loading package description!'
        self.update()
        current_selection = self.parent.parentApp.MainForm.PkgBoxObj.value
        pkg = self.parent.parentApp.MainForm.PkgBoxObj.values[current_selection].split()[
            0]
        request = requests.get('https://pypi.org/pypi/{}/json'.format(pkg))
        if request.status_code == 200:
            data = request.json()
            info = data.get('info')
            description = info.get('description')
            summary = info.get('summary')
            self.value = description or summary or "Package description unavailable"
        else:
            self.value = "Couldn't find this package on pypi.org! ERROR: " + \
                str(request.status_code)
        self.update()
