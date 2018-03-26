# import the functions in other python script
import regrid_swaths as rs

# dates and maths
from datetime import datetime
import numpy as np

# for plotting
import matplotlib.pyplot as plt

import pandas as pd
import xarray as xr

## Read in data

ds=xr.open_dataset('CLM4_PFT.geos.025x03125.nc')

lats = ds.lat
lons = ds.lon

df = ds.to_dataframe()
df = df.reset_index()
df = df.drop('time',1)

### 
### Limit df to just Australian region data ~ S W N E ~ [-45, 108.75, -10, 156.25]

for i in reversed(range(len(df))):
    if df.loc[i,'lat'] > -10:
        lat_max = i

for i in range(len(df)):
    if df.loc[i,'lat'] < -45:
        lat_min = i+1



X = df.iloc[lat_min:lat_max,:]
X = X.reset_index(drop=True)

X = X.sort_values(['lon','lat'])
X = X.reset_index(drop=True)

for i in reversed(range(len(X))):
    if X.loc[i,'lon'] > 156.25:
        lon_max = i

for i in range(len(X)):
    if X.loc[i,'lon'] < 108.75:
        lon_min = i+1
 
    
Aus_lons = np.unique(X.loc[lon_min:lon_max-1,'lon'])
Aus_lats = np.unique(df.loc[lat_min:lat_max-1,'lat'])


df = X.iloc[lon_min:lon_max,:]
df = df.reset_index(drop=True)

X = X.sort_values(['lat','lon'])
X = X.reset_index(drop=True)
df = df.sort_values(['lat','lon'])
df = df.reset_index(drop=True)


## Remove oceans

from mpl_toolkits.basemap import Basemap
from matplotlib.path import Path


# S W N E
__AUSREGION__=[-45, 108.75, -7, 156.25]
region=__AUSREGION__
map =Basemap(llcrnrlat=region[0], urcrnrlat=region[2], llcrnrlon=region[1], urcrnrlon=region[3],
                  resolution='i', projection='merc')

x, y = map(df.loc[:,'lon'].values, df.loc[:,'lat'].values)

locations = np.c_[x, y]

polygons = [Path(p.boundary) for p in map.landpolygons]

result = np.zeros(len(locations), dtype=bool) 

for polygon in polygons:

    result += np.array(polygon.contains_points(locations))

df = df[~result==False]
df = df.reset_index(drop=True)

no_ocean_lons = np.unique(df.loc[:,'lon'])
no_ocean_lats = np.unique(df.loc[:,'lat'])
no_ocean_data1 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data2 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data3 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data4 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data5 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data6 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data7 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data8 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data9 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data10 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data11 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data12 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data13 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data14 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data15 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)
no_ocean_data16 = np.full((len(no_ocean_lats),len(no_ocean_lons)), np.nan)

for i in range(len(df)):
    value_lon = df.loc[i,'lon']
    value_lat = df.loc[i,'lat']
    pos_lon = np.where( no_ocean_lons==value_lon )
    pos_lat = np.where( no_ocean_lats==value_lat )
    no_ocean_data1[pos_lat,pos_lon] = df.iloc[i,2]
    no_ocean_data2[pos_lat,pos_lon] = df.iloc[i,3]
    no_ocean_data3[pos_lat,pos_lon] = df.iloc[i,4]
    no_ocean_data4[pos_lat,pos_lon] = df.iloc[i,5]
    no_ocean_data5[pos_lat,pos_lon] = df.iloc[i,6]
    no_ocean_data6[pos_lat,pos_lon] = df.iloc[i,7]
    no_ocean_data7[pos_lat,pos_lon] = df.iloc[i,8]
    no_ocean_data8[pos_lat,pos_lon] = df.iloc[i,9]
    no_ocean_data9[pos_lat,pos_lon] = df.iloc[i,10]
    no_ocean_data10[pos_lat,pos_lon] = df.iloc[i,11]
    no_ocean_data11[pos_lat,pos_lon] = df.iloc[i,12]
    no_ocean_data12[pos_lat,pos_lon] = df.iloc[i,13]
    no_ocean_data13[pos_lat,pos_lon] = df.iloc[i,14]
    no_ocean_data14[pos_lat,pos_lon] = df.iloc[i,15]
    no_ocean_data15[pos_lat,pos_lon] = df.iloc[i,16]
    no_ocean_data16[pos_lat,pos_lon] = df.iloc[i,17]    

