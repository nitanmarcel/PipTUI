import subprocess
import sys
import requests
from . import __version__


def check_update():
    request = requests.get('https://pypi.org/pypi/PipTUI/json')
    if request.status_code == 200:
        json_data = request.json()
        release = max(json_data.get('releases'))
        if __version__.__version__ != release:
           question =  input("A new version is available! Do you wish to update? (y/n) ")
           if question.lower() in ('y', 'yes'):
               subprocess.run([sys.executable,
                                 '-m',
                                 'pip',
                                 'install',
                                 'PipTUI==' + release,
                                 '--user'])
               quit()