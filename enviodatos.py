trama_1=b'REGISTER sip:192.168.8.102;transport=UDP SIP/2.0\r\nVia: SIP/2.0/UDP 192.168.8.100:51988;branch=z9hG4bK-524287-1---8195c1b7ed89720f;rport\r\nMax-Forwards: 70\r\nContact: <sip:ext101@192.168.8.100:51988;rinstance=1cf3b433f0cb9154;transport=UDP>\r\nTo: <sip:ext101@192.168.8.102;transport=UDP>\r\nFrom: <sip:ext101@192.168.8.102;transport=UDP>;tag=68335916\r\nCall-ID: -_5sdBMyyCXiYQc31wxRn..\r\nCSeq: 1 REGISTER\r\nExpires: 60\r\nAllow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE\r\nUser-Agent: Z 5.4.12 v2.10.13.2-mod\r\nAllow-Events: presence, kpml, talk\r\nContent-Length: 0\r\n\r\n'

trama_2=b'REGISTER sip:192.168.8.102;transport=UDP SIP/2.0\r\nVia: SIP/2.0/UDP 192.168.8.100:51988;branch=z9hG4bK-524287-1---b798ccd99054508a;rport\r\nMax-Forwards: 70\r\nContact: <sip:ext101@192.168.8.100:58017;rinstance=1cf3b433f0cb9154;transport=UDP>\r\nTo: <sip:ext101@192.168.8.102;transport=UDP>\r\nFrom: <sip:ext101@192.168.8.102;transport=UDP>;tag=68335916\r\nCall-ID: -_5sdBMyyCXiYQc31wxRn..\r\nCSeq: 2 REGISTER\r\nExpires: 60\r\nAllow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE\r\nUser-Agent: Z 5.4.12 v2.10.13.2-mod\r\nAuthorization: Digest username="ext101",realm="asterisk",nonce="4d1841c7",uri="sip:192.168.8.102;transport=UDP",response="960f5777a16e9d973f1792f41f11cc32",algorithm=MD5\r\nAllow-Events: presence, kpml, talk\r\nContent-Length: 0\r\n\r\n'

trama_3=b'SIP/2.0 200 OK\r\nVia: SIP/2.0/UDP 192.168.8.103:5060;branch=z9hG4bK0027142e\r\nContact: <sip:192.168.8.100:51988>\r\nTo: <sip:ext101@192.168.8.100:51988;rinstance=1cf3b433f0cb9154;transport=UDP>;tag=e426f96f\r\nFrom: "asterisk" <sip:asterisk@192.168.8.103>;tag=as08343e99\r\nCall-ID: 79cc1e2511e096fa4ed444b5112a9cdb@192.168.8.103:5060\r\nCSeq: 102 OPTIONS\r\nAccept: application/sdp, application/sdp\r\nAccept-Language: en\r\nAllow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE\r\nSupported: replaces, norefersub, extended-refer, timer, outbound, path, X-cisco-serviceuri\r\nUser-Agent: Z 5.4.12 v2.10.13.2-mod\r\nAllow-Events: presence, kpml, talk\r\nContent-Length: 0\r\n\r\n'

trama_11=b'REGISTER sip:192.168.8.103;transport=UDP SIP/2.0\r\nVia: SIP/2.0/UDP 192.168.8.100:39678;rport;branch=z9hG4bKPj5e975790-ef8e-4d69-a22f-dd0c4a6a3dbc\r\nMax-Forwards: 70\r\nFrom: <sip:ext101@192.168.8.103>;tag=b52e01d2-f346-4920-ae71-acc3fad67fbc\r\nTo: <sip:ext101@192.168.8.103>\r\nCall-ID: ed2a0536-2274-405c-9024-5669b1bc01d9\r\nCSeq: 57991 REGISTER\r\nUser-Agent: Calls+\r\nContact: <sip:ext101@192.168.8.100:39678;ob>\r\nExpires: 300\r\nAllow: PRACK, INVITE, ACK, BYE, CANCEL, UPDATE, INFO, SUBSCRIBE, NOTIFY, REFER, MESSAGE, OPTIONS\r\nContent-Length:  0\r\n\r\n'

trama_21=b'REGISTER sip:192.168.8.103;transport=UDP SIP/2.0\r\nVia: SIP/2.0/UDP 192.168.8.100:39678;rport;branch=z9hG4bKPj5c6cf18d-307d-4e2b-be8d-8ad34b9a171b\r\nMax-Forwards: 70\r\nFrom: <sip:ext101@192.168.8.103>;tag=b52e01d2-f346-4920-ae71-acc3fad67fbc\r\nTo: <sip:ext101@192.168.8.103>\r\nCall-ID: ed2a0536-2274-405c-9024-5669b1bc01d9\r\nCSeq: 57992 REGISTER\r\nUser-Agent: Calls+\r\nContact: <sip:ext101@192.168.8.100:39678;ob>\r\nExpires: 300\r\nAllow: PRACK, INVITE, ACK, BYE, CANCEL, UPDATE, INFO, SUBSCRIBE, NOTIFY, REFER, MESSAGE, OPTIONS\r\nAuthorization: Digest username="ext101", realm="asterisk", nonce="57b50c42", uri="sip:192.168.8.103;transport=UDP", response="5018fbcd8bb010df2fe138f3989fd2fc", algorithm=MD5\r\nContent-Length:  0\r\n\r\n'



import socket

class UDP_PROTOCOL:
    def __init__(self,server_udp,port_server,data_frame):
        self.resp=self._config_UDP(server_udp,port_server,data_frame)

    def _config_UDP(self,addr,port,data):
        try:
            UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            UDPClientSocket.settimeout(4)
            UDPClientSocket.sendto(data, (addr, port))
            msgFromServer = UDPClientSocket.recvfrom(40000)
            print('esto  contest',msgFromServer)
            return msgFromServer
        except:
            pass
            return None

#UDP_PROTOCOL('192.168.8.102',5060,trama_1)
UDP_PROTOCOL('192.168.8.102',5060,trama_2)
#UDP_PROTOCOL('192.168.8.102',5060,trama_3)
