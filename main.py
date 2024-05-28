from function_stats import function_stats as fs
from function_matchs import function_matchs as fm

api_key = ""

gameID = 35008221
test = fm(api_key)

print(test.GetMatchResult(gameID))