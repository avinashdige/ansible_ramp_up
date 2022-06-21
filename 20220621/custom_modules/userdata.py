#!/usr/bin/python
try:
    import json
except Exception as e:
    import simplejson as json

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            age=dict(required=True, type='str'),
        )
    )
    name = module.params["name"]
    age = module.params["age"]
    
    data = dict(
        output="Your data has been stored successfully.",
    )
    # Successful exit
    try:
        file = open("/tmp/userdata.txt", "r")
        file.write(name+" , "+age+"\n")
        module.exit_json(changed=True, success=data, msg=data)
    except Exception as e:
        # Fail exit
        module.fail_json(msg="Something went wrong during writing userdata to file :( ")

if __name__ == "__main__":
    main()