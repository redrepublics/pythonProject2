Pi = 3.14
def fun_test_z(r):
  global Pi
  print(Pi)
  return Pi*(r**2)
fun_test_zz = fun_test_z(int(input("Введите радииус и мы узнаем площадь круга\n")))
print(fun_test_zz)
