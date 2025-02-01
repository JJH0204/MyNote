import os
import shutil
import sys
from pathlib import Path

# stdout 인코딩을 UTF-8로 설정
sys.stdout.reconfigure(encoding='utf-8')

# 소스 디렉토리 경로
source_dirs = [
    "Excalidraw",
    "Spaces",
    "XML"
]

# 대상 디렉토리 경로
target_dirs = {
    "image": ["png", "jpg", "jpeg", "gif", "svg", "webp"],
    "markdown": ["md", "markdown"],
    "etc": []  # 기타 모든 확장자
}

def organize_files():
    # 현재 작업 디렉토리 경로 가져오기
    base_path = Path(os.path.dirname(os.path.abspath(__file__)))
    
    # 대상 디렉토리가 없으면 생성
    for target_dir in target_dirs.keys():
        target_path = base_path / target_dir
        target_path.mkdir(exist_ok=True)
    
    # 각 소스 디렉토리 처리
    for source_dir in source_dirs:
        source_path = base_path / source_dir
        if not source_path.exists():
            print(f"디렉토리를 찾을 수 없습니다: {source_dir}")
            continue
            
        # 디렉토리 순회
        for root, _, files in os.walk(source_path):
            for file in files:
                file_path = Path(root) / file
                extension = file_path.suffix.lower().lstrip('.')
                
                # 파일 분류
                target_dir = "etc"  # 기본값
                for dir_name, extensions in target_dirs.items():
                    if extension in extensions:
                        target_dir = dir_name
                        break
                
                # 파일 이동
                target_path = base_path / target_dir / file
                
                # 중복 파일 처리
                if target_path.exists():
                    base_name = target_path.stem
                    extension = target_path.suffix
                    counter = 1
                    while target_path.exists():
                        new_name = f"{base_name}_{counter}{extension}"
                        target_path = target_path.parent / new_name
                        counter += 1
                
                try:
                    shutil.move(str(file_path), str(target_path))
                    print(f"이동됨: {file} -> {target_dir}")
                except Exception as e:
                    print(f"오류 발생: {file} - {str(e)}")

if __name__ == "__main__":
    organize_files()