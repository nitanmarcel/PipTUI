import webbrowser

import requests
from npyscreen import BoxTitle, Event

from . import INSTALLED


class PkgBox(BoxTitle):
    def create(self):
        self.display()
        self.values = INSTALLED
        self.update()

    def when_value_edited(self):
        self.parent.parentApp.queue_event(
            Event("event_package_select"))

    def open_in_browser(self):
        pkg = self.values[self.value].split()[0]
        request = requests.get('https://pypi.org/pypi/{}/json'.format(pkg))
        if request.status_code == 200:
            js_data = request.json()
            info = js_data.get('info')
            project_url = info.get('project_url')
            webbrowser.open(project_url)
        else:
            print('\a')

    def open_homepage(self):
        pkg = self.values[self.value].split()[0]
        request = requests.get('https://pypi.org/pypi/{}/json'.format(pkg))
        if request.status_code == 200:
            js_data = request.json()
            info = js_data.get('info')
            home_page = info.get('home_page')
            if home_page:
                webbrowser.open(home_page)
            else:
                print('\a')
        else:
            print('\a')
