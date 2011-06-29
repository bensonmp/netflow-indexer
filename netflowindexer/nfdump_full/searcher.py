import datetime
import sys
import os

from netflowindexer.nfdump.searcher import NFDUMPSearcher

class NFDUMPFullSearcher(NFDUMPSearcher):
    def docid_to_date(self, fn):
        """turn /data/nfsen/profiles/live/podium/nfcapd.200903011020 into
        a date of 2009-03-01 10:20"""
        t = fn[-12:]
        return datetime.datetime.strptime(t,'%Y%m%d%H%M')

    def show(self, doc, filter, mode=None):
        pipe = ""
        if mode=="pipe":
            pipe = "-o pipe"
        for line in os.popen("nfdump %s %s -q -r %s '%s'"  % (self.ipv6_flag, pipe, doc, filter)):
            yield line.rstrip()

searcher_class = NFDUMPFullSearcher
