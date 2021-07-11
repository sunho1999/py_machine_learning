# pandas 공부하기 

* part1
  ---
    * chap1
      ---
        * make series
        ~~~
        a = pandas.Series("딕셔너리")
        ~~~
        판다스 Series()함수로 dictionary를 Series로 변환. 변수 a로 저장
        *****
        * index 속성
        ~~~
        인덱스 배열: Series객체.index
        ~~~
        * value 속성
        ~~~
        데이터 값 배열: Series객체.values
        ~~~
      *****
    * chap2 
      ---
        * make DataFrame
        ~~~
        딕셔너리 --> 데이터프레임 변환: pandas.DataFrame(딕셔너리객체)
        ~~~
        ~~~python
        dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 
                    'c3':[10,11,12], 'c4':[13,14,15]}
        # 판다스 DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환. 
        # 변수 df에 저장. 
        df = pd.DataFrame(dict_data)
        ~~~
        테이블 생성
    
        "  "|c0|c1|c2|c3|c4
        ---|---|---|---|---|---
        0|1|4|7|10|13
        1|2|5|8|11|14
        2|3|6|9|12|15
        *****
        * row and column delete
        ~~~
        * 행 삭제: DataFrame 객체.drop(행 인덱스 또는 배열, axis = 0)
        * 열 삭제: DataFrame 객체.drop(열 이름 또는 배열, axis = 1)
        ~~~
      *****
    * chap3 
      ---
        * select row
        ~~~
        데이터 프레임에서 인덱스 이름을 기준으로 행을 선택할 때 loc
        정수형 위치 인덱스를 사용할 때 iloc
        ~~~
        구분|loc|iloc
        ---|---|---|
        탐색대상|인덱스 이름|정수형 위치 인덱스
        범위지정|ex)['a':'c']->'a','b',c'|[3:6]->'3','4','5'
        * select column
        ~~~
        열 1개 선택: DataFrame 객체["열 이름"]
        열 n개 선택: DataFrame 객체[[열1,열2,...,열n]]
        ~~~
        * select element
        ~~~
        * 인덱스 이름: DataFrame 객체.loc[행 인덱스,열 이름]
        * 정수 위치 인덱스: DataFrame 객체.iloc[행 번호,열번호]
        ~~~
        * add column
        ~~~
        열 추가: DataFrame 객체['추가하려는 열 이름'] = 데이터 값
        ~~~
        * add row
        ~~~
        행 추가: DataFrame.loc['새로운 행 이름'] = 데이터 값(또는 배열)
        ~~~
        * change element
        ~~~
        원소 값 변경: DataFrame 객체의 일부분 또는 원소를 선택 = 새로운 값
        ~~~
        * trans column and row
        ~~~
        행, 열 바꾸기: DataFrame 객체.transpose() 또는 DataFrame 객체.T
        ~~~
    * chap4 
        ---
      
        * 특정 열을 행 인덱스로 설정
        ~~~
        DataFrame 객체.set_index(['열 이름'] 또는 '열 이름')
        ~~~
        * 행 인덱스 재배열
        ~~~
        새로운 배열로 행 인덱스를 재지정: DataFrame 객체.reindex(새로운 인덱스 배열)
        ~~~
        * 행 인덱스 초기화
        ~~~
        정수형 위치 인덱스로 초기화: DataFrame 객체.reset_index()
        ~~~
        * 행 인덱스 기준 정렬
        ~~~
        행 인덱스 기준 정렬: DataFrame 객체.sort_index() 
        sort_index(ascending = False 내림차순)
        sort_index(ascending = True 오름차순)
        ~~~
        * 열 기준 정렬
        ~~~ 
        열기준 정렬: DataFrame 객체.sort_values()
        ~~~
      
    
        
            
          