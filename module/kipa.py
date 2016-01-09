import urllib.request

baseurl = "http://kapimda.kipa.com.tr/tr-TR/"

caturl = "Product/BrowseProducts?taxonomyID=Cat00000336&pageNo=1&sortBy=Default"

listsource = urllib.request.urlopen(baseurl).read()



