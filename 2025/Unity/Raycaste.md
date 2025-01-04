~~~ cs
private void SelectTargetWithRaycast()

{

  Ray ray = mainCamera.ScreenPointToRay(Input.mousePosition);
  
  RaycastHit hit;
  
  float maxRayDistance = 100f; // 레이캐스트 최대 거리를 충분히 크게 설정
  
    
  
  // 디버그 레이 시각화 (Scene 뷰에서 확인 가능)
  
  if (showDebugRay)
  
  {
  
    Debug.DrawRay(ray.origin, ray.direction * maxRayDistance, Color.red, 1f);
    
    Debug.Log($"Raycast fired from: {ray.origin}, direction: {ray.direction}");
  
  }
  
    
  
  if (Physics.Raycast(ray, out hit, maxRayDistance, enemyLayer))
  
  {
  
    Debug.Log($"Raycast hit something: {hit.collider.name} at position {hit.point}");
  
    if (hit.collider.CompareTag("Enemy"))
    
    {
    
      float distance = Vector3.Distance(transform.position, hit.transform.position);
      
      currentTarget = hit.collider.gameObject;
      
      Debug.Log($"Hit object layer: {LayerMask.LayerToName(hit.collider.gameObject.layer)}");
      
      Debug.Log($"Selected target: {currentTarget.name} at distance {distance:F2}m" + (distance <= maxAttackDistance ? " (In attack range)" : " (Out of attack range)"));
    
    }
    
    else
    
    {
    
      Debug.Log($"Hit object does not have Enemy tag. Tag: {hit.collider.tag}");
    
    }
  
  }
  
  else
  
  {
  
    Debug.Log($"Raycast missed. Layer mask: {LayerMask.LayerToName(enemyLayer)}");
    
    if (currentTarget != null)
    
    {
    
      Debug.Log($"Deselected target: {currentTarget.name}");
      
      currentTarget = null;
    
    }
  
  }

}
~~~
