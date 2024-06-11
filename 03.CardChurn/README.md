# ▶ 카드 이탈 고객 예측 모델 제작 <img src="https://img.shields.io/badge/Team_Project-000000"/>

### - 과제
- 이전 기수의 프로젝트보다 개선된 모델 제작하기

### - 과제 목적
- 카드 이탈 고객 예상 모델 제작

### - 기대 효과
- 이탈 고객 예측하고 맞춤 마케팅을 통한 수익 극대화

### - 사용 툴
- Python(Pandas,Numpy,Matplotlib, Seaborn, Scikitlearn)

### - 역할
- 조원 4명
  - 기획, 데이터 전처리, 코드 작성, 발표

### - 데이터
- 만 여명 고객의 연령, 성별 등 21가지 항목으로 이루어진 데이터
- 이탈율 16.1%의 불균형 데이터![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/fff51551-22cd-4d62-a07a-a4d5f438ab48/Untitled.png)

### - 분석
- 여성, 높은 교육 수준, 낮은 소득 수준, 가장 높은 카드 등급에서 상대적으로 높은 이탈율
- 상관관계가 높은 대출한도와 신용한도 중 신용 한도만 사용![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/b2549ce9-4685-491c-b8e0-f8d2716bd717/Untitled.png)
- 범위가 큰 금액 관련 이상치 처리, 최대값에 붙여보기도 하고 진행했지만 큰차이가 없었으며 새로운 평가 지표 투입으로 인해 이상치 처리 없이 진행
- 금액에 이상치 존재하여 스탠다드 스케일링 적용
- 데이터 편향 감소 및 오버피팅 방지 위해 Stratify적용하여 트레이닝/검증/테스트 세트 진행
- SMOTE도 진행해 보았지만 기존 방식의  더 좋은 결과
- 신규 평가 지표 : Revenue_Risk![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/de27f95c-ad2c-4242-8eda-f724bed5a371/Untitled.png)


### - 결과 및 결론
- 이전 기수의 결과![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/0502787f-b063-4a42-8bc4-8d933cbf6f54/Untitled.png)
- 좋은 결과가 나온 LGBM을 추가적인 하이퍼 파라미터 조정![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/2d75cef9-d1f1-4be1-9001-0236722bb4a8/Untitled.png)
- 가장 높은 단계인 플레티넘의 높은 이탈로 보아 차별화된 혜택 부족하여 추가 혜택 필요
- 이탈이 의심되는 고객에게 추가적인 마케팅을 통한 고객 유지 필요
- **LGBM 재현율 93.3%/정확도 97.9% 달성, 이전 기수 대비 1.7%p/4.2%p 상승**