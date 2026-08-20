# 🖥️ Data Surveillance System

A Python-based automation project designed to continuously monitor system resources and generate detailed surveillance logs at scheduled intervals.

The application collects information about CPU usage, RAM usage, Disk usage, Network activity, and Running Processes, then stores the collected information in timestamped log files for future analysis and monitoring.

---

# 📌 Features

## System Monitoring
- CPU Usage Monitoring
- RAM Usage Monitoring
- Disk Usage Monitoring
- Network Usage Monitoring

## Process Monitoring
- Process ID (PID)
- Process Name
- Username
- Process Status
- Process Creation Time
- CPU Consumption
- Memory Consumption

## Automated Logging
- Generates timestamped log files
- Stores logs in user-defined directory
- Creates structured surveillance reports

## Scheduler Support
- Periodic execution using scheduler
- User-defined monitoring interval
- Continuous background monitoring

## Command Line Interface
- Help option
- Usage option
- User-defined time interval
- User-defined log directory

---

# 🛠 Technologies Used

- Python 3
- psutil
- schedule
- os
- sys
- time

---

# 📂 Project Structure

```text
Data-Surveillance-System
│
├── ProcessLoggerWithSystemInfo.py
├── Logs
│   ├── Surveillance_2026-08-20_10-00-00.log
│   ├── Surveillance_2026-08-20_10-05-00.log
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/atharv-bhosale11/Data-Surveillance-System.git
```

## Navigate to Repository

```bash
cd Data-Surveillance-System
```

## Install Required Packages

```bash
pip install psutil
pip install schedule
```

or

```bash
pip install -r requirements.txt
```

---

# 🚀 Usage

## Display Help

```bash
python ProcessLoggerWithSystemInfo.py --h
```

## Display Usage

```bash
python ProcessLoggerWithSystemInfo.py --u
```

## Start Surveillance

```bash
python ProcessLoggerWithSystemInfo.py 5 Logs
```

### Parameters

```text
5      → Time interval in minutes
Logs   → Directory where log files will be created
```

The application will automatically generate a surveillance log every 5 minutes.

---

# 📄 Sample Log Report

```text
--------------------------------------------------

Data Surveillance System

--------------------------------------------------

Log Created At:
Thu Aug 20 12:00:00 2026

--------------------------------------------------

CPU Usage : 15 %

--------------------------------------------------

RAM Usage : 42 %

--------------------------------------------------

Disk Usage Report

C:\ -> 61 % used

D:\ -> 48 % used

--------------------------------------------------

Network Usage Report

Sent : 125.42 MB
Received : 340.18 MB

--------------------------------------------------

PID : 1234
Name : chrome.exe
Username : User
Status : running
CPU % : 3.10
Memory % : 4.55

--------------------------------------------------
```

---

# 🎯 Learning Objectives

This project demonstrates:

- Python Automation
- System Monitoring
- Process Monitoring
- Scheduler Implementation
- Command Line Programming
- File Handling
- Log Generation
- Exception Handling
- Operating System Utilities
- Resource Monitoring

---

# 📈 Future Enhancements

- Email Notifications
- PDF Report Generation
- CSV Report Export
- Real-Time Dashboard
- GUI Application
- Database Storage
- Process Filtering
- Resource Threshold Alerts
- Cloud Log Storage

---

# 💡 Use Cases

- System Administration
- Resource Monitoring
- Performance Analysis
- Server Monitoring
- Process Tracking
- Infrastructure Health Checks
- Automation Learning Projects

---

# 👨‍💻 Author

**Atharv Tushar Bhosale**

Computer Engineer | Software Developer | Python Automation Enthusiast

GitHub:
https://github.com/atharv-bhosale11

---

# ⭐ Repository Highlights

✔ Real-Time System Monitoring

✔ Automated Log Generation

✔ Process Surveillance

✔ Scheduler-Based Execution

✔ Command Line Support

✔ Timestamped Reports

✔ Python Automation Project

---

# 📜 License

This project is developed for educational, learning, and portfolio purposes.
