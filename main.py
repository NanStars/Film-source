import requests
from lxml import etree

www = ['https://www.hls5.world']
urll = []
MOVE_LIST = []


def source_code():
    url = 'https://www.hls5.world/cn/home/web/'
    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}
    respoes = requests.get(url=url, headers=headers)
    return respoes.text


def category(html):
    a = 9
    for i in range(a):
        sequenc = 2 + i
        sequenc1 = 0 + i
        # 类目标签查询
        category_location = '//nav/div/ul/li[' + str(sequenc) + ']/a/text()'
        # 类目url查询
        category_url = '//nav/div/ul/li[' + str(sequenc) + ']/a/@href'
        html1 = etree.HTML(html)
        # 类目名称
        html_category = html1.xpath(category_location)
        # 标注类目序号
        print(str(sequenc1) + ''.join(html_category))
        # 类目名称url
        html_category_url = html1.xpath(category_url)
        # list元素拼接成新的元素
        url = ''.join(www + html_category_url)
        # url添加到list来选择
        urll.append(url)

        # print(url)


def Directory_selection():
    index = int(input('请输入你要看的类目：1~9  '))
    directory = urll[index]
    return directory


def Movie_List(url):
    a = 71
    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}
    respoes = requests.get(url=url, headers=headers)
    html = respoes.text
    for i in range(a):
        se = 1 + i
        se1 = 0 + i
        # 电影名字查询条件
        Movie_List_name = '//*[@id="lycms_list_videos_videos_watched_right_now_items"]/div[' + str(
            se) + ']/a/strong/text()'
        # url查询条件
        Movie_List_URL = '//*[@id="lycms_list_videos_videos_watched_right_now_items"]/div[' + str(
            se) + ']/a/@href'

        html1 = etree.HTML(html)
        # 电影名字
        list_name = html1.xpath(Movie_List_name)
        # 电影url
        list_url = html1.xpath(Movie_List_URL)
        # 电影名字序号
        print(str(se1) + ':' + ''.join(list_name))
        # 电影url拼接
        url = ''.join(www + list_url)
        # url传入list
        MOVE_LIST.append(url)


if __name__ == '__main__':
    category(source_code())
    Movie_List(Directory_selection())
    index = int(input('请输入你要看的电影：  '))
    directory = MOVE_LIST[index]
    print(directory)