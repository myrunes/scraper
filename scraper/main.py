#!/usr/bin/python3

import sys
import argparse

import rest
import champs
import avatars


COMMANDS = {
    'champs': champs.exec,
    'avatars': avatars.exec,
}


VERSION_API_URL = 'https://ddragon.leagueoflegends.com/api/versions.json'


def get_patches():
    versions = rest.get_json(VERSION_API_URL)
    return versions


def parse_args():
    patches = get_patches()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--output', '-o', help='Output location', type=str, default='./output')
    parser.add_argument(
        '--patch', '-p', help='League of Legends patch', type=str,
        choices=patches[:10], default=patches[0])
    subcmds = parser.add_subparsers(dest='subcmd', help='sub commands')

    # champs subcommand
    subcmds.add_parser('champs')
    s_avatars = subcmds.add_parser('avatars')
    s_avatars.add_argument(
        '--champions', '-c',
        help='Comma seperated list of champions to fetch avatars from.', type=str)

    args = parser.parse_args()

    if args.subcmd is None:
        parser.print_help()
        sys.exit(1)

    return args


def main():
    args = parse_args()
    COMMANDS[args.subcmd](args)
    return 0


if __name__ == '__main__':
    sys.exit(main())
