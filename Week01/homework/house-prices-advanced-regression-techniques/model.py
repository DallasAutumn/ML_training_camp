import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Binarizer, OneHotEncoder

from xgboost import XGBRegressor

# load data
data_train = pd.read_csv('datasets/train.csv')
data_test = pd.read_csv('datasets/test.csv')
# cols_with_missing = [col for col in original_data.columns
#                      if original_data[col].isnull().any()]
# data_train = data_train.drop(cols_with_missing, axis=1)
# data_test = data_test.drop(cols_with_missing, axis=1)
target = 'SalePrice'
y = data_train[target]
data_train.pop('SalePrice')
data = pd.concat([data_train, data_test])

# set features
features = list(data.columns)
num_feats = [col for col in features if data_train[col].dtype in [
    np.int64, np.float64]]
text_feats = [col for col in features if col not in num_feats]

# 合并之后进行统一编码，防止index冲突
data = pd.get_dummies(data, columns=text_feats,
                      prefix=text_feats).dropna(axis=1)
features = list(data.columns)
features.remove('Id')
train = data.iloc[:1460]
test = data.iloc[1460:]

# train the model
train['SalePrice'] = y
x = train[features]
train_x, val_x, train_y, val_y = train_test_split(
    x.values, y.values, test_size=0.25)

# model = XGBRegressor(n_estimators=30000, learning_rate=0.01)
model = LinearRegression(normalize=True)
model.fit(train_x, train_y)

# predict
test_x = test[features]
test_y = pd.Series(model.predict(test_x.values), dtype=np.float64)

output = pd.DataFrame({'Id': data_test.Id, 'SalePrice': test_y})
output.to_csv('submission.csv')
