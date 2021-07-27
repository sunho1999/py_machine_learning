# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('ggplot')   # 스타일 서식 지정
plt.rcParams['axes.unicode_minus']=False   # 마이너스 부호 출력 설정

# Excel 데이터를 데이터프레임 변환 
df = pd.read_excel('./남북한발전전력량.xlsx', engine= 'openpyxl', convert_float=True)
df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis='columns', inplace=True)
df.set_index('발전 전력별', inplace=True)
df = df.transpose()

# 증감율(변동률) 계산
df = df.rename(columns={'합계':'총발전량'})
print(df)
df['총발전량 - 1년'] = df['총발전량'].shift(1)
print(df)
df['증감율'] = ((df['총발전량'] / df['총발전량 - 1년']) - 1) * 100
print(df)

# 2축 그래프 그리기
#stacked = True로 인해 수력위에 화력이 쌓임
ax1 = df[['수력','화력']].plot(kind='bar', figsize=(15, 8), width=0.7, stacked=True)
ax2 = ax1.twinx()
ax2.plot(df.index, df.증감율, ls='--', marker='o', markersize=20, 
         color='green', label='전년대비 증감율(%)')  

ax1.set_ylim(0, 500)
ax2.set_ylim(-50, 50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량(억 KWh)')
ax2.set_ylabel('전년 대비 증감율(%)')

plt.title('북한 전력 발전량 (1990 ~ 2016)', size=30)
#범례 위치 설정
ax1.legend(loc='upper right')

plt.show()