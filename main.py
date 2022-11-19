import hashlib
import requests


def get_hash(pass_str: str) -> str:

    result = hashlib.md5(pass_str.encode())  # nosec CWE-327
    print(result.hexdigest())
    return result.hexdigest()


def get_salted(pass_str: str, salt: str) -> str:

    pass_salted = pass_str + salt
    result = hashlib.md5(pass_salted.encode()) # nosec CWE-327
    print(result.hexdigest())
    return result.hexdigest()


def get_dynamic(pass_str: str, username: str, creation_date: str) -> str:

    count = len(pass_str)
    pass_salted = pass_str + username + creation_date + str(count)
    result = hashlib.md5(pass_salted.encode()) # nosec CWE-327
    print(result.hexdigest())
    return result.hexdigest()


def call_api():

    url = 'http://ipwho.is'
    data = requests.post(url, headers={'Content-Type': 'application/json', 'Host': 'ipwho.is'})

    if data.status_code == 200:
        print(data.text)
        return data.text

    return "Cannot call {}".format(url)


if __name__ == '__main__':

    my_value = 'MyPassword'
    salt = 'RandomSaltText'
    username = 'MyUserName'
    creation_date = '01/01/1970'

    get_hash(my_value)
    get_salted(my_value, salt)
    get_dynamic(my_value, username, creation_date)
    call_api()
