import os

import click

from databases import Database
from models import ModelFacturaItem, ModelFactura, ModelTimbrado, ModelCaja, ModelSucursal


def main():
    click.echo("Instalación")
    click.echo("1. Creando base de datos")

    directory_path = os.path.join(os.path.dirname(__file__), 'database')
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    database_path = os.path.join(directory_path, 'database.sqlite')

    click.echo("2. Creando entidades")
    tables = [ModelSucursal, ModelCaja, ModelTimbrado, ModelFactura, ModelFacturaItem]
    tables_to_setup = []

    db = Database(path=database_path)

    click.echo("Creando entidades")
    for table in tables:
        if not db.check_table(table):
            db.create_table(table)
            click.echo("Entidad {} creada".format(table.__tablename__))
            tables_to_setup.append(table)
            click.echo("Entidad {} inicializada".format(table.__tablename__))
        else:
            click.echo("Entidad {} ya existe".format(table.__tablename__))

    for table in tables_to_setup if len(tables_to_setup) > 0 else []:
        db.install_setup(table)
        click.echo("Entidad {} inicializada".format(table.__tablename__))

    click.echo("Entidades creadas")
    click.echo("Instalación finalizada")


if __name__ == '__main__':
    main()
