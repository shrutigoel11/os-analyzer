from sklearn.preprocessing import MinMaxScaler

def normalize(df):
    scaler = MinMaxScaler()
    return scaler.fit_transform(df)