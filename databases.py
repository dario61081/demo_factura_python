from contextlib import contextmanager

from sqlalchemy import create_engine, NullPool
from sqlalchemy.orm import Session, sessionmaker


class Database:
    """
    Database
    :param path: database sqlite path

    """

    def __init__(self, **kwargs):
        self.path = kwargs.get('path', None)
        self.engine = create_engine('sqlite:///' + self.path, echo=False)
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.engine)()

    # def __del__(self):
    #     if self.session:
    #         self.session.close()
    #     self.connection.close()
    #     self.engine.dispose()

    def execute(self, sql, **kwargs):
        """
        Execute sql
        :param sql: sql statement
        :return: result
        """
        return self.connection.execute(sql, **kwargs)

    def fetch_one(self, sql, **kwargs):
        """
        Fetch one
        :param sql: sql statement
        :return: result
        """
        return self.connection.execute(sql, **kwargs).fetchone()

    def fetch_all(self, sql, **kwargs):
        """
        Fetch all
        :param sql: sql statement
        :return: result
        """
        return self.connection.execute(sql, **kwargs).fetchall()

    def fetch_scalar(self, sql, **kwargs):
        """
        Fetch scalar
        :param sql: sql statement
        :return: result
        """
        return self.connection.execute(sql, **kwargs).scalar()

    def get_session(self):
        """
        Get session
        :return: session
        """
        return self.session

    def check_table(self, cls):
        """
        Check table
        :param cls: class
        :return: True if table exists
        """
        return self.engine.dialect.has_table(connection=self.connection, table_name=cls.__tablename__)

    def create_table(self, cls):
        """
        Create table
        :param cls: class
        :return: True if table exists
        """
        cls.__table__.create(self.engine)

    def drop_table(self, cls):
        """
        Drop table
        :param cls: class
        :return: True if table exists
        """
        cls.__table__.drop(self.engine)

    def install_setup(self, cls):
        """
        Install setup
        :param cls: class
        :return: True if table exists
        """
        instance = cls()
        if hasattr(instance, 'setup'):
            list = instance.setup()
            for item in list:
                s = self.get_session()
                s.merge(item)
                s.commit()


@contextmanager
def session(path):
    """
    Session
    :param path: database sqlite path
    :return: session
    """
    db = Database(path=path)
    yield db
