import site
from subprocess import Popen
import sys

python_dir = site.getsitepackages()[0]
sys.stdout.write("Python installation directory is %s\n" % python_dir)
sys.stdout.flush()
site_packages_dir = site.getsitepackages()[1]
sys.stdout.write("Python installation directory is %s\n" % site_packages_dir)
sys.stdout.flush()
python_cmd = python_dir + "\python.exe " + site_packages_dir + "\selenium_sniper\selenium.py"
schtasks_cmd = "schtasks /Create /TR" + ''' "''' + python_cmd + '''"''' + " /ST 00:05 /SC DAILY" + " /TN SeleniumSniper"
Popen(schtasks_cmd)
sys.stdout.write("Scheduled task process ran.\n")
sys.stdout.flush()
