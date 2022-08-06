# SIFFER 물성 예측 AI

## 전처리

- 파일명 : preprocess.py
- 역할 : root에 있는 clothes.csv파일을 output.csv파일로 만들어줍니다.
- 필요한 column만 남겨두며, 분류 모델로 작업할때를 위해 thickOut, weightOut이라는 칼럼을 추가해, 1부터 7까지 수치를 집어넣습니다.

## 분류모델

- 파일명 : classification/main.py
- 역할 : 전처리된 데이터 output.csv파일을 가지고 물성 데이터를 예측해보는 분류 모델입니다.
- 1부터 7까지의 수준으로 분류했기 떄문에, 길이가 7인 배열로 y data를 수정하는 로직이 있습니다.

```python
example = [0,0,0,1,0,0,0] # 4
```

## 회귀모델

- 파일명 : classification/main.py
- 역할 : 전처리된 데이터 output.csv파일을 가지고 물성 데이터를 예측해보는 분류 모델입니다.
- 1부터 7까지의 수준으로 분류했기 떄문에, 길이가 7인 배열로 y data를 수정하는 로직이 있습니다.
