#pandas 공부하기 

* part1
    * chap1
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
    
        
            
          