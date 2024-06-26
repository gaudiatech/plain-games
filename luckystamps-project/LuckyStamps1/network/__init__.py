# PY CONNECTOR, automatically gen. Do not modify by hand!
# filename:autogened_localctx_connector.py
# Generation date: 2024-03-22 09:24:01
import requests
import json


api_url = 'https://beta-services.kata.games'


# ----dummy----, thats not network
def get_jwt():
    #return None
    return '9467e3e3a7b1c2837744d79a47147318ce99f4771ce594ce'
    # return 'e13059b6ac587ad5e98b451f59546229356fcaac382ffe57'
    # return '3f289658cf5fc1bcf7bc96a4b534ca175e35de59f501922f' #1
    # '0e96cfd68afd2208fe192a0204bff4be8b33be2cba0e6f46'  # user 8


def get_username():
    # return None
    return 'Mickeys38'
    # 'rogergo'


def get_user_id():
    # return None
    return 1
    # 8


class GetResult:
    def __init__(self, rawtxt):
        self.text = rawtxt

    def to_json(self):
        return json.loads(self.text)


def _ensure_type_hexstr(data):
    # Ensure that the provided data is a string containing only hexadecimal characters.
    if isinstance(data, str) and all(c in '0123456789abcdefABCDEF' for c in data):
        return True
    return False


def _get_request(url, given_data=None):
    try:
        response = requests.get(f"{api_url}{url}", params=given_data)
        print('sending GET, url:', f"{api_url}{url}")
        print('sending GET, params:', given_data)
        response.raise_for_status()
        print('raw result:', response.text)
        return GetResult(response.text)
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


# added alias
def get(url, data=None):
    return _get_request(url, data)


def _post_request(url, given_data=None):
    try:
        print('sending POST, url:', f"{api_url}{url}")
        print('sending POST, params:', given_data)
        response = requests.post(f"{api_url}{url}", json=given_data)
        response.raise_for_status()
        print('raw result:', response.text)
        return GetResult(response.text)
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def get_version():
    # GET request to /version
    try:
        resobj = _get_request('/version')
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def get_user_infos(user_id: int):
    # GET request to /user/infos
    try:
        resobj = _get_request('/user/infos', {'user_id': user_id})
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def can_pay_challenge(jwt: str, game_id: int):
    # GET request to /challenge/canPay
    if not _ensure_type_hexstr(jwt):
        raise Exception("hexstr type not recognized! Value: "+str(jwt))
    try:
        resobj = _get_request('/challenge/canPay', {'jwt': jwt, 'game_id': game_id})
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def get_rank(user_id: int, game_id: int):
    # GET request to /challenge/user/rank
    try:
        resobj = _get_request('/challenge/user/rank', {'user_id': user_id, 'game_id': game_id})
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def can_pay_game_fee(jwt: str, game_price: int):
    # GET request to /games/canPayGameFee
    if not _ensure_type_hexstr(jwt):
        raise Exception("hexstr type not recognized! Value: "+str(jwt))
    try:
        resobj = _get_request('/games/canPayGameFee', {'jwt': jwt, 'game_price': game_price})
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def pay_challenge(jwt: str, game_id: int):
    # GET request to /challenge/pay
    if not _ensure_type_hexstr(jwt):
        raise Exception("hexstr type not recognized! Value: "+str(jwt))
    try:
        resobj = _get_request('/challenge/pay', {'jwt': jwt, 'game_id': game_id})
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def register_score(score: int, token: str):
    # GET request to /challenge/score
    if not _ensure_type_hexstr(token):
        raise Exception("hexstr type not recognized! Value: "+str(token))
    try:
        resobj = _get_request('/challenge/score', {'score': score, 'token': token})
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def pay_game_fee(jwt: str, game_id: int, game_price: int):
    # GET request to /games/payGameFee
    if not _ensure_type_hexstr(jwt):
        raise Exception("hexstr type not recognized! Value: "+str(jwt))
    try:
        resobj = _get_request('/games/payGameFee', {'jwt': jwt, 'game_id': game_id, 'game_price': game_price})
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def auth(username: str, password: str):
    # GET request to /user/auth
    try:
        resobj = _get_request('/user/auth', {'username': username, 'password': password})
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def get_challenge_entry_price(game_id: int):
    # GET request to /challenge/entryPrice
    try:
        resobj = _get_request('/challenge/entryPrice', {'game_id': game_id})
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def get_challenge_seed(game_id: int):
    # GET request to /challenge/seed
    try:
        resobj = _get_request('/challenge/seed', {'game_id': game_id})
        return resobj.to_json()
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None
