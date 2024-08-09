import os
from termcolor import colored
import importlib
from .base import *

__all__ = ["base"]
env = os.getenv("APP_ENV", "LOCAL")


def print_message_and_import_settings(env, module_name):
    print(colored(f"USING {env.upper()} SETTINGS", "green", attrs=["bold"]))
    importlib.import_module(f".{module_name}", package=__package__)


env_settings = {
    "PROD": "prod",
    "DEV": "dev",
    "TEST": "test",
    "LOCAL": "local",
}

if env in env_settings:
    print_message_and_import_settings(env, env_settings[env])
else:
    raise Exception(
        colored(
            "APP_ENV must be set to run the project, example: export APP_ENV=LOCAL / TEST / DEV / PROD",
            "red",
            attrs=["bold"],
        )
    )
