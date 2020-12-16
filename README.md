# py-image-crawler
Hi, that's the Crawler module for python, currenty under development and maybe don't work perfectly.
If you want to test or contribute, feel free to clone the repository and help me with the next best web scraping module for python.
It's not already published in **pip**, so, the only way is using it locally.
## Commands

 ### **sitemapFetcher**

Search and filter the url's of a sitemapfile or a sitemap url (both XML).
 
````
crawler.sitemapFetcher(url, path, local)
````

 - url (string) = where to search for the used sitemap, can be a file in the directory or the url to the sitemap, usually like 'https://python.com/sitemap.xml'. If you are using the url, need to set local to False 
 - path (string) = a filter to the url that you want to select, example: '/products' will pick only url's with '/products' included
 - local (boolean) = defaulted to True, it determines if you are using a local file .xml (True) or looking for a url (False)
 
 ````
crawler.sitemapFetcher('https://www.kabum.com.br/sitemap/eletronicos.xml','calculadora', False)
 ````
 
It returns a **array** with all the url's that **matched your filter**.

### **getImages**
Download all the images from a webpage.

````
crawler.getImages(urlsArray)
```` 

 - urlsArray = a array with the url's that you want to download the images, made for using with **sitemapFetcher**

## Continue...
