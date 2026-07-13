from api_helper import ShoonyaApiPy
from NorenRestApiPy.NorenApi import NorenApi
import logging
import time
import json
import hashlib
import requests
import pyotp
from time import sleep
import yaml
import queue
import threading
import datetime
import csv,sys, os
#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)


# ───────────────── CONFIG ─────────────────
with open('cred.yml') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)


def generate_totp(TOTP_SECRET):
    """Generate current TOTP"""
    return pyotp.TOTP(TOTP_SECRET).now()


# ───────────────── API CLASS ─────────────────
class ShoonyaApiPy(NorenApi):
    def __init__(self):
        super().__init__(
            host="https://api.shoonya.com/NorenWClientAPI",
            websocket="wss://api.shoonya.com/NorenWSAPI",
        )


# ───────────────── PROXY  ─────────────────
staticip = False

def get_my_home_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

print(f"My Home Public IP is: {get_my_home_ip()}")

if staticip:
    # Use your Windows VPS IP and the port you just opened
    vps_ip = ""
    os.environ['HTTP_PROXY'] = f"http://{vps_ip}:"
    os.environ['HTTPS_PROXY'] = f"http://{vps_ip}:"

try:
    current_ip = requests.get("https://api.ipify.org", timeout=10).text
    print(f"Trading through IP: {current_ip}") 
    # This MUST show your VPS IP, not your local IP.
except Exception as e:
    print(f"Proxy Connection Failed: {e}")

# ───────────────── API CLASS ─────────────────
class ShoonyaApiPy(NorenApi):
    def __init__(self):
        super().__init__(
            host="https://api.shoonya.com/NorenWClientAPI",
            websocket="wss://api.shoonya.com/NorenWSAPI",
        )


api = ShoonyaApiPy()
ret = api.login(userid=cred['user'], password=cred['pwd'], twoFA=generate_totp(cred['factor2']), vendor_code=cred['vc'], api_secret=cred['apikey'], imei=cred['imei'],secret_code= cred['secret'],appkey= cred['appkey'])
print(ret)

