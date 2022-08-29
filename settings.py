from dotenv import load_dotenv

from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


def get_start():
    config = {
        'token': os.getenv('token'),
        'prefix': os.getenv('prefix')
    }
    return config


if __name__ == '__main__':
    str(get_start())

