def getImages(arr):
    import re
    import urllib.request
    import pathlib
    import requests
    from bs4 import BeautifulSoup
    for index,url in enumerate(arr):
        print('Downloading:',url)
        with urllib.request.urlopen(url) as f:
            data = f.read()
            parsed_html = BeautifulSoup(data)
            imgs = parsed_html.find_all('img')
            for img in imgs:
                imgLink = img.get('src')
                if imgLink == None:
                    continue

                if not(imgLink.startswith('http')):
                    imgLink = 'http:' + imgLink

                if re.search(r'\.(\w{3,4})$', imgLink) == None:
                    continue

                response = requests.get(imgLink)
                reqUrl = re.split('/', url)
                folderName = reqUrl[len(reqUrl) - 1]
                hrefUrl = re.split('/', imgLink)
                fileName = hrefUrl[len(hrefUrl) - 1]
                fileFormat = f'./images/{folderName}/{fileName}'
                    
                pathlib.Path(f'./images/{folderName}/').mkdir(parents=True, exist_ok=True) 

                file = open(fileFormat, "wb")
                file.write(response.content)
                file.close()
            print('Folder name:', folderName)
        print(index + 1,'/',len(arr))
        