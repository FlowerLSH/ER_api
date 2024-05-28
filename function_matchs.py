import requests
import json
from function_base import function_Base

#여기는 플레이어의 대전 기록이나 관련 요소에 대한 함수 작성
class function_matchs(function_Base):
    def __init__(self, api_key):
        super().__init__(api_key)

    def CurrentSeason(): # 현재 시즌의 고유번호를 얻는 함수
        
        return None
    
    def GetMatchResult(self, gameID): #gameID 입력해서 해당 게임의 모든 플레이어의 데이터 획득
        url = "https://open-api.bser.io/v1/games/%d"%(gameID)
        headers = {'x-api-key': self.api_key}
        response = requests.get(url, headers=headers)
        data = self.CheckStatus(response)
        print(json.dumps(data, ensure_ascii=False, indent=3))
        
        return None