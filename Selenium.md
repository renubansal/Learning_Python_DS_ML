# Selenium Installation

# Operating System : Preferably Linux (16.04,14.04,12.04)

### Install python2 /python3 (python3 is installed Ubuntu 14.04 onwards)
To check if python is installed :  
Type Python in the terminal, if python is installed :- python interpreter will open  
Otherwise (if you are still using Ubuntu 12.04):-  
Perform the following steps on terminal :-  
 sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7  
 sudo apt-get update  
 sudo apt-get install python2.7  

### Install selenium :- sudo pip install selenium
#### For Chrome Browser-
Download Chrome driver or firefox driver using below link : https://chromedriver.storage.googleapis.com/index.html?path=2.30/.  
You might need to update Your chrome for it : sudo apt-get install chromium-browser or update manually.  
Unzip downloaded chrome webdriver /firefox driver file.  
 Type following commands on terminal :  
  cd /usr/bin  
  sudo mv chromedriver /usr/bin  
  sudo chmod A+x  chromedriver  
#### For Firefox browser-
Go to the geckodriver releases page. Find the latest version of the driver for your platform and download it. For example:
wget  https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz  
Extract the file with:  
 tar -xvzf geckodriver*  
Make it executable:  
chmod a+x geckodriver  
Add the driver to your PATH so other tools can find it:  
export PATH=$PATH:/path-to-extracted-file/geckodriver  

### Install Appium :-  (for mobile automation)
sudo apt-get update   
sudo apt install nodejs-legacy  
sudo apt-get install npm   
sudo pip install Appium-Python-Client  

## P.S. Always go for latest version
