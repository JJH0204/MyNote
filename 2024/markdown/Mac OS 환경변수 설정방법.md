환경 변수 확인

```
printenv
```

```
__CFBundleIdentifier=com.apple.Terminal

TMPDIR=/var/folders/h3/2rlty04j6qb4ctqgd1mfhks00000gn/T/

XPC_FLAGS=0x0

TERM=xterm-256color

SSH_AUTH_SOCK=/private/tmp/com.apple.launchd.e3uPH3pqDZ/Listeners

XPC_SERVICE_NAME=0

TERM_PROGRAM=Apple_Terminal

TERM_PROGRAM_VERSION=453

TERM_SESSION_ID=9212E694-878A-433B-9959-10122DF85E0E

SHELL=/bin/zsh

HOME=/Users/admin

LOGNAME=admin

USER=admin

PATH=/opt/anaconda3/bin:/opt/homebrew/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/opt/homebrew/bin:/opt/homebrew/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/share/dotnet:/Users/admin/.dotnet/tools:/Library/Apple/usr/bin:/Library/Frameworks/Mono.framework/Versions/Current/Commands:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin

SHLVL=1

PWD=/Users/admin

OLDPWD=/Users/admin

HOMEBREW_PREFIX=/opt/homebrew

HOMEBREW_CELLAR=/opt/homebrew/Cellar

HOMEBREW_REPOSITORY=/opt/homebrew

MANPATH=/opt/homebrew/share/man::

INFOPATH=/opt/homebrew/share/info:

LANG=ko_KR.UTF-8

_=/usr/bin/printenv
```

특정 환경 변수값 확인

```
echo $환경변수명
```

```
echo $PATH

/opt/anaconda3/bin:/opt/homebrew/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/opt/homebrew/bin:/opt/homebrew/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/share/dotnet:/Users/admin/.dotnet/tools:/Library/Apple/usr/bin:/Library/Frameworks/Mono.framework/Versions/Current/Commands:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin
```

새 환경 변수 설정
