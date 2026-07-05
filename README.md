# DevStore: Full-Stack Django E-Commerce Pipeline

A modular, production-ready e-commerce storefront web application built completely using Python and the Django framework. This project features a persistent relational database architecture to manage product lines, dynamic client-side rendering with Tailwind CSS, and a simulated checkout integration blueprint designed for secure Stripe and Razorpay processing workflows.

---

## ⚠️ Important Note & Disclaimer
> **Development & Prototype Status:** This project is engineered strictly as a full-stack architectural prototype for portfolio and evaluation purposes. 
> 
> - **Simulated Checkouts:** The transaction pipeline uses a robust mock payment engine to safely demonstrate data routing workflows on your local machine without needing active credit cards or live bank APIs.
> - **Production Warning:** Do not attempt to use this specific configuration in a live production environment to handle real money without first updating `core/settings.py` with your verified private Stripe/Razorpay merchant API secret credentials and establishing secure HTTPS webhook endpoints.
> - **Local Execution:** If you run into any local environment conflicts, ensure your virtual environment (`.venv`) is completely activated and your folder names mirror the structure guide below exactly to avoid file mapping errors.

---

## 🚀 Core Features

- **Dynamic Inventory Grid:** Renders live inventory records dynamically extracted from a local persistent SQLite database via the Django Object-Relational Mapper (ORM).
- **Dual-Gateway Checkout Layer:** A custom checkout module providing client routing choices for both international credit transactions (Stripe) and local unified payment interfaces like UPI and NetBanking (Razorpay).
- **Automated Data Seeding:** Integrated logic that detects empty database states on startup and safely instantiates mock hardware inventory automatically.
- **Responsive Frontend:** Clean, scannable user interface layouts engineered with utility-first CSS styling using Tailwind CDN modules.
- **Relational Transaction History:** Robust relational architecture linking order processing IDs directly to specific item records with strict status lifecycle management (`PENDING`, `COMPLETED`, `FAILED`).

---

## 🛠️ Tech Stack & Architecture

- **Backend Framework:** Python 3.11+, Django 5.x
- **Database Engine:** SQLite3 (Production convertible to PostgreSQL via settings layout)
- **Frontend Architecture:** Django Template Engine, HTML5, Tailwind CSS
- **Payment SDK Blueprints:** Stripe API, Razorpay Python SDK

---

## 📦 Project Directory Structure

```text
PROJECT 6/
├── core/                  # Core Project Configuration
│   ├── settings.py        # Environment variables & engine configurations
│   ├── urls.py            # Primary application routing table
│   └── wsgi.py            # Web Server Gateway Interface entry point
├── store/                 # Main E-Commerce Application
│   ├── models.py          # Database relational schema (Product, Order)
│   ├── views.py           # Backend control logic & request handlers
│   └── urls.py            # Localized endpoint paths
├── templates/             # Frontend Layout Templates
│   └── store/
│       ├── index.html     # Active product display grid
│       ├── checkout.html  # Secure gateway selection view
│       └── success.html   # Verified payment feedback screen
├── db.sqlite3             # Persistent application database file
└── manage.py              # Django administrative command-line execution utility
