from matplotlib import pyplot as plt

def plotInfo(tbl, text, valX, valY):
  tbl.plot(figsize = (10, 7), title = text)
  plt.xlabel(valX)
  plt.ylabel(valY)
  plt.show()
