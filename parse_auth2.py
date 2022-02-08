import requests
from bs4 import BeautifulSoup
import fake_useragent

session=requests.Session()
user = fake_useragent.UserAgent().random
head = {
    'user-agent': user
    }
HOMEPAGE_URL='https://cp.beget.com/vps/vs-4'
LOGIN_URL = 'https://cp.beget.com/login'
info = {

}
session.post(LOGIN_URL, data=info, headers=head)
r = session.get(HOMEPAGE_URL, headers=head)
soup = BeautifulSoup(r.text, 'lxml')
print(session.post(LOGIN_URL, data=info, headers=head))
#azi = soup.find('title').text
#print(azi)