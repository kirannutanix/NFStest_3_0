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
# Generated by process_xdr.py from mount3.x on Sun Oct 04 08:09:27 2015
"""
MOUNTv3 constants module
"""
import nfstest_config as c

# Module constants
__author__    = "Jorge Mora (%s)" % c.NFSTEST_AUTHOR_EMAIL
__copyright__ = "Copyright (C) 2014 NetApp, Inc."
__license__   = "GPL v2"
__version__   = "3.0"

#
# Sizes
MNTPATHLEN = 1024  # Maximum bytes in a path name
MNTNAMLEN  = 255   # Maximum bytes in a name
FHSIZE3    = 64    # Maximum bytes in a V3 file handle

# Enum mountstat3
MNT3_OK             = 0      # no error
MNT3ERR_PERM        = 1      # Not owner
MNT3ERR_NOENT       = 2      # No such file or directory
MNT3ERR_IO          = 5      # I/O error
MNT3ERR_ACCES       = 13     # Permission denied
MNT3ERR_NOTDIR      = 20     # Not a directory
MNT3ERR_INVAL       = 22     # Invalid argument
MNT3ERR_NAMETOOLONG = 63     # Filename too long
MNT3ERR_NOTSUPP     = 10004  # Operation not supported
MNT3ERR_SERVERFAULT = 10006  # A failure on the server

mountstat3 = {
        0 : "MNT3_OK",
        1 : "MNT3ERR_PERM",
        2 : "MNT3ERR_NOENT",
        5 : "MNT3ERR_IO",
       13 : "MNT3ERR_ACCES",
       20 : "MNT3ERR_NOTDIR",
       22 : "MNT3ERR_INVAL",
       63 : "MNT3ERR_NAMETOOLONG",
    10004 : "MNT3ERR_NOTSUPP",
    10006 : "MNT3ERR_SERVERFAULT",
}

# Enum rpc_auth_flavors
AUTH_NULL      = 0
AUTH_UNIX      = 1
AUTH_SHORT     = 2
AUTH_DES       = 3
AUTH_KRB       = 4
AUTH_GSS       = 6
AUTH_MAXFLAVOR = 8
# pseudoflavors:
AUTH_GSS_KRB5  = 390003
AUTH_GSS_KRB5I = 390004
AUTH_GSS_KRB5P = 390005
AUTH_GSS_LKEY  = 390006
AUTH_GSS_LKEYI = 390007
AUTH_GSS_LKEYP = 390008
AUTH_GSS_SPKM  = 390009
AUTH_GSS_SPKMI = 390010
AUTH_GSS_SPKMP = 390011

rpc_auth_flavors = {
         0 : "AUTH_NULL",
         1 : "AUTH_UNIX",
         2 : "AUTH_SHORT",
         3 : "AUTH_DES",
         4 : "AUTH_KRB",
         6 : "AUTH_GSS",
         8 : "AUTH_MAXFLAVOR",
    390003 : "AUTH_GSS_KRB5",
    390004 : "AUTH_GSS_KRB5I",
    390005 : "AUTH_GSS_KRB5P",
    390006 : "AUTH_GSS_LKEY",
    390007 : "AUTH_GSS_LKEYI",
    390008 : "AUTH_GSS_LKEYP",
    390009 : "AUTH_GSS_SPKM",
    390010 : "AUTH_GSS_SPKMI",
    390011 : "AUTH_GSS_SPKMP",
}

# Enum mount_proc3
MOUNTPROC3_NULL    = 0
MOUNTPROC3_MNT     = 1
MOUNTPROC3_DUMP    = 2
MOUNTPROC3_UMNT    = 3
MOUNTPROC3_UMNTALL = 4
MOUNTPROC3_EXPORT  = 5

mount_proc3 = {
    0 : "MOUNTPROC3_NULL",
    1 : "MOUNTPROC3_MNT",
    2 : "MOUNTPROC3_DUMP",
    3 : "MOUNTPROC3_UMNT",
    4 : "MOUNTPROC3_UMNTALL",
    5 : "MOUNTPROC3_EXPORT",
}
