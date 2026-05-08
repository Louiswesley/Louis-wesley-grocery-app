import streamlit as st
from groq import Groq
import json
from datetime import datetime
import time

# Enhanced Page Setup with Modern Styling
st.set_page_config(
    page_title="Louis Wesley Grocery Store",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/louiswesley',
        'Report a bug': 'https://github.com/louiswesley/grocery-app/issues',
        'About': 'Built with ❤️ by Louis Wesley'
    }
)

# Custom CSS for Modern UI
st.markdown("""
<style>
    :root {
        color-scheme: dark;
        font-family: 'Inter', sans-serif;
    }

    body {
        background: radial-gradient(circle at top, rgba(59, 179, 255, 0.14), transparent 24%),
                    radial-gradient(circle at bottom right, rgba(205, 88, 255, 0.14), transparent 24%),
                    linear-gradient(180deg, #08101f 0%, #0c182d 100%);
        overflow-x: hidden;
    }

    .stApp {
        background: transparent !important;
    }

    .main-header {
        background: rgba(14, 23, 39, 0.88);
        color: #f5f7ff;
        padding: 2.5rem 2rem;
        border-radius: 28px;
        margin-bottom: 2rem;
        text-align: left;
        box-shadow: 0 28px 80px rgba(0, 0, 0, 0.35);
        backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .nav-bar {
        background: rgba(12, 18, 33, 0.92);
        padding: 1rem 1rem 0.9rem;
        border-radius: 28px;
        margin-bottom: 1.8rem;
        box-shadow: 0 18px 50px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(18px);
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .nav-button {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #e8eef9;
        padding: 0.95rem 1.4rem;
        border-radius: 999px;
        font-weight: 600;
        letter-spacing: 0.02em;
        transition: all 0.25s ease;
        backdrop-filter: blur(16px);
    }

    .nav-button:hover {
        background: rgba(255, 255, 255, 0.14);
        border-color: rgba(255, 255, 255, 0.22);
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.18);
    }

    .nav-button-active {
        background: linear-gradient(135deg, #5d8cff 0%, #2b76ff 100%) !important;
        color: white !important;
        border-color: rgba(255, 255, 255, 0.28) !important;
        box-shadow: 0 18px 30px rgba(63, 125, 255, 0.35) !important;
    }

    .product-card {
        background: rgba(14, 23, 39, 0.88);
        border-radius: 22px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.22);
        border: 1px solid rgba(255, 255, 255, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(18px);
    }

    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 26px 70px rgba(0, 0, 0, 0.28);
    }

    .product-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, rgba(91, 182, 255, 0.9), rgba(248, 146, 231, 0.9));
    }

    .product-image {
        font-size: 3.2rem;
        text-align: center;
        margin-bottom: 1.2rem;
    }

    .product-price {
        font-size: 1.45rem;
        font-weight: 700;
        color: #7ee8fa;
        margin: 0.5rem 0;
    }

    .cart-badge {
        background: #4db6ff;
        color: white;
        border-radius: 50%;
        padding: 0.35rem 0.55rem;
        font-size: 0.8rem;
        font-weight: 700;
        position: absolute;
        top: -10px;
        right: -10px;
    }

    .success-message {
        background: rgba(18, 100, 80, 0.92);
        color: #f8fff4;
        padding: 1rem;
        border-radius: 16px;
        margin: 1rem 0;
        animation: slideIn 0.45s ease-out;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    @keyframes slideIn {
        from { transform: translateY(-16px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    .hero-section {
        background: rgba(255, 255, 255, 0.08);
        color: #f4f7ff;
        padding: 3rem 2rem;
        border-radius: 32px;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
        box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.08), 0 30px 60px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(20px);
    }

    .hero-section::before {
        content: '';
        position: absolute;
        top: -20%;
        right: -15%;
        width: 220px;
        height: 220px;
        background: radial-gradient(circle, rgba(255,255,255,0.18), transparent 60%);
        filter: blur(28px);
    }

    .hero-section::after {
        content: '';
        position: absolute;
        bottom: -25%;
        left: -15%;
        width: 260px;
        height: 260px;
        background: radial-gradient(circle, rgba(95, 216, 255, 0.16), transparent 54%);
        filter: blur(28px);
    }

    .metric-card {
        background: rgba(255, 255, 255, 0.08);
        padding: 1.5rem;
        border-radius: 24px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.18);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #f4f7ff;
    }

    .checkout-summary {
        background: rgba(7, 15, 32, 0.94);
        padding: 2.2rem;
        border-radius: 30px;
        margin: 2rem 0;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 24px 80px rgba(0, 0, 0, 0.26);
        backdrop-filter: blur(22px);
    }

    .ai-chat-bubble {
        background: rgba(10, 18, 35, 0.95);
        border-radius: 28px;
        padding: 1.8rem;
        margin: 1rem 0;
        border-left: 4px solid rgba(82, 180, 255, 0.9);
        box-shadow: 0 20px 50px rgba(0,0,0,0.22);
    }

    .glass-panel {
        background: rgba(16, 24, 44, 0.9);
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 18px 40px rgba(0,0,0,0.2);
        backdrop-filter: blur(20px);
    }

    .stButton>button {
        border-radius: 999px !important;
        font-weight: 700 !important;
        transition: transform 0.25s ease, box-shadow 0.25s ease !important;
        min-height: 48px;
    }

    .stButton>button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 14px 30px rgba(0,0,0,0.18) !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(255, 255, 255, 0.05);
        padding: 0.6rem;
        border-radius: 22px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(18px);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 18px !important;
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #e8eef9 !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(93, 140, 255, 0.95), rgba(53, 187, 255, 0.95)) !important;
        color: #ffffff !important;
        box-shadow: 0 16px 30px rgba(43, 118, 255, 0.18) !important;
    }

    .css-18ni7ap.e8zbici2 {
        padding: 0 !important;
    }

    .css-1gk3yp4.egzxvld3 {
        padding: 0 !important;
    }

    .css-1d391kg {
        background-color: transparent !important;
    }

    @media (max-width: 900px) {
        .app-shell {
            padding: 1rem;
        }

        .nav-bar {
            padding: 0.8rem 0.6rem 0.7rem;
        }

        .main-header {
            padding: 1.8rem 1rem;
        }

        .product-card {
            margin: 1rem 0;
        }
    }

    .app-shell {
        max-width: 1440px;
        margin: 0 auto 2rem;
        padding: 1.8rem 2rem 2.5rem;
        border-radius: 36px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 40px 120px rgba(0,0,0,0.25);
        background: rgba(4, 11, 23, 0.88);
        backdrop-filter: blur(28px);
    }

    .section-title {
        font-size: 2.2rem;
        letter-spacing: 0.01em;
        margin-bottom: 1rem;
        color: #f7fbff;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-shell">', unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"
if 'cart' not in st.session_state:
    st.session_state.cart = {}
if 'checkout' not in st.session_state:
    st.session_state.checkout = False
if 'order_history' not in st.session_state:
    st.session_state.order_history = []
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {"name": "", "email": "", "address": ""}
if 'notifications' not in st.session_state:
    st.session_state.notifications = []

# Enhanced Product Data with More Details
products = {
    "Fruits & Vegetables": [
        {
            "name": "Organic Apples",
            "price": 3.99,
            "unit": "lb",
            "category": "Fruits",
            "image": "🍎",
            "description": "Fresh, crisp organic apples perfect for snacking",
            "rating": 4.8,
            "reviews": 124,
            "organic": True,
            "in_stock": True
        },
        {
            "name": "Bananas",
            "price": 0.59,
            "unit": "each",
            "category": "Fruits",
            "image": "🍌",
            "description": "Sweet and ripe bananas, great for smoothies",
            "rating": 4.6,
            "reviews": 89,
            "organic": False,
            "in_stock": True
        },
        {
            "name": "Fresh Spinach",
            "price": 2.49,
            "unit": "bag",
            "category": "Vegetables",
            "image": "🥬",
            "description": "Nutrient-rich fresh spinach leaves",
            "rating": 4.9,
            "reviews": 67,
            "organic": True,
            "in_stock": True
        },
        {
            "name": "Carrots",
            "price": 1.99,
            "unit": "lb",
            "category": "Vegetables",
            "image": "🥕",
            "description": "Crunchy organic carrots, perfect for cooking",
            "rating": 4.7,
            "reviews": 95,
            "organic": True,
            "in_stock": True
        },
        {
            "name": "Strawberries",
            "price": 4.99,
            "unit": "pint",
            "category": "Fruits",
            "image": "🍓",
            "description": "Juicy red strawberries, seasonally fresh",
            "rating": 4.9,
            "reviews": 156,
            "organic": False,
            "in_stock": True
        },
    ],
    "Dairy & Eggs": [
        {
            "name": "Whole Milk",
            "price": 3.49,
            "unit": "gallon",
            "category": "Dairy",
            "image": "🥛",
            "description": "Fresh whole milk from local dairy farms",
            "rating": 4.5,
            "reviews": 78,
            "organic": False,
            "in_stock": True
        },
        {
            "name": "Cheddar Cheese",
            "price": 5.99,
            "unit": "lb",
            "category": "Dairy",
            "image": "🧀",
            "description": "Aged cheddar cheese, sharp and flavorful",
            "rating": 4.8,
            "reviews": 112,
            "organic": False,
            "in_stock": True
        },
        {
            "name": "Greek Yogurt",
            "price": 1.29,
            "unit": "container",
            "category": "Dairy",
            "image": "🥄",
            "description": "Creamy Greek yogurt, high in protein",
            "rating": 4.7,
            "reviews": 203,
            "organic": False,
            "in_stock": True
        },
        {
            "name": "Free Range Eggs",
            "price": 4.99,
            "unit": "dozen",
            "category": "Eggs",
            "image": "🥚",
            "description": "Farm fresh free-range eggs",
            "rating": 4.9,
            "reviews": 145,
            "organic": True,
            "in_stock": True
        },
    ],
    "Meat & Seafood": [
        {
            "name": "Chicken Breast",
            "price": 7.99,
            "unit": "lb",
            "category": "Meat",
            "image": "🍗",
            "description": "Boneless, skinless chicken breast",
            "rating": 4.6,
            "reviews": 98,
            "organic": False,
            "in_stock": True
        },
        {
            "name": "Ground Beef",
            "price": 6.49,
            "unit": "lb",
            "category": "Meat",
            "image": "🥩",
            "description": "80/20 ground beef, perfect for burgers",
            "rating": 4.4,
            "reviews": 87,
            "organic": False,
            "in_stock": True
        },
        {
            "name": "Atlantic Salmon",
            "price": 12.99,
            "unit": "lb",
            "category": "Seafood",
            "image": "🐟",
            "description": "Fresh Atlantic salmon fillet",
            "rating": 4.9,
            "reviews": 76,
            "organic": False,
            "in_stock": True
        },
        {
            "name": "Turkey Bacon",
            "price": 4.99,
            "unit": "pack",
            "category": "Meat",
            "image": "🥓",
            "description": "Low-fat turkey bacon, 12 slices per pack",
            "rating": 4.5,
            "reviews": 134,
            "organic": False,
            "in_stock": True
        },
    ],
    "Bakery & Bread": [
        {
            "name": "Whole Wheat Bread",
            "price": 2.99,
            "unit": "loaf",
            "category": "Bread",
            "image": "🍞",
            "description": "Fresh baked whole wheat bread",
            "rating": 4.7,
            "reviews": 89,
            "organic": False,
            "in_stock": True
        },
        {
            "name": "Croissants",
            "price": 3.49,
            "unit": "pack",
            "category": "Bakery",
            "image": "🥐",
            "description": "Buttery French croissants, 6 per pack",
            "rating": 4.8,
            "reviews": 167,
            "organic": False,
            "in_stock": True
        },
        {
            "name": "Chocolate Chip Cookies",
            "price": 4.99,
            "unit": "pack",
            "category": "Bakery",
            "image": "🍪",
            "description": "Homemade chocolate chip cookies",
            "rating": 4.9,
            "reviews": 234,
            "organic": False,
            "in_stock": True
        },
    ]
}

# Enhanced Navigation Bar with Active States
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
nav_cols = st.columns([1, 1, 1, 1, 1, 2.5])

nav_buttons = [
    ("🏠 Home", "home", "nav_home"),
    ("🛍️ Shop", "shop", "nav_shop"),
    ("🤖 AI", "ai", "nav_ai"),
    ("📋 Orders", "history", "nav_orders"),
    ("👤 Profile", "profile", "nav_profile")
]

for i, (label, page, key) in enumerate(nav_buttons):
    with nav_cols[i]:
        button_type = "primary" if st.session_state.current_page == page else "secondary"
        if st.button(label, key=key, type=button_type, use_container_width=True):
            st.session_state.current_page = page
            st.session_state.checkout = False
            st.rerun()

# Enhanced Cart Display in Navigation
with nav_cols[5]:
    cart_count = sum(details['quantity'] for details in st.session_state.cart.values())
    cart_total = sum(details['price'] * details['quantity'] for details in st.session_state.cart.values())

    if cart_count > 0:
        cart_button = st.button(
            f"🛒 Cart ({cart_count}) - ${cart_total:.2f}",
            key="nav_cart",
            type="primary",
            use_container_width=True
        )
        if cart_button:
            st.session_state.checkout = True
            st.session_state.current_page = "checkout"
            st.rerun()
    else:
        st.button("🛒 Cart (0)", key="nav_cart_empty", disabled=True, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Notification System
if st.session_state.notifications:
    for notification in st.session_state.notifications:
        st.success(notification)
    st.session_state.notifications = []

# Enhanced Sidebar Cart
with st.sidebar:
    st.markdown("### 🛒 Shopping Cart")

    if st.session_state.cart:
        total = 0
        for item, details in st.session_state.cart.items():
            with st.container():
                col1, col2, col3 = st.columns([2, 1, 0.5])
                with col1:
                    st.write(f"**{item}**")
                with col2:
                    st.write(f"${details['price']:.2f} × {details['quantity']}")
                with col3:
                    if st.button("🗑️", key=f"sidebar_remove_{item}", help=f"Remove {item}"):
                        del st.session_state.cart[item]
                        st.rerun()

                item_total = details['price'] * details['quantity']
                total += item_total
                st.caption(f"Subtotal: ${item_total:.2f}")

        st.divider()
        st.markdown(f"### 💰 Total: ${total:.2f}")

        if st.button("🚀 Proceed to Checkout", type="primary", use_container_width=True):
            st.session_state.checkout = True
            st.session_state.current_page = "checkout"
            st.rerun()

        if st.button("🗑️ Clear All", use_container_width=True):
            st.session_state.cart = {}
            st.success("Cart cleared!")
            time.sleep(0.5)
            st.rerun()
    else:
        st.info("🛒 Your cart is empty")
        st.write("Browse our products and add items to get started!")

# Main Content Based on Current Page
if st.session_state.checkout or st.session_state.current_page == "checkout":
    st.markdown('<div class="checkout-summary">', unsafe_allow_html=True)
    st.title("🛒 Secure Checkout")

    if st.session_state.cart:
        # Progress indicator
        progress_bar = st.progress(0)
        st.caption("Step 1 of 3: Review Order")

        # Order Summary
        st.subheader("📋 Order Summary")

        # Customer Information Form
        with st.expander("👤 Customer Information", expanded=True):
            st.markdown("### Personal Details")
            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input(
                    "Full Name *",
                    value=st.session_state.user_profile.get("name", ""),
                    help="Required for delivery"
                )
                email = st.text_input(
                    "Email Address",
                    value=st.session_state.user_profile.get("email", ""),
                    help="For order confirmation"
                )

            with col2:
                phone = st.text_input(
                    "Phone Number",
                    help="For delivery coordination"
                )
                address = st.text_area(
                    "Delivery Address *",
                    value=st.session_state.user_profile.get("address", ""),
                    help="Required for delivery"
                )

            if st.button("💾 Save Information", type="secondary"):
                st.session_state.user_profile.update({
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "address": address
                })
                st.success("✅ Information saved!")

        st.divider()

        # Order Items Display
        st.subheader("🛍️ Your Items")

        order_items = []
        total = 0

        for item, details in st.session_state.cart.items():
            with st.container():
                col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

                # Find product details
                product_details = None
                for category_items in products.values():
                    for prod in category_items:
                        if prod['name'] == item:
                            product_details = prod
                            break
                    if product_details:
                        break

                with col1:
                    if product_details:
                        st.write(f"{product_details['image']} **{item}**")
                        if product_details.get('organic'):
                            st.caption("🌱 Organic")
                    else:
                        st.write(f"**{item}**")

                with col2:
                    st.write(f"${details['price']:.2f}")

                with col3:
                    st.write(f"Qty: {details['quantity']}")

                with col4:
                    item_total = details['price'] * details['quantity']
                    st.write(f"${item_total:.2f}")
                    total += item_total

        # Order Totals
        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📦 Subtotal", f"${total:.2f}")

        with col2:
            delivery_fee = 2.99 if total < 25 else 0
            st.metric("🚚 Delivery", f"${delivery_fee:.2f}" if delivery_fee > 0 else "FREE")

        with col3:
            tax = total * 0.08
            st.metric("💼 Tax (8%)", f"${tax:.2f}")

        final_total = total + delivery_fee + tax

        st.markdown(f"## 💰 **Grand Total: ${final_total:.2f}**")

        # Delivery Time Selection
        st.subheader("⏰ Delivery Time")
        delivery_option = st.selectbox(
            "Choose delivery time:",
            ["ASAP (30-45 mins)", "Within 1 hour", "Within 2 hours", "Schedule for later"],
            help="Select your preferred delivery time"
        )

        # Payment Method
        with st.expander("💳 Payment Method", expanded=True):
            st.markdown("### Secure Payment")
            payment_method = st.selectbox(
                "Select Payment Method",
                ["💳 Credit Card", "💳 Debit Card", "📱 PayPal", "💵 Cash on Delivery"],
                help="Choose your preferred payment method"
            )

            if payment_method in ["💳 Credit Card", "💳 Debit Card"]:
                st.markdown("#### Card Information")
                card_col1, card_col2 = st.columns(2)

                with card_col1:
                    card_number = st.text_input(
                        "Card Number",
                        type="password",
                        placeholder="1234 5678 9012 3456"
                    )
                    expiry = st.text_input(
                        "Expiry Date",
                        placeholder="MM/YY"
                    )

                with card_col2:
                    card_name = st.text_input(
                        "Name on Card",
                        placeholder="John Doe"
                    )
                    cvv = st.text_input(
                        "CVV",
                        type="password",
                        max_chars=4,
                        placeholder="123"
                    )

                st.caption("🔒 Your payment information is secure and encrypted")

        # Place Order Button
        st.divider()

        col1, col2 = st.columns([1, 1])

        with col1:
            if st.button("⬅️ Continue Shopping", use_container_width=True):
                st.session_state.checkout = False
                st.session_state.current_page = "shop"
                st.rerun()

        with col2:
            order_valid = bool(name.strip() and address.strip())

            if not order_valid:
                st.error("⚠️ Please fill in your name and delivery address")

            place_order = st.button(
                f"🎉 Place Order - ${final_total:.2f}",
                type="primary",
                use_container_width=True,
                disabled=not order_valid
            )

            if place_order and order_valid:
                # Process order
                progress_bar.progress(50)
                time.sleep(0.5)

                order = {
                    "order_id": f"LWG{datetime.now().strftime('%Y%m%d%H%M%S')}",
                    "items": st.session_state.cart.copy(),
                    "totals": {
                        "subtotal": total,
                        "delivery_fee": delivery_fee,
                        "tax": tax,
                        "final_total": final_total
                    },
                    "customer": {
                        "name": name,
                        "email": email,
                        "phone": phone,
                        "address": address
                    },
                    "payment_method": payment_method,
                    "delivery_time": delivery_option,
                    "order_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "status": "confirmed"
                }

                st.session_state.order_history.append(order)
                st.session_state.cart = {}
                st.session_state.checkout = False
                st.session_state.current_page = "home"

                progress_bar.progress(100)
                st.success("🎉 Order placed successfully!")
                st.balloons()

                st.session_state.notifications.append(f"Order #{order['order_id']} confirmed! Expected delivery in 30-45 minutes.")
                time.sleep(2)
                st.rerun()

    else:
        st.warning("🛒 Your cart is empty")
        if st.button("🛍️ Start Shopping", use_container_width=True):
            st.session_state.checkout = False
            st.session_state.current_page = "shop"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == "home":
    # Enhanced Home Page
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("🏪 Louis Wesley Grocery Store")
    st.markdown("### *Fresh • Local • Quality • AI-Powered*")
    st.markdown('</div>', unsafe_allow_html=True)

    # Hero Section
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        ## 🛒 Welcome to the Future of Grocery Shopping

        Experience grocery shopping like never before with:

        ✨ **AI-Powered Recommendations** - Get personalized suggestions
        🚚 **Fast Delivery** - 30-minute delivery to your doorstep
        🌱 **Fresh & Local** - Support local farmers and producers
        💳 **Secure Checkout** - Multiple payment options
        📱 **Mobile Friendly** - Shop anywhere, anytime
        """)

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🛍️ Start Shopping", type="primary", use_container_width=True):
                st.session_state.current_page = "shop"
                st.rerun()
        with col_b:
            if st.button("🤖 Try AI Assistant", type="secondary", use_container_width=True):
                st.session_state.current_page = "ai"
                st.rerun()

    with col2:
        st.markdown("""
        ### 📊 Why Choose Us?

        - ⭐ **4.8/5** Customer Rating
        - 🚚 **10,000+** Orders Delivered
        - 🌟 **500+** Happy Customers
        - 🏆 **Best Local Grocery** 2024
        """)

        # Quick stats
        stat_col1, stat_col2 = st.columns(2)
        with stat_col1:
            st.metric("📦 Orders Today", "247")
        with stat_col2:
            st.metric("⭐ Avg Rating", "4.8")

    st.markdown('</div>', unsafe_allow_html=True)

    # Featured Products Section
    st.header("⭐ Featured Products")

    featured_items = [
        products["Fruits & Vegetables"][0],  # Organic Apples
        products["Dairy & Eggs"][2],         # Greek Yogurt
        products["Meat & Seafood"][2],       # Atlantic Salmon
        products["Bakery & Bread"][1]        # Croissants
    ]

    featured_cols = st.columns(4)

    for i, product in enumerate(featured_items):
        with featured_cols[i]:
            with st.container():
                st.markdown('<div class="product-card">', unsafe_allow_html=True)

                # Product Image and Badge
                st.markdown(f'<div class="product-image">{product["image"]}</div>', unsafe_allow_html=True)
                if product.get('organic'):
                    st.markdown('<span style="background: #4CAF50; color: white; padding: 2px 8px; border-radius: 10px; font-size: 12px;">🌱 Organic</span>', unsafe_allow_html=True)

                # Product Details
                st.subheader(product['name'])
                st.markdown(f'<div class="product-price">${product["price"]:.2f}</div>', unsafe_allow_html=True)
                st.caption(f"per {product['unit']}")

                # Rating
                st.caption(f"⭐ {product['rating']} ({product['reviews']} reviews)")

                # Add to Cart Button
                if st.button(f"🛒 Add to Cart", key=f"featured_{i}", use_container_width=True):
                    if product["name"] in st.session_state.cart:
                        st.session_state.cart[product["name"]]["quantity"] += 1
                    else:
                        st.session_state.cart[product["name"]] = {
                            "price": product["price"],
                            "quantity": 1,
                            "unit": product["unit"]
                        }
                    st.session_state.notifications.append(f"✅ Added {product['name']} to cart!")
                    st.rerun()

                st.markdown('</div>', unsafe_allow_html=True)

    # Store Information
    st.header("🏪 About Our Store")

    info_cols = st.columns(3)

    with info_cols[0]:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📍 Location", "123 Main Street")
        st.write("Downtown District")
        st.markdown('</div>', unsafe_allow_html=True)

    with info_cols[1]:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🕒 Hours", "8AM - 9PM")
        st.write("7 days a week")
        st.markdown('</div>', unsafe_allow_html=True)

    with info_cols[2]:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📞 Contact", "(555) 123-4567")
        st.write("support@louiswesley.com")
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == "shop":
    st.title("🛍️ Shop Our Products")

    # Search and Filter Section
    col1, col2 = st.columns([3, 1])

    with col1:
        search_query = st.text_input(
            "🔍 Search products...",
            placeholder="Try 'organic', 'chicken', 'fresh'...",
            help="Search by name, description, or keywords"
        )

    with col2:
        sort_by = st.selectbox(
            "Sort by:",
            ["Name", "Price: Low to High", "Price: High to Low", "Rating"],
            help="Sort products by different criteria"
        )

    # Category Tabs with Enhanced Styling
    tabs = st.tabs(list(products.keys()))

    for tab_idx, (category, items) in enumerate(products.items()):
        with tabs[tab_idx]:
            # Filter and sort items
            display_items = items.copy()

            # Apply search filter
            if search_query:
                display_items = [
                    item for item in display_items
                    if search_query.lower() in item['name'].lower() or
                       search_query.lower() in item['description'].lower() or
                       search_query.lower() in item['category'].lower()
                ]

            # Apply sorting
            if sort_by == "Price: Low to High":
                display_items.sort(key=lambda x: x['price'])
            elif sort_by == "Price: High to Low":
                display_items.sort(key=lambda x: x['price'], reverse=True)
            elif sort_by == "Rating":
                display_items.sort(key=lambda x: x['rating'], reverse=True)

            if display_items:
                st.write(f"Showing {len(display_items)} product{'s' if len(display_items) != 1 else ''}")

                # Product Grid
                cols = st.columns(2)

                for idx, product in enumerate(display_items):
                    with cols[idx % 2]:
                        with st.container():
                            st.markdown('<div class="product-card">', unsafe_allow_html=True)

                            # Product Header
                            header_col1, header_col2 = st.columns([3, 1])
                            with header_col1:
                                st.markdown(f'<div class="product-image">{product["image"]}</div>', unsafe_allow_html=True)
                            with header_col2:
                                if product.get('organic'):
                                    st.markdown('<div class="cart-badge">🌱</div>', unsafe_allow_html=True)

                            # Product Info
                            st.subheader(product['name'])

                            # Rating and Reviews
                            rating_col, review_col = st.columns([1, 1])
                            with rating_col:
                                st.caption(f"⭐ {product['rating']}")
                            with review_col:
                                st.caption(f"({product['reviews']} reviews)")

                            # Price
                            st.markdown(f'<div class="product-price">${product["price"]:.2f}</div>', unsafe_allow_html=True)
                            st.caption(f"per {product['unit']}")

                            # Description
                            st.write(product['description'])

                            # Quantity and Add to Cart
                            qty_col, btn_col = st.columns([1, 2])

                            with qty_col:
                                quantity = st.number_input(
                                    "Qty",
                                    min_value=1,
                                    max_value=10,
                                    value=1,
                                    key=f"qty_{category}_{idx}",
                                    help=f"Select quantity (per {product['unit']})"
                                )

                            with btn_col:
                                if st.button(
                                    f"🛒 Add {quantity} to Cart",
                                    key=f"add_{category}_{idx}",
                                    use_container_width=True,
                                    type="primary"
                                ):
                                    if product["name"] in st.session_state.cart:
                                        st.session_state.cart[product["name"]]["quantity"] += quantity
                                    else:
                                        st.session_state.cart[product["name"]] = {
                                            "price": product["price"],
                                            "quantity": quantity,
                                            "unit": product["unit"]
                                        }

                                    st.session_state.notifications.append(
                                        f"✅ Added {quantity} {product['unit']} of {product['name']} to cart!"
                                    )
                                    st.rerun()

                            st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.info("🔍 No products found matching your search. Try different keywords!")

