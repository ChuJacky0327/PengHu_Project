'''
當出現TypeError: ufunc 'isnan' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
這個錯誤
我把
File "C:/Users/88696/Anaconda3/lib/site-packages/sklearn/utils/_encode.py", line 261, in _check_unknown
if np.isnan(known_values).any():#這段住解掉了
'''
from xgboost import XGBClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from random import randrange
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import accuracy_score
from matplotlib import pyplot

'''#############景點推薦####################'''
def XGboost_push(test):
    le = LabelEncoder()
    tree_deep = 100 #可理解成epoch
    learning_rate = 0.3
    
    Data = pd.read_csv('penghu_orignal2.csv',encoding='utf-8-sig')
    df_data = pd.DataFrame(data= np.c_ [Data['gender'], Data['age'], Data['設置點']],
                           columns= ['gender','age','label'])
    #轉換文字要做one-hot encode前要先做label encode
    
    X = df_data.drop(labels=['label'],axis=1).values # 移除label並取得剩下欄位資料    
    Y = df_data['label'].values    
    
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)# stratify=Y  -> 依据标签y，按原数据y中各类比例，分配给train和test，使得train和test中各类数据的比例与原数据集一样
    Y_train = le.fit_transform(Y_train) #由於字串無法做訓練，所以進行Label encoding編碼
    print('encode class:' +str( le.classes_.shape))
    #print(X_train[0])
    
    
    xgboostModel = XGBClassifier(n_estimators=tree_deep, learning_rate= learning_rate)
    xgboostModel.fit(X_train, Y_train)
    #xgboostModel.save_model('PHtest.model')

    predicted = xgboostModel.predict([test])
    print('訓練集Accuracy: %.2f%% ' % (xgboostModel.score(X_train,Y_train) * 100.0))
    #predicted = xgboostModel.predict([X_test])
    #print('訓練集: ',xgboostModel.score(X_train,Y_train))
    #print('測試集: ',xgboostModel.score(X_test,Y_test))
    print(predicted)
    result = le.inverse_transform(predicted)
    #print(type(result))
    print(result[0])
    return result[0]



def XGboost_newpush(arr,gender,age):    
    le = LabelEncoder()
    labelencoder = LabelEncoder()
    tree_deep = 100 #可理解成epoch
    learning_rate = 0.3
    
    Data = pd.read_csv('penghu_orignal2.csv',encoding='utf-8-sig')
    df_data = pd.DataFrame(data= np.c_ [Data['weather'], Data['gender'], Data['age'], Data['設置點']],
                           columns= ['weather','gender','age','label'])
    
    df_data['weather'] = labelencoder.fit_transform(df_data['weather'])#轉換文字要做one-hot encode前要先做label encode

    X = df_data.drop(labels=['label'],axis=1).values # 移除label並取得剩下欄位資料

    onehotencoder = OneHotEncoder(categories = 'auto')
    X=onehotencoder.fit_transform(X).toarray()    
    #print(list(X.columns))
    #R = pd.DataFrame(X)
    #print(R)
    Y = df_data['label'].values    
    
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)# stratify=Y  -> 依据标签y，按原数据y中各类比例，分配给train和test，使得train和test中各类数据的比例与原数据集一样
    Y_train = le.fit_transform(Y_train) #由於字串無法做訓練，所以進行Label encoding編碼

    arr_labelencode = labelencoder.transform(arr) #用同一個labelencoder能transform到一樣的編碼
    Value_arr = np.array([arr_labelencode[0],gender,age])
    print(Value_arr)
    final=onehotencoder.transform([Value_arr]).toarray()#用同一個onehotencoder能transform到一樣的編碼
    
    xgboostModel = XGBClassifier(n_estimators=tree_deep, learning_rate= learning_rate)
    xgboostModel.fit(X_train, Y_train)
    #xgboostModel.save_model('PHtest.model')
    predicted = xgboostModel.predict([final[0]])
    print('訓練集Accuracy: %.2f%% ' % (xgboostModel.score(X_train,Y_train) * 100.0))
    #predicted = xgboostModel.predict([X_test])
    result = le.inverse_transform(predicted)
    #importance = xgboostModel.feature_importances_
    #print(importance)
    print(result[0])
    
    return result[0]

