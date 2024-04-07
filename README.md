# Esilv_Api_Project

### Project
**Create an API for AI News Overview**

This project involves creating an API that provides news related to Artificial Intelligence (AI). Each group will select an AI-related site (e.g., OpenAI blog) as their source.

### Objective

The goal is to fetch information from the chosen site, either by scraping or through an existing API. You will create several endpoints for different purposes:

    - /get_data: Fetches a list of articles from the site. Retrieving 5 articles might be sufficient.
    - /articles: Displays information about the articles, including the article number, title, publication date, etc., but not the content itself.
    - /article/<number>: Accesses the content of a specified article.
    - /ml or /ml/<number>: Executes a machine learning script. Depending on the desired goal, it applies to either all articles or a single one. For example, sentiment analysis.

You can choose website about many subject like:

    - Updates on new AI tools.
    - News about image generation.
    - Information on new models.
    - Research papers, such as those from ArXiv or Google DeepMind.

### Process

    1. Each group should create a branch named after the names of the group members.
    2. Inside the branch, create a working directory named after the chosen site.
    3. Add a file named composition.txt that lists the members of the group.
    4. Add a section below these rules to explain your project, describe the created endpoints and their uses, and provide examples.


### Project Explanition
    Before launching project:
    pip install -r requirements.txt

    We decided to use the News API for our project.
    It has an everything endpoint: 'https://newsapi.org/v2/everything' that works with a query parameter.
    This helps to decide what type of articles we are searching for and how many we wants to have.
    In this project we have 4 endpoints:
        - get_data: which retrieve all the data about the 5 first articles of the given query sorted by publication dates.
        - articles: which retrieve same data as the previous endpoint but it formats the given content to not display the content and summary of the article.
        - articles/{number}: which retrieve the content of a specific article
        - ml/{number}: which apply machine translation algorithm to translate the article summary from english to french
