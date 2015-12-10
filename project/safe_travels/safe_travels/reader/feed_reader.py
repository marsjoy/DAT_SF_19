#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
from safe_travels.config.config import Config
from safe_travels.utils.arguments import Arguments


class FeedReader(object):

    def __init__(self,
                 feed_path=None):
        self.config = Config()
        self.feed_path = feed_path
        self.raw_feed = self.get_feed()

    def get_feed(self):
        return feedparser.parse(self.feed_path)

    def get_feed_metadata(self):
        metadata = dict()
        metadata['title'] = self.raw_feed.feed.title
        metadata['subtitle'] = self.raw_feed.feed.subtitle
        metadata['description'] = self.raw_feed.feed.description
        metadata['etag'] = self.raw_feed.headers['ETag']
        metadata['source'] = self.raw_feed.feed.title_detail.base
        metadata['value'] = self.raw_feed.feed.title_detail.value
        return metadata

    def get_feed_entries(self):
        return self.raw_feed.entries

    def read_feed(self):
        feed = dict()
        feed['metadata'] = self.get_feed_metadata()
        feed['entries'] = self.get_feed_entries()
        return feed


if __name__ == "__main__":
    args = Arguments()
    args.add_argument('--feed')
    feed_source = args.get('feed', str())
    reader = FeedReader(feed_path='http://travel.state.gov/_res/rss/TWs.xml')
    feed = reader.read_feed()
