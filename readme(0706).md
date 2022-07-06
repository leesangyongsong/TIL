# 📘Git
- Git은 분산버전관리시스템으로 코드의 버전을 관리하는 도구
- 2005년 리눅스 커널을 위한 도구로 리누스 토르발스가 개발
- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율
    1. 작업을 하고
    2. 변경된 파일을 모아(add)
    3. 버전으로 남긴다.(commit)
- Git은 파일을 modified, staged, committed로 관리
    - modified: 파일이 수정된 상태(add 명령어를 통하여 staging area로)
    - staged: 수정한 파일을 곧 커밋할 것이라고 표시한 상태(commit 명령어로 저장소)
    - committed: 커밋이 된 상태

## ✔ Git 기본 명령어
- log($ git log)
    - 현재 저장소에 기록된 커밋을 조회할 수 있음
        - $ git log -1
        - $ git log --oneline
        - $ git log -2--oneline
- status($ git status)
    - Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용
        - 파일의 상태를 알 수 있음
            - Untracked files
            - Changes not staged for commit
            - Changes th be commiteed
        - Nothing to commit, working tree clean
    - Status로 확인할 수 있는 파일의 상태
        - Tracked : 이전부터 버전으로 관리되고 있는 파일
            - Unmodified: git status에 나타나지 않음
            - Modified: Changes not staged for commit
            - Staged: Changes to be committed
        - Untracked: 버전으로 관리된 적 없는 파일(파일을 새로 만든 경우)
- init($ git init)
    - 로컬 저장소 생성
- add($ git add <파일명>)
    - 특정 파일/폴더의 변경사항 추가
- commit($ git commit -m '<커밋메시지>')
    - 커밋(버전 기록)
- 원격저장소 경로 설정($ git remote add origin <원격저장소url>)
    - 최초 1회만 설정하면 된다.
- pull($ git pull)
    - 다른 사람이 원격저장소에 올려놓은 수정내역 내 로컬에 다운받기
- push($ git push)
    - 내가 작업한 수정내역 원격저장소에 공유하기
    