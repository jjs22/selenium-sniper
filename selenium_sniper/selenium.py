#!/usr/bin/env python3
# Selenium Sniper
# WPCP Selenium program that automagically signs you up for enrichments in a timely fashion
# Version 0.3.1
# See NEWS file for what's changed in this version
# Written by Benjamin Mintz
# Send your spam (and any questions) to: benjabean1@gmail.com
# Haha I have Gmail, I won't get your spam


from bs4 import BeautifulSoup
import requests
import configparser
import datetime
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP
import os # For getting the current working directory

# Get the current working directory

# Read the config file using absolute paths
config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'selenium.ini'))

# TODO: Add ability to sign up by enrichment name, as well as by ID
# TODO: Ability to choose alternative enrichments
# TODO: Specific "Off day"/seminar day detection
# TODO: Make an installer for Windoze noobs (alternatively, make a zip ball with all the imports)


# Send the email
def email(date):
    msg = MIMEText("Hello!\n"
                   "Just wanted to let you know that you could not be signed up for %s.\n"
                   "Please sign up for that date manually, or if that was a seminar day, please "
                   "ignore this message.\n\n"
                   "Thanks,\n"
                   "Selenium Sniper" % date)
    msg['Subject'] = 'Selenium—could not be signed up for %s' % date
    msg['To'] = config['email']['name']
    msg['From'] = config['email']['name']
    s = SMTP(host=config['email']['server'], port=config['email']['port'])
    s.login(user=config['email']['username'], password=config['email']['password'])
    s.send_message(msg)
    s.quit()


session = requests.Session()


# Get the login credentials
def password_auth():
    auth_creds = {'username': config['login']['username'],
                  'password': config['login']['password']}
    return auth_creds

# Log in
login_count = 0
while login_count < 3:
    auth_creds = password_auth()
    print("Logging in")
    start_page = session.post("http://selenium.wpcp.org/m/index.php", data=auth_creds, allow_redirects=True)
    soup_start_page = BeautifulSoup(start_page.text)
    if len(start_page.history) != 0 and start_page.history[0].status_code == 302:
        print("Login successful!")
        break
    else:
        print("Login unsuccessful! Please check your username and password and try again.")
        login_count += 1
        if login_count == 3:
            print("Three unsuccessful login attempts! Exiting.")
            exit(1)


# Signup function
def signup(enrichment_id, enddate_formatted):
    links = soup_start_page.find_all('a')
    enrichment_link = links[10]
    # Check if that day's enrichment is not available
    # if enrichment_link.get("class") == "ui-disabled":
    if enrichment_link.get("class") is not None:
        if "ui-disabled" in enrichment_link['class']:
            print("No enrichments for ", enddate_formatted, ", bye now!", sep='')
            if day_of_week != 0 and day_of_week != 6:
                email(enddate_formatted)
                exit(1)
    # Check if that day's enrichment is available, and if so, check if locked in
    elif enddate_formatted in enrichment_link['href']:
        date_payload = {'date': enddate_formatted}
        enrichment_payload = {'enrichment': enrichment_id}
        selector_page = session.get("http://selenium.wpcp.org/m/add_enrichment.php", params=date_payload)
        soup_selector_page = BeautifulSoup(selector_page.text)
        for span in soup_selector_page.find_all("span"):
            if span.get("span") is not None:
                if "Locked in" in span.string:
                    print("Locked in! Exiting.")
                    email(enddate_formatted)
                    exit(1)
        session.post('http://selenium.wpcp.org/m/add_enrichment.php', params=date_payload,
                     data=enrichment_payload)
        print("Signed up!")
        exit(0)

# Enrichment choices
enrichments = [config['enrichments']['0'],
               config['enrichments']['1'],
               config['enrichments']['2'],
               config['enrichments']['3'],
               config['enrichments']['4'],
               config['enrichments']['5'],
               config['enrichments']['6'], ]
# Parameters to be passed to signup()
enddate = datetime.date.today()
enddate = enddate + datetime.timedelta(days=9)
enddate_formatted = enddate.strftime("%Y-%m-%d")
day_of_week = int(enddate.strftime('%w'))
# Sign up
signup(enrichments[day_of_week], enddate_formatted)
