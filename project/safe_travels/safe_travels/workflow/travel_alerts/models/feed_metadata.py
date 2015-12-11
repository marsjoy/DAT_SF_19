#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column, DateTime

Base = declarative_base()


class FeedMetadata(Base):
    __tablename__ = 'feed_metadata'

    title = Column(types.VARCHAR(200), index=True)
    subtitle = Column(types.VARCHAR(200), index=True)
    value = Column(types.VARCHAR(200), nullable=True, index=True)
    description = Column(types.Text, nullable=True)
    source = Column(types.VARCHAR(200), index=True)
    etag = Column(types.CHAR(50), nullable=True)
    feed_id = Column(types.VARCHAR(50), primary_key=True, index=True)
    created = Column(types.DateTime, index=True)
    modified = Column(types.DateTime, index=True)
