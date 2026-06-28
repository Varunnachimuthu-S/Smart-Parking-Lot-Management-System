# 🚗 Smart Parking Lot Management System

A Python-based **Smart Parking Lot Management System** that automates parking operations using **Object-Oriented Programming (OOP)** and **Data Structures & Algorithms (DSA)**. The application efficiently manages vehicle entry/exit, parking slot allocation, ticket generation, parking fee calculation, and revenue tracking.

---

## 📌 Project Overview

Managing large parking facilities manually can lead to inefficient slot allocation, inaccurate fee calculation, and poor vehicle tracking.

This project provides an automated parking management solution that:

- Allocates parking slots efficiently
- Tracks vehicle entry and exit
- Generates parking tickets
- Calculates parking fees
- Maintains parking occupancy
- Generates parking reports

---

## 🚀 Features

- ✅ Multi-floor parking management (3 Floors, 150 Slots)
- ✅ Vehicle Entry & Exit Management
- ✅ Automatic Parking Ticket Generation
- ✅ Priority Queue (Heap) Based Slot Allocation
- ✅ O(1) Vehicle Search using HashMap (Dictionary)
- ✅ Parking Fee Calculation
- ✅ Revenue Tracking
- ✅ Real-time Slot Availability Monitoring
- ✅ Interactive Menu-Driven Console Application

---

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Data Structures & Algorithms (DSA)

### Python Libraries

- heapq
- uuid
- datetime

---

## 🧠 Data Structures Used

| Data Structure | Purpose |
|---------------|---------|
| Dictionary (HashMap) | O(1) Vehicle Lookup |
| Priority Queue (Heap) | Nearest Slot Allocation |
| Lists | Floor & Slot Management |

---

## 📂 Project Structure

```text
ParkingLotManagement/
│
├── main.py
├── parking_lot.py
├── parking_slot.py
├── parking_ticket.py
├── vehicle.py
└── README.md
```

---

## ⚙️ How It Works

### Vehicle Entry

- Enter vehicle number and type
- System allocates the nearest available parking slot
- Parking ticket is generated automatically

### Vehicle Exit

- Search vehicle using vehicle number
- Calculate parking duration
- Calculate parking fee
- Release parking slot
- Update revenue

---

## 📊 System Workflow

```text
Vehicle Entry
      │
      ▼
Priority Queue
(Nearest Slot Allocation)
      │
      ▼
Parking Ticket Generation
      │
      ▼
Vehicle Search
(HashMap)
      │
      ▼
Parking Fee Calculation
      │
      ▼
Revenue Report
```

---

## 💻 Sample Menu

```text
===== PARKING LOT SYSTEM =====

1. Park Vehicle
2. Remove Vehicle
3. Search Vehicle
4. Show Available Slots
5. Generate Report
6. Exit
```

---

## 📈 Time Complexity

| Operation | Complexity |
|-----------|------------|
| Vehicle Search | O(1) |
| Slot Allocation | O(log n) |
| Slot Release | O(log n) |
| Report Generation | O(n) |

---

## 🎯 OOP Concepts Implemented

- Encapsulation
- Composition
- Abstraction
- Modular Design

---

## 📌 Future Enhancements

- SQL Server Integration
- Persistent Data Storage
- User Authentication
- PDF Ticket Generation
- Web-Based Interface (Flask/Django)
- Parking Analytics Dashboard

---

## 👨‍💻 Created By

**Varunnachimuthu S**
