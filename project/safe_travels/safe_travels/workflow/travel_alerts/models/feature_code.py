#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types, Column

Base = declarative_base()


class FeatureCode(Base):
    __tablename__ = 'feature_code'

    code = Column(types.CHAR(50), index=True)
    name = Column(types.VARCHAR(200), primary_key=True, index=True)
    description = Column(types.Text, nullable=True)