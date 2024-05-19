import requests

headers = {"x-api-key" : "l4e16DGDho3UkY2mXoAYPaInXzgEuBkV2dYFJVrp"}

# 유저 닉네임으로 번호 받기
def GetNickNum():
    nick = input("유저 닉네임 입력 : ")
    url = "https://open-api.bser.io/v1/user/nickname?query=%s"%(nick)

    response = requests.get(url, headers = headers)

    print(response.text)

GetNickNum()
