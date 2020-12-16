def sitemapFetcher(sitemap,path,local=True):
    import xmltodict
    import requests
    import time
    import re

    if local == False:
        response = requests.get(sitemap)
        sitemapD = 'sitemap.xml'
        with open('sitemap.xml','wb') as file:
            file.write(response.content)
            time.sleep(10)      
    else:
        sitemapD = sitemap

    print(sitemapD)

    with open(sitemapD) as fd:
        doc = xmltodict.parse(fd.read())
        arr = []
        for i in range(len(doc['urlset']['url'])):
            if (re.search(path, doc['urlset']['url'][i]['loc']) != None):
                arr.append(doc['urlset']['url'][i]['loc'])
        return arr
        