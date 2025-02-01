import subprocess
import os
from pathlib import Path
import shutil
import sys

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
        patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return patterns

def should_be_ignored(file_path):
    """Check if file should be ignored based on .gitignore patterns."""
    try:
        result = subprocess.run(['git', 'check-ignore', file_path], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def scan_directory(root_dir):
    """재귀적으로 디렉터리를 스캔하여 .gitignore 규칙에 맞는 파일들을 찾습니다."""
    files_to_delete = []
    empty_dirs = set()
    
    for root, dirs, files in os.walk(root_dir, topdown=False):
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, root_dir)
            
            if file == '.gitignore':
                continue
                
            if should_be_ignored(rel_path):
                files_to_delete.append(file_path)
        
        if root != root_dir:
            all_files = [os.path.join(root, f) for f in files]
            if all(f in files_to_delete for f in all_files):
                empty_dirs.add(root)
                
    return files_to_delete, empty_dirs

def delete_files(files_to_delete, empty_dirs):
    """파일과 빈 디렉터리를 실제로 삭제합니다."""
    deleted_files = []
    deleted_dirs = []
    errors = []
    
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            deleted_files.append(file_path)
        except Exception as e:
            errors.append(f"Failed to delete {file_path}: {str(e)}")
    
    for dir_path in sorted(empty_dirs, reverse=True):
        try:
            if os.path.exists(dir_path) and not os.listdir(dir_path):
                os.rmdir(dir_path)
                deleted_dirs.append(dir_path)
        except Exception as e:
            errors.append(f"Failed to delete directory {dir_path}: {str(e)}")
    
    return deleted_files, deleted_dirs, errors

def run_with_auto_input(auto_confirm=False):
    """자동 입력 모드로 스크립트를 실행합니다."""
    git_root = get_git_root()
    if not git_root:
        return

    os.chdir(git_root)
    print("Scanning repository for files that should be ignored...")
    
    files_to_delete, empty_dirs = scan_directory('.')

    if not files_to_delete and not empty_dirs:
        print("No files found that should be deleted.")
        return

    print("\nFound the following files that should be deleted:")
    for file in files_to_delete:
        print(f"- {file}")
    
    if empty_dirs:
        print("\nThe following empty directories will be removed:")
        for directory in empty_dirs:
            print(f"- {directory}")

    print("\n" + "!"*80)
    print("WARNING: This operation will permanently delete the files listed above!")
    print("This action cannot be undone!")
    print("!"*80)

    if not auto_confirm:
        print("\nOperation cancelled. Run with -y flag to confirm deletion.")
        return

    deleted_files, deleted_dirs, errors = delete_files(files_to_delete, empty_dirs)

    print("\nOperation completed!")
    print(f"Successfully deleted {len(deleted_files)} files and {len(deleted_dirs)} directories.")
    
    if errors:
        print("\nThe following errors occurred:")
        for error in errors:
            print(f"- {error}")

def main():
    # 커맨드 라인 인자 확인
    auto_confirm = '-y' in sys.argv or '--yes' in sys.argv
    run_with_auto_input(auto_confirm)

if __name__ == "__main__":
    main()
