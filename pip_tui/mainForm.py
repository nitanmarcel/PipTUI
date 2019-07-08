import npyscreen
import curses
from .pkgBox import PkgBox
from .pkgInfoBox import PkgInfoBox
from .managerBox import ManagerBox


class MainForm(npyscreen.FormBaseNew):
    def create(self):
        exit_handlers = {'^Q': lambda x: exit(0),
                        155: lambda x: exit(0),
                        curses.ascii.ESC: lambda x: exit(0)}
        action_handlers = {'^R': lambda x: self.parentApp.switchForm("UNINSTALL"),
                           '^U': lambda x: self.parentApp.switchForm("UPDATE")
                            }

        self.add_handlers(exit_handlers)
        self.add_handlers(action_handlers)

        self.add_event_hander(
            "event_update_main_form",
            self.event_update_main_form)
        self.add_event_hander(
            'event_package_select',
            self.event_package_select)
        y, x = self.useable_space()
        self.PkgBoxObj = self.add(
            PkgBox,
            name="Installed Packages",
            value=0,
            relx=1,
            max_width=x // 5,
            rely=(y // 50))
        self.PkgBoxObj.update_pkgs_list()
        self.PkgInfoBoxObj = self.add(
            PkgInfoBox, rely=2, relx=(
                x // 5) + 1, max_height=-5)
        self.PkgInfoBoxObj.create()
        self.InstallBoxObj = self.add(ManagerBox, relx=(x // 5) + 1, rely=-7, max_height=-5)

    def event_update_main_form(self, event):
        self.display()
        self.PkgBoxObj.display()

    def event_package_select(self, event):
        current_selection = self.PkgBoxObj.value
        self.PkgInfoBoxObj.display_pkg_info()
