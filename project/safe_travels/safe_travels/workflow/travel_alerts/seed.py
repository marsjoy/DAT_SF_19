#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from safe_travels.config.config import Config
from safe_travels.workflow.base_workflow import BaseWorkflow

from safe_travels.workflow.travel_alerts.models.admin1_code import \
    Admin1Code
from safe_travels.workflow.travel_alerts.models.admin2_code import Admin2Code
from safe_travels.workflow.travel_alerts.models.alternate_name import \
    AlternateName
from safe_travels.workflow.travel_alerts.models.continent_code import \
    ContinentCode
from safe_travels.workflow.travel_alerts.models.country_info import CountryInfo
from safe_travels.workflow.travel_alerts.models.feature_code import FeatureCode
from safe_travels.workflow.travel_alerts.models.geoname import Geoname
from safe_travels.workflow.travel_alerts.models.hierarchy import Hierarchy
from safe_travels.workflow.travel_alerts.models.iso_language_code import \
    ISOLanguageCode
from safe_travels.workflow.travel_alerts.models.postal_code import PostalCode
from safe_travels.workflow.travel_alerts.models.time_zone import TimeZone
from sqlalchemy.ext.declarative import declarative_base


class GeonameDataLoader(BaseWorkflow):
    def __init__(self):
        super(GeonameDataLoader, self).__init__()
        self.config = Config()
        self.engine = self.create_engine()
        self.session = self.create_session(engine=self.engine)

    def create_engine(self):
        mysql = '{connector}://' \
                '{user}:{password}@{host}/' \
                '{database}?charset=utf8'.format(host=self.config.mysql.get('host', None),
                                                   connector=self.config.mysql.get('connector', None),
                                                   password=self.config.mysql.get('password', None),
                                                   database=self.config.mysql.get('database', None),
                                                   user=self.config.mysql.get('user', None),
                                                   port=self.config.mysql.get('port', None))
        engine = create_engine(mysql,
                               echo=True)
        return engine

    def create_session(self, engine=None):
        session = scoped_session(sessionmaker(bind=engine,
                                              autocommit = False,
                                              autoflush = False))
        return session()

    def process(self):
        self.clear_database()
        self.create_metadata()
        self.fill_tables()

    def clear_database(self):
        Base = declarative_base(self.engine)
        Base.metadata.drop_all()
        Base.metadata.clear()

    def create_metadata(self):
        Admin1Code().metadata.create_all(self.engine)
        Admin2Code().metadata.create_all(self.engine)
        AlternateName().metadata.create_all(self.engine)
        ContinentCode().metadata.create_all(self.engine)
        CountryInfo().metadata.create_all(self.engine)
        FeatureCode().metadata.create_all(self.engine)
        Geoname().metadata.create_all(self.engine)
        Hierarchy().metadata.create_all(self.engine)
        ISOLanguageCode().metadata.create_all(self.engine)
        PostalCode().metadata.create_all(self.engine)
        TimeZone().metadata.create_all(self.engine)

    def fill_tables(self):
        self.load_admin1_code(self.session)
        self.load_admin2_code(self.session)
        self.load_alternate_name(self.session)
        self.load_continent_code(self.session)
        self.load_country_info(self.session)
        self.load_feature_code(self.session)
        self.load_geoname(self.session)
        self.load_hierarchy(self.session)
        self.load_iso_language_code(self.session)
        self.load_postal_code(self.session)
        self.load_time_zone(self.session)

    def load_admin1_code(self, session):
        with open("{source_data_path}/admin1CodesASCII.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            reader = csv.reader(table_data, delimiter='\t')
            for row in reader:
                code, name, nameAscii, geonameid = row
                admin1_code = Admin1Code()
                admin1_code.code = code
                admin1_code.name = name
                admin1_code.name_ascii = nameAscii
                admin1_code.geoname_id = geonameid
                #adds user to session
                session.add(admin1_code)

        #commits session changes
        session.commit()

    def load_admin2_code(self, session):
        with open("{source_data_path}/admin2Codes.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            reader = csv.reader(table_data, delimiter='\t')
            for row in reader:
                code, name, name_ascii, geoname_id = row
                admin2_code = Admin2Code()
                admin2_code.code = code
                admin2_code.name = name
                admin2_code.name_ascii = name_ascii
                admin2_code.geoname_id = geoname_id
                #adds user to session
                session.add(admin2_code)

        #commits session changes
        session.commit()

    def load_alternate_name(self, session):
        with open("{source_data_path}/alternateNames.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            reader = csv.reader(table_data, delimiter='\t')
            for row in reader:
                alternate_name_id, geoname_id, iso_language, alternate_name, is_preferred_name, is_short_name, is_colloquial, is_historic = row
                alternate_name = AlternateName()
                alternate_name.alternate_name_id = alternate_name_id
                alternate_name.geoname_id = geoname_id
                alternate_name.iso_language = iso_language
                alternate_name.alternate_name = alternate_name
                alternate_name.is_preferred_name = is_preferred_name
                alternate_name.is_short_name = is_short_name
                alternate_name.is_colloquial = is_colloquial
                alternate_name.is_historic = is_historic
                #adds user to session
                session.add(alternate_name)

        #commits session changes
        session.commit()

    def load_continent_code(self, session):
        with open("{source_data_path}/continentCodes.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            reader = csv.reader(table_data, delimiter=',')
            for row in reader:
                code, name, geoname_id = row
                continent_code = ContinentCode()
                continent_code.code = code
                continent_code.name = name
                continent_code.geoname_id = geoname_id
                #adds user to session
                session.add(continent_code)

        #commits session changes
        session.commit()

    def load_country_info(self, session):
        with open("{source_data_path}/countryInfo.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            reader = csv.reader(table_data, delimiter='\t')
            for row in reader:
                iso_alpha2, iso_alpha3, iso_numeric, fips_code, \
                name, capital, area_in_sqkm, population, continent, tld, \
                currency, currency_name, phone, postal_code_format, postal_code_regex, \
                geoname_id, languages, neighbours, equivalent_fips_code = row
                country_info = CountryInfo()
                country_info.iso_alpha2 = iso_alpha2
                country_info.iso_alpha3 = iso_alpha3
                country_info.iso_numeric = iso_numeric
                country_info.fips_code = fips_code
                country_info.name = name
                country_info.capital = capital
                country_info.area_in_sqkm = area_in_sqkm
                country_info.population = population
                country_info.continent = continent
                country_info.tld =tld
                country_info.currency = currency
                country_info.currency_name = currency_name
                country_info.phone = phone
                country_info.postal_code_format = postal_code_format
                country_info.postal_code_regex = postal_code_regex
                country_info.geoname_id = geoname_id
                country_info.languages = languages
                country_info.neighbours = neighbours
                country_info.equivalent_fips_code = equivalent_fips_code
                #adds user to session
                session.add(country_info)

        #commits session changes
        session.commit()

    def load_feature_code(self, session):
        with open("{source_data_path}/featureCodes_en.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            reader = csv.reader(table_data, delimiter='\t')
            for row in reader:
                name, code, description = row
                feature_code = FeatureCode()
                feature_code.name = name
                feature_code.code = code
                feature_code.description = description
                #adds user to session
                session.add(feature_code)

        #commits session changes
        session.commit()

    def load_geoname(self, session):
        with open("{source_data_path}/geonames.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            csv.field_size_limit(sys.maxsize)
            reader = csv.reader(table_data, delimiter='\t')
            for row in reader:
                geoname_id, name, ascii_name, alternate_names, latitude, longitude, \
                fclass, fcode, country, cc2, admin1, admin2, admin3, admin4, \
                population, elevation, gtopo30, time_zone, mod_date = row
                geoname = Geoname()
                geoname.geoname_id = geoname
                geoname.name = name
                geoname.ascii_name = ascii_name
                geoname.alternate_names = alternate_names
                geoname.latitude = latitude
                geoname.longitude =longitude
                geoname.fclass = fclass
                geoname.fcode = fcode
                geoname.country = country
                geoname.cc2 = cc2
                geoname.admin1 = admin1
                geoname.admin2 = admin2
                geoname.admin3 = admin3
                geoname.admin4 = admin4
                geoname.population = population
                geoname.elevation = elevation
                geoname.gtopo30 = gtopo30
                geoname.time_zone = time_zone
                geoname.mod_date = mod_date
                #adds user to session
                session.add(geoname)

        #commits session changes
        session.commit()

    def load_hierarchy(self, session):
        with open("{source_data_path}/hierarchy.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            reader = csv.reader(table_data, delimiter='\t')
            for row in reader:
                parent_id, child_id, type = row
                hierarchy = Hierarchy()
                hierarchy.parent_id = parent_id
                hierarchy.child_id = child_id
                hierarchy.type = type
                #adds user to session
                session.add(hierarchy)

        #commits session changes
        session.commit()

    def load_iso_language_code(self, session):
        with open("{source_data_path}/iso-languagecodes.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            reader = csv.reader(table_data, delimiter='\t')
            for row in reader:
                iso_639_3, iso_639_2, iso_639_1, language_name = row
                iso_language_code = ISOLanguageCode()
                iso_language_code.iso_639_3 = iso_639_3
                iso_language_code.iso_639_2 = iso_639_2
                iso_language_code.iso_639_1 = iso_639_1
                iso_language_code.language_name = language_name
                #adds user to session
                session.add(iso_language_code)

        #commits session changes
        session.commit()

    def load_postal_code(self, session):
        with open("{source_data_path}/postalCodes.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            reader = csv.reader(table_data, delimiter='\t')
            for row in reader:
                print(row, len(row))
                country, postal_code, name, admin1_name, admin1_code, \
                admin2_name, admin2_code, admin3_name, admin3_code, latitude, longitude, accuracy= row
                postal_code = PostalCode()
                postal_code.country = country
                postal_code.postal_code = postal_code
                postal_code.name = name
                postal_code.admin1_name = admin1_name
                postal_code.admin1_code = admin1_code
                postal_code.admin2_name = admin2_name
                postal_code.admin2_code = admin2_code
                postal_code.admin3_name = admin3_name
                postal_code.admin3_code = admin3_code
                postal_code.latitude = latitude
                postal_code.longitude = longitude
                postal_code.accuracy = accuracy
                # adds user to session
                session.add(postal_code)

        #commits session changes
        session.commit()

    def load_time_zone(self, session):
        with open("{source_data_path}/timeZones.txt".format(
            source_data_path=self.source_data), "r") as table_data:
            reader = csv.reader(table_data, delimiter='\t')
            for row in reader:
                country_code, time_zone_id, gmt_offset, dst_offset, raw_offset = row
                time_zone = TimeZone()
                time_zone.country_code = country_code
                time_zone.time_zone_id = time_zone_id
                time_zone.gmt_offset = gmt_offset
                time_zone.dst_offset = dst_offset
                time_zone.raw_offset = raw_offset
                #adds user to session
                session.add(time_zone)

        #commits session changes
        session.commit()

if __name__ == "__main__":
    workflow = GeonameDataLoader()
    workflow.process()