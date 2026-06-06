import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("AI Dashboard Project")

# Load Dataset
df = pd.read_csv("dataset.csv")

# Dataset Overview
st.header("Dataset Overview")
st.write(df.head())

# Data Cleaning
st.header("Data Cleaning")
st.write("Missing Values:")
st.write(df.isnull().sum())

df = df.dropna()

# KPI Section
st.header("Key Metrics")

st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

# Interactive Filter
st.header("Filters")

column = st.selectbox("Select Column", df.columns)

if df[column].dtype == 'object':
    option = st.selectbox("Select Value", df[column].unique())
    filtered_df = df[df[column] == option]
else:
    filtered_df = df

st.write(filtered_df)

# Visualization 1
st.header("Visualization 1")
st.bar_chart(df.select_dtypes(include='number'))

# Visualization 2
st.header("Visualization 2")

numeric_cols = df.select_dtypes(include='number').columns

if len(numeric_cols) >= 2:
    fig, ax = plt.subplots()
    sns.scatterplot(
        x=numeric_cols[0],
        y=numeric_cols[1],
        data=df,
        ax=ax
    )
    st.pyplot(fig)

# Visualization 3
st.header("Visualization 3")

if len(numeric_cols) >= 1:
    fig, ax = plt.subplots()
    sns.histplot(df[numeric_cols[0]], kde=True, ax=ax)
    st.pyplot(fig)

# Visualization 4
st.header("Visualization 4")

if len(numeric_cols) >= 2:
    fig, ax = plt.subplots()
    sns.lineplot(
        x=numeric_cols[0],
        y=numeric_cols[1],
        data=df,
        ax=ax
    )
    st.pyplot(fig)

# Visualization 5
st.header("Visualization 5")

if len(numeric_cols) >= 2:
    fig, ax = plt.subplots()
    sns.heatmap(df[numeric_cols].corr(), annot=True, ax=ax)
    st.pyplot
