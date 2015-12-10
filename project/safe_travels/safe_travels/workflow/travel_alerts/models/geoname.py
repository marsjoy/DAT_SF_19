#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column

Base = declarative_base()


class Geoname(Base):
    __tablename__ = 'geoname'

    geoname_id = Column(types.Integer, nullable=False, primary_key=True, index=True)
    name = Column(types.VARCHAR(200), nullable=True, index=True)
    ascii_name = Column(types.VARCHAR(200), nullable=True)
    alternate_names = Column(types.VARCHAR(4000), nullable=True)
    latitude = Column(types.DECIMAL(10, 7), nullable=True, index=True)
    longitude = Column(types.DECIMAL(10, 7), nullable=True, index=True)
    fclass = Column(types.CHAR(1), nullable=True, index=True)
    fcode = Column(types.VARCHAR(10), nullable=True, index=True)
    country = Column(types.VARCHAR(2), nullable=True, index=True)
    cc2 = Column(types.VARCHAR(60), nullable=True, index=True)
    admin1 = Column(types.VARCHAR(20), nullable=True, index=True)
    admin2 = Column(types.VARCHAR(20), nullable=True)
    admin3 = Column(types.VARCHAR(20), nullable=True)
    admin4 = Column(types.VARCHAR(20), nullable=True)
    population = Column(types.Integer, nullable=True, index=True)
    elevation = Column(types.Integer, nullable=True, index=True)
    gtopo30 = Column(types.Integer, nullable=True, index=True)
    time_zone = Column(types.VARCHAR(40), nullable=True)
    mod_date = Column(types.Date, nullable=True)
