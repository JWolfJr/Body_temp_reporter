"""Following script is to automate my kids school fever check survey that is 
to be submitted every morning before she can enter school. On an already busy 3 kids
going to school morning. The survey can only be accessed once a school day."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

browser.set_window_size(700, 600)
browser.set_window_position(0, 0)

#browser.get("https://www.brookfieldlagrange.iad1.qualtrics.com")

# having trouble with the website, maybe due to link was originally sent to my wife!
browser.get("https://brookfieldlagrange.iad1.qualtrics.com/jfe/form/SV_5uoAn5rdUOcUiqx?Q_DL=GQiC2BdRdpm00g6_5uoAn5rdUOcUiqx_CGC_J0q5oiAd598GByx&Q_CHL=email")

#sleep(5)




#sleep(5)
#browser.close()