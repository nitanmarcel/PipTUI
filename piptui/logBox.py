import subprocess
import sys

import requests
from npyscreen import BoxTitle

from .run_threaded import threaded
from.settings import get_config_value


class LogBox(BoxTitle):
    @threaded
    def uninstall_pkg(self, pkg, current_selection):
        uninstalled = False
        self.refresh()
        proc = subprocess.Popen([sys.executable,
                                 '-m',
                                 'pip',
                                 'uninstall',
                                 pkg,
                                 '-y'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
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
            if not proc.poll() and not stdout and not stderr:
                if uninstalled is True:
                    self.parent.parentApp.MainForm.PkgBoxObj.values.pop(
                        current_selection)
                try:
                    self.uninstall_pkg.__thread__.join()
                except BaseException:
                    pass
                break

    @threaded
    def update_pkg(self, pkg, current_selection):
        updated = False
        self.refresh()
        cmd = [sys.executable,
               '-m',
               'pip',
               'install',
               pkg,
               '--upgrade']
        if get_config_value('use_user_arg', as_bool=True) is True:
            cmd.append('--user')
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
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
            if not proc.poll() and not stdout and not stderr:
                if updated is True:
                    data = requests.get(
                        'https://pypi.org/pypi/{}/json'.format(pkg))
                    if data.status_code == 200:
                        json_data = data.json()
                        releases = json_data.get("releases")
                        if releases:
                            self.parent.parentApp.MainForm.PkgBoxObj.values[current_selection] = pkg + " " + max(
                                releases)
                try:
                    self.uninstall_pkg.__thread__.join()
                except BaseException:
                    pass
                break

    @threaded
    def install_pkg(self, pkg, current_selection):
        global INSTALLED
        self.refresh()
        cmd = [sys.executable,
               '-m',
               'pip',
               'install',
               pkg,
               ]
        if get_config_value('use_user_arg', as_bool=True) is True:
            cmd.append('--user')
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        while True:
            stdout = proc.stdout.readline()
            stderr = proc.stderr.readline()
            if stdout:
                self.values.append(stdout.decode().strip())
                self.update()
            if stderr:
                self.values.append(stderr.decode().strip())
                self.update()
            if not proc.poll() and not stdout and not stderr:
                try:
                    self.uninstall_pkg.__thread__.join()
                except BaseException:
                    pass
                break

    def update_app(self):
        self.refresh()
        release = self.parent.parentApp.release
        cmd = [sys.executable,
               '-m',
               'pip',
               'install',
               'PipTUI==' + release]
        if get_config_value('use_user_arg', as_bool=True) is True:
            cmd.append('--user')
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        while True:
            stdout = proc.stdout.readline()
            stderr = proc.stderr.readline()
            if stdout:
                self.values.append(stdout.decode().strip())
                self.update()
            if stderr:
                self.values.append(stderr.decode().strip())
                self.update()
            if not proc.poll() and not stdout and not stderr:
                try:
                    self.uninstall_pkg.__thread__.join()
                except BaseException:
                    pass
                break

    def refresh(self):
        self.values = []
        self.update()
