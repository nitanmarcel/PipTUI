from npyscreen import BoxTitle, Event

from . import INSTALLED


class PkgBox(BoxTitle):
    def create(self):
        self.display()
        self.values = INSTALLED
        self.update()

    def when_value_edited(self):
        self.parent.parentApp.queue_event(
            Event("event_package_select"))
