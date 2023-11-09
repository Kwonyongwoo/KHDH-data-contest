import pandas as pd
import random
import openpyxl


# Data rows
df= pd.DataFrame({
    '2013': [11,5, 13, 19, 10, 8,5 , 9, 5, 20, 17, 20, 23, 31, 24, 17, 20],
    '2014': [12,7, 14, 20, 10, 10,7 , 9, 6, 21, 18, 20, 24, 32, 25, 18, 20]
    })


# Create the DataFrame

df1 = pd.DataFrame({'지역': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']})

# 년도 데이터를 월별 데이터로 변환하는 함수
def year_to_month(year_data):
    month_data = []
    for year in year_data:
        for month in range(1, 13):
            month_data.append(year + random.random())
    return month_data

for year in range(2013, 2015):
    # 년도 데이터 리스트

    year_data = df[str(year)].values.tolist()

        # 변환된 월별 데이터를 출력
    month_data = year_to_month(year_data)
    df16 = pd.DataFrame([month_data[i:i+12] for i in range(0, len(month_data), 12)],
                            columns=[f"{year}년 01월", f"{year}년 02월", f"{year}년 03월", f"{year}년 04월",
                                     f"{year}년 05월", f"{year}년 06월", f"{year}년 07월", f"{year}년 08월",
                                     f"{year}년 09월", f"{year}년 10월", f"{year}년 11월", f"{year}년 12월"])
    df1 = pd.concat([df1, df16], axis=1)
print(df1)
# Save Excel file
df1.to_excel('추가.xlsx', index=False)