from Enums.TimeSeriesPurpose import TimeSeriesPurpose


class TimeSeries:
    time_series_purpose = TimeSeriesPurpose.Investment
    data = {}

    def __init__(self, data: dict, time_series_purpose: TimeSeriesPurpose):
        self.data = data
        self.time_series_purpose = time_series_purpose
