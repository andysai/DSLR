import requests
from time import sleep

url = 'http://pos-pre.cosmo-lady.com/posWeb/showip.jsp'  # 替换为你想要刷新的网页地址
refresh_interval = 2  # 刷新间隔，单位为秒

while True:
    response = requests.get(url)
    # 处理response，例如打印状态码或内容
    print(f"Status code: {response.status_code}")
    # 可以添加处理response内容的代码
    # 例如，打印网页内容
    # print(response.text)

    sleep(refresh_interval)  # 休眠指定的时间间隔