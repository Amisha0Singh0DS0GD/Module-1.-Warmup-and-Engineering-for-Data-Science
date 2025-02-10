CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE offset_N INT;
    SET offset_N = N - 1;
    RETURN (
        SELECT DISTINCT salary FROM Employee 
        ORDER BY salary DESC
        LIMIT 1 OFFSET offset_N
  );
END