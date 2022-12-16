from github import Github, NamedUser
from secret import GPAT

ENDPOINT = "https://api.github.com/"
OWNER = "CannonLock"
REPO = "AutoPR"
BRANCH = "master"
PROJECT_NAME = "asynchrony"
SAMPLE_INPUT = """Department: Institute of Neuroscience
Description: We investigate how synchronous population activity arise in spiking dynamics
  of the sensory and other cortical areas. We especially focus on how primary auditory
  cortex modulate dynamical timescales during spontaneous bump dynamics in quiet wake
  condition and up and down states in anesthetized and sleep conditions.
FieldOfScience: Neuroscience
ID: '437'
Organization: University of Oregon
PIName: Yashar Ahmadian
Sponsor:
  CampusGrid:
    Name: OSG Connect
"""


def main():

    g = Github(GPAT)

    repo = g.get_repo(f"{OWNER}/{REPO}")

    # Create new branch
    target_branch = f"add-project-{PROJECT_NAME}"
    repo.create_git_ref(ref=f"refs/heads/{target_branch}", sha=repo.get_branch(repo.default_branch).commit.sha)

    info = repo.create_file(f"data/{PROJECT_NAME}.yaml", f"Add User {PROJECT_NAME}", SAMPLE_INPUT, branch=target_branch)

    pull_info = repo.create_pull(title=f"Add User {PROJECT_NAME}", body="Add a new user", head=target_branch, base=repo.default_branch)


if __name__ == "__main__":
    main()
