@ECHO ON
:for /F %%i in ('start python schtask.py 0') do set pydir=%%i
:for /F %%i in ('start python schtask.py 1') do set pysitedir=%%i

for /f "usebackq delims=" %%x in (`python schtask.py 0`) do set pydir=%%x
for /f "usebackq delims=" %%x in (`python schtask.py 1`) do set pysitedir=%%x

schtasks /Create /TR "%pydir%\python.exe %pysitedir%\selenium_sniper\selenium.py" /ST 00:05 /SC DAILY /TN SeleniumSniper