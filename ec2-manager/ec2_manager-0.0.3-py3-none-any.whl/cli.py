import os
import sys
import click
import boto3
import time
from ec2_manager import EC2Manager
from importlib.machinery import SourceFileLoader

config = click.option(
    '--config',
    default=os.environ.get('EC2_MANAGER_CONFIG', 'config.yaml'),
    help='Path to config file.',
    required=True
)
repo = click.option(
    '--repo',
    default=os.environ.get('REPO'),
    help='The name of the repo i.e. "Hello-World"',
    required=True
)
github_username = click.option(
    '--github-username',
    default=os.environ.get('GITHUB_USERNAME'),
    help='Your github username i.e. "octocat"',
    required=True
)
github_token = click.option(
    '--github-token',
    default=os.environ.get('GITHUB_TOKEN'),
    help='A github personal access token that has permission to pull the repo',
    required=True
)
subclass_file = click.option(
    '--subclass-file',
    default=None,
    help='Path to the python file that subclasses the base EC2Manager class.'
)
subclass_name = click.option(
    '--subclass-name',
    default=None,
    help='The name of the subclass of EC2Manager.'
)


def get_class(**kwargs):
    config_file = kwargs.get('config')
    file_path = kwargs.get('subclass_file')
    class_name = kwargs.get('subclass_name')

    if not os.path.exists(config_file):
        raise click.UsageError(f'The config file "{config_file}" was not found.')
    if not class_name or not file_path:
        return EC2Manager
    if not os.path.exists(file_path):
        raise click.UsageError(f'The subclass file {file_path} was not found on disk.')

    subclass_module = SourceFileLoader("subclass_module", file_path).load_module()
    return getattr(subclass_module, class_name)


@click.group(name='ec2-manager')
def cli():
    pass


@click.command()
def init():
    if click.confirm(f'Continue setting up project in this folder {os.getcwd()}'):
        # setup local project on disk
        ec2_manager = EC2Manager()
        ec2_manager.init()


@click.command()
@repo
@github_username
@github_token
def set_secrets(**kwargs):
    repo_name = kwargs.get('repo')
    username = kwargs.get('github_username')

    secrets = {}
    ec2_manager = EC2Manager(**kwargs)
    repo_instance = ec2_manager.get_repo()

    if click.confirm(
            f'Do you want to update your AWS credentials?'
    ):
        user_session = boto3.session.Session()
        user_credentials = user_session.get_credentials()

        time.sleep(0.1)
        print()
        secrets['AWS_REGION'] = click.prompt(
            'Please enter your AWS_REGION',
            default=user_session.region_name
        )
        secrets['AWS_ACCESS_KEY_ID'] = click.prompt(
            'Please enter your AWS_ACCESS_KEY [********************]',
            default=user_credentials.access_key,
            show_default=False
        )
        secrets['AWS_SECRET_ACCESS_KEY'] = click.prompt(
            'Please enter your AWS_SECRET_KEY [****************************************]',
            default=user_credentials.secret_key,
            show_default=False
        )

    if click.confirm(
      f'Do you want to update your encoded env file?'
    ):
        while True:
            key_name = click.prompt(
                'Please enter the env file secret name',
                default='ENV_FILE'
            )
            default_file_path = os.path.join(os.getcwd(), 'compose', '.env')
            env_file_path = click.prompt(
                'Please enter the local env file path',
                default=default_file_path if os.path.exists(default_file_path) else None
            )
            if not os.path.exists(env_file_path):
                click.echo(f'There was no env file found on disk at "{env_file_path}"!')
                continue

            # read the env file and encode it
            with open(env_file_path, 'r') as env_file:
                secrets[key_name] = EC2Manager.encode_string(env_file.read())

            if click.confirm(f'Do you want to add another env file?'):
                continue
            else:
                break

    if secrets:
        if click.confirm(
                f'Do you want to set these secrets {list(secrets.keys())} on the repo f"{username}/{repo_name}"?'
        ):
            for key, value in secrets.items():
                click.echo(f'Setting {key} on {username}/{repo_name}...')
                repo_instance.create_secret(key, value)


@click.command()
@config
@repo
@github_username
@github_token
@subclass_file
@subclass_name
def apply(**kwargs):
    ec2_manager = get_class(**kwargs)()
    ec2_manager.apply()


def main():
    cli.add_command(init)
    cli.add_command(apply)
    cli.add_command(set_secrets)
    cli()


if __name__ == '__main__':
    sys.exit(main())
