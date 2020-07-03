# Claudio Perez
# Python 3.8

# standard library
import json, os, shutil, sys, subprocess
# from subprocess import Popen, PIPE, STDOUT

import jinja2
from ruamel_yaml import YAML



yaml=YAML(typ='rt')


FILE_VARS = {
    'fem':
        {'OpenSees': ['mainInput','mainPostprocessScript'],
         'OpenSeesPy':['mainInput','parametersFile','mainPostprocessScript'],
         'FEAPpv': []}
}

def _pandoc(inputs: str, t: str):
    # sys.stdout.write(f)
    # p = Popen(, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    
    # out, e = p.communicate()[0]
    # print('\nout: \n',out, '\ne: \n',e); input()

    arguments = ['pandoc', '-f', 'markdown', '-t', t, '--wrap=preserve']

    p = subprocess.Popen(
            arguments,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            encoding='utf8'
    )
    return p.communicate(inputs)[0]

def _md2rst(ex):
    for key in ex['docs']: 
        print(ex['docs'][key])
        if ex['docs'][key]: 
            ex['docs'][key] = _pandoc(ex['docs'][key], 'rst')
    

def make_doc(ex: dict, folder: str, template='base.rst', ext = '.rst'):
    """Make a doc page for an example that is serialized in `ex`.

    - create _build/{{ folder }}/{{ ex[id] + ext }}
    - copy content from static/ to _build/{{folder}}/
    """

    filename = '_build/' + folder + '/' + ex['id'] + ext
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Jinja
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_dir))

    tm = env.get_template(template)
    
    # tm = jinja2.Template(template)
    
    
    _md2rst(ex)
    # print(ex)
    # input()
    docstring = tm.render(page=ex)
    # print(docstring)
    # input()
    with open(filename , 'w') as f: f.write(docstring)


def make_dir(ex):
    """Make a dir for an example that is serialized in `ex`.

    - create _build/{{ folder }}/src/
    """
    # Create input.json file
    filename = app_name +'/src/'+ ex['id']+'/'+'input.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename,'w+') as f: json.dump(ex['input'], f, indent=4)

    # Populate quo-xx/ dir
    # src_dir = ex['srcDir'] + '/'
    # for file_var in FILE_VARS['fem'][ex['input']['fem']['program']]:
    #     if fname := ex['input']['fem'][file_var]:
    #         try: shutil.copyfile(src_dir+fname, target_dir+fname)
    #         except Exception as e: print(e)
# (lambda f, *a: f(f, *a))(lambda rec, n: 1 if n == 0 else n*rec(rec, n-1), n)
# (lambda Y,*a: Y(Y,*a) )(lambda rec, d: dict(d) if  not isinstance(d,dict))

def make_all(app_name, to_ext='.rst'):
    with open('conf.yml') as file: index = dict(yaml.load(file))

    for ex in index[app_name]:
        # print(ex); input()
        # create .rst files
        if 'docs' in ex: make_doc( ex, folder=app_name )



if __name__ == "__main__":
    #app_name = 'EE-UQ'
    #app_name = 'PBE'
    #app_name = 'WE-UQ'
    app_name = 'quoFEM'
    #app_name = 'pelicun'
    make_all(app_name)
