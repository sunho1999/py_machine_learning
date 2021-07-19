# 데이터 살펴보기

* part3
    ---
    
    UCI 데이터 셋 - "auto mpg" 상세 항목
    
    No.|속성(attributes)|속성(name)|데이터 상세(범위)
    ---|---|---|---
    1|mpg|연비|연속 값
    2|cylinders|실린더 수|이산 값(예시:3,4,6,8)
    3|displacement|배기량|연속 값
    4|horsepower|출력| 연속 값
    5|weight|차중|연속 값
    6|aceeleration|가속능력| 연속 값
    7|model_year|출시년도|이산 값(예:70,81,80,81)
    8|origin|제조국|이산 값(예:1(USA),2(EU),3(JPN)
    9|name|모델명|문자 열
    * chap1 데이터프레임의 구조
        ---
        * 데이터 내용 미리보기
        ~~~
        * 앞부분 미리보기:DataFrame 객체.head(n) (디폴드 값:n=5)
        * 뒷부분 미리보기:DataFrame 객체.tail(n) (n은 행의 개수)
        ~~~
        * 데이터 요약 정보 확인하기
        ~~~
        데이터프레임의 크기 확인:DataFrame 객체.shape
        ~~~
        ~~~
        데이터프레임의 기본 정보 출력:DataFrame 객체.info()
        ~~~
    
        판다스 자료형의 종류 
  
         판다스 자료형|파이썬 자료형|비고
        ---|---|---
        int64|int|정수형 데이터
        float64|float|실수형 데이터(소수점이 있는수)
        object|string|문자열데이터
        datetime64,timedelta64|없음(datetime라이브러리활용)|시간 데이터

        * 데이터프레임의 기술 통계 정보요약
        ~~~
        데이터프레임의 기술 정보 요약: DataFrame 객체.describe()
        산술데이터가 아닌 열에 대한 정보를 포함하고 싶을 때는, include = 'all'을 추가
        ~~~
        * 데이터 개수 확인
        ~~~
        열 데이터 개수 확인: DataFrame 객체.count()
        count()메소드는 데이터프레임의 각 열이 가지고 있는 데이터 개수를 시리즈 객체로 반환.
        이때 유효한 값의 개수만을 계산한다.
        ~~~
        * 각 열의 고유값 개수
        ~~~
        열 데이터의 고유값 개수: Dataframe 객체["열 이름"].value_counts()
        dropna=True를 설정하면 데이터 값 중 NaN을 제외하고 카운트함.
        기본으로 dropna=False가 설정됨. 
        ~~~
    * chap2 통계 함수 적용
        ---
        * 평균값
        ~~~
        * 모든 열의 평균값: DataFrame 객체.mean()
        * 특정 열의 평균값: DataFrame 객체["열 이름"].mean()
        ~~~
        * 중간값
        ~~~
        * 모든 열의 중간값: DataFrame 객체.median()
        * 특정 열의 중간값: DataFrame 객체["열 이름"].median()
        ~~~
        * 최대값
        ~~~
        * 모든 열의 중간값: DataFrame 객체.max()
        * 특정 열의 중간값: DataFrame 객체["열 이름"].max()
        ~~~
        * 최소값
        ~~~
        * 모든 열의 중간값: DataFrame 객체.min()
        * 특정 열의 중간값: DataFrame 객체["열 이름"].min()
        ~~~
    * chap 3 판다스 내장 그래프 도구 활용
        ---
        판다스 내장 plot() 메소드 - 그래프 종류
        
        kind 옵션|설명|kind 옵션|설명
        ---|---|---|---
        'line'|선 그래프|'kde'|커널 밀도 그래프
        'bar'|수직 막대 그래프|'area'|면적 그래프
        'barh'|수평 막대 그래프|'pie'|파이 그래프
        'his'|히스토그램|'scatter'|산점도 그래프
        'box'|박스 플롯|'hexbin'|고밀도 산점도 그래프
        
        * 선 그래프
        ~~~
        선 그래프 : DataFrame 객체.plot()
        ~~~
        * 막대 그래프
        ~~~
        * 막대 그래프: DataFrame 객체.plot(kind='bar')
        ~~~
        * 히스토그램
        ~~~
        * 히스토그램: DataFrame 객체.plot(kind='hist')
        ~~~