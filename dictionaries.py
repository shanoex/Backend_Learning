#dictionaries
band = {
    'name': 'the beatles',
    'perfume': 'yes'
    
}
band2 = dict(name='the beatles', perfume='yes')
print(band)
print(band2)
print(type(band))
print(type(band2))
print(band.items())
print(band.keys())
print(band['name'])
print(band.get('perfume'))
band['name']='the rolling stones'
band.update({'pulshie':'charmander'})
print(band)
