import yaml

with open('./examples/catalog.yml', mode='r') as real_cat:
    d = yaml.load(real_cat)
    with open('./examples/data/.data_stubs/catalog.yml') as test_cat:
        d['sources'].update(**yaml.load(test_cat)['sources'])
    print('NEW CATALOG CONTENTS:', d)
    
    with open('test_catalog.yml', mode='w') as output_cat:
        output_cat.write(yaml.dump(d))