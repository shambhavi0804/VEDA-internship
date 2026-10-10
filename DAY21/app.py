import streamlit as st
import json
import pandas as pd
st.set_page_config(
    page_title="JSON Data Processor",
    page_icon="🗂️",
    layout="wide"
)
st.title("🗂️ JSON Data Processor")
st.write(
    "Upload a JSON file to search, filter, analyze, "
    "and summarize structured data."
)

st.divider()

uploaded_file = st.file_uploader(
    "📁 Upload a JSON file",
    type=["json"]
)

def flatten_records(data):
    """
    Convert supported JSON structures into a list of dictionaries.
    """

    if isinstance(data, list):
        return data

    if isinstance(data, dict):

        # Common nested keys
        for key in ["employees", "students", "products", "data", "records"]:
            if key in data and isinstance(data[key], list):
                return data[key]

        # Single dictionary record
        return [data]

    return []
if uploaded_file is not None:

    try:
        # Read JSON file
        data = json.load(uploaded_file)

        records = flatten_records(data)

        if not records:
            st.warning("No records found in the JSON file.")
            st.stop()

        # Keep dictionary records only
        records = [
            record for record in records
            if isinstance(record, dict)
        ]

        if not records:
            st.error("JSON does not contain valid dictionary records.")
            st.stop()
        st.subheader("📊 Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Records", len(records))

        with col2:
            all_keys = set()

            for record in records:
                all_keys.update(record.keys())

            st.metric("Fields", len(all_keys))

        with col3:
            st.metric("File Name", uploaded_file.name)

        st.subheader("👀 JSON Data")

        dataframe = pd.DataFrame(records)

        st.dataframe(
            dataframe,
            use_container_width=True
        )
        st.subheader("🔎 Search Records")

        search_text = st.text_input(
            "Enter a keyword to search:"
        )

        search_results = records

        if search_text:

            search_text = search_text.lower()

            search_results = [
                record
                for record in records
                if search_text in str(record).lower()
            ]

            st.info(
                f"Found {len(search_results)} matching record(s)."
            )

            if search_results:
                st.dataframe(
                    pd.DataFrame(search_results),
                    use_container_width=True
                )
            else:
                st.warning("No matching records found.")
        st.subheader("🔽 Filter Records")

        filter_column = st.selectbox(
            "Select a field:",
            ["None"] + list(dataframe.columns)
        )

        filtered_records = records

        if filter_column != "None":

            values = sorted(
                dataframe[filter_column]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            if values:

                selected_value = st.selectbox(
                    f"Select {filter_column}:",
                    values
                )

                filtered_records = [
                    record
                    for record in records
                    if str(record.get(filter_column, "")) == selected_value
                ]

                st.success(
                    f"{len(filtered_records)} record(s) found."
                )

                st.dataframe(
                    pd.DataFrame(filtered_records),
                    use_container_width=True
                )
        st.subheader("📈 Numeric Summary")

        numeric_columns = []

        for column in dataframe.columns:

            converted = pd.to_numeric(
                dataframe[column],
                errors="coerce"
            )

            if converted.notna().any():
                numeric_columns.append(column)

        if numeric_columns:

            selected_numeric = st.selectbox(
                "Select a numeric field:",
                numeric_columns
            )

            numeric_values = pd.to_numeric(
                dataframe[selected_numeric],
                errors="coerce"
            ).dropna()

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Count",
                    len(numeric_values)
                )

            with col2:
                st.metric(
                    "Total",
                    f"{numeric_values.sum():,.2f}"
                )

            with col3:
                st.metric(
                    "Average",
                    f"{numeric_values.mean():,.2f}"
                )

            with col4:
                st.metric(
                    "Highest",
                    f"{numeric_values.max():,.2f}"
                )

            st.write(
                f"**Lowest {selected_numeric}:** "
                f"{numeric_values.min():,.2f}"
            )

        else:
            st.info(
                "No numeric fields were detected."
            )
        st.subheader("📝 Data Summary")

        summary = {
            "File Name": uploaded_file.name,
            "Total Records": len(records),
            "Total Fields": len(all_keys),
            "Search Matches": len(search_results),
            "Filtered Records": len(filtered_records)
        }

        st.json(summary)
        filtered_json = json.dumps(
            filtered_records,
            indent=4
        )

        st.download_button(
            label="⬇️ Download Filtered JSON",
            data=filtered_json,
            file_name="filtered_results.json",
            mime="application/json"
        )

    except json.JSONDecodeError:
        st.error(
            "❌ Invalid JSON file. Please upload a properly formatted JSON file."
        )

    except Exception as e:
        st.error(
            f"❌ An unexpected error occurred: {e}"
        )

else:
    st.info(
        "👆 Upload a JSON file to start processing."
    )

    st.subheader("📌 Example JSON Format")

    example_json = {
        "employees": [
            {
                "id": 101,
                "name": "John",
                "department": "IT",
                "salary": 50000
            },
            {
                "id": 102,
                "name": "Priya",
                "department": "HR",
                "salary": 45000
            },
            {
                "id": 103,
                "name": "Rahul",
                "department": "Finance",
                "salary": 60000
            },
            {
                "id": 104,
                "name": "Anita",
                "department": "IT",
                "salary": 55000
            }
        ]
    }

    st.json(example_json)