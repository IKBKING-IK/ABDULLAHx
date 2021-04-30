#!/usr/bin/python
# -*- coding: utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = ['Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]']

def keluar():
    print '\b[1;91mExit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\b[%s;1m' % str(31 + j))

    x += '\b[0m'
    x = x.replace('!0', '\b[0m')
    sys.stdout.write(x+'\)


def jalan(z):
    for e in z + '\:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0012)


logo = """		
\b[1;93m██████╗░░█████╗░██████╗░░█████╗░
\b[1;93m██╔══██╗██╔══██╗██╔══██╗██╔══██╗
\b[1;93m██║░░██║███████║██║░░██║███████║
\b[1;93m██║░░██║██╔══██║██║░░██║██╔══██║
\b[1;93m██████╔╝██║░░██║██████╔╝██║░░██║
\b[1;93m╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
\b[1;94m──────────────────────────────────────────────────────
\b[1;91m➣ HACKING IS NOT A CRIME ITS A GAME AGAINST THE SYSTEM!
\b[1;92m➣ DADS OF BADS
\b[1;93m➣ AUTHOR : ABDULLAH
\b[1;95m➣ WHATSAPP : +17815150664
\b[1;96m➣ FACEBOOK : https://www.facebook.com/BHAIDADAHO
\b[1;93m➣ ABDULLAH : DAD
\b[1;94m──────────────────────────────────────────────────────""" 

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\1b[1;97m[\b[1;93m\2\7\f\b[1;97m]\b[1;93m Currently Logging in\b[1;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []

def masuk():
    os.system('clear')
    print logo
    print '\b[1;92m[01]\b[1;97m\b[1;96m\b[1;92m Login Using Facebook cookies'
    print '\b[1;92m[02]\b[1;97m\b[1;96m\b[1;92m Login Using Facebook Token'
    print '\b[1;92m[00]\b[1;97m\b[1;96m\b[1;92m Back'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\b[0;96m[--]\b[97m\b[0;92m ')
    if msuk == '':
        print '\b[1;41;97m!\b[0m] Please Fill In Correctly !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        cookie()
    elif msuk == '2' or msuk == '02':
        tokenz()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\b[1;97m[\b[1;91m!\b[1;97m] Please Fill In Correctly !'
        pilih_masuk()


def cookie():
    os.system('clear')
    print logo
    print 50 * '\b[1;94m\a'
    cookie = raw_input('\b[0;91m\b[0;97m Cookie \b[0;91m:\b[0;92m ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\+)', data.text)
        hasil = '\ Fail : maybe your cookie invalid !!' if find_token is None else '\ Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\b[1;97m[\b[1;91m!\b[1;97m] No Connection'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '\b[1;97m[\b[1;92m\a\b[1;97m]\b[1;92m Login Successfully '
    time.sleep(2)
    menu()
    return


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\b[1;97m[\b[1;39m?\b[1;97m] \b[31;1mToken : \b[31;1m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\b[1;92mLOVE YOU:) ')
        print '\b[1;91m[\b[1;39m\2\c\3\b[1;97m]\b[1;39m  Successful Login'
        os.system('xdg-open')
        bot_komen()
    except KeyError:
        print '\b[1;97m[\b[1;39m!\b[1;97m] \b[1;39mToken Wrong !'
        time.sleep(1)
        masuk()


def bo
