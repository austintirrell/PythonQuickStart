import json
from scripts.log import HELPER_LOG as LOG


def write_json(data, filename):
    LOG.info(f'Writing to {filename}...')
    try:
        with open(f'reports/{filename}', 'w') as file:
            json.dump(data, file, indent=4)
        return data
    except Exception as err:
        LOG.error(f'Failed to write to {filename}: {err}')


def read_json(filename):
    LOG.info(f'Reading from {filename}...')
    try:
        with open(f'reports/{filename}', 'r') as file:
            return json.load(file)
    except Exception as err:
        LOG.error(f'Failed to read from {filename}: {err}')