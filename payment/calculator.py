class TariffCalculator:
    def calculate_tariff(self, entry_time, exit_time, spot_type):
        raise NotImplementedError

class FlatRateCalculator(TariffCalculator):
    def __init__(self, rate_table):
        self.rate_table = rate_table

    def calculate_tariff(self, entry_time, exit_time, spot_type):
        duration = (exit_time - entry_time) / 3600
        hourly_rate = self.rate_table.get(spot_type, 30)
        return round(max(duration, 1) * hourly_rate, 2)
