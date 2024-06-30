# IoT Temperature Monitoring System

This project demonstrates a comprehensive IoT temperature monitoring system using AWS services. The system collects temperature data from sensors (script), processes it, stores it in DynamoDB, analyzes it in Athena, and visualizes it in Amazon QuickSight.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
  - [AWS Configuration](#aws-configuration)
  - [Local Setup](#local-setup)
- [Usage](#usage)
- [Analyzing Data in Athena](#analyzing-data-in-athena)
- [Visualizations](#visualizations)
- [License](#license)

## Project Overview

This project simulates IoT temperature sensors and processes their data using AWS services. The data is stored in DynamoDB and visualized using Amazon QuickSight. The main components are:

- **AWS IoT**: For ingesting sensor data.
- **AWS Lambda**: For processing data and storing it in DynamoDB.
- **Amazon DynamoDB**: For storing temperature data.
- **AWS Glue**: For cataloging DynamoDB data.
- **Amazon Athena**: For querying DynamoDB data.
- **Amazon QuickSight**: For data visualization.

## Architecture

![Architecture Diagram](Architecture.jpg)

## Setup Instructions

### AWS Configuration

1. **Create and Configure IoT Thing**:
   - Create an IoT thing in the AWS IoT console.
   - Attach the necessary policy to allow data publishing.

2. **Deploy Lambda Functions**:
   - Upload the `process_temperature_data` Lambda function.
   - Set up necessary IAM roles with appropriate permissions for DynamoDB, SNS, and CloudWatch.

3. **Set Up DynamoDB**:
   - Create a DynamoDB table named `TemperatureData` with appropriate attributes.

4. **Configure AWS Glue**:
   - Create a Glue database named `temperature_database`.
   - Create a Glue crawler to catalog the DynamoDB table.

5. **Athena Setup**:
   - Create an Athena data source using the Glue catalog.
   - Set the query results location in an S3 bucket.

6. **QuickSight Integration**:
   - Connect QuickSight to the Athena data source.
   - Create visualizations.

### Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amirmalaeb/IoT-Temperature-Monitoring-System.git
   cd IoT-Temperature-Monitoring-System
