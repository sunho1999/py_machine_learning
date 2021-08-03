# 시각화 도구 

* part4
    ---
    * Matplotlib - 기본 그래프 도구
        ---
        * chap 1-1 선그래프
            ---
            - 선 그래프(line plot)는 연속하는 데이터 값들을 직선 또는 곡선으로 연결하여
            데이터 값 사이의 관계를 나타낸다.
            - Excel파일을 다루다 보면 누락 데이터(NaN)이 발생하는데 이는 병합된 셀을 데이터프레임으로
            변환할 때 적절한 값을 찾지못해서 발생하는것이다.
            * fillna()메소드의 methond ='ffill'을 사용하면 누락데이터가 들어 있는 행의 바로 앞에 위치한 행의 데이터 값으로 채운다.
            ~~~python
            df.fillna(method = 'ffill')
            ~~~
            - 차트 제목,축 이름 추가
            ~~~
            그래프 객체에 차트 제목을 추가할 때 title()
            x 축이름은 xlabel()
            y 축이름은 ylabel()
            ~~~
            - 그래프 꾸미기
            ~~~
            x축 눈금 라벨의 글씨가 서로 곂쳐 잘 안보이는 이유: 눈금 라벨이 들어갈 만한 충분한 여유 공간이 없어서 발생함.
            >> 두 가지 해결책
            -figure()함수로 그림틀의 사이즈를 더 크게 설정 -xticks()함수를 활용하여 x축 눈금라벨을 반시계 방향으로 회전
            ~~~
            
            ex)4.3_matplotlib_hangul.py 실행 화면
            <img width="644" alt="4 3_matlplotlib_hangul py 예시" src="https://user-images.githubusercontent.com/80037682/127850037-43c1c00b-1b28-4cf3-b917-c72ae6f07b6d.png">
            > 글자가 여유공간이 부족해 깨진상태로 그래프가 만들어진다.
            
            ex)4.4_matplotlib.line3.py 실행화면
            <img width="1395" alt="스크린샷 2021-08-02 오후 7 48 14" src="https://user-images.githubusercontent.com/80037682/127850161-4ca425ef-0413-475b-a45e-54a84756ea5b.png">
            > 가로,세로 비중을 늘리고 x축 눈금 라벨을 반시계방향으로 돌려 글자 깨짐현상을 해결하였다.
            
            ex) 4.5_matplotlib.line4.py 실행화면 
            
            <img width="1400" alt="스크린샷 2021-08-02 오후 7 59 24" src="https://user-images.githubusercontent.com/80037682/127851715-99801cec-8841-45e7-99f2-ee2e8e215cd5.png">
    
            >plt.style.use('ggplot')으로 그래프 스타일 서식을 지정함          
            marker = 'o',markersize = 10 을 이용하여 그래프에 원모양의 점을 마커로 표시한다.
            
            * 그래프에 대한 설명을 덧붙이는 주석에 대해 알아보기.
            ~~~python
            #범례 표시
            plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)
            
            # y축 범위 지정 (최소값, 최대값)
            plt.ylim(50000, 800000)
            
            # 주석 표시 - 화살표
            plt.annotate('',
                         xy=(20, 620000),       #화살표의 머리 부분(끝점)
                         xytext=(2, 290000),    #화살표의 꼬리 부분(시작점)
                         xycoords='data',       #좌표체계
                         arrowprops=dict(arrowstyle='->', color='skyblue', lw=5), #화살표 서식
                         )
            
            plt.annotate('',
                         xy=(47, 450000),       #화살표의 머리 부분(끝점)
                         xytext=(30, 580000),   #화살표의 꼬리 부분(시작점)
                         xycoords='data',       #좌표체계
                         arrowprops=dict(arrowstyle='->', color='olive', lw=5),  #화살표 서식
                         )
            
            # 주석 표시 - 텍스트
            plt.annotate('인구이동 증가(1970-1995)',  #텍스트 입력
                         xy=(10, 550000),            #텍스트 위치 기준점
                         rotation=25,                #텍스트 회전각도
                         va='baseline',              #텍스트 상하 정렬
                         ha='center',                #텍스트 좌우 정렬
                         fontsize=15,                #텍스트 크기
                         )
            
            plt.annotate('인구이동 감소(1995-2017)',  #텍스트 입력
                         xy=(40, 560000),            #텍스트 위치 기준점
                         rotation=-11,               #텍스트 회전각도
                         va='baseline',              #텍스트 상하 정렬
                         ha='center',                #텍스트 좌우 정렬
                         fontsize=15,                #텍스트 크기
                         )
            ~~~
            * ex) 4.7_matploylib.annotate.py 실행화면
            
            <img width="1395" alt="스크린샷 2021-08-02 오후 8 05 53" src="https://user-images.githubusercontent.com/80037682/127852158-92bea3a9-b4d2-4da9-9e83-f3ee21d9e609.png">
          
            > annotate()함수로 주석을 넣고 ylim()함수로 주석을 넣을 y축 여백공간을 늘려준다.  
            plt.legend()을 이용해 우측 상단에 범례를 넣어준다.
            
            * 화면 분할하여 그래프 여러개 그리기 -axe 객체 활용
            ~~~
            figure()함수를 사용하여 그림틀을 만들고 figsize옵션으로 그림틀의 크기를 설정한다.
            fig 객체에 add_suplot()메소드를 적용하여 그림틀을 여러개로 분할한다.
            ~~~
          
            * ex) 4.8_matplotlib_lines1.py 실행화면
            
            <img width="1197" alt="스크린샷 2021-08-02 오후 8 12 46" src="https://user-images.githubusercontent.com/80037682/127852950-aaccd5e8-4f27-4034-a0bc-d9a0decb97fa.png">
            
            * ex) 4.10_matplotlib_lines3.py 실행화면
            
            <img width="1434" alt="스크린샷 2021-08-02 오후 8 14 01" src="https://user-images.githubusercontent.com/80037682/127853099-c2794e0b-b83c-4576-be79-06d13959b92c.png">
          
            > 이처럼 axe 객체를 이용하여 화면분할과 한화면에 다중의 그래프를 만들수 있다.
          
        * chap 1-2 면적그래프
          ---
            - 면적 그래프(area plot)는 선 그래프를 확장한 개념으로 누적 선 그래프라고 부르기도 한다.
            - 면적 그래프는 각 열의 데이터를 선 그래프로 구현하는데, 선 그래프와 x 축 사이의 공간에 색이 입혀진다.
            - 색의 투명도(alpha)는 기본값 0.5로 투과되어 보인다.(투명도:0~1범위)
            - stacked = True 옵션으로 각 열의 선 그래프를 다른 열의 선 그래프 위로 쌓아 올리는 방식으로 표현된다.
            
            * ex) 4.13_matplotlib_area1.py 실행화면 (stacked=False)로 그래프 누적x
            
            <img width="1295" alt="스크린샷 2021-08-03 오후 7 57 40" src="https://user-images.githubusercontent.com/80037682/128004624-6a15b812-fcdb-4063-8c25-d902eb98b803.png">

            * ex) 4.14_matplotlib_area2.py 실행화면 (stacked=True)로 그래프 누적o
    
            <img width="1264" alt="스크린샷 2021-08-03 오후 7 58 02" src="https://user-images.githubusercontent.com/80037682/128004932-25becf8f-fb7d-41fc-b91d-c7e944526ae9.png">
            
        * chap 1-3 막대그래프
          ---
            - 막대 그래프(bar plot)는 데이터 값의 크기에 비례하여 높이를 갖는 직사각형 마대로 표현된다.
            - 막대 높이의 상대적 길이 차이를 통해 값의 크고 작음을 설명한다.
            - 세로형 막대 그래프는 시간적으로 차이가 나는 두점에서 데이터 값의 차이를 잘 설명한다.
            - 가로형 막대 그래프는 각 변수 사이 값의 크기를 설명하는데 적합하다.
            ~~~
            * 세로형 막대 그래프 : plot() 메소드에 kind = 'bar'을 입력함
            * 가로형 막대 그래프 : plot() 메소드에 kind = 'barh'을 입력함
            ~~~
            
            * ex) 4.16_matplotlib_bar1.py 실행화면 (세로형 막대 그래프)
            
            <img width="1125" alt="스크린샷 2021-08-03 오후 8 06 11" src="https://user-images.githubusercontent.com/80037682/128005528-c78835ec-777e-4382-9796-c94c699ddf5b.png">
            
            * ex) 4.17_matplotlib_barh1.py 실행화면 (가로형 막대 그래프)
    
            <img width="1195" alt="스크린샷 2021-08-03 오후 8 06 43" src="https://user-images.githubusercontent.com/80037682/128005572-39d25cce-8177-411b-b71d-8c908b2d6e57.png">
        
        * chap 1-4 히스토그램
            ---
            - 히스토그램(histogram)은 변수가 하나인 단변수 데이터의 빈도수를 그래프로 표현한다.
            - x축을 같은 크기의 여러 구간으로 나누고 각 구간에 속하는 데이터 값의 개수(빈도)를 y축에 표시한다.
            
            * ex) 4.19_matplotlib_hist.py 실행화면 
            
            <img width="790" alt="스크린샷 2021-08-03 오후 8 16 57" src="https://user-images.githubusercontent.com/80037682/128006649-7cbb38d5-cf62-4ab7-af3e-dfb83eeba6f0.png">
            
            ~~~
            plot() 메소드에 kind = 'hist'옵션을 넣고 bins=10 옵션을 지정하여 10개의 구간으로 나눔
            ~~~
