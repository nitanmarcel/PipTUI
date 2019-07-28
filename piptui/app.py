import requests
import re
from npyscreen import setTheme

from .actionForms import InstallForm, InstallVersionForm, UninstallForm, UpdateForm, UpdateAppForm
from .custom.apNPSApplicationEvents import PipTuiApp
from .custom.customTheme import PipTuiTheme
from .mainForm import MainForm
from .pkgInfoForm import PkgInfoForm
from .settingsForm import SettingsForm
from . import __version__
from .run_threaded import threaded
from .settings import get_config_value


class App(PipTuiApp):
    def onStart(self):
        setTheme(PipTuiTheme)
        self.release = __version__.__version__
        self.MainForm = self.addForm("MAIN", MainForm)
        self.InstallForm = self.addForm(
            "INSTALL", InstallForm, lines=6, columns=26)
        self.InstallVersionForm = self.addForm(
            "INSTALL_VERSION", InstallVersionForm, lines=6, columns=26)
        self.UninstallForm = self.addForm(
            "UNINSTALL", UninstallForm, lines=6, columns=26)
        self.UpdateForm = self.addForm(
            "UPDATE", UpdateForm, lines=6, columns=26)
        self.PkgInfoForm = self.addForm('PKG_INFO', PkgInfoForm)

        self.UpdateAppForm = self.addForm(
            'APP_UPDATE', UpdateAppForm, lines=6, columns=26)
        self.SettingsForm = self.addForm('SETTINGS', SettingsForm)
        if get_config_value('check_for_update') is True:
            self.check_for_update()

    @threaded
    def check_for_update(self):
        request = requests.get('https://pypi.org/pypi/PipTUI/json')
        if request.status_code == 200:
            json_data = request.json()
            self.release = max(
                list(
                    json_data.get('releases')),
                key=self.major_minor_micro)
            if __version__.__version__ != self.release:
                self.switchForm("APP_UPDATE")

    def major_minor_micro(self, version):
        major, minor, micro = re.search(
            r'(\d+)\.(\d+)\.(\d+)', version).groups()
        return int(major), int(minor), int(micro)


def main():
    App().run()


if __name__ == "__main__":
    main()
