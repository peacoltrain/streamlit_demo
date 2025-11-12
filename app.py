import streamlit as st
import pandas as pd

def main():
    st.title("Iris Dataset")

    st.markdown(
        """
        This is a fun first app that can be used to explore the Iris Dataset.
        Here is jsut the first 10 entries of the dataset!
        """
    )

    df = pd.read_csv("Iris.csv")

    st.dataframe(df.head(5))

    S, P = st.tabs(['Sepal', 'Petal'])

    with S:
        st.scatter_chart(data=df, x='SepalLengthCm', y='SepalWidthCm')

    with P:
        st.scatter_chart(data=df, x='PetalLengthCm', y='PetalWidthCm')

if __name__ == "__main__":
    main()
