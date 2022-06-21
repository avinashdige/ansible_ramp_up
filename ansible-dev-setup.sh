#!/bin/sh
git clone https://github.com/ansible/ansible.git
cd ansible
pip install virtualenv
# python3 -m venv venv
virtualenv -p python3 virtenv_38
# . venv/bin/activate
source ./virtenv_38/bin/activate
pip install -r requirements.txt
. hacking/env-setup

