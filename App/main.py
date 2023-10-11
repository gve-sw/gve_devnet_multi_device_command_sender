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

import logging
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException
import config

logging.basicConfig(level=logging.INFO)

def send_commands(device, commands):
    """Send a list of commands to a given device."""
    # Extract only the connection-related parameters from the device dictionary.
    connection_params = {k: v for k, v in device.items() if k != 'commands'}
    try:
        conn = ConnectHandler(**connection_params)
        output = conn.send_config_set(commands)
        logging.info(f"Commands sent to {device['ip']}:\n{output}")
        conn.disconnect()
        return True

    except NetMikoTimeoutException:
        logging.error(f"Timeout connecting to {device['ip']}")
        return False
    except NetMikoAuthenticationException:
        logging.error(f"Authentication error with {device['ip']}")
        return False
    except Exception as e:
        logging.error(f"Error sending commands to {device['ip']}: {e}")
        return False


def validate_device_config(device):
    """Validate if essential parameters are present in the device configuration."""
    essential_keys = ['ip', 'device_type', 'username', 'password']
    for key in essential_keys:
        if key not in device:
            logging.error(f"'{key}' not found in device config for {device.get('ip', 'Unknown IP')}")
            return False
    return True

if __name__ == "__main__":
    for device in config.DEVICES:
        if not validate_device_config(device):
            continue  # Skip this device if validation fails

        device_commands = device.get('commands', config.GENERAL_COMMANDS)
        success = send_commands(device, device_commands)

        if not success:
            logging.warning(f"Retrying for {device['ip']}")
            send_commands(device, device_commands)  # Retry once if the first attempt fails