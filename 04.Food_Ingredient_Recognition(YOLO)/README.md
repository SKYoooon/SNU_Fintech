# ▶ 식재료 이미지 인식을 통한 레시피 추천 모델 제작 <img src="https://img.shields.io/badge/Team_Project-000000"/>

### - 과제
- 딥러닝 모델을 활용해 상업적인 아이템 제작(자연어 제외)

### - 과제 목적
- 식재료 인식하여 부족한 식재료를 알려주는 요리 도우미 제작

### - 기대 효과
- 요리의 진입장벽을 낮추어 줄 수 있어, 요리에 관심있는 고객이 구매 가능

### - 사용 툴
- Python(YOLO v5~v8)

### - 역할
- 조원 4명
  - 데이터 확보, 도우미 코드 작성, PPT 제작, 시연 발표

### - 데이터
- <img width="900" alt="스크린샷 2024-01-09 135318" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/0e4ba350-f996-47da-9a19-ab2c52bad2d0">
- <img width="901" alt="스크린샷 2024-01-09 135324" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/c91793ea-6121-44ee-bf9a-9ebef31dd253">

### - 요리 도우미의 작동 방식
- YOLO 모델 학습 → 각 모델별 best.pt 추출 및 실행→ 실시간 사물 인식 → 이미지내 객체 저장 → 부족한 재료 파악 후 표시


### - 결과 및 결론
- 전체비교 결과
  - yolo v5,v8의 높은 인식률
  - v6 인식률이 높으나 오답률이 높음
  - v7의 낮은 인식률
      <img width="900" alt="스크린샷 2024-01-09 135540" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/a22a4d2e-223b-41e6-a17b-b4bc333b3d4a">

  - 인식률 높은 v5, v8 추가 학습
      - yolo v5의 경우 더 큰 모델인 v5m로 변경
      - 데이터 증강 학습 및 에포크 증가
          - 데이터 불균형으로 인해 학습량이 적은 데이터의 정답률이 낮음
          - 에포크 증가로 평가 지표가 좋아지는 모습→ 에포크 증가하여 학습시 좋은 결과가 예상됨(추가 결제 필요로 불가)![Untitled2](https://github.com/SKYoooon/SNU_Fintech/assets/138483304/19ad0511-e18d-4e03-beb7-fa591fa06658)![Untitled3](https://github.com/SKYoooon/SNU_Fintech/assets/138483304/32658209-0b61-4cd3-9b79-7d4352352cb6)


### - YOLO v8 실시간 시연 및 어플리케이션
<img width="898" alt="스크린샷 2024-01-09 135601" src="https://github.com/SKYoooon/SNU_Fintech/assets/138483304/06f230d4-4e1a-44b8-ae03-525ea6a84ea7">
- 추가 활용 가능 어플리케이션 아이디어
    - 부족한 식재료 확인하여 마트 장바구니 추가
    - 냉장고 내부 식재료 확인
    - 식재료 기반 레시피 추천