#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':24}
    if not param:
        param = defult_param
        
    t = param['t']
    
    dv.add_formula('ret','Return(close_adj,1)',is_quarterly=False,add_data=True)
    dv.add_formula('ret_f','ret+1',is_quarterly=False,add_data=True)
    dv.add_formula('vl','If(volume>0,1,0)',is_quarterly=False,add_data=True)
    cmraMx = dv.add_formula('cmraMx0','Ts_Product(ret_f*vl,%s)'%t,is_quarterly=False,add_data=True)
    cmraMn = dv.add_formula('cmraMn0','cmraMx0',is_quarterly=False,add_data=True)
# step max
    for k in range(t-1):
        temp_prod = dv.add_formula('temp_prod','Ts_Product(Delay(ret_f*vl,%s),%s)'%(k+1,t-k),is_quarterly=False,add_data=True)
        cmra_Mx = dv.add_formula('cmraMx%s'%(k+1),'Max(cmraMx%s,temp_prod)'%(k),is_quarterly=False,add_data=True)
        cmra_Mn = dv.add_formula('cmraMn%s'%(k+1),'Min(cmraMn%s,temp_prod)'%(k),is_quarterly=False,add_data=True)
    Cmra = dv.add_formula('Cmra_J','Log(cmraMx%s)-Log(cmraMn%s)'%(t-1,t-1),is_quarterly=False,add_data=True)

    return Cmra

