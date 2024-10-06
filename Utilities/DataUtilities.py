import pandas as pd


class DataUtilities:

    @staticmethod
    def dataframe_to_matrix(data_frame: pd.DataFrame):
        return data_frame.to_numpy()