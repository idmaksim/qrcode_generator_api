# QR Code Generator Service

## Overview

This project is a QR code generator service built using FastAPI. The main functionality provided by this service is to generate QR codes based on user input and return the QR code image as a byte array.

## Features

- Generate QR codes with customizable settings such as box size, border size, fill color, and background color.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/idmaksim/qrcode_generator_api.git
   cd qrcode_generator_api
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the FastAPI application:**

   ```bash
   uvicorn src.main:app --reload
   ```

2. **Access the API documentation:**

   Open your web browser and navigate to `http://127.0.0.1:8000/docs` to interact with the API using the automatically generated Swagger UI.

## Main Service

The core functionality of this project is encapsulated in the `QrCodeService` class. The service handles QR code generation and converts the generated QR code image into a byte array for easy transmission.

### QrCodeInfo Schema

The `QrCodeInfo` schema is used to validate the input data required for generating a QR code. It includes fields like `data`, `box_size`, `border`, `fill`, and `back_color`.
