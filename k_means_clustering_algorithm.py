import random
import math

#generating some random data points as sample
random.seed(0)
data = [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(200)]
#defining the number of clusters (K)
K = 3
#initializing centroids
centroids = random.sample(data, K)

#defining a function to calculate distance b/w centroids and points
#euclidean distance formula
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

#to perform kmeans
for _ in range(200):
    labels = [] #creating a list for cluster labels
    for x in data:
        distances = [distance(x, c) for c in centroids]
        cluster = distances.index(min(distances)) #taking the index of the minimum distance and assigning it to a variable
        labels.append(cluster) #adding it to labels

#updating new centroids
new_centroids = []

for k in range(K):
    cluster_x_sum = 0
    cluster_y_sum = 0
    cluster_count = 0

    for i in range(len(data)):
        if labels[i] == k:
            point = data[i]
            cluster_x_sum += point[0]
            cluster_y_sum += point[1]
            cluster_count += 1

    if cluster_count > 0:
        new_centroid = (
            cluster_x_sum / cluster_count,
            cluster_y_sum / cluster_count
        )
        new_centroids.append(new_centroid)
    else:
        new_centroids.append(centroids[k])
    #checking for convergence
    if new_centroids == centroids:
        break

    centroids = new_centroids

#creating an empty dictionary to store data points for each cluster
clusters = {}

for i, label in enumerate(labels):
    if label not in clusters:
        clusters[label] = []  #if the cluster label label is not already a key in the clusters dictionary, create an empty list
    clusters[label].append(data[i])  #add the current data point to it

#creating 2 variables
#one for the label of the cluster(0,1,2)
#one for data points belong to that cluster
for cluster_label, data_points in clusters.items():
    print(f"Cluster {cluster_label}:")
    for point in data_points:
        print(point)