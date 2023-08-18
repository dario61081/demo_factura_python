from typing import Protocol

from databases import session, Database
from models import ModelSucursal, ModelCaja, ModelTimbrado


class Repository(Protocol):

    def __init__(self):
        self.session = None

    def __del__(self):
        self.session.close()
        self.session = None

    def get_instance(self):
        self.session = Database(path='database/database.sqlite').get_session()

    def get_by_codigo(self, codigo):
        pass

    def list(self):
        pass

    def insert(self, item):
        pass

    def update(self, item):
        pass

    def delete(self, item):
        pass


class RepositorySucursal(Repository):

    def list(self):
        return self.session.query(ModelSucursal).all()

    def get_by_codigo(self, codigo):
        return self.session.query(ModelSucursal).filter_by(codigo=codigo).first()

    def insert(self, item):
        try:
            self.session.add(item)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        return item

    def update(self, item):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        return item

    def delete(self, item):
        try:
            self.session.delete(item)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class RepositoryCaja(Repository):

    def list(self):
        return self.session.query(ModelCaja).all()

    def get_by_codigo(self, codigo):
        return self.session.query(ModelCaja).filter_by(codigo=codigo).first()

    def insert(self, item):
        try:
            self.session.add(item)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        return item

    def update(self, item):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        return item

    def delete(self, item):
        try:
            self.session.delete(item)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class RepositoryTimbrado(Repository):

    def list(self):
        return self.session.query(ModelTimbrado).all()

    def get_by_codigo(self, codigo):
        return self.session.query(ModelTimbrado).filter_by(codigo=codigo).first()

    def insert(self, item):
        try:
            self.session.add(item)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        return item

    def update(self, item):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        return item

    def delete(self, item):
        try:
            self.session.delete(item)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def get_timbrado_numero(self, codigo_caja):
        return self.session.query(ModelTimbrado).filter_by(codigo_caja=codigo_caja).first()
