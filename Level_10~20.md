# Bandit Level 10 → Level 11

## Level Goal

The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

## Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

## Helpful Reading Material

- [Base64 on Wikipedia](https://en.wikipedia.org/wiki/Base64)

```sh
cat ./data.txt | base64 -d
```

The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

# Bandit Level 11 → Level 12

## Level Goal

The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

## Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

## Helpful Reading Material

- [Rot13 on Wikipedia](https://en.wikipedia.org/wiki/ROT13)

![[Pasted image 20241017121930.png]]
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

# Bandit Level 12 → Level 13

## Level Goal

The password for the next level is stored in the file **data.txt**, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work. Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

> [!번역]
> 다음 레벨의 비밀번호는 반복적으로 압축된 파일의 헥스덤프인 data.txt 파일에 저장됩니다. 이 레벨의 경우 /tmp 아래에 작업할 수 있는 디렉토리를 만드는 것이 유용할 수 있습니다. 디렉토리 이름을 추측하기 어려운 mkdir를 사용합니다. 또는 "mktemp -d" 명령을 사용하는 것이 좋습니다. 그런 다음 cp를 사용하여 데이터 파일을 복사하고 mv를 사용하여 이름을 변경합니다(매뉴얼 페이지 읽기!)
## Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file

## Helpful Reading Material

- [Hex dump on Wikipedia](https://en.wikipedia.org/wiki/Hex_dump)

- 압축 확장자가 명확하지 않을 때 tar tool은 자동으로 압축 형태를 감지해 동작한다.
``` sh
tar -xf 파일명
```
