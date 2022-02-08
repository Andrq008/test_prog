import requests
from bs4 import BeautifulSoup
from requests.models import cookiejar_from_dict
from requests.auth import HTTPDigestAuth
import fake_useragent
from requests.sessions import session
client = requests.Session()
d = requests.Session()
#head = {'Authorization': 'token {}'.format(F784377697)}
user = fake_useragent.UserAgent().random
head = {
    'user-agent': user
    }
telmi = "F784377697"
password = '20ewXwoVoDH*'
HOMEPAGE_URL='https://my.beeline.ru/b/index.xhtml'
LOGIN_URL = 'https://my.beeline.ru/login.xhtml'
login_information = {
    'loginFormB2C:loginForm': 'loginFormB2C:loginForm',
    'loginFormB2C:loginForm:login': 'F784377697',
    'loginFormB2C:loginForm:password': '20ewXwoVoDH*',
    'loginFormB2C:loginForm:passwordPwd': '20ewXwoVoDH*'
#    'loginFormB2C:loginForm:loginButton' : ''
#    'remember': 1,
}
client.post(LOGIN_URL, data=login_information, headers=head)
# client.post(LOGIN_URL, auth=HTTPDigestAuth(telmi,password), headers=head)
#client.post('https://lka.azimuth.aero', {
#    'P101_USERNAME': 'А4_45АЗМ',
#    'P101_PASSWORD': 'Qwerty45!',
#    'button': 'button',
#    'remember': 1,
#})
r = client.get(HOMEPAGE_URL, headers=head)
d.post(LOGIN_URL, auth=HTTPDigestAuth('F784377697', '20ewXwoVoDH*'))
h = d.get(HOMEPAGE_URL)
soup = BeautifulSoup(r.text, 'lxml')
soup2 = BeautifulSoup(h.text, 'lxml')

azi = soup.find('title').text
az2 = soup2.find('title').text
print(azi)
print(az2)
print(head)
print(client.cookies)

cookies_dict = [
    {"domain": key.domain, "name": key.name, "path":key.path, "value": key.value}
    for key in client.cookies
]

session2 = requests.Session()

for cookies in cookies_dict:
    session2.cookies.set(**cookies)

resp = session2.get(HOMEPAGE_URL, headers=head)
soup3 = BeautifulSoup(resp.text, 'lxml')
az3 = soup3.find('title').text
print(az3)