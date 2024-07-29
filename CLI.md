# CLI

- GUI (Graphic User Interface)
  - GUI -> 그래픽으로 유저와 컴퓨터가 상호작용하는 접점
- CLI (Command Line Interface)
  - command line을 통해서 유저와 컴퓨터가 상호작용하는 접점
  - 터미널을 통해서!

> 왜? CLI를 써야 하나요?
- 새폴더 생성할 때,
  - GUI : 마우스 우클릭 -> 새로 만들기 -> 폴더 -> 'new'폴더 생성
  - CLI : 터미널 켜서, 'mkdir new' (make directory new)

# 경로

- 현재 내가 위치한 곳! 그 주소

1. 루트 디렉토리 (/)
   - 모든 파일과 폴더를 담고 있는 최상위의 폴더
   - C 드라이브!
2. 홈 디렉토리 (~)
   - 현재 로그인 된 사용자의 홈 폴더
   - C:/Users/alex
  
# 경로의 두 가지 종류
1. 절대경로 : 루트 디렉토리부터 목적지점을 모두 표현한 경로
2. 상대경로 : 현재 작업 디렉토리(working directory)를 기준으로 계산된 경로
    - . : 현재 작업하고 있는 폴더
    - .. : 현재 작업 폴더의 부모를 의미

pwd(print working directory)

# 터미널 명령어
1. 'touch' : 파일을 생성하는 명령어 (뛰어쓰기로 구분하여 파일을 한번에 여러개 생성 가능)
2. 'mkdir' : make directory의 약자 -> 폴더를 만들어 줍니다.
3. 'ls' : list segments의 약자 -> 현재 작업중인 디렉토리의 목록을 보여줍니다. 
   - 'ls -a' : 숨겨진 모든 파일과 폴더까지 볼 수 있는 옵션
4. 'mv' : move의 약자 -> 이동시킨다. 파일을 폴더내로 이동
이동 / 해당하는 폴더가 없는 경우? 파일명을 바꾸어 낸다
  => 파일을 이동시킨다. / 이름을 변경한다.
1. 'cd' : change directory의 약자 -> 현재의 위치를 변경합니다.
2. 'pwd' : print working directory -> 현재의 나의 위치를 출력
3. 'rm' : remove의 약자 -> 폴더/파일을 지우는 명령어 (완전삭제, 주의!) rm -r 22(폴더삭제) rm *.txt