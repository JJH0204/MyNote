피연산자를 2진수로 표현하여 비트(bit) 단위로 연산하는 것을 비트 연산이라고 한다.
비트 단위로 논리 연산을 수행하거나, 비트를 특정 값만큼 이동하는 시프트(shift) 연산을 수행

# 논리 연산
---

|**논리 연산자**|**설명**|
|---|---|
|x **\|** y|둘 중 하나라도 참이면 결과는 참입니다. (OR)|
|x **&&** y|둘 다 참이면 결과는 참입니다. (AND)|
|**!**x|참이면 결과는 거짓, 거짓이면 결과는 참입니다. (NOT)|


# 비트 연산자
---

|**비트 연산자**|**설명**|
|---|---|
|x **\|** y|두 비트 중 하나라도 1이면 결과는 1입니다. (OR)|
|x **&** y|두 비트 모두 1이면 결과는 1입니다. (AND)|
|x **^** y|두 비트가 같으면 결과는 0, 다르면 결과는 1입니다. (XOR)|
|**~**x|비트가 0이면 결과는 1, 1이면 결과는 0으로 모든 비트를 반전시킵니다. (NOT)|

# 시프트 연산자
---

|**시프트 연산자**|**설명**|
|---|---|
|x **<<** n|비트를 n만큼 왼쪽으로 이동합니다.<br><br>오른쪽 빈 칸은 모두 0으로 채웁니다.<br><br>== **x * 2n**|
|x **>>** n<br><br>(산술 시프트)|비트를 n만큼 오른쪽으로 이동합니다.<br><br>왼쪽 빈 칸은 가장 왼쪽에 있던 비트(MSB)와 동일한 비트 값으로 채웁니다.<br><br>(양수는 양수, 음수는 음수로 부호가 유지됩니다.)<br><br>== **x / 2n**|
|x **>>>** n<br><br>(논리 시프트)|비트를 n만큼 오른쪽으로 이동합니다.<br><br>왼쪽 빈 칸은 모두 0으로 채웁니다.<br><br>(음수는 부호가 유지되지 않습니다.)|

# 비트 연산자 활용
---
## AND (&) 연산을 활용한 비트 마스킹

어떤 데이터가 존재할 때, 특정 위치의 비트만 표시하거나 가리는 연산을 **비트 마스킹(Bit Masking)** 이라고 부릅니다. 앞서 살펴보았듯이 AND 연산은 대응하는 비트가 모두 1이어야 1이 됩니다. 대응하는 비트 중에 하나라도 0이면 0이 됩니다. 이러한 AND 연산의 특징을 활용한 비트 마스킹의 예시를 살펴보겠습니다.

예를 들어 2바이트 크기의 데이터인 0xABCD가 존재할 때, AND 연산을 활용하면 상위 8비트에 해당하는 0xAB는 없애고, 하위 8비트에 해당하는 0xCD만 남길 수 있습니다. 이를 위해서 다음과 같이 0xABCD에 0x00FF를 AND 연산하면 됩니다.

![](https://dreamhack-lecture.s3.amazonaws.com/media/5d4d3227d55431ea41ed061c6c185b06ce660e0789da449bb70dd3cd679264bb.png)

16진수 F(1111)는 특정 값과 AND 연산하면 기존 값에서 비트 값이 1이면 결과가 1, 0이면 결과가 0이기 때문에 기존 값과 동일한 결과가 나옵니다. 반대로 0(0000)은 특정 값과 AND 연산하면 모든 비트가 0이 되어 결과는 0입니다. 따라서 상위 1바이트인 0xAB는 모두 0이되고, 하위 1바이트인 0xCD는 1인 비트만 남아 결국 0xCD가 남습니다.

## AND (&) 연산과 시프트 연산을 활용하여 특정 비트/바이트 가져오기

또한 AND 연산과 시프트 연산을 함께 활용하면 특정 위치의 비트를 가져올 수 있습니다. 다음은 32비트 즉, 4바이트 크기의 데이터인 0x12345678 (0001 0010 0011 0100 0101 0110 0111 1000) 에서 특정 비트만 가져오는 예시입니다.

- 하위 1 바이트만 가져오기 : 0x000000FF와 AND 연산합니다.
    
0x12345678 & 0x000000FF = 0x00000078 (0000 0000 0000 0000 0000 0000 0111 1000)
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkiIGhlaWdodD0iMzQiIHZpZXdCb3g9IjAgMCAyOSAzNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTIxIDAuNUgzQzEuMzUgMC41IDAgMS44NSAwIDMuNVYyNC41SDNWMy41SDIxVjAuNVpNMjUuNSA2LjVIOUM3LjM1IDYuNSA2IDcuODUgNiA5LjVWMzAuNUM2IDMyLjE1IDcuMzUgMzMuNSA5IDMzLjVIMjUuNUMyNy4xNSAzMy41IDI4LjUgMzIuMTUgMjguNSAzMC41VjkuNUMyOC41IDcuODUgMjcuMTUgNi41IDI1LjUgNi41Wk0yNS41IDMwLjVIOVY5LjVIMjUuNVYzMC41WiIgZmlsbD0iIzFBMUExQiIvPgo8L3N2Zz4K)

