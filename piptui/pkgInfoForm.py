import curses

import requests
from npyscreen import ActionForm, TitleMultiLine, TitleText


class PkgInfoForm(ActionForm):
    def create(self):
        self.name = 'Package Info!'
        exit_handlers = {'^Q': lambda x: exit(0),
                         155: lambda x: exit(0),
                         curses.ascii.ESC: lambda x: exit(0)}

        self.add_handlers(exit_handlers)

        self.pkg_name = self.add(
            TitleText,
            name='Package Name:',
            editable=False)
        self.author = self.add(TitleText, name='Author:', editable=False)
        self.version = self.add(TitleText, name='Version:', editable=False)
        self.size = self.add(TitleText, name='Size:', editable=False)
        self.license = self.add(TitleText, name='License:', editable=False)
        self._new_line = self.add(TitleText, name='\n', editable=False)
        self.releases = self.add(
            TitleMultiLine,
            name='Releases:',
            max_height=5,
            scroll_exit=True)

    def update(self):
        current_selection = self.parentApp.MainForm.PkgBoxObj.value
        pkg = self.parentApp.MainForm.PkgBoxObj.values[current_selection].split()[
            0]
        request = requests.get('https://pypi.org/pypi/{}/json'.format(pkg))
        if request.status_code == 200:
            js_data = request.json()
            info = js_data.get('info')

            self.pkg_name.value = pkg
            self.author.value = info.get('author', '')
            self.version.value = info.get('version', '')

            releases = js_data.get('releases', '')
            self.size.value = self.get_max_release_size(releases)
            self.license.value = info.get('license', '')
            self.releases.values = [release for release in releases.keys()]

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
