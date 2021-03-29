import random
import numpy as np


def ed_cross_validation(X,Y,day_sample,n_splits=5):
    day = len(Y)//day_sample
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    if day_sample/n_splits<1:
        raise ValueError("error!")
    for i in range(day):
        l = list(range(day_sample))
        lr = random.sample(l, len(l))
        for j in range(day_sample//n_splits):
            x_test.append(X[day_sample*i+lr[0]])
            y_test.append(Y[day_sample*i+lr[0]])
            lr=lr[1:]
        for m in lr:
            x_train.append(X[day_sample*i+m])
            y_train.append(Y[day_sample*i+m])
    return np.array(x_train), np.array(x_test), np.array(y_train).flatten(), np.array(y_test).flatten()