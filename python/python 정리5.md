# 에러/예외 처리

## 문법에러=Syntax Error

EoL(end of line)

Eof(end of file)

Invalid syntax

assign to literal

## 예외

ZeroDivisonError

NameError

TypeError

ValueError

IndexError

KeyError

ModuleNotFoundError

importError

indentationError

KeyboardInterrupt

## 예외 처리

try:오류 발생 가능성 있는 코드를 적어둠
예외 x면 except실행 x
except:예외가 발생하면 실행됨
적절한 조치용

else:try문에서 예외가 발생하지 않으면 실행함

finally: 예외발생과 상관x 항상 실행

raise를 통해서 예외의 강제적 발생 가능