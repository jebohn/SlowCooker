# Precision Slow Cooker (In-Progress)
Contributors: Adam Vekris, Jessica Bohn

## Description:
RemoteCook is a precision slow cooker which takes user inputted temperature intervals to dynamically adjust the internal cooking temperature with SSR control, PID logic, a web API interface, and a database managed with SQLite. For demonstration purposes, hardware is simulated with mock classes, allowing the program to run on any machine.

## Motivation:
The purpose of this project is to enable precise temperature control for recipes that require lower temperatures than slow cookers are built to maintain. Slow cookers in the US are designed to eventually reach 212 degrees F, even on the ‘low’ setting. This makes recipes that require lower, gentler cooking over long periods impossible, in spite of the fact that low & slow cooking is the exact purpose of a slow cooker. RemoteCook allows a user to set a desired cook temperature and time for their slow cooker, providing true slow cooking as well as greater precision than high/low and 4 hr/8 hr settings. This allows preparation of dishes such as seitan which require true slow cooking.

## Installation:
1. Clone the repository
2. Navigate to the project folder
3. Create and activate the virtual environment
4. Install dependencies
5. Run the Flask app
6. Go to `http://127.0.0.1:5000/home` in your browser

## Languages & Frameworks:
- Python
- Flask
- HTML
- SQLite

## Components:
- Raspberry Pi
- Solid State Relay
- Thermocouple
- Amplifier
- Crock-Pot

## Features:
- PID control logic to reach and maintain target temperature
- Configurable cook times, temperatures, and intervals
- API and web interface using Flask to control program and view temperature log
- Recipe preset creation system that saves presets to the disk
- Fully testable with simulated hardware

## Future Work/Planned Functionality:
- Integration with hardware
- Refinement of web interface and integration with recipe preset creator backend
