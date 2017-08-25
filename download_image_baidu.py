import requests
from urllib.parse import urlencode
import json
from requests.exceptions import RequestException
from hashlib import md5
import os
import re

def get_page_index(keyword,page):
    urls = []
    for i in range(30, 30*int(page)+30, 30):
        data={
            'tn': 'resultjson_com',
            'ipn':'rj',
            'ct': 201326592,
            'is': '',
            'fp':'result',
            'queryWord': keyword,
            'cl':2,
            'lm':-1,
            'ie':'utf - 8',
            'oe':'utf - 8',
            'adpicid':'',
            'st':-1,
            'z':'',
            'ic':0,
            'word': keyword,
            's':'',
            'se':'',
            'tab':'',
            'width':'',
            'height':'',
            'face':0,
            'istype':2,
            'qc':'',
            'nc':1,
            'fr':'',
            'pn':i,
            'rn':30,
            'gsm':'1e',
            '1502988509180':''
                             }

        url = 'https://image.baidu.com/search/acjson?'+urlencode(data)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                urls.append(response.text)
            else:
                continue
        except RequestException:
            print('Not Foung Index')

    return urls

def parse_page_index(html):
    html=re.sub('\'','\"',html)
    data=json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('thumbURL')

def download_images(url):
    print('downloading images',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
             save_images(response.content)
        return None
    except RequestException:
        print('Error IMG_URL',url)
        return None

def save_images(content):
    file_path='{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()


def main():
    obj=str(input('pls input image object:'))
    page=input('pls input pages:')
    htmls = get_page_index(obj, page)
    for html in htmls:
        if html:
            urls = parse_page_index(html)
            for url in urls:
                download_images(url)


if __name__=='__main__':
    main()
