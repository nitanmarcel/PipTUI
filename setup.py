from setuptools import find_packages, setup
from setuptools.command.install import install
from piptui import __version__
from pathlib import Path
import os

requirements = ['npyscreen', 'requests', 'windows-curses; sys_platform == "win32"']

class PostInstall(install):
        def run(self):
                HOME_DIR = str(Path.home())
                PIPTUI_DIR = HOME_DIR + '/.piptui/'
                CONFIG_PATH = PIPTUI_DIR + 'config.ini'
                THEME_FOLDER = PIPTUI_DIR + 'themes/'
                if not os.path.isdir(PIPTUI_DIR):
                        os.mkdir(PIPTUI_DIR)
                if not os.path.isdir(THEME_FOLDER):
                        os.mkdir(THEME_FOLDER)

                with open('.piptui/config.ini') as original:
                        with open(PIPTUI_DIR + 'config.ini', 'w') as new:
                                new.write(original.read())

                for file in os.listdir('.piptui/themes'):
                        with open('.piptui/themes/' + file) as original:
                                with open(THEME_FOLDER + file, 'w') as new:
                                        new.write(original.read())

setup(
        name='PipTUI',
        version=__version__.__version__,
        packages=find_packages(),
        data_files=None,
        description='A console PIP GUI!',
        license="MIT",
        author='Nitan Alexandru Marcel',
        author_email='nitan.marcel@gmail.com',
        classifiers=[
                'Environment :: Console',
                'Development Status :: 4 - Beta',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7'
        ],
        keywords='pip, npyscreen, pip-gui',
        install_requires=requirements,
        entry_points={'console_scripts': ['piptui = piptui.app:main']},
        cmdclass={'install': PostInstall}
)