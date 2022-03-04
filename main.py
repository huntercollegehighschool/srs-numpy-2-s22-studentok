import os

program = input("Enter A, B, or C: ").upper()

while program not in ["A", "B", "C"]:
  os.system('clear')
  print("Not a valid input.")
  program = input("Enter A, B, or C: ").upper()

if program == "A":
  import AColumnCypher
elif program == "B":
  import BPercentDailyReturn
elif program == "C":
  import CWindStatistics