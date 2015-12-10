#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column

Base = declarative_base()


class AlternateName(Base):
    __tablename__ = 'alternate_name'

    alternate_name_id = Column(types.Integer, nullable=False, primary_key=True, index=True)
    geoname_id = Column(types.Integer, nullable=True, index=True)
    iso_language = Column(types.VARCHAR(7), nullable=True, index=True)
    alternate_name = Column(types.VARCHAR(200), nullable=True, index=True)
    is_preferred_name = Column(types.Boolean, nullable=True)
    is_short_name = Column(types.Boolean, nullable=True)
    is_colloquial = Column(types.Boolean, nullable=True)
    is_historic = Column(types.Boolean, nullable=True)
