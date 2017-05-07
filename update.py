#!/usr/b*********/python
import re
import mechanize
from mechanize import Browser

#first form
browser = mechanize.Browser()
browser.open("*********s://log*********.naukri.*********/nLog*********/Log*********.php")
browser.select_form(nr = 1)

browser.form.set_all_readonly(False)
browser.form["USERNAME"] = "vaishalibaghel7@gmail.*********"
browser.form["PASSWORD"] = "*********puterscience"
browser.submit()

#second form
req=browser.click_l*********k(text='Edit Profile')
browser.open(req)

#third form
browser.select_form(nr = 0)
browser.form["p*********code"]="562103"
browser.submit()
#pr*********t browser.response().read()
