
import streamlit as st


def main():
    st.set_page_config(
        page_title="Machine Learning Coach",
        layout="centered",
    )

    st.title("Machine Learning Coach")

    st.write(
        "Review your dataset before starting a "
        "machine learning project."
    )

    st.info(
        "The first feature will load a CSV file and "
        "check for missing target labels."
    )


if __name__ == "__main__":
    main()
