import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../resources/configurations/config.ini'))


class ReadConfig:
    """Method that returns the application url"""
    @staticmethod
    def get_api_url():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_folder = os.path.dirname(current_dir) + '/resources/configurations/config.ini'
        config = configparser.ConfigParser()
        config.read(parent_folder);

        url = config['CREDs']['url']
        return url

    @staticmethod
    def get_api_url2():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_folder = os.path.dirname(current_dir) + '/resources/configurations/config.ini'
        config = configparser.ConfigParser()
        config.read(parent_folder);

        url = config['CREDs']['url2']
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
