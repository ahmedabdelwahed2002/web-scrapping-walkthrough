# 🧪 Egyptian Drug Ingredients Finder

provides two scripts to help retrieve active and inactive ingredients for Egyptian drugs using two different methods:

1. 🤖 **AI-based extraction** using the Groq API (Llama 3 model).
2. 🌐 **Web scraping** from the official Egyptian "Drug Eye" website using Selenium and BeautifulSoup.

---

## 📄 Features

- 🔍 Search for a drug by name
- 🧪 Retrieve:
  - Active Ingredients
  - Inactive Ingredients (Excipients)
- 🛠️ Two methods available:
  - Groq Llama 3 AI model
  - Live web scraping of the Drug Eye database

---

## 🚀 How to Run

### 1. Install Dependencies

Make sure you have Python 3.8+ installed. Then install the required packages:

```bash
pip install groq selenium beautifulsoup4 webdriver-manager
