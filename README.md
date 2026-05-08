# Louis Wesley Grocery Store 🛒

**Student Name:** OYORIA WESLEY  
**Student mattno:** FPS/CSC/24/90070  
**Student ID:** E1153183

A modern, AI-powered grocery shopping application built with Streamlit. The app offers a complete e-commerce experience with browsing, cart management, checkout, order history, and an intelligent AI shopping assistant.

## 🚀 Features

### Core Shopping Experience
- **Product Catalog**: Organized in categories (Fruits & Vegetables, Dairy & Eggs, Meat & Seafood, Bakery & Bread)
- **Search & Filtering**: Search products by name, description, or keywords
- **Shopping Cart**: Add items, update quantities, and track totals
- **Checkout Flow**: Customer info, payment options, and delivery settings
- **Order History**: Review past orders and confirm delivery details

### AI-Powered Functionality
- **Intelligent Shopping Assistant**: Uses Groq's AI model for personalized product suggestions
- **Recipe Planning**: Provides shopping recommendations for meals
- **Smart Suggestions**: Offers contextual advice for budget shopping, healthy eating, and meal prep
- **No Login Required**: Shop and use AI without signing into an account

### Experience & Design
- **Modern UI**: Custom CSS, glassmorphism styling, and animations
- **Session Management**: Cart, profile, order history, and preferences are preserved during the session
- **Notifications**: Real-time UI feedback for user actions
- **Responsive Layout**: Designed for desktop and mobile screens

## 🔧 What's Included

### Main App Functionality (`app.py`)
- Page configuration and custom styling
- Session state initialization and persistence
- Product catalog with detailed item metadata
- Sidebar navigation and cart summary
- Shop page with categories, search, and sorting
- Checkout flow with order confirmation
- AI assistant page for natural language shopping help
- Order history and profile sections

### AI Integration
The AI assistant is powered by Groq and is available from the sidebar as **AI Assistant**. It uses the following pattern:

```python
client = Groq(api_key=api_key)
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": prompt}]
)
```

## ✅ Updated Project Details

- Added **AI Assistant** navigation in the sidebar
- Removed login and signup flows for a simpler shopping experience
- Fixed empty label accessibility warning for the home search field
- Added `.streamlit/secrets.toml` to `.gitignore` for secure local API key storage

## 🧩 Setup and Run

1. Clone the repository:
   ```bash
git clone https://github.com/Louiswesley/Louis-wesley-grocery-app.git
cd "Grocery app"
```

2. Create and activate a virtual environment:
   ```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
   ```bash
pip install -r requirements.txt
```

4. Add your Groq API key locally:
   - Create `.streamlit/secrets.toml`
   - Add:
     ```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

5. Run the app:
   ```bash
streamlit run app.py --server.port 8501
```

6. Open the browser:
   ```
http://localhost:8501
```

## 🤖 AI Assistant Instructions

- Navigate to the **AI Assistant** page via the sidebar
- Enter your Groq API key if prompted
- Ask questions like:
  - `What should I buy for Italian dinner?`
  - `Suggest healthy snacks for the week`
  - `Help me meal prep for 4 people`

## 📌 Notes

- The app uses **session state only** and does not persist data across server restarts
- Payment processing is **simulated** for demo purposes only
- Store secrets locally with `.streamlit/secrets.toml`
- `.streamlit/secrets.toml` is ignored by Git due to `.gitignore`

## 🚀 Future Enhancements

- Persistent database storage for users, orders, and inventory
- User authentication and account management
- Real payment gateway integration
- Inventory and delivery tracking
- Enhanced AI recommendations with product availability awareness

---

**Built by Louis Wesley** | **Student Project** | **Streamlit + Groq AI**
