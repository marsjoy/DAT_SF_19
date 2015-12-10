#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column

Base = declarative_base()

class PostalCode(Base):
    __tablename__ = 'postal_code'

    country = Column(types.CHAR(2), nullable=True, index=True)
    postal_code = Column(types.VARCHAR(20), index=True, primary_key=True)
    name = Column(types.VARCHAR(180), nullable=True, index=True)
    admin1_name = Column(types.VARCHAR(100), nullable=True, index=True)
    admin1_code = Column(types.VARCHAR(20), nullable=True, index=True)
    admin2_name = Column(types.VARCHAR(100), nullable=True)
    admin2_code = Column(types.VARCHAR(20), nullable=True)
    admin3_name = Column(types.VARCHAR(100), nullable=True)
    admin3_code = Column(types.VARCHAR(20), nullable=True)
    latitude = Column(types.DECIMAL(10, 7), nullable=True, index=True)
    longitude = Column(types.DECIMAL(10, 7), nullable=True, index=True)
    accuracy = Column(types.Boolean, nullable=True)

