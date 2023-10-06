import pymysql
from data import config


class MySqlBot:
    def __init__(self):
        self.connect = pymysql.connect(host=config.host,
                                       user=config.user,
                                       password=config.password,
                                       database=config.database
                                       )
        self.cursor = self.connect.cursor()

    def write_command_to_database(self, user_id, commands):
        self.cursor.execute('INSERT INTO history (user_id, commands) VALUES (%s, %s)', (user_id, commands))
        self.connect.commit()

    def output_commands_from_databases(self, user_id):
        self.cursor.execute(f'SELECT * FROM history WHERE user_id = {user_id}')
        result = self.cursor.fetchall()
        list_commands = [i[1] for i in result]
        return list_commands


my_sql_bot = MySqlBot()