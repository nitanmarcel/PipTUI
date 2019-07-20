import collections

from npyscreen import StandardApp, apNPSApplicationEvents


class PipTuiEvents(object):
    def __init__(self):
        self.interal_queue = collections.deque()
        super(apNPSApplicationEvents).__init__()

    def get(self, maximum=None):
        if maximum is None:
            maximum = -1
        counter = 1
        while counter != maximum:
            try:
                yield self.interal_queue.pop()
            except IndexError:
                pass
            counter += 1


class PipTuiApp(StandardApp):
    def __init__(self):
        super(StandardApp, self).__init__()
        self.event_directory = {}
        self.event_queues = {}
        self.initalize_application_event_queues()
        self.initialize_event_handling()

    def process_event_queues(self, max_events_per_queue=None):
        for queue in self.event_queues.values():
            try:
                for event in queue.get(maximum=max_events_per_queue):
                    try:
                        self.process_event(event)
                    except StopIteration:
                        pass
            except RuntimeError:
                pass
