import pandas as pd

def cargar_datos(path):
    return pd.read_csv(path, sep=";")

def procesar_fecha(df):
    df.columns = df.columns.str.strip()
    df['dt'] = pd.to_datetime(df['dt'], dayfirst=True)
    df['year'] = df['dt'].dt.year
    return df

if __name__ == "__main__":
    df = cargar_datos("data/datos_mock.csv")
    df = procesar_fecha(df)
    print(df.head())
