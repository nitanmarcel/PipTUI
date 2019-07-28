import curses
import site

import requests
from . import INSTALLED
from .run_threaded import threaded
from npyscreen import TitleMultiLine, TitleText
from .custom.customForm import ActionFormHinted


class PkgInfoForm(ActionFormHinted):
    def create(self):
        self.name = 'Package Info!'
        exit_handlers = {
            '^Q': lambda x: self.parentApp.switchForm('MAIN'),
            155: lambda x: self.parentApp.switchForm('MAIN'),
            curses.ascii.ESC: lambda x: self.parentApp.switchForm('MAIN')}

        self.add_handlers(exit_handlers)
        self.add_handlers(
            {'^A': lambda x: self.parentApp.switchForm('INSTALL_VERSION')})

        self.pkg_name = self.add(
            TitleText,
            name='Package Name:',
            editable=False)
        self.version = self.add(TitleText, name='Version:', editable=False)
        self.size = self.add(TitleText, name='Size:', editable=False)
        self.summary = self.add(TitleText, name='Summary:', editable=False)
        self.home_page = self.add(TitleText, name='Home-Page:', editable=False)
        self.author = self.add(TitleText, name='Author:', editable=False)
        self.author_email = self.add(
            TitleText, name='Author Email:', editable=False)
        self.license = self.add(TitleText, name='License:', editable=False)
        self.location = self.add(TitleText, name='Location:', editable=False)
        self._new_line = self.add(TitleText, name='\n', editable=False)
        self.releases = self.add(
            TitleMultiLine,
            name='Releases:',
            max_height=5,
            scroll_exit=True)

    @threaded
    def update(self):
        current_selection = self.parentApp.MainForm.PkgBoxObj.value
        pkg = self.parentApp.MainForm.PkgBoxObj.values[current_selection].split()[
            0]
        request = requests.get('https://pypi.org/pypi/{}/json'.format(pkg))
        if request.status_code == 200:
            js_data = request.json()
            info = js_data.get('info')
            releases = js_data.get('releases', '')

            self.pkg_name.value = pkg
            self.version.value = info.get('version', '')
            self.size.value = self.get_max_release_size(releases)
            self.summary.value = info.get('summary', '')
            self.home_page.value = info.get('home_page', '')
            self.author.value = info.get('author', '')
            self.author_email.value = info.get('author_email', '')

            self.license.value = info.get('license', '')
            for package in INSTALLED:
                if pkg == package.split()[0]:
                    self.location.value = site.getusersitepackages()
            self.releases.values = [release for release in releases]
            self.releases.value = 0
        else:
            print('\a')
        self.display()

    def on_ok(self):
        self.parentApp.switchForm('MAIN')

    def on_cancel(self):
        self.parentApp.switchForm('MAIN')

    def get_max_release_size(self, data):
        latest = max(data.items())
        lst = latest[1]
        size = lst[0].get('size')

        power = 2**10
        n = 0
        units = {
            0: '',
            1: 'kilobytes',
            2: 'megabytes',
            3: 'gigabytes',
            4: 'terabytes'}
        while size > power:
            size /= power
            n += 1
        final_size = round(size, 2), units[n]
        return str(final_size[0]) + ' ' + str(final_size[1])
