#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column

Base = declarative_base()


class TimeZone(Base):
    __tablename__ = 'time_zone'

    country_code = Column(types.CHAR(2), index=True, primary_key=True)
    time_zone_id = Column(types.VARCHAR(200), primary_key=True)
    gmt_offset = Column(types.DECIMAL(3, 1), nullable=True)
    dst_offset = Column(types.DECIMAL(3, 1), nullable=True)
    raw_offset = Column(types.DECIMAL(3, 1), nullable=True)