rs.plot_map(no_ocean_data1,no_ocean_lats,no_ocean_lons,linear=False,
            vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')

plt.savefig('test_plot3.png')
plt.close()
print('test_plot3.png saved')



no_ocean_data1_reshape = np.reshape(no_ocean_data1,(len(no_ocean_data1)*len(no_ocean_data1[0])))
no_ocean_data2_reshape = np.reshape(no_ocean_data2,(len(no_ocean_data2)*len(no_ocean_data2[0])))
no_ocean_data3_reshape = np.reshape(no_ocean_data3,(len(no_ocean_data3)*len(no_ocean_data3[0])))
no_ocean_data4_reshape = np.reshape(no_ocean_data4,(len(no_ocean_data4)*len(no_ocean_data4[0])))
no_ocean_data5_reshape = np.reshape(no_ocean_data5,(len(no_ocean_data5)*len(no_ocean_data5[0])))
no_ocean_data6_reshape = np.reshape(no_ocean_data6,(len(no_ocean_data6)*len(no_ocean_data6[0])))
no_ocean_data7_reshape = np.reshape(no_ocean_data7,(len(no_ocean_data7)*len(no_ocean_data7[0])))
no_ocean_data8_reshape = np.reshape(no_ocean_data8,(len(no_ocean_data8)*len(no_ocean_data8[0])))
no_ocean_data9_reshape = np.reshape(no_ocean_data9,(len(no_ocean_data9)*len(no_ocean_data9[0])))
no_ocean_data10_reshape = np.reshape(no_ocean_data10,(len(no_ocean_data10)*len(no_ocean_data10[0])))
no_ocean_data11_reshape = np.reshape(no_ocean_data11,(len(no_ocean_data11)*len(no_ocean_data11[0])))
no_ocean_data12_reshape = np.reshape(no_ocean_data12,(len(no_ocean_data12)*len(no_ocean_data12[0])))
no_ocean_data13_reshape = np.reshape(no_ocean_data13,(len(no_ocean_data13)*len(no_ocean_data13[0])))
no_ocean_data14_reshape = np.reshape(no_ocean_data14,(len(no_ocean_data14)*len(no_ocean_data14[0])))
no_ocean_data15_reshape = np.reshape(no_ocean_data15,(len(no_ocean_data15)*len(no_ocean_data15[0])))
no_ocean_data16_reshape = np.reshape(no_ocean_data16,(len(no_ocean_data16)*len(no_ocean_data16[0])))
no_ocean_lats_reshape = np.repeat(no_ocean_lats, len(no_ocean_lons))
no_ocean_lons_reshape = np.tile(no_ocean_lons, len(no_ocean_lats))
X = np.full((len(no_ocean_data1_reshape),18), np.nan) 
X[:,0] = no_ocean_data1_reshape
X[:,1] = no_ocean_data2_reshape 
X[:,2] = no_ocean_data3_reshape
X[:,3] = no_ocean_data4_reshape
X[:,4] = no_ocean_data5_reshape
X[:,5] = no_ocean_data6_reshape
X[:,6] = no_ocean_data7_reshape
X[:,7] = no_ocean_data8_reshape
X[:,8] = no_ocean_data9_reshape
X[:,9] = no_ocean_data10_reshape
X[:,10] = no_ocean_data11_reshape 
X[:,11] = no_ocean_data12_reshape
X[:,12] = no_ocean_data13_reshape
X[:,13] = no_ocean_data14_reshape
X[:,14] = no_ocean_data15_reshape
X[:,15] = no_ocean_data16_reshape
X[:,16] = no_ocean_lats_reshape
X[:,17] = no_ocean_lons_reshape



to_delete = np.full(len(X)*18,np.nan)
count = 0
for y in range(len(X[0])):
    for i in range(len(X)):
        if not np.isfinite(X[i,y]):
            to_delete[count] = i
            count +=1
        
to_delete = np.unique(to_delete)
# =============================================================================
# to_delete = np.lib.pad(to_delete, (0,(len(X)-len(to_delete))), 'constant', constant_values=(np.nan))
# =============================================================================

         
for i in reversed(range(len(X))):
    if np.isfinite(to_delete[i]):
        X = np.delete(X,to_delete[i],0)




###
### K-Means clustering


# =============================================================================
# from mpl_toolkits.mplot3d import Axes3D
# 
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=X[:,0])
# 
# # rotate the axes and update
# for angle in range(0, 360):
#     ax.view_init(90, angle)
# =============================================================================


