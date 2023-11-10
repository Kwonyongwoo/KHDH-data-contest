from google.colab import drive
drive.mount('/content/drive')
#HGB
import pandas as pd
df=pd.read_excel('/content/drive/MyDrive/final/의사(최종).xlsx')
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.ensemble import HistGradientBoostingClassifier

data = df[['인구', '매매가격','전세가격', '노령화지수','녹지비율','생활편의시설 수', '대중교통 이용객 수','임금','요양기관 수']].to_numpy()
target = df['지역'].to_numpy()

hgb = HistGradientBoostingClassifier()
scores = cross_validate(hgb, data,target,return_train_score=True, n_jobs=-1)

#print(np.mean(scores['train_score']), np.mean(scores['test_score']))

from sklearn.inspection import permutation_importance

hgb.fit(data,target)
result = permutation_importance(hgb, data, target, n_repeats=10,
                                random_state=42, n_jobs=-1)
#print(result.importances_mean)
#check the Correlation between doctors' work area and other factors in the area
#hgb.predict([[ ]])
