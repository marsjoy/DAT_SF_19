#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column

Base = declarative_base()


class ContinentCode(Base):
    __tablename__ = 'continent_code'

    code = Column(types.CHAR(2), index=True, primary_key=True)
    name = Column(types.VARCHAR(20), nullable=True, index=True)
    geoname_id = Column(types.Integer, nullable=True, index=True)