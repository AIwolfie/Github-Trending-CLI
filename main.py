import argparse
import sys
import github_api
import utils

def main():
    parser = argparse.ArgumentParser(
        description="GitHub Trending CLI - Fetch trending repositories on GitHub.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "--duration", 
        choices=["day", "week", "month", "year"], 
        default="week",
        help="Time range for repository creation."
    )
    
    parser.add_argument(
        "--limit", 
        type=int, 
        default=10,
        help="Number of repositories to display."
    )

    args = parser.parse_args()

    print(f"\n--- Fetching top {args.limit} trending repositories for the last {args.duration} ---\n")

    try:
        repos = github_api.fetch_trending_repos(duration=args.duration, limit=args.limit)
        
        if not repos:
            print("No trending repositories found matching your criteria.")
            return

        table_output = utils.format_table(repos)
        print(table_output)
        print(f"\nTotal fetched: {len(repos)}")

    except github_api.GitHubAPIError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
