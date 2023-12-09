import os
import git

def clone_repositories(file_path, destination_folder):
    with open(file_path, 'r') as file:
        repositories = [line.strip() for line in file if line.strip()]

    for repo_url in repositories:
        try:
            repo_name = get_repo_name(repo_url)
            repo = git.Repo.clone_from(repo_url, os.path.join(destination_folder, f'{repo_name[0]}_{repo_name[1]}'))
            print(f"Repository cloned successfully: {repo_url}")
        except Exception as e:
            print(f"Failed to clone repository {repo_url}. Error: {str(e)}")
def get_repo_name(repo_url):
    # Extract owner name from GitHub repository URL
    parts = repo_url.split('/')
    return parts[-2],parts[-1]

if __name__ == "__main__":
    # Provide the path to the text file containing GitHub repository URLs
    file_path = r"your path to the list of repos to clone"

    # Provide the path to the folder where you want to clone repositories
    destination_folder = r"your path to the folder where to clone the repos"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    clone_repositories(file_path, destination_folder)