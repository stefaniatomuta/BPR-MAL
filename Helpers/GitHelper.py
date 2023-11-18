import os
import git
import uuid

def clone_repositories(file_path, destination_folder):
    with open(file_path, 'r') as file:
        repositories = [line.strip() for line in file if line.strip()]

    for repo_url in repositories:
        try:
            repo = git.Repo.clone_from(repo_url, os.path.join(destination_folder, str(uuid.uuid4())))
            print(f"Repository cloned successfully: {repo_url}")
        except Exception as e:
            print(f"Failed to clone repository {repo_url}. Error: {str(e)}")


if __name__ == "__main__":
    # Provide the path to the text file containing GitHub repository URLs
    file_path = r"path to file with repositories"

    # Provide the path to the folder where you want to clone repositories
    destination_folder = r"path to repo folder"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    clone_repositories(file_path, destination_folder)