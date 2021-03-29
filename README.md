# each_day_cross-validation
A method of cross-validation to modelling object what change condition each day.

実験日ごとに目的変数が増減し、サンプリング数が少ないデータをクロスバリデーションすると、
testとtrainデータ目的変数の分布が偏ることがあります。
それを防ぐために、この関数を作りました。
