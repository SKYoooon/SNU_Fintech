# ▶ P2P 대출 업체 부도 고객 예측 모델 제작 <img src="https://img.shields.io/badge/Team_Project-000000"/>

### - 과제
- P2P 대출 업체 고객 데이터로부터 부도 예측 모델 제작

### - 과제 목적
- P2P 대출 업체 고객 부도 예측하여 대출 여부 판단

### - 기대 효과
- 부도 여부 예측을 통한 손해 최소화

### - 사용 툴
- Python(Pandas,Numpy,Matplotlib, Seaborn, Scikitlearn)

### - 역할
- 조원 5명
  - 데이터 전처리, 코드 작성, 시각화

### - 데이터
- 87만명의 데이터로 334개의 변수(55종류)로 이루어짐
- 부도 여부 16.2%의 불균형 데이터
- 모델 학습을 위해 대출 승인 시점에 조회 가능한 변수만 선정 - 24종류
- 0 비율이 매우 높은 변수(0.999이상)  8개 제거
- 금액적으로 압도적으로 높은 두개의 데이터 제거
- 지속적인 상환 중 부도가 나는 경우가 있어서, 이를 파악하기 위해 고객으로 부터 받은 금액과 대출금액을 비교한 컬럼 생성 → 이익을 발생시키기에 대출 해주고자함

### - 모델링
- 이익을 주지만 대출이 거절된 고객(FP)은 18%의 수익률을 놓쳤다고 판단하여 0.18을 곱해주고 손해를 내지만 대출 승인된 고객(FN)은 44%의 손해를 입힌다고 판단하여 0.44를 곱하고 해당 합이 가장 낮을 때의 모델을 선정하고자함
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/f0087878-7631-47cc-aa56-a0b3e27302fa/Untitled.png)
![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/53bf8a43-b3f3-45a8-b457-9757213e3a08/Untitled.png)
- 6:2:2= Train:Valid:Test세트
- logistic regression과 random forest 실행

### - 결과
- Random Forest의 가장 낮은 리스크 때 가장 높은 수익률![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/0351af66-a129-4578-8eb4-cbffed50bd7f/Untitled.png)
- 평가를 위한 기존 제공되지 않던 데이터세트 적용 시 더 높아진 모습![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/2efa88c5-ab86-49c6-81d8-0248d6aa7b5d/12a2eca1-abd1-4e84-afb1-ff6010b282e8/Untitled.png)

### - 결론
- 이미 P2P 대출업체에서 심사 후 대출은 진행한 고객들의 데이터이기에 모두에게 대출을 승인해도 9.08%의 수익률이 얻어짐 → 그리하여 수익률 상승에 큰 어려움이 존재
- 총 투자금이 119억 달러이기에 0.2%p 상승도 2.4억달러 가량으로 큰 금액
- **RandomForest 수익률  9.28% 달성,  기존 대비 2%p 상승**

### - 추가 분석
- 수익을 통해 문턱값 설정해보았지만 너무 많은 인원에게 대출 승인되어 수익률이 낮아짐
- 수익률을 통해 문턱값 설정해보았지만 수익률은 높지만 낮은 수익금을 얻었다
