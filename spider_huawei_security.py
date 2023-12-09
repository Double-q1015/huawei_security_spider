import os
import requests


def calculate_start(pageindex):
    return (pageindex - 1) * 50


def save_response_to_file(pageindex, response_text):
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.join(directory, f"{pageindex}.html")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(response_text)


url = "https://isecurity.huawei.com/sec/web/ipsVulnerability.do"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "sessionid=E4E15E588A876C75F9454A00436226EF3FAEDDF0114AB582; OnceCsrfToken=3B7650A33E1093D0835C99BE34BFA4B8D7F145543074DA9F; supportelang=zh; lang=zh; _abck=E99C9DE43BA1A0DA78A67416F8AD1CA7~0~YAAQzyE1FxcnHTWMAQAAB56pPAvsNU2I3JNRxpsKxzE+KjKrXyNhq4x4oxUxPc5QQaDYQHQon58FWUZfq+77EqgfzI+3/DlHzSopx0Fozd6sYFh48SP1UCKJ5cTY1yLBGJaGDsw6Q3Mv6xwX1Nx3mh259yQ1am+TF5awkv62MdJPYLeirNtQy4+rOVojqx4oBIctu4/RGs5FWQ1rtPNZWhQjI9bqNmW66hpXevG7YvMP88AbLHO6b92pGT83w/N6TYc0oi7EH+rpz+fGRrg1C5IB06WllMe+jojKygQ7JujPIkGlXmxq2Hvo302ul/qLYXCi0fVS/nylrq80iCRos+QFZFysiXXaYoZJQGDFP2ykOR5i4XZGgCK91YrMNrbz9JpqVUlLoULQqDo4JhQgTRx7ETCljLLb~-1~-1~-1; __hau=SUPPORTE.1701824798.484673704; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1",
    "Host": "isecurity.huawei.com",
    "Origin": "https://isecurity.huawei.com",
    "Pragma": "no-cache",
    "Referer": "https://isecurity.huawei.com/sec/web/ipsVulnerability.do",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

for pageindex in range(2, 5):
    data = {
        "start": str(calculate_start(pageindex)),
        "pageSize": "50",
        "pageIndex": str(pageindex),
        "ipsThreatId": "",
        "ipsName": "",
        "ipsCve": "",
        "ipsCnnvd": "",
        "ipsLastUpdateStart": "",
        "ipsLastUpdateEnd": "",
        "ipsSeverity": "",
        "ipsVendor": "",
        "ipsVendorLeakId": "",
        "_csrf": "94414AB4736CA944A0278CFBD453DEDE8B955D6BC6BA9FC1",
    }

    response = requests.post(url, headers=headers, data=data)
    # print(data)
    # 打印响应内容
    print(f"Page {pageindex} Response:")
    print(response.text)

    # 将响应写入文件
    save_response_to_file(pageindex, response.text)