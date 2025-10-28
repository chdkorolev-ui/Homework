x = int(input())
if (x // 100 + x // 10 % 10 + x % 10) % 2 == 0:
  print("True")
else:
  print("False")
