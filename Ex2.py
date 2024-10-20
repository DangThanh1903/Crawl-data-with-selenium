import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('results.csv')

statistics_columns = ['Gls', 'Ast', 'xG', 'npxG', 'xAG', 'PrgC', 'PrgP', 'PrgR']

for col in statistics_columns:
    data[col] = pd.to_numeric(data[col], errors='coerce') 

results = []

for stat in statistics_columns:
    median_all = data[stat].median()
    mean_all = data[stat].mean()
    std_all = data[stat].std()

    top_3 = data.nlargest(3, stat)[['Player', stat]]
    top_3_players = ', '.join(top_3['Player'].values)

    bottom_3 = data.nsmallest(3, stat)[['Player', stat]]
    bottom_3_players = ', '.join(bottom_3['Player'].values)

    best_team = data.groupby('Squad')[stat].mean().idxmax()

    results.append({
        'Statistic': stat,
        'Median_all': median_all,
        'Mean_all': mean_all,
        'Std_all': std_all,
        'Top_3_Players': top_3_players,
        'Bottom_3_Players': bottom_3_players,
        'Best_Team': best_team
    })

results_df = pd.DataFrame(results)

results_df.to_csv('./results2/results2.csv', index=False)


numeric_stats = data[statistics_columns]
team_stats = data.groupby('Squad')[numeric_stats.columns].mean()
team_stats.to_csv('./Results/results2/team_stats.csv', index=True)


for stat in statistics_columns:
    plt.figure()
    data[stat].hist(bins=20, alpha=0.7, label=f'Distribution of {stat}')
    plt.title(f'Histogram of {stat}')
    plt.xlabel(stat)
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(f'./results2/{stat}_histogram.png') 
    plt.close()

print("Analysis and histograms saved.")
