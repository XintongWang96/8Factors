#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
    t = param['t']
    ret_f = dv.add_formula('ret_f','Return(close_adj,%s)'%t,is_quarterly=False,add_data=True)

    GainVariance20 = dv.add_formula('GainVariance20_J','If(ret_f>0,250*((Ts_Mean(ret_f^2,%s)-(Ts_Mean(ret_f,%s))^2)),0)'%(t,t),is_quarterly=False,add_data=True)
    
    return GainVariance20
