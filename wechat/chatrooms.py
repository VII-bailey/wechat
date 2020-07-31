#!/usr/bin/python
# coding: utf-8

import itchat, datetime
from itchat.content import TEXT


class WeChat(object):
    def get_all_info_from_wechat(self):
        itchat.auto_login(hotReload=True)
        # 获取群
        roomslist = itchat.get_chatrooms()
        # 群名称
        itchat.dump_login_status()  # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
        myroom = itchat.search_chatrooms(name=u'IT技术人才交流群9')  # 群聊名称
        gsq = itchat.update_chatroom(myroom[0]['UserName'], detailedMember=True)

        return gsq


if __name__ == '__main__':
    obj = WeChat()
    gsq = obj.get_all_info_from_wechat()
    maleNum = 0
    femaleNum = 0
    other = 0
    othersList=[]
    femaleList=[]
    for name in gsq['MemberList']:
        if int(name['Sex']) == 1:
            maleNum += 1
        elif int(name['Sex']) == 2:
            femaleList.append(name['NickName'])
            femaleNum += 1
        else:
            othersList.append(name['NickName'])
            other += 1

    total = maleNum + femaleNum + other
    malePer = '{}%'.format(round(float(maleNum) / total, 2) * 100)
    femalePer = '{}%'.format(round(float(femaleNum) / total, 2) * 100)
    otherPer = '{}%'.format(round(float(other) / total, 2) * 100)
    print('malePer=', malePer)
    print('femalePer=', femalePer)
    print('femaleList=',femaleList)
    print('otherPer=', otherPer)
    print('othersList=', othersList)