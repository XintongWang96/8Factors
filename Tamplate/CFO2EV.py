#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    
    #(ncf_oper_ttm,lt_borrow,st_borrow,total_mv,end_bal_cash) =(dv.get_ts(x) 
                                                         #for x in ('ncf_oper_ttm','lt_borrow','st_borrow','total_mv','end_bal_cash'))
    #CFO2EV_J=ncf_oper_ttm/(lt_borrow+st_borrow+total_mv-end_bal_cash) 
    CFO2EV = dv.add_formula('CFO2EV_J',"ncf_oper_ttm/(lt_borrow+st_borrow+total_mv-end_bal_cash)",is_quarterly=False, add_data=True)
    #CFO2EV=dv.append_df(CFO2EV_J,'CFO2EV_J')

    return CFO2EV

