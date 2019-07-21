from npyscreen import setTheme

from .actionForms import InstallForm, InstallVersionForm, UninstallForm, UpdateForm
from .custom.apNPSApplicationEvents import PipTuiApp
from .custom.customTheme import PipTuiTheme
from .mainForm import MainForm
from .pkgInfoForm import PkgInfoForm


class App(PipTuiApp):
    def onStart(self):
        setTheme(PipTuiTheme)
        self.MainForm = self.addForm("MAIN", MainForm)
        self.InstallForm = self.addForm(
            "INSTALL", InstallForm, lines=5, columns=20)
        self.InstallVersionForm = self.addForm(
            "INSTALL_VERSION", InstallVersionForm, lines=5, columns=20)
        self.UninstallForm = self.addForm(
            "UNINSTALL", UninstallForm, lines=5, columns=20)
        self.UpdateForm = self.addForm(
            "UPDATE", UpdateForm, lines=5, columns=20)
        self.PkgInfoForm = self.addForm('PKG_INFO',PkgInfoForm)


def main():
    App().run()


if __name__ == "__main__":
    main()
