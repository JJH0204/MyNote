# [nmap](https://nmap.org/)
---
0-1023(잘 알려진 포트):
1024-49151: 예약된 포트
49152-65535: 사설 포트

## TCP Scan: `-sT` 
---
`-sS`: SYN 플래그
- kali > SYN(80) > earth -> kali < SYN + ACK(80) < earth()
  : TCP 응답에 따라 포트가 활성화 되어 있는지 확인한다.
  : 포트에 반응이 없다면 활성화 되지 않았다는 의미
`-sN`: Null 플래그
- 아무 플래그가 없이 패킷 전달
`-sF`: FIN 플래그
`-sX`: xMas Scan
- 다양한 종류의 플래그를 패킷 전달함 한번에 전달하는 방식
`-xM`: 둘 이상 플래그를 조합해서 패킷에 포함
`-sA`: ACK 플래그
`-sW`: windows scan(windows size)
- 웹 사이트의 정보를 담은 windows의 정보를 알아내는 플래그
`-sL`: idle
- 좀비 시스템에서 사용하는 플래그

## UDP Scan: `-sU`
---
`-F`: Fast
`-r`: 순차적

## Timing Option
---
스캐닝 대상으로 하여금 공격을 위한 스캐닝인지 알 수 없도록 딜레이 시간을 설정하는 방법
0 : 5분 마다
1 : 15초 마다
2 : 0.4초 마다
3 : 다중 대상에 다중 탐색(기본 옵션)
4 : 정해진 시간(5분 동안) 만큼
5 : 75초만 

## NSE(Nmap Script Engine)
---
- 인증, 기본(-sC, -A), 발견, 익스플로잇, DoSS, 침투(), 취약점 점검 등
- https://nmap.org/ 에서 새로운 엔진을 설치 받을 수 있다.
- `-vuln-` : 취약점 점검 스크립트

### 파일 경로
---
`/usr/share/nmap`: nmap 설정 파일 경로
`./scripts`: 스크립트 엔진 파일 경로

#### http-wordpress-brute.nse
---
```
cat /usr/share/nmap/scripts/http-wordpress-brute.nse
local brute = require "brute"
local creds = require "creds"
local http = require "http"
local shortport = require "shortport"
local stdnse = require "stdnse"

description = [[
performs brute force password auditing against Wordpress CMS/blog installations.

This script uses the unpwdb and brute libraries to perform password guessing. Any successful guesses are
stored using the credentials library.

Wordpress default uri and form names:
* Default uri:<code>wp-login.php</code>
* Default uservar: <code>log</code>
* Default passvar: <code>pwd</code>
]]

---
-- @usage
-- nmap -sV --script http-wordpress-brute <target>
-- nmap -sV --script http-wordpress-brute
--   --script-args 'userdb=users.txt,passdb=passwds.txt,http-wordpress-brute.hostname=domain.com,
--                  http-wordpress-brute.threads=3,brute.firstonly=true' <target>
--
-- @output
-- PORT     STATE SERVICE REASON
-- 80/tcp   open  http    syn-ack
-- | http-wordpress-brute:
-- |   Accounts
-- |     0xdeadb33f:god => Login correct
-- |   Statistics
-- |_    Perfomed 103 guesses in 17 seconds, average tps: 6
--
-- @args http-wordpress-brute.uri points to the file 'wp-login.php'. Default /wp-login.php
-- @args http-wordpress-brute.hostname sets the host header in case of virtual
--       hosting
-- @args http-wordpress-brute.uservar sets the http-variable name that holds the
--                                    username used to authenticate. Default: log
-- @args http-wordpress-brute.passvar sets the http-variable name that holds the
--                                    password used to authenticate. Default: pwd
-- @args http-wordpress-brute.threads sets the number of threads. Default: 3
--
-- Other useful arguments when using this script are:
-- * http.useragent = String - User Agent used in HTTP requests
-- * brute.firstonly = Boolean - Stop attack when the first credentials are found
-- * brute.mode = user/creds/pass - Username password iterator
-- * passdb = String - Path to password list
-- * userdb = String - Path to user list
--
-- @see http-form-brute.nse

author = "Paulino Calderon <calderon@websec.mx>"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"intrusive", "brute"}


portrule = shortport.http

local DEFAULT_WP_URI = "/wp-login.php"
local DEFAULT_WP_USERVAR = "log"
local DEFAULT_WP_PASSVAR = "pwd"
local DEFAULT_THREAD_NUM = 3

---
--This class implements the Driver class from the Brute library
---
Driver = {
  new = function(self, host, port, options)
    local o = {}
    setmetatable(o, self)
    self.__index = self
    o.hostname = stdnse.get_script_args('http-wordpress-brute.hostname')
    o.http_options = {
      no_cache = true,
      header = {
        -- nil just means not set, so default http.lua behavior
        Host = stdnse.get_script_args('http-wordpress-brute.hostname')
      }
    }
    o.host = host
    o.port = port
    o.uri = stdnse.get_script_args('http-wordpress-brute.uri') or DEFAULT_WP_URI
    o.options = options
    return o
  end,

  connect = function( self )
    -- This will cause problems, as there is no way for us to "reserve"
    -- a socket. We may end up here early with a set of credentials
    -- which won't be guessed until the end, due to socket exhaustion.
    return true
  end,

  login = function( self, username, password )
    stdnse.debug2("HTTP POST %s%s", self.http_options.header.Host or stdnse.get_hostname(self.host), self.uri)
    local response = http.post( self.host, self.port, self.uri, self.http_options,
      nil, { [self.options.uservar] = username, [self.options.passvar] = password } )
    -- This redirect is taking us to /wp-admin
    if response.status == 302 then
      return true, creds.Account:new( username, password, creds.State.VALID)
    end

    return false, brute.Error:new( "Incorrect password" )
  end,

  disconnect = function( self )
    return true
  end,

  check = function( self )
    local response = http.get( self.host, self.port, self.uri, self.http_options )
    stdnse.debug1("HTTP GET %s%s", self.http_options.header.Host or stdnse.get_hostname(self.host), self.uri)
    -- Check if password field is there
    if ( response.status == 200 and response.body:match('type=[\'"]password[\'"]')) then
      stdnse.debug1("Initial check passed. Launching brute force attack")
      return true
    else
      stdnse.debug1("Initial check failed. Password field wasn't found")
    end

    return false
  end

}
---
--MAIN
---
action = function( host, port )
  local status, result, engine
  local uservar = stdnse.get_script_args('http-wordpress-brute.uservar') or DEFAULT_WP_USERVAR
  local passvar = stdnse.get_script_args('http-wordpress-brute.passvar') or DEFAULT_WP_PASSVAR
  local thread_num = tonumber(stdnse.get_script_args("http-wordpress-brute.threads")) or DEFAULT_THREAD_NUM

  engine = brute.Engine:new( Driver, host, port, { uservar = uservar, passvar = passvar } )
  engine:setMaxThreads(thread_num)
  engine.options.script_name = SCRIPT_NAME
  status, result = engine:start()

  return result
end
```
- wordpress 대상으로 무작위 스캐닝을 진행하는 엔진
- 설명 / 사용방법 / 예시 결과를 알 수 있다.

## 방화벽/IDS 등 장비 우회 옵션
---
-f: 패킷을 세분화
--source-ports, -g "출발 ip": 출발 ip 변조
--data-length "데이터 사이즈": 패킷 길이 조작
--scan-delay "시간":
-D(가짜 ip 생성)

