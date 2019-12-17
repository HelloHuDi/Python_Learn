# -*- coding:utf-8 -*-
# Created by hd on 2019/12/14.


import socket

exitFlag = "exit"
targetPort = 7788
targetTuple = ("", targetPort)


# udp rev

def receiveMessage():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(targetTuple)
    print("开始接收")
    while True:
        # 接收最大字节
        rev_data = udp_socket.recvfrom(1024)
        recv_msg = rev_data[0].decode('utf-8')
        send_msg = rev_data[1]
        print(recv_msg, send_msg, "\n")
        if recv_msg == exitFlag:
            print("退出")
            break
    udp_socket.close()


receiveMessage()
