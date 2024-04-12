import configparser

config = configparser.ConfigParser()
user_config = '/home/john/Desktop/dev-desktop-folder/devpyconf.ini'
# fields_config = 
config.read(user_config)

def get_config_data():
    section_and_key = f"{config.sections()[0]}: {[*config[config.sections()[0]]][0]}"
    data_values = f"{config['config-section-0']['data-key-0'].split(',')[0]}, {config['config-section-0']['data-key-0'].split(',')[1]}"
    return section_and_key, data_values

def get_locations():
    r_set = set([int(n) for n in config['locations']['toset'].split(',')])
    return sorted(r_set)

def set_locations(l_list):
    try:
        config['locations']['toset'] = ','.join([str(i) for i in l_list])
        with open(user_config, 'w')as wf:
            config.write(wf)    
    except:
        raise

    return get_locations()

def remove_location(location) -> list[int]:
    toset_data = config['locations']['toset'].split(',')
    try:
        toset_data.remove(str(location))
        config['locations']['toset'] = ','.join(toset_data)        
        with open(user_config, 'w')as wf:
            config.write(wf)
        return get_locations()
    except ValueError:
        raise


if __name__ == '__main__':
    # print(get_config_data())
    print(get_locations())