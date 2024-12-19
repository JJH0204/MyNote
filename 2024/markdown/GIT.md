---
sticker: lucide//github
---
- [깃 과 옵시디언 연동 방법](https://alive-wong.tistory.com/65)
- [깃 저장소 병합 방법](https://velog.io/@jisuuuu/Git-Repository%EB%93%A4-%ED%95%98%EB%82%98%EB%A1%9C-%ED%95%A9%EC%B9%98%EA%B8%B0)
- [커밋 버전 이전으로 되돌리는 방법](https://medium.com/@kwoncharles/git-%EC%9D%B4%EC%A0%84-commit%EC%9C%BC%EB%A1%9C-%EB%8F%8C%EC%95%84%EA%B0%80%EA%B8%B0-cf6caed43ed5) 
- https://ittrue.tistory.com/91 깃 클론
## 사용하지 않는 PC에서 git연결 해제하기
Git 사용 후 현재 PC에서 계정 사용을 중지하려면 몇 가지 단계를 따라야 해. 주로 Git의 글로벌 설정을 삭제하거나 변경하는 방법으로 진행해. 다음은 그 방법들이야:

1. **Git 글로벌 설정에서 사용자 정보 삭제하기**:
    
    bash
    
    코드 복사
    
    `git config --global --unset user.name git config --global --unset user.email`
    
    이렇게 하면 글로벌 설정에서 사용자 이름과 이메일이 제거돼.
    
2. **SSH 키 삭제하기**: 만약 SSH 키를 사용하고 있다면, 해당 키를 삭제하거나 비활성화해야 해. 보통 SSH 키는 `~/.ssh` 디렉토리에 있어. 여기서 `id_rsa`, `id_rsa.pub` 같은 파일을 삭제하거나 백업해두면 돼.
    
    bash
    
    코드 복사
    
    `rm ~/.ssh/id_rsa rm ~/.ssh/id_rsa.pub`
    
3. **캐시된 자격 증명 삭제하기**: 만약 Git 자격 증명 헬퍼를 사용하고 있다면, 캐시된 자격 증명을 삭제할 필요가 있어.
    
    bash
    
    코드 복사
    
    `git credential-cache exit`
    
4. **Windows의 경우 자격 증명 관리자 사용**: 만약 Windows에서 Git을 사용하고 있다면, "자격 증명 관리자"에서 Git 자격 증명을 찾아 삭제할 수 있어.
    
    - **제어판 > 사용자 계정 > 자격 증명 관리자**로 이동해.
    - "Windows 자격 증명" 또는 "일반 자격 증명"에서 Git 관련 항목을 찾아 삭제해.

- [git_pull_error](https://goddaehee.tistory.com/253)
- [git_stash_clear](https://iiii.tistory.com/156)
- [git_commant_add](https://hygge-wavy.tistory.com/m/94)
- [git_team_add](https://velog.io/@gmlstjq123/%EB%82%B4-Github-Repository%EB%A1%9C-%ED%8C%80%EC%9B%90-%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0)
- [git_web](https://brunch.co.kr/@everiwon/42)
- [GIT 간단 사용법](How2UseGit.md)
## git_LF_commit
---
- https://guide.ncloud-docs.com/docs/sourcecommit-use-lfs
- https://sbjjsurfing.tistory.com/110
