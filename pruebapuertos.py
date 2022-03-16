#prueba puertos

import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.8.102', 5060)
message=b'REGISTER sip:192.168.8.102;transport=UDP SIP/2.0\r\nVia: SIP/2.0/UDP 192.168.8.100:51988;branch=z9hG4bK-524287-1---8195c1b7ed89720f;rport\r\nMax-Forwards: 70\r\nContact: <sip:ext101@192.168.8.100:51988;rinstance=1cf3b433f0cb9154;transport=UDP>\r\nTo: <sip:ext101@192.168.8.102;transport=UDP>\r\nFrom: <sip:ext101@192.168.8.102;transport=UDP>;tag=68335916\r\nCall-ID: -_5sdBMyyCXiYQc31wxRn..\r\nCSeq: 1 REGISTER\r\nExpires: 60\r\nAllow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE\r\nUser-Agent: Z 5.4.12 v2.10.13.2-mod\r\nAllow-Events: presence, kpml, talk\r\nContent-Length: 0\r\n\r\n'

#message1=b'REGISTER sip:192.168.8.102 SIP/2.0\r\nVia: SIP/2.0/UDP 192.168.8.100;rport;branch=z9hG4bK\r\nMax-Forwards: 70\r\nContact: <sip:ext101@192.168.8.100:51988;rinstance=1cf3b433f0cb9154;transport=UDP>\r\nTo: <sip:ext101@192.168.8.102;transport=UDP>\r\nFrom: <sip:ext101@192.168.8.102;tag=68335916\r\nCall-ID: -_5sdBMyyCXiYQc31wxRn..\r\nCSeq: 1 REGISTER\r\nExpires: 60E\r\nContent-Length: 0\r\n\r\n'

#message=b'REGISTER sip:192.168.8.103;transport=UDP SIP/2.0\r\nVia: SIP/2.0/UDP 192.168.8.100:51988;branch=z9hG4bK-524287-1---b798ccd99054508a;rport\r\nMax-Forwards: 70\r\nContact: <sip:ext101@192.168.8.100:58017;rinstance=1cf3b433f0cb9154;transport=UDP>\r\nTo: <sip:ext101@192.168.8.103;transport=UDP>\r\nFrom: <sip:ext101@192.168.8.103;transport=UDP>;tag=68335916\r\nCall-ID: -_5sdBMyyCXiYQc31wxRn..\r\nCSeq: 2 REGISTER\r\nExpires: 60\r\nAllow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE\r\nUser-Agent: Z 5.4.12 v2.10.13.2-mod\r\nAuthorization: Digest username="ext101",realm="asterisk",nonce="0be93fff",uri="sip:192.168.8.103;transport=UDP",response="960f5777a16e9d973f1792f41f11cc32",algorithm=MD5\r\nAllow-Events: presence, kpml, talk\r\nContent-Length: 0\r\n\r\n'
try:

    # Send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(409611)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
