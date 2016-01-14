from mysql_connection import MysqlPython

class fireplace_mv1():

    connect_mysql = MysqlPython('localhost', 'root', '', 'fireplace_sessionIDs')
    def return_sessionid_list(connection, table_name):
        table_name = "%s" % table_name
        result = connection.select_basic(table_name)
        print result

    def return_sessionid(connection, table_name, row_number):
        # sql_query = 'SELECT session_id FROM %s' % table_name
        table_name = "%s" % table_name
        result = connection.select_basic(table_name)
        # print result
        print result[row_number]

    mv1_tables = {"mv1.1":"sessionids_mv1_2014_12_16", "mv1.2":"sessionids_mv1_2014_12_22_02"}
    rows = [1, 2, 3, 4, 7, 3, 5, 6]
    for row in rows:
        return_sessionid(connect_mysql, mv1_tables["mv1.1"],row)
