import requests
import statistics

GITHUB_TOKEN = "your_token_here"
USERNAME = "ivybiosciences"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def get_all_repos():
    """Get all public repos"""
    url = f"https://api.github.com/users/{USERNAME}/repos"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_commit_stats(repo_name):
    """Get commit statistics for a repository"""
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/stats/contributors"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        total_commits = sum(contributor['total'] for contributor in data)
        return total_commits
    return 0

def calculate_metrics():
    """Calculate custom metrics"""
    repos = get_all_repos()

    metrics = {
        'total_repos': len(repos),
        'total_stars': sum(repo['stargazers_count'] for repo in repos),
        'total_forks': sum(repo['forks_count'] for repo in repos),
        'languages': set(repo['language'] for repo in repos if repo['language']),
        'total_commits': 0,
    }

    for repo in repos:
        metrics['total_commits'] += get_commit_stats(repo['name'])

    return metrics

if __name__ == '__main__':
    metrics = calculate_metrics()

    print("## Custom Metrics")
    print(f"- Total Repositories: {metrics['total_repos']}")
    print(f"- Total Stars: {metrics['total_stars']}")
    print(f"- Total Forks: {metrics['total_forks']}")
    print(f"- Total Commits: {metrics['total_commits']}")
    print(f"- Languages: {', '.join(metrics['languages'])}")