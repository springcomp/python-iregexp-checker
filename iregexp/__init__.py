from iregexp.checker import IRegexpChecker

__version__ = '0.6.0'

def check(expression, nothrow = True):
  try:
    print(expression)
    checker = IRegexpChecker()
    for ch in expression:
      checker.check(ord(ch))

    checker.finalCheck()
    return (True, None)

  except Exception as e:
    if nothrow:
      return (False, None)
    else:
      raise e