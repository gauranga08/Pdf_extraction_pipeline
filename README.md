# PDF Information Extraction Pipeline

## Objective

This project creates a pipeline that utilizes LLMs from the Groq API to extract structured information from a PDF document. The pipeline processes the PDF and generates summaries, flashcards, search queries, and curated image URLs based on the content. It also leverages OCR technology using PyTesseract to extract text from images generated from the PDF.

## Technology Overview

- **OCR Technology**: The pipeline uses [PyTesseract](https://pypi.org/project/pytesseract/) for Optical Character Recognition (OCR) to extract text from images.
- **LLM Model**: The project employs the `llama-3.1-70b-versatile` model from the Groq API(https://groq.com/), which is known for its speed and efficiency in inference tasks. Groq utilizes a specialized architecture called **Language Processing Unit (LPU)**, designed specifically for Natural Language Processing (NLP) tasks, which significantly enhances performance compared to traditional CPU or GPU processing.

## Setup Instructions

### Prerequisites

1. **Create a Groq API Key**: 
   - Sign up for an account on the Groq website.
   - Generate your free API key from your Groq account dashboard (https://console.groq.com/keys).
2. **Install Tesseract OCR**: Setup in your machine

## Requirements

### Input

- A PDF(CVS) document in 'inputs/pdfs' folder.

### Output

The pipeline generates the following for the given PDF:

1. A summary of the content for each page.
2. A set of useful flashcards based on the content.
3. For each page:
   - A search query that can be used to find relevant images for the content.
   - A curated list of image URLs from Google Images that are relevant to the content.

## Specific Tasks

1. **Prompt Engineering**: Thoughtfully designed prompts for each task that interact with the LLM.
2. **Page Summarization**: Generated concise summaries (50-100 words) for each page using LLMs.
3. **Flashcard Generation**: Create question-answer pairs based on the content, with at least 3 flashcards per page.
4. **Search Query Generation and Image Search**: Generate relevant search queries for each page, fetch image URLs programmatically, and provide a list of 5-10 relevant image URLs.
5. **Pipeline Integration**: Combine all components into a cohesive pipeline to process the entire 100-page document efficiently.

## Technical Requirements

- **Language**: Python
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gauranga08/Pdf_extraction_pipeline.git
   cd Pdf_extraction_pipeline

2. Create a Virtual Environment:
3. ```bash
   python -m venv myenv
   source myenv/bin/activate  # Use `myenv\Scripts\activate` on Windows
4. Install Dependencies:
   ```bash
   pip install -r requirements.txt
6. Set Up the Groq API Key in .env file(recommended practice) or directly paste in llm_processor.py
7. Ensure the PDF file is placed in the input/pdfs folder of your project.
8. ```bash
   Run python main.py
9. Monitor the logs.log file to keep track of the processing status.
10. Upon completion, the generated JSON files will be located in the output folder
11. For any directory related issue refer to config.yaml file



## Scope for Improvement

The current implementation can be enhanced in several ways:

- **Parallel Processing**: The image processing and LLM processing can be performed using parallel processing or multiprocessing techniques. This approach will significantly increase the processing speed, allowing multiple pages to be processed simultaneously.


- **User Interface**: Consider adding a user-friendly interface for easier interaction with the pipeline.

- **Testing**: Implement unit tests and integration tests to ensure the reliability and maintainability of the codebase.

- **Cloud Storage**: Using cloud services like AWS S3 to store images and JSON files will provide additional robustness and scalability, enabling easy access and management of large datasets.

- **Data Security**: If processing data in a secured environment is a priority, consider utilizing Azure OpenAI services. This can enhance data security by leveraging cloud-based infrastructure and advanced AI capabilities.






