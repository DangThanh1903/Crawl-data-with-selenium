from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('results.csv')
statistics_columns = ['Gls', 'Ast', 'xG', 'npxG', 'xAG', 'PrgC', 'PrgP', 'PrgR']
X = data[statistics_columns].fillna(0)
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
data['Cluster'] = kmeans.labels_
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot 2D PCA of the clusters
plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=data['Cluster'], cmap='viridis')
plt.title('Player Clusters with PCA')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.savefig('./Results/results3/PCA/pca_clusters.png')
plt.show()

print("PCA and cluster visualization completed.")
