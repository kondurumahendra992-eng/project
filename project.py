import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv')
df

plt.plot(df.index, df['SepalLength'])
plt.xlabel('Index')
plt.ylabel('Sepal Length')
plt.title(' Index vs Sepal Length')
plt.show()

print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.info())
print(df.columns)
print(df.dtypes)

print("Average SepalLength:", df["SepalLength"].mean())
print("Average petal length:", df["PetalLength"].mean())
print("Maximum Sepal Length:", df["SepalLength"].max())
print("Minimum Petal Width:", df["PetalWidth"].min())
print("Total Number of Species:", df["Species"].nunique())
print(df["Species"].value_counts())

import numpy as np
print("Mean of Sepal Length:", np.mean(df["SepalLength"]))
print("Mean of Petal Length:", np.mean(df["PetalLength"]))
print("Median of Sepal Length:", np.median(df["SepalLength"]))
print("Median of Petal Length:", np.median(df["PetalLength"]))
print("Maximum Sepal Length:", np.max(df["SepalLength"]))
print("Maximum Petal Length:", np.max(df["PetalLength"]))
print("Minimum Sepal Length:", np.min(df["SepalLength"]))
print("Minimum Petal Length:", np.min(df["PetalLength"]))
print("Standard Deviation of Sepal Length:", np.std(df["SepalLength"]))
print("Standard Deviation of Petal Length:", np.std(df["PetalLength"]))

import matplotlib.pyplot as plt
import os
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.figure(figsize=(8, 5))
plt.plot(df.index, df["SepalLength"], marker="o")
plt.title("Sepal Length by Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, "line_chart_sepal_length.png"))
plt.show()

species_counts = df["Species"].value_counts()

plt.figure(figsize=(6, 5))
species_counts.plot(kind="bar")
plt.title("Species Count")
plt.xlabel("Species")
plt.ylabel("Count")
plt.savefig(os.path.join(OUTPUT_DIR, "bar_chart_species_count.png"))
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["SepalLength"], df["PetalLength"])
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.savefig(os.path.join(OUTPUT_DIR, "scatter_plot.png"))
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["SepalWidth"], bins=10)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.savefig(os.path.join(OUTPUT_DIR, "histogram_sepal_width.png"))
plt.show()

print("All charts saved successfully in the 'output' folder.")

import plotly.express as px
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

fig1 = px.scatter(
    df,
    x="SepalLength",
    y="PetalLength",
    color="Species",
    title="Sepal Length vs Petal Length"
)
fig1.update_layout(
    xaxis_title="Sepal Length",
    yaxis_title="Petal Length"
)
fig1.write_html(f"{OUTPUT_DIR}/scatter_plot.html")
fig1.show()

fig2 = px.box(
    df,
    x="Species",
    y="PetalLength",
    title="Petal Length Distribution by Species"
)
fig2.update_layout(
    xaxis_title="Species",
    yaxis_title="Petal Length"
)
fig2.write_html(f"{OUTPUT_DIR}/box_plot.html")
fig2.show()

fig3 = px.histogram(
    df,
    x="SepalLength",
    title="Distribution of Sepal Length"
)
fig3.update_layout(
    xaxis_title="Sepal Length",
    yaxis_title="Count"
)
fig3.write_html(f"{OUTPUT_DIR}/histogram.html")
fig3.show()

species_count = df["Species"].value_counts().reset_index()
species_count.columns = ["Species", "Count"]

fig4 = px.pie(
    species_count,
    names="Species",
    values="Count",
    title="Species Distribution"
)
fig4.write_html(f"{OUTPUT_DIR}/pie_chart.html")
fig4.show()

print("All Plotly charts saved successfully in the output folder.")

marks = [78, 82, 91, 65, 88]
marks.append(95)
print("Updated Marks:", marks)

marks.remove(65)
print("After removing a Mark:", marks)

marks.sort()
print("Sorted Marks:", marks)

highest_mark = max(marks)
print("Highest Mark:", highest_mark)

lowest_mark = min(marks)
print("Lowest Mark:", lowest_mark)