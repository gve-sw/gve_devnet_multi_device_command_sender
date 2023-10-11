# gve_devnet_multi_device_command_sender

This script allows users to execute device commands remotely on multiple devices in a network.

## Contacts

* Rey Diaz

## Solution Components

* IOS
* Netmiko
* Python

## Related Sandbox Environment

This sample code can be tested using a Cisco dCloud demo instance that contains a Cisco IOS-based network with multiple devices.

## Installation/Configuration

1. **Install Python**:
   If you haven't already, install [Python](https://www.python.org/downloads/). This script is best suited for Python 3.

2. **Install Required Packages**:
Navigate to your project directory and run:

```bash
pip install -r requirements.txt
```

3. **Update Device and Command Details**:
   Before executing the code, ensure to update the device details and desired commands in the `config.py` file.

   You'll have to set:

   - `ip`: Replace 'Change-to-device-IP' with the actual IP address of your device.
   - `device_type`: This is set to 'cisco_ios' by default, but change if your device type differs.
   - `username`: Replace 'Change-to-device-username' with the actual username used to access the device.
   - `password`: Replace 'Change-to-device-password' with the actual password for the device.
   - `commands`: If you have specific commands for this one device, replace 'Change-to-your-commands' with them. If not, you MUST remove this field completely. If this field is not removed and is left empty, no commands will be run on the device.

   In addition, there's a list of `GENERAL_COMMANDS` that will be run if no specific commands are provided for a device. Update this list as needed.

```bash
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
```

## Usage

After updating the device details and commands, you can run the `main.py` file to send commands to the devices.

For instance, to send commands use the following:

```bash
$ python main.py
```

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:

Please note: This script is meant for demo purposes only. All tools/scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