## Normalise variables
        
from sklearn import preprocessing

d = preprocessing.MinMaxScaler().fit_transform(X)
X[:,16] = d[:,16]
X[:,17] = d[:,17]

# =============================================================================
# df.loc[:,'lat'] = d[:,16]
# df.loc[:,'lon'] = d[:,17]
# =============================================================================


# =============================================================================
# W = np.full((8900,2), np.nan) 
# W[:,1] = X[:,3]
# W[:,0] = X[:,2]
# =============================================================================

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=6)
kmeans = kmeans.fit(X)
labels = kmeans.predict(df)
C = kmeans.cluster_centers_
L = kmeans.labels_
# =============================================================================
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=L)
# ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c='#050505', s=1000)
# =============================================================================
           
L = np.array(L, dtype=float)
for i in range(len(to_delete)):
    if np.isfinite(to_delete[i]):
        L = np.insert(L,to_delete[i].astype(int),np.nan)
L_reshape = np.reshape(L,(len(no_ocean_lats),len(no_ocean_lons)))
L_reshape = L_reshape+1    



rs.plot_map(L_reshape,no_ocean_lats,no_ocean_lons,linear=False,
            vmin=1,vmax=7,cbarlabel='Cluster', cmap="tab10")
plt.savefig('test_plot4.png')
plt.close()
print('test_plot4.png saved')



        




######## Plot Elbow Curve
# =============================================================================
# 
# from scipy.spatial.distance import cdist
# 
# # create new plot and data
# plt.plot()
# colors = ['b', 'g', 'r']
# markers = ['o', 'v', 's']
#  
# # k means determine k
# distortions = []
# K = range(1,10)
# for k in K:
#     kmeanModel = KMeans(n_clusters=k).fit(X)
#     kmeanModel.fit(X)
#     distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
#  
# # Plot the elbow
# plt.plot(K, distortions, 'bx-')
# plt.xlabel('k')
# plt.ylabel('Distortion')
# plt.title('The Elbow Method showing the optimal k')
# # =============================================================================
# # plt.savefig('Elbow Plot.png')
# # =============================================================================
# plt.show()
# =============================================================================


