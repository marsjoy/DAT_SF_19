#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column

Base = declarative_base()


class ISOLanguageCode(Base):
    __tablename__ = 'iso_language_code'

    iso_639_3 = Column(types.VARCHAR(50), nullable=True)
    iso_639_2 = Column(types.VARCHAR(50), nullable=True)
    iso_639_1 = Column(types.VARCHAR(200), primary_key=True)
    language_name = Column(types.VARCHAR(200), nullable=True)