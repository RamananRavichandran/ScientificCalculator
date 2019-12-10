<<<<<<< HEAD
#!C:\Users\nivetha.samraj\PycharmProjects\ScientificCalculator\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==40.8.0','console_scripts','easy_install-3.7'
__requires__ = 'setuptools==40.8.0'
=======
#!C:\Users\karishma.murali\PycharmProjects\ScientificCalculator\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==39.1.0','console_scripts','easy_install-3.7'
__requires__ = 'setuptools==39.1.0'
>>>>>>> 17edfa78bf9d7e6eb71318aef6a85c11a025a5ea
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('setuptools==39.1.0', 'console_scripts', 'easy_install-3.7')()
    )
