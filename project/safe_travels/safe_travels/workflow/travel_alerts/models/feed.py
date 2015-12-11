#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column, Datetime, Date

Base = declarative_base()


class Feed(Base):
    __tablename__ = 'feed'

    identifier = Column(types.VARCHAR(50), primary_key=True, index=True)
    title = Column(types.VARCHAR(200), index=True)
    description = Column(types.Text, nullable=True)
    published = Column(types.CHAR(50), index=True)
    publisher_name = Column(types.VARCHAR(200), index=True)
    source = Column(types.VARCHAR(200), nullable=True)
    bureau_code = Column(types.CHAR(10))
    start = Column(types.Datetime, index=True)
    end = Column(types.Datetime, index=True)
    modified = Column(types.Date)
