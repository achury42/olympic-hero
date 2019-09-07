# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns ={'Total':'Total_Medals'}, inplace=True)
data.head(10)

#Code starts here



# --------------
#Code starts here




data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event'])
better_event = data['Better_Event'].value_counts().idxmax()



# --------------
#Code starts here




top_countries = data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']]
# The below line is also correct
#top_countries.drop(top_countries.tail(1).index, inplace=True)
top_countries = top_countries[:-1]

#def top_ten(x, y):
 #   country_list =[]
  #  country_list.append(x.nlargest(10,y)['Country_Name'].values)
   # return(country_list)

def top_ten(x,y):
    country_list=[]
    TC = x.nlargest(10,y)
    country_list.append(TC.Country_Name.tolist())
    return(country_list[0])

top_10_summer = top_ten(top_countries, 'Total_Summer')
print(top_10_summer)
top_10_winter = top_ten(top_countries, 'Total_Winter')
print(top_10_winter)
top_10 = top_ten(top_countries, 'Total_Medals')
print(top_10)
#common = np.intersect1d(top_10_summer, top_10_winter, top_10)
common = [x for x in top_10_summer if x in top_10_winter and x in top_10]
print(common)



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summ_pos = np.arange(len(summer_df['Country_Name']))
plt.bar(summ_pos,summer_df['Total_Medals'])
plt.xticks(summ_pos, summer_df['Country_Name'])
plt.show()

win_pos = np.arange(len(winter_df['Country_Name']))
plt.bar(win_pos,winter_df['Total_Medals'])
plt.xticks(win_pos, winter_df['Country_Name'])
plt.show()

y_pos = np.arange(len(top_df['Country_Name']))
plt.bar(y_pos,top_df['Total_Medals'])
plt.xticks(y_pos, top_df['Country_Name'])
plt.show()



# --------------
#Code starts here



summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df['Country_Name'][summer_df.Golden_Ratio.idxmax()]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df['Country_Name'][winter_df.Golden_Ratio.idxmax()]

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df['Country_Name'][top_df.Golden_Ratio.idxmax()]


# --------------
#Code starts here


data_1 = data[:-1]
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']
most_points = max(data_1.Total_Points)
best_country = data_1['Country_Name'][data_1.Total_Points.idxmax()]


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


