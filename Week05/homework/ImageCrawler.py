# -*- coding:utf-8 -*-
import html
import yaml
import json
import os
import re
import pathlib
import time
from urllib.parse import urlencode
from multiprocessing.pool import Pool
import requests
from pyquery import PyQuery as pq

# url = 'https':'//image.baidu.com/search/index?tn = baiduimage & ct = 201326592 & lm = -1 & cl = 2 & ie = gb18030 & word = dog & fr = ala & ala = 1 & alatpl = adress & pos = 0 & hs = 2 & xthttps = 111111'',

base_url = 'https://image.baidu.com/search/acjson?'

headers = {'Accept': 'text/plain, */*; q=0.01',
           'Accept-Encoding':  'gzip, deflate, br',
           'Accept-Language':  'zh-CN,zh;q=0.9',
           'Cache-Control': 'no-cache',
           'Connection':  'keep-alive',
           'Cookie':  'winWH=%5E6_1920x937; BDIMGISLOGIN=0; BDqhfp=dog%26%26NaN-1undefined%26%261938%26%263; BAIDUID=FB814E9C74F927DAD03A5CD836416F6C:FG=1; PSTM=1551260442; BIDUPSID=0F9E99CF7B4B88E1ED8CD82B56B33AF1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[PaHiFN6tims]=9xWipS8B-FspA7EnHc1QhPEUf; delPer=0; PSINO=1; BDRCVFR[rePVrIVEn7n]=9xWipS8B-FspA7EnHc1QhPEUf; H_PS_PSSID=1444_21093_28607_28584_26350_28604_28627_28606; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=ala',
           'Host':  'image.baidu.com',
           'Pragma':  'no-cache',
           'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=dog&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
           'X-Requested-With':  'XMLHttpRequest'}

# Fuck the AJAX!

# Let me show you how to fuck it!


def get_page(pn=0, word='dog', queryWord='dog', rn=30):
    params = {'tn': 'resultjson_com',
              'ipn': 'rj',
              'ct': '201326592',
              'is': '',
              'fp': 'result',
              'queryWord': queryWord,
              'cl': '2',
              'lm': '-1',
              'ie': 'utf-8',
              'oe': 'utf-8',
              'adpicid': '',
              'st': '',
              'z': '',
              'ic': '',
              'hd': '',
              'latest': '',
              'copyright': '',
              'word': word,
              's': '',
              'se': '',
              'tab': '',
              'width': '',
              'height': '',
              'face': '',
              'istype': '',
              'qc': '',
              'nc': '',
              'fr': '',
              'expermode': '',
              'force': '',
              'pn': pn,
              'rn': rn,
              'gsm': '1e'}
    url = base_url + urlencode(params)
    print(url)

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        regex = re.compile(r'\\(?![/u"])')
        fixed = regex.sub(r"\\\\", response.text)
        _json = json.loads(fixed)
        print(_json)
        return _json
        # except requests.ConnectionError as e:
        #     print(e.args)
        # except json.decoder.JSONDecodeError:


def parse(_json):
    if _json:
        items = _json.get('data')
        for item in items:
            img_url = item.get('thumbURL')
            print(img_url)
            yield img_url


def get_image(img_url):
    global num
    global kw

    r = requests.get(img_url)
    if r.status_code == 200:
        fp = 'images\\wolves\\{}{}.jpg'.format(kw, str(num))
        with open(fp, 'wb') as f:
            f.write(r.content)


if __name__ == '__main__':
    num = 1
    kw = 'wolf'

    for pn in [10*i for i in range(0, 33, 3)]:
        try:
            _json = get_page(pn=pn, queryWord=kw, word=kw)
            for img_url in (parse(_json)):
                get_image(img_url)
                num += 1
        except requests.exceptions.MissingSchema:
            continue
