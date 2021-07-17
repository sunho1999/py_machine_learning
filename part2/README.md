# 데이터 입출력

* part2
    ---
    판다스 데이터 입출력 도구
    
    File Format|Reader|Writer
    ---|---|---
    CSV|read_csv|to_csv
    JSON|read_json|to_json
    HTML|read_html|to_html
    MS Excel|read_excel|to_excel
    SQL|read_sql|to_sql
    * chap1 (외부 파일 읽어오기)
        ---
        * CSV 파일
        ~~~
        CSV 파일 -> 데이터 프레임: pandas.read_csv("파일경로(이름)")
        header옵션:
            -'열 이름'이 되는 행을 지정
            -read_csv(file,header =?)
                - header = 0 (기본값: 0행을 열 지정)
                - header = None(행을 열 지정하지 않음)
        index_col 옵션
            - '행 주소'가 되는 열을 지정
            - read_csv(file, index_col = ?)
                - index_col = False (인덱스 지정하지 않음)
        ~~~
        * Excel 파일(확장자: .xlsx)
        ~~~
        Excel -> 데이터프레임 : pandas.read_excel("파일 경로(이름)")
        - 실행 환경에 따라서 Excel 파일 데이터 추출을 지원하는 
          xlrd라이브러리와 openpyxl라이브러리 설치가 필요함. 
          xlsx확장자는 engine옵션에 'openpyxl'이 필요!
        ~~~
        * Json 파일
        ~~~
        Json 파일 --> 데이터프레임: pandas.read_json("파일경로(이름)")
        ~~~
      *****
    * chap2 (web에서 가져오기)
        ---
        * HTML 웹 페이지에서 표 속성 가져오기
        ~~~
        판다스 read_html()함수는 HTML 웹 페이지에 있는 <table>태그에서 
        표 형식을 모두 찾아서 데이터프레임으로 변환함
        ~~~
        ~~~
        HTML 표 속성 읽기: pandas.read_html("웹 주소(URL)" 또는 "HTML 파일 경로(이름)")
        ~~~
    * chap3 (데이터 저장하기)
        ---
        * csv 파일로 저장
        ~~~
        CSV 파일로 저장: DataFrame 객체.to_csv("파일 이름(경로)")
        ~~~
        * JSON 파일로 저장
        ~~~
        JSON 파일로 저장: DataFrame 객체.to_json("파일 이름(경로)")
        ~~~
        * Excel 파일로 저장
        ~~~
        Excel 파일로 저장: DataFrame 객체.to_excel("파일 이름(경로)")
        데이터프레임 여러개를 Excel 파일로 저장: pandas.ExcelWriter("파일 이름(경로)")
        ~~~
    