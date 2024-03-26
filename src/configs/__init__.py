# INIT CONFIG
# So what this file does is it chooses which configs to load depending on what the environment is
# Currently, it's set to local

import os

environment = os.environ.get("ENVIRONMENT", "local")

# Load the appropriate configuration file based on the environment
if environment == "local":
    from .config_local import *
elif environment == "production":
    from .config_production import *
else:
    raise ValueError(f"Invalid environment: {environment}")
