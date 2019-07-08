import npyscreen
import curses

class UninstallForm(npyscreen.ActionForm):
    def create(self):
        y, x = self.parentApp.MainForm.useable_space()
        self.show_atx = x // 2 - 10
        self.show_aty = y // 2 - 5
        exit_handlers = {'^Q': lambda: exit(0),
                        155: lambda: exit(0),
                        curses.ascii.ESC: lambda: exit(0)}
        self.add_handlers(exit_handlers)
        self.name = "Uninstall Pkg?"
        self.display()
    def on_ok(self):
        self.name = "Uninstall pkg?"
        current_selection = self.parentApp.MainForm.PkgBoxObj.value
        pkg = self.parentApp.MainForm.PkgBoxObj.values[current_selection].split()[0]
        self.parentApp.MainForm.InstallBoxObj.uninstall_package(pkg, current_selection)
        self.parentApp.switchForm('MAIN')
    def on_cancel(self):
        self.parentApp.switchForm('MAIN')

class UpdateForm(npyscreen.ActionForm):
    def create(self):
        y, x = self.parentApp.MainForm.useable_space()
        self.show_atx = x // 2 - 10
        self.show_aty = y // 2 - 5
        exit_handlers = {'^Q': lambda: exit(0),
                        155: lambda: exit(0),
                        curses.ascii.ESC: lambda: exit(0)}
        self.add_handlers(exit_handlers)
        self.name = "Update pkg?"
        self.display()
    def on_ok(self):
        current_selection = self.parentApp.MainForm.PkgBoxObj.value
        pkg = self.parentApp.MainForm.PkgBoxObj.values[current_selection].split()[0]
        self.parentApp.MainForm.InstallBoxObj.update_package(pkg, current_selection)
        self.parentApp.switchForm('MAIN')
    def on_cancel(self):
        self.parentApp.switchForm('MAIN')