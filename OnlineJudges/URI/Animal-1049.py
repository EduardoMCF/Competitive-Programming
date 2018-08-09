#EMCF

key1 = raw_input()
key2 = raw_input()
key3 = raw_input()

dicio = { 'vertebrado': {'ave':
                              {'carnivoro':'aguia','onivoro':'pomba'},
                          'mamifero':
                              {'onivoro':'homem','herbivoro':'vaca'}},
          'invertebrado':
              {'inseto':
                   {'hematofago':'pulga','herbivoro':'lagarta'},
          'anelideo':
              {'hematofago':'sanguessuga','onivoro':'minhoca'}}}

print dicio[key1][key2][key3]