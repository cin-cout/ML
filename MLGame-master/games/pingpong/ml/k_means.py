import os
import pickle
import numpy as np

def load_pickle(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    return data['ml_1P']

now = True
allFileList = os.listdir('kmean_log/')
for file in allFileList:
    data = load_pickle('kmean_log/' + file)
    if now:
        game_info = data['scene_info'][1:-1]
        game_command = data['command'][1:-1]
        now = False
    else:
        game_info = game_info + data['scene_info'][1:-1]
        game_command = game_command + data['command'][1:-1]

#找特徵
g = game_info[0]
feature = np.array([game_info[0]['ball'][0],game_info[0]['ball'][1], game_info[0]['ball_speed'][0], 
                    game_info[0]['ball_speed'][1],  game_info[0]['blocker'][0] ])

for i in range(1, len(game_info)):
    ball_x = game_info[i]['ball'][0]
    ball_y = game_info[i]['ball'][1]
    dx = game_info[i]['ball_speed'][0]
    dy = game_info[i]['ball_speed'][1]
    platform = game_info[i]['platform_1P'][0]
    block = game_info[i]['blocker'][0]
    feature = np.vstack((feature, [ball_x, ball_y, dx, dy, block]))


#取feature
for i in range(len(game_command)):
    if game_command[i] == "NONE": game_command[i] = 0
    elif game_command[i] == "MOVE_RIGHT": game_command[i] = 1
    else: game_command[i] = 2
    
answer = np.array(game_command)

'''
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.decomposition import PCA
kmeans = KMeans(n_clusters = 3) 
kmeans.fit(feature)  
print(kmeans.score(feature, answer))
from matplotlib import pyplot as plt
pca = PCA(n_components=2).fit(feature)
pca_2d = pca.transform(feature)
# Plot based on Class
for i in range(0, pca_2d.shape[0]):
    if kmeans.labels_[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
    elif kmeans.labels_[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif kmeans.labels_[i] == 2:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')

plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2', 'Cluster 3'])
plt.show()



from sklearn.svm import SVC
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
svm = SVC(kernel='rbf',C=1,gamma='auto')
svm.fit(feature, answer)  
print(svm.score(feature, answer))
predict_label = svm.predict(feature)
pca = PCA(n_components=2).fit(feature)
pca_2d = pca.transform(feature)
# Plot based on Class
for i in range(0, pca_2d.shape[0]):
    if predict_label[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
    elif predict_label[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif predict_label[i] == 2:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')

plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2', 'Cluster 3'])
plt.show()

'''
# KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

x = np.array(feature)
y = np.array(answer)
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(feature, answer)
print(clf.score(feature, answer))
predict_label = clf.predict(feature)

pca = PCA(n_components=2).fit(feature)
pca_2d = pca.transform(feature)
# Plot based on Class
for i in range(0, pca_2d.shape[0]):
    if predict_label[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
    elif predict_label[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif predict_label[i] == 2:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')

plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2', 'Cluster 3'])
plt.show()
'''
# Actual Label
pca = PCA(n_components=2).fit(feature)
pca_2d = pca.transform(feature)
# Plot based on Class
for i in range(0, pca_2d.shape[0]):
    if answer[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
    elif answer[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif answer[i] == 2:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')

plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2', 'Cluster 3'])
plt.show()
'''