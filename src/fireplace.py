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

    mv1_tables = {"fireplace_mv1.1":"sessionids_mv1_2014_12_16", "fireplace_mv1.2":"sessionids_mv1_2014_12_22_02"}
    rows = [1, 2, 3, 4, 7, 3, 5, 6]
    for table in mv1_tables:
        tbl = mv1_tables[table]
        print table
        for row in rows:
            return_sessionid(connect_mysql, tbl,row)
