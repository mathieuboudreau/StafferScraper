import yaml

def load_config(filename):
    '''Load Config Files
    Uses yaml library to parse config file
    
    Args:
        filename: string
    
    Return:
        config: dict
    '''
    
    with open(filename, 'r') as ymlfile:
        config = yaml.load(ymlfile)
    
    return config    