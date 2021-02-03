--tipo t_endereco
create type t_endereco as (
rua character varying(80),
numero smallint,
bairro  character varying(30),
cidade character varying(50),	
cep  character varying(8)
);

-- cliente
create table cliente(cpf varchar(11) primary key,endereco t_endereco,name varchar(100),telefone varchar[]);
insert into cliente values('12345678901',row('Rua A',1,'Acácia','Andradas','1234'),'Ana','{"3341-3341","3341-3342"}');
insert into cliente values('12345678902',row('Rua B',1,'Bahamas','Baependi','1434'),'Bernadina','{"3342-3342"}');
insert into cliente values('12345678903',row('Rua C',1,'Caxias','Cruzília','1244'),'Carina','{"3351-3341"}');
insert into cliente values('12345678904',row('Rua D',1,'Dourados','Diamantina','1254'),'Diana','{"3341-3341","3341-3342","3332-1111"}');
insert into cliente values('12345678905',row('Rua E',1,'Esperança','Extrema','1334'),'Eliana','{"3366-3366"}');
insert into cliente values('12345678906',row('Rua F',1,'Famas','Formosa','1134'),'Fabiana','{"3353-3353","3353-3342"}');
insert into cliente values('12345678907',row('Rua G',1,'Gramado','Guaxupé','1111'),'Giuliana','{"3361-3345"}');
insert into cliente values('12345678908',row('Rua H',1,'Horto','Heliodora','2234'),'Heuleriana','{"3355-3355"}');
insert into cliente values('12345678909',row('Rua I',1,'Iguaçu','Itajubá','1222'),'Iriana','{"3333-3333","3333-3342"}');
insert into cliente values('12345678910',row('Rua J',1,'Jatobá','Jesuânia','1134'),'Joana','{"3377-3377","3377-3342"}');
insert into cliente values('12345678921',row('Rua J',1,'Jatobá','Jesuânia','1134'),'Joana','{{"3377-3377"},{"3377-3342"}}');


--financiamento

create table financiamento (numero int primary key,cpf_cliente varchar(11),data date,valor real,prazo int,foreign key (cpf_cliente)
references cliente(cpf));
insert into financiamento values('1','12345678901','10/12/2012',60000,60);
insert into financiamento values('2','12345678901','10/12/2013',70000,50);
insert into financiamento values('3','12345678902','10/11/2012',50000,60);
insert into financiamento values('4','12345678903','10/09/2012',80000,60);
insert into financiamento values('5','12345678903','10/12/2011',90000,60);
insert into financiamento values('6','12345678904','10/12/2018',65000,60);
insert into financiamento values('7','12345678904','11/12/2012',73000,60);
insert into financiamento values('8','12345678907','13/11/2012',82000,60);
insert into financiamento values('9','12345678909','10/10/2019',44000,60);
insert into financiamento values('10','12345678910','10/12/2011',86000,60);

--tipo year
create type year as enum ('2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',
						 '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020');

--veiculo
create table veiculo(num_renavam int primary key,valor real ,marca varchar(20),ano year,num_financiamento int,foreign key (num_financiamento) references financiamento(numero) );
insert into veiculo values(12,30000,'Ford','2000','1');
insert into veiculo values(13,60000,'Fiat','2010','2');
insert into veiculo values(14,30000,'Pegeout','2011','4');
insert into veiculo values(15,40000,'Wolksvagem','2000','9');
insert into veiculo values(16,20000,'Toyota','2012','3');
insert into veiculo values(17,30000,'Hyundai','2013','3');
insert into veiculo values(18,50000,'Renault','2009','4');
insert into veiculo values(19,30000,'Chevrolet','2003','8');
insert into veiculo values(20,50000,'Jeep','2006','8');
insert into veiculo values(21,33000,'Honda','2001','6');

--passeio
create table passeio (qtd_passageiros smallint)inherits (veiculo);
insert into passeio values(12,30000,'Ford','2000','1',10);
insert into passeio values(13,60000,'Fiat','2010','2',8);
insert into passeio values(14,30000,'Pegeout','2011','4',9);
insert into passeio values(15,40000,'Wolksvagem','2000','9',5);
insert into passeio values(16,20000,'Toyota','2012','3',7);
insert into passeio values(17,20000,'Ford','2012','3',7);
insert into passeio values(18,13000,'Ford','2012','3',7);
insert into passeio values(19,15000,'Toyota','2011','2',5);
insert into passeio values(20,15000,'Fiat','2010','1',5);
insert into passeio values(21,15000,'Ford','2003','4',5);

--tipo enum
create type enum as enum('1','2','3','4');

--carga
create table carga (carga_maxima int,numero_eixos enum)inherits (veiculo)
insert into carga values(17,30000,'Hyundai','2013','3',100,'1');
insert into carga values(18,50000,'Renault','2009','4',200,'2');
insert into carga values(19,30000,'Chevrolet','2003','8',110,'3');
insert into carga values(20,50000,'Jeep','2006','8',100,'4');
insert into carga values(21,33000,'Honda','2001','6',80,'1');
insert into carga values(21,15000,'Honda','2001','5',80,'4');
insert into carga values(21,15000,'Honda','2001','5',80,'3');
insert into carga values(21,15000,'Honda','2001','5',80,'2');
insert into carga values(21,23000,'Honda','2001','8',80,'1');
insert into carga values(21,33000,'Fiat','2010','9',80,'2');




--funcoes
--carga
create function realizaFinanciamento(n_renavam int,val real ,mar varchar(10),anoA year,n_financiamento int,carg int,numeixo enum)
returns bool as
$body$
	begin
		insert into carga values(n_renavam,val,mar,anoA,n_financiamento,carg,numeixo);
		raise notice 'Financiamento realizado com sucesso!';
	return true;	
	end
$body$
language 'plpgsql' volatile
--realiza um financiamento de um carro do tipo carga
select realizaFinanciamento(25,30000,'Ford','2000','2',3,'2');

--passeio
create function realizaFinanciamento(n_renavam int,val real ,mar varchar(10),anoA year,n_financiamento int,qtdpassageiro int)
returns bool as
$body$
	begin
		insert into passeio values(n_renavam,val,mar,anoA,n_financiamento,qtdpassageiro);
		raise notice 'Financiamento realizado com sucesso!';
	return true;	
	end
$body$
language 'plpgsql' volatile
--realiza um financiamento de um carro do tipo passeio
select realizaFinanciamento(25,30000,'Ford','2000','2',3);






