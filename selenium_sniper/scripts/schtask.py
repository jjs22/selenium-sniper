# schtask.py
# Used for variables in schtask.cmd
import site
import sys

python_dir = site.getsitepackages()[0]
site_packages_dir = site.getsitepackages()[1]
if sys.argv[1] == "0":
    print(python_dir)
if sys.argv[1] == "1":
    print(site_packages_dir)

print(python_dir)
print(site_packages_dir)
# python_cmd = python_dir + "\python.exe" + " " + site_packages_dir + "\selenium_sniper\selenium.py"
# schtasks_cmd = "schtasks /Create /TR" + ''' "''' + python_cmd + '''"''' + " /ST 00:05 /SC DAILY" + " /TN SeleniumSniper"
# Popen(schtasks_cmd)