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
- 이탈율 16.1%의 불균형 데이터![Untitled](https://github.com/SKYoooon/SNU_Fintech/assets/138483304/da3772b7-fef7-473a-a70d-a9b1c7f22fbc)

### - 분석
- 여성, 높은 교육 수준, 낮은 소득 수준, 가장 높은 카드 등급에서 상대적으로 높은 이탈율
- 상관관계가 높은 대출한도와 신용한도 중 신용 한도만 사용![Untitled1](https://github.com/SKYoooon/SNU_Fintech/assets/138483304/d3bcde18-688f-4fab-a601-0533959c7bbb)
- 범위가 큰 금액 관련 이상치 처리, 최대값에 붙여보기도 하고 진행했지만 큰차이가 없었으며 새로운 평가 지표 투입으로 인해 이상치 처리 없이 진행
- 금액에 이상치 존재하여 스탠다드 스케일링 적용
- 데이터 편향 감소 및 오버피팅 방지 위해 Stratify적용하여 트레이닝/검증/테스트 세트 진행
- SMOTE도 진행해 보았지만 기존 방식의  더 좋은 결과
- 신규 평가 지표 : Revenue_Risk<img width="767" alt="스크린샷 2024-01-09 134226" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/e6ab4f12-9371-418f-bc1a-c49d88d689dc">


### - 결과 및 결론
- 이전 기수의 결과<img width="765" alt="스크린샷 2024-01-09 134027" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/64df25cf-7460-400d-a2f7-1d3a17b98969">
- 좋은 결과가 나온 LGBM을 추가적인 하이퍼 파라미터 조정<img width="767" alt="스크린샷 2024-01-09 134356" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/724c843a-7acd-4f76-b237-926649523b67">
- 가장 높은 단계인 플레티넘의 높은 이탈로 보아 차별화된 혜택 부족하여 추가 혜택 필요
- 이탈이 의심되는 고객에게 추가적인 마케팅을 통한 고객 유지 필요
- **LGBM 재현율 93.3%/정확도 97.9% 달성, 이전 기수 대비 1.7%p/4.2%p 상승**