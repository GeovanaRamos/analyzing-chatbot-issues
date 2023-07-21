import csv
import requests

def fetch_github_repositories(organization, token):
    repositories = []
    page = 1
    per_page = 100
    url = f"https://api.github.com/orgs/{organization}/repos?page={page}&per_page={per_page}"
    headers = {"Authorization": f"Bearer {token}"}

    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            page_repositories = response.json()
            repositories += [repo["name"] for repo in page_repositories]
            if len(page_repositories) == per_page:
                page += 1
                url = f"https://api.github.com/orgs/{organization}/repos?page={page}&per_page={per_page}"
            else:
                break
        else:
            print(f"Error: {response.status_code}")
            break

    return repositories

def fetch_repository_issues(organization, repository, token):
    issues = []
    page = 1
    per_page = 100
    url = f"https://api.github.com/repos/{organization}/{repository}/issues?state=all&page={page}&per_page={per_page}"
    headers = {"Authorization": f"Bearer {token}"}

    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repository_issues = response.json()
            for issue in repository_issues:
                if "pull_request" not in issue:
                    issues.append(issue)
            if len(repository_issues) == per_page:
                page += 1
                url = f"https://api.github.com/repos/{organization}/{repository}/issues?state=all&page={page}&per_page={per_page}"
            else:
                break
        else:
            print(f"Error: {response.status_code}")
            break

    return issues

def save_issues_to_csv(issues, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Repository", "Title", "Body", "Link"])
        for issue in issues:
            repo_name = issue["repository_url"].split("/")[-1]
            issue_link = issue["html_url"]
            writer.writerow([repo_name, issue["title"], issue["body"], issue_link])

organization_name = "BLIND"

# Enter your GitHub personal access token
token = ""

repositories = [
    '2019.1-ADA',
    '2022-2-Bote',
    '2019.1-Aix',
    '2021.1-AlligaBot',
    '2019.1-ADA-github',
    '2020.1-DoctorS-Bot',
    '2019.2-Chatbot-Nilo',
    '2019.1-Ludum',
    '2019.1-Gaia',
    '2019.1-PyLearner',
    '2019.1-Tino',
    '2019.2-GloriaBot',
]

all_issues = []
for repository in repositories:
    repository_issues = fetch_repository_issues(organization_name, repository, token)
    all_issues += repository_issues

save_issues_to_csv(all_issues, "issues_chatbot.csv")


