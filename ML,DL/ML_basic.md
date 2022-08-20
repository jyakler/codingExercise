# 머신러닝 종류
- 지도학습  
    레이블된 데이터  
    직접 피드백  
    출력 및 미래 예측  
- 비지도학습  
    레이블 없음  
    피드백 없음    
    데이터에서 숨겨진 구조 찾기  
- 강화 학습  
    결정과정  
    보상시스템  
    연속된 행동에서 학습  

## 용어



sklearn

    sklearn.model_selection 
        - train_test_split : train, test용 데이터 나누기
    sklearn.metrics : 모델 테스트
        - mean_absolute_error : 평균차이 절대값
    sklearn.impute : na값 대체
        - SimpleImputer : strategy에따라 간단하게 na값 교체 (default:mean)
    sklearn.preprocessing: 전처리
        - OrdinalEncoder
        - OneHotEncoder
    
    sklearn.tree - DecisionTreeRegressor - 결정트리모델
    sklearn.ensemble - RandomForestRegressor
    

### overfitting

모델이 train데이터에 거이 완벽하게 일치하지만 validation이나 새로운 데이터에는 잘 맞지않음

### underfitting

모델이 중요한 차별점(distinction)을 구분하지 못하여서 train데이터도 예측에 실패

# 모델 향상하기 위해서 어떻게

전처리 방식에따라 성능이 많이 갈림 -> 매우 중요



## 모델

- RandomForest

앙상블 기법: 여러개의 모델들을 돌려 더나은 결과를 도출하는 기법( voting, bagging, boosting)


## categorical variable

1. drop
2. ordinal encoding
3. one-hot encoding
```
전처리시 A.select_dtypes(exclude=['object']) 로 category 칼럼 제외가능
```
