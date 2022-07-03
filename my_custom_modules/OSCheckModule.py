#!/usr/bin/python
import pydevd_pycharm

try:
    import json
except ImportError:
    import simplejson as json

import os

DOCUMENTATION = '''
---
module: OSCheckModule
short_description: A custom module to check OS of target machine.
description:
        - A custom module to check OS of target machine.
options:
  os_name:
    description:
      - Name of OS to check
    required: true
'''

EXAMPLES = '''
# Example
module_name:
    os_name: Linux
'''


def main():
    module = AnsibleModule(
        argument_spec=dict(
            os_name=dict(required=True),
            # os_name2=dict(required=True),
        )
    )

    # Retreive parameters
    os_name = module.params['os_name']
    # os_name = module.params['os_name2']

    # Check for OS
    pydevd_pycharm.settrace('192.168.29.23', port=54654, stdoutToServer=True, stderrToServer=True)
    if os_name in os.uname():
        # Successfull Exit
        module.exit_json(changed=True, msg="OS Match")
    else:
        # Fail Exit
        module.fail_json(msg="OS Mismatch. OS =" + os.uname()[0])

# import sys
# sys.path += ['', '/home/osboxes/ansible_ramp_up/ansible/test/lib', '/home/osboxes/ansible_ramp_up/ansible/lib', '/home/osboxes/ansible_ramp_up/ansible/virtenv_38/lib/python38.zip', '/home/osboxes/ansible_ramp_up/ansible/virtenv_38/lib/python3.8', '/home/osboxes/ansible_ramp_up/ansible/virtenv_38/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8', '/home/osboxes/ansible_ramp_up/ansible/virtenv_38/lib/python3.8/site-packages', '/home/osboxes/.ansible/collections/']
from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    main()