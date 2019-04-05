import os
from pygit2 import Repository, discover_repository, GitError
import click


def list_dir_repositories(path):
    repositories = [discover_repository(path+dir_name)
                    for dir_name in os.listdir(path)]

    return [repo for repo in repositories if repo is not None]


def get_current_branch_name(repo_path):
    repo = Repository(repo_path.rstrip('/'))
    try:
        return repo.head.shorthand
    except GitError:
        return "Not Found"


if __name__ == "__main__":
    print({get_current_branch_name(repo_path): repo_path
           for repo_path in list_dir_repositories(path)})
