from datetime import date

def is_bissetile(y):
  assert y > 1582
  return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def nb_jours(y, m):
  if m in (1, 3, 5, 7, 8, 10, 12):
    return 31
  if m == 2:
    return 29 if is_bissetile(y) else 28
  return 30    

def is_valid_date(y, m, d):
  return (1 <= m <= 12) and (1 <= d <= nb_jours(y, m))    

def days_between_approx(y, m, d, Y, M, D):
  return ((y-Y)*365.2425 + (m-M)*(365.2425/12) + (d-D))

# print(days_between_approx(2010, 9, 1, 2020, 5, 6))

# def nb_anne_bissetile(y, Y):
#   nb = 0
#   if y < Y:
#     for a in range(y+1, Y):
#       if is_bissetile(a):
#         nb += 1
#   elif y > Y:
#     for a in range(Y+1, y):
#       if is_bissetile(a):
#         nb += 1              
#   return nb 

# def days_between_mois(y, m, Y, M):
#   nb_day = 0
#   if y < Y:
#     if m != 12:
#       for mois in range(m+1, 12+1):
#         nb_day += nb_jours(y, mois)
#         # print(nb_jours(y, mois))
#         # print(nb_day)
#     if M != 1:
#       for mois in range(1, M):
#         nb_day += nb_jours(Y, mois)
#         # print("%d:%d" %(mois, nb_jours(y, mois)))
#         # print(nb_day)
#   elif y > Y:
#     if M != 12:
#       for mois in range(M+1, 12+1):
#         nb_day += nb_jours(Y, mois)
#     if m != 1:
#       for mois in range(1, m):
#         nb_day += nb_jours(y, mois)
#   else:
#     if m < M:
#       for mois in range(m+1, M):
#         nb_day += nb_jours(y, mois)
#     elif m > M:
#       for mois in range(M+1, m):
#         nb_day += nb_jours(y, mois)
#     return 0  
#   return nb_day  

# def days_between(y, m, d, Y, M, D):
#   assert is_valid_date(y, m, d) and is_valid_date(Y, M, D)
#   if y < Y:
#     days_between = nb_jours(y, m) - d + D
#     # print(days_between)
#   elif y > Y:
#     days_between = nb_jours(Y, M) - D + d
#     # print(days_between)

#   else:
#     if m < M:
#       days_between = nb_jours(y, m) - d + D
#       # print(days_between)
#     elif m > M:
#       days_between = nb_jours(Y, M) - D + d
#       # print(days_between)
#     else:
#       days_between = D - d
#       # print(days_between)

#   days_between += days_between_mois(y, m, Y, M)
#   if y != Y:
#     days_between += nb_anne_bissetile(y, Y) + (abs(Y-y)-1)*365
#   if y > Y:
#     return -days_between
#   else:  
#     return days_between  

# print(nb_anne_bissetile(1985, 2017))
# print(days_between_mois(1985,10,2017,9))   
# print(days_between(2020, 2, 25, 2020, 2, 13))

def days_in_year(y):
  return 366 if is_bissetile(y) else 365

def day_num_in_year(y, m, d):
  return sum(nb_jours(y, _m) for _m in range(1, m)) + d  

def days_between_corr(y, m, d, Y, M, D):
  if (Y, M, D) < (y, m, d):
    return -days_between_corr(Y, M, D, y, m, d)
  n, N = day_num_in_year(y, m, d), day_num_in_year(Y, M, D)
  return sum(days_in_year(yy) for yy in range(y, Y)) + N - n  

def weekday_hard(y, m, d):
  assert is_valid_date(y, m, d)
  return (days_between_corr(1900, 1, 1, y, m, d) + 1) % 7

# print(weekday_hard(1700, 1, 4))

def cal(y, m, weekday="weekday_hard"):
  cal = []
  cal.append(["di", "lu", "ma", "me", "je", "ve", "sa"])
  week = []
  
  if weekday == weekday_hard:
    first_day = weekday_hard(y,m, 1)
  else:
    first_day = weekday_delambre(y, m, 1)  
  for day in range(0, first_day+1):
    if day != first_day:
      week.append(0)
    else:
      week.append(1)
  for day in range(2, nb_jours(y, m) + 1):
    if len(week) == 7:
      cal.append(week.copy())
      # print(cal)
      week.clear()
    week.append(day)
    if day == nb_jours(y, m):
      cal.append(week.copy())
      week.clear()
      # print(cal)

  for week in cal:
    for day in week:
        if day == 0:
          print("", end="\t")
        else:
          print(day, end="\t")    
    print("\n")

  # print(cal)  

# for m in range(1, 13):
#   print(cal(2018, m))            

def weekday_delambre(y, m, d):
  code_mois_normal = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
  code_mois_bissetile = [3, 6, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
  if is_bissetile(y):
    K = d + code_mois_bissetile[m-1] + int((21/4) * (y/100)) + int((5/4) * (y%100)) + 2
  else:
    K = d + code_mois_normal[m-1] + int((21/4) * (y/100)) + int((5/4) * (y%100)) + 2
  return K % 7

# cal(2018, 9, weekday="weekday_delambre")

def daysgen(y, m, d, Y, M, D,week=False):
  if week == False:
    while y != Y or m != M or d != D:
      yield y, m, d
      if d == nb_jours(y, m):
        if m == 12:
          m, d = 1, 1
          y += 1
        else:
          m += 1
          d = 1
      else:
        d += 1
  else:
    weekday = weekday_hard(y, m, d)
    while y != Y or m != M or d != D:
      yield (y, m, d), weekday
      if d == nb_jours(y, m):
        if m == 12:
          m, d = 1, 1
          y += 1    
        else:
          m += 1
          d = 1
      else:
        d += 1
      if weekday == 6:
        weekday = 0
      else:
        weekday += 1    



# print(list(daysgen(2019, 2, 28, 2019, 3, 2)))
assert sum(1 for _ in daysgen(1985, 10, 21, 2017, 9, 19)) == 11656


# print(list((date(*t).weekday()+1)%7 for t in daysgen(1800, 1, 1, 1800, 12, 31)))
# print(list(weekday_hard(*t) for t in daysgen(1800, 1, 1, 1800, 12, 31)))
assert all( (date(*t).weekday()+1)%7 == weekday_hard(*t)
           for t in daysgen(1800, 1, 1, 2100, 1, 1))

print(weekday_hard(1899, 12, 31))
print(list(daysgen(1899, 12, 31, 1900, 1, 4, True)))

assert list(daysgen(1899, 12, 31, 1900, 1, 4, True)) == [((1899, 12, 31), 0), ((1900, 1, 1), 1), ((1900, 1, 2), 2), ((1900, 1, 3), 3)]