import requests
from requests.sessions import session
from conf import usern, password
from pprint import pprint
from requests.auth import HTTPDigestAuth
import fake_useragent

user = fake_useragent.UserAgent().random
head = {
    'user-agent': user
    }

def main():
    url = 'https://my.beeline.ru/login.xhtml'
    url2 = 'https://my.beeline.ru/b/index.xhtml'
    with requests.session() as session:
        # response = session.post(url, auth=HTTPDigestAuth(user,password), headers=head)
        session.post(url, auth=HTTPDigestAuth(usern,password), headers=head)
        r = session.get(url2, headers=head)
        pprint(r.text)
        with open('index.html', 'w') as f:
            f.write(r.text)

if __name__ == '__main__':
    main()

# loginForm:loginForm:passwordPwdB2C
# hiddenpwd
# loginFormB2C:loginForm:loginButton
# javax.faces.ViewState
# loginFormB2C:loginForm:passwordPwd