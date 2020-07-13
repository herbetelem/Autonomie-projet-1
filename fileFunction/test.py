def checkInput(value, require):
  if type(value) is require:
    print("ok")
  else:
    print("ko")


checkInput("test", str)