elif st.session_state.current_page == "ai":
    st.markdown('<div class="ai-chat-bubble">', unsafe_allow_html=True)
    st.title("🤖 AI Shopping Assistant")

    api_key = st.text_input(
        "🔑 Enter Groq API Key",
        type="password",
        help="Get your free API key at console.groq.com",
        key="ai_api_key"
    )

    if api_key:
        st.success("✅ AI Assistant is ready!")

        # Quick Suggestion Buttons
        st.subheader("💡 Quick Suggestions")
        suggestion_cols = st.columns(3)

        suggestions = [
            ("🍽️ Dinner Ideas", "Suggest ingredients for a healthy family dinner for 4"),
            ("🥗 Healthy Snacks", "What healthy snacks should I buy for the week?"),
            ("👨‍👩‍👧‍👦 Family Meal", "Plan a complete family dinner for 6 people")
        ]

        for i, (label, query) in enumerate(suggestions):
            with suggestion_cols[i]:
                if st.button(label, key=f"suggestion_{i}", use_container_width=True):
                    st.session_state.ai_query = query
                    st.rerun()

        # Main AI Input
        user_query = st.text_input(
            "💬 Ask me anything about shopping:",
            placeholder="e.g., 'What should I buy for Italian dinner?' or 'Suggest meal prep ingredients'",
            key="ai_input",
            value=getattr(st.session_state, 'ai_query', '')
        )

        if user_query:
            with st.spinner("🤖 Thinking..."):
                try:
                    client = Groq(api_key=api_key)
                    prompt = f"""You are Louis, a helpful AI shopping assistant at Louis Wesley Grocery Store.

Customer question: {user_query}

Please provide helpful, personalized shopping recommendations based on our available products.
Include specific product names, prices, and explanations for why these items would be good choices.
Be conversational and friendly, like a knowledgeable store employee.

Available product categories: Fruits & Vegetables, Dairy & Eggs, Meat & Seafood, Bakery & Bread.

Keep your response practical and focused on helping the customer make good shopping decisions."""

                    completion = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[{"role": "user", "content": prompt}]
                    )

                    ai_response = completion.choices[0].message.content

                    st.markdown("### 🤖 Louis Says:")
                    st.write(ai_response)

                    # Clear the query after showing results
                    if hasattr(st.session_state, 'ai_query'):
                        del st.session_state.ai_query

                except Exception as e:
                    st.error(f"❌ AI Error: {str(e)}")
                    st.info("💡 Make sure your Groq API key is correct and you have internet connection.")
    else:
        st.info("👆 Please enter your Groq API key to start chatting with our AI assistant!")

        st.markdown("""
        ### 🌟 What can the AI help you with?

        - 🍳 **Recipe planning** - Get ingredient lists for any meal
        - 🥗 **Healthy eating** - Suggestions for nutritious options
        - 💰 **Budget shopping** - Find deals and save money
        - 🎯 **Meal prep** - Weekly shopping lists for meal planning
        - ❓ **Product questions** - Learn about our products and pairings
        """)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == "history":
    st.title("📋 Order History")

    if st.session_state.order_history:
        st.write(f"📦 You have {len(st.session_state.order_history)} order{'s' if len(st.session_state.order_history) != 1 else ''}")

        for order_idx, order in enumerate(reversed(st.session_state.order_history)):
            with st.expander(f"📦 Order #{order['order_id']} - {order['order_date']}", expanded=(order_idx == 0)):

                # Order Status
                status_colors = {
                    "confirmed": "🟢",
                    "preparing": "🟡",
                    "out_for_delivery": "🟠",
                    "delivered": "✅"
                }
                status_emoji = status_colors.get(order.get('status', 'confirmed'), "🟢")
                st.markdown(f"**Status:** {status_emoji} {order.get('status', 'confirmed').replace('_', ' ').title()}")

                # Customer and Delivery Info
                info_col1, info_col2 = st.columns(2)

                with info_col1:
                    st.markdown("**👤 Customer Details:**")
                    customer = order.get('customer', {})
                    st.write(f"Name: {customer.get('name', 'N/A')}")
                    st.write(f"Phone: {customer.get('phone', 'N/A')}")
                    st.write(f"Email: {customer.get('email', 'N/A')}")

                with info_col2:
                    st.markdown("**📍 Delivery Info:**")
                    st.write(f"Address: {customer.get('address', 'N/A')}")
                    st.write(f"Time: {order.get('delivery_time', 'ASAP')}")
                    st.write(f"Payment: {order.get('payment_method', 'N/A')}")

                st.divider()

                # Order Items
                st.subheader("🛍️ Items Ordered")
                totals = order.get('totals', {})

                for item_name, item_details in order['items'].items():
                    item_col1, item_col2, item_col3 = st.columns([3, 1, 1])

                    with item_col1:
                        st.write(f"**{item_name}**")

                    with item_col2:
                        st.write(f"${item_details['price']:.2f} × {item_details['quantity']}")

                    with item_col3:
                        item_total = item_details['price'] * item_details['quantity']
                        st.write(f"${item_total:.2f}")

                st.divider()

                # Order Totals
                total_col1, total_col2, total_col3, total_col4 = st.columns(4)

                with total_col1:
                    st.metric("📦 Subtotal", f"${totals.get('subtotal', 0):.2f}")

                with total_col2:
                    st.metric("🚚 Delivery", f"${totals.get('delivery_fee', 0):.2f}")

                with total_col3:
                    st.metric("💼 Tax", f"${totals.get('tax', 0):.2f}")

                with total_col4:
                    st.metric("💰 Total", f"${totals.get('final_total', 0):.2f}")

                # Reorder Button
                if st.button(f"🔄 Reorder This", key=f"reorder_{order['order_id']}", use_container_width=True):
                    # Add items back to cart
                    for item_name, item_details in order['items'].items():
                        if item_name in st.session_state.cart:
                            st.session_state.cart[item_name]["quantity"] += item_details['quantity']
                        else:
                            st.session_state.cart[item_name] = item_details.copy()

                    st.session_state.notifications.append(f"✅ Added {len(order['items'])} items back to cart!")
                    st.session_state.current_page = "checkout"
                    st.rerun()

    else:
        st.info("📭 No orders yet")
        st.write("Start shopping to see your order history here!")

        if st.button("🛍️ Start Shopping", use_container_width=True):
            st.session_state.current_page = "shop"
            st.rerun()

