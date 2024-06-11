# ▶ 캡스톤 프로젝트(@에이젠글로벌) - 전기 이륜차 배터리 재고 최적화 <img src="https://img.shields.io/badge/Team_Project-000000"/>

### - 과제 목적
- 자카르타 내 전기 이륜차 배터리 재고 최적화

### - 기대 효과
- 현황에 맞는 배터리 재고 재배치를 통한 고객 만족도 상승
- 재고 최적화를 통해 방치되는 배터리 최소화

### - 사용 툴
- Python(Pandas,Numpy,Matplotlib,Plotly)
- Excel
- Tableau

### - 역할
- 조원 4명
  - 기획, 데이터 전처리, 3D 시각화, 대시보드 작성, PPT 제작

### - 데이터
- <img width="664" alt="스크린샷 2024-01-09 135741" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/faee4ce1-1216-4bcd-89c1-d7eb486cdf05">
- <img width="661" alt="스크린샷 2024-01-09 135746" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/4470fbfa-3f28-4f98-8b9d-fd2669cf4f51">
- <img width="661" alt="스크린샷 2024-01-09 135751" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/820e65c2-1e42-46d2-9a65-1677f6a17b36">


### - 분석
- 수요 정의 - 스테이션 인근 이동중인 스쿠터의 개수
- 재고 정의 - 스테이션이 보유하고 있는 배터리 개수
- 종합 관리 지표 - 격자 내 배터리 1개당 스쿠터 수
  - 격자 1.6kmx1.3km 900개(30x30)
  - 1.4km= 이동중인 스쿠터의 10분 평균 거리<img width="661" alt="스크린샷 2024-01-09 135808" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/41862eae-4c3f-4ffb-88a7-f3d2537f9c9a">
- 최적화 방안 - 스쿠터 수에 맞춘 배터리 재배치(Grid)<img width="660" alt="스크린샷 2024-01-09 135826" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/f9abc256-ef02-4383-a5dd-1c93458822b2">
    - 최적화 전 :
https://github.com/SKYoooon/SNU_Fintech/assets/138483304/f7dd382d-cf94-4216-a2f8-6e825c8a5226

    - 최적화 후 :
https://github.com/SKYoooon/SNU_Fintech/assets/138483304/7b06a965-6348-439a-84c8-7e712ddd53d4


- 최적화 방안 - 스쿠터 수에 맞춘 배터리 재배치(3D)
https://github.com/SKYoooon/SNU_Fintech/assets/138483304/4c3ba699-ed41-4cdd-9429-9b99269ed57d


- 스테이션 현황 대시보드
    - 스테이션 내 배터리 잔량 평균 퍼센트 색으로 표시
    - 스테이션 배터리 보관율(0~1) 사이즈로 표시
    - 스테이션 정보 툴팁
https://github.com/SKYoooon/SNU_Fintech/assets/138483304/3cbda9cf-64ca-4c0a-a891-0e28836b2018

### - 결과 및 결론
- 기존 수요를 고려하지 않고 배터리가 분배되어있었음<br/>
→ 배터리 재배치를 통해 관리 지표였던 배터리 1개당 스쿠터 개수가 모든 시간과 격자 전체적으로 낮아짐<br/>
그리드 종합 관리 지표 평균 1.924 → 1.346 (30% 감소)<br/>
그리드 종합 관리 지표 최대값 48 → 16.5 (34% 감소)<br/>
그리드 종합 관리 지표 10 이상 그리드 1054 → 15<br/>
- 지속적으로 전기 스쿠터의 개수가 늘어날 것이기에 스테이션의 재배치 또는 추가 설치를 위해 추가 분석이 필요함
- 격자 내 스쿠터 개수, 스테이션 내 배터리 잔량, 교체 횟수 등을 학습시켜, 추후에 스쿠터의 개수나 배터리 개수가 변동 되어도 수요 예측 및 시뮬레이션이 가능하다 판단됨
- 격자만이 아니라 행정구역 별 특성을 추가적으로 학습하는 방안도 고려