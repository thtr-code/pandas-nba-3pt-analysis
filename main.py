import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Problem Definition: Is NBA (2024-2025) team success (wins/net rating) more strongly correlated with 3-point volume 
                    or 3-point efficiency
'''

player_df = pd.read_csv('player_data.csv')
team_df = pd.read_csv('team_data.csv')


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

player_df = player_df[~player_df['Team'].isin(['2TM', '3TM'])]
player_df['Team'] = player_df['Team'].map(team_map)
merged_df = player_df.merge(team_df, how='left', on='Team')
merged_df = merged_df.fillna(0)

grouping = merged_df.groupby('Team').agg({
    'W': 'mean',
    'L': 'mean',
    'NRtg': 'first',
    '3P': 'sum',
    '3PA': 'sum',
})

'''
The following result is WRONG because we did not account for the fact that
the csv displays seperate stats for players before and after they were traded. The 76'ers 
for example have such a high 3PA because they have many trades, meaning old players
and new players are contributing to the 3PA. 
'''
print(grouping[['W', 'L', '3P', '3PA']])

'''
Playing around with diff funcs ignore 

print(player_df[player_df['3P'] == player_df['3P'].max()].to_string())
print(player_df.loc[player_df['3P'].idxmax(),'Player'])
'''


