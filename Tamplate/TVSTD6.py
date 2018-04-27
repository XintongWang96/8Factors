#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':6}
    if not param:
        param = defult_param
        
    t = param['t']
    
    dv.add_formula('turn_over_value','close_adj*volume/Pow(10,%s)'%t,is_quarterly=False,add_data=True)
    TVSTD6=dv.add_formula('TVSTD6_J','StdDev(turn_over_value,24)',is_quarterly = False,add_data = True)

    return TVSTD6

