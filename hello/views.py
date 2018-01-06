from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
# from .models import AnanLib

from bs4 import BeautifulSoup
import requests
# import os

import time
from datetime import datetime
import random
import csv
# import urllib
# import json


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


# def index(request):
#     r = requests.get('http://httpbin.org/status/418')
#     print(r.text)
#     return HttpResponse('<pre>' + r.text + '</pre>')


# def index(request):
#     times = int(os.environ.get('TIMES', 3))
#     return HttpResponse('Hello! ' * times)


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


def anan(request):
    today = datetime.now()
    now = f'{today.year}{str(today.month).zfill(2)}{str(today.day).zfill(2)}'
    params = {
        'BOOK': 'ON', 'ITEM1': 'AB', 'KEY1': '',
        'COMP1': '3', 'ITEM2': 'CD', 'KEY2': '',
        'COMP2': '1', 'ITEM3': 'EF', 'KEY3': '',
        'COMP3': '1', 'COND': '1', 'SORT': '5',
        'BUNRUI1': '  ', 'BUNRUI2': '', 'BUNRUI': '',
        'ISBN': '', 'YEARFROM': '', 'YEARTO': '',
        'LIBRARY': '   ', 'MATER': '   ', 'TRGUSER': '   ',
        'MAXVIEW': '300', 'RTNPAGE': 'http://anan-lib.jp/search.html'
    }
    search_words = 'マジックアウト'
    params['KEY1'] = search_words.encode('shift_jis')
    soup = crawling_post('http://db.anan-lib.jp/cgi-bin/CLIS/search', params)

    trs = [tr.find_all('td') for tr in soup.select('.FULL tbody tr')]
    texts = []
    for tds in trs:
        td_texts = [td.get_text().replace('　', ' ') for td in tds]
        texts.append(td_texts[:-1])

    filepath = f'hello/static/{now}_searched.csv'
    clear_csv(filepath)  # 同名のファイルがあれば初期化。なければ作成。
    save_csv(soup, filepath)

    return render(request, 'anan.html', {'texts': texts})


def crawling_post(uri, params={}, min_time=1, max_time=2):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    #     'Referer': 'http://anan-lib.jp/search.html'
    # }
    time.sleep(get_random_int(min_time, max_time))
    r = requests.post(uri, data=params)
    # print(r.text, r.encoding)
    if r.status_code == 200:
        return BeautifulSoup(r.content, 'html.parser')
    else:
        print(f'{uri}にアクセス中、エラー:{r.status_code}発生')


def get_random_int(min, max):
    """ところどころでランダムな待ち時間を入れておくと、人間らしくなって安全です"""
    return random.random() * (max - min + 1) + min


def clear_csv(filepath):
    with open(filepath, 'w'):
        pass


def save_csv(data, filepath, *, header=[]):
    """
    エクセルへの対応としてUTF-16LEかつタブ文字区切りで保存する。
    """
    with open(filepath, 'a', newline='', encoding='utf-16') as f:
        writer = csv.writer(f, lineterminator='\n', delimiter='\t')
        if header:
            writer.writerow(header)

        if isinstance(data, list):
            for row in data:
                if isinstance(row, list):
                    writer.writerow(row)
                else:
                    writer.writerow([row])
        else:
            writer.writerow([data])
