# ๐git branch

- Git Flow(ํ์์์์ ํ๋ฆ)์์ branch๋ฅผ ์ด์ฉํจ

- ์ค๊ธฐ(master, ํ ์์ ์์์ ๋ฒ์  ) ํ๋๋ฅผ ๋๊ณ  ๊ฐ์ง๋ฅผ ์ณ์ ๊ฐ์ ๊ฐ๋ฐ
- merge๋ก ํตํฉ 

- HEAD ํ์ฌ ์๋ ๋ธ๋์น

## ๐branch commands

- git branch name  ๋ธ๋์น ์์ฑ
-  git branch ์๊ฒจ๋ ๋ธ๋์น ๋ชฉ๋ก
- git checkout name ํด๋น ๋ธ๋์น๋ก ์ด๋
- git checkout -b name ํด๋น ๋ธ๋์น ์์ฑ ๋ฐ ์ด๋
- git branch -d name ํด๋น ๋ธ๋์น ์ญ์ 

----

## ๐ฆขbranch merge 

- fast forward
  - master์์ ์์ x ๊ทธ์  ์ถ๊ฐ๋จ
  - master์์ ๋ฐ๋ก git merge
- merge commit
  - ๋ค๋ฅธ ํ์ผ์ด ์์ ๋์ด ์๋ ์ํฉ
  - git merge ๊ฐ๋ฅ

- merge commit conflict
  - ๊ฐ์ ํ์ผ์ ๊ฐ์ ๊ณณ์ด branch๋ง๋ค ๋ค๋ฅด๊ฒ ๋์ด์์ ๊ฒฝ์ฐ ์ถฉ๋ ๋ฐ์
  - ํด๋น ํ์ผ ๋๋ฌ์ ํ์ธํ ๋ณ๊ฒฝ
  - git merge ๊ฐ๋ฅ

## ๐ฆํ์ ๋ชจ๋ธ

1. Feature Branch Workflow
   - shared repository model(์ ์ฅ์ ์์ ๊ถ o)
2. forking workflow
   - fork & pull model(์ ์ฅ์ ์์ ๊ถ x)

----

$ git restore -- staged ํ์ผ์ด๋ฆ.ํ์ฅ์

->  add๋ฅผ ์ค์๋ก ํ ํ์ผ๋ ๋ค์ ๋๋๋ฆฌ๊ธฐ ๊ฐ๋ฅ

$ git restore ํ์ผ์ด๋ฆ.ํ์ฅ์

-> ๋ณ๊ฒฝ์ฌํญ ๋ฒ๋ฆฌ๊ธฐ

