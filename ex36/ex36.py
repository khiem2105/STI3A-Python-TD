def is_bissetile(y):
  assert y > 1582
  return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def days_between_approx(y, m, d, Y, M, D):
  return abs((y-Y)*365.2425 + (m-M)*(365.2425/12) + (d-D))

# print(days_between_approx(2010, 9, 1, 2020, 5, 6))

def nb_anne_bissetile(y, Y):
  nb = 0
  if y < Y:
    for a in range(y, Y+1):
      if is_bissetile(a):
        nb += 1
  elif y > Y:
    for a in range(Y, y+1):
      if is_bissetile(a):
        nb += 1
  else:
    if is_bissetile(y):
      nb += 1            
  return nb

def nb_jours(m):
  if m in (1, 3, 5, 7, 8, 10, 12):
    return 31
  if m == 2:
    return 28
  else:
    return 30    

def days_between_mois(m, M):
  days = 0
  if m < M:
    for mois in range(m, M+1):
      days += nb_jours(mois)
  elif m > M:
    for mois in range(M, m+1):
      days -= nb_jours(mois)
  else:
    return 0          

def days_between(y, m, d, Y, M, D):
  days_between = 0
  days_between += nb_anne_bissetile() 



