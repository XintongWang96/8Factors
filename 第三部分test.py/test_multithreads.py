import timeit
start=timeit.default_timer()
import pandas as pd

def get_dv(start = 20170101,end = 20180101): 
    import jaqs_fxdayu
    jaqs_fxdayu.patch_all()
    from jaqs_fxdayu.data import DataView
    from jaqs_fxdayu.data.dataservice import LocalDataService
    
    import warnings
    warnings.filterwarnings("ignore")
    
    #--------------------------------------------------------
    
    #define
    factor_list  = ['fcffps','lt_borrow','st_borrow','LCAP','end_bal_cash']
    check_factor = ','.join(factor_list)
    
    dataview_folder = r'D:/data'
    ds = LocalDataService(fp = dataview_folder)
    
    ZZ800_id = ds.query_index_member("000906.SH", start, end)
    stock_symbol = list(set(ZZ800_id))
    
    dv_props = {'start_date': start, 'end_date': end, 'symbol':','.join(stock_symbol),
             'fields': check_factor,
             'freq': 1,
             "prepare_fields": True}
    
    dv = DataView()
    dv.init_from_config(dv_props, data_api=ds)
    dv.prepare_data()

    # total market value
    data_config = {
        "remote.data.address": "tcp://data.tushare.org:8910",
        "remote.data.username": "13662241013",
        "remote.data.password": "eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVfdGltZSI6IjE1MTc2NDQzMzg5MTIiLCJpc3MiOiJhdXRoMCIsImlkIjoiMTM2NjIyNDEwMTMifQ.sVIzI5VLqq8fbZCW6yZZW0ClaCkcZpFqpiK944AHEow"
    }
    from jaqs_fxdayu.data.dataservice import RemoteDataService
    ds1 = RemoteDataService()
    ds1.init_from_config(data_config)
    dv.add_field('total_mv',ds1)
    dv.add_field('ncf_oper_ttm',ds1)

    return dv


if 'dv' not in dir():
    dv = get_dv()
    
#--------------------------------------------------------- 
#test output
def test(factor,data):
    if not isinstance(data, pd.core.frame.DataFrame):
        raise TypeError('On factor {} ,output must be a pandas.DataFrame!'.format(factor))
    else:
        try:
            index_name = data.index.names[0]
            columns_name = data.index.names[0]
        except:
            if not (index_name in ['trade_date','report_date'] and columns_name == 'symbol'):
                raise NameError('''Error index name,index name must in ["trade_date","report_date"],columns name must be "symbol" ''')
                
        index_dtype = data.index.dtype_str
        columns_dtype = data.columns.dtype_str
        
        if columns_dtype not in ['object','str']:
            raise TypeError('error columns type')
            
        if index_dtype not in ['int32','int64','int']:
            raise TypeError('error index type')
        print ('{} OK!'.format(factor))

def test_w(factor):
    test(factor, globals()[factor].run_formula(dv))

from Tamplate import Alpha12,Alpha22,Alpha76,CFO2EV,Cmra,EnterpriseFCFPS,TVSTD6,GainVariance20

from concurrent import futures
with futures.ThreadPoolExecutor(8) as executor:
    executor.map(test_w, ['Alpha12','Alpha22','Alpha76','CFO2EV','Cmra','EnterpriseFCFPS','GainVariance20','TVSTD6'])
    
elapsed=timeit.default_timer()-start
print('Elapsed time with multi-threads: %d', elapsed)