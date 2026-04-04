import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

marks =([45, 67, 78, 56, 89, 90, 34, 76, 88, 54, 69, 73, 81, 47, 92, 60, 71, 84, 58, 77])
score = ([450, 670, 780, 560, 890, 900, 340, 760, 880, 540, 690, 730, 810, 470, 920, 600, 710, 840, 580, 770])

df = pd.DataFrame({"Marks": marks, "Score": score})
print(df)
print(df.describe())
plt.bar(df["Marks"], df["Score"])
plt.xlabel("Marks")
plt.ylabel("Score")
plt.title("Marks vs Score")
plt.show()

