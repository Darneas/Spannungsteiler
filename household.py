import pandas as pd

class Household():
    def __init__(self):
        file = './Messdaten.xlsx'

        self._current_time = 0
        self._max_samples = 96

        self.buffer = 1.0
        self.buffer_target = 0.2
        self.buffer_capacity = 10000
        self.production = 0
        self.consumption = 0
        dataframe = pd.read_excel(file)
        dataframe = dataframe[0:self._max_samples]
        self._profile = dataframe

    def round_callback(self):
        def callback(dt):
            # TODO: parse ID
            row = self._profile.iloc[self._current_time]
            self.produce(row["Energieproduktion [W]"])
            self.consume(row['Energieverbrauch1 [W]'])
            self._current_time = (self._current_time + 1) % self._max_samples
        return callback

    def consume(self, value):
        self.consumption = value
        self.buffer -= value / self.buffer_capacity
        assert(self.buffer >= 0)

    def produce(self, value):
        self.production = value
        self.buffer += value / self.buffer_capacity
        if self.buffer > 1.0:
            self.buffer = 1.0

    @property
    def balance(self):
        return self.production - self.consumption

    @property
    def demand(self):
        delta = self.buffer * self.buffer_capacity + self.balance
        return max(0, self.buffer_target * self.buffer_capacity - delta)

    @property
    def offer(self):
        delta = self.buffer * self.buffer_capacity + self.balance
        return max(0, delta - self.buffer_target * self.buffer_capacity)
