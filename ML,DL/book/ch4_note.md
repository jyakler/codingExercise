# 데이터 전처리

1. drop


2. interpolation


3. scale
  
  MinMaxScaler
  
  normalization(StandardScaler) - 이상치에 덜민감 
  
  RobustScaler - 이상치 포함된 작은 데이터셋일경우 유리, 과대적합이 되기 쉬운 경우에도 유리
  
  
  ## 과대적합 해결법
  
  1) 더 많은 데이터
  2) 규제를 통해 복잡도 제한
  3) 파라미터 개수가 적은 간단한 모델 선택
  4) 차원축소


L1 Regularization - 모델복잡도 줄이는 방법

  - sparse vector를 만듬
  - 대부분 특성 가중치가 0
  - 훈련샘플보다 관련없는 특성이 많은경우 유리



logisticRegression solver 중 lbfgs, newton-cg, sag는 L2만 지원   
saga, liblinear는 L1,L2지원



## 차원축소

특성선택 

순차 특성 선택

  - 규제 사용하지 않는 알고리즘때 유리
  - greedy algorithm방식
  - 순차 후진 선택(sequential backward selection) - 전통적 알고리즘
