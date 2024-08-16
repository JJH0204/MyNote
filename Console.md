**콘솔(Console)**은 프론트엔드의 자바스크립트 코드에서 발생한 각종 메세지를 출력하고, 이용자가 입력한 자바스크립트 코드를 실행도 해주는 도구입니다.

자바스크립트로 웹 개발을 할 때, `console` 오브젝트에는 개발자 도구의 콘솔에 접근할 수 있는 함수가 정의되어 있습니다. 코드를 작성하면서 어떤 변수의 값을 중간에 출력해보고 싶다면, `console.log` 등을 유용하게 사용할 수 있습니다.

NodeJS의 console 오브젝트
```
> console
Console {
  log: [Function: bound consoleCall],
  debug: [Function: bound consoleCall],
  info: [Function: bound consoleCall],
  dirxml: [Function: bound consoleCall],
  warn: [Function: bound consoleCall],
  error: [Function: bound consoleCall],
  ...
  context: [Function: context],
  [Symbol(counts)]: Map {},
  [Symbol(kColorMode)]: 'auto' }
```

| 💡 단축키 |  |
| ---- | ---- |
| Windows/Linux | Ctrl + Shift + J |
| macOS | Option(**⌥**) +Cmd(**⌘**) + J |

콘솔을 사용하면 브라우저에서 자바스크립트를 실행하고 결과를 확인할 수 있습니다. 단축키로 콘솔을 열고, **아래 내용**을 콘솔에 입력해보세요.