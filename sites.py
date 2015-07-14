root = "http://assets.austintexas.gov/police/mug_shots/images/NAMES/%s/"
for a in range(1, 100):
  print root % (str(a).zfill(2))
