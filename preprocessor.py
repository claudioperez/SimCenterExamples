

def _pandoc(inputs: str, t: str):
    #  -f html-native_divs+raw_html
    arguments = ['pandoc', '-f', 'markdown-native_divs+raw_html', '-t', t]
    p = subprocess.Popen(
            arguments,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            encoding='utf8'
    )
    return p.communicate(inputs)[0]



class Processor:
    def __init__(self,**args):
        pass




class PreProcessor:
    def __init__(self, build_dir, filters={}, templates=[]):
        self.build_dir = build_dir
        self.filters = filters 
        self.templates = templates

    def stage(self): pass

    def run(self): pass

