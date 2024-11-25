CREATE TABLE `estudante` (
  `id_estudante` integer PRIMARY KEY,
  `nome` varchar(100),
  `email` varchar(100),
  `curso` varchar(50),
  `ano_entrada` integer
);

CREATE TABLE `emprestimo` (
  `id_emprestimo` integer PRIMARY KEY,
  `id_estudante` integer,
  `valor_emprestimo` decimal(10,2),
  `data_inicio` date,
  `data_vencimento` date,
  `taxa_juros` decima(5,2)
);

CREATE TABLE `parcelas` (
  `id_parcelas` interger PRIMARY KEY,
  `id_emprestimo` integer,
  `numero_parcela` integer,
  `valor_parcela` decimal(10,2),
  `data_vencimento` date,
  `status` varchar(20)
);

CREATE TABLE `garantia` (
  `id_garantia` integer PRIMARY KEY,
  `id_emprestimo` integer,
  `tipo_garantia` varchar(50),
  `descrição` varchar(100)
);

CREATE TABLE `fiadores` (
  `id_fiador` integer PRIMARY KEY,
  `id_estudante` integer,
  `nome_fiador` varchar(100),
  `contato` varchar(10)
);

CREATE TABLE `pagamentos` (
  `id_pagamento` integer PRIMARY KEY,
  `id_parcela` integer,
  `data_pagamento` date,
  `valor_pago` decimal(10,2)
);

CREATE TABLE `instituicoes_financeiras` (
  `id_instituicao` integer PRIMARY KEY,
  `id_emprestimo` integer,
  `nome_instituicao` varchar(40),
  `taxa_base` decimal(10,5)
);

CREATE TABLE `contratos` (
  `id_contrato` integer PRIMARY KEY,
  `id_emprestimo` integerger,
  `data_contrato` date,
  `arquivo` blob
);

ALTER TABLE `garantia` ADD FOREIGN KEY (`id_emprestimo`) REFERENCES `emprestimo` (`id_emprestimo`);

ALTER TABLE `parcelas` ADD FOREIGN KEY (`id_emprestimo`) REFERENCES `emprestimo` (`id_emprestimo`);

ALTER TABLE `estudante` ADD FOREIGN KEY (`id_estudante`) REFERENCES `emprestimo` (`id_emprestimo`);

ALTER TABLE `fiadores` ADD FOREIGN KEY (`id_estudante`) REFERENCES `estudante` (`id_estudante`);

ALTER TABLE `pagamentos` ADD FOREIGN KEY (`id_parcela`) REFERENCES `parcelas` (`id_parcelas`);

ALTER TABLE `contratos` ADD FOREIGN KEY (`id_emprestimo`) REFERENCES `emprestimo` (`id_emprestimo`);

ALTER TABLE `instituicoes_financeiras` ADD FOREIGN KEY (`id_emprestimo`) REFERENCES `emprestimo` (`id_emprestimo`);
