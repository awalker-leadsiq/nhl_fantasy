import requests
import json
#######################################################################################################
r = requests.get("https://statsapi.web.nhl.com/api/v1/teams/16/roster")
rjson = r.json()
roster = rjson['roster']

for player in roster:
    person = player['person']
    name = person['fullName']
    #print(name + " stats:")
    playerId = person['id']
    #print(playerId)
    playerStats = requests.get("https://statsapi.web.nhl.com/api/v1/people/" + str(playerId) +  "/stats?stats=yearByYear")
    pjson = playerStats.json()
    splits = pjson['stats'][0]['splits']
    for season in splits:
        year = season['season']
        league = season['league']['name']
        if league == 'National Hockey League':
            try:
                stats = season['stat']
                games = stats['games']
                plusMinus = stats['plusMinus']
                #print("    " + year + " - " + str(games) + " games " + str(plusMinus) + " plusMinus")
            except:
                print("  " + year + " - no data")
#######################################################################################################################



##list of teams -> make team reference table
req = requests.get("https://statsapi.web.nhl.com/api/v1/teams")
teamjson = req.json()
team = teamjson['teams']

for x in range(0,32):
    team2 = json.dumps(team[x])
    team3 = json.loads(team2)
    teamId = team3['id']
    print(teamId)
    teamName = team3['name']
    print(teamName)
    teamAbr = team3['abbreviation']
    print(teamAbr)



##go through teams to get rosters
teamIdList = list(range(1,11)) + list(range(12,27)) + list(range(28,31)) + list(range(52,56))
for y in teamIdList:
    req = requests.get("https://statsapi.web.nhl.com/api/v1/teams/" + str(y) + "/roster")
    rosterjson = req.json()
    roster = rosterjson['roster']
    #rosterLen = len(roster) 
    rosterLen = 2 ##switch with above to get actual lengths
    for z in range(0,rosterLen):
        playerId = roster[z]['person']['id']
        playerName = roster[z]['person']['fullName']
        playerPosAbr = roster[z]['position']['abbreviation']
        playerPosType = roster[z]['position']['type']   
        print(playerId)
        print(playerName)
        print(playerPosAbr)


#in future devise way to get # of teams per season -> number of games per season

##list of numbers in 0003 format
gameCount = [] 
for x in range(1,10):#change to 1313
    gameCount.append(format(x, "04"))



for a in gameCount:
    gameReq = requests.get("https://statsapi.web.nhl.com/api/v1/game/202102" + str(a) + "/boxscore")
    gameJson = gameReq.json()
    teams = gameJson['teams']['away']['team']['name']
    print(teams)
#combine with below to do all games




req = requests.get("https://statsapi.web.nhl.com/api/v1/game/2021020997/boxscore")
json = req.json()
teams = json['teams']

for key, value in teams.items():
    players = value['players']
    for key, value in players.items():
        print(key)
        playerInfo = value['person']
        playerName = playerInfo['fullName'] 
        playerId = playerInfo['id']
        playerStats = value['stats']
        playerPosition = value['position']['type']
        playerAbbrevation = value['position']['abbreviation']
        print(playerName)
        print(playerPosition)
        for key, value in playerStats.items():
            if key == 'skaterStats':
                print(key)
                playerToi = value['timeOnIce']
                print("TOI: " + playerToi)
                playerAssists = value['assists']
                print("Assists: " + str(playerAssists))
                playerGoals = value['goals']
                print("Goals:" + str(playerGoals))
                playerShots = value['shots']
                print("Shots: " + str(playerShots))
                playerHits = value['hits']
                print("Hits: " + str(playerHits))    
                playerFaceoffwins = value['faceOffWins']
                print("FO Wins: " + str(playerFaceoffwins))    
                playerFaceofftaken = value['faceoffTaken']
                playerFoloss = playerFaceofftaken-playerFaceoffwins
                print("FO Losses: " + str(playerFoloss))  
                playerBlocks = value['blocked']
                print("Blocks: " + str(playerBlocks))   
                playerShg = value['shortHandedGoals']
                playerSha = value['shortHandedAssists']
                playerShp = playerSha+playerShg
                print("SHP: " + str(playerShp))   
                playerPptoi = value['powerPlayTimeOnIce']
                print("PP TOI: " + playerPptoi)
            else:
                print(key)
                playerToi = value['timeOnIce']
                print("TOI: " + playerToi)
                playerShots = value['shots']
                print("Shots: " + str(playerShots))
                playerSaves = value['saves']
                print("Saves: " + str(playerSaves))
                playerDecision = value['decision']
                print("Game Decision: " + playerDecision)


    
    





{
    'ID123': {
        "Name": 'Joe Shmo',
        "Faceoffs": [
            {
                "Game": 1,
                "Count": 4,
                "Wins": 2,
                "Rate": .5
            },
            {
                "Game": 1,
                "Count": 4,
                "Wins": 2
            }
        ]
    }
}


