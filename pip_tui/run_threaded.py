import functools
from threading import Thread


def threaded(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        wrapper.__thread__ = thread
        return thread
    return wrapper
