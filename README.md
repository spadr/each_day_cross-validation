# each_day_cross-validation
A method of cross-validation to modelling object what change condition each day.

実験日ごとに目的変数が増減し、サンプリング数が少ないデータをクロスバリデーションすると、
testとtrainデータ目的変数の分布が偏ることがあります。
それを防ぐために、測定日ごとにデータを分割する関数を作りました。

## Usage
import ed_cross-validation<br>
<br>
X_train, X_test, y_train, y_test = ed_cross-validation(X,Y,day_sample,n_splits=5)<br>
model = XXXRegression()<br>
model.fit(X_train, y_train)<br>
pred_train = model.predict(X_train)<br>
pred_test = model.predict(X_test)<br>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br>
