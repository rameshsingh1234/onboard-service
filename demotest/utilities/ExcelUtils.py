import csv
import os


class Excel:
    @staticmethod
    def get_data():
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../resources/test_data/Onboarding_API - AA.csv')
        with open(filepath,'r') as f:
            reader = csv.reader(f)
            next(reader) #skipping the first row
            data = [tuple(row) for row in reader]
        return  data
