""" Copyright (c) 2023 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

# List of devices with their connection details
DEVICES = [
    # Device 1
    {
        'ip': 'Change-to-device-IP',
        'device_type': 'cisco_ios',
        'username': 'Change-to-device-password',
        'password': 'Change-to-device-password',
        # Optional: Commands specific to this device, Remove completely if not being used
        'commands': [
            'Change-to-your-commands',
            'Change-to-your-commands'
        ]
    },
    # Device 2    
    {
        'ip': 'Change-to-device-IP',
        'device_type': 'cisco_ios',
        'username': 'Change-to-device-password',
        'password': 'Change-to-device-password',
        # Optional: Commands specific to this device, Remove completely if not being used
        'commands': [
            'Change-to-your-commands',
            'Change-to-your-commands'
        ]
    }
    # ... other devices
]

# General commands to run if no specific commands are provided for a device, must be comma separated
GENERAL_COMMANDS = [
    'Change-to-your-commands',
    'Change-to-your-commands'
]
