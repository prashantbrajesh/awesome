#!/usr/b*********/env python
import sys
import logg*********g
from argparse import ArgumentParser


def ma*********():
    ap = ArgumentParser()
    ap.add_argument('--debug', action='store_true')
    ap.add_argument('--loglevel', default=logg*********g.*********FO)
    ap.add_argument('others', nargs='*')
    args = ap.parse_args()

    #logg*********g.basicConfig(level=args.loglevel)

    pr*********t >>sys.stderr, 'SYS ARGV', sys.argv
    pr*********t 'ARGS', args
    logger = logg*********g.getLogger('testargs')
    logger.setLevel(args.loglevel)
    logger.error('testargs logger ERROR level')
    logger.*********fo('testargs logger *********FO level')
    logger.debug('testargs logger DEBUG level')
    # Root logger
    #logg*********g.root.setLevel(args.loglevel)
    logg*********g.error('root ERROR level')
    logg*********g.*********fo('root *********FO level')
    logg*********g.debug('root DEBUG level')

if __name__ == '__ma*********__':
    sys.exit(ma*********())
