"""
run
---
Start the development server. Not for use in production.

"""

import os

import yaml

from src import app

ENV_FILE_PATH = "env.dev.yaml"


def load_env_variables(env_file_path=ENV_FILE_PATH):
    """
    Load environment variables from a YAML config, to simulate production.

    """
    env = None
    with open(env_file_path) as f:
        env = yaml.safe_load(f)
    if env is None:
        raise EnvironmentError(f"Unable to load config file from `{env_file_path}`")

    for var in env:
        os.environ[var] = env[var]

    return


if __name__ == "__main__":
    load_env_variables()
    app.run(
        host=os.environ["HOST"],
        port=os.environ["PORT"],
        debug=True,
        # additional options are forwarded to Werkzeug server
        threaded=True,
    )
