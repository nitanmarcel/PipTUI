import curses

from .custom.customForm import FormBaseNewHinted
from .infoBox import InfoBox
from .logBox import LogBox
from .pkgBox import PkgBox
from .searchBox import QueryPypi, SearchBox


class MainForm(FormBaseNewHinted):
    def create(self):
        exit_handlers = {'^Q': lambda x: exit(0),
                         155: lambda x: exit(0),
                         curses.ascii.ESC: lambda x: exit(0)}
        action_handlers = {
            '^A': lambda x: self.parentApp.switchForm("INSTALL"),
            '^R': lambda x: self.parentApp.switchForm("UNINSTALL"),
            '^U': lambda x: self.parentApp.switchForm("UPDATE"),
            '^O': lambda x: self.PkgBoxObj.open_in_browser(),
            '^H': lambda x: self.PkgBoxObj.open_homepage(),
            '^D': lambda x: self.show_details_form(),
            curses.KEY_F1: lambda x: self.parentApp.switchForm("SETTINGS")}

        self.add_handlers(exit_handlers)
        self.add_handlers(action_handlers)
        self.add_event_hander(
            'event_package_select',
            self.event_package_select)

        y, x = self.useable_space()

        self.PkgBoxObj = self.add(PkgBox,
                                  name="Packages",
                                  value=0, relx=1, max_width=x // 5, rely=0,
                                  max_height=-5)

        self.InfoBoxObj = self.add(
            InfoBox, name='Description', rely=0, relx=(
                x // 5) + 1, max_height=-5)
        self.SearchBoxObj = self.add(
            SearchBox,
            name="Search",
            value=0,
            relx=1,
            max_width=x // 5,
            max_height=-5,
        )

        self.LogBoxObj = self.add(LogBox, name='Pip Log', relx=(
            x // 5) + 1, rely=-7, max_height=0)

        self.action_controller = QueryPypi

        self.display()
        self.PkgBoxObj.create()
        self.InfoBoxObj.create()

    def event_package_select(self, *args, **kwargs):
        self.InfoBoxObj.display_info()

    def show_details_form(self, *args, **kwargs):
        self.parentApp.getForm("PKG_INFO").update()
        self.parentApp.switchForm("PKG_INFO")
