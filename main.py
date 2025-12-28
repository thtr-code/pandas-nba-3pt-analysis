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

player_df['3PA_total'] = player_df['3PA'] * player_df['G'] / 82
player_df['3P_total'] = (player_df['3P'] * player_df['G']) / 82


merged_df = player_df.merge(team_df, how='left', on='Team')
merged_df = merged_df.fillna(0)

final_df = merged_df.groupby('Team').agg({
    '3P_total': 'sum',
    '3PA_total': 'sum',
})
final_df = team_df[['Team','Rk', 'W', 'L', 'NRtg']].merge(final_df, how='left', on='Team')

final_df['3P_PCT'] = final_df['3P_total'] / final_df['3PA_total']

final_df = final_df.sort_values('Rk', inplace=False, ascending=True)
final_df = final_df.set_index('Rk')
print(final_df)

'''
Playing around with diff funcs ignore 

print(player_df[player_df['3P'] == player_df['3P'].max()].to_string())
print(player_df.loc[player_df['3P'].idxmax(),'Player'])
print(final_df[['W', 'L','NRtg','3P_total', '3PA_total', '3P_PCT']])

'''


