#!/usr/bin/python3

import urllib.request

target_url = 'https://www.douban.com'

def open_url():
    try:
        myheader = {'User_Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

        response = urllib.request.Request(target_url, headers = myheader)
        html = urllib.request.urlopen(response)
        result = html.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print('error reason is ' + str(e.reason))
    except urllib.error.HTTPError as e:
        if hasattr(e, 'code'):
            print('error code is ' + str(e.code))
    else:
        print('open url : {} success!'.format(target_url))

def main():
    open_url()

if __name__ == '__main__':
    main()
