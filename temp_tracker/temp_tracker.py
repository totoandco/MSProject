class TempTracker:

    max_temp = 110  # type: int max temperature value
    min_temp = 0  # type: int min temperature value

    def __init__(self):
        self.__temperatures = []

    def insert(self, new_value):
        """

        :param new_value: insert new value into the tab where we save the previous temperature
        """
        if isinstance(new_value, int):
            if TempTracker.min_temp <= new_value <= TempTracker.max_temp:
                self.__temperatures.append(new_value)
            else:
                raise ValueError('out of range, input should be between ' + str(TempTracker.min_temp) + ' and ' + str(
                    TempTracker.max_temp))
        else:
            raise ValueError('input should be an integer')

    def get_max(self):
        """

        :return: max temperature in the tab. if no temperatures have been saved , it will return 0
        """
        if len(self.__temperatures) == 0:
            return 0
        else:
            return max(self.__temperatures)

    def get_min(self):
        """

        :return: min temperature in the tab. if no temperatures have been saved , it will return 0
        """
        if len(self.__temperatures) == 0:
            return 0
        else:
            return min(self.__temperatures)

    def get_mean(self):
        """

        :return: the mean of the current temperatures saved in the tab. if no temperatures have been saved , it will return 0
        """
        if len(self.__temperatures) == 0:
            return float(0)
        else:
            return float(sum(self.__temperatures)) / float(len(self.__temperatures))
