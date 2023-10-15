# Ouo.io Bypass Application 

## Overview
This application is developed in Python using the FastAPI framework. It provides a simple tool to bypass ouo.io based URL's. 

## System Requirements
- Python 3.11.5
- FastAPI
- Pydantic
- bypass (note: this package is not listed among the installed packages in the system message. Please ensure this package is installed)

## How to run the app

1. Install all necessary packages listed in the system requirements.
2. Run your FastAPI application using command: `uvicorn main:app --reload`
3. Open `http://127.0.0.1:8000/` in your browser to access the root endpoint.
4. POST requests can be sent to `http://127.0.0.1:8000/bypass/` with a JSON body containing an "url" key with a string value representing the ouo.io url you want to bypass.

## API Reference

### Root Endpoint (`GET /`)
Returns a welcoming message indicating the service is running.

**Sample response:**