- 상위 1 바이트만 가져오기 : 24번 우측으로 논리 시프트를 수행합니다. 또는, 24번 우측으로 산술 시프트한 후 0x000000FF와 AND연산 합니다.
    
0x12345678 >>> 24 = 0x00000012 (0000 0000 0000 0000 0000 0000 0001 0010)
0x12345678 >> 24 & 0x000000FF = 0x00000012 (0000 0000 0000 0000 0000 0000 0001 0010)
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkiIGhlaWdodD0iMzQiIHZpZXdCb3g9IjAgMCAyOSAzNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTIxIDAuNUgzQzEuMzUgMC41IDAgMS44NSAwIDMuNVYyNC41SDNWMy41SDIxVjAuNVpNMjUuNSA2LjVIOUM3LjM1IDYuNSA2IDcuODUgNiA5LjVWMzAuNUM2IDMyLjE1IDcuMzUgMzMuNSA5IDMzLjVIMjUuNUMyNy4xNSAzMy41IDI4LjUgMzIuMTUgMjguNSAzMC41VjkuNUMyOC41IDcuODUgMjcuMTUgNi41IDI1LjUgNi41Wk0yNS41IDMwLjVIOVY5LjVIMjUuNVYzMC41WiIgZmlsbD0iIzFBMUExQiIvPgo8L3N2Zz4K)

- 상위에서 두 번째 바이트 가져오기: 16번 우측으로 시프트 후 0x000000FF와 AND 연산합니다.
    
0x12345678 >> 16 & 0x000000FF = 0x00000034 (0000 0000 0000 0000 0000 0000 0011 0100)
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkiIGhlaWdodD0iMzQiIHZpZXdCb3g9IjAgMCAyOSAzNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTIxIDAuNUgzQzEuMzUgMC41IDAgMS44NSAwIDMuNVYyNC41SDNWMy41SDIxVjAuNVpNMjUuNSA2LjVIOUM3LjM1IDYuNSA2IDcuODUgNiA5LjVWMzAuNUM2IDMyLjE1IDcuMzUgMzMuNSA5IDMzLjVIMjUuNUMyNy4xNSAzMy41IDI4LjUgMzIuMTUgMjguNSAzMC41VjkuNUMyOC41IDcuODUgMjcuMTUgNi41IDI1LjUgNi41Wk0yNS41IDMwLjVIOVY5LjVIMjUuNVYzMC41WiIgZmlsbD0iIzFBMUExQiIvPgo8L3N2Zz4K)

- 하위 1바이트의 상위 4비트 가져오기 : 4번 우측으로 시프트한 후 0x0000000F와 AND 연산합니다
    
0x12345678 >> 4 & 0x0000000F = 0x00000007 (0000 0000 0000 0000 0000 0000 0000 0111)
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjkiIGhlaWdodD0iMzQiIHZpZXdCb3g9IjAgMCAyOSAzNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTIxIDAuNUgzQzEuMzUgMC41IDAgMS44NSAwIDMuNVYyNC41SDNWMy41SDIxVjAuNVpNMjUuNSA2LjVIOUM3LjM1IDYuNSA2IDcuODUgNiA5LjVWMzAuNUM2IDMyLjE1IDcuMzUgMzMuNSA5IDMzLjVIMjUuNUMyNy4xNSAzMy41IDI4LjUgMzIuMTUgMjguNSAzMC41VjkuNUMyOC41IDcuODUgMjcuMTUgNi41IDI1LjUgNi41Wk0yNS41IDMwLjVIOVY5LjVIMjUuNVYzMC41WiIgZmlsbD0iIzFBMUExQiIvPgo8L3N2Zz4K)

## XOR 연산을 활용한 비교와 암호화

XOR 연산은 비트 값이 같으면 0을 반환합니다. 즉, 자기 자신과 XOR 연산하면 결과는 0입니다. 두 변수에 저장된 값끼리 XOR 연산하여 결과가 0인지 확인하면 두 값이 같은지 비교할 수 있습니다.

더 나아가서, 같은 값에 어떤 값을 2번 XOR 하면 원래의 값과 동일해진다는 특성을 이용할 수도 있습니다. 예를 들어 `x ^ y`를 수행한 결과가 `z`일 때, `z ^ y = x ^ y ^ y = x` 입니다. 이러한 특성을 기반으로, `y`를 key로 설정하면 간단한 암호화, 복호화가 가능합니다.

XOR 연산은 이러한 특성에 의해 어셈블리 코드나 암호 기법에 자주 등장하니, 잘 기억해 두면 좋습니다.

## 시프트 연산을 활용한 곱셈, 나눗셈

앞서 시프트 연산은 2n을 곱하거나 나눈 결과와 동일하다는 것을 보았습니다. 따라서 곱셈이나 나눗셈 연산자 대신 시프트 연산자를 사용하여 간단한 산술 연산을 수행할 수 있습니다. 시프트 연산자를 사용하면 비트 레벨에서 연산을 하므로 더 효율적이고 속도가 빠릅니다.