#===============================================================================
# Copyright 2014 NetApp, Inc. All Rights Reserved,
# contribution by Jorge Mora <mora@netapp.com>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#===============================================================================
# Generated by process_xdr.py from nfs3.x on Sun Oct 04 08:09:27 2015
"""
NFSv3 constants module
"""
import nfstest_config as c

# Module constants
__author__    = "Jorge Mora (%s)" % c.NFSTEST_AUTHOR_EMAIL
__copyright__ = "Copyright (C) 2014 NetApp, Inc."
__license__   = "GPL v2"
__version__   = "3.0"

# Enum nfs_bool
FALSE = 0
TRUE  = 1

nfs_bool = {
    0 : "FALSE",
    1 : "TRUE",
}

# Sizes
NFS3_FHSIZE         = 64
NFS3_COOKIEVERFSIZE = 8
NFS3_CREATEVERFSIZE = 8
NFS3_WRITEVERFSIZE  = 8

# Enum nfsstat3
NFS3_OK             = 0
NFS3ERR_PERM        = 1
NFS3ERR_NOENT       = 2
NFS3ERR_IO          = 5
NFS3ERR_NXIO        = 6
NFS3ERR_ACCES       = 13
NFS3ERR_EXIST       = 17
NFS3ERR_XDEV        = 18
NFS3ERR_NODEV       = 19
NFS3ERR_NOTDIR      = 20
NFS3ERR_ISDIR       = 21
NFS3ERR_INVAL       = 22
NFS3ERR_FBIG        = 27
NFS3ERR_NOSPC       = 28
NFS3ERR_ROFS        = 30
NFS3ERR_MLINK       = 31
NFS3ERR_NAMETOOLONG = 63
NFS3ERR_NOTEMPTY    = 66
NFS3ERR_DQUOT       = 69
NFS3ERR_STALE       = 70
NFS3ERR_REMOTE      = 71
NFS3ERR_BADHANDLE   = 10001
NFS3ERR_NOT_SYNC    = 10002
NFS3ERR_BAD_COOKIE  = 10003
NFS3ERR_NOTSUPP     = 10004
NFS3ERR_TOOSMALL    = 10005
NFS3ERR_SERVERFAULT = 10006
NFS3ERR_BADTYPE     = 10007
NFS3ERR_JUKEBOX     = 10008

nfsstat3 = {
        0 : "NFS3_OK",
        1 : "NFS3ERR_PERM",
        2 : "NFS3ERR_NOENT",
        5 : "NFS3ERR_IO",
        6 : "NFS3ERR_NXIO",
       13 : "NFS3ERR_ACCES",
       17 : "NFS3ERR_EXIST",
       18 : "NFS3ERR_XDEV",
       19 : "NFS3ERR_NODEV",
       20 : "NFS3ERR_NOTDIR",
       21 : "NFS3ERR_ISDIR",
       22 : "NFS3ERR_INVAL",
       27 : "NFS3ERR_FBIG",
       28 : "NFS3ERR_NOSPC",
       30 : "NFS3ERR_ROFS",
       31 : "NFS3ERR_MLINK",
       63 : "NFS3ERR_NAMETOOLONG",
       66 : "NFS3ERR_NOTEMPTY",
       69 : "NFS3ERR_DQUOT",
       70 : "NFS3ERR_STALE",
       71 : "NFS3ERR_REMOTE",
    10001 : "NFS3ERR_BADHANDLE",
    10002 : "NFS3ERR_NOT_SYNC",
    10003 : "NFS3ERR_BAD_COOKIE",
    10004 : "NFS3ERR_NOTSUPP",
    10005 : "NFS3ERR_TOOSMALL",
    10006 : "NFS3ERR_SERVERFAULT",
    10007 : "NFS3ERR_BADTYPE",
    10008 : "NFS3ERR_JUKEBOX",
}

# Enum ftype3
NF3REG  = 1
NF3DIR  = 2
NF3BLK  = 3
NF3CHR  = 4
NF3LNK  = 5
NF3SOCK = 6
NF3FIFO = 7

