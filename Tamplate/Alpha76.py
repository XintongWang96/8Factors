#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):

    
    alpha76 = dv.add_formula('alpha76','StdDev(Abs((close_adj/Delay(close_adj,1)-1))/volume,20)/Ts_Mean(Abs((close_adj/Delay(close_adj,1)-1))/volume,20)',is_quarterly=False,add_data=True)
    
    return alpha76
