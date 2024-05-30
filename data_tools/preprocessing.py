import pandas as pd


class PriceDataProcessor:
    def __init__(self, df):
        self.df = df.copy()
        self.df_grouped = pd.DataFrame

    def group_by_columns(self):
        group_columns = ['brand',
                         'model',
                         'horsepower',
                         'horsepower_range',
                         'country']
        df_grouped = self.df.groupby(by=group_columns, as_index=False).agg({
            '2012': 'median',
            '2013': 'median',
            '2014': 'median',
            '2015': 'median',
            '2016': 'median',
            '2017': 'median',
            '2018': 'median',
            '2019': 'median',
            '2020': 'median',
            '2021': 'median',
            '2022': 'median',
            '2023': 'median',
            '2024': 'median',
        })
        self.df_grouped = df_grouped
        return self.df_grouped

    def calculate_growth(self):
        years = list(map(str, range(2024, 2012, -1)))

        for i in years:
            j = str(int(i)-1)
            self.df[i] = self.df[i]/self.df[j]
        return self.df

    def fill_missing_values(self):
        def fill_by_group(df, group_cols, value_col):
            group_medians = df.groupby(group_cols)[value_col].transform('median')
            df[value_col] = df[value_col].fillna(group_medians)
            return df

        years = list(map(str, range(2024, 2011, -1)))
        for year in years:
            if year == '2012':
                self.df[year] = 1
            else:
                self.df = fill_by_group(self.df, ['brand', 'model', 'horsepower_range'], year)
                self.df = fill_by_group(self.df, ['brand', 'horsepower_range'], year)
                self.df = fill_by_group(self.df, ['country', 'horsepower_range'], year)
                self.df = fill_by_group(self.df, ['horsepower_range'], year)
                self.df[year] = self.df[year].fillna(self.df[year].median())

        return self.df