##### Silhouette Method
# =============================================================================
# 
# from sklearn.metrics import silhouette_samples, silhouette_score
# import matplotlib.cm as cm
# 
# range_n_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# for n_clusters in range_n_clusters:
#     # Create a subplot with 1 row and 2 columns
#     fig, (ax1, ax2) = plt.subplots(1, 2)
#     fig.set_size_inches(18, 7)
# 
#     # The 1st subplot is the silhouette plot
#     # The silhouette coefficient can range from -1, 1 but in this example all
#     # lie within [-0.1, 1]
#     ax1.set_xlim([-0.1, 1])
#     # The (n_clusters+1)*10 is for inserting blank space between silhouette
#     # plots of individual clusters, to demarcate them clearly.
#     ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])
# 
#     # Initialize the clusterer with n_clusters value and a random generator
#     # seed of 10 for reproducibility.
#     clusterer = KMeans(n_clusters=n_clusters, random_state=10)
#     cluster_labels = clusterer.fit_predict(X)
# 
#     # The silhouette_score gives the average value for all the samples.
#     # This gives a perspective into the density and separation of the formed
#     # clusters
#     silhouette_avg = silhouette_score(X, cluster_labels)
#     print("For n_clusters =", n_clusters,
#           "The average silhouette_score is :", silhouette_avg)
# 
#     # Compute the silhouette scores for each sample
#     sample_silhouette_values = silhouette_samples(X, cluster_labels)
# 
#     y_lower = 10
#     for i in range(n_clusters):
#         # Aggregate the silhouette scores for samples belonging to
#         # cluster i, and sort them
#         ith_cluster_silhouette_values = \
#             sample_silhouette_values[cluster_labels == i]
# 
#         ith_cluster_silhouette_values.sort()
# 
#         size_cluster_i = ith_cluster_silhouette_values.shape[0]
#         y_upper = y_lower + size_cluster_i
# 
#         color = cm.spectral(float(i) / n_clusters)
#         ax1.fill_betweenx(np.arange(y_lower, y_upper),
#                           0, ith_cluster_silhouette_values,
#                           facecolor=color, edgecolor=color, alpha=0.7)
# 
#         # Label the silhouette plots with their cluster numbers at the middle
#         ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
# 
#         # Compute the new y_lower for next plot
#         y_lower = y_upper + 10  # 10 for the 0 samples
# 
#     ax1.set_title("The silhouette plot for the various clusters.")
#     ax1.set_xlabel("The silhouette coefficient values")
#     ax1.set_ylabel("Cluster label")
# 
#     # The vertical line for average silhouette score of all the values
#     ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
# 
#     ax1.set_yticks([])  # Clear the yaxis labels / ticks
#     ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
# 
#     # 2nd Plot showing the actual clusters formed
#     colors = cm.spectral(cluster_labels.astype(float) / n_clusters)
#     ax2.scatter(X[:, 0], X[:, 1], marker='.', s=30, lw=0, alpha=0.7,
#                 c=colors, edgecolor='k')
# 
#     # Labeling the clusters
#     centers = clusterer.cluster_centers_
#     # Draw white circles at cluster centers
#     ax2.scatter(centers[:, 0], centers[:, 1], marker='o',
#                 c="white", alpha=1, s=200, edgecolor='k')
# 
#     for i, c in enumerate(centers):
#         ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
#                     s=50, edgecolor='k')
# 
#     ax2.set_title("The visualization of the clustered data.")
#     ax2.set_xlabel("Feature space for the 1st feature")
#     ax2.set_ylabel("Feature space for the 2nd feature")
# 
#     plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
#                   "with n_clusters = %d" % n_clusters),
#                  fontsize=14, fontweight='bold')
# 
# # =============================================================================
# #     plt.savefig('Silhouette Plot' + str(n_clusters) + '.png')
# # =============================================================================
# 
#     plt.show()
# =============================================================================


#### PFT Plots
# =============================================================================
# data = df['PFT_CROP']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT1.png')
# plt.close()
# 
# data = df['PFT_C4_GRSS']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT2.png')
# plt.close()
# 
# data = df['PFT_C3_NARC_GRSS']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT3.png')
# plt.close()
# 
# data = df['PFT_C3_ARCT_GRSS']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT4.png')
# plt.close()
# 
# data = df['PFT_BDLF_DECD_BORL_SHRB']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT5.png')
# plt.close()
# 
# data = df['PFT_BDLF_DECD_TMPT_SHRB']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT6.png')
# plt.close()
# 
# data = df['PFT_BDLF_EVGN_SHRB']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT7.png')
# plt.close()
# 
# data = df['PFT_BDLF_DECD_BORL_TREE']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT8.png')
# plt.close()
# 
# data = df['PFT_BDLF_DECD_TMPT_TREE']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT9.png')
# plt.close()
# 
# data = df['PFT_BDLF_DECD_TROP_TREE']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT10.png')
# plt.close()
# 
# data = df['PFT_BDLF_EVGN_TMPT_TREE']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT11.png')
# plt.close()
# 
# data = df['PFT_BDLF_EVGN_TROP_TREE']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT12.png')
# plt.close()
# 
# data = df['PFT_NDLF_DECD_BORL_TREE']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT13.png')
# plt.close()
# 
# data = df['PFT_NDLF_EVGN_BORL_TREE']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT14.png')
# plt.close()
# 
# data = df['PFT_NDLF_EVGN_TMPT_TREE']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT15.png')
# plt.close()
# 
# data = df['PFT_BARE']
# data = np.reshape(data,(len(Aus_lats),len(Aus_lons)))
# 
# rs.plot_map(data,Aus_lats,Aus_lons,linear=False,
#             vmin=0.0000001,vmax=1,cbarlabel='molec/cm2')
# 
# plt.savefig('PFT16.png')
# plt.close()
# =============================================================================
