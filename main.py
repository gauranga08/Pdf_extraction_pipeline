import yaml
from pathlib import Path
import logging
# from pdf_parser import process_pdf
import os
from pdf_parser import process_pdf




# Set up logging to write to a file
logging.basicConfig(filename="logs.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()  # Add a console handler for terminal output
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

# Function to load configuration
def load_config():
    try:
        executable_path = os.path.abspath(__file__)
        executable_dir = os.path.dirname(executable_path)
        with open(f"{executable_dir}/config.yaml", "r") as file:
            yaml_data = yaml.safe_load(file)
        logging.info("Configuration file loaded successfully.")
        return yaml_data
    except FileNotFoundError:
        logging.error("Configuration file not found.")
        raise
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        raise

# Main function to load config and start processing
def main():
    try:
        logging.info("Starting the application...")
        yaml_data = load_config()
        logging.info(f"Configuration loaded: {yaml_data}")

        # Use the pdf_path from YAML configuration
        pdf_directory = Path(os.path.expanduser(yaml_data["pdf_path"]))
        logging.info(f"Processing PDFs in directory: {pdf_directory}")

        if not pdf_directory.exists() or not any(pdf_directory.glob("*.pdf")):
            logging.error(f"No PDF files found in {pdf_directory}")
            return

        # Process each PDF file in the directory
        for pdf_path in pdf_directory.glob("*.pdf"):
            try:
                logging.info(f"Processing PDF file: {pdf_path}")
                process_pdf(pdf_path, yaml_data)
            except Exception as e:
                logging.error(f"Failed to process {pdf_path}: {e}")

        logging.info("All PDFs processed.")
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
