import streamlit as st
st.set_page_config(
    page_title="Shopping Bill Generator",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Shopping Bill Generator")
st.write("Enter product details to generate a formatted shopping bill.")

st.subheader("Add Products")

num_products = st.number_input(
    "Number of Products",
    min_value=1,
    max_value=20,
    value=3,
    step=1
)

products = []

for i in range(int(num_products)):
    st.markdown(f"### Product {i + 1}")

    col1, col2, col3 = st.columns(3)

    with col1:
        product_name = st.text_input(
            "Product Name",
            key=f"name_{i}"
        )

    with col2:
        quantity = st.number_input(
            "Quantity",
            min_value=1,
            value=1,
            step=1,
            key=f"quantity_{i}"
        )

    with col3:
        price = st.number_input(
            "Price (₹)",
            min_value=0.0,
            value=0.0,
            step=0.01,
            key=f"price_{i}"
        )

    products.append({
        "name": product_name,
        "quantity": quantity,
        "price": price
    })

st.subheader("Bill Settings")

col1, col2 = st.columns(2)

with col1:
    discount_percent = st.number_input(
        "Discount (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
    )

with col2:
    tax_percent = st.number_input(
        "Tax / GST (%)",
        min_value=0.0,
        max_value=100.0,
        value=18.0,
        step=1.0
    )

if st.button("🧾 Generate Bill", use_container_width=True):

    valid_products = [
        product for product in products
        if product["name"].strip() and product["quantity"] > 0
    ]

    if not valid_products:
        st.error("Please enter at least one valid product.")
    else:

        subtotal = 0

        for product in valid_products:
            product["total"] = product["quantity"] * product["price"]
            subtotal += product["total"]

        discount_amount = subtotal * (discount_percent / 100)

        amount_after_discount = subtotal - discount_amount

        tax_amount = amount_after_discount * (tax_percent / 100)

        final_amount = amount_after_discount + tax_amount



        st.success("Bill generated successfully!")

        st.markdown("---")
        st.subheader("🧾 Shopping Bill")

        st.write("**Product Details**")

        for product in valid_products:
            st.write(
                f"**{product['name']}** — "
                f"{product['quantity']} × ₹{product['price']:.2f} "
                f"= **₹{product['total']:.2f}**"
            )

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Subtotal")
            st.write("Discount")
            st.write("Amount After Discount")
            st.write("Tax / GST")
            st.write("### Final Amount")

        with col2:
            st.write(f"₹{subtotal:.2f}")
            st.write(f"- ₹{discount_amount:.2f}")
            st.write(f"₹{amount_after_discount:.2f}")
            st.write(f"+ ₹{tax_amount:.2f}")
            st.write(f"### ₹{final_amount:.2f}")

        st.markdown("---")
        st.info("Thank you for shopping! 🛍️")