@ECHO OFF
for %%a in ('start python schtask.py 0') do @set pydir=%%a
for %%a in ('start python schtask.py 1') do @set pysitedir=%%a

@echo on
schtasks /Create /TR %pydir%\python.exe %pysitedir%\selenium_sniper\selenium.py /ST 00:05 /SC DAILY /TN SeleniumSniper