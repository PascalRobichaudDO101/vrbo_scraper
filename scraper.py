import scraperwiki
from pyquery import PyQuery

ROOT = 'https://fairemtl.ca'
dom = PyQuery('%s/fr/projets' % ROOT)

#url = 'http://www.vrbo.com/373926'

#q = PyQuery(url)

#print q('.ratesdetails').text()

#Fin du traitement
traitement_fin = datetime.now() 
print("Fin du traitement: %s " % traitement_fin)


