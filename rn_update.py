#!/usr/b*********/python
import re
import mechanize
from mechanize import Browser

#first form
browser = mechanize.Browser()
browser.open("")
browser.select_form(nr = 1)

browser.form.set_all_readonly(False)
browser.form["USERNAME"] = "********"
browser.form["PASSWORD"] = "**********"
browser.submit()

#second form
req=browser.click_l*********k(text='Edit Profile')
browser.open(req)

#third form
browser.select_form(nr = 0)
browser.form["p*********code"]="560013"
browser.submit()
#pr*********t browser.response().read()
