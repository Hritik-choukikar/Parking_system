# 🚗 Parking System

A modular, scalable parking lot management system built with clean architecture and design patterns. Supports dynamic slot assignment, vehicle tracking, and billing logic — ideal for real-world deployment in malls, offices, or smart cities.

---

## 🧱 Architecture Overview

- **Language**: Python  
- **Design Patterns**: Factory, Strategy, Singleton  
- **Structure**: Layered modules for entry/exit, slot allocation, billing, and reporting  
- **Extensibility**: Easily adaptable for multi-level parking, EV charging, or reservation systems

---

## 📦 Features

- 🚙 Dynamic slot assignment based on vehicle type  
- 🕒 Entry/Exit tracking with timestamps  
- 💰 Billing logic based on duration and vehicle category  
- 🧠 Strategy pattern for flexible pricing models  
- 🔒 Singleton pattern for centralized parking lot state  
- 🏭 Factory pattern for vehicle and slot instantiation

---

## 🧪 Testing

Includes unit tests for:

- Slot availability and assignment  
- Billing calculations  
- Edge cases (e.g., full lot, invalid vehicle type)

 

---

## 🚀 Deployment

To run locally:

```bash
python main.py
```

To deploy as an API (Flask/FastAPI wrapper coming soon):

```bash
uvicorn app:app --reload
```

---

 

---

## 🧠 Future Enhancements

- Cloud deployment (AWS/OCI)  
- Admin dashboard for analytics  
- Reservation and pre-booking system  
- Integration with IoT sensors

---

## 👨‍💻 Author

**Hritik Choukikar**  
AI Data Development Lead | System Design Enthusiast  
[GitHub Profile](https://github.com/Hritik-choukikar)
