#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) 2019 Baptiste Agasse
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: foreman_config_group
short_description: Manage (Puppet) config groups using Foreman API
description:
  - Create and Delete Foreman (Puppet) config groups using Foreman API
author:
  - "Baptiste Agasse (@bagasse)"
options:
  name:
    description: The config group name
    required: true
    type: str
  updated_name:
    description: New config group name. When this parameter is set, the module will not be idempotent.
    type: str
  puppetclasses:
    description: List of puppet classes to include in this group
    required: false
    type: list
extends_documentation_fragment:
  - foreman
  - foreman.entity_state
'''

EXAMPLES = '''
- name: create new config group
  foreman_config_group:
    name: "My config group"
    puppetclasses:
      - ntp
      - mymodule::myclass
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "secret"
    state: present
'''

RETURN = ''' # '''

from ansible.module_utils.foreman_helper import ForemanEntityAnsibleModule


class ForemanConfigGroupModule(ForemanEntityAnsibleModule):
    pass


def main():
    module = ForemanConfigGroupModule(
        argument_spec=dict(
            updated_name=dict(),
        ),
        entity_spec=dict(
            name=dict(required=True),
            puppetclasses=dict(type='entity_list'),
        ),
    )

    with module.api_connection():
        module.run()


if __name__ == '__main__':
    main()
