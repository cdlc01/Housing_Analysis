import pandas as pd
import numpy as np
df = pd.read_csv('Data_For_Code/kc_house_data_copy.csv')

def edited_dataframe():

    def make_month(string):
        if string[:2] == '1/':
            return 'Jan'
        if string[:2] == '2/':
            return 'Feb'
        if string[:2] == '3/':
            return 'Mar'
        if string[:2] == '4/':
            return 'Apr'
        if string[:2] == '5/':
            return 'May'
        if string[:2] == '6/':
            return 'Jun'
        if string[:2] == '7/':
            return 'Jul'
        if string[:2] == '8/':
            return 'Aug'
        if string[:2] == '9/':
            return 'Sep'
        if string[:2] == '10':
            return 'Oct'
        if string[:2] == '11':
            return 'Nov'
        if string[:2] == '12':
            return 'Dec'

        df_alt = df.drop(['id', 'date', 'yr_built', 'yr_renovated', 'lat', 'long'], axis = 1)
        month_list = []
        sqft_basement_list = []
        yr_renovated = []
        for date in df['date'].values:
            month_list.append(make_month(date))
        for num in df['sqft_basement'].values:
            if num == '?':
                sqft_basement_list.append(np.nan)
            else:
                sqft_basement_list.append(float(num))
        for data in df['yr_renovated'].values:
                if data == 0:
                    yr_renovated.append(0)
                elif data == np.nan:
                    yr_renovated.append(np.nan)
                else:
                    yr_renovated.append(1)
        df_alt['month'] = month_list
        df_alt['sqft_basement'] = sqft_basement_list
        df_alt['renovated'] = yr_renovated
        df_alt['zipcode'] = df_alt['zipcode'].apply(str)
        df_alt['age_of_house'] = 2021 - df['yr_built']
        df_alt['total_sq_ft'] = df['sqft_above'] + df['sqft_basement']

        return df_alt
