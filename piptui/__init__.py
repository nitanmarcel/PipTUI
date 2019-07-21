import pkg_resources

from .run_threaded import threaded

INSTALLED = []


@threaded
def get_insalled():
    global INSTALLED
    for pkg in sorted(pkg_resources.working_set, key=lambda x: x.key):
        INSTALLED.append(str(pkg))


get_insalled()
