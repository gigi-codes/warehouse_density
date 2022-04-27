# SECOND, MODIFIED MODULE

# takes FOUR (4) args: clean, numeric, dummified (X, y) and train_size (0-1), and leaf depth 
# runs model, prints and returns 6 errors and feature importances

# checks LINE assumptions, returns plots 


##### IMPORTS #####  --- --- --- --- --- --- --- --- --- --- --- ---
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('gstyle.mplstyle') 

from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import metrics        					

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures

##### RF FUNCTION DEF #####  --- --- --- --- --- --- --- --- --- --- --- ---
def gs_rf(X, y, t_size, m_d):

	X = X
	y = y 

	# making model 
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, train_size = t_size)
	
	# scale
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)
	
	
	# fit
	rf = RandomForestRegressor(max_depth=m_d, random_state=0)
	rf.fit(X_train, y_train)
			
# 		RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
#                        max_depth=None, max_features='auto', max_leaf_nodes=None,
#                        min_impurity_decrease=0.0, min_impurity_split=None,
#                        min_samples_leaf=1, min_samples_split=2,
#                        min_weight_fraction_leaf=0.0, n_estimators=10,
#                        n_jobs=None, oob_score=False, random_state=0, verbose=0,
#                        warm_start=False)

	# Features Importances
	rf_coef_df = pd.DataFrame({
        'Feature' : X.columns,
        'Importances' : rf.feature_importances_})
		
	# making predictions to get residuals  
	predictions = rf.predict(X)
	residuals = y - predictions
	
	# errors 
	rss = round((residuals **2).sum(), 4)									# rss = sse 
	max_e = round(metrics.max_error(y, predictions)  , 4)					# max error
	rmse = round(np.sqrt(metrics.mean_squared_error(y, predictions)), 4)    # root mean squared error
	mae = round(metrics.mean_squared_error(y, predictions),4)               # mean absolute error
	mse = round(metrics.mean_squared_error(y, predictions),4)               # mean squared error  
	r2 = round(metrics.r2_score(y, predictions), 4)                        	# coefficient of determination
	r2xval = round(cross_val_score(rf, X, y).mean(), 4)					# X-val score
	
	my_metrics_s = ['r2', 'rss', 'max_e', 'rmse', 'mae', 'mse', 'r2xval']
	my_metrics = [r2, rss, max_e, rmse, mae, mse, r2xval ]

	lr_df = pd.DataFrame({
	'Metric':	my_metrics_s,
	'Value':	my_metrics})
	
	# plot feature importances
	pd.Series(rf.feature_importances_, X.columns).sort_values().plot(kind = 'barh');
	
	return(rf.base_estimator_, rf_coef_df, lr_df)
	

##### SVR FUNCTION #####  --- --- --- --- --- --- --- --- --- --- --- ---
def gs_svr(X, y, t_size):

	X = X
	y = y 

	# making model 
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, train_size = t_size)
	
	# scale
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)
	
	# fit	
# 	svr = SVR()
	svr = SVR(kernel="linear")
	svr.fit(X_train, y_train)
	
	# MAKE PREDICTIONS, get residuals
#	train_preds = svr.predict(X_train)
	predictions = svr.predict(X)
	residuals = y - predictions
	
# 		# making predictions to get residuals  
# 	predictions = rf.predict(X)
# 	residuals = y - predictions
# 	
	
# 	# Features Importances
# 	svr_coef_df = pd.DataFrame({
#         'Feature' : X.columns,
#         'Importances' : svr.coef_})
	importen = svr.coef_
        
        	
	# errors 
	rss = round((residuals **2).sum(), 4)									# rss = sse 
	max_e = round(metrics.max_error(y, predictions)  , 4)					# max error
	rmse = round(np.sqrt(metrics.mean_squared_error(y, predictions)), 4)    # root mean squared error
	mae = round(metrics.mean_squared_error(y, predictions),4)               # mean absolute error
	mse = round(metrics.mean_squared_error(y, predictions),4)               # mean squared error  
	r2 = round(metrics.r2_score(y, predictions), 4)                        	# coefficient of determination
	r2xval = round(cross_val_score(svr, X, y).mean(), 4)					# X-val score
	
	svr_mets = ['r2', 'rss', 'max_e', 'rmse', 'mae', 'mse', 'r2xval']
	my_metricss = [r2, rss, max_e, rmse, mae, mse, r2xval ]


	svr_df = pd.DataFrame({
	'Metric':	svr_mets,
	'Value':	my_metricss})
	
	# plot feature importances
	pd.Series(rf.feature_importances_, X.columns).sort_values().plot(kind = 'barh');
	
	
	final_score = svr.score(X_train, y_train)
	return(final_score, importen)