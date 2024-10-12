# PDF Information Extraction Pipeline

## Objective

This project creates a pipeline that utilizes LLMs from the Groq API to extract structured information from a PDF document. The pipeline processes the PDF and generates summaries, flashcards, search queries, and curated image URLs based on the content. It also leverages OCR technology using PyTesseract to extract text from images generated from the PDF.

## Technology Overview

- **OCR Technology**: The pipeline uses [PyTesseract](https://pypi.org/project/pytesseract/) for Optical Character Recognition (OCR) to extract text from images.
- **LLM Model**: The project employs the `llama-3.1-70b-versatile` model from the Groq API(https://groq.com/), which is known for its speed and efficiency in inference tasks. Groq utilizes a specialized architecture called **Language Processing Unit (LPU)**, designed specifically for Natural Language Processing (NLP) tasks, which significantly enhances performance compared to traditional CPU or GPU processing.

## Design

### Process Flow
1. **PDF Loading**: The PDF document is loaded using the PyMuPDF library.
2. **Image Extraction**: Each page of the PDF is converted into images using the `get_pixmap` method.
3. **Text Extraction**: For each image, the `image_to_string` function uses Tesseract OCR to extract text.
4. **LLM Processing**: The extracted text is sent to a single LLM call where:
   - A concise summary of the page content is generated.
   - Flashcards in the form of question and answer pairs are created.
   - A search query is formulated based on the text.
5. **Web Scraping**: The generated search query is passed to a function that uses Beautiful Soup to scrape relevant URLs from the web.
6. **Data Compilation**: All results (summary, flashcards, search query, and URLs) are compiled into seperate structured JSON format.
## Prompt Engineering Strategies
In this project, I employed various prompt engineering strategies to optimize interactions with the language model (LLM), enhance clarity, and address prompt injection risks. Key strategies include:

- **Clarity and Specificity**: Used straightforward language and tailored prompts to clearly specify tasks, avoiding ambiguity.
- **One-Shot Prompting**: Used one-shot prompting for clarity, demonstrating expected outputs with single examples while ensuring robustness against manipulation.
- **Robust with Prompt injection** 
- **Contextual Alignment**: Provided necessary background information and aligned prompts with user intent to ensure relevance.
- **Structured and Dynamic Format**: Employed structured templates with dynamic placeholders for variables to guide the model towards the desired output format.
- **Validation and Conciseness**: Sanitized inputs for security and kept prompts concise yet informative.
- **Task-Specific Language**: Utilized relevant terminology and phrasing tailored to specific tasks.
- **Testing and Iteration**: Regularly tested and refined prompts based on response quality.


### JSON Output Structure
The final output will be structured in a JSON format that includes:
- **Page Number**
- **Summary**
- **Flashcards** (as question-answer pairs)
- **Search Query**
- **Related URLs**

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

- **Parallel Processing**: The image extraction and LLM processing tasks can be parallelized using multi-processing techniques. By processing multiple pages simultaneously in batches, the pipeline's speed and efficiency will be significantly improved, especially for larger documents.
- **Fine-tuning**: Because these models used are foundational LLMs, they can be fine-tuned on specific to the subject to be more accurate and efficient.
- **Improved Image URL Quality**: Currently, the pipeline uses BeautifulSoup to scrape image URLs. Implementing a more specialized Google Image API or a similar service will yield higher-quality image results and more relevant content, improving the accuracy and relevance of image URL suggestions.
- **User Interface**: Consider adding a user-friendly interface for easier interaction with the pipeline.

- **Testing**: Implement unit tests and integration tests to ensure the reliability and maintainability of the codebase.

- **Cloud Storage**: Using cloud services like AWS S3 to store images and JSON files will provide additional robustness and scalability, enabling easy access and management of large datasets.

- **Data Security**: If processing data in a secured environment is a priority, consider utilizing Azure OpenAI services. This can enhance data security by leveraging cloud-based infrastructure and advanced AI capabilities.






