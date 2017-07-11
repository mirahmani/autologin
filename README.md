# autologin
I have cookies and browser history automatically deleted everytime I close my browser and as the result, it forces me to login manually 
into all of my account everytime I open new browser. It becomes quite repetitive, so I made a Python script to automate logins into my
most visited account: gmail, quora, and wordpress--all in one click.<br />
Features:
* Open the webpage as new tabs in Chrome browser
* Open chrome browser with existing browser configuration (bookmarks, extensions)
* Runs in OSX

### Requirement
Python 3.4.x <br />
Selenium Webdriver (latest update) <br />
ChromeDriver version: 2.30 (link : https://chromedriver.storage.googleapis.com/index.html?path=2.30/) <br />
Custom Credential info : you have to make it on your own before running the script

### How to make custom credentials (this file is not included in repo for security reason)
* Go to python site-package folder (e.g. /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages)
* Create new folder with name 'credentials'
* Inside credential folder, create 2 python files: "\_\_init\_\_.py" (just left it empty), and "credentials.py" (contains dictionary of your own login information)

### Format for credentials.py
google = {
    'uid' : 'username',
    'pwd'   : 'passwd'
}

quora_login = {
    'uid' : 'youremail@domain.com',
    'pwd'   : 'passwd'
}

wp = {
    'uid' : 'username',
    'pwd'   : 'passwd'
}

alternatively, you can put this credential info within the same folder as autologin.py, 
but you need to change every input for .send_keys() function. If that's the case, you also need to change 'from credentials import credentials'
--> import credentials.

Hope this helps.
