from pathlib import Path
import pandas as pd
import numpy as np
import pickle
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


def data_cleaning(data):
    # Handling Missing Values
    data['CREDIT_LIMIT'] = data['CREDIT_LIMIT'].fillna(data['CREDIT_LIMIT'].median())
    data['MINIMUM_PAYMENTS'] = data['MINIMUM_PAYMENTS'].fillna(data['MINIMUM_PAYMENTS'].median())
    # Drop Columns that are unique to all customers
    data.drop('CUST_ID', inplace=True, axis=1)
    return data


def handle_skewness(data):
    positively_skewed_cols = ['BALANCE', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE',
                              'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY', 'CASH_ADVANCE_TRX',
                              'PURCHASES_TRX', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT']

    for col in positively_skewed_cols:
        data[col] = np.log1p(data[col])
    return data

def handle_dimensions(data):
    pca = PCA(n_components=0.95)
    X = pca.fit_transform(data)
    return X


def model_training(X, n_clusters):
    model = KMeans(n_clusters=n_clusters)
    model.fit(X)
    labels = model.labels_
    return labels, model


def save_data_with_clusters(data_cleaned, labels):
    clusters = pd.concat([data_cleaned, pd.DataFrame({'cluster': labels})], axis=1)
    clusters.to_csv(str(Path(__file__).parents[1] / 'data/cluster_data.csv'), index=False)


if __name__ == "__main__":
    # Load Data
    data = pd.read_csv(str(Path(__file__).parents[1] / 'data/credit_card_data.csv'))
    # Clean Data
    data_cleaned = data_cleaning(data)
    data = data_cleaned.copy()
    # Handle Skewness
    data_skewed = handle_skewness(data)
    # Handle High Dimension
    X = handle_dimensions(data_skewed)
    # Build Model
    labels, model = model_training(X, n_clusters=4)
    # Save Data along with cluster info
    save_data_with_clusters(data_cleaned, labels)
    # Save Model
    with open(str(Path(__file__).parents[1] / 'model/model.pickle'), 'wb') as f:
        pickle.dump(model, f)
