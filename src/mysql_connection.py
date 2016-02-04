#!/usr/bin/env python
# coding=utf-8
"""This is a Mysql Python wrapper class, modified fork of : git@github.com:nestordeharo/mysql-python-class.git"""

import MySQLdb
from collections import OrderedDict

class MysqlPython(object):
    """ Python Class for connecting to MySQL server """

    __instance   = None
    __host       = None
    __user       = None
    __password   = None
    __database   = None
    __session    = None
    __connection = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance or not cls.__database:
             cls.__instance = super(MysqlPython, cls).__new__(cls,*args,**kwargs)
        return cls.__instance
    ## End def __new__

    def __init__(self, host='localhost', user='root', password='', database=''):
        self.__host     = host
        self.__user     = user
        self.__password = password
        self.__database = database
    ## End def __init__

    def __open(self):
        try:
            cnx = MySQLdb.connect(self.__host, self.__user, self.__password, self.__database)
            self.__connection = cnx
            self.__session    = cnx.cursor()
        except MySQLdb.Error as e:
            print "Error %d: %s" % (e.args[0],e.args[1])
    ## End def __open

    def __close(self):
        self.__session.close()
        self.__connection.close()
    ## End def __close

    def select_major_version_database(self, major_version_database, table):
        """  """
        """ Moodle """
        if major_version_database == 'moodle':
            query = "SELECT date_created FROM %s" % table

        """ Fireplace """
        if major_version_database == 'fireplace_mv1': # Select All rows
            query = "SELECT session_id FROM %s" % table

        if major_version_database == 'fireplace_mv2':
            query = "SELECT session_id FROM %s" % table

        if major_version_database == 'fireplace_mv3':
            query = "SELECT session_id FROM %s where id != 3" % table

        if major_version_database == 'fireplace_mv4':
            query = "SELECT session_id FROM %s where id != 3" % table

        """ Jenkins Core """
        if major_version_database == 'jenkins_core_mv1':
            query = "SELECT session_id FROM %s where id != 12 and id != 18 and id != 19 and id != 20" % table

        if major_version_database == 'jenkins_core_mv2':
            query = "SELECT session_id FROM %s where id != 3 and id != 6 and id != 7 and id !=16" % table

        if major_version_database == 'jenkins_core_mv3':
            query = "SELECT session_id FROM %s where id != 16 and id != 17" % table

        if major_version_database == 'jenkins_core_mv4':
            query = "SELECT session_id FROM %s where id != 17 and id != 18" % table

        """ AMO """
        if major_version_database == 'amo_mv1': #MV1 starts at 2015_01_01
            query = "SELECT session_id FROM %s where id != 4 and id != 5 and id != 6 and id != 7" % table

        if major_version_database == 'amo_mv2': #MV2 starts at 2015_04_25
            query = "SELECT session_id FROM %s where id != 4 and id != 5 and id != 6 and id != 7" % table

        if major_version_database == 'amo_mv3': #MV3 starts at 2015_07_31
            query = "SELECT session_id FROM %s where id != 4 and id != 5 and id != 6 and id != 7" % table

        """ Bedrock """
        if major_version_database == 'bedrock_mv2':
            query = "SELECT session_id FROM %s where id != 30 and id != 57 and id != 58" % table

        if major_version_database == 'bedrock_mv1':
            query = "SELECT session_id FROM %s where id !=53 and id != 54 and id != 25 and id != 30 and id != 58" % table
            #added failed ID rows, missing ID rows,

        self.__open()
        self.__session.execute(query)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        else:
            result = [item[0] for item in self.__session.fetchall()]
        return result
## End class