# ---------------------------
# module has two functions
# ---------------------------
#
# 1: G's Random Forest Regressor
# gs_rf(X, y, params)
# 	X, y
# 	t_size : train set size
#	params_in : parameters dict
# takes FOUR (4) args: clean, numeric, dummified (X, y) and train_size (0-1), and leaf depth 
#
# ---------------------------
# 2: G's SVR (?)
# gs_svr(X, y, t_size, m_d)
# 	X, y
# 	t_size : train set size
#	m_d: max_leaf_depth
# takes FOUR (4) args: clean, numeric, dummified (X, y) and train_size (0-1)
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

def gs_rf(X, y, params_in):

    X = X
    y = y 
    
    print ('pre-processing ... ')
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, train_size = 0.7)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    

    rf = RandomForestRegressor()
    params = params_in
    
    print ('fitting ...')
    gs = GridSearchCV(rf, params, cv = 3)
    
    gs.fit(X_train, y_train)
    results = gs.best_estimator_.feature_importances_
    
    print ('error calculations ... ')
    # making predictions to get residuals  
    preds = gs.predict(X)
    residuals = y - preds
    
    # errors
    rss = round((residuals **2).sum(), 4)
    max_e = round(metrics.max_error(y, preds), 4)
    rmse = round(np.sqrt(metrics.mean_squared_error(y, preds)), 4)
    mae = round(metrics.mean_squared_error(y, preds),4)
    mse = round(metrics.mean_squared_error(y, preds),4)
    r2 = round(metrics.r2_score(y, preds), 4)
    
    my_metrics_s = ['r2', 'rss', 'max_e', 'rmse', 'mae', 'mse']
    my_metrics = [r2, rss, max_e, rmse, mae, mse]

    gs_fi = pd.DataFrame({
        'Feature':	X.columns,
        'Importance': gs.best_estimator_.feature_importances_
        })
    
    gs_metrics = pd.DataFrame({
        'Metric':	my_metrics_s,
        'Value':	my_metrics
        })
        
    print ('plotting ... ')
    
    f, ax = plt.subplots(figsize=(5,7))
    ax.tick_params(bottom=False, left = False)  # remove the ticks
    pd.Series(results, X.columns).sort_values(ascending = False).plot(kind = 'barh');
    (sns.despine(left=True, bottom=True))

    #return(gs_fi, gs_metrics)
    return(gs.best_estimator_.get_params, gs_fi, gs_metrics)