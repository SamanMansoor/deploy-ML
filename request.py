import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'home_team_fifa_rank','away_team_fifa_rank','home_team_total_fifa_points','away_team_total_fifa_points','home_team_score','away_team_score','home_team_result'})

print(r.json())
