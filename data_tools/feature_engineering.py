import numpy as np
import pandas as pd

from config import country_map, segment_map


def bi_search(hp, ranges):
    low, high = 0, len(ranges)
    while low < high:
        mid = (low + high) // 2
        if hp < ranges[mid]:
            high = mid
        else:
            low = mid + 1
    return low


def horsepower_range(hp):
    ranges = [100, 200, 250, 300, 350, 400, 450, 500]
    labels = ['<100', '100-199', '200-249', '250-299', '300-349', '350-399', '400-449', '450-499', '500+']

    return labels[bi_search(hp, ranges)]


def create_hp_classes(df):
    df['horsepower_range'] = df['horsepower'].apply(horsepower_range)
    return df


def create_segments(df, model_to_segment=segment_map):
    def classify_model(model):
        return model_to_segment.get(model, 'Other')

    # Создание нового столбца 'Segment' на основе модели автомобиля
    df['segment'] = df['model'].apply(classify_model)
    return df


def add_country(df):
    df['country'] = df['brand'].map(country_map)
    df['brand'] = df['brand'].fillna('Other')
    return df


def create_avg_price(df):
    # df['avg_price'] = df.iloc[:, 4:].mean(axis=1)
    # return df
    df['avg_price'] = df.iloc[:, 4:].mean(axis=1)
    years = [str(year) for year in range(2012, 2025)]
    df['year_embedding'] = df[years].apply(lambda row: [1 if not pd.isna(value) else 0 for value in row], axis=1)

    return df


def create_price_classes(df, price_column):
    price_bins = [0, 1000000, 2000000, 3000000, 4000000, 5000000, 10000000, float('inf')]
    price_labels = ['Very Low', 'Low', 'Medium-Low', 'Medium', 'Medium-High', 'High', 'Very High']

    df['price_class'] = pd.cut(df[price_column], bins=price_bins, labels=price_labels, right=False)

    return df


def update_avg_price(data_final):
    def adjust_avg_price(row):
        if not pd.isna(row['price']):
            num_years = sum(row['year_embedding'])

            if num_years > 1:
                new_avg_price = (row['avg_price'] * num_years - row['price']) / (num_years - 1)
                row['avg_price'] = new_avg_price
            else:
                row['avg_price'] = np.nan

        return row

    data = data_final.copy()
    data['year_embedding'] = data['year_embedding'].apply(
        lambda x: list(map(int, x.strip('[]').split(','))) if isinstance(x, str) else x
    )
    data = data.apply(adjust_avg_price, axis=1)

    return data