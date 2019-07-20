import curses

from npyscreen import ActionForm


class UninstallForm(ActionForm):
    def create(self):
        y, x = self.parentApp.MainForm.useable_space()
        self.show_atx = x // 2 - 10
        self.show_aty = y // 2 - 5
        self.name = "Uninstall Pkg?"

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
    def create(self):
        y, x = self.parentApp.MainForm.useable_space()
        self.show_atx = x // 2 - 10
        self.show_aty = y // 2 - 5
        self.name = "Update Pkg?"

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
    def create(self):
        y, x = self.parentApp.MainForm.useable_space()
        self.show_atx = x // 2 - 10
        self.show_aty = y // 2 - 5
        self.name = "Install Pkg?"

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
