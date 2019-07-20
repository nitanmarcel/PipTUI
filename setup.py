from setuptools import find_packages, setup
from pip_tui import __version__
import sys


requirements = [['npyscreen', 'requests', ]]
if 'win' in sys.platform:
    requirements = [requirements[0] + ['windows-curses']]

setup(
        name='PipTUI',
        version=__version__.__version__,
        packages=find_packages(),
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
        entry_points={'console_scripts': ['pip_tui = pip_tui:app.main']}
)
