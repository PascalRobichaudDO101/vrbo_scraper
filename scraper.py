import scraperwiki
from pyquery import PyQuery

ROOT = 'https://fairemtl.ca'
dom = PyQuery('%s/fr/projets' % ROOT)

pages = int(dom.find('.pager-last a').attr('href').split('%2C')[-1])

urls = []
for page in range(0, pages + 1):
    dom = pyquery.PyQuery('%s/fr/projets?page=0,%s' % (ROOT, page))
    urls.extend("%s%s" % (ROOT, a.attrib['href']) for a in dom.find('h3 a'))
#url = 'http://www.vrbo.com/373926'

#q = PyQuery(url)

#print q('.ratesdetails').text()

#Fin du traitement
print("Fin du traitement")


