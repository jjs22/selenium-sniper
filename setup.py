from setuptools import setup

includefiles = ['selenium_sniper/selenium.ini', 'selenium_sniper/docs/README.txt', 'selenium_sniper/docs/NEWS.txt']
 
setup(
    name='selenium_sniper',
    version='0.3.1',
    packages=['', 'bs4', 'bs4.tests', 'bs4.builder', 'requests', 'selenium_sniper', 'chardet', 'urllib3', 'urllib3.packages', 'urllib3.contrib', 'urllib3.util', 'urllib3.packages.ssl_match_hostname'],
    url='',
    license='GNU GPL v3',
    author='Benjamin Mintz',
    author_email='benjabean1@gmail.com',
    description='WPCP Selenium program that automagically signs you up for enrichments in a timely fashion',
    long_description="Selenium Sniper",
    package_dir={"selenium_sniper": "selenium_sniper"},
    package_data={'selenium_sniper': ['*.ini'], 'selenium_sniper/docs': ['*.txt']},
    # packages=find_packages("bs4", "requests", exclude="docs")
    scripts=['selenium_sniper/scripts/schtask.py']
)
