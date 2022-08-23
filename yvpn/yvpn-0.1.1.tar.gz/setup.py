# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yvpn']

package_data = \
{'': ['*']}

install_requires = \
['paramiko>=2.11.0,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['yvpn = yvpn.main:main']}

setup_kwargs = {
    'name': 'yvpn',
    'version': '0.1.1',
    'description': 'Command line tool to manage yvpn endpoints',
    'long_description': '# yvpn\n> A CLI client to manage YOUR vpn.\n\n## Overview\n\nThe yvpn tool is a command line client that allows users to manage VPN endpoints by communicating with the yourvpn.info service.  \n\nUsers can create, use, and destroy VPN endpoints at will.  These endpoints are Virtual Private Servers that are created for the exclusive use of the user unlike other VPN providers where thousands of users share a single endpoint.\n\nThis tool is meant to be extensible.  Beneath the hood SSH is used for the initial wireguard key exchange and future releases will allow users to quickly drop directly into a shell on the remote machine, perform file transfers, or remotely execute scripts.  \n\nThis is not just a a tool for managing your VPN needs, but also a powerful resource for quickly deploying on demand services limited only by your creativity.\n\n## Installation\n\nThe quickest way to get up and running is to install the tool from pip:\n\n`pip3 install yvpn`\n\nYou will need wireguard:\n\n(https://www.wireguard.com/install/)(https://www.wireguard.com/install/)\n\nYou need to set two environment variables:\n\n1. The server url:\n\t`URL_yVPN="https://yourvpn.info"`\n\n2. Your token:\n\t`TOKEN_yVPN="<token>"`\n\n## Where to get tokens\n\nRight now yvpn is in closed alpha.  Tokens are available by invitation only.\n\n## What even is a token?  Like an account?\n\nNo, we do not and will never offer accounts.  Privacy is a core principal and we figure the best way to preserve user\'s privacy is to simply store zero user information.  That\'s where Tokens come in.\n\nThink of a token as a sort of prepaid calling card.  Remember those good old days?  Where you\'d buy a calling card with however many minutes preloaded and then you had to call a 1-800 number from a payphone and enter the little code beneath the scratch off material?  That\'s what our token model will be.  \n\nOne day, once we\'re ready for a beta, there will be a simple storefront where you can buy a token preloaded with some amount of credit and off you go.\n\n## How will billing work then?\n\nThere will be no billing as in no invoicing.  Your token\'s fund balance will be debited based directly on usage.  If you don\'t have any endpoints running, you won\'t pay anything. \n\n## Overview of commands\n\n### `yvpn clean`\n\nDestroys all of your endpoints and refreshes your wireguard keys.\n\n### `yvpn connect`\n\nConnect to an endpoint.  You can pass the name or number of the endpoint to connect to a specific one, i.e. `yvpn connect 3`, or automatically connect to the first one on the list without.\n\n### `yvpn create`\n\nCreate a new endpoint.  You can optionally specify a specific datacenter, `yvpn create lon1`, see `yvpn datacenters` below, or create a new endpoint in a randomly selected datacenter by omitting the final argument.\n\n### `yvpn datacenters`\n\nDisplays a list of the currently available datacenters.  \n\n### `yvpn destroy <num>`\n\nDestroy the specified endpoint.\n\n### `yvpn disconnect`\n\nDisconnect from the active endpoint.\n\n### `yvpn status`\n\nDisplay a table of your endpoints with a number, name, location, and creation timestamp.  Also displays your token\'s balance and expected depletion date at current usage.\n\n',
    'author': 'Ben Simcox',
    'author_email': 'ben@bnsmcx.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
