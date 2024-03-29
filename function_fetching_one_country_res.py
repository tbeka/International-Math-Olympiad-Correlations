#Joining the venues and results tables
total = pd.merge(venues, results_transposed, left_index=True, right_index=True)

import country_converter as coco

#Function accessing results of one of the countries
def res_one_con(country):
    country_code = coco.convert(country, to='ISO3')     
    con_results = total[['Host', 'Countries', country_code]]
    con_results[country_code] = con_results[country_code].apply(pd.to_numeric)
    #con_results = con_results[country_code].replace(['', '—'] , 0).astype(int)
    con_results['Raiting'] = (con_results['Countries']- con_results[country_code])/con_results['Countries']
    con = con_results.iloc[0:25] 
    con['Distance'] = con.apply(lambda x: dist(country, x['Host']), axis=1)
    print(con.head())
    return con
