#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column

Base = declarative_base()


class CountryInfo(Base):
    __tablename__ = 'country_info'

    iso_alpha2 = Column(types.CHAR(2), index=True, primary_key=True)
    iso_alpha3 = Column(types.CHAR(3), nullable=True, index=True)
    iso_numeric = Column(types.Integer, nullable=True, index=True)
    fips_code = Column(types.VARCHAR(3), nullable=True, index=True)
    name = Column(types.VARCHAR(200), nullable=True, index=True)
    capital = Column(types.VARCHAR(200), nullable=True)
    area_in_sqkm = Column(types.Integer, nullable=True)
    population = Column(types.Integer, nullable=True)
    continent = Column(types.CHAR(2), nullable=True)
    tld = Column(types.CHAR(3), nullable=True)
    currency = Column(types.CHAR(3), nullable=True)
    currency_name = Column(types.CHAR(20), nullable=True)
    phone = Column(types.CHAR(10), nullable=True)
    postal_code_format = Column(types.VARCHAR(100), nullable=True)
    postal_code_regex = Column(types.VARCHAR(255), nullable=True)
    geoname_id = Column(types.Integer, nullable=True)
    languages = Column(types.VARCHAR(200), nullable=True)
    neighbours = Column(types.CHAR(100), nullable=True)
    equivalent_fips_code = Column(types.CHAR(10), nullable=True)