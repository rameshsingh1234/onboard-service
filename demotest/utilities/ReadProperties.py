import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../resources/configurations/config.ini'))


class ReadConfig:
    """Method that returns the application url"""
    @staticmethod
    def get_api_url():
        url = config.get('config', 'url')
        return url

    """Method that returns the logs dir path """
    @staticmethod
    def get_logs_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("utilities", "")
        logs_directory = os.path.join(current_directory, 'logs')
        return logs_directory

    """Method that returns the reports dir path """

    @staticmethod
    def get_reports_directory():
        current_directory = os.path.dirname(__file__)
        current_directory = current_directory.replace("utilities", "")
        reports_directory = os.path.join(current_directory, 'reports')
        return reports_directory
