

import sys
import argparse

def parser():

    parser = argparse.ArgumentParser(
        description="Search firewall configs for certain rules"
    )
    parser.add_argument(
        '-p',
        '--path',
        dest='path',
        type=str,
        required=True,
        help="path to folder containing config text files"
    )

    parser.add_argument(
        '-a',
        '--acl-name',
        dest='acl_name',
        type=str,
        required=False,
        const='all',
        nargs='?',
        help="Specify ACL (default all acl's searched)"
    )

    parser.add_argument(
        '-x',
        '--permission',
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
        '--trans-protocol',
        dest='trans_proto',
        choices=['tcp', 'udp', 'icmp','ip','any'],
        type=str,
        required=False,
        const='any',
        nargs='?',
        help="Specify Transport protocol (default any)"
    )

    parser.add_argument(
        '-sh',
        '--source-host',
        dest='source_host',
        type=str,
        required=False,
        nargs='?',
        help="source ip address (single host address)"
    )

    parser.add_argument(
        '-sn',
        '--source-network',
        dest='source_net',
        type=str,
        required=False,
        nargs='?',
        help='Source Network (CIDR notation eg 192.68.2.0/24'
    )

    parser.add_argument(
        '-so',
        '--source-object',
        dest='source_obj',
        type=str,
        required=False,
        nargs='?',
        help='Source Object Group Name or any'
    )

    parser.add_argument(
        '-sp',
        '--source-port',
        dest='source_port',
        type=str,
        required=False,
        const='',
        nargs='?',
        help="source port (default any)"
    )

    parser.add_argument(
        '-dh',
        '--dest-host',
        dest='dest_host',
        type=str,
        required=False,
        nargs='?',
        help="source ip address (single host address eg: 192.168.2.1)"
    )

    parser.add_argument(
        '-dn',
        '--dest-net',
        dest='dest_net',
        type=str,
        required=False,
        nargs='?',
        help="Destination Network (CIDR notation eg: 192.68.2.0/24)"
    )

    parser.add_argument(
        '-do',
        '--dest-object',
        dest='dest_obj',
        type=str,
        required=False,
        nargs='?',
        help="Destination Object Group Name or any"
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

    args = parser.parse_args()

    # Must Have one and only 1 source option
    if args.source_host is None and args.source_net is None and args.source_obj is None:
        parser.error('One Source Option required (-sh -sn -so)')
        sys.exit(-1)
    if args.source_host is None and args.source_net is not None and args.source_obj is not None:
        parser.error('Only One Source Option Can be specified')
        sys.exit(-1)
    if args.source_host is not None and args.source_net is not None and args.source_obj is None:
        parser.error('Only One Source Option Can be specified')
        sys.exit(-1)
    if args.source_host is not None and args.source_net is None and args.source_obj is not None:
        parser.error('Only One Source Option Can be specified')
        sys.exit(-1)
    if args.source_host is not None and args.source_net is not None and args.source_obj is not None:
        parser.error('Only One Source Option Can be specified')
        sys.exit(-1)

    # Must have one and only 1 dest option
    if args.dest_host is None and args.est_net is None and args.est_obj is None:
        parser.error('One Source Option required (-sh -sn -so)')
        sys.exit(-1)
    if args.dest_host is None and args.dest_net is not None and args.dest_obj is not None:
        parser.error('Only One Source Option Can be specified')
        sys.exit(-1)
    if args.dest_host is not None and args.dest_net is not None and args.dest_obj is None:
        parser.error('Only One Source Option Can be specified')
        sys.exit(-1)
    if args.dest_host is not None and args.dest_net is None and args.dest_obj is not None:
        parser.error('Only One Source Option Can be specified')
        sys.exit(-1)
    if args.dest_host is not None and args.dest_net is not None and args.dest_obj is not None:
        parser.error('Only One Source Option Can be specified')
        sys.exit(-1)




    return args



ARGS = parser()




def main():

    if ARGS.source_host:
        print('a')
    else:
        print('b')

    if ARGS.source_net:
        print('aa')
    else:
        print('bb')
    print(ARGS.source_net)
    print(ARGS.source_obj)




main()

