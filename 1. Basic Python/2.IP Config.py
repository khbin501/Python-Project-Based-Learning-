import socket
import requests
import re

try:
    in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    in_addr.connect(("www.google.com", 443))
    print(f"내부 ip : {in_addr.getsockname()[0]}")

    req = requests.get("http://ipconfig.kr/")
    out_addr = requests.get("https://api.ipify.org").text
    print(f"외부 ip : {out_addr}")

except Exception as e:
    print(f"연결 실패 :{e}")

finally:
    in_addr.close()
