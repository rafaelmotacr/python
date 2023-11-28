# Site está acessível?

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br/")
except:
    print("> \033[31mO site pudim não está acessível! :(\033[m")
else:
    print("> \033[32mO site pudim está acessível! :)\033[m")
print(site.read())
