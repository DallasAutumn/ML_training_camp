# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import Binarizer, OneHotEncoder

# from xgboost import XGBRegressor

# # load data
# # data_train = pd.read_csv('datasets/train.csv')
# # data_test = pd.read_csv('datasets/test.csv')
# # data_train.dropna(axis=0)
# # data_test.dropna(axis=0)

# # # set features
# # target = 'SalePrice'
# # y = data_train[target]
# # features = list(data_train.columns)
# # features.remove('Id')
# # features.remove(target)

# # num_feats = [
# #     col for col in features if data_train[col].dtype in [np.int64, np.float64]]
# # text_feats = [col for col in features if col not in num_feats]

# data_train = pd.read_csv('datasets/train.csv')
# data_test = pd.read_csv('datasets/test.csv')

# print(data_test.Id)
# import os
# from tensorflow.python.client import device_lib
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "99"

# if __name__ == "__main__":
#     print(device_lib.list_local_devices())
import
