#!/usr/bin/env python2.7
import json, time, random, requests, itertools

session=requests.session()
username=raw_input('Username: ')
password=raw_input('Password: ')
clientToken=raw_input('Client Token: ')
clientAuthToken=raw_input('Client Auth Token: ')

url='https://app.snapchat.com/loq/login'
headers={
    'host':                          'app.snapchat.com',                                                                                                                    
    'Accept-Locale':                 'en_US',
    'Accept':                        '*/*',                                                                                                                                
    'Proxy-Connection':              'keep-alive',                                                                                                                          
    'X-Snapchat-Client-Token':       clientToken,
    'Accept-Language':               'en-US;q=1',                                                                                                                           
    'Accept-Encoding':               'gzip',                                                                                                                                
    'Content-Type':                  'application/x-www-form-urlencoded; charset=utf-8',                                                                                    
    'User-Agent':                    'Snapchat/9.40.1.0 (iPhone6,1; iOS 9.3.3; gzip)',                                                                                      
    'X-Snapchat-Client-Auth-Token':  clientAuthToken,
    'Connection':                    'keep-alive',
    'X-Snapchat-UUID':               '6DD67BA9-7BC3-4E1C-80C1-7FCEC191DE6B',
}

payload={
    'dsig':                   '7F25A21BF3E91985432B',
    'dtoken1i':               '00001:AlNT9i5xT3aCNd1KZw9Fq2z8anp256+YfCwpi0Dk99HXSRZygB',
    'from_deeplink':          'false',
    'height':                 '1136',
    'password':               password,
    'pre_auth_token':         '',
    'reactivation_confirmed': 'false',
    'remember_device':        'true',
    'req_token':              '930f095b813134886e679ae6fbaa48b419f9aa83d9b4914d9c5102b',
    'screen_height_in':       '3.5',
    'screen_height_px':       '568',
    'screen_width_in':        '1.9',
    'screen_width_px':        '320',
    'timestamp':              str(int(time.time()*1000)),
    'username':               username,
    'width':                  '640',
}
r=session.post(url,data=json.dumps(payload),headers=headers)
print r.status_code
print r.json()
raw_input('')
pre_auth_token=r.json()['pre_auth_token']

sel=[0,1,2,3,4,5,6,7,8,9]
choice=random.choice([p for p in itertools.product(sel, repeat=6)])
verifyCode=str(choice[0])+str(choice[1])+str(choice[2])+str(choice[3])+str(choice[4])+str(choice[5])


#adjust headers['X-Snapchat-Client-Auth-Token'] and headers[X-Snapchat-Client-Token] and headers['X-Snapchat-UUID']
payload={
    'dsig':                   '16A1E5B3C70BEB568034',
    'dtoken1i':               '00001:AlNT9i5xT3aCNd1KZw9Fq2z8ws256+YfCwpi0Dk99HXSRZygB',
    'from_deeplink':          'false',
    'height':                 '1136',
    'password':               verifyCode,
    'pre_auth_token':         pre_auth_token,
    'reactivation_confirmed': 'false',
    'remember_device':        'true',
    'req_token':              '9308bf5166d1ea486eb9bce6f2a80e241988ea8de9b48714d1c510b',
    'screen_height_in':       '3.5',
    'screen_height_px':       '568',
    'screen_width_in':        '1.9',
    'screen_width_px':        '320',
    'timestamp':              str(int(time.time()*1000)),
    'two_fa_mechanism_used':  'otp',
    'username':               username,
    'width':                  '640'
}

r=session.post(url,data=json.dumps(payload),headers=headers)
print r.status_code
print r.json()

