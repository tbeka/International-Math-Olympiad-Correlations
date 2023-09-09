#Accessing one countries result
country = input('Give us the country name:')
country_results = res_one_con(country)

sns.scatterplot(data = country_results, x = 'Distance', y = 'Raiting', hue = country_results.index, palette = 'rocket', legend = False)
sns.regplot(data = country_results, x = 'Distance', y = 'Raiting')
