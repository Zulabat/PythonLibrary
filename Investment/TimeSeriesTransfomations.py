from CustomObjects.TimeSeries import TimeSeries
class TimeSeriesTransformations:

    @staticmethod
    def get_daily_returns(data: TimeSeries) -> dict:
        raise NotImplementedError()
        return {}

    @staticmethod
    def get_cumulative_return(data: TimeSeries) -> float:
        return 100
