import time
from selenium import webdriver
import json
import requests

headers = {
    'Cookie': 'XSRF-TOKEN=HTjCiwdScQW8CWyc4qSnSSPP; _s_tentry=weibo.com; Apache=8965520555172.314.1644034670529; SINAGLOBAL=8965520555172.314.1644034670529; ULV=1644034670648:1:1:1:8965520555172.314.1644034670529:; login_sid_t=b4dc147db401865d7abab9c3cdb2f47e; cross_origin_proto=SSL; WBStorage=09a9c7be|undefined; wb_view_log=1536*8641.25; SUB=_2A25M-Y_sDeRhGeRI4lQW9i3PyT-IHXVvjuYkrDV8PUNbmtB-LW6kkW9NUpW_xFHV1tJliUHKbsOEe5QntrnnzleP; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5vwXwAn2vQGw17P9apD8CS5JpX5KzhUgL.Fozc1KqNSoe0eoe2dJLoIp7LxKqL1KqLBo5LxK-L122LBK5LxK-L12BLBoUG; ALF=1675572028; SSOLoginState=1644036028; WBPSESS=Dt2hbAUaXfkVprjyrAZT_OyBZ2T6nFRc_MuRwcsUyP-Eg4XHMCZjp_98X05Km-N5iDAy3mFETXW5FpxYW6fPpPqLJJ74-GN5DCINbSVXPzEOFOf1kCtZsf5zB0s-BYf6btV5Ai27FKjMiQ8qhgNdMuhqgSa8C3H2xyh2w8tPws7geZSeJ_OI0KIIZaFRmWdStnClxwCQERuUZD914HbOWw==',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://weibo.com/u/2696763323'}


def getMineBlogs():
    url = "https://weibo.com/ajax/statuses/mymblog"
    items = []
    index = 0
    for x in range(1, 25):
        data = {'uid': '2696763323', 'page': x, 'feature': 0}
        responses = requests.get(url=url,
                                 headers=headers, data=data).text
        res = json.loads(responses)
        print(res['data']['list'])
        for i in res['data']['list']:
            items.append(i['id'])
            index += 1
            print("第", index, "条:", i['id'])
        print(x, "加载入文件完成...")
    with open("record.json", "w", encoding='utf8') as f:
        json.dump(items, f)


def deleteMineBlog():
    data = {id: '4645825009421412'}
    url = 'https://weibo.com/ajax/statuses/destroy'
    res = requests.post(url=url, headers=headers, data=data).text
    print(res)


bro = webdriver.Edge(executable_path='msedgedriver.exe')


def deleteAuto():
    bro.get("https://weibo.com/login.php")
    a_input = bro.find_element_by_xpath('//*[@id="loginname"]')
    a_input.send_keys('976680003@qq.com')
    b_input = bro.find_element_by_xpath(
        '//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
    b_input.send_keys('18977501507')
    c_button = bro.find_element_by_xpath(
        '//*[@id="pl_login_form"]/div/div[3]/div[6]')
    c_button.click()
    time.sleep(20)
    bro.get("https://weibo.com/u/2696763323")
    time.sleep(1)

    for ii in range(3, 251):
        i = str(ii)
        url = '//*[@id ="scroller"]/div[1]/div[' + i + \
              ']/div/article/div/header/div[2]/div[2]/span/div/i'
        # e_tag = bro.find_element_by_xpath(url)
        # e_tag.click()
        # time.sleep(1)
        # url = '//*[@id="scroller"]/div[1]/div[' + i + \
        #       ']/div/article/div[2]/header/div[2]/div[2]/div/div/div[7]'
        if (-1 > 0):
            f_div = bro.find_element_by_xpath(url)
            f_div.click()
            time.sleep(1)
            url = '//*[@id="scroller"]/div[1]/div[' + i + \
                  ']/div/article/div[2]/header/div[2]/div[2]/div/div/div[7]'
            f_div = bro.find_element_by_xpath(url)
            f_div.click()
            time.sleep(1)
        else:
            url = '//*[@id="scroller"]/div[1]/div[' + i + \
                  ']/div/article/div/header/div[2]/div/span/div/i'
            e_tag = bro.find_element_by_xpath(url)
            if e_tag.get_attribute('title') == "负反馈":
                continue
            else:
                e_tag.click()
                time.sleep(1)
                url = '//*[@id = "scroller"]/div[1]/div[' + i + \
                      ']/div/article/div[2]/header/div[2]/div/div/div/div[1]'
                e_tag = bro.find_element_by_xpath(url)
                e_tag.click()
                time.sleep(1)
                url = '//*[@id="app"]/div[3]/div[1]/div/div[3]/button[2]'
                g_button = bro.find_element_by_xpath(url)
                g_button.click()
                time.sleep(1)


if __name__ == '__main__':
    deleteAuto()
