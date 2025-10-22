FarmTrack

A Django-based farm management system for tracking operations, expenses, sales, and profit-loss reports.
Uses MySQL for data storage and Django templates for responsive web pages.

Features

Manage fields (name, size, location, crop type)

Record operations (planting, spraying, harvesting)

Track all expenses by category

Log produce sales and revenue

Auto-calculate profit or loss per field or month

View clean dashboards with Bootstrap layout

Works with MySQL database

Requirements

Python 3.10+

Django 5.x

MySQL Server

mysqlclient library

farmtrack/
│
├── manage.py
├── farmtrack/          # Settings and root configuration
├── fields/             # Field management
├── operations/         # Farm operations
├── expenses/           # Expense tracking
├── sales/              # Sales records
└── reports/            # Profit-loss reports
