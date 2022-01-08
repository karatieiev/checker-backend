import os


class PersistManager:
    @staticmethod
    def init(config):
        if not os.path.exists(configDATABASE):
            pass
        new_db_file = open(config.DATABASE, 'w+')
        new_db_file.close()
