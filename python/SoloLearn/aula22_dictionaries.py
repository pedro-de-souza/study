# Dicionários são estruturas de dados usadas para mapear chaves arbitrárias para valores.
# As listas podem ser consideradas dicionários com chaves inteiras dentro de um determinado intervalo.
# Os dicionários podem ser indexados da mesma maneira que as listas, usando colchetes contendo chaves.

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

# 

primary = {
  "red": [255, 0, 0], 
  "green": [0, 255, 0], 
  "blue": [0, 0, 255], 
}

print(primary["red"])
print(primary["yellow"])

# 

dict = {}
  dict['a'] = 'alpha'
  dict['g'] = 'gamma'
  dict['o'] = 'omega'

  print dict  # {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

  print dict['a']     # Simple lookup, returns 'alpha'
  dict['a'] = 6       # Put new key/value into dict
  'a' in dict         # True
  #print dict['z']                  # Throws KeyError
  if 'z' in dict: print dict['z']     # Avoid KeyError
  print dict.get('z')  ## None (instead of KeyError)

  ## By default, iterating over a dict iterates over its keys.
  ## Note that the keys are in a random order.
  for key in dict: print key
  ## prints a g o
  
  ## Exactly the same as above
  for key in dict.keys(): print key

  ## Get the .keys() list:
  print dict.keys()  ## ['a', 'o', 'g']

  ## Likewise, there's a .values() list of values
  print dict.values()  ## ['alpha', 'omega', 'gamma']

  ## Common case -- loop over the keys in sorted order,
  ## accessing each key/value
  for key in sorted(dict.keys()):
    print key, dict[key]
  
  ## .items() is the dict expressed as (key, value) tuples
  print dict.items()  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])



pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  None: "True",
}

# 

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

# 


print(fib.get(4, 0) + fib.get(7, 5))

slots = {"request": {"type": "IntentRequest",	"intent": {	"name": "ChamadoIntent",	"slots": {"servico": {"name": "servico","value": "pedro","confirmationStatus": "NONE","source": "USER"}}}}}
print(slots["request"]["intent"]["slots"]["servico"]["value"])
