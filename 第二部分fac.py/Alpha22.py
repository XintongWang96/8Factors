#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):

    
    alpha22 = dv.add_formula('alpha22','Ts_Mean(((close_adj-Ts_Mean(close_adj,6))/Ts_Mean(close_adj,6)-Delay((close_adj-Ts_Mean(close_adj,6))/Ts_Mean(close_adj,6),3)),12)',is_quarterly=False,add_data=True)
    
    return alpha22
