import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm

'''
Problem Definition:
Is three-point efficiency an independent driver of offensive strength 
at the team level, beyond shot volume and defensive context?
'''


player_df = pd.read_csv('player_data.csv')
team_df = pd.read_csv('team_data.csv')

team_map = {
    'Atlanta Hawks': 'ATL',
    'Boston Celtics': 'BOS',
    'Brooklyn Nets': 'BRK',
    'Chicago Bulls': 'CHI',
    'Charlotte Hornets': 'CHO',
    'Cleveland Cavaliers': 'CLE',
    'Dallas Mavericks': 'DAL',
    'Denver Nuggets': 'DEN',
    'Detroit Pistons': 'DET',
    'Golden State Warriors': 'GSW',
    'Houston Rockets': 'HOU',
    'Indiana Pacers': 'IND',
    'Los Angeles Clippers': 'LAC',
    'Los Angeles Lakers': 'LAL',
    'Memphis Grizzlies': 'MEM',
    'Miami Heat': 'MIA',
    'Milwaukee Bucks': 'MIL',
    'Minnesota Timberwolves': 'MIN',
    'New Orleans Pelicans': 'NOP',
    'New York Knicks': 'NYK',
    'Oklahoma City Thunder': 'OKC',
    'Orlando Magic': 'ORL',
    'Philadelphia 76ers': 'PHI',
    'Phoenix Suns': 'PHO',
    'Portland Trail Blazers': 'POR',
    'Sacramento Kings': 'SAC',
    'San Antonio Spurs': 'SAS',
    'Toronto Raptors': 'TOR',
    'Utah Jazz': 'UTA',
    'Washington Wizards': 'WAS'
}

player_df = player_df[~player_df['Team'].isin(['2TM', '3TM'])]
team_df['Team'] = team_df['Team'].map(team_map)
player_df.fillna(0)


merged_df = team_df.merge(player_df, on='Team', how='left')
merged_df['3PA_total'] = (merged_df['G'] * merged_df['3PA']) / 82
merged_df['3P_total'] = (merged_df['G'] * merged_df['3P']) / 82


final_df = merged_df.groupby('Team').agg({
    'ORtg': 'first',
    '3PA_total': 'sum',
    '3P_total': 'sum',
    'DRtg': 'first'
})
final_df = final_df.merge(team_df[['Team', 'Rk']], on='Team', how='left')

final_df['3P_PCT'] = final_df['3P_total'] / final_df['3PA_total']

final_df = final_df.sort_values('Rk', inplace=False, ascending=True)
final_df = final_df.set_index('Rk')


## Regression and analysis starts here.
x = final_df[['3P_PCT', '3PA_total', 'DRtg']]
y = final_df['ORtg']

x_std = (x - x.mean()) / x.std()
x_std = sm.add_constant(x_std)

result = sm.OLS(y, x_std).fit()
print(result.summary())


sm.graphics.plot_partregress_grid(result)
plt.show()


'''
Conclusion: 3P% remains a strong, statistically significant predictor of offensive performance even when controlling 
for defense. This is reinforced by the values we obtain from the table, β ≈ 2.89, p < 0.001


'''