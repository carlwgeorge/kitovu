import yaml
from .errors import KitovuError, ConfigError


def load_profile(profile):
    try:
        import appdirs
    except ImportError:
        raise KitovuError('failed to import appdirs module')
    config_dir = appdirs.user_config_dir(__package__)
    config = '{}/{}.yaml'.format(config_dir, profile)
    return load_config(config)


def load_config(config):
    data = safe_yaml_load(config)
    hub = data.get('hub')
    token = data.get('token')
    return hub, token


def safe_yaml_load(path):
    try:
        with open(path) as f:
            try:
                return yaml.load(f.read())
            except yaml.YAMLError:
                raise ConfigError('{}: yaml error'.format(path))
    except FileNotFoundError:
        raise ConfigError('{}: file does not exist'.format(path))
