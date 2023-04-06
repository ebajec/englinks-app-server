# EngLinks-App-Server
Server for testing features of the EngLinks workshop app.


**bounce_scraper.py:** Gathers data from EngLinks Bounce page to be used for event calendars.  Uses BeautifulSoup and Selenium.

Works under the assumption that the account being used to log in does not have a phone number connected. I have not checked if Bounce has two-factor authentication for phone-numer linked accounts.  If it does, this script will not work.  I figured it would be a safer bet to not connect a phone number and make this skip the prompt asking to do so. 

Will not work unless a file named "username-password.txt" is placed in the same folder as this file. This file must contain the username and THEN the password, separated by a single comma, with NO extra spaces.

**NOTE:**  A valid web driver must be installed for Selenium to work.  See https://selenium-python.readthedocs.io/installation.html#drivers for more info.

**server.py** Flask server for testing the app.  Pretty self-explanatory I'm sure. 

'/tutor-requests' recieves tutor requests and stores the data in folders for each username.

'/login'  Supposed to verify login info.  For now it just returns true because it's only for testing.  

'/load/filename.txt' Entering the name of a valid file containing will return the contents of that file.  "Valid files" include anything in the readable folder.  Currently, this is 'events_first_year.txt', 'events_upper_year.txt', and 'events_misc.txt.'  These files are auto-generated by bounce_scraper.py, but a version of them has been left in.
