# GitHub Trending CLI

A simple command-line tool to fetch and display trending repositories from GitHub based on a selected time range.

## Features
- Fetches trending repositories using the GitHub Search API.
- Filter by duration: `day`, `week`, `month`, `year`.
- Customizable limit on the number of results.
- Clean, table-style output with repository details and descriptions.
- Proper error handling for network issues and rate limiting.

## Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/AIwolfie/Github-Trending-CLI.git
   cd Github-Trending-CLI
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the tool using Python:

```bash
python main.py --duration [day|week|month|year] --limit [number]
```

### Examples

- **Fetch trending repos from the last week (default)**:
  ```bash
  python main.py
  ```

- **Fetch top 20 trending repos from the last month**:
  ```bash
  python main.py --duration month --limit 20
  ```

- **Fetch trending repos from the last day**:
  ```bash
  python main.py --duration day
  ```

## Project Structure
- `main.py`: CLI entry point and argument parsing.
- `github_api.py`: Logic for interacting with the GitHub REST API.
- `utils.py`: Utility functions for date calculation and output formatting.
- `requirements.txt`: Project dependencies.

## Output Format
The tool displays results in a clean table format:
```text
#   | Repository                     | Stars    | Language        | URL
----------------------------------------------------------------------------------------------------
1   | user/repo                      | 1234     | Python          | https://github.com/user/repo
    └─ A brief description of the repository...
```