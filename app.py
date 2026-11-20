import pandas as pd
import streamlit as st


def main():
    st.set_page_config(
        page_title="Machine Learning Coach",
        layout="centered",
    )

    st.title("Machine Learning Coach")
    st.write(
        "Review your dataset before starting a "
        "classification modeling project."
    )

    uploaded_file = st.file_uploader(
        "Upload a CSV file",
        type=["csv"],
    )

    if uploaded_file is None:
        st.info("Upload a CSV file to preview it and check its target labels.")
        return

    try:
        data = pd.read_csv(uploaded_file)
    except (
        pd.errors.EmptyDataError,
        pd.errors.ParserError,
        UnicodeDecodeError,
        OSError,
        ValueError,
    ) as error:
        st.error(f"Could not read this CSV file: {error}")
        return

    if data.empty:
        st.error("This CSV has column headers but no data rows.")
        return

    if len(data.columns) == 0:
        st.error("This CSV does not contain any columns.")
        return

    st.subheader("Dataset profile")
    profile_col1, profile_col2 = st.columns(2)
    profile_col1.metric("Rows", len(data))
    profile_col2.metric("Columns", len(data.columns))

    st.subheader("Data preview")
    st.dataframe(data.head(10), use_container_width=True)

    target_column = st.selectbox(
        "Select the classification target column",
        options=list(data.columns),
    )

    st.subheader("Missing target labels")
    missing_mask = data[target_column].isna()
    missing_count = int(missing_mask.sum())

    if missing_count == 0:
        st.success(f"No missing labels found in `{target_column}`.")
    else:
        # CSV row 1 is the header, so the first data row is row 2.
        source_rows = (data.index[missing_mask] + 2).tolist()
        st.warning(
            f"Found {missing_count} missing label(s) in "
            f"`{target_column}`. Review CSV record row(s): "
            f"{', '.join(map(str, source_rows))}."
        )

    st.caption(
        "A missing target label needs review before classification analysis. "
        "This check does not change or remove any data."
    )


if __name__ == "__main__":
    main()