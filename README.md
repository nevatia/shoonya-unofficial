
👉 [shoonya-unofficial GitHub Repository](https://github.com/nevatia/shoonya-unofficial.git)

# 🚀 Shoonya Unofficial Python API Wrapper

Unofficial Python wrapper for Finvasia Shoonya Trading API — designed for fast integration, algo trading, and automation.

Installing this repo may overwrite your existing norenapi.
So to avoid that, you are advised to use it in a separate environment or by installing locally.
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

You need to get appkey from your weblogin once and save it in .yml for appkey in quotes. 
This is one time process as of now.

```python
from NorenRestApiPy.NorenApi import NorenApi
class ShoonyaApiPy(NorenApi):
    def __init__(self):
        super().__init__(
            host="https://api.shoonya.com/NorenWClientAPI",
            websocket="wss://api.shoonya.com/NorenWSAPI",
        )
api = ShoonyaApiPy()
ret = api.login(userid=cred['user'], 
password=cred['pwd'], 
twoFA=generate_totp(cred['factor2']), 
vendor_code=cred['vc'], 
api_secret=cred['apikey'], 
imei=cred['imei'],
secret_code= cred['secret'],
appkey= cred['appkey'])
print(ret)


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

MIT License 

---

## ⭐ Support

If this helps you:

👉 Star the repo
👉 Share with trading community



