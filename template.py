from blogengine import pageLocation
from example import main
import pickle, os, ast

def createPage(info):
    pageInfo = ast.literal_eval(info)
    path = os.path.join(pageLocation, list(pageInfo.keys())[0] + '.page')
    print(path)
    #path = list(pageInfo.keys())[0] + '.txt'
    with open(path, 'wb') as f:
        pickle.dump(pageInfo, f)

def getPage(name):
    path = os.path.join(pageLocation, name + '.page')

    with open(path, 'rb') as f:
        out = pickle.load(f)
        print(out[name]['content'][1]['src'])
        return out[name]
