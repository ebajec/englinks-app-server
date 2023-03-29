# EngLinks-App-Server
Server for testing features of the EngLinks workshop app.

**bounce_scraper.py:** Gathers data from EngLinks Bounce page to be used for event calendars.

Works under the assumption that the account being used to log in does not have a phone number connected. I have not checked if Bounce has two-factor authentication for phone-numer linked accounts.  If it does, this script will not work.  I figured it would be a safer bet to not connect a phone number and make this skip the prompt asking to do so. 

Will not work unless a file named"password-username.txt" is placed in the the repository containing valid account info for Bounce.  This file name is in .gitignore, and this script is hard-coded to open a file with this name to acquire login info. Make sure this file contains the username and THEN the password, and separate them with a single comma. Make sure there are no extra spaces.

**server.py** Pretty self-explanatory I'm sure.  

'/tutor-requests' recieves tutor requests and stores the data in folders named 
