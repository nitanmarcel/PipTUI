import curses

from npyscreen import ActionForm


class UninstallForm(ActionForm):
    CANCEL_BUTTON_BR_OFFSET = (2, 45)
    OK_BUTTON_BR_OFFSET = (2, 5)
    CANCEL_BUTTON_TEXT = 'Cancel'
    OK_BUTTON_TEXT = 'Uninstall'

    def create(self):
        y, x = self.parentApp.MainForm.useable_space()
        self.show_atx = x // 2 - 10
        self.show_aty = y // 2 - 5
        self.name = "Uninstall Package?"

        exit_handlers = {'^Q': lambda: exit(0),
                         155: lambda: exit(0),
                         curses.ascii.ESC: lambda: exit(0)}
        self.add_handlers(exit_handlers)
        self.display()

    def on_ok(self):
        current_selection = self.parentApp.MainForm.PkgBoxObj.value
        pkg = self.parentApp.MainForm.PkgBoxObj.values[current_selection].split()[
            0]
        self.parentApp.MainForm.LogBoxObj.uninstall_pkg(pkg, current_selection)
        self.parentApp.switchForm('MAIN')

    def on_cancel(self):
        self.parentApp.switchForm('MAIN')


class UpdateForm(ActionForm):
    CANCEL_BUTTON_BR_OFFSET = (2, 45)
    OK_BUTTON_BR_OFFSET = (2, 5)
    CANCEL_BUTTON_TEXT = 'Cancel'
    OK_BUTTON_TEXT = 'Update'

    def create(self):
        y, x = self.parentApp.MainForm.useable_space()
        self.show_atx = x // 2 - 10
        self.show_aty = y // 2 - 5
        self.name = "Update Package?"

        exit_handlers = {'^Q': lambda: exit(0),
                         155: lambda: exit(0),
                         curses.ascii.ESC: lambda: exit(0)}
        self.add_handlers(exit_handlers)
        self.display()

    def on_ok(self):
        current_selection = self.parentApp.MainForm.PkgBoxObj.value
        pkg = self.parentApp.MainForm.PkgBoxObj.values[current_selection].split()[
            0]
        self.parentApp.MainForm.LogBoxObj.update_pkg(pkg, current_selection)
        self.parentApp.switchForm('MAIN')

    def on_cancel(self):
        self.parentApp.switchForm('MAIN')


class InstallForm(ActionForm):
    CANCEL_BUTTON_BR_OFFSET = (2, 45)
    OK_BUTTON_BR_OFFSET = (2, 5)
    CANCEL_BUTTON_TEXT = 'Cancel'
    OK_BUTTON_TEXT = 'Install'

    def create(self):
        y, x = self.parentApp.MainForm.useable_space()
        self.show_atx = x // 2 - 10
        self.show_aty = y // 2 - 5
        self.name = "Install Release?"

        exit_handlers = {'^Q': lambda: exit(0),
                         155: lambda: exit(0),
                         curses.ascii.ESC: lambda: exit(0)}
        self.add_handlers(exit_handlers)
        self.display()

    def on_ok(self):
        current_selection = self.parentApp.MainForm.PkgBoxObj.value
        pkg = self.parentApp.MainForm.PkgBoxObj.values[current_selection].split()[
            0]
        self.parentApp.MainForm.LogBoxObj.install_pkg(pkg, current_selection)
        self.parentApp.switchForm('MAIN')

    def on_cancel(self):
        self.parentApp.switchForm('MAIN')


class InstallVersionForm(ActionForm):
    CANCEL_BUTTON_BR_OFFSET = (2, 45)
    OK_BUTTON_BR_OFFSET = (2, 5)
    CANCEL_BUTTON_TEXT = 'Cancel'
    OK_BUTTON_TEXT = 'Install'

    def create(self):
        y, x = self.parentApp.MainForm.useable_space()
        self.show_atx = x // 2 - 10
        self.show_aty = y // 2 - 5
        self.name = "Install Package?"

        exit_handlers = {'^Q': lambda: exit(0),
                         155: lambda: exit(0),
                         curses.ascii.ESC: lambda: exit(0)}
        self.add_handlers(exit_handlers)
        self.display()

    def on_ok(self):
        current_selection = self.parentApp.PkgInfoForm.releases.value
        version = self.parentApp.PkgInfoForm.releases.values[current_selection].split()[
            0]
        pkg = self.parentApp.PkgInfoForm.pkg_name.value + '==' + version
        self.parentApp.MainForm.LogBoxObj.install_pkg(pkg, current_selection)
        self.parentApp.switchForm('MAIN')

    def on_cancel(self):
        self.parentApp.switchForm('PKG_INFO')


class UpdateAppForm(ActionForm):
    CANCEL_BUTTON_BR_OFFSET = (2, 45)
    OK_BUTTON_BR_OFFSET = (2, 5)
    CANCEL_BUTTON_TEXT = 'Cancel'
    OK_BUTTON_TEXT = 'Update'

    def create(self):
        y, x = self.parentApp.MainForm.useable_space()
        self.show_atx = x // 2 - 10
        self.show_aty = y // 2 - 5
        self.name = "Update App?"

        exit_handlers = {'^Q': lambda: exit(0),
                         155: lambda: exit(0),
                         curses.ascii.ESC: lambda: exit(0)}
        self.add_handlers(exit_handlers)
        self.display()

    def on_ok(self):
        self.parentApp.MainForm.LogBoxObj.update_app()
        self.parentApp.switchForm('MAIN')

    def on_cancel(self):
        self.parentApp.switchForm('MAIN')
