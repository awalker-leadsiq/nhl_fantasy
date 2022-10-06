from db_cnx import db_cnx
import requests
import json

db_cnx = db_cnx()

#print(db_cnx.execute('select * from team'))


##insert and update
req = requests.get("https://statsapi.web.nhl.com/api/v1/teams")
teamjson = req.json()
team = teamjson['teams']

for x in range(0,32):
    team2 = json.dumps(team[x])
    team3 = json.loads(team2)
    teamId = team3['id']
    teamName = team3['name']
    teamAbr = team3['abbreviation']
    print(teamName)
    team_insert = open('sql/team_insert.sql', 'r').read()
    value = (teamName, str(teamId), teamAbr)
    db_cnx.insert_one(team_insert, value)


#exp_variants = db_cnx.execute(open('sql/experiment_variants.sql').read().replace("#exp-id#", str(exp_id)))

#experiment_summary = open('sql/active_variants.sql', 'r').read()