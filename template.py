from blogengine import pageLocation
from example import main
import pickle, os, ast

def createPage(info):

    print(info['pageName'])
    path = os.path.join(pageLocation, info['pageName'])
    content = {'content': info['content'], 'meta': info['meta']}
    checkPath = os.path.abspath(path)
    if ".." in path:
        return 'Not Allowed'
    #path = list(pageInfo.keys())[0] + '.txt'
    with open(path, 'wb') as f:
        pickle.dump(content, f)
    return 'success'

def getPage(name):
    path = os.path.join(pageLocation, name)

    with open(path, 'rb') as f:
        out = pickle.load(f)
        return out
