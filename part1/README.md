#pandas 입문

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
        ~~~
        dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 
                    'c3':[10,11,12], 'c4':[13,14,15]}
        # 판다스 DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환. 
        변수 df에 저장. 
        df = pd.DataFrame(dict_data)
        ~~~
        테이블 생성
    
        "  "|c0|c1|c2|c3|c4
        ---|---|---|---|---|---
        0|1|4|7|10|13
        1|2|5|8|11|14
        2|3|6|9|12|15
                
          