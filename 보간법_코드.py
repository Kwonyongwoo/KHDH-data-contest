import numpy as np
from sklearn.linear_model import LinearRegression
data=pd.read_excel('/노후 주택 비율.xlsx')
# 예제 데이터
X = np.array([j for j in range(0,84)]).reshape(-1, 1)  # 독립 변수 (2차원 배열로 변환)
y = np.array(iloc.data[i])  # 종속 변수

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(X, y)

# 새로운 독립 변수 값에 대한 종속 변수 예측
new_X = np.array([6]).reshape(-1, 1)
predicted_y = model.predict(new_X)

print("Predicted value:", predicted_y)