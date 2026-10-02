import pandas as pd


def clean_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.drop_duplicates().copy()
    for column in df.select_dtypes(include='number').columns:
        df[column] = df[column].fillna(df[column].median())
    for column in df.select_dtypes(exclude='number').columns:
        df[column] = df[column].fillna('Unknown')
    return df


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe(include='all').transpose()


if __name__ == '__main__':
    data = clean_data('data/input.csv')
    data.to_csv('data/clean.csv', index=False)
    summarize(data).to_csv('data/summary.csv')
    print(data.head())
