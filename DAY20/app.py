import streamlit as st
import csv
import io
st.set_page_config(
    page_title="CSV Data Processor",
    page_icon="📊",
    layout="wide"
)
st.title("📊 CSV Data Processor")
st.write(
    "Upload a CSV file to analyze records and generate "
    "useful statistical summaries."
)

st.divider()
uploaded_file = st.file_uploader(
    "📁 Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        # Read uploaded CSV
        content = uploaded_file.getvalue().decode("utf-8")

        reader = csv.DictReader(io.StringIO(content))
        rows = list(reader)

        if not rows:
            st.warning("The CSV file is empty.")
            st.stop()

        columns = reader.fieldnames

        if not columns:
            st.error("No columns found in the CSV file.")
            st.stop()
        st.subheader("📋 Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Records", len(rows))

        with col2:
            st.metric("Total Columns", len(columns))

        with col3:
            st.metric("File Name", uploaded_file.name)
        st.subheader("👀 Uploaded Data")

        st.dataframe(
            rows,
            use_container_width=True
        )
        st.subheader("📈 Statistical Analysis")

        numeric_columns = []

        for column in columns:
            valid_values = []

            for row in rows:
                value = row.get(column, "").strip()

                if value:
                    try:
                        valid_values.append(float(value))
                    except ValueError:
                        pass

            if valid_values:
                numeric_columns.append(column)

        if not numeric_columns:
            st.warning(
                "No numeric columns were found in the uploaded CSV."
            )
            st.stop()

        selected_column = st.selectbox(
            "Select a numeric column to analyze:",
            numeric_columns
        )
        valid_values = []
        invalid_count = 0
        missing_count = 0

        for row in rows:
            value = row.get(selected_column, "").strip()

            if value == "":
                missing_count += 1
                continue

            try:
                valid_values.append(float(value))
            except ValueError:
                invalid_count += 1

        if not valid_values:
            st.error(
                "No valid numeric values found in this column."
            )
            st.stop()

        total = sum(valid_values)
        average = total / len(valid_values)
        highest = max(valid_values)
        lowest = min(valid_values)
        count = len(valid_values)
        stat1, stat2, stat3, stat4 = st.columns(4)

        with stat1:
            st.metric(
                "🔢 Valid Count",
                count
            )

        with stat2:
            st.metric(
                "➕ Total",
                f"{total:,.2f}"
            )

        with stat3:
            st.metric(
                "📊 Average",
                f"{average:,.2f}"
            )

        with stat4:
            st.metric(
                "🏆 Highest",
                f"{highest:,.2f}"
            )

        st.divider()
        col1, col2, col3 = st.columns(3)

        with col1:
            st.info(f"**Lowest Value:** {lowest:,.2f}")

        with col2:
            st.warning(f"**Missing Values:** {missing_count}")

        with col3:
            st.error(f"**Invalid Values:** {invalid_count}")
        st.subheader("📝 Summary Report")

        summary = f"""
CSV Data Processing Summary

File Name       : {uploaded_file.name}
Total Records   : {len(rows)}
Total Columns   : {len(columns)}

Analyzed Column : {selected_column}

Valid Values    : {count}
Missing Values  : {missing_count}
Invalid Values  : {invalid_count}

Total           : {total:,.2f}
Average         : {average:,.2f}
Highest         : {highest:,.2f}
Lowest          : {lowest:,.2f}
"""

        st.code(summary, language="text")
        st.download_button(
            label="⬇️ Download Summary Report",
            data=summary,
            file_name="csv_summary_report.txt",
            mime="text/plain"
        )

    except UnicodeDecodeError:
        st.error(
            "Unable to read the CSV file. "
            "Please upload a UTF-8 encoded CSV file."
        )

    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

else:
    st.info(
        "👆 Upload a CSV file to start processing."
    )

    st.subheader("📌 Example CSV Format")

    example_csv = """Employee,Department,Salary
John,IT,45000
Priya,HR,40000
Rahul,Finance,50000
Anita,IT,55000
"""

    st.code(example_csv, language="csv")

    st.write(
        "The processor can analyze numeric columns such as "
        "Salary, Sales, Marks, Quantity, Revenue, etc."
    )