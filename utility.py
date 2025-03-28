from sklearn.base import BaseEstimator, TransformerMixin


class DataCleaner(BaseEstimator, TransformerMixin):
    def __init__(self, nan_column=None, duplicate_column=None):

        self.nan_column = nan_column
        self.duplicate_column = duplicate_column

    def fit(self, X, y=None):

        return self

    def transform(self, X):

        if self.nan_column:
            X = X[X[self.nan_column].notna()]
        if self.duplicate_column:
            X = X.drop_duplicates(subset=self.duplicate_column, keep="first")
        return X
