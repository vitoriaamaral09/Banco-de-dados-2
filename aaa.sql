CREATE PROCEDURE ConsultarEmprestimosPorCurso
    @curso NVARCHAR(50) -- Parâmetro para o nome do curso
AS
BEGIN
    -- Consulta principal
    SELECT 
        e.curso,
        COUNT(DISTINCT e.id_estudante) AS total_estudantes,
        SUM(emp.valor_emprestimo) AS valor_total_emprestado,
        AVG(emp.taxa_juros) AS taxa_media_juros
    FROM 
        estudante e
    JOIN 
        emprestimo emp ON e.id_estudante = emp.id_estudante
    JOIN 
        parcelas p ON emp.id_emprestimo = p.id_emprestimo
    WHERE 
        p.status = 'Pendente' -- Considera apenas empréstimos pendentes
        AND e.curso = @curso -- Filtra pelo curso informado
    GROUP BY 
        e.curso;
END;

EXEC ConsultarEmprestimosPorCurso @curso = 'Engenharia';