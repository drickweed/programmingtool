import pynder
import itertools

import robobrowser
import re

MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
FB_AUTH = 'Put your facebook access token here'

def get_access_token(email, password):
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    s.open(FB_AUTH)
    ##submit login form##
    f = s.get_form()
    f["pass"] = password
    f["email"] = email
    s.submit_form(f)
    ##click the 'ok' button on the dialog informing you that you have already authenticated with the Tinder app##
    f = s.get_form()
    s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
    ##get access token from the html response##
    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]

    return access_token
    
    
import requests
import json

send_url = 'put your ipstack access api token here'
r = requests.get(send_url)
j = json.loads(r.text)


FB_ID = 'your facebook ID'
FB_token = get_access_token('fb email','fb password')
session = pynder.Session(FB_token ) #kwargs
