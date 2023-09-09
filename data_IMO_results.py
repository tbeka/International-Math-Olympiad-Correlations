results = table_scrapper("https://www.imo-official.org/results.aspx")
#Getting rid off duplicates
results = results.iloc[:, ~results.columns.duplicated()]
results.rename(columns={'Year': 'Country'}, inplace=True)

column_names_list = results.columns.tolist()
column_names_list.reverse()
base = 1959

for i in column_names_list[:-1]:
    if base == 1980:
        base = base+1
        results.rename(columns={i:str(base)}, inplace=True)
        base = base+1
        continue
    results.rename(columns={i:str(base)}, inplace=True)
    base = base+1
results = results.set_index(['Country'])

results_transposed = results.transpose()
results_transposed.rename(columns={'Country':'Year'}, inplace=True)
results_transposed.index.name = None
