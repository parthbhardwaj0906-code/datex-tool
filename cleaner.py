import pandas as pd
import numpy as np

def clean(data):
    df = pd.read_csv(data)

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].median())

    non_numeric_cols = df.select_dtypes(exclude=[np.number]).columns
    for col in non_numeric_cols:
        if df[col].isnull().sum() > 0:
            mode1 = df[col].mode()
            fill = "UNKNOWN"
            if not mode1.empty:
                 fill = mode1[0];
            df[col].fillna(fill)

    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        df[col] = np.clip(df[col], lower_bound, upper_bound)

    return df