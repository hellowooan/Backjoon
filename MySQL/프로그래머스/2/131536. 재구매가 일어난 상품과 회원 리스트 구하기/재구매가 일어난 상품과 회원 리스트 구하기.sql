-- 동일한 회원이 동일한 상품을 재구매한 데이터
-- HAVING -> GROUP으로 묶은 다음에 그 특성 가지고 필터링
-- COUNT(*) -> 모든 행을 다 셈
-- COUNT(컬럼 명) -> NULL은 빼고 셈
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID HAVING COUNT(*)>1
ORDER BY USER_ID ASC, PRODUCT_ID DESC