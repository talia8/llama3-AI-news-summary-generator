# Briefly: News AI Summarizer

Welcome to the News AI Summarizer project! This web application allows users to input specific keywords or topics and receive summarized news articles, making it easier to stay informed about current events without sifting through large amounts of text.
#

<img src="screenshots/Screenshot 2024-10-03 210301.png" >
<br/>
<img src="screenshots/Screenshot 2024-10-03 210409.png">

## Why LLama3 Hosted on Groq?

For the summarization process, I chose to use LLama3 hosted on Groq because I wanted to leverage the 70 billion parameter model without worrying about hardware resources. However, please note that the open-source version has a limited number of API calls per minute.

## Features

- Input specific keywords/topics to fetch relevant news articles.
- Generate concise summaries of the latest news using LLama3.
- User-friendly interface designed with Bootstrap for easy navigation.

## Technologies Used

- **Django**: Web framework for building the application.
- **News API**: To scrape relevant news articles from various sources.
- **LLama3**: LLM with advanced NLP capabilities.
- **Groq**: Hosting platform for running LLMs.
- **Bootstrap**: Frontend framework used for responsive design.
- **Figma**: Design tool for creating the user interface.

## Getting Started

To clone and run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
     
4. **Add your own API Keys**:
   You can get them from [Groq](https://console.groq.com/keys) and [News API](https://newsapi.org/).

5. **Run the app**:
   ```bash
   python manage.py runserver
   ```
   Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions will help improve the project and expand its functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
