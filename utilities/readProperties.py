import configparser
config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
            
class ReadConfig:
    @staticmethod
    def get_application_url():
        url=config.get('common_data','base_url')
        return url

    @staticmethod
    def get_username():
        user_name=config.get('common_data','username')
        return user_name

    @staticmethod
    def get_password():
        password=config.get('common_data','password')
        return password 
    