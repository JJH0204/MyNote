log를 보기 쉽게 보고서로 작성하고 관리자의 이메일로 전송하는 서비스

```
dnf install -y logwatch
```

> [!ls /etc/logwatch]
> conf(설정파일)  scripts(관련 스크립트)

- cat /etc/logwatch/conf/logwatch.conf
```
# Local configuration options go here (defaults are in /usr/share/logwatch/default.conf/logwatch.conf)
```

- cat /usr/share/logwatch/default.conf/logwatch.conf
```
########################################################
# This was written and is maintained by:
#    Kirk Bauer <kirk@kaybee.org>
#
# Please send all comments, suggestions, bug reports,
#    etc, to kirk@kaybee.org.
#
########################################################

(생략)
#Output/Format Options
#By default Logwatch will print to stdout in text with no encoding.
#To make email Default set Output = mail to save to file set Output = file
Output = stdout
#To make Html the default formatting Format = html
Format = text # 출력 형태
#To make Base64 [aka uuencode] Encode = base64
Encode = none # 암호화 여부

# Input Encoding
# Logwatch assumes that the input is in UTF-8 encoding.  Defining CharEncoding
# will use iconv to convert text to the UTF-8 encoding.  Set CharEncoding
# to an empty string to use the default current locale.  If set to a valid
# encoding, the input characters are converted to UTF-8, discarding any
# illegal characters.  Valid encodings are as used by the iconv program,
# and `iconv -l` lists valid character set encodings.
# Setting CharEncoding to UTF-8 simply discards illegal UTF-8 characters.
#CharEncoding = ""

# Default person to mail reports to.  Can be a local account or a
# complete email address.  Variable Output should be set to mail, or
# --output mail should be passed on command line to enable mail feature.
MailTo = root # (중요) 시스템 관리자의 메일 주소 입력

(생략)

# The default detail level for the report.
# This can either be Low, Med, High or a number.
# Low = 0
# Med = 5
# High = 10
Detail = Low # log 출력의 상세함 정도 (중요)
(생략)

```

```
logwatch --output stdout


 ################### Logwatch 7.5.5 (01/22/21) ####################
        Processing Initiated: Fri Sep 20 16:29:54 2024
        Date Range Processed: yesterday
                              ( 2024-Sep-19 )
                              Period is day.
        Detail Level of Output: 10
        Type of Output/Format: stdout / text
        Logfiles for Host: Linux1
 ##################################################################

 --------------------- Disk Space Begin ------------------------

 Filesystem           Size  Used Avail Use% Mounted on
 /dev/mapper/rl-root   17G  2.1G   15G  13% /
 /dev/sda1            960M  404M  557M  43% /boot


 ---------------------- Disk Space End -------------------------


 ###################### Logwatch End #########################


```