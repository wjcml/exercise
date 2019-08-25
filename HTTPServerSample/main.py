#!/usr/bin/env python3

# -- coding: utf-8 --
import socketserver

import psutil


class HttpsResponse:
    def __init__(self, http_request_message):
        self.http_request_message = http_request_message

    def cpu_info(self):
        """
        获取CPU使用率
        :return: cpu_percent
        """
        cpu_percent = psutil.cpu_percent(interval=1)

        return cpu_percent

    @property
    def message_parse(self):
        """
        返回CPU使用率
        :return:res
        """
        cpu_percent = self.cpu_info()
        print(cpu_percent)
        cpu_info = "CPU使用率：{}%".format(cpu_percent)

        body = "<html>\r\n" \
               "<head>\r\n" \
               "<title>极客营</title>\r\n" \
               "</head>\r\n" \
               "<body>\r\n" \
               "{}\r\n" \
               "</body>\r\n" \
               "</html>\r\n"

        # 使用率以6%为界限
        if 6 >= cpu_percent:
            res_body = body.format(cpu_info)
            response_message = "HTTP/1.1 200 OK\r\n" \
                               "content-type: text/html; charset=UTF-8\r\n" \
                               "cache - control: no - cache, must - revalidate\r\n"\
                               "content-language: zh-CN\r\n"\
                               "content-length:{0}\r\n" \
                               "\r\n" \
                               "{1}".format(str(len(res_body)), res_body)
        else:
            res_body = body.format("<h1>503</h1>")
            response_message = "HTTP/1.1 503 Service Unavailable\r\n" \
                               "content-type: text/html; charset=UTF-8\r\n" \
                               "content-length:{0}\r\n" \
                               "content-language: zh-CN\r\n" \
                               "\r\n" \
                               "{1}".format(str(len(res_body)), res_body)

        return response_message


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
     我们服务器的请求处理程序类。

     每次连接到服务器时都会实例化一次，并且必须
     覆盖handle（）方法以实现与之通信
     客户。
    :return:dict
    """

    def handle(self):
        self.data = self.request.recv(1024).strip()
        # print(self.data)

        data = HttpsResponse(self.data)

        self.request.sendall(bytes(data.message_parse, 'utf-8'))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9001

    socketserver.TCPServer.allow_reuse_address = True

    # 创建服务器，绑定到端口9001上的localhost
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
