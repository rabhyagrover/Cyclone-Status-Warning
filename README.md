🌀 Cyclone Status & Risk Assessment Tool


A Python-based diagnostic utility designed to categorize cyclonic threats based on meteorological inputs. This project serves as a foundational logic model for weather monitoring systems, utilizing atmospheric pressure, wind velocity, and environmental conditions to output real-time safety protocols.

Table of Contents

Overview

Core Logic & Thresholds

Key Features

Installation

Usage Guide

Technical Implementation

Future Roadmap

Overview

The Cyclone Status Checker is a command-line interface (CLI) application that automates the decision-making process during volatile weather events. By analyzing the inverse relationship between atmospheric pressure and wind speed, the script identifies if a weather system has crossed the threshold into a "Cyclone Warning" state.

Parameter...................Threshold.........................Significance


Atmospheric Pressure.................<995 hPa......................Indicates a low-pressure system typical of storms.


Wind Speed...........................>60 km/h.......................Represents the transition from a gale to a cyclonic storm.


Condition..............................Windy/Rainy..................Qualitative data used to determine storm acceleration.


Risk Levels

1.Normal: Both pressure and wind speed are within safe operational limits.

2.Weather Alert: One parameter is breached (e.g., high wind but stable pressure). Requires indoor monitoring.

3.Cyclone Warning: Both critical thresholds are breached simultaneously. Requires immediate evacuation

Key Features:

Error Resilience: Utilizes try-except blocks to prevent crashes during improper data entry (e.g., entering text instead of numbers for pressure).

String Sanitization: Automatically handles user input casing (e.g., "RAINY", "Rainy", and "rainy" are all processed correctly).

Contextual Warnings: If a "Cyclone Warning" is active, the script checks the condition variable to provide a secondary warning about rain/wind accelerating the storm.

Modular Design: The logic is contained within a main function check_cyclone_status(), making it easy to import into other weather modules.

Installation

1.Prerequisites: * Ensure you have Python 3.x installed on your system.

2.Clone/Download: git clone https://github.com/yourusername/cyclone-status-checker.git
cd cyclone-status-checker

3.Execution: python Cyclone-Status.py

Usage Guide
When prompted, provide the following data points:

Pressure: Enter the value in Hectopascals (hPa).

Typical sea-level pressure is 1013 hPa.

Wind Speed: Enter the speed in km/h.

Condition: Choose between Sunny, Windy, or Rainy.

Example Scenario:

Input: Pressure: 990, Wind: 85, Condition: Windy

Result: The script will trigger a 🚨 CYCLONE WARNING due to the combination of low pressure and high wind, specifically noting that the windy conditions are accelerating the threat.

Technical Implementation
The script utilizes a Decision Tree structure:

Primary Logic: if is_extreme_pressure and is_high_wind:

Secondary Logic: elif is_extreme_pressure or is_high_wind:

Fall-through: else: (Normal status).

This hierarchical approach ensures that the most dangerous conditions are prioritized first in the evaluation flow.

Future Roadmap
[ ] API Integration: Fetch live weather data from OpenWeatherMap API instead of manual input.

[ ] Data Logging: Save every check to a .csv file for historical trend analysis.

[ ] GUI Version: Develop a simple visual interface using Tkinter or PyQt.

[ ] SMS Alerts: Integrate Twilio to send automated text alerts when a "Warning" status is reached.
