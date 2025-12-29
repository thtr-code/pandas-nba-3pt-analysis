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

corr_efficiency = final_df['3P_PCT'].corr(final_df['NRtg'])
corr_volume = final_df['3PA_total'].corr(final_df['NRtg'])

print("Correlation (3P% vs Net Rating):", corr_efficiency)
print("Correlation (3PA vs Net Rating):", corr_volume)




print(final_df) ## In hindsight, probably didn't need team win loss


figure, axes = plt.subplots(2,1)

## 3% vs Net Rating

axes[0].scatter(final_df['3P_PCT'], final_df['NRtg'])
axes[0].set_xlabel('3P%')
axes[0].set_ylabel('Net Rating')
x = final_df['3P_PCT']
y = final_df['NRtg']

m, b = np.polyfit(x, y, 1)
axes[0].plot(x, m * x + b, linewidth = 1, color = 'black')

##3PA vs Net Rating
axes[1].scatter(final_df['3PA_total'], final_df['NRtg'])
axes[1].set_xlabel('3P Attempted')
axes[1].set_ylabel('Net Rating')


axes[0].text(0.315 , 12 , f'r:  {corr_efficiency}', color = 'red')
axes[0].text(0.315 , 10 , 'Conclusion: Moderately Strong Correlation', color = 'red')



axes[1].text(32,12, f'r: {corr_volume}', color = 'red')
axes[1].text(32 , 10 , 'Conclusion: Weak Correlation ', color = 'red')



for team, x, y in zip(final_df['Team'], final_df['3P_PCT'], final_df['NRtg']):
    axes[0].annotate(team, (x, y), fontsize=8)
for team, x, y in zip(final_df['Team'], final_df['3PA_total'], final_df['NRtg']):
    axes[1].annotate(team, (x, y), fontsize=8)
plt.tight_layout()
plt.show()



'''
Conclusion: During the 2024 - 2025 NBA season, a team's 3-point shooting percentage matters far more than
how many 3's they are attempting (in terms of net rating). Boston appears as a high-volume outlier that succeeds
despite not leading the league in efficiency, suggesting that extreme volume CAN PARTIALLY compensate for 
non-elite efficieny, though this effect is not broadly consistent across teams
'''
