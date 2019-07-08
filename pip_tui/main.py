from .mainForm import MainForm
from .actionForms import UninstallForm, UpdateForm
from .custom.apNPSApplicationEvents import PipTuiApp

class App(PipTuiApp):
    def onStart(self):
        self.MainForm = self.addForm("MAIN", MainForm)
        self.UninstallForm = self.addForm("UNINSTALL", UninstallForm, lines=5, columns=20)
        self.UpdateForm = self.addForm("UPDATE", UpdateForm, lines=5, columns=20)


def main():
    App().run()

if __name__ == "__main__":
    main()
