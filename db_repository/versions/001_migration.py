from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
person = Table('person', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('booking_number', String(length=64)),
    Column('name', String(length=64)),
    Column('last_name', String(length=64)),
    Column('passport_number', String(length=64)),
    Column('delivery_needed', Boolean),
    Column('sex', String(length=7)),
    Column('address', String(length=40)),
    Column('citizenship', Integer),
    Column('birth_date', Date),
    Column('entry_date', Date),
    Column('exit_date', Date),
    Column('kids', String(length=64)),
    Column('transport', String(length=64)),
    Column('email', String(length=64)),
    Column('cities', String(length=64)),
    Column('if_double', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person'].columns['address'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person'].columns['address'].drop()
