#!/usr/bin/env python3

# -- coding: utf-8 --
import socketserver


class HttpsResponse:
    def __init__(self, http_request_message):
        self.http_request_message = http_request_message

    def parse(self):
        """
        解析HTTP Request报文
        :return: 字典
        """
        flag = "\r\n"
        req_head = str(self.http_request_message).split("\r\n\r\n")[0]

        # method
        req_first_line = req_head.split(flag)[0]


        return True

    def message(self):
        """
        根据Request报文，打印用户上传的参数
        :return:
        """
        info_dict = self.parse()

        body = "<html>\r\n" \
               "<head>\r\n" \
               "<title>极客营</title>\r\n" \
               "</head>\r\n" \
               "<body>\r\n" \
               "abc\r\n" \
               "</body>\r\n" \
               "</html>\r\n"

        response_message = "GET HTTP/1.1\r\n" \
                           "content-type: text/html; charset=UTF-8\r\n" \
                           "cache - control: no - cache, must - revalidate\r\n"\
                           "content-language: zh-CN\r\n"\
                           "content-length:" + str(len(body)) + "\r\n" \
                           "\r\n" + body

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
        print(self.data)

        data = HttpsResponse(self.data)

        self.request.sendall(bytes(data.message(), 'utf-8'))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9001

    socketserver.TCPServer.allow_reuse_address = True

    # 创建服务器，绑定到端口9001上的localhost
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
