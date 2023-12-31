#!/usr/bin/env python

#PyNetHealthWatchCore is a simple client to test network speeds
#
# There are two scripts:
# PyNetHealthWatchLatency
# PyNetHealthWatchSpeed
# Author: ravagedshell <github.com/ravagedshell> <>

import argparse, argcomplete, os, PyNetHealthWatchCore,json
from re import L

PORT = 443

parser = argparse.ArgumentParser()
argcomplete.autocomplete(parser)

parser.add_argument('--hostname', help="Enter the IP or hostname of the location you would like to test.")
parser.add_argument('--hostfile', help="Enter a file path to import hosts to test.")
parser.add_argument('--output', help="Enter a file name to write the outputs to.")

args = parser.parse_args()

if args.hostfile is not None and os.path.exists(args.hostfile):
    hosts = open(args.hostfile, "r")
    results = []
    for host in hosts:
        hostname = host.rstrip('\n')
        if len(hostname) > 0:
            results.append(PyNetHealthWatchCore.tcpSockTest(hostname,PORT))

elif args.hostname is not None: 
    results = PyNetHealthWatchCore.tcpSockTest(args.hostname,PORT)

else:
    hosts = [
        "www.google.com",
        "www.github.com",
        "www.lumen.com",
        "www.slack.com",
        "www.microsoft.com"
    ]
    results = []
    for host in hosts:
        results.append(PyNetHealthWatchCore.tcpSockTest(host,PORT))

jsondata = json.dumps(results,indent=6)
if args.output is not None:
    f = open(args.output, "w")
    f.write(jsondata)
    print ('Wrote results to' + args.output)
else:
    print(jsondata)
