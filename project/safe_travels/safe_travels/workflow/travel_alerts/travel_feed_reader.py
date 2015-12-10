#!/usr/bin/env python
# -*- coding: utf-8 -*-
from safe_travels.utils.arguments import Arguments
from safe_travels.utils.strings import remove_escape_characters, parse_url, build_url_from_parts
from safe_travels.reader.feed_reader import FeedReader
from safe_travels.writer.csv_writer import save_rows
from bs4 import BeautifulSoup
from safe_travels.config.config import Config
import json
import arrow
import logging

logger = logging.getLogger(__name__)


class TravelFeedReader(object):

    def __init__(self,
                 feed_path=None,
                 metadata_path=None,
                 description=None):
        self.config = Config()
        self.source_data = self.config.path.get('source_data', None)
        self.process_date = arrow.now().format('YYYY_MM_DD')
        self.description = description
        self.reader = FeedReader(feed_path=feed_path)
        self.feed = self.reader.read_feed()
        self.metadata = metadata_path
        self.travel_feed = None

    def process(self):
        self.read_feed()
        self.read_feed_metadata(metadata_path=self.metadata)
        self.save_feed(
            feed=self.travel_feed['metadata'],
            field_names=['title', 'subtitle', 'value', 'description',
                         'source', 'etag', 'created', 'modified'],
            file='{source_data}/travel_{description}_feed_metadata_{date}.csv'.format(
                source_data=self.source_data,
                description=self.description,
                date=self.process_date,
            )
        )
        self.save_feed(
            feed=self.travel_feed['entries'],
            field_names=['id', 'title', 'published', 'dc_identifier',
                         'summary', 'links', 'created', 'modified'],
            file='{source_data}/travel_{description}_feed_entries_{date}.csv'.format(
                source_data=self.source_data,
                date=self.process_date,
                description=self.description,
            )
        )
        self.save_feed(
            feed=self.metadata,
            field_names=['identifier', 'title', 'description', 'published', 'publisher_name',
                         'source', 'bureau_code', 'start', 'end', 'modified'],
            file='{source_data}/travel_{description}_feed_{date}.csv'.format(
                source_data=self.source_data,
                date=self.process_date,
                description=self.description,
            )
        )

    def read_feed(self):
        travel_feed = dict()
        travel_feed['metadata'] = self.get_metadata()
        travel_feed['entries'] = self.get_parsed_entries(entries=self.feed['entries'])
        self.travel_feed = travel_feed

    def get_metadata(self):
        metadata = self.feed['metadata']
        metadata['created'] = arrow.now().format('YYYY-MM-DD HH:mm:ss')
        metadata['modified'] = arrow.now().format('YYYY-MM-DD HH:mm:ss')
        return [metadata]

    def get_parsed_entries(self, entries=None):
        parsed_entries = list()
        for entry in entries:
            parsed_entries.append(self.parse_entry(entry))
        return parsed_entries

    def parse_entry(self, entry=None):
        parsed_entry = dict()
        parsed_entry['id'] = entry.id
        parsed_entry['title'] = entry.title
        parsed_entry['published'] = arrow.get(entry.published_parsed).format('YYYY-MM-DD HH:mm:ss')
        parsed_entry['dc_identifier'] = entry.dc_identifier
        parsed_entry['summary'] = self.parse_summary_detail(summary_detail=entry.summary_detail)
        parsed_entry['links'] = self.get_parsed_summary_links(value=entry.summary_detail.value)
        parsed_entry['created'] = arrow.now().format('YYYY-MM-DD HH:mm:ss')
        parsed_entry['modified'] = arrow.now().format('YYYY-MM-DD HH:mm:ss')
        return parsed_entry

    def parse_summary_detail(self, summary_detail=None):
        parsed_summary = dict()
        parsed_summary['value'] = self.parse_summary_value(value=summary_detail.value)
        return parsed_summary

    def parse_summary_value(self, value=None):
        parsed_value = list()
        try:
            soup = BeautifulSoup(value, 'lxml')
            for p in soup.find_all('p'):
                if p.text:
                    parsed_value.append(
                        remove_escape_characters(value=p.text).strip()
                    )
            return '\n'.join(parsed_value)
        except Exception as e:
            logger.error('Not valid xml format', e)

    def get_parsed_summary_links(self, value=None):
        parsed_links = list()
        try:
            soup = BeautifulSoup(value, 'lxml')
            for a in soup.find_all('a'):
                link = dict()
                link['title'] = a.text.strip()
                link['link'] = self.parse_link(link=a['href'])
                parsed_links.append(link)
            return parsed_links
        except Exception as e:
            logger.error('Not valid xml format', e)

    def parse_link(self, link=None):
            parsed_link = parse_url(link).__dict__
            formatted_link = []
            if not parsed_link['scheme']:
                formatted_link.append('http')
            else:
                formatted_link.append(parsed_link['scheme'])
            if not parsed_link['netloc']:
                formatted_link.append('travel.state.gov')
            else:
                formatted_link.append(parsed_link['netloc'])
            formatted_link.extend([
                parsed_link['path'],
                parsed_link['params'],
                parsed_link['query'],
                parsed_link['fragment']
            ])
            return build_url_from_parts(formatted_link)

    def read_feed_metadata(self, metadata_path=None):
        with open(metadata_path) as metadata_json:
            metadata = json.loads(metadata_json.read())
            feed_metadata = dict()
            feed_metadata['title'] = metadata['title']
            feed_metadata['source'] = metadata['describedBy']
            feed_metadata['publisher_name'] = metadata['publisher']['name']
            feed_metadata['bureau_code'] = metadata['bureauCode']
            feed_metadata['start'], feed_metadata['end'] = self.parse_temporal(metadata['temporal'])
            feed_metadata['identifier'] = metadata['identifier']
            feed_metadata['modified'] = metadata['modified']
            feed_metadata['description'] = metadata['description']
            self.metadata = [feed_metadata]

    def parse_temporal(self, temporal=None):
        start = arrow.get(temporal.split('/')[0]).format('YYYY-MM-DD HH:mm:ss')
        try:
            end = arrow.get(temporal.split('/')[1]).format('YYYY-MM-DD HH:mm:ss')
        except:
            end = 'Null'
        return start, end

    def save_feed(self, file=None, feed=None, field_names=None):
        save_rows(file=file, rows=feed, field_names=field_names)
        pass

if __name__ == "__main__":
    args = Arguments(description='this script is for reading and writing'
                                 'travel feeds from travel.gov')
    args.add_argument('--feed_path',
                      help='The path is the path to your resource',
                      required=True,
                      )
    args.add_argument('--metadata_path',
                      help='The path is the path to your resource',
                      required=True,
                      )
    args.add_argument('--description',
                      help='The description describes the type of feed '
                           '(e.g., "alerts")',
                      required=True,
                      )
    feed_path = args.get('--feed_path', str())
    metadata_path = args.get('--metadata_path', str())
    description = args.get('--description', str())
    reader = TravelFeedReader(feed_path=feed_path,
                              metadata_path=metadata_path,
                              description=description
                              )
    reader.process()

