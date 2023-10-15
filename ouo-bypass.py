import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from curl_cffi import requests


def get_recaptcha_v3():
    ANCHOR_URL = 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcr1ncUAAAAAH3cghg6cOTPGARa8adOf-y9zv2x&co=aHR0cHM6Ly9vdW8ucHJlc3M6NDQz&hl=en&v=pCoGBhjs9s8EhFOHJFe8cqis&size=invisible&cb=ahgyd1gkfkhe'
    url_base = 'https://www.google.com/recaptcha/'
    post_data = "v={}&reason=q&c={}&k={}&co={}"
    client.headers.update({'content-type': 'application/x-www-form-urlencoded'})
    matches = re.findall('([api2|enterprise]+)\/anchor\?(.*)', ANCHOR_URL)[0]
    url_base += matches[0] + '/'
    params = {pair.split('='): pair for pair in matches[1].split('&')}
    res = client.get(url_base + 'anchor', params=params)
    token = re.findall(r'"recaptcha-token" value="(.*?)"', res.text)[0]
    post_data = post_data.format(params["v"], token, params["k"], params["co"])
    res = client.post(url_base + 'reload', params=f'k={params["k"]}', data=post_data)
    answer = re.findall(r'"rresp","(.*?)"', res.text)[0]
    return answer


def ouo_bypass(url):
    id = url.split('/')[-1]
    temp_url = url.replace("ouo.press", "ouo.io")
    parsed_url = urlparse(temp_url)
    next_url = f"{parsed_url.scheme}://{parsed_url.hostname}/go/{id}"

    res = client.get(temp_url, impersonate="chrome110")

    for _ in range(2):
        if res.headers.get('Location'):
            break

        bs4 = BeautifulSoup(res.content, 'html.parser')
        data = {input_elem.get('name'): input_elem.get('value') for input_elem in bs4.form.findAll("input", {"name": re.compile(r"token$")})}
        data['x-token'] = get_recaptcha_v3()

        headers = {'content-type': 'application/x-www-form-urlencoded'}

        res = client.post(next_url, data=data, headers=headers, allow_redirects=False, impersonate="chrome110")

        next_url = f"{parsed_url.scheme}://{parsed_url.hostname}/xreallcygo/{id}"

    return {
        'original_link': url,
        'bypassed_link': res.headers.get('Location')
    }


url = "https://ouo.press/Zu7Vs5"

client = requests.Session()
client.headers.update({
    'authority': 'ouo.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'referer': 'http://www.google.com/ig/adde?moduleurl=',
    'upgrade-insecure-requests': '1',
})

out = ouo_bypass(url)
print(out)