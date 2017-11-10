#!/usr/bin/env python

"""
./ctcf.py <ctcf_peaks.tsv> <Nora_Primers.bed>
"""

import numpy as np
import sys

def hifivedata():
    data = np.load('noraenr.heat.npz')
    return data['0.forward'], data['0.reverse'], data['0.enrichment']

def ctcfbinding():
    ctcf = []
    for line in open(sys.argv[1]):
        line = line.rstrip('\r\n').split('\t')
        if line[0] == 'chrX':
            ctcf.append(line[1])
    return ctcf
    
def primerdic():
    primer = {}
    for line in open(sys.argv[2]):
        line = line.rstrip('\r\n').split('\t')
        if line[0] == '#chr':
            pass
        else:
            primer[line[1] + '_' + line[2]] = line[3]
    return primer

def ctcfindex(primers, ctcf):
    index = []
    for i, each in enumerate(primers):
        start, stop = int(each[0]), int(each[1])
        for site in ctcf:
            if int(site) >= start and int(site) <= stop:
                index.append(i)
                break
    return index

def pairs(fwd, rev, enr):
    fwdpairs, revpairs = [], []
    for f in fwd:
        toprev, top = None, 0.
        for r in rev:
            if float(enr[f][r]) > top:
                toprev = r
                top = float(enr[f][r])
        fwdpairs.append((f,toprev))
    for r in rev:
        topfor, top = None, 0.
        for f in fwd:
            if float(enr[f][r]) > top:
                topfor = f
                top = float(enr[f][r])
        revpairs.append((topfor, r))
    return fwdpairs, revpairs

def nameixns(f, r, pairs, primer, direction):
    for ixn in pairs:
        fwkey = str(f[ixn[0]][0]) + '_' + str(f[ixn[0]][1])
        rvkey = str(r[ixn[1]][0]) + '_' + str(r[ixn[1]][1])
        if direction == 'fwd':
            print '%s\t%s' % (primer[fwkey], primer[rvkey])
        else:
            print '%s\t%s' % (primer[rvkey], primer[fwkey])
def main():
    ## load in all data
    ctcf = ctcfbinding()
    f, r, enr = hifivedata()
    primer = primerdic()
    ## get indices of ctcf binding sites in hifive data
    fwd, rev = ctcfindex(f, ctcf), ctcfindex(r, ctcf)
    ## find top interacting ctcf pairs
    fwdpairs, revpairs = pairs(fwd, rev, enr)
    ## map top interactions to primer names
    print 'Top interactions with forward primers:'
    nameixns(f, r, fwdpairs, primer, 'fwd' )
    print '\nTop interactions with reverse primers:'
    nameixns(f, r, revpairs, primer, 'rev' )
        
main()