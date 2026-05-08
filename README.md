# Louis Wesley Grocery Store 🛒

**Student Name: OYORIA WESLEY**
**Student mattno:FPS/CSC/24/90070
**Student iD:E1153183

A modern, AI-powered grocery shopping application built with Streamlit, featuring a complete e-commerce experience with shopping cart, checkout, order history, and an intelligent AI shopping assistant.

## 🚀 Features

### Core Shopping Experience
- **Product Catalog**: Organized into categories (Fruits & Vegetables, Dairy & Eggs, Meat & Seafood, Bakery & Bread)
- **Advanced Search & Filtering**: Search by name, description, or keywords with sorting options
- **Shopping Cart**: Real-time cart management with quantity controls and persistent storage
- **Secure Checkout**: Complete checkout flow with customer information, payment methods, and delivery options
- **Order History**: Track all past orders with detailed summaries and reorder functionality

### AI-Powered Features
- **Intelligent Assistant**: Powered by Groq's Llama 3 model for personalized shopping recommendations
- **Recipe Planning**: Get ingredient suggestions for meals and dietary needs
- **Smart Suggestions**: Contextual product recommendations based on user queries

### User Experience
- **Responsive Design**: Modern UI with custom CSS styling and smooth animations
- **Session Management**: Persistent user sessions with cart and profile data
- **Notification System**: Real-time feedback for user actions
- **Mobile-Friendly**: Optimized for all device sizes

## 🏗️ Architecture & Code Structure

### Main Components

#### 1. **Page Configuration & Styling** (`app.py` lines 1-220)
```python
st.set_page_config(
    page_title="Louis Wesley Grocery Store",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)
```
- Sets up the Streamlit app configuration
- Defines custom CSS for modern UI components
- Includes responsive design elements and animations

#### 2. **Session State Management** (`app.py` lines 221-235)
```python
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"
if 'cart' not in st.session_state:
    st.session_state.cart = {}
```
- Manages application state across user interactions
- Tracks current page, shopping cart, user profile, and order history
- Ensures data persistence during the session

#### 3. **Product Data Structure** (`app.py` lines 236-400)
```python
products = {
    "Fruits & Vegetables": [
        {
            "name": "Organic Apples",
            "price": 3.99,
            "unit": "lb",
            "category": "Fruits",
            "image": "🍎",
            "description": "Fresh, crisp organic apples",
            "rating": 4.8,
            "reviews": 124,
            "organic": True,
            "in_stock": True
        }
    ]
}
```
- Comprehensive product catalog with detailed metadata
- Includes pricing, ratings, descriptions, and availability
- Supports organic labeling and stock status

#### 4. **Navigation System** (`app.py` lines 401-450)
```python
nav_buttons = [
    ("🏠 Home", "home", "nav_home"),
    ("🛍️ Shop", "shop", "nav_shop"),
    ("🤖 AI", "ai", "nav_ai"),
    ("📋 Orders", "history", "nav_orders"),
    ("👤 Profile", "profile", "nav_profile")
]
```
- Dynamic navigation bar with active state indicators
- Integrated cart display showing item count and total
- Page routing based on user selection

#### 5. **Shopping Cart Sidebar** (`app.py` lines 451-500)
- Real-time cart display with item management
- Individual item removal and quantity display
- Total calculation and checkout initiation
- Cart clearing functionality

#### 6. **Checkout Process** (`app.py` lines 501-700)
- Multi-step checkout flow with progress tracking
- Customer information collection and validation
- Order summary with detailed item breakdown
- Payment method selection and processing
- Delivery time scheduling
- Order confirmation and processing

#### 7. **Home Page** (`app.py` lines 701-850)
- Hero section with store introduction
- Featured products showcase
- Store information and statistics
- Call-to-action buttons for shopping and AI features

#### 8. **Shop Page** (`app.py` lines 851-1000)
- Category-based product browsing with tabs
- Advanced search functionality
- Multiple sorting options (name, price, rating)
- Product grid layout with detailed cards
- Quantity selection and cart addition

#### 9. **AI Assistant** (`app.py` lines 1001-1100)
```python
client = Groq(api_key=api_key)
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": prompt}]
)
```
- Integration with Groq API for AI-powered assistance
- Contextual prompts for shopping recommendations
- Quick suggestion buttons for common queries
- Error handling for API interactions

#### 10. **Order History** (`app.py` lines 1101-1200)
- Complete order tracking and display
- Detailed order information including customer details
- Status tracking with visual indicators
- Reorder functionality to recreate past orders

#### 11. **User Profile** (`app.py` lines 1201-1371)
- Personal information management
- Shopping preferences and dietary restrictions
- Multiple address management
- Profile data persistence

## 🔧 Technical Implementation

### Dependencies
- **Streamlit**: Web application framework
- **Groq**: AI model API for intelligent assistance
- **datetime**: Date and time handling
- **json**: Data serialization (used in AI responses)
- **time**: Timing controls for UI feedback

### Key Technologies
- **Frontend**: Streamlit components with custom CSS
- **Backend**: Python session state management
- **AI**: Groq API integration
- **Data**: In-memory data structures (could be extended to databases)

### State Management
The application uses Streamlit's session state to maintain:
- Current page navigation
- Shopping cart contents
- User profile information
- Order history
- UI state (notifications, form expansions)

### Security Considerations
- API keys stored in session (not persisted)
- Payment information masked in UI
- No actual payment processing (demo implementation)
- Secure API communication with Groq

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Louiswesley/Louis-wesley-grocery-app.git
   cd louis-wesley-grocery-app
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the app**:
   Open your browser to `http://localhost:8501`

## 🤖 AI Assistant Setup

To use the AI shopping assistant:

1. Visit [console.groq.com](https://console.groq.com)
2. Create a free account and get your API key
3. Enter the API key in the AI assistant section of the app

## 📊 Application Flow

1. **Landing**: User sees home page with featured products
2. **Browsing**: Navigate to shop page, search/filter products
3. **Shopping**: Add items to cart, adjust quantities
4. **Checkout**: Enter customer info, select payment/delivery
5. **Confirmation**: Order processed, added to history
6. **AI Help**: Get personalized shopping recommendations
7. **Profile**: Manage personal info and preferences

## 🔄 Data Flow

- **Products**: Static data loaded at startup
- **Cart**: Session-based, persists during user session
- **Orders**: Stored in session state, could be persisted to database
- **User Profile**: Session-based user information
- **AI Responses**: Real-time API calls to Groq

## 🎨 UI/UX Design

- **Modern Design**: Gradient backgrounds, card-based layouts
- **Responsive**: Works on desktop and mobile devices
- **Interactive**: Smooth animations and transitions
- **Accessible**: Clear navigation and feedback messages
- **Intuitive**: Logical flow from browsing to checkout

## 🚀 Future Enhancements

- Database integration for persistent data
- User authentication and accounts
- Real payment processing
- Inventory management
- Delivery tracking
- Mobile app development
- Advanced AI features (image recognition, voice shopping)

## 📝 Notes

- The AI assistant requires a valid Groq API key
- Payment processing is simulated for demo purposes
- All data is stored in session state (resets on app restart)
- Built with ❤️ using Streamlit and AI technology

---

**Built by Louis Wesley** | **Contact**: support@louiswesley.com | **Phone**: 9032667375
