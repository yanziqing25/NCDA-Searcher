"""
@Time: 2021/8/14 21:28
@Author: YzKing
@Website: https://www.yzking.cn
"""
import os

import requests
from bs4 import BeautifulSoup


def get_tides_list():
    """
    :return: 作品类别(不支持详细类别如A1，仅支持A, B, C等)
    """
    tides_list = []
    url = 'http://www.fd.show/list-262-1.html?tid='
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    for option in soup.find_all('option'):
        tid = option.attrs.get('value')
        if tid:
            tides_list.append(tid)
    return tides_list


def find_title(tid, title, exact=False, show_detial=True):
    """
    查找作品是否入围，返回入围作品列表
    :param tid: 作品类别
    :param title: 作品名
    :param exact: 是否精确查找。如果为True则精确查找，否则为模糊查找
    :param show_detial: 是否打印详细信息
    :return: 入围的作品list
    """
    tid = tid.upper()
    if tid not in get_tides_list():
        print('类别不存在!')
        return []

    url = 'http://www.fd.show/list-262-1.html?tid={}'.format(tid)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    pages_root = soup.find(id='pages')
    card_count = int(pages_root.find('a').get_text(strip=True)[:-1])
    page_count = int(pages_root.find_all('a')[-2].get_text(strip=True))

    title_list = []
    url = 'http://www.fd.show/list-262-{}.html?tid={}'
    if exact:
        print('作品名(精确): ' + title)
    else:
        print('作品名(模糊): ' + title)
    print('---------------开始爬取类别{}的内容(共{}页, {}条作品)---------------'.format(tid, page_count, card_count))
    found = False
    for i in range(1, page_count + 1):
        if found and exact:
            break
        if show_detial:
            print('正在爬取第{}页内容'.format(i))

        url_i = url.format(i, tid)
        res_i = requests.get(url_i)

        soup_i = BeautifulSoup(res_i.text, 'html.parser')
        for tag in soup_i.find_all('div', class_='card'):
            text = tag.find('h6', class_='card-title').get_text(strip=True)
            if exact:
                if title == text:
                    title_list.append(text)
                    found = True
                    break
            else:
                if title in text:
                    title_list.append(text)

    print('---------------执行完毕，入围作品如下---------------')
    if title_list:
        for i in title_list:
            print('类别: {}, 作品名: {}'.format(tid, i))
    else:
        print('{}未入围'.format(title))
    return title_list


def find_all(title, exact=False):
    """
    如果您不知道您的作品属于哪个类别(不太可能吧)，可以使用此方法进行模糊查找并打印结果
    :param title: 作品名
    :param exact: 是否精确查找(同上)
    :return: None
    """
    for tid in get_tides_list():
        find_title(tid, title, exact, show_detial=False)


if __name__ == '__main__':
    # The example:
    tid = input('类别: ').upper()
    title = input('作品名(关键字即可无需输入全名): ')
    find_title(tid, title)
    os.system('pause')
