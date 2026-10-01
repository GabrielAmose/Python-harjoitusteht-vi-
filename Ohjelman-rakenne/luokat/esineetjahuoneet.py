from .esine import Esine
from .huone import Huone

hiusharja = Esine("Hiusharja", 30.3)
pallo = Esine("Pallo", 402.8)
tyyny = Esine("Tyyny", 175.3)
pehmo = Esine("pehmolelu", 76.9)
lappari = Esine("Kannettavatietokone", 1200.0)
tyhja = Esine("Ei ole", 0.0)

huoneet = []
huoneet.append(Huone("Olohuone", lappari))
huoneet.append(Huone("Makuuhuone", tyyny))
huoneet.append(Huone("Vessa", hiusharja))
huoneet.append(Huone("Kellari", pallo))
huoneet.append(Huone("Lastenhuone", pehmo))