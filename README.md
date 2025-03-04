# Capital Edge Analytics – Financial Data Pipeline


## Table of Contents

- [Introduction](#introduction)
- [Project Scope](#project-scope)
- [Project Workflow](#project-workflow)
- [Data Extraction Process](#data-extraction-process)
- [Storage and Database Creation](#storage-and-database-creation)
- [Data Ingestion into Azure](#data-ingestion-into-azure)
- [Transformation using Databricks](#transformation-using-databricks)
- [Data Architecture](#data-architecture)
- [Project Execution and Results](#project-execution-and-results)
- [Conclusion](#conclusion)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [License](#license)

## Introduction

The Capital Edge Analytics project is focused on developing a robust, cloud-based data pipeline for financial data management. This pipeline automates the ingestion, staging, transformation, and loading of financial market data, ensuring real-time availability, data integrity, and operational efficiency for accurate analytics.

## Project Scope

This project aims to streamline financial market data management by:
- Automating data extraction from the Alpha Vantage API.
- Storing raw and processed data using a structured, scalable cloud-based storage solution.
- Transforming the data to enhance reliability and analytical readiness.
- Providing a scalable pipeline to support real-time analytics.

## Project Workflow

The ETL pipeline follows these key steps:
1. **Data Extraction:**  
   Leverages the Alpha Vantage API to fetch daily time series data for selected stocks.
2. **Storage:**  
   Uses an Azure Medallion storage structure to manage raw and transformed data seamlessly.
3. **Data Ingestion:**  
   Loads the extracted data into the Azure Data Lake Storage container.
4. **Transformation:**  
   Utilizes Databricks for cleaning and structuring data, ensuring high data quality.
5. **Orchestration:**  
   Integrates all steps into a continuous pipeline for real-time data updates.

## Data Extraction Process

The data extraction module is designed to:
- **Fetch Data:** Call the Alpha Vantage API for financial market data.
- **Error Handling:** Validate API responses and manage rate limits.
- **Modular Design:** Support multiple stock symbols (e.g., AAPL, GOOGL, MSFT) through configuration settings.

## Storage and Database Creation

The project uses an Azure-based storage solution that follows the Medallion architecture:
- **Raw Data Zone:** Stores initial API responses.
- **Staging/Processed Data Zone:** Holds data after transformation, ready for analysis.
- **Scalability:** Designed to integrate with other database services as needed.

## Data Ingestion into Azure

Extracted data is ingested into an Azure Data Lake Storage container, which:
- **Ensures Accessibility:** Centralizes financial data for analytics.
- **Maintains Structure:** Uses CSV format with defined columns (Date, Open, High, Low, Close, Volume, Symbol).
- **Supports Re-ingestion:** Allows new data to be combined with existing datasets.

## Transformation using Databricks

Databricks is employed to transform and orchestrate the data:
- **Data Cleaning:** Ensures that only new or updated records are processed.
- **Standardization:** Converts raw JSON into a consistent, tabular format.
- **Integration:** Provides a secure environment to access Azure Data Storage and transform data efficiently.

## Data Architecture

The project architecture is built on modern cloud technologies:
- **API Integration:** Fetches real-time data from Alpha Vantage.
- **Spark & PySpark:** Utilized for reading from and writing to Azure storage.
- **Cloud Scalability:** Uses Azure services to maintain a robust, scalable data pipeline.
- **Modular Components:** Separates concerns into extraction, transformation, and loading modules for maintainability.

## Project Execution and Results

The execution of the pipeline has yielded:
- **Consistent Data Updates:** Reliable ingestion of daily stock data.
- **Enhanced Data Integrity:** Automated checks and error handling ensure high-quality data.
- **Actionable Insights:** Transformed data is now ready for further financial analysis.

## Conclusion

The Capital Edge Analytics project demonstrates a comprehensive solution for managing financial data through automation and cloud technology. The pipeline not only streamlines data ingestion but also ensures that the data is reliable and scalable for real-time analytics.

## Installation & Setup

### Prerequisites

- **Python 3.7+**
- **Apache Spark** with PySpark installed
- Libraries:
  - `requests`
  - `pandas`
  - `pyspark`

Install dependencies via pip:

```bash
pip install requests pandas pyspark




