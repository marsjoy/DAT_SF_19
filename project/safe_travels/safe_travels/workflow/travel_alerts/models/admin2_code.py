#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column, Index

Base = declarative_base()


class Admin2Code(Base):
    __tablename__ = 'admin2_code'
    table_args__ = (
            Index('name', 'name_ascii', mysql_length=200))

    code = Column(types.CHAR(30), index=True, primary_key=True)
    name = Column(types.Text, nullable=True)
    name_ascii = Column(types.Text, nullable=True)
    geoname_id = Column(types.Integer, nullable=True)