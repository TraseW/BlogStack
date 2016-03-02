from blogengine import pageLocation
from example import main
import pickle, os, ast

def createPage(info):
    pageInfo = ast.literal_eval(info)
    path = os.path.join(pageLocation, list(pageInfo.keys())[0])
    checkPath = os.path.abspath(path)
    if ".." in path:
        return 'Not Allowed'
    #path = list(pageInfo.keys())[0] + '.txt'
    with open(path, 'wb') as f:
        pickle.dump(pageInfo, f)
    return 'success'

def getPage(name):
    path = os.path.join(pageLocation, name)

    with open(path, 'rb') as f:
        out = pickle.load(f)
        print(out[name]['content'][1]['src'])
        return out
