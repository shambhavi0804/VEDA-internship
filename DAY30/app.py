import re
from collections import Counter

import pandas as pd
import streamlit as st

# Common/combined Apache and Nginx access-log format
LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+)\s+\S+\s+\S+\s+'
    r'\[(?P<timestamp>[^\]]+)\]\s+'
    r'"(?P<method>\S+)\s+(?P<endpoint>\S+)(?:\s+[^"]*)?"\s+'
    r'(?P<status>\d{3})\s+'
    r'(?P<size>\S+)'
)


def parse_log(text: str):
    """Return parsed rows and the number of lines that did not match."""
    rows = []
    malformed = 0

    for line in text.splitlines():
        if not line.strip():
            continue

        match = LOG_PATTERN.match(line)
        if not match:
            malformed += 1
            continue

        data = match.groupdict()
        try:
            rows.append({
                "IP address": data["ip"],
                "Timestamp": data["timestamp"],
                "Method": data["method"],
                "Endpoint": data["endpoint"],
                "Status code": int(data["status"]),
                "Bytes": int(data["size"]) if data["size"].isdigit() else None,
            })
        except (TypeError, ValueError):
            malformed += 1

    return rows, malformed


st.set_page_config(page_title="Log File Analyzer", page_icon="📊", layout="wide")
st.title("📊 Log File Analyzer")
st.write(
    "Upload a server access log to explore request volume, errors, "
    "frequent IP addresses, and popular endpoints."
)

uploaded_file = st.file_uploader("Choose a .log or .txt file", type=["log", "txt"])

if uploaded_file:
    log_text = uploaded_file.getvalue().decode("utf-8", errors="replace")
    rows, malformed_count = parse_log(log_text)

    if not rows:
        st.error("No lines matched the supported access-log format.")
        st.caption(f"Malformed or unsupported lines: {malformed_count}")
    else:
        df = pd.DataFrame(rows)
        error_count = int((df["Status code"] >= 400).sum())

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Valid requests", len(df))
        col2.metric("Error responses (4xx/5xx)", error_count)
        col3.metric("Unique IP addresses", df["IP address"].nunique())
        col4.metric("Malformed lines", malformed_count)

        st.subheader("Most frequent IP addresses")
        ip_counts = Counter(df["IP address"])
        st.bar_chart(
            pd.DataFrame(ip_counts.most_common(10), columns=["IP address", "Requests"])
            .set_index("IP address")
        )

        st.subheader("Most requested endpoints")
        endpoint_counts = Counter(df["Endpoint"])
        st.dataframe(
            pd.DataFrame(
                endpoint_counts.most_common(10),
                columns=["Endpoint", "Requests"],
            ),
            use_container_width=True,
            hide_index=True,
        )

        st.subheader("Status-code counts")
        status_counts = df["Status code"].value_counts().sort_index()
        st.bar_chart(status_counts)

        st.subheader("Parsed log entries")
        st.dataframe(df, use_container_width=True, hide_index=True)

        csv_data = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download parsed entries as CSV",
            data=csv_data,
            file_name="log_analysis.csv",
            mime="text/csv",
        )

        st.caption(
            "Parsing supports a common Apache/Nginx combined access-log format. "
            "Other log formats may need a different parsing pattern."
        )