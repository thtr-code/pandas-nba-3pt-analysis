import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Problem Definition: Is NBA (2024-2025) team success (wins/net rating) more strongly correlated with 3-point volume 
                    or 3-point efficiency
'''


df = pd.read_csv('player_data.csv')
teamdf = pd.read_csv('team_data.csv')

team_map = {
    'ATL': 'Atlanta Hawks',
    'BOS': 'Boston Celtics',
    'BRK': 'Brooklyn Nets',
    'CHI': 'Chicago Bulls',
    'CHO': 'Charlotte Hornets',
    'CLE': 'Cleveland Cavaliers',
    'DAL': 'Dallas Mavericks',
    'DEN': 'Denver Nuggets',
    'DET': 'Detroit Pistons',
    'GSW': 'Golden State Warriors',
    'HOU': 'Houston Rockets',
    'IND': 'Indiana Pacers',
    'LAC': 'Los Angeles Clippers',
    'LAL': 'Los Angeles Lakers',
    'MEM': 'Memphis Grizzlies',
    'MIA': 'Miami Heat',
    'MIL': 'Milwaukee Bucks',
    'MIN': 'Minnesota Timberwolves',
    'NOP': 'New Orleans Pelicans',
    'NYK': 'New York Knicks',
    'OKC': 'Oklahoma City Thunder',
    'ORL': 'Orlando Magic',
    'PHI': 'Philadelphia 76ers',
    'PHO': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'WAS': 'Washington Wizards'
}


df = df[~df['Team'].isin(['2TM', '3TM'])]
df = df.fillna(0)
df['Team'] = df['Team'].map(team_map)

df = df.drop(['Rk' , 'Player', 'Age',
              'Pos', 'Player-additional', 'Awards',
              'G', 'GS'], axis=1)

df = df.merge(teamdf, how='left', on='Team')

print(df.to_string())


