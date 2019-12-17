# -*- coding:utf-8 -*-
# Created by hd on 2019/12/14.


import socket

exitFlag = "exit"
targetPort = 7788
targetTuple = ("", targetPort)
selfTuple = ("", 7799)


# udp send

def sendMessage():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(selfTuple)
    while True:
        udp_msg = input("请输入：")
        udp_socket.sendto(udp_msg.encode("utf-8"), targetTuple)
        if udp_msg == exitFlag:
            print("退出")
            break
    udp_socket.close()


sendMessage()
