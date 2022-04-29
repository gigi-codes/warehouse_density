# ---------------------------
# module has two functions
# ---------------------------
# 1: G's Random Forest Regressor
# gs_rf(X, y, t_size, m_d)
# 	X, y
# 	t_size : train set size
#	m_d: max_leaf_depth
# takes FOUR (4) args: clean, numeric, dummified (X, y) and train_size (0-1), and leaf depth 
# ---------------------------
# 2: G's SVR (?)
# gs_svr(X, y, t_size, m_d)
# 	X, y
# 	t_size : train set size
#	m_d: max_leaf_depth
# takes FOUR (3) args: clean, numeric, dummified (X, y) and train_size (0-1)
# runs grid search over fixed values in function
# ---------------------------

# checks LINE assumptions, returns plots 


##### IMPORTS #####  --- --- --- --- --- --- --- --- --- --- --- ---
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('gstyle.mplstyle') 

from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn import metrics        					

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
	
##### --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
##### RF FUNCTION DEF #####   --- --- --- --- --- --- --- --- --- --- ---
##### --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
def gs_rf(X, y, t_size, m_d):
    X = X
    y = y 
	# pre-processing --- --- ---
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, train_size = t_size)
    # scale
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    
##### S E A R C H   --- --- --- --- --- --- --- --- --- --- --- --- --- ---
    rf = RandomForestRegressor()

    #(['bootstrap', 'ccp_alpha', 'criterion', 'max_depth', 'max_features', 
    # 'max_leaf_nodes', 'max_samples', 'min_impurity_decrease', 'min_impurity_split', 
    # 'min_samples_leaf', 'min_samples_split', 'min_weight_fraction_leaf', 'n_estimators', 
    # 'n_jobs', 'oob_score', 'random_state', 'verbose', 'warm_start'])
    
#     params  =  {
#     	'n_estimators': [100,150], 
#     	'max_depth': [2, 5, 10],
#         'max_features': [0, 10]
#         }

    # Instantiate GridSearchCV.
    gs = GridSearchCV(rf, params, cv = 3)
    
    # FIT gs
    gs.fit(X_train, y_train)
#     results = sorted(gs.best_estimator_.feature_importances_)
    results = gs.best_estimator_.feature_importances_
# 	# making predictions to get residuals  
# 	pred = gs.predict(X_test)
	#plot feature importances
    pd.Series(results, X.columns).sort_values(ascending = false).plot(kind = 'barh');
    
#     f_list = (results)
#     keys = list(feature_important.keys())
# values = list(feature_important.values())
# 
# data = pd.DataFrame(data=values, index=keys, columns=["score"]).sort_values(by = "score", ascending=False)
# data.nlargest(40, columns="score").plot(kind='barh', figsize = (20,10)) ## plot top 40 features
    
    return(results)
# ##### --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# 			
# # 		RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
# #                        max_depth=None, max_features='auto', max_leaf_nodes=None,
# #                        min_impurity_decrease=0.0, min_impurity_split=None,
# #                        min_samples_leaf=1, min_samples_split=2,
# #                        min_weight_fraction_leaf=0.0, n_estimators=10,
# #                        n_jobs=None, oob_score=False, random_state=0, verbose=0,
# #                        warm_start=False)
# 
# 	# Features Importances
# 	gs.rf_coef_df = pd.DataFrame({
#         'Feature' : X.columns,
#         'Importances' : rf.feature_importances_})
# 		
# 	# making predictions to get residuals  
	pred = gs.predict(X_test)
# 	
# 	# errors 
# 	rss = round((residuals **2).sum(), 4)									# rss = sse 
# 	max_e = round(metrics.max_error(y, predictions)  , 4)					# max error
# 	rmse = round(np.sqrt(metrics.mean_squared_error(y, predictions)), 4)    # root mean squared error
# 	mae = round(metrics.mean_squared_error(y, predictions),4)               # mean absolute error
# 	mse = round(metrics.mean_squared_error(y, predictions),4)               # mean squared error  
# 	r2 = round(metrics.r2_score(y, predictions), 4)                        	# coefficient of determination
# 	r2xval = round(cross_val_score(rf, X, y).mean(), 4)					# X-val score
# 	
# 	my_metrics_s = ['r2', 'rss', 'max_e', 'rmse', 'mae', 'mse', 'r2xval']
# 	my_metrics = [r2, rss, max_e, rmse, mae, mse, r2xval ]
# 
# 	lr_df = pd.DataFrame({
# 	'Metric':	my_metrics_s,
# 	'Value':	my_metrics})
	
# 	return(rf.base_estimator_, rf_coef_df, lr_df)