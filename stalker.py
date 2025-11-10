#!/usr/bin/env python3
import argparse
from relicforge import RelicForge

def main():
    parser = argparse.ArgumentParser(description="Stalker: Relic-grade password generator by Hexr")
    subparsers = parser.add_subparsers(dest="command")

    gen = subparsers.add_parser("generate", help="Generate password lists")
    gen.add_argument("-n", type=int, required=True, help="Number of passwords")
    gen.add_argument("-len", nargs=2, type=int, required=True, help="Min and max length")
    gen.add_argument("--style", choices=["human", "random"], default="random", help="Choose password style")
    gen.add_argument("--info", type=str, help="Path to target info file (.txt)")

    args = parser.parse_args()

    if args.command == "generate":
        print(r"""
   _____ _        _    _
  / ____| |      | |  (_)
 | (___ | |_ __ _| | ___ _ __   __ _
  \___ \| __/ _` | |/ / | '_ \ / _` |
  ____) | || (_| |   <| | | | | (_| |
 |_____/ \__\__,_|_|\_\_|_| |_|\__, |
                                __/ |
                               |___/   by Hexr
        """)
        forge = RelicForge(info_file=args.info)
        forge.generate_passlists(args.n, tuple(args.len), style=args.style)
        forge.save_passlists("txt")
        print(f"[+] Generated {args.n} passwords with style '{args.style}' and saved to higher_chance_passlist.txt and general_passlist.txt")

if __name__ == "__main__":
    main()
