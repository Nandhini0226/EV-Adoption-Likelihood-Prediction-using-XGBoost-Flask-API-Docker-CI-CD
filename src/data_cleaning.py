

def clean_data(df):
    # 1. Missing value handling

    # Replace missing values in education_level with mode
    df['education_level'].fillna(
        df['education_level'].mode()[0],
        inplace=True
    )

    # Replace missing values with median
    df['charging_station_accessibility'].fillna(
        df['charging_station_accessibility'].median(),
        inplace=True
    )

    df['ev_knowledge_score'].fillna(
        df['ev_knowledge_score'].median(),
        inplace=True
    )

    # 2. Binary value conversion

    df['home_charging_available'] = df['home_charging_available'].map({
        1: 'Yes',
        0: 'No'
    })

    df['previous_ev_experience'] = df['previous_ev_experience'].map({
        1: 'Yes',
        0: 'No'
    })

    # 3. Outlier capping

    num_cols = df.select_dtypes(include=['int64', 'float64']).columns

    for col in num_cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)

        df[col] = df[col].clip(
            lower=lower_bound,
            upper=upper_bound
        )

    return df