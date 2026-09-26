# github-docgen-ai

`github-docgen-ai` is an AI-powered tool designed to automatically generate documentation for GitHub repositories. This tool leverages natural language processing and machine learning to understand the codebase and generate comprehensive documentation that is both accurate and user-friendly.

## Key Features

- **Automatic Documentation Generation**: Automatically analyzes the codebase and generates documentation in Markdown format.
- **Real-time Updates**: Keeps documentation up-to-date with changes in the codebase.
- **Cross-language Support**: Supports multiple programming languages, ensuring broad compatibility.
- **Customizable Templates**: Allows users to customize the templates used for generating documentation.
- **Integration with GitHub**: Seamlessly integrates with GitHub, ensuring that documentation is always up-to-date.

## Project Structure

```
github-docgen-ai/
├── .env.example          # Example environment variables
├── .gitignore              # Files and directories to be ignored by git
├── config.yaml             # Configuration file for the application
├── main.py                 # Main entry point of the application
├── requirements.txt        # List of dependencies
└── src/
    ├── __init__.py           # Python package marker
    ├── doc_generator.py      # Module for generating documentation
    ├── github_client.py      # Module for interacting with GitHub API
    └── parser.py             # Module for parsing the codebase
```

## Getting Started & Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/yourusername/github-docgen-ai.git
    cd github-docgen-ai
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Copy the `.env.example` file to `.env` and set the necessary environment variables:

    ```sh
    cp .env.example .env
    # Edit .env to set your GitHub API token and other necessary configurations
    ```

## Usage Guide

### Running the Application

To generate documentation for a specific GitHub repository, run the following command:

```sh
python main.py --repo <repository_url>
```

Replace `<repository_url>` with the URL of the GitHub repository you want to document.

### Customizing Documentation

You can customize the templates used for generating documentation by modifying the `config.yaml` file. The available options include:

- `template_path`: Path to the template file.
- `output_path`: Path to the output documentation file.
- `language`: Programming language of the codebase.

For more details, refer to the `config.yaml` file and the `doc_generator.py` module.

### Additional Features

- **Real-time Updates**: The tool automatically updates the documentation whenever changes are made to the codebase.
- **Cross-language Support**: The tool supports multiple programming languages, ensuring broad compatibility.

### Troubleshooting

- If you encounter any issues, check the `.env` file for the correct configuration and ensure that the GitHub API token has the necessary permissions.
- If the tool is not updating the documentation as expected, check the logs for any errors or warnings.

By following these steps, you can easily generate and maintain up-to-date documentation for your GitHub repositories using `github-docgen-ai`.