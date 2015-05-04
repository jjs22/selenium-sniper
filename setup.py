from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

includefiles = ['selenium_sniper/selenium.ini', 'selenium_sniper/docs/README.txt', 'selenium_sniper/docs/NEWS.txt']
 
setup(
    name='selenium-sniper',
    version='0.3.1',
   #packages=['', 'bs4', 'bs4.tests', 'bs4.builder', 'requests', 'selenium_sniper', 'chardet', 'urllib3', 'urllib3.packages', 'urllib3.contrib', 'urllib3.util', 'urllib3.packages.ssl_match_hostname'],
    url='https://bmintz.github.io/selenium-sniper',
    license='GNU GPL v2',
    author='Benjamin Mintz',
    description='WPCP Selenium program that automagically signs you up for enrichments in a timely fashion',
    long_description=read('README.md'),
    py_modules=['selenium-sniper'],
    include_package_data=True,
    package_dir={"selenium_sniper": "selenium_sniper"},
    package_data={'selenium_sniper': ['*.ini'], 'selenium_sniper/docs': ['*.txt']},
  # packages=find_packages("bs4", "requests", exclude="docs")
    scripts=['selenium_sniper/scripts/schtask.py']
)
