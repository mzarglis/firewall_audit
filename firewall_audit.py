import argparse
import os
import re


def parser():
    parser = argparse.ArgumentParser(
        description="Search firewall configs for certain rules"
    )
    parser.add_argument(
        '-p',
        '--p',
        dest='path',
        type=str,
        required=True,
        help="path to folder containing config text files"
    )

    parser.add_argument(
        '-a',
        '--a',
        dest='acl_name',
        type=str,
        required=False,
        const='all',
        nargs='?',
        help="Specify ACL (default all acl's searched)"
    )

    parser.add_argument(
        '-x',
        '--x',
        dest='permission',
        choices=['permit','deny','either'],
        type=str,
        required=False,
        const='either',
        nargs='?',
        help="Specify Rule permitting or denying (default either)"
    )


    parser.add_argument(
        '-t',
        '--t',
        dest='trans_proto',
        choices=['tcp', 'udp', 'icmp','ip','any'],
        type=str,
        required=False,
        const='any',
        nargs='?',
        help="Specify Transport protocol (default any)"
    )

    parser.add_argument(
        '-s',
        '--s',
        dest='source_ip',
        type=str,
        required=False,
        const='any4',
        nargs='?',
        help="source ip address / network  (default any4)"
    )
    parser.add_argument(
        '-sp',
        '--sp',
        dest='source_port',
        type=str,
        required=False,
        const='',
        nargs='?',
        help="source port (default any)"
    )

    parser.add_argument(
        '-d',
        '--d',
        dest='dest_ip',
        type=str,
        required=False,
        const='any4',
        nargs='?',
        help="destination ip / network (default any4)"
    )

    parser.add_argument(
        '-dp',
        '--dp',
        dest='dest_port',
        type=str,
        required=False,
        const='',
        nargs='?',
        help="destination port (default any)"
    )

    return parser.parse_args()

ARGS = parser()

# iterates through all config files and finds which ones are firewalls
# returns dictionary of firewalls
def find_firewalls(path):
    dict = {}
    for filename in os.listdir(path):
        if filename.endswith(".cfg"):
            with open(os.path.join(path, filename)) as file:
                for line in file:
                    if "hostname fw" in line:
                        dict[str(filename)] = [line.rstrip().replace('hostname ', '')]

    return dict


def make_search_pattern():

    #acl name pattern
    if ARGS.acl_name == 'all':
        re_name = '[\w]*\s'
    else:
        re_name = ARGS.acl_name + " "

    #permit deny pattern
    if ARGS.permission == 'permit ':
        re_permission = ARGS.permission
    elif ARGS.permission == 'deny ':
        re_permission = ARGS.permission
    else:
        re_permission = '(permit|deny)\s'

    #Transport protocol pattern
    if ARGS.trans_proto == 'any':
        re_trans_proto = '(tcp|ip|icmp|udp)\s'
    else:
        re_trans_proto = ARGS.trans_protol

    #source ip pattern












    pattern = 'access-list ' + re_name + 'extended ' + re_permission + re_trans_proto

    return True


def main():


    print( find_firewalls(ARGS.path))






if __name__ == '__main__':
    main()



