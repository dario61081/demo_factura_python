import pytest

from databases import Database
from models import ModelSucursal, ModelCaja, ModelTimbrado


class ModelTest:

    def test_database(self):
        db = Database(path='database/database.sqlite')
        assert db is not None

    def test_model_sucursal(self):
        sucursal = ModelSucursal()
        assert sucursal is not None

    def test_model_caja(self):
        caja = ModelCaja()
        assert caja is not None

    def test_model_timbrado(self):
        timbrado = ModelTimbrado()
        assert timbrado is not None
