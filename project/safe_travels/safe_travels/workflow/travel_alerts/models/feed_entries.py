#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column, Datetime

Base = declarative_base()


class FeedEntries(Base):
    __tablename__ = 'feed_entries'

    id = Column(types.CHAR(50), primary_key=True, index=True)
    title = Column(types.VARCHAR(200), index=True)
    published = Column(types.Datetime, index=True)
    dc_identifier = Column(types.CHAR(2), index=True)
    summary = Column(types.Text, index=True)
    links = Column(types.Text, nullable=True)
    created = Column(types.Datetime, index=True)
    modified = Column(types.Datetime, index=True)