elif st.session_state.current_page == "profile":
    st.title("👤 Customer Profile")

    # Profile Tabs
    profile_tabs = st.tabs(["Personal Info", "Preferences", "Addresses"])

    with profile_tabs[0]:
        st.header("Personal Information")

        profile_col1, profile_col2 = st.columns(2)

        with profile_col1:
            name = st.text_input(
                "Full Name",
                value=st.session_state.user_profile.get("name", ""),
                help="Your full legal name"
            )
            email = st.text_input(
                "Email Address",
                value=st.session_state.user_profile.get("email", ""),
                help="For order confirmations and updates"
            )

        with profile_col2:
            phone = st.text_input(
                "Phone Number",
                value=st.session_state.user_profile.get("phone", ""),
                help="For delivery coordination"
            )
            birth_date = st.date_input(
                "Birth Date",
                help="For special offers and birthday treats"
            )

        if st.button("💾 Save Personal Info", type="primary", use_container_width=True):
            st.session_state.user_profile.update({
                "name": name,
                "email": email,
                "phone": phone,
                "birth_date": str(birth_date)
            })
            st.success("✅ Personal information saved!")

    with profile_tabs[1]:
        st.header("Shopping Preferences")

        pref_col1, pref_col2 = st.columns(2)

        with pref_col1:
            dietary_restrictions = st.multiselect(
                "Dietary Restrictions",
                ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Nut-Free", "Kosher", "Halal"],
                default=st.session_state.user_profile.get("dietary_restrictions", []),
                help="We'll use this for personalized recommendations"
            )

            favorite_categories = st.multiselect(
                "Favorite Categories",
                list(products.keys()),
                default=st.session_state.user_profile.get("favorite_categories", []),
                help="Categories you'll see first when shopping"
            )

        with pref_col2:
            budget_range = st.selectbox(
                "Budget Range",
                ["Under $25", "$25-$50", "$50-$100", "Over $100"],
                index=["Under $25", "$25-$50", "$50-$100", "Over $100"].index(
                    st.session_state.user_profile.get("budget_range", "Under $25")
                ),
                help="Your typical order size"
            )

            notifications = st.checkbox(
                "Email Notifications",
                value=st.session_state.user_profile.get("notifications", True),
                help="Receive order updates and special offers"
            )

        if st.button("💾 Save Preferences", type="primary", use_container_width=True):
            st.session_state.user_profile.update({
                "dietary_restrictions": dietary_restrictions,
                "favorite_categories": favorite_categories,
                "budget_range": budget_range,
                "notifications": notifications
            })
            st.success("✅ Preferences saved!")

    with profile_tabs[2]:
        st.header("Saved Addresses")

        # Default Address
        st.subheader("🏠 Default Delivery Address")
        default_address = st.text_area(
            "Address",
            value=st.session_state.user_profile.get("address", ""),
            height=100,
            help="Your primary delivery address"
        )

        # Additional Addresses
        st.subheader("📍 Additional Addresses")

        if st.button("➕ Add New Address", type="secondary"):
            st.session_state.show_add_address = True

        if st.session_state.get('show_add_address', False):
            with st.form("add_address_form"):
                st.write("Add New Address")
                address_name = st.text_input("Address Name (e.g., Work, Home 2)")
                new_address = st.text_area("Full Address", height=80)

                col1, col2 = st.columns(2)
                with col1:
                    save_address = st.form_submit_button("💾 Save Address", type="primary", use_container_width=True)
                with col2:
                    cancel = st.form_submit_button("❌ Cancel", use_container_width=True)

                if save_address and address_name and new_address:
                    if "additional_addresses" not in st.session_state.user_profile:
                        st.session_state.user_profile["additional_addresses"] = {}

                    st.session_state.user_profile["additional_addresses"][address_name] = new_address
                    st.session_state.show_add_address = False
                    st.success(f"✅ Address '{address_name}' saved!")
                    st.rerun()

                if cancel:
                    st.session_state.show_add_address = False
                    st.rerun()

        # Display saved addresses
        additional_addresses = st.session_state.user_profile.get("additional_addresses", {})
        if additional_addresses:
            for addr_name, addr_details in additional_addresses.items():
                with st.expander(f"📍 {addr_name}"):
                    st.write(addr_details)
                    if st.button(f"🗑️ Delete {addr_name}", key=f"delete_{addr_name}"):
                        del st.session_state.user_profile["additional_addresses"][addr_name]
                        st.success(f"✅ Address '{addr_name}' deleted!")
                        st.rerun()

        if st.button("💾 Save Addresses", type="primary", use_container_width=True):
            st.session_state.user_profile["address"] = default_address
            st.success("✅ Addresses saved!")

# Enhanced Footer
st.divider()
footer_col1, footer_col2, footer_col3, footer_col4 = st.columns(4)

with footer_col1:
    st.markdown("**🏪 Louis Wesley Grocery Store**")
    st.caption("Fresh • Local • Quality")

with footer_col2:
    st.markdown("**📞 Contact Us**")
    st.caption("9032667375")
    st.caption("support@louiswesley.com")

with footer_col3:
    st.markdown("**🕒 Store Hours**")
    st.caption("Mon-Sun: 8AM - 9PM")
    st.caption("24/7 Online Shopping")

with footer_col4:
    st.markdown("**📍 Visit Us**")
    st.caption("123 Main Street")
    st.caption("Downtown District")

st.caption("---")
st.caption("© 2026 Louis Wesley Grocery Store. Built with ❤️ using Streamlit and AI.")
st.caption("**Student Information:**")
st.caption("Name: OYORIA WESLEY")
st.caption("Matric No: FPS/CSC/24/90070")
st.caption("Student ID: E1153183")
st.caption("Course: CSC206 - WEB DESIGN AND DEVELOPMENT")
st.caption("Date: May 8, 2026")

st.markdown('</div>', unsafe_allow_html=True)