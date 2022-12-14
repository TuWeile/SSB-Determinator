from import_datasets import RunImport
import os


class FixedBondYields:

    @staticmethod
    def calc_fixed_yields():
        if os.path.exists("script/config.ini"):
            instance = RunImport()
            data = instance.import_data()

            eer = [0 for i in range(10)]

            # Obtain the simple average of the daily 1 Year SGS benchmark yields for that month
            eer[0] = (sum(data[3]) / len(data[3]))

            # Obtain the simple average of the daily 2 Year SGS benchmark yields for that month
            eer[1] = (sum(data[4]) / len(data[4]))

            # Obtain the simple average of the daily 5 Year SGS benchmark yields for that month
            eer[4] = (sum(data[5]) / len(data[5]))

            # Obtain the simple average of the daily 10 Year SGS benchmark yields for that month
            eer[-1] = (sum(data[6]) / len(data[6]))

            return eer
