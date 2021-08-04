# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import folium

# 서울 지도 만들기
# 산악 지형 등의 지형이 보다 선명하게 드러난다.
seoul_map2 = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain',
                        zoom_start=12)
# 흑백 스타일로 도로망을 강조해서 보여준다.
seoul_map3 = folium.Map(location=[37.55,126.98], tiles='Stamen Toner', 
                        zoom_start=15)

# 지도를 HTML 파일로 저장하기
seoul_map2.save('./seoul2.html')
seoul_map3.save('./seoul3.html')