from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from Initial_exploration_manipulation import df_vectorized, df

import plotly.graph_objects as go
#check df_vectorised imported correctly
#print(df_vectorized.head())

#using the elbow method to determin the optimum no of clusters
# wcss = []  # Within-cluster sum of squares list
# for i in range(1, 11):  # Test 1 through 10 clusters
#     kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
#     kmeans.fit(df_vectorized)
#     wcss.append(kmeans.inertia_)

        #plot the results in plotly
        # Create the plot with Plotly
# fig = go.Figure(data=go.Scatter(x=np.arange(1, 11, 1), y=wcss, mode='lines+markers'))

# # Add titles and labels
# fig.update_layout(title='Elbow Method with Plotly',
#                   xaxis_title='Number of clusters',
#                   yaxis_title='WCSS',
#                   xaxis=dict(tickmode='linear'),
#                   plot_bgcolor='white')

        # # Show the plot
# fig.show()
        # from the results the optimum clusters looks to be 5 or 8, given the domain is job categories,
        #according to Linkedin they have 7 most dominant
        # Financial Services.
        # Information Technology and Services.
        # Hospital & Health Care.
        # Construction.
        # Retail.
        # Education Management.
        # Accounting.
k = 5 #  chosen number of clusters

# Fit K-means with the chosen number of clusters
kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(df_vectorized)

# Retrieve the cluster assignments for each data point
cluster_labels = kmeans.labels_
#print(cluster_labels)
# write the cluster labels to the csv data set
df['Cluster']= kmeans.labels_
df.to_csv('job_adverts_with_clusters_1.1.csv', index=False)