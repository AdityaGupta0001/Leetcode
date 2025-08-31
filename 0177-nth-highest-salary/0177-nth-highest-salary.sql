CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE COUNTER INT;
    SET COUNTER = N-1;
    RETURN (
        SELECT COALESCE(
            (SELECT DISTINCT salary
            FROM Employee
            ORDER BY salary DESC
            LIMIT 1 OFFSET COUNTER),
            NULL
        )
    );
END