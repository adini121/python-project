#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: Mysql Python wrapper class, facilitates selection of sessionIds.
    # Each application has a separate database in which SessionIds for each application version are stored as a MySQL table.
    # Contents of this file are based on (inspired and modified from): https://github.com/nestordeharo/mysql-python-class

import MySQLdb

class MysqlPython(object):
    """ Python Class for connecting to MySQL server """

    __instance   = None
    __host       = None
    __user       = None
    __password   = None
    __database   = None
    __session    = None
    __connection = None


    def __init__(self, host='localhost', user='root', password='', database=''):
        self.__host     = host
        self.__user     = user
        self.__password = password
        self.__database = database

    def __open(self):
        """ Opens MySQL connection to the database """
        try:
            cnx = MySQLdb.connect(self.__host, self.__user, self.__password, self.__database)
            self.__connection = cnx
            self.__session    = cnx.cursor()
        except MySQLdb.Error as e:
            print "MySQL Error %d: %s" % (e.args[0],e.args[1])

    def check_open(self):
        """ Checks the connection to given database with given credentials """
        try:
            cnx = MySQLdb.connect(self.__host, self.__user, self.__password, self.__database)
            self.__connection = cnx
            self.__session    = cnx.cursor()
        except MySQLdb.Error as e:
            print "MySQL Connection Error %d: %s" % (e.args[0],e.args[1])
            connected = False
        else:
            connected = True
        return connected

    def check_table_exists(self,table):
        """ Checks whether given table exists within given database"""
        query = "SHOW TABLES LIKE '%s'" % table
        self.__open()
        self.__session.execute(query)
        result = self.__session.fetchone()
        if result:
            table_exists=True
        else:
            table_exists=False
            print "Following MySQL table does not exist: %s" % table
        return table_exists

    def __close(self):
        self.__session.close()
        self.__connection.close()

    def select_major_version_database(self, major_version_database, table):
        """
        Selects sessionId(s) from given table - for phase one. Provides the facility to select or de-select specific rows of sessionId tables for the sake of comparison.
        This can be accomplished through argument 'major_version_database'

        :param major_version_database: Major version of the application. This dictates which sessionIds are to be deselected for comparison.
        :param table: Name of the MySQL sessionId table
        :return: List of sessionIds
        """

        # """ Moodle """
        if major_version_database == 'moodle':
            query = "SELECT date_created FROM %s" % table # date_created column stores sessionIds for Moodle

        # """ Fireplace """
        if major_version_database == 'fireplace_mv1':
            query = "SELECT session_id FROM %s" % table

        if major_version_database == 'fireplace_mv2':
            query = "SELECT session_id FROM %s" % table

        if major_version_database == 'fireplace_mv3':
            query = "SELECT session_id FROM %s where id != 3" % table

        if major_version_database == 'fireplace_mv4':
            query = "SELECT session_id FROM %s where id != 3" % table

        # """ Jenkins Core """
        if major_version_database == 'jenkins_core_mv1':
            query = "SELECT session_id FROM %s where id != 12 and id != 18 and id != 19 and id != 20" % table

        if major_version_database == 'jenkins_core_mv2':
            query = "SELECT session_id FROM %s where id != 3 and id != 6 and id != 7 and id !=16" % table

        if major_version_database == 'jenkins_core_mv3':
            query = "SELECT session_id FROM %s where id != 16 and id != 17" % table

        if major_version_database == 'jenkins_core_mv4':
            query = "SELECT session_id FROM %s where id != 17 and id != 18" % table

        # """ AMO """
        if major_version_database == 'amo_mv1':
            query = "SELECT session_id FROM %s where id != 4 and id != 5 and id != 6 and id != 7" % table

        if major_version_database == 'amo_mv2':
            query = "SELECT session_id FROM %s where id != 4 and id != 5 and id != 6 and id != 7" % table

        if major_version_database == 'amo_mv3':
            query = "SELECT session_id FROM %s where id != 4 and id != 5 and id != 6 and id != 7" % table

        # """ Bedrock """
        if major_version_database == 'bedrock_mv2':
            query = "SELECT session_id FROM %s where id != 17 and id != 24 and id != 34 and id != 22 and id != 30 and id != 57 and id != 58" % table

        if major_version_database == 'bedrock_mv1':
            query = "SELECT session_id FROM %s where id != 22 and id !=53 and id != 54 and id != 25 and id != 30 and id != 58" % table


        # """ Jenkins plugins """
        if major_version_database == 'jenkins_plugins_mv1':
            query = "SELECT session_id FROM %s where id != 2 and id != 12 and id != 13 and id != 22 and id != 28 and id != 29 and id != 31" % table

        if major_version_database == 'jenkins_plugins_mv2':
            query = "SELECT session_id FROM %s where id != 2 and id != 11 and id != 14 and id != 15" % table

        if major_version_database == 'jenkins_plugins_mv3':
            query = "SELECT session_id FROM %s where id != 2 and id != 12 and id != 15 and id != 16 and id !=17 and id !=20 and id !=21 and id != 22 and id != 30 and id !=31 and id !=32 and id != 33 and id !=34 and id != 40 and id !=46 and id !=47 and id !=48 and id !=49 " % table

        if major_version_database == 'jenkins_plugins_mv4':
            query = "SELECT session_id FROM %s where id != 15 and id != 16 and id !=17 and id !=20 and id !=21 and id !=22 and id !=30 and id !=42 and id !=43 and id !=44 and id !=45 and id !=1 and id !=12 and id !=19 and id !=41 " % table


        self.__open()
        self.__session.execute(query)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        else:
            result = [item[0] for item in self.__session.fetchall()]
        return result

    def select_table_for_phase_two(self, table, querymodifier=''):
        """
        Selects sessionId(s) from given table - for phase two. Provides the facility to select or de-select specific rows of sessionId tables for the sake of comparison.
        This can be accomplished through an optional argument 'querymodifier' - which, if not specified, defaults to null.

        :param table: Name of the MySQL sessionId table
        :param querymodifier: Parameter that dictates which sessionIds are to be deselected for comparison. For example, querymodifier= 'id != 9' deselects
        the row where primary key 'id' is 9.
        :return: List of sessionIds
        """
        if querymodifier:
            query = "SELECT session_id FROM %s" % table + " " + "where %s" % querymodifier
        else:
            query = "SELECT session_id FROM %s" % table

        self.__open()
        self.__session.execute(query)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        else:
            result = [item[0] for item in self.__session.fetchall()]
        return result