ftype3 = {
    1 : "NF3REG",
    2 : "NF3DIR",
    3 : "NF3BLK",
    4 : "NF3CHR",
    5 : "NF3LNK",
    6 : "NF3SOCK",
    7 : "NF3FIFO",
}

# Enum time_how
DONT_CHANGE        = 0
SET_TO_SERVER_TIME = 1
SET_TO_CLIENT_TIME = 2

time_how = {
    0 : "DONT_CHANGE",
    1 : "SET_TO_SERVER_TIME",
    2 : "SET_TO_CLIENT_TIME",
}

# ACCESS3res NFSPROC3_ACCESS(ACCESS3args) = 4;
ACCESS3_READ    = 0x0001
ACCESS3_LOOKUP  = 0x0002
ACCESS3_MODIFY  = 0x0004
ACCESS3_EXTEND  = 0x0008
ACCESS3_DELETE  = 0x0010
ACCESS3_EXECUTE = 0x0020

# Enum stable_how
UNSTABLE  = 0
DATA_SYNC = 1
FILE_SYNC = 2

stable_how = {
    0 : "UNSTABLE",
    1 : "DATA_SYNC",
    2 : "FILE_SYNC",
}

# Enum createmode3
UNCHECKED = 0
GUARDED   = 1
EXCLUSIVE = 2

createmode3 = {
    0 : "UNCHECKED",
    1 : "GUARDED",
    2 : "EXCLUSIVE",
}

# FSINFO3res NFSPROC3_FSINFO(FSINFO3args) = 19;
FSF3_LINK        = 0x0001
FSF3_SYMLINK     = 0x0002
FSF3_HOMOGENEOUS = 0x0008
FSF3_CANSETTIME  = 0x0010

# Enum nfs_proc3
NFSPROC3_NULL        = 0
NFSPROC3_GETATTR     = 1
NFSPROC3_SETATTR     = 2
NFSPROC3_LOOKUP      = 3
NFSPROC3_ACCESS      = 4
NFSPROC3_READLINK    = 5
NFSPROC3_READ        = 6
NFSPROC3_WRITE       = 7
NFSPROC3_CREATE      = 8
NFSPROC3_MKDIR       = 9
NFSPROC3_SYMLINK     = 10
NFSPROC3_MKNOD       = 11
NFSPROC3_REMOVE      = 12
NFSPROC3_RMDIR       = 13
NFSPROC3_RENAME      = 14
NFSPROC3_LINK        = 15
NFSPROC3_READDIR     = 16
NFSPROC3_READDIRPLUS = 17
NFSPROC3_FSSTAT      = 18
NFSPROC3_FSINFO      = 19
NFSPROC3_PATHCONF    = 20
NFSPROC3_COMMIT      = 21

nfs_proc3 = {
     0 : "NFSPROC3_NULL",
     1 : "NFSPROC3_GETATTR",
     2 : "NFSPROC3_SETATTR",
     3 : "NFSPROC3_LOOKUP",
     4 : "NFSPROC3_ACCESS",
     5 : "NFSPROC3_READLINK",
     6 : "NFSPROC3_READ",
     7 : "NFSPROC3_WRITE",
     8 : "NFSPROC3_CREATE",
     9 : "NFSPROC3_MKDIR",
    10 : "NFSPROC3_SYMLINK",
    11 : "NFSPROC3_MKNOD",
    12 : "NFSPROC3_REMOVE",
    13 : "NFSPROC3_RMDIR",
    14 : "NFSPROC3_RENAME",
    15 : "NFSPROC3_LINK",
    16 : "NFSPROC3_READDIR",
    17 : "NFSPROC3_READDIRPLUS",
    18 : "NFSPROC3_FSSTAT",
    19 : "NFSPROC3_FSINFO",
    20 : "NFSPROC3_PATHCONF",
    21 : "NFSPROC3_COMMIT",
}
