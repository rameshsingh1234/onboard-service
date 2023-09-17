import csv
import os


class Excel:
    @staticmethod
    def get_data():
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '/home/ramesh/onboard-service/test/resources/test_data/Onboarding_API - AA.csv')
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skipping the first row
            data = [tuple(row) for row in reader]
        return data

    def fiu_get_data():
        filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '../resources/test_data/Onborading_API - FIU.csv')
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skipping the first row
            data = [tuple(row) for row in reader]
        return data


    # client credentials
    csv_file = '/home/ramesh/onboard-service/test/resources/test_data/client_credentials.csv'

    def read_client_credentials(csv_file):
        client_credentials = []
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                client_credentials.append(row)
        return client_credentials
