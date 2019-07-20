import functools
from threading import Thread


def threaded(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        wrapper.__thread__ = thread
        try:
            thread.start()
        except KeyboardInterrupt:
            thread.stop()
        return thread

    return wrapper
