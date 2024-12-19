import subprocess
import os
from pathlib import Path

def get_git_root():
    """Get the root directory of the Git repository."""
    try:
        result = subprocess.run(['git', 'rev-parse', '--show-toplevel'], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        print("Error: This is not a git repository")
        return None

def read_gitignore(git_root):
    """Read .gitignore file and return list of patterns."""
    gitignore_path = os.path.join(git_root, '.gitignore')
    if not os.path.exists(gitignore_path):
        print("Error: .gitignore file not found")
        return []
    
    with open(gitignore_path, 'r', encoding='utf-8') as f:
        # Filter out empty lines and comments
        patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return patterns

def get_tracked_files():
    """Get list of all tracked files in git."""
    try:
        result = subprocess.run(['git', 'ls-files'], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        print("Error: Failed to get tracked files")
        return []

def should_be_ignored(file_path, patterns):
    """Check if file should be ignored based on .gitignore patterns."""
    try:
        result = subprocess.run(['git', 'check-ignore', file_path], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def main():
    # Get git repository root
    git_root = get_git_root()
    if not git_root:
        return

    # Change to git root directory
    os.chdir(git_root)

    # Get .gitignore patterns
    patterns = read_gitignore(git_root)
    if not patterns:
        return

    # Get tracked files
    tracked_files = get_tracked_files()
    
    # Find tracked files that should be ignored
    files_to_untrack = []
    for file_path in tracked_files:
        if should_be_ignored(file_path, patterns):
            files_to_untrack.append(file_path)

    if not files_to_untrack:
        print("No tracked files found that should be ignored.")
        return

    print("\nFound the following tracked files that should be ignored:")
    for file in files_to_untrack:
        print(f"- {file}")

    # Confirm with user
    response = input("\nDo you want to untrack these files? (y/N): ").lower()
    if response != 'y':
        print("Operation cancelled.")
        return

    try:
        # Remove files from git tracking but keep them in working directory
        files_arg = ' '.join(f'"{f}"' for f in files_to_untrack)
        subprocess.run(f'git rm --cached {files_arg}', shell=True, check=True)
        print("\nSuccessfully untracked files. Changes have been staged.")
        print("Please commit these changes to complete the cleanup.")
    except subprocess.CalledProcessError:
        print("Error: Failed to untrack files")

if __name__ == "__main__":
    main()
