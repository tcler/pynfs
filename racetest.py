#!/usr/bin/env python

import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], 'lib'))
import rpc
from nfs4.nfs4lib import NFS4Client
from nfs4.nfs4_const import *

c = NFS4Client('tester', host='rhel5')

c = env.c1
basedir = c.homedir + [t.code]
c.maketree([t.code, ['TRACEME_dir', ['foo']]])
parent = do_getfh(c.homedir + [t.code])
dir = do_getfh(c.homedir + [t.code, 'TRACEME_dir'])
file = do_getfh(c.homedir + [t.code, 'TRACEME_dir', 'foo'])
res = os.fork();
if res == 0:
    ops = [c.putfh_op(parent), c.remove_op('TRACEME')]
    res = c.compound(ops)
    os._exit(0)
    sleep(.5)
res = os.fork()
if res == 0:
    ops = [c.putfh_op(dir), c.savefh_op]
    ops += [c.putfh_op(dir), c.rename_op('foo', 'TRACEME_foo')]
    res = c.compound(ops)
    os._exit(0)
ops = [c.putfh_op(parent), c.lookup_op('TRACEME_foo')]
