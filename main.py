# Encryption Machine

def enigma_light():
  # Create key string
  keys = 'abcdefghijklmnopqrstuvwxyz !'

  #Autogenerate the vaules string by offsetting original string 

  values = keys[-1] + keys[0:-1]
  # print(keys)
  # print(values)

  # Create two dictionaries 
  dict_e = dict(zip(keys,values))
  dict_d = dict(zip(values, keys))

  # Or create 1 dict and then flip it for decrypt
  # dict_e = dict(zip(keys, values))
  # dict_d = {value:key for key, value in dict_e.items()}

  msg = input('Enter your secret message quietly: ')

  mode = input('Crypto mode: encode (e) Or Decode (d) by default: ')

  # Run either encode or decode 

  if mode.lower() == 'e':
    new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
  
  else:
    new_msg = ''.join([dict_d[letter] for letter in msg.lower()])

  return new_msg.capitalize()


print(enigma_light())

