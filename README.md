# CityFinder - Smart City Location Discovery Platform

CityFinder is a full-stack, city-based location discovery platform that allows users to find specific amenities within a configured city. 

## Installation & Setup

1. **Clone the repository and enter directory:**
   ```bash
   git clone <your-repo-url>
   cd CityFinder
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Rename `.env.example` to `.env` and fill in the values.

## Running the Application
```bash
python app.py
```
Open `http://127.0.0.1:5000` in your web browser.
