"""

Utils hier zitten de functies voor startup en background


"""
import utils.ntp
import platform
import logging
import os

logger = logging.getLogger(__name__)


def read_controller_config():
    """
    Read controller configuration from file, or retrieve it from other sources if not present.
    """
    # Check if controller configuration file exists

    config_file = os.path.join(os.path.dirname(__file__), '..', 'config', 'controller.conf')
    print(config_file)
    if os.path.isfile(config_file):
        # Read configuration from file
        with open(config_file, "r") as f:
            config = dict(line.strip().split("=") for line in f)
    else:
        # Retrieve configuration from other sources
        config = {
            "controllernaam": get_controller_name(),
            "ip_wan": get_wan_ip(),
            "ip_vpn": get_vpn_ip(),
            "poort": 9080,
        }
        # Write configuration to file
        with open(config_file, "w") as f:
            for key, value in config.items():
                f.write(f"{key}={value}\n")

    # Read current configuration
    with open(config_file, "r") as f:
        current_config = dict(line.strip().split("=") for line in f)

    # Check if configuration is still valid
    if (
            current_config["controllernaam"] == get_controller_name()
            and current_config["ip_wan"] == get_wan_ip()
            and current_config["ip_vpn"] == get_vpn_ip()
            and current_config["poort"] == 9080
    ):
        return current_config
    else:
        # Update configuration
        current_config.update({
            "controllernaam": get_controller_name(),
            "ip_wan": get_wan_ip(),
            "ip_vpn": get_vpn_ip(),
            "poort": 9080,
        })
        with open(config_file, "w") as f:
            for key, value in current_config.items():
                f.write(f"{key}={value}\n")
    return current_config


def get_controller_name():
    """
    Het ophalen van de hostname in het bestand /etc/hostname
    :return: hostname
    """

    if platform.system() == "Darwin":
        logger.info("Running from MacOs")
        hostname = "lc0001"
    elif platform.system() == "Windows":
        logger.info("Running from Windows")
        hostname = "lc0001"
    else:
        logger.info("Running from Linux")
        with open('/etc/hostname', 'r') as f:
            hostname = f.readline()
    return hostname


def get_vpn_ip():
    if platform.system() == "Darwin":
        logger.info("Running from MacOs")
        ip = "127.0.0.1"
    elif platform.system() == "Windows":
        logger.info("Running from Windows")
        ip = "127.0.0.1"
    else:
        logger.info("Running from Linux")
        # todo: nog op te zoeken hoe dit op te vragen
        # with open('/etc/hostname', 'r') as f:
        #     hostname = f.readline()
    return ip


def get_wan_ip():
    if platform.system() == "Darwin":
        logger.info("Running from MacOs")
        ip = "127.0.0.1"
    elif platform.system() == "Windows":
        logger.info("Running from Windows")
        ip = "127.0.0.1"
    else:
        logger.info("Running from Linux")
        # todo: nog op te zoeken hoe dit op te vragen
        # with open('/etc/hostname', 'r') as f:
        #     hostname = f.readline()
    return ip


def get_ntp():
    return utils.ntp.get_ntp()
