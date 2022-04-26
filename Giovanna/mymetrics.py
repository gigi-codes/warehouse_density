# SECOND, MODIFIED MODULE

# takes FOUR (3) args: clean, numeric, dummified (X, y) and train_size (0-1), and leaf depth 
# runs model, prints and returns 6 errors and feature importances

# checks LINE assumptions, returns plots 


##### IMPORTS #####  --- --- --- --- --- --- --- --- --- --- --- ---
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('gstyle.mplstyle') 

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import metrics        					

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures

##### FUNCTION DEF #####  --- --- --- --- --- --- --- --- --- --- --- ---
def allmet(X, y, t_size, m_d):

	X = X
	y = y 

	# making model 
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, train_size = t_size)
	
	# scale
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)
	
	
	# fit
	rfc = RandomForestRegressor(max_depth=m_d, random_state=0)
	rfc.fit(X_train, y_train)
			
# 		RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
#                        max_depth=None, max_features='auto', max_leaf_nodes=None,
#                        min_impurity_decrease=0.0, min_impurity_split=None,
#                        min_samples_leaf=1, min_samples_split=2,
#                        min_weight_fraction_leaf=0.0, n_estimators=10,
#                        n_jobs=None, oob_score=False, random_state=0, verbose=0,
#                        warm_start=False)

	# Features Importances
	rfc_coef_df = pd.DataFrame({
        'Feature' : X.columns,
        'Importances'   : rfc.feature_importances_})
		
	# making predictions to get residuals  
	predictions = rfc.predict(X)
	residuals = y - predictions
	
	# errors 
	rss = round((residuals **2).sum(), 4)									# rss = sse 
	max_e = round(metrics.max_error(y, predictions)  , 4)					# max error
	rmse = round(np.sqrt(metrics.mean_squared_error(y, predictions)), 4)    # root mean squared error
	mae = round(metrics.mean_squared_error(y, predictions),4)               # mean absolute error
	mse = round(metrics.mean_squared_error(y, predictions),4)               # mean squared error  
	r2 = round(metrics.r2_score(y, predictions), 4)                        	# coefficient of determination
	r2xval = round(cross_val_score(rfc, X, y).mean(), 4)					# X-val score
	
	my_metrics_s = ['r2', 'rss', 'max_e', 'rmse', 'mae', 'mse', 'r2xval']
	my_metrics = [r2, rss, max_e, rmse, mae, mse, r2xval ]

	lr_df = pd.DataFrame({
	'Metric':	my_metrics_s,
	'Value':	my_metrics})
	
	return(rfc.base_estimator_, rfc_coef_df, lr_df)
		
# 	# --- LINE checks, plots with help from Jessely --- --- --- --- --- ---
# 	
# 	fig, ax = plt.subplots(nrows=1, ncols=3, sharey=False, figsize=(15, 6))
# 	fig.suptitle('LINE Checks')
# 	
# 	# linearity
# 	ax[0].set(xlabel='Target (Actual Price, $)', ylabel='Predictions')
# 	sns.scatterplot(x= y , y=predictions, ax = ax[0], color = 'lightcoral').set(title='Linearity');
# 	
# 	#normality 
# 	ax[1].set(xlabel='Frequency', ylabel='Residuals')
# 	sns.histplot(x = residuals, ax = ax[1], color = 'lightcoral', bins = 50).set(title = 'Normality');
# 	
# 	# equal variance
# 	ax[2].set(xlabel='Target', ylabel='Residuals')
# 	sns.scatterplot(x= y , y = residuals, ax = ax[2], color = 'lightcoral').set(title = 'Equal Variance');