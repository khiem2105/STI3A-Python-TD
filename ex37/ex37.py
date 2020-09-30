import ngram_score as ns
fitness = ns.ngram_score()

def print_grille():
  for i in range(ord("A")-2, ord("Z")+1):
    if i == ord("A") - 2:
      print("\t", end="")
      for j in range(ord("A"), ord("Z") + 1):
        print(chr(j), end=" ")
      print("")  
    elif i == ord("A") - 1:
      for j in range(ord("A"), ord("Z") + 3):
        print("-", end=" ")
      print("")
    else:
      print(chr(i) + " |", end=" ")
      for j in range(i, ord("Z") + 1):
        print(chr(j), end=" ")
      for j in range(ord("A"), i):
        print(chr(j), end=" ")
      print("")         

# print_grille()

def crypt(msg, key, dechiffre=False):
  msg_len = len(msg)
  key_len = len(key)
  result = str()
  j = 0
  for i in range(msg_len):
    if j == key_len:
      j = 0
    # print(j)  
    if not dechiffre:
      c = chr(ord("A") + ((ord(msg[i]) + ord(key[j])) % 26))
      # print(c, end="")
      # msg.replace(msg[i], c)
      result = result + c
    else:
      c = chr(ord("A") + ((ord(msg[i]) - ord(key[j])) % 26))
      result = result + c
    j += 1

  return result   

msg1 = "THESTUDENTSARENICEANDHARDWORKING"
key1 = "ORARETHEY"
crypt1 = crypt(msg1, key1)
# print(crypt1, crypt(crypt1, key1, True))

def find_max_score(cyp, l):
  key = str()
  for _ in range(l):
    key = key + "A"
  key 

def autobreak(cyp):
  print(fitness.score("LCINBROMPLNEMMKTKGSIHCIOOEQJFMIO"))

autobreak("")
print(crypt(crypt1, "W", True))
print(crypt(crypt1, "XUMC", True))
print(fitness.score(crypt(crypt1, "TION", True)))