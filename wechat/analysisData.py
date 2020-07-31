# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from pyecharts import Geo,Map
from wordcloud import WordCloud
import jieba
from PIL import Image


# 将个性签名获取出来写入文件
def writeSignature():
    dataFrame = pd.read_csv('friendInfo.csv')  # 读取csv文件获取sex数据
    dataFrame.fillna('', inplace=True)  # 用''替换为NAN的数据 inplace=True直接修改原数据
    with open('signature.txt', 'a+', encoding='utf-8') as f:
        for signature in dataFrame['signature']:
            if '<' not in signature and '>' not in signature:
                if signature:
                    f.write(str(signature).replace('\n', '').replace(' ', '') + '\n')


# 画出个性签名词云
def wordCloid():
    file = open('signature.txt', encoding='utf-8').read()
    # jieba分词。。。好奇怪的名字
    default_mode = jieba.cut(file)
    text = " ".join(default_mode)
    # 将电脑自带的字体文件放进去，解决中文乱码
    font = "simfang.ttf"
    # 需要做背景的图片
    background_image = np.array(Image.open('1111.jpg'))
    # 创建词云
    cloud = WordCloud(background_color='white', max_font_size=40, max_words=20000, mask=background_image,
                      font_path=font)

    wCloud = cloud.generate(text)
    # 生成词云文件
    wCloud.to_file('signature.jpg')

    # # 页面展示
    # import matplotlib.pyplot as plt
    # plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    # plt.imshow(wCloud, interpolation='bilinear')
    # plt.axis('off')
    # plt.show()


def genderAnalysis():
    man = 0
    woman = 0
    other = 0
    labels = ['男', '女', '其他']
    dataFrame = pd.read_csv('friendInfo.csv')  # 读取csv文件获取sex数据
    for sex in dataFrame['sex']:
        if sex == '男':
            man = man + 1
        elif sex == '女':
            woman = woman + 1
        else:
            other = other + 1
    values = [man, woman, other]  # 获取各个部分的值
    colors = ['#00CDCD', '#00FFFF', '#528B8B']  # 饼图颜色
    explode = [0.05, 0.005, 0.005]  # 离圆心的距离
    # fontdict={'size':30}
    # plt.title('微信好友性别组成',fontdict=fontdict)
    plt.title('微信好友性别组成')  # 标题
    # 画图
    # values :画图数据 lables :标签 startangle：图从多少度开始(90度比较好看)  autopct：展示各部分占比
    plt.pie(values, labels=labels, shadow=True, colors=colors, startangle=90, explode=explode, autopct='%1.1f%%')
    # 右上角说明
    plt.legend()
    # 展示
    plt.show()


def regionalAnalysis():
    # 中国所有省
    provinceDict = {'北京': 0, '上海': 0, '天津': 0, '重庆': 0,
                    '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
                    '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
                    '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
                    '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
                    '四川': 0, '贵州': 0, '云南': 0,
                    '内蒙古': 0, '新疆': 0, '宁夏': 0, '广西': 0, '西藏': 0,
                    '香港': 0, '澳门': 0, '其他': 0}
    dataFrame = pd.read_csv('friendInfo.csv')  # 读取csv文件获取sex数据
    dataFrame.fillna('其他', inplace=True)  # 用'其他'替换为NAN的数据 inplace=True直接修改原数据
    for province in dataFrame['province']:
        if province not in list(provinceDict.keys()):
            # provinceDict[province] = 1
            provinceDict['其他'] = provinceDict['其他'] + 1
        else:
            provinceCnt = provinceDict[province] + 1
            provinceDict[province] = provinceCnt
    return provinceDict


# def map(provinceDict):
#     from pyecharts import Map
#     data = [(province, provinceDict[province]) for province in list(provinceDict.keys()) if province != '其他']
#     # province_list = df['Province'].fillna('').tolist()
#     # count_province = pd.value_counts(province_list)
#     # attr = count_province.index.tolist()
#     # value1 = count_province.tolist()
#     map = Map("各省微信好友分布", title_color="#2E2E2E", title_text_size=24, title_top=20, title_pos="center", width=1200,
#               height=600, background_color="#404a59")
#     attr, value = Map.cast(data)
#     print('attr=', attr)
#     print('value=', value)
#     map.add("", attr, value, maptype='china', is_visualmap=True, visualmap_text_color='#000', is_label_show=True,
#             visual_range=[0, 200], visual_text_color="#fff", symbol_size=10)
#     # map.show_config()
#     map.render('map.html')
#     print("map已生成")


# def map(provinceDict):
#     # print(provinceDict)
#     data = [(province, provinceDict[province]) for province in list(provinceDict.keys()) if province!='其他']
#     print(data)
#     geo = Geo("微信好友地区分布",title_color="#2E2E2E", title_text_size=24, title_top=20, title_pos="center", width=1200,
#               height=600, background_color="#404a59")
#     attr, value = geo.cast(data)
#     geo.add("", attr, value, visual_range=[0, 200],maptype='中国', visual_text_color="#fff", symbol_size=10, is_visualmap=True)
#     geo.render(path=u'map.html')

# def map(provinceDict):
#     # 创建一个地图对象
#     map = Map("地域分布")
#     # 添加数据(是否使用视觉映射组件)
#     map.add("地域分布", provinceDict.keys(), provinceDict.values(), is_visualmap=True)
#     # 生成html文件
#     map.render("地域分布.html")
#
#     # webbrowser.open("地域分布.html")


def analysisData():
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
    plt.rcParams['font.size'] = 20  # 设置字体大小
    plt.figure(figsize=(10, 10))  # 设置画布大小
    writeSignature()  # 获取好友微信个性签名
    # 好友性别分析
    genderAnalysis()
    # 地区分析
    provinceDict = regionalAnalysis()
    # print(provinceDict)
    # map(provinceDict)
    # 画词云
    wordCloid()
