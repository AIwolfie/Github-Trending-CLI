import requests
import utils

class GitHubAPIError(Exception):
    """Custom exception for GitHub API related errors."""
    pass

def fetch_trending_repos(duration='week', limit=10):
    """
    Fetches trending repositories from GitHub based on duration and limit.
    """
    since_date = utils.get_since_date(duration)
    query = f"created:>{since_date}"
    
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        
        # Handle Rate Limiting
        if response.status_code == 403:
            raise GitHubAPIError("API rate limit exceeded. Please try again later.")
        
        # Handle other non-200 responses
        response.raise_for_status()
        
        data = response.json()
        return data.get('items', [])
        
    except requests.exceptions.ConnectionError:
        raise GitHubAPIError("Network error: Could not connect to GitHub API. Please check your internet connection.")
    except requests.exceptions.Timeout:
        raise GitHubAPIError("Request timed out. GitHub API might be slow or unreachable.")
    except requests.exceptions.RequestException as e:
        raise GitHubAPIError(f"An unexpected error occurred: {str(e)}")
