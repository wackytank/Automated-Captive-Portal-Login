# Automated-Captive-Portal-Login
A small python script to automatically login to the Captive Portal of BIET Jhansi's Intranet.
Upgrade : A desktop file for double click execution is being added *(for linux only)*.

## Pre-Requisites:
Selenium library for Python (install using $ pip install selenium)
chromedriver for Google Chrome added to the path.(<a href="https://chromedriver.storage.googleapis.com/index.html?path=2.33/">Download Link!</a>)

## Usage:
```
$ git clone https://github.com/wackytank/Automated-Captive-Portal-Login
$ cd Automated-Captive-Portal-Login/
```

## Task:
Open login.py in text editor.
Replace "trump_user" and "trump_pw" with your username and password. 
Save and Exit.

Open auto.desktop in text editor.
Replace /path/to/login.py with the path to login.py in your PC.
Replace /path/to/icon.png with path to icon.png in your PC.
Save and Exit.

Replace /path/to/login.py with the path to login.py in your PC. Save and exit.

Now whenever you want to log-on, use auto_login.
If you want to add the script to your PATH:

 $ sudo cp login /usr/local/bin
And execute it from anywhere as:

 $ login
