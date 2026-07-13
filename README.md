Here’s a **clean, professional `README.md`** tailored for your repo:

👉 [shoonya-unofficial GitHub Repository](https://github.com/nevatia/shoonya-unofficial.git?utm_source=chatgpt.com)

You can **copy–paste this directly** into your repo.

---

# 🚀 Shoonya Unofficial Python API Wrapper

Unofficial Python wrapper for **Finvasia Shoonya Trading API** — designed for fast integration, algo trading, and automation.

---

## 📦 Features

* ✅ Login / Session handling
* ✅ Order placement (BUY / SELL / MODIFY / CANCEL)
* ✅ Market data access (LTP, Quotes, Option Chain)
* ✅ WebSocket support (if implemented)
* ✅ Lightweight & fast
* ✅ Easy to integrate with trading strategies

---

## 📁 Project Structure

```
shoonya-unofficial/
│
├── NorenRestApiPy/
│   ├── __init__.py
│   └── NorenApi.py
│
├── dist/
│   └── shoonya_unofficial-<version>.whl
│
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 🔹 Option 1: Install from Wheel (Recommended)

```bash
pip install https://github.com/nevatia/shoonya-unofficial/raw/main/dist/shoonya_unofficial-<version>.whl
```

---

### 🔹 Option 2: Install from GitHub (requires Git)

```bash
pip install git+https://github.com/nevatia/shoonya-unofficial.git
```

---

### 🔹 Option 3: Manual Install

```bash
git clone https://github.com/nevatia/shoonya-unofficial.git
cd shoonya-unofficial
pip install .
```

---

## 🔑 Usage Example

```python
from NorenRestApiPy.NorenApi import NorenApi

api = NorenApi()

# Login
api.login(
    userid="YOUR_USER_ID",
    password="YOUR_PASSWORD",
    twoFA="YOUR_2FA",
    vendor_code="YOUR_VENDOR_CODE",
    api_secret="YOUR_API_SECRET",
    imei="YOUR_IMEI"
)

# Get Quote
quote = api.get_quotes(exchange="NSE", token="26000")
print(quote)
```

---

## 📌 Requirements

If not auto-installed:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Important Notes

* This is an **unofficial wrapper**
* Not affiliated with Finvasia / Shoonya
* Use at your own risk for live trading
* Always test in paper / demo environment first

---

## 🧠 Use Cases

* Algo trading bots
* Options strategy automation
* Market data streaming dashboards
* Backtesting pipelines

---

## 🛠️ Development Setup

```bash
git clone https://github.com/nevatia/shoonya-unofficial.git
cd shoonya-unofficial
pip install -e .
```

---

## 🐞 Common Issues

### ❌ ModuleNotFoundError

✔ Ensure:

* `NorenRestApiPy/__init__.py` exists
* Package installed correctly

---

### ❌ Login Fails

✔ Check:

* Credentials
* TOTP / 2FA
* API permissions

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, open an issue first.

---

## 📜 License

MIT License (or update if different)

---

## ⭐ Support

If this helps you:

👉 Star the repo
👉 Share with trading community



