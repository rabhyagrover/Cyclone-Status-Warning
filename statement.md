Project Statement: Cyclone Status & Risk Assessment Tool

1. Problem Statement

Accurate and immediate interpretation of meteorological data is critical for disaster preparedness. 
Manual observation of atmospheric parameters can lead to delayed responses during rapid weather changes. 
This project addresses the need for a simplified, automated decision-making tool that translates complex data—specifically atmospheric pressure and wind speed—into clear, actionable safety statuses for general users or local emergency monitors.


2. Scope of the Project

 
The Cyclone Status & Risk Assessment Tool is a Python-based utility designed to:

Analyze Quantitative Data: Process user-provided atmospheric pressure (hPa) and wind speed (km/h).

Evaluate Qualitative Conditions: Incorporate environmental factors such as "Rainy" or "Windy" states to refine risk levels.

Provide Immediate Protocols: Output specific safety actions (e.g., evacuation vs. monitoring) based on a defined logical decision tree.

This project focuses on the logic of early warning systems and does not currently include direct hardware sensor integration or live API fetching.


3. Target Users

Local Emergency Coordinators:

For quick field assessments when automated weather stations are unavailable.

Coastal Residents: Individuals requiring a straightforward tool to understand the severity of local weather reports.

Educational Institutions: As a demonstration tool for applying conditional logic to real-world safety scenarios.


4. High-Level Features

 
 Dynamic Risk Categorization: Uses a hierarchical logic system to differentiate between "Normal," "Weather Alert," and "Cyclone Warning" statuses.
 
 Context-Aware Alerts: Adjusts the severity of the warning based on whether current conditions (rain/wind) are likely to accelerate the storm.
 
 Input Validation & Error Handling: Ensures system reliability by catching non-numerical input errors and preventing script crashes.
 
 Standardized Input/Output: Features a clean CLI workflow for ease of use in high-stress environments.
