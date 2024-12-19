# Automated-News-Email-Service-Using-NewsAPI-and-Email-Integration
This project implements a script that fetches the latest news articles on a specific topic using the NewsAPI and sends them as an email. It demonstrates the integration of APIs, email functionality, and basic data processing in Python.
 News Fetching with NewsAPI

  The script uses the NewsAPI to retrieve the latest news articles related to a given topic.
  Configurable parameters include:
        Topic: The keyword to filter news articles (e.g., "Tesla").
        Date Range: Retrieves articles published from a specific date.
        Sorting: Sorts articles by publication date for the most recent news.
        Language: Filters articles by language (default: English).

2. Dynamic Email Composition

    Collects the top 20 articles and formats them into an email body.
    Includes:
        Title: The title of the article.
        Description: A brief summary of the article.
        URL: A direct link to the full article.

3. Email Integration

    Uses a custom send_email module to send the compiled news digest to the recipient's email address.
    Encodes the email content in UTF-8 to handle diverse characters and languages.

How It Works

  Set the Topic:
      Specify the topic of interest in the topic variable (e.g., "tesla").

  API Request:
      The script sends a GET request to the NewsAPI endpoint, passing the topic and other parameters.

  Process News Data:
      Parses the JSON response and extracts relevant information (title, description, URL) for up to 20 articles.

  Send Email:
      Formats the extracted information into an email body.
      Sends the email using the send_email module.

Setup Instructions

  Install Dependencies:
      Ensure requests and an email-sending library (e.g., smtplib) are installed:

        pip install requests

Obtain API Key:

    Sign up at NewsAPI and generate an API key.
    Replace the api_key variable with your API key.

Configure Email Settings:

    Set up the send_email module with the necessary SMTP configuration for your email service (e.g., Gmail, Outlook).

Run the Script:

    python news_email.py

