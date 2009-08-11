#-----------------------------------------------------------------------------
#   Copyright (c) 2008-2009, David P. D. Moss. All rights reserved.
#
#   Released under the BSD license. See the LICENSE file for details.
#-----------------------------------------------------------------------------
"""A Python library for manipulating IP and EUI network addresses."""

import sys as _sys

if _sys.version_info[0:2] < (2, 4):
    raise RuntimeError('Python 2.4.x or higher is required!')

__version__ = '0.7'

from netaddr.core import AddrConversionError, AddrFormatError, \
    NotRegisteredError

from netaddr.ip import IPAddress, IPNetwork, IPRange, all_matching_cidrs, \
    cidr_abbrev_to_verbose, cidr_exclude, cidr_merge, iprange_to_cidrs, \
    iter_iprange, iter_unique_ips, largest_matching_cidr, \
    smallest_matching_cidr, spanning_cidr

from netaddr.ip.sets import IPSet

from netaddr.ip.glob import IPGlob, cidr_to_glob, glob_to_cidrs, \
    glob_to_iprange, glob_to_iptuple, iprange_to_globs, valid_glob

from netaddr.ip.rfc1924 import base85_to_ipv6, ipv6_to_base85

from netaddr.eui import EUI, IAB, OUI

from netaddr.strategy.ipv4 import valid_str as valid_ipv4

from netaddr.strategy.ipv6 import valid_str as valid_ipv6, ipv6_compact, \
    ipv6_full, ipv6_verbose

from netaddr.strategy.eui48 import mac_eui48, mac_unix, mac_cisco, \
    mac_bare, mac_pgsql, valid_str as valid_mac

__all__ = [
    #   Custom Exceptions.
    'AddrConversionError', 'AddrFormatError', 'NotRegisteredError',

    #   IP classes.
    'IPAddress', 'IPNetwork', 'IPRange', 'IPSet',

    #   IPv6 dialect classes.
    'ipv6_compact', 'ipv6_full', 'ipv6_verbose',

    #   IP functions and generators.
    'all_matching_cidrs', 'cidr_abbrev_to_verbose', 'cidr_exclude',
    'cidr_merge', 'iprange_to_cidrs', 'iter_iprange', 'iter_unique_ips',
    'largest_matching_cidr', 'smallest_matching_cidr', 'spanning_cidr',

    #   IP globbing class.
    'IPGlob',

    #   IP globbing functions.
    'cidr_to_glob', 'glob_to_cidrs', 'glob_to_iprange', 'glob_to_iptuple',
    'iprange_to_globs',

    #   IEEE EUI classes.
    'EUI', 'IAB', 'OUI',

    #   EUI-48 (MAC) dialect classes.
    'mac_bare', 'mac_cisco', 'mac_eui48', 'mac_pgsql', 'mac_unix',

    #   Validation functions.
    'valid_ipv4', 'valid_ipv6', 'valid_glob', 'valid_mac',

    #   RFC 1924 functions.
    'base85_to_ipv6', 'ipv6_to_base85',
]
