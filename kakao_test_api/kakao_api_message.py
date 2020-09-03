import requests
import json
#
# 초기 키 땡기기
app_key = "ab8a034a2ce173f4e9ede0b812318427" # 초기 앱키 rest_key
# code = "A1JHUh_gsbaPGjf2SUFc1XFjOdBwSOG4EbVcqvOLR_uGhMjP_HgQNDzAHTZ9ssjLUnzPzgo9dVsAAAF0B8tEiw"
#
# url = "https://kauth.kakao.com/oauth/token"
#
# data = {
#     "grant_type"    : "authorization_code",
#     "client_id"     : app_key,
#     "redirect_url"  : "https://localhost.com",
#     "code"          : code
# }
#
# response = requests.post(url, data=data)
# #
# tokens = response.json()
# #
# print(tokens)
# #
# with open("kakao_token.json", 'w') as fp:
#     json.dump(tokens, fp) # 저장하는 것


# 저장된 제이슨 파일에서 읽어오기
#
with open("kakao_token.json", 'r') as fp:
    tokens = json.load(fp) # 저장하는 것
#
print(tokens)
# # access token 재발급받기
# #
url = "https://kauth.kakao.com/oauth/token"
#
#
data = {
    "grant_type"     : "refresh_token",
    "client_id"      : app_key,
    "refresh_token"  : tokens['refresh_token']
}
#
response = requests.post(url, data=data)
response.status_code
response.json()
tokens['access_token'] = response.json()['access_token']
tokens['app_key'] = app_key

with open("kakao_token.json", 'w') as fp:
    json.dump(tokens, fp) # 저장하는 것
#
# print(tokens)

with open("kakao_token.json", 'r') as fp:
    tokens = json.load(fp) # 저장하는 것

# POST /v2/api/talk/memo/default/send HTTP/1.1
# Host: kapi.kakao.com

# Authorization: Bearer {tokens['access_token']}

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {"Authorization" : "Bearer " + tokens['access_token']}

template_object={
        "object_type": "text",
        "text": "텍스트 영역입니다. 최대 200자 표시 가능합니다.",
        "link": {"web_url": "https://daum.net"},
        "button_title": "바로 확인"
    }

# data = {'template_object' : template_object}


template_object = {
    'object_type': 'text',
    'text': '운동기록확인',
    'link': {
        'web_url': 'https://daum.net',
    },
    'button_title': '바로 확인'
}

data = {'template_object': json.dumps(template_object)}


# return request('post', url, data=data, json=json, **kwargs)

response = requests.post(url, headers=headers, data=data)

response.status_code
print(response.status_code)




# 스크랩 형식
# curl -v -X POST "https://kapi.kakao.com/v2/api/talk/memo/scrap/send" \
#     -H "Authorization: Bearer {USER_ACCESS_TOKEN}" \
#     -d 'request_url=https://developers.kakao.com'

url = "https://kapi.kakao.com/v2/api/talk/memo/scrap/send"
headers = {"Authorization" : "Bearer " + tokens['access_token']}
data = {
    "request_url" : "https://daum.net"
}

response = requests.post(url, headers=headers, data=data)

response.status_code
print(response.status_code)
