#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    alpha12=dv.add_formula('alpha12','(Rank((open_adj- (Ts_Sum(vwap_adj, 10) / 10)))) * (-1 * (Rank(Abs((close_adj - vwap_adj)))))',is_quarterly=False,add_data=True)
    
    return alpha12
