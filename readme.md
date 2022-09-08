# 작업환경 구성

1. Anaconda 설치

- https://www.anaconda.com 에 접속하여 현재 사용중인 os 에 맞춰서 프로그램 설치
  - 다음다음 누르시면 문제없이 설치가 끝납니다.
  - 윈도우의 경우 환경변수를 추가하는것도 좋지만 그보다는 `anaconda shell` 을 사용하여 작업하시는걸 추천드립니다.

2.  가상환경 구성(안해도 되지만 패키지를 이것저것 막 깔다면 컴터가 맛이
    갈수도 있어서요...)

    #### 1. os 가 window 라면 anaconda shell 을 실행하시고 mac 이라면 터미널을 실행해주세요.

    #### 2. 아래 명령어들을 순서대로 실행해주세요

        conda create --name mecab-env python=3.8 -y
        conda activate mecab-env
        pip install -r requirements.txt

3.  스크립트 실행
    #### ※ 크롤링한 결과를 mecab 라이브러리로 품사나 조사 등은 제거하고 명사면 count 를 계산해서 tsv 로 떨궈주는 스크립트입니다.(mecab 에서 명사가 아닌데 명사라고 틀린결과를 리턴해줄수는 있어용...ㅠㅠ)
    #### 1.크롤링을 진행하고 크롤링된 결과파일을 별도로 읽어서 처리
        python calc_words.py --with-crawling
    #### 2.크롤링은 안하고 결과파일만 읽어서 단어 count 확인
        python calc_words.py --result-file result.tsv
