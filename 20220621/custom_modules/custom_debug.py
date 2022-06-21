#!/usr/bin/python
try:
    import json
except Exception as e:
    import simplejson as json

from ansible.module_utils.basic import AnsibleModule
import time
import sys

def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg=dict(required=True, type='str')
        )
    )
    msg_var = module.params["msg"]
    # print(msg_var)
    # Successful exit
    try:
        # print(json.dumps({
        #     "msg": "%s - %s"%(time.strftime("%c"), msg_var),
        #     "changed": True
        # }))
        # sys.exit(0)
        msg_var = "%s - %s"%(time.strftime("%c"), msg_var)
        module.exit_json(changed=True, success=msg_var, msg=msg_var)
    except Exception as e:
        # Fail exit
        print(json.dumps({
            "failed": True,
            "msg": "Failed debug module"
        }))

if __name__ == "__main__":
    main()