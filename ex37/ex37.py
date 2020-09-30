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
crypt2 = crypt("THISISATEST", "K")
print(crypt2)

def find_key(c, l, cyp):
  key = str()
  for _ in range(l):
    key = key + c  
  alphabet = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
  is_changed = True
  while is_changed:
    is_changed = False
    for j in range(l):
      find_character = max(alphabet, key=lambda x:fitness.score(crypt(cyp, key[:j] + x + key[j + 1:], True)))
      if find_character != key[j]:
        is_changed = True
        key = key[:j] + find_character + key[j+1:]
  return key    

# print(find_key("A", 4))
       
def autobreak(cyp):
  for i in range(10):
    key = [find_key(chr(j), i+1, cyp) for j in range(ord("A"), ord("Z") + 1)]
    # print(key)
    best_key = max(key, key=lambda x: fitness.score(crypt(cyp, x, True)))
    cyp_dechiffre = crypt(cyp, best_key, True)
    score = fitness.score(cyp_dechiffre)
    print(f"{best_key:>10} {cyp_dechiffre:10} {score}")

autobreak(crypt2)    

# def test(text):
#   for i in text:
#     text = text.replace(i, chr(ord(i)+1))
#     print(text)
#   print(text)    

# test("ABC")
# print([fitness.score("AMAA") for i in range(ord("A"), ord("Z")+1)])
# autobreak("")
# print(crypt(crypt1, "W", True))
# print(crypt(crypt1, "XUMC", True))
# print(fitness.score(crypt(crypt1, "TION", True)))