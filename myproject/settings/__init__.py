import os

env = os.getenv("APP_ENV", "LOCAL")


def print_terminal_message(message):
    BOLD = "\033[1m"
    RED = "\033[91m"
    RESET = "\033[0m"
    return f"{BOLD}{RED}{message}{RESET}"


match env:

    case "PROD":
        from .prod import *  # noqa
    case "DEV":
        from .dev import *  # noqa
    case "TEST":
        from .test import *  # noqa
    case "LOCAL":
        from .local import *  # noqa
    case _:
        raise Exception(
            print_terminal_message(
                "APP_ENV must be set to run the project , example : export APP_ENV=LOCAL / TEST / DEV / PROD"
            )
        )
