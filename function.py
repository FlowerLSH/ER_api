import requests
import json

headers = {"x-api-key" : "여기에 api키 입력"}

# 유저 닉네임으로 id번호 받기
def GetNickNum(nick):
    url = "https://open-api.bser.io/v1/user/nickname?query=%s"%(nick)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'user' in data:
            user_id = data['user']['userNum']
            print(user_id)
        else:
            print("해당 닉네임의 유저를 찾을 수 없습니다.")
    else:
        print("API 요청 실패:", response.status_code)
        print(response.text)

#유저 id로 닉네임, mmr, 랭킹 출력
def GetUserRank(UserNum, season, Team):
    
    url = "https://open-api.bser.io/v1/rank/%d/%d/%d"%(UserNum, season, Team)

    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        data = response.json()
        
        if 'userRank' in data:
            user_rank = data['userRank']
            user = user_rank.get('nickname')
            mmr = user_rank.get('mmr')
            rank = user_rank.get('rank')
            print("User:", user)
            print("MMR:", mmr)
            print("Rank:", rank)
            
        else:
            print("해당 유저의 랭크 정보를 찾을 수 없습니다.")

    else:
        print("API 요청 실패:", response.status_code)
        print(response.text)

#유저 통계 획득(통계가 매우 기므로 주의)
def GetUserStats(userNum):
    url = "https://open-api.bser.io/v1/user/games/%d"%(userNum)
    
    response = requests.get(url, headers = headers)
    print(response.text)
