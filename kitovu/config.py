import yaml


def load_profile(profile):
    try:
        import appdirs
    except ImportError:
        raise SystemExit('The appdirs module is required for profile support, but could not be imported.')
    config_dir = appdirs.user_config_dir('github')
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
                return yaml.load(f)
            except yaml.YAMLError:
                raise SystemExit('{}: yaml error'.format(path))
    except FileNotFoundError:
        raise SystemExit('{}: file does not exist'.format(path))
