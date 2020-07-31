# -*-coding:utf-8 -*-
import itchat
import json
import traceback
import os
from analysisData import analysisData



def checkLogin(func):
    def wrapper(*args, **kwargs):
        """
        装饰器：检查登录
        """
        try:
            print('checkLogin....  ...')
            uuid = itchat.get_QRuuid()
            if itchat.check_login(uuid) != '200':
                # 扫码登录微信，并保存登录信息
                itchat.auto_login(hotReload=True)
            return func(*args, **kwargs)
        except:
            print(traceback.format_exc())

    return wrapper

import pandas as pd
import numpy as np
import json
import csv

def writeCSV(lines):
    with open('friendInfo.csv','w+',encoding='utf-8') as f:
        write=csv.writer(f)
        write.writerow(['remarkName','nickName','sex','province','city','signature'])
        for line in lines:
            write.writerow(line)

# def writeJson(infoList):
#     """
#     JSON数据写入文本文件
#     """
#     os.remove('friendInfo.txt')
#     for info in infoList:
#         infoJsonStr = json.dumps(info, ensure_ascii=False)
#         with open('friendInfo.txt', 'a+', encoding='utf-8') as f:
#             f.writelines('{0}{1}'.format(infoJsonStr, '\n'))


# @checkLogin
# def sendMsgToOne(userName):
#     """
#     给单个人发送消息
#     """
#     userId = itchat.search_friends(name=userName)[0]['UserName']  # 根据Name查询用户id
#     itchat.send_msg('测试信息', toUserName=userId)  # 发送消息


@checkLogin
def statistic():
    """
    统计维信好友信息
    """
    try:
        friendList = itchat.get_friends(update=True)[0:]
        friendInfoList = []
        for info in friendList:
            # friendInfo = {}
            remarkName = info['RemarkName']
            # friendInfo['remarkName'] = remarkName
            nickName = info['NickName']
            # friendInfo['nickName'] = nickName
            if info['Sex'] == 1:
                sex = '男'
            elif info['Sex'] == 2:
                sex = '女'
            else:
                sex = '其他'
            # friendInfo['sex'] = sex
            province = info['Province']
            # friendInfo['province'] = province
            city = info['City']
            # friendInfo['city'] = city
            signature = info['Signature']
            # friendInfo['signature'] = signature
            friendInfo = [remarkName,nickName,sex,province,city,signature]
            friendInfoList.append(friendInfo)
            # break
        # print('friendInfoList=',friendInfoList)
        return friendInfoList
    except:
        print(traceback.format_exc())


if __name__ == '__main__':
    """
    主函数
    """
    try:
        # 扫码登录微信，并保存登录信息
        itchat.auto_login(hotReload=True)
        # sendMsgToOne()
        infoList = statistic()
        # writeJson(infoList)
        writeCSV(infoList)
        # print(infoList)
        analysisData()
    except:
        print(traceback.format_exc())
