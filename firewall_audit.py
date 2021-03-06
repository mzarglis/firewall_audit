import argparse
import os
import re
import sys
import ipaddress


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

    if not (ARGS.source_host or ARGS.source_net or ARGS.source_obj):
        parser.error('One Source Option required -sh or -sn or -so')
        parser.print_help()
        sys.exit(0)
    if not (ARGS.dest_host or ARGS.dest_net or ARGS.dest_obj):
        parser.error('One Destination Option required -dh or -dn or -do')
        parser.print_help()
        sys.exit(0)



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


def ip_valid(ip):
    if ip == 'any':
        return False
    else:
        try:
            ipaddress.ip_address(ip)
            print("source ip valid")
            return True
        except ValueError:
            print("source ip invalid")
            return False
        except Exception as e:
            print(e)



def network_valid(network):
    if network == 'any':
        return False
    try:
        ipaddress.ip_network(network)
        print("source ip valid")
        return True
    except ValueError:
        print("source ip invalid")
        return False
    except Exception as e:
        print(e)



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
    if ARGS.source == 'any':
        re_source = ARGS.source_ip










    pattern = 'access-list ' + re_name + 'extended ' + re_permission + re_trans_proto + re_source

    return True


def main():



    print( find_firewalls(ARGS.path))






if __name__ == '__main__':
    main()



