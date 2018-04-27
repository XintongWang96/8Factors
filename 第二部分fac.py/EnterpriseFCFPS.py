#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    

    temp=dv.get_ts('fcffps')
    dv.append_df(temp,'EnterpriseFCFPS_J')
    return temp      

