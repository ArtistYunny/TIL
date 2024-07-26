# <aside>
# 📌 **IQR의 계산 방법**

# 1. 데이터 셋을 **크기 순으로 정렬**합니다.
# 2. **중간값(2사분위수)을 찾아** 데이터를 하위 그룹과 상위 그룹 두 부분으로 나눕니다.
# 3. 하위 그룹(하위 50% 데이터)의 중간값을 찾아 **1사분위수(Q1, 25%)를 결정**합니다.
# 4. 상위 그룹(상위 50% 데이터)의 중간값을 찾아 **3사분위수(Q3, 75%)를 결정**합니다.
# 5. IQR은 **3사분위수(Q3)에서 1사분위수(Q1)를 뺀 값으로 계산**합니다.
# </aside>

iqr = [55, 60, 65, 70, 75, 80, 85, 90, 95]

iqr.sort()