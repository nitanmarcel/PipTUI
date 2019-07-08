import npyscreen
import subprocess
import sys
import requests
from .run_threaded import threaded

class ManagerBox(npyscreen.BoxTitle):

    @threaded
    def uninstall_package(self, pkg, current_selection=None):
        uninstalled = False
        if self.values:
            self.values = []
            self.update()
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'uninstall', pkg, '-y'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            stdout = proc.stdout.readline()
            stderr = proc.stderr.readline()
            if stdout:
                self.values.append(stdout.decode().strip())
                self.update()
                uninstalled = True
            if stderr:
                self.values.append(stderr.decode().strip())
                self.update()
                uninstalled = False
            if proc.poll() is not None and not stdout and not stderr:
                if current_selection and uninstalled is True:
                    self.parent.parentApp.MainForm.PkgBoxObj.values.pop(current_selection)
                    if not self.uninstall_package.__thread__.isAlive():
                        self.uninstall_package.__thread__.join()
                break

        ret_value = proc.poll()

    @threaded
    def update_package(self, pkg, current_selection=None):
        updated = False
        if self.values:
            self.values = []
            self.update()
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'install', pkg, '--upgrade', '--user'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            stdout = proc.stdout.readline()
            stderr = proc.stderr.readline()
            if stdout:
                self.values.append(stdout.decode().strip())
                self.update()
                updated = True
            if stderr:
                self.values.append(stderr.decode().strip())
                self.update()
                updated = False
            if proc.poll() is not None and not stdout and not stderr:
                if current_selection and updated is True:
                    data = requests.get('https://pypi.org/pypi/{}/json'.format(pkg))
                    if data.status_code == 200:
                        json_data = data.json()
                        releases = json_data.get("releases")
                        if releases:
                            self.parent.parentApp.MainForm.PkgBoxObj.values[current_selection] = pkg + " " + max(releases)
                    if not self.update_package.__thread__.isAlive():
                        self.update_package.__thread__.join()
                break

        ret_value = proc.poll()

