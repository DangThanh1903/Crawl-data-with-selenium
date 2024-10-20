from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('results.csv')
statistics_columns = ['Gls', 'Ast', 'xG', 'npxG', 'xAG', 'PrgC', 'PrgP', 'PrgR']
X = data[statistics_columns].fillna(0)  # Replace missing values with 0
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    inertia.append(kmeans.inertia_)

# Plot inertia vs. number of clusters
plt.figure()
plt.plot(K, inertia, 'bo-')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.savefig('./Results/results3/elbow_kmeans/elbow_method.png')
plt.show()

print("Optimal number of clusters can be inferred from the elbow method.")