def XGboost_newpushadd(arr,gender,age,tidal,temperature):    
    le = LabelEncoder()
    labelencoder = LabelEncoder()
    tree_deep = 100 #可理解成epoch
    learning_rate = 0.3
    
    Data = pd.read_csv('penghu_orignal2.csv',encoding='utf-8-sig')
    df_data = pd.DataFrame(data= np.c_ [Data['weather'], Data['gender'], Data['age'] ,Data['tidal'],Data['temperature'],Data['設置點']],
                           columns= ['weather','gender','age','tidal','temperature','label'])
    
    df_data['weather'] = labelencoder.fit_transform(df_data['weather'])#轉換文字要做one-hot encode前要先做label encode

    X = df_data.drop(labels=['label'],axis=1).values # 移除label並取得剩下欄位資料

    onehotencoder = OneHotEncoder(categories = 'auto')
    X=onehotencoder.fit_transform(X).toarray()    
    #print(list(X.columns))
    #R = pd.DataFrame(X)
    #print(R)
    Y = df_data['label'].values    
    
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)# stratify=Y  -> 依据标签y，按原数据y中各类比例，分配给train和test，使得train和test中各类数据的比例与原数据集一样
    Y_train = le.fit_transform(Y_train) #由於字串無法做訓練，所以進行Label encoding編碼

    arr_labelencode = labelencoder.transform(arr) #用同一個labelencoder能transform到一樣的編碼
    Value_arr = np.array([arr_labelencode[0],gender,age,tidal,temperature])
    print(Value_arr)
    final=onehotencoder.transform([Value_arr]).toarray()#用同一個onehotencoder能transform到一樣的編碼
    
    xgboostModel = XGBClassifier(n_estimators=tree_deep, learning_rate= learning_rate)
    xgboostModel.fit(X_train, Y_train)
    #xgboostModel.save_model('PHtest.model')
    predicted = xgboostModel.predict([final[0]])
    print('訓練集Accuracy: %.2f%% ' % (xgboostModel.score(X_train,Y_train) * 100.0))
    #predicted = xgboostModel.predict([X_test])
    result = le.inverse_transform(predicted)
    #importance = xgboostModel.feature_importances_
    #print(importance)
    print(result[0])
    
    return result[0]


    
def RandomForest_push(arr,gender,age):
    le = LabelEncoder()
    labelencoder = LabelEncoder()
    tree_deep = 100 #可理解成epoch
    Data = pd.read_csv('penghu_orignal2.csv',encoding='utf-8-sig')
    df_data = pd.DataFrame(data= np.c_ [Data['weather'], Data['gender'], Data['age'], Data['設置點']],
                           columns= ['weather','gender','age','label'])
    
    df_data['weather'] = labelencoder.fit_transform(df_data['weather'])#轉換文字要做one-hot encode前要先做label encode

    X = df_data.drop(labels=['label'],axis=1).values # 移除label並取得剩下欄位資料

    onehotencoder = OneHotEncoder(categories = 'auto')
    X=onehotencoder.fit_transform(X).toarray()    
    
    Y = df_data['label'].values    
    
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)# stratify=Y  -> 依据标签y，按原数据y中各类比例，分配给train和test，使得train和test中各类数据的比例与原数据集一样
    Y_train = le.fit_transform(Y_train) #由於字串無法做訓練，所以進行Label encoding編碼
    
    #print('encode class:' +str( le.classes_.shape))
    #print(X_train[0])

    arr_labelencode = labelencoder.transform(arr) #用同一個labelencoder能transform到一樣的編碼
    Value_arr = np.array([arr_labelencode[0],gender,age])
    print(Value_arr)
    final=onehotencoder.transform([Value_arr]).toarray()#用同一個onehotencoder能transform到一樣的編碼
    #print(final[0])
    classifier = RandomForestClassifier(n_estimators = tree_deep, criterion = 'entropy', random_state = 0)
    classifier.fit(X_train,Y_train)
    predicted = classifier.predict([final[0]])
    print('訓練集Accuracy: %.2f%% ' % (classifier.score(X_train,Y_train) * 100.0))
    result = le.inverse_transform(predicted)
    print(result[0])
    
    return result[0]


def stacking_push():
    le = LabelEncoder()
    labelencoder = LabelEncoder()
    Data = pd.read_csv('penghu_orignal2.csv',encoding='utf-8-sig')
    df_data = pd.DataFrame(data= np.c_ [Data['weather'], Data['gender'], Data['age'], Data['設置點']],
                           columns= ['weather','gender','age','label'])
    
    df_data['weather'] = labelencoder.fit_transform(df_data['weather'])#轉換文字要做one-hot encode前要先做label encode

    X = df_data.drop(labels=['label'],axis=1).values # 移除label並取得剩下欄位資料

    onehotencoder = OneHotEncoder(categories = 'auto')
    X=onehotencoder.fit_transform(X).toarray()    
    
    Y = df_data['label'].values    
    
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)# stratify=Y  -> 依据标签y，按原数据y中各类比例，分配给train和test，使得train和test中各类数据的比例与原数据集一样
    Y_train = le.fit_transform(Y_train) #由於字串無法做訓練，所以進行Label encoding編碼
    
    estimators = [
    ('rf', RandomForestRegressor(random_state = 42)),
    ('svr', svm.SVR()),
    ('knn', KNeighborsRegressor()),
    ('dt', DecisionTreeRegressor(random_state = 42))
    ]
    clf = StackingRegressor(
        estimators=estimators, final_estimator= MLPRegressor(activation = "relu", alpha = 0.1, hidden_layer_sizes = (8,8),
                                learning_rate = "constant", max_iter = 2000, random_state = 1000)
    )
    clf.fit(X_train, Y_train)
    
    print("訓練集 Score: ",clf.score(X_train,Y_train))

