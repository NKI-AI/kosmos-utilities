"""Console script for kosmos_utilities."""
import argparse
import sys
from fabric import Connection, Config
import getpass

def main():
    """Console script for kosmos_utilities."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')

    parser.add_argument('--project', '-p', type=str, help='Project name')
    parser.add_argument('--user', '-u', type=str, help='User name')
    parser.add_argument('--group', '-g', type=str, help='User group')
    parser.add_argument('--quota', '-q', type=str, help='Project quota')
    parser.add_argument('--chmod', '-c', type=str, help='Project chmod')

    args = parser.parse_args()

    commands = []

    if not args.project:
        args.project = input("Project name: ")
        if not args.project:
            print("Please provide a project name.")
            sys.exit(1)
        commands.append(f"zfs create project-pool/project/{args.project}")

    if not args.user:
        args.user = input("User name (default=root): ")
        # TODO: Check if user exists
        if not args.user:
            args.user = "root"

    if not args.group:
        args.group = input(f"Group name (default={args.user}): ")

    if not args.chmod:
        args.chmod = input("Chmod (default=750): ")
        if not args.chmod:
            args.chmod = "750"

    commands.append(f"chmod {args.chmod} /project-pool/project/{args.project}")
    commands.append(f"chown {args.user}:{args.group} /project-pool/project/{args.project}")

    if not args.quota:
        args.quota = input("Please provide a quota (default=100G): ")
        if not args.quota:
            args.quota = "100G"

    commands.append(f"zfs set quota={args.quota} /project-pool/project/{args.project}")

    # sudo_pass = getpass.getpass("Password for sudo on teuwen-ansible: ")
    # config = Config(overrides={'sudo': {'password': sudo_pass}})
    #
    # c = Connection(
    #     host="teuwen-ansible",
    #     config=config,
    # )
    print(" && ".join(commands))
    
    # c.run(" && ".join(commands), echo=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
