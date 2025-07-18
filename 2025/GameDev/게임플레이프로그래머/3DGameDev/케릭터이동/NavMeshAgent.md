---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
CharacterController 와 함께 NavMeshAgent를 사용하면 마우스 클릭으로 캐릭터 제어가 가능하도록 만들 수 있다. ^y0DbG3rF

NavMesh 기능은 Unity에서 제공하는 AI 기능으로 사용하기전 패키지를 설치해야 한다. ^NU00u4aS

설치하면 아래와 같이 사용가능하다 ^7Iyrvcxt

NavMeshAgent 의 설정 ^qkDPz0Uf

??? ^8Kr6stAe

NavMesh를 생성할 대상설정 ^tP3Gp9mz

생성할 NavMesh의 Bake 시에 적용할 설정을 조절 할 수 있다. ^hYDhCKY6

Bake 버튼으로 NavMesh를 생성할 수 있다. ^RZXc2Afn

private void Awake()
{
    characterController = GetComponent<CharacterController>();
    navMeshAgent = GetComponent<NavMeshAgent>();
    navMeshAgent.updatePosition = false;
    navMeshAgent.updateRotation = true;
    
    cam = Camera.main;
}

private void Update()
{
    if (Input.GetMouseButton(0))
    {
        // 카메라 피킹으로 이동할 위치 계산
        var ray = cam.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;
        if (Physics.Raycast(ray, out hit, 100f, groundLayerMask))
        {
            // NavMeshAgent를 사용하여 이동
            navMeshAgent.SetDestination(hit.point);
        }
    }

    if (navMeshAgent.remainingDistance > navMeshAgent.stoppingDistance)
        characterController.Move(navMeshAgent.velocity * Time.deltaTime);
    else
        characterController.Move(Vector3.zero);
}

private void LateUpdate()
{
    transform.position = navMeshAgent.nextPosition;
} ^IQu2OSvS

초기 값 설정 ^34CxKps6

마우스 좌 클릭 입력 확인 ^MgzhBGAY

마우스 입력이 있었던 위치를 Ray를 이용해 스크린 좌표에서 월드 좌표로 변환
변환 과정에서 RayCast를 활용해 지면과 충돌했는지 검사 ^YpXMgGyM

마우스로 클릭한 지점을 목적지로 NavMesh 설정 ^xHSEiPS4

목적지로 이동 ^pj4PHNPK

목적지 도착여부 확인 ^SwVAx3qJ

이동 정지 ^XzlfOIyB

캐릭터의 이동 위치를 마지막에 보정 ^D3yFN60o

이거 때문에 Scene 실행하면 캐릭터가 바닥에 박힌체로 시작하는 것 같은데 플레이어의 초기 위치를 따로 설정해 줘야겠다. ^j6mNwpJF

바닥에 붙여 놓은 체로 LastUpdate() 메서드는 주석 처리했다. ^t5jJgYwC

## Embedded Files
3db0469195aa6ce44dbc363565729a444979e1e6: [[스크린샷 2025-06-15 오후 9.10.37.png]]

b97b156cd83c2a18308760fcffa158a42c8c3b3c: [[스크린샷 2025-06-15 오후 9.12.31.png]]

4e0f350c8eb242fb54f8bd8ce0391d575e638e0a: [[스크린샷 2025-06-15 오후 9.23.49.png]]

%%
## Drawing
```compressed-json
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

AD0EAA9CAA==
```
%%