'''#############景點推薦####################'''
    

'''#############行程規劃####################'''
def XGboost_plan(plan_data,gender,age):
    le = LabelEncoder()
    tree_deep = 100 #可理解成epoch
    learning_rate = 0.3
    
    Data = plan_data
    df_data = pd.DataFrame(data= np.c_ [Data['gender'], Data['age'], Data['UserID/MemID']],
                           columns= ['gender','age','label'])
    #轉換文字要做one-hot encode前要先做label encode
    
    X_train = df_data.drop(labels=['label'],axis=1).values # 移除label並取得剩下欄位資料    
    Y_train = df_data['label'].values    
    print(X_train[0])
    print(Y_train[0])
    
    
    #X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)# stratify=Y  -> 依据标签y，按原数据y中各类比例，分配给train和test，使得train和test中各类数据的比例与原数据集一样
    Y_train = le.fit_transform(Y_train) #由於字串無法做訓練，所以進行Label encoding編碼
    print('encode class:' +str( le.classes_.shape))
    #print(X_train[0])
    
    
    xgboostModel = XGBClassifier(n_estimators=tree_deep, learning_rate= learning_rate)
    xgboostModel.fit(X_train, Y_train)
    #xgboostModel.save_model('PHtest.model')
    test = np.array([gender,age])
    predicted = xgboostModel.predict([test])
    print('訓練集Accuracy: %.2f%% ' % (xgboostModel.score(X_train,Y_train) * 100.0))
    #predicted = xgboostModel.predict([X_test])
    #print('訓練集: ',xgboostModel.score(X_train,Y_train))
    #print('測試集: ',xgboostModel.score(X_test,Y_test))
    print(predicted)
    result = le.inverse_transform(predicted)
    #print(type(result))
    print(result[0])
    return result[0] #回傳關聯性最高的UUID
    

'''#############行程規劃####################'''

'''#############畫圖####################'''
def XGboost_plot():
    le = LabelEncoder()
    labelencoder = LabelEncoder()
    tree_deep = 2000  #可理解成epoch
    learning_rate = 0.1
    
    Data = pd.read_csv('penghu_orignal2.csv',encoding='utf-8-sig')
    df_data = pd.DataFrame(data= np.c_ [Data['weather'], Data['gender'], Data['age'] ,Data['tidal'],Data['temperature'],Data['設置點']],
                           columns= ['weather','gender','age','tidal','temperature','label'])
    
    df_data['weather'] = labelencoder.fit_transform(df_data['weather'])#轉換文字要做one-hot encode前要先做label encode

    X = df_data.drop(labels=['label'],axis=1).values # 移除label並取得剩下欄位資料

    onehotencoder = OneHotEncoder(categories = 'auto')
    X=onehotencoder.fit_transform(X).toarray()    
    #print(list(X.columns))
    #R = pd.DataFrame(X)
    #print(R)
    Y = df_data['label'].values    
    #Y = le.fit_transform(Y)

    '''
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)# stratify=Y  -> 依据标签y，按原数据y中各类比例，分配给train和test，使得train和test中各类数据的比例与原数据集一样

    xgboostModel = XGBClassifier(n_estimators=tree_deep, learning_rate= learning_rate,max_depth = 10)
    Y_train = le.fit_transform(Y_train)
    Y_test = le.fit_transform(Y_test)

    
    evalset = [(X_train, Y_train),(X_test, Y_test)]
    xgboostModel.fit(X_train, Y_train,eval_metric='mlogloss', eval_set = evalset)
    print('訓練集Accuracy: %.2f%% ' % (xgboostModel.score(X_train,Y_train) * 100.0))    
    predicted = xgboostModel.predict(X_test)
    
    score = accuracy_score(Y_test,predicted)
    print('Accuracy : %.3f' % score)
    '''
    

    xgboostModel = XGBClassifier(n_estimators=tree_deep, learning_rate= learning_rate,max_depth = 10)
    Y = le.fit_transform(Y)
    
    evalset = [(X, Y)]
    xgboostModel.fit(X, Y,eval_metric='mlogloss', eval_set = evalset)
    print('訓練集Accuracy: %.2f%% ' % (xgboostModel.score(X,Y) * 100.0)) 
    
    results = xgboostModel.evals_result()
    pyplot.plot(results['validation_0']['mlogloss'], label = 'train')
    #pyplot.plot(results['validation_1']['mlogloss'], label = 'test')
    pyplot.legend()
    pyplot.show()

'''#############畫圖####################'''
#XGboost_plot()
























