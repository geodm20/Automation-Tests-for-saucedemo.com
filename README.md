
# Automated Tests for Sauce Demo

**Description**

This script automates a series of tests in the sample [website] (https://www.saucedemo.com/ "website") from Sauce Labs through the use of Selenium and Python.

**Requirements**

- Python 3
- Selenium
- WebDriver for Google Chrome

**Installation**

- Python can be downloaded from python.org.
- Selenium can be downloaded executing "pip install selenium" in the terminal
- WebDriver for Google Chrome must be downloaded into the folder and it should match your Chrome version. Make sure you indicate the correct route in the script
- Indicate the route for you downloaded WebDriver in the script (s - Service(r'C:\Users\yourroute'))   

**How to use**
1. Execute the script SauceDemo.py
2. The script will automatically execute some tests, such as login with invalid and valid credentials, check products, add them and remove them from the cart, sort products and the buying function. Results of every test will be prited into the console.  

 
**Considerations**
- Make sure to have a stable connection to Internet while executing the tests.
- The script may need adjusts depending on future changes in the web structure.

**Contributions** 
- All contributions are welcomed. If you have any suggestion, please let me know it.
- There are some repetitions on this code, so it can be refactored.

**License**

This project is under License MIT.