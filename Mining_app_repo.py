import requests
import markdown
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Function to fetch and parse README.md content from a GitHub repo URL
def parse_readme_from_url(repo_url):
    # Parse the GitHub URL to extract the owner and repo name
    parsed_url = urlparse(repo_url)
    path_parts = parsed_url.path.split('/')
    owner = path_parts[1]
    repo_name = path_parts[2]

    # Construct the README.md URL
    readme_url = f"https://raw.githubusercontent.com/{owner}/{repo_name}/main/README.md"

    # Fetch the README.md content
    response = requests.get(readme_url)
    markdown_content = response.text

    # Parse the markdown content
    html_content = markdown.markdown(markdown_content)

    # Use BeautifulSoup to parse HTML and extract links
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all links containing the keyword "github.com"
    github_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and 'github.com' in href:
            github_links.append(href)

    return github_links

# Fetch the main README.md content
url = "https://raw.githubusercontent.com/zhimin-z/awesome-awesome-artificial-intelligence/main/README.md"
response = requests.get(url)
markdown_content = response.text

# Parse the main markdown content
html_content = markdown.markdown(markdown_content)
soup = BeautifulSoup(html_content, 'html.parser')

# Find all links containing the keyword "GPT"
links_with_gpt_keyword = []
for link in soup.find_all('a'):
    if 'gpt' in link.get_text().lower():
        links_with_gpt_keyword.append((link.get_text(), link.get('href')))
    elif 'agent' in link.get_text().lower():
        links_with_gpt_keyword.append((link.get_text(), link.get('href')))
    elif 'llm' in link.get_text().lower():
        links_with_gpt_keyword.append((link.get_text(), link.get('href')))

# For each GitHub link containing "GPT", parse its README.md content and extract GitHub linkages
app_repo_links = set()
for title, github_link in links_with_gpt_keyword:
    github_links = parse_readme_from_url(github_link)
    print(f"Awesome List: {title}\nGitHub Link: {github_link}\n")
    for link in github_links:
        if len(link.split('/')) == 5:
            app_repo_links.add(link)

with open('app_repo_links.txt', 'w') as f:
    for link in app_repo_links:
        f.write(link + '\n')
