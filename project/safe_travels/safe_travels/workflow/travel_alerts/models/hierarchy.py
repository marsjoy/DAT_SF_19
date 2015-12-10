#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column, PrimaryKeyConstraint

Base = declarative_base()


class Hierarchy(Base):
    __tablename__ = 'hierarchy'
    __table_args__ = (
        PrimaryKeyConstraint('parent_id', 'child_id', 'type'),
    )
    parent_id = Column(types.Integer, index=True)
    child_id = Column(types.Integer, index=True)
    type = Column(types.VARCHAR(50), index=True)
