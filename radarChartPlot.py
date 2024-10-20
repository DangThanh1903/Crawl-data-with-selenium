import matplotlib.pyplot as plt
import numpy as np
import argparse
import pandas as pd

def radar_chart(player1, player2, attributes):

    data = pd.read_csv('results.csv')

    p1_data = data[data['Player'].str.lower() == player1.lower()][attributes].values.flatten()
    p2_data = data[data['Player'].str.lower() == player2.lower()][attributes].values.flatten()

    print(f"Player 1 Data: {p1_data}")
    print(f"Player 2 Data: {p2_data}")

    if len(p1_data) == 0 or len(p2_data) == 0:
        print("One or both players not found.")
        return

    num_vars = len(attributes)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Complete the loop

    p1_data = np.concatenate((p1_data, [p1_data[0]]))  # Close the loop
    p2_data = np.concatenate((p2_data, [p2_data[0]]))  # Close the loop

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, p1_data, color='blue', alpha=0.25)
    ax.fill(angles, p2_data, color='red', alpha=0.25)
    ax.plot(angles, p1_data, color='blue', linewidth=2, label=player1)
    ax.plot(angles, p2_data, color='red', linewidth=2, label=player2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes)

    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    plt.title(f'Radar Chart: {player1} vs {player2}')
    plt.savefig(f'./Results/results3/Charts/{player1}_vs_{player2}_radar.png')
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Radar chart for player comparison.")
    parser.add_argument('--p1', type=str, required=True, help="Name of Player 1") # name of player 1
    parser.add_argument('--p2', type=str, required=True, help="Name of Player 2") # name of player 2
    parser.add_argument('--Attribute', type=str, nargs='+', required=True, help="List of statistics to compare") # The atribute
    
    args = parser.parse_args()
    radar_chart(args.p1, args.p2, args.Attribute)

# EXAMPLE
# python radarChartPlot.py --p1 'Gabriel Martinelli' --p2 'Amad Diallo' --Attribute Gls Ast xG 