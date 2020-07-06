# Claudio Perez
# Python 3.8

# standard library
import json, os, shutil, sys, subprocess, urllib.request
from distutils.dir_util import copy_tree
# from subprocess import Popen, PIPE, STDOUT

import jinja2
from ruamel_yaml import YAML


yaml=YAML(typ='rt')



# _BUILD_DIR = '..\\SimCenterDocumentation\\docs\\common\\user_manual\\examples\\desktop'
_BUILD_DIR = 'C:\\Users\\claud\depot\\sim\\SimCenterDocumentation\\docs\\common\\user_manual\\examples\\desktop'

# SCHEMA = urllib.request.urlopen("https://raw.githubusercontent.com/claudioperez/SimCenterDocumentation/examples/docs/common/user_manual/schemas/quoFEM_Schema.json").read()
# schema = json.loads(SCHEMA)
# RV_SCHEMA = urllib.request.urlopen("https://raw.githubusercontent.com/claudioperez/SimCenterDocumentation/examples/docs/common/user_manual/schemas/RV_Schema.json").read()
# rv_schema = json.loads(RV_SCHEMA)

sdir = "C:\\Users\\claud\\depot\\sim\\SimCenterDocumentation\\docs\\common\\user_manual\\schemas\\"
with open(sdir + "quoFEM_Schema.json") as f : schema = json.load(f)
with open(sdir + "RV_Schema.json") as f : rv_schema = json.load(f)


FILE_VARS = {
    'fem':
        {'OpenSees': ['mainInput','mainPostprocessScript'],
         'OpenSeesPy':['mainInput','parametersFile','mainPostprocessScript'],
         'FEAPpv': []}
}

def _pandoc(inputs: str, t: str):
    arguments = ['pandoc', '-f', 'markdown', '-t', t, '--wrap=preserve']
    p = subprocess.Popen(
            arguments,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            encoding='utf8'
    )
    return p.communicate(inputs)[0]



# def tab_titles(dic):
#     for k, v in schema.items():
#         if 'title' in v: dic[k] = dic.pop(v['title'])
def schemaTable(input,schema):
    out=[]
    for Prop in schema['options']:
        if Prop in input:
            for prop in schema['properties'][Prop]['properties']:
                # try: out.join('{}, {}\n'.format([schema['properties'][Prop]['properties'][prop]['title'], input[Prop][prop]]))
                try: out.append([schema['properties'][Prop]['properties'][prop]['title'], input[Prop][prop]])
                except Exception as e: print(e)
    return out

def rv_filter(in_dict):
    out = []
    for rv_dict in in_dict:
        var = {}
        var['distribution'] = dist = rv_dict['distribution']
        RV = rv_schema['properties'][dist.lower()]
        var['params'] = [{
            'tex': RV['properties'][prop]['tex'],
            'title': RV['properties'][prop]['title'],
            'value':  rv_dict[prop]
        } for prop in RV['properties']]
        var['title'] = rv_dict['title']
        var['name'] = rv_dict['name']
        out.append(var)
        # print(var)
    return out
    
def _md2rst(ex):
    for key in ex['docs']: 
        # print(ex['docs'][key])
        if ex['docs'][key]: 
            ex['docs'][key] = _pandoc(ex['docs'][key], 'rst')
    
def make_doc(ex: dict, folder: str, template='example.md', ext = '.rst'):
    """Make a doc page for an example that is serialized in `ex`.

    - create _build/{{ folder }}/{{ ex[id] + ext }}
    - copy content from static/ to _build/{{folder}}/
    """
    # create output directory and file
    filename = os.path.join(_BUILD_DIR, folder + '\\' + ex['id'] + ext)
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # load jinja template
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_dir))
    env.filters['schemaTable'] = schemaTable
    env.filters['basename'] = lambda path: os.path.basename(path)
    tm = env.get_template(template)
    
    try: ex['rvars'] = rv_filter(ex['input']['randomVariables'])
    except Exception as e: print(e, ex['id'])

    page = tm.render(page=ex)
    # _md2rst(ex) # convert docstrings from md to rst
    
    with open(filename , 'w') as f: f.write(_pandoc(page, 'rst'))
    copy_tree( 'static', _BUILD_DIR + '\\' + folder )


def make_dir(ex, folder, filter = lambda x: x):
    """Make a dir for an example that is serialized in `ex`.

    - create _build/{{ folder }}/src/
    """
    # Create input.json file
    build_path = os.path.join(_BUILD_DIR, folder, 'src', ex['id'])
    filename = os.path.join(build_path, 'input.json')
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename,'w+') as f: json.dump(ex['input'], f, indent=4)

    if 'files' in ex: 
        for file in ex['files']: 
            filename = os.path.split(file['loc'])[1]
            src = os.path.join('static', file['loc'])
            try:  shutil.copyfile(src, os.path.join(build_path, filename))
            except Exception as e: print(e)


def make_all(app_name, schema, to_ext='.rst'):
    with open('conf.yml') as file: index = dict(yaml.load(file))

    for ex in index[app_name]:
        ex['schema'] = schema
        # print(ex); input()
        # create .rst files
        if 'docs' in ex:
            make_doc( ex, folder=app_name )
        make_dir(ex, folder=app_name )



if __name__ == "__main__":
    #app_name = 'EE-UQ'
    #app_name = 'PBE'
    #app_name = 'WE-UQ'
    app_name = 'quoFEM'
    #app_name = 'pelicun'
    make_all(app_name, schema)

