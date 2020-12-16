import crawler

calculadoraArray = crawler.sitemapFetcher('https://www.kabum.com.br/sitemap/eletronicos.xml','calculadora', False)
crawler.getImages(calculadoraArray)