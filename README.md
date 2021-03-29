# each_day_cross_validation
A method of cross-validation to modelling object what change condition each day.

実験日ごとに目的変数が増減し、サンプリング数が少ないデータをクロスバリデーションすると、
testとtrainデータ目的変数の分布が偏ることがあります。
それを防ぐために、測定日ごとにデータを分割する関数を作りました。

## Usage
```
import ed_cross-validation

X_train, X_test, y_train, y_test = ed_cross_validation(X,Y,day_sample,n_splits=5)

#day_sampleは一日あたりのサンプル数
#n_splitsはサンプル数を何分割するか
#X,Yはnp.arrayで入力する(scikit-learnと同じ)

model = XXXRegression()
model.fit(X_train, y_train)
pred_train = model.predict(X_train)
pred_test = model.predict(X_test)

```
