import yaml


def load_template(path):

    with open(path, "r") as file:
        config = yaml.safe_load(file)

    return config