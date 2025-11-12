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

    S, P = st.tabs(['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])

    with S:
        st.scatter_chart(data=df, x='SepalLengthCM', y='SepalWidthCM')

    with P:
        st.scatter_chart(data=df, x='PetalLengthCM', y='PetalWidthCM')

if __name__ == "__main__":
    main()
