#! /usr/bin/python
import requests
import os
import sys

test = requests.get('https://www.cloudflare.com/cdn-cgi/trace/')

warp = test.text.split('''text
''')[1].split('''
gate''')[0]

if warp == 'warp=on':
    print('All good!')

if warp == 'warp=off':
    print('Warp off.\nEnableing ...')
    os.system('warp-cli connect')
    os.system('warp-cli enable-always-on')
    os.system('warp-cli enable-wifi')
    os.system('warp-cli enable-ethernet')
print('Exiting.')
sys.exit()

