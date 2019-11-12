import GEOparse
import sys # to access command line arguments
import json # used to read JSON from eSearch/eSummary/eFetch requests
import urllib.request # used to read JSON from eSearch/eSummary/eFetch requests
print("python script")
print("reading file")
accIDs=list()
dir = "/data/GEO_DL"
print(sys.argv[1])
with open(sys.argv[1]) as fp:
    line = fp.readline()
    while line:
        accIDs.append(line.rstrip())
        line = fp.readline()

# accIDs = " ".join(sys.argv[1:])
for acc_num in accIDs:
    print(acc_num)
    gse = GEOparse.get_GEO(geo=acc_num, destdir=dir)

# for acc_num in acc_nums:
#     ds = GEOparse.get_GEO(geo=acc_num, destdir="./")