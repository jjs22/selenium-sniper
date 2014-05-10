import site
from subprocess import Popen

python_dir = site.getsitepackages()[0]
site_packages_dir = site.getsitepackages()[1]
python_cmd = python_dir + "\python.exe" + " " + site_packages_dir + "\selenium_sniper\selenium.py"
schtasks_cmd = "schtasks /Create /TR" + ''' "''' + python_cmd + '''"''' + " /ST 00:05 /SC DAILY" + " /TN SeleniumSniper"
Popen(schtasks_cmd)