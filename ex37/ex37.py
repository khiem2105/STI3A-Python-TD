import ngram_score as ns
from collections import Counter
from math import log10 as lg
fitness = ns.ngram_score()

def print_grille():
  for i in range(ord("A")-2, ord("Z")+1):
    if i == ord("A") - 2:
      print("    ", end="")
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

print_grille()

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
crypt2 = crypt("THISISATEST", "K")

#------------------------
#n-gram analysis

def is_alpha(c):
  return ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z")

assert all(is_alpha(chr(n)) == chr(n).isalpha() for n in range(128))
assert all(not is_alpha(chr(n)) for n in range(128, 256))

def gramiter(s, n=4):
  i = 0
  while len(s) - i >= n:
    yield s[i:i+n]
    i += 1

# print(tuple(gramiter("ATTACK", n=1)))

def process(text="WP.txt", out="quads.txt"):
  with open(text) as t, open(out, "w") as o:
    input = str()
    for line in t:
      for word in line.split():
        for c in word:
          if not is_alpha(c):
            word = word.replace(c, "")
        input = input + word.upper()
    c = Counter([quad_gram for quad_gram in gramiter(input)])
    for quad_gram, count in c.most_common(len(c)):
      o.write(quad_gram + " " + str(count) + "\n")     

# process()

def load_grams(fname="quads.txt"):
  c = Counter()
  with open(fname) as f:
    for line in f:
      data = line.split()
      c.update({data[0]:int(data[1])})
  return c

C = load_grams()
total = sum(count for count in C.values())
p0 = 1 / (100 * total)

def score(s, C=C):
  score = 1
  for quad_gram in gramiter(s):
    # score += C[quad_gram]
    if quad_gram not in C:
      score += lg(p0)
    else:
      score += lg(C[quad_gram]/total)  
  return score

def find_key(c, l, cyp):
  key = str()
  for _ in range(l):
    key = key + c  
  alphabet = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
  is_changed = True
  while is_changed:
    is_changed = False
    for j in range(l):
      find_character = max(alphabet, key=lambda x:score(crypt(cyp, key[:j] + x + key[j + 1:], True)))
      if find_character != key[j]:
        is_changed = True
        key = key[:j] + find_character + key[j+1:]
  return key    
       
def autobreak(cyp):
  for i in range(10):
    key = [find_key(chr(j), i+1, cyp) for j in range(ord("A"), ord("Z") + 1)]
    # print(key)
    best_key = max(key, key=lambda x:score(crypt(cyp, x, True)))
    cyp_dechiffre = crypt(cyp, best_key, True)
    point = score(cyp_dechiffre)
    print(f"{best_key:>9} {cyp_dechiffre:15} {point}")

autobreak("MVUDHIVKSMREKSGMMEKOZXSVZVNMTATSLZTOITYGIROLZWMGFRIMIQCLXECSIXLASULCR")
autobreak("GVVMFEMMCTKYQBPZBDPYHJYYZIYSOHZRMNIOXMIQPYGBPMLUKVWZRFHAIWECJC")
# autobreak("LXATDEMAFLIDVVFZKZHPBWARJEWXMAHSMZATGWPCJIDIWFSSVTMNAUTVJCYFDVVL")
# autobreak("LXATDEMAFLIDVVFZKZHPBWARJEZEHWQTIINWRMNUWEXMTTPMQZXHQDLIPKZSYMDHREVVXCZPX")
# autobreak(crypt2)
print(score("THISISACOHERENTSENTENCE"))
print(score("BLAHIBLAHBLOBYAAKNOWAHH"))
print(score("LKFJLSDFJIOJZOJMIOFJNZA"))
# print(fitness.score("THISISACOHERENTSENTENCE"))    