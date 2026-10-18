import streamlit as st
import requests
from bs4 import BeautifulSoup
import csv
import io
from urllib.parse import urljoin

st.set_page_config(
    page_title="Web Scraping Program",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Web Scraping Program")
st.write(
    "Extract publicly available structured information from a permitted webpage "
    "and export the results as CSV."
)

def scrape_books(base_url, max_pages):
    all_books = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for page_number in range(1, max_pages + 1):

        if page_number == 1:
            url = base_url
        else:
            url = urljoin(base_url, f"catalogue/page-{page_number}.html")

        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()

        except requests.RequestException as e:
            st.warning(
                f"Could not access page {page_number}: {e}"
            )
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.select("article.product_pod")

        if not products:
            break

        for product in products:

            # Book title
            title_tag = product.select_one("h3 a")
            title = (
                title_tag.get("title", "").strip()
                if title_tag
                else "N/A"
            )

            # Price
            price_tag = product.select_one(".price_color")
            price = (
                price_tag.get_text(strip=True)
                if price_tag
                else "N/A"
            )

            # Rating
            rating_tag = product.select_one(".star-rating")

            if rating_tag:
                rating_classes = rating_tag.get("class", [])
                rating = (
                    rating_classes[-1]
                    if len(rating_classes) > 1
                    else "N/A"
                )
            else:
                rating = "N/A"

            # Availability
            availability_tag = product.select_one(".availability")
            availability = (
                availability_tag.get_text(" ", strip=True)
                if availability_tag
                else "N/A"
            )

            # Product URL
            link_tag = product.select_one("h3 a")

            if link_tag and link_tag.get("href"):
                product_url = urljoin(
                    url,
                    link_tag.get("href")
                )
            else:
                product_url = "N/A"

            all_books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability,
                "Product URL": product_url
            })

    return all_books

st.sidebar.header("⚙️ Scraping Settings")

default_url = "https://books.toscrape.com/"

url = st.sidebar.text_input(
    "Website URL",
    value=default_url
)

max_pages = st.sidebar.number_input(
    "Number of Pages",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

st.sidebar.info(
    "Use only websites where automated access is permitted "
    "and respect robots.txt and website terms."
)

if st.button("🚀 Start Scraping", type="primary"):

    if not url.strip():
        st.error("Please enter a valid URL.")

    else:

        with st.spinner("Scraping webpage..."):

            data = scrape_books(
                url.strip(),
                int(max_pages)
            )

        if data:

            st.success(
                f"Successfully extracted {len(data)} records."
            )

            # Store data in session state
            st.session_state["scraped_data"] = data

        else:

            st.warning(
                "No data was extracted. "
                "Check the URL and webpage structure."
            )


if "scraped_data" in st.session_state:

    data = st.session_state["scraped_data"]

    st.subheader("📊 Extracted Data")

    st.dataframe(
        data,
        use_container_width=True
    )

    st.subheader("📈 Scraping Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Records",
            len(data)
        )

    with col2:
        st.metric(
            "Fields Extracted",
            len(data[0])
        )

    csv_buffer = io.StringIO()

    fieldnames = [
        "Title",
        "Price",
        "Rating",
        "Availability",
        "Product URL"
    ]

    writer = csv.DictWriter(
        csv_buffer,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(data)

    csv_data = csv_buffer.getvalue()

    st.subheader("📥 Download Dataset")

    st.download_button(
        label="⬇️ Download CSV",
        data=csv_data,
        file_name="scraped_books.csv",
        mime="text/csv"
    )


    with st.expander("ℹ️ Extracted Field Explanation"):

        st.write("""
        **Title:** Name of the book extracted from the webpage.

        **Price:** Listed price of the book.

        **Rating:** Star rating available on the webpage.

        **Availability:** Availability status of the product.

        **Product URL:** Direct URL of the product page.
        """)