import json
main = \
    {
    'page':
        {   'content':
            [
                {
                    'tag':'div',
                    'class':'text',
                    'id':'example',
                    'content':'Hello World!'
                },
                {
                    'tag':'img',
                    'class':'text',
                    'id':'example',
                    'src':'Hello World!'
                },
                {

                    'tag':'h1',
                    'class':'text',
                    'id':'example',
                    'content':'Hello World!'
                }

            ],
            'meta':
                {
                    'blurb': 'stuff and things',
                    'author': 'trase'
                }
        }
    }
print(json.dumps(main))
"""
/admin/panel
"""