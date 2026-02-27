   
import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(page_title="Matplotlib Charts", layout="wide")
# ---------------- Line Chart ---------------
st.subheader("Line Chart")
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.subplot(2,2,1)
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title("Line Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
st.pyplot(plt)
# ---------------- Bar Chart ---------------
st.subheader("Bar Chart")
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
plt.subplot(2,2,2)
plt.figure(figsize=(2,1))
plt.bar(categories, values, color='green')
plt.title("Bar Chart Example")
st.pyplot(plt)
# ---------------- Scatter Plot ---------------
st.subheader("Scatter Plot")
x_scatter = [5, 7, 8, 7, 2, 17]
y_scatter = [99, 86, 87, 88, 100, 86]
plt.figure(figsize=(2,1))
plt.scatter(x_scatter, y_scatter, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
st.pyplot(plt)
# ---------------- Histogram ---------------
st.subheader("Histogram")
data = [22, 55, 62, 45, 21, 22, 34, 42, 42, 60]
plt.figure(figsize=(2,1))
plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.title("His0togram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
st.pyplot(plt)