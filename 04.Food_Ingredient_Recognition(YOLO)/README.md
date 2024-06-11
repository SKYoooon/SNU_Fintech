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
- ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/79ef0434-a6be-4c14-8f63-1c22c4dca40f/Untitled.png)
- ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/b29dfed5-f42f-472f-ad75-01ef45b30540/Untitled.png)

### - 요리 도우미의 작동 방식
- YOLO 모델 학습 → 각 모델별 best.pt 추출 및 실행→ 실시간 사물 인식 → 이미지내 객체 저장 → 부족한 재료 파악 후 표시


### - 결과 및 결론
- 전체비교 결과
  - yolo v5,v8의 높은 인식률
  - v6 인식률이 높으나 오답률이 높음
  - v7의 낮은 인식률
      ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/5acf3c18-5bd2-48c7-a885-ddd4f77b5bf0/Untitled.png)

  - 인식률 높은 v5, v8 추가 학습
      - yolo v5의 경우 더 큰 모델인 v5m로 변경
      - 데이터 증강 학습 및 에포크 증가
          - 데이터 불균형으로 인해 학습량이 적은 데이터의 정답률이 낮음
          - 에포크 증가로 평가 지표가 좋아지는 모습→ 에포크 증가하여 학습시 좋은 결과가 예상됨(추가 결제 필요로 불가)![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/73549eb8-70d9-4aac-b3c1-bd70c6bc3e19/Untitled.png)![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/8e318186-fe1d-47af-aa0f-82bcbe39240c/Untitled.png)

### - YOLO v8 실시간 시연 및 어플리케이션
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/53a095e4-4525-4cc6-b517-0d27fae08348/Untitled.png)
- 추가 활용 가능 어플리케이션 아이디어
    - 부족한 식재료 확인하여 마트 장바구니 추가
    - 냉장고 내부 식재료 확인
    - 식재료 기반 레시피 추천