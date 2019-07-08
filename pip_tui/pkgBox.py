import npyscreen
import pkg_resources

from .run_threaded import threaded


class PkgBox(npyscreen.BoxTitle):
    def when_value_edited(self):
        self.parent.parentApp.queue_event(
            npyscreen.Event("event_package_select"))


    def update_pkgs_list(self):
        if not self.values:
            self.get_pkg_list()
            self.parent.parentApp.queue_event(
                npyscreen.Event("event_update_main_form"))
        else:
            self.values = []
            self.get_pkg_list()
            self.update()

    @threaded
    def get_pkg_list(self):
        self.values = []
        for pkg in sorted(pkg_resources.working_set, key=lambda x: x.key):
            self.values.append(str(pkg))
