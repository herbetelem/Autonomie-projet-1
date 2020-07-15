def checkInput(value, require):
  while type(value) is not require:
    value = input(f"On vous a demander une {require}")

checkInput(5, str)