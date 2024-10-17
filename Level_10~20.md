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
> 다음 레벨의 암호는 파일 데이터.txt에서 저장됩니다, 반복된 파일의 6헥타르프입니다.이 수준에서 작업을 수행할 수 있는 /time/ties에서 디렉토리를 생성할 수 있습니다.Mkdird를 사용하여 디렉토리 이름을 입력합니다.더 나은, 명령 "mp-d"를 사용합니다.그러면 CP를 사용하여 데이터 파일을 복사하고 변경할 수 있습니다.
## Commands you may need to solve this level

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file

## Helpful Reading Material

- [Hex dump on Wikipedia](https://en.wikipedia.org/wiki/Hex_dump)

