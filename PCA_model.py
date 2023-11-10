#PCA
import pandas as pd

file_name = './final final data/의사(최종).xlsx'

# Daraframe형식으로 엑셀 파일 읽기
df = pd.read_excel(file_name)
df.drop(['연도'], axis=1, inplace=True)

onehot= pd.get_dummies(df['지역'])

df = pd.concat([df, onehot], axis=1)

from sklearn.preprocessing import StandardScaler

# 정규화를 적용할 열들 선택
cols_to_normalize = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산','서울', '세종', '울산', '인천', '전남', '전북', '제주', '충남', '충북']

# StandardScaler 객체 생성 및 정규화 수행
scaler = StandardScaler()
df[cols_to_normalize] = scaler.fit_transform(df[cols_to_normalize])

from sklearn.cluster import KMeans

df.drop(['인구','매매가격','전세가격','노령화지수','녹지비율','생활편의시설 수','대중교통 이용객 수','임금','요양기관 수'], axis=1, inplace=True)

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# 'Category' 컬럼을 별도로 보관
categories = df['지역']

# 'Category' 컬럼 제거 후, 정규화
df.drop(columns=['지역'], inplace=True)
scaler = StandardScaler()
df_norm = scaler.fit_transform(df)

# K-Means 클러스터링 모델 생성 및 학습
num_clusters = 17  # 클러스터의 개수 (원하는 클러스터 수로 조정)
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(df_norm)

# PCA를 사용하여 2차원으로 축소
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_norm)

# 클러스터링 결과를 DataFrame에 추가
df_pca = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])
df_pca['Cluster'] = kmeans.labels_

# 'Category' 컬럼 다시 추가
df_pca['지역'] = categories

# 시각화
plt.figure(figsize=(10, 6))
colors = ['blue', 'red', 'green','pink','white','yellow','blue', 'red', 'green','blue', 'red', 'green','blue', 'red', 'green','blue', 'red']
for cluster_num, color in zip(range(num_clusters), colors):
    plt.scatter(
        df_pca.loc[df_pca['Cluster'] == cluster_num, 'PC1'],
        df_pca.loc[df_pca['Cluster'] == cluster_num, 'PC2'],
        c=color, label=f'Cluster {cluster_num}'
    )
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('K-Means Clustering Visualization with PCA')
plt.legend()
plt.grid(True)
plt.show()