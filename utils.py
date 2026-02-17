from datetime import datetime, timedelta

def get_since_date(duration):
    """
    Calculates the YYYY-MM-DD date based on the duration string.
    """
    today = datetime.utcnow()
    
    if duration == 'day':
        delta = timedelta(days=1)
    elif duration == 'week':
        delta = timedelta(weeks=1)
    elif duration == 'month':
        delta = timedelta(days=30)
    elif duration == 'year':
        delta = timedelta(days=365)
    else:
        # Default to week if somehow invalid
        delta = timedelta(weeks=1)
        
    since_date = today - delta
    return since_date.strftime('%Y-%m-%d')

def format_table(repos):
    """
    Formats the repository list into a clean numbered table style.
    Using standard string formatting (no external libs).
    """
    if not repos:
        return "No repositories found for the selected criteria."

    header = f"{'#':<3} | {'Repository':<30} | {'Stars':<8} | {'Language':<15} | {'URL'}"
    separator = "-" * 100
    
    lines = [header, separator]
    
    for i, repo in enumerate(repos, 1):
        name = repo.get('full_name', 'N/A')[:30]
        stars = repo.get('stargazers_count', 0)
        lang = repo.get('language') or 'N/A'
        url = repo.get('html_url', 'N/A')
        
        line = f"{i:<3} | {name:<30} | {stars:<8} | {lang:<15} | {url}"
        lines.append(line)
        
        # Add description on a new line (indented)
        desc = repo.get('description')
        if desc:
            # Simple truncation for description
            desc_text = desc[:90].strip() + '...' if len(desc) > 90 else desc
            lines.append(f"    └─ {desc_text}")
            lines.append("") # Empty line for readability
            
    return "\n".join(lines)
