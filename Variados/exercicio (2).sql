--tipo t_endereco
create type t_endereco as (
rua character varying(80),
numero smallint,
bairro  character varying(30),
cidade character varying(50),	
cep  character varying(8)
);
--implementação de modelo substituindo os relacionamentos por inclusão de array de tipos
--tipo enum
create type enum as enum('1','2','3','4');
--tipo year
create type year as enum ('2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',
'2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020');
--tipo cliente
create type cliente as(
cpf varchar(11),
endereco t_endereco,
name varchar(100),
telefone varchar[]);

--financiamento de varios veiculos
create type financiamento as (
numero int ,
client cliente,
data date,
valor real,
prazo int
);

--objeto pode assumir o tipo passeio ou carga
create table veiculo(num_renavam int primary key not null ,valor real not null,marca varchar(20) not null,ano year,fin financiamento not null);
create table passeio (qtd_passageiros smallint)inherits (veiculo);
create table carga (carga_maxima int,numero_eixos enum)inherits (veiculo)
--examples insert
insert into veiculo values(1,20000,'Fiat','2009',row('123',row('12345678901',row('Rua A',10,'Acácia','Andradas','1234'),'Ana','{{"3343-1111"},{"3343-1112"}}'),'10/10/2010',25000,300))
insert into veiculo values(5,22000,'Toyota','2009',row('121',row('12345678945',row('Rua A',10,'Acácia','Andradas','124'),'Ana','{{"3343-1111"},{"3343-1112"}}'),'10/10/2010',25000,300))
insert into veiculo values(11,20000,'Fiat','2009',row('123',row('12345678901',row('Rua A',10,'Acácia','Andradas','1234'),'Ana','{{"3343-1111"},{"3343-1112"}}'),'10/10/2010',25000,300))
insert into veiculo values(23,21000,'Toyota','2003',row('125',row('12345678945',row('Rua A',10,'Acácia','Andradas','124'),'Ana','{{"3343-1111"}}'),'10/10/2010',25000,300))
insert into veiculo values(51,50000,'Honda','2005',row('123',row('12345678801',row('Rua D',10,'São Paulo','Andradas','1234'),'Fábia','{{"3343-1121"}}'),'10/10/2010',25000,500))
insert into veiculo values(15,12000,'Reneault','2001',row('121',row('12345678845',row('Rua G',10,'Passos','Caxambu','1111'),'Maria','{{"3343-1112"}}'),'11/10/2011',55000,300))
insert into veiculo values(55,52000,'Fiat','2001',row('126',row('12345678915',row('Rua B',11,'Cascata','Andradas','121'),'Ana','{{"3322-1111"}}'),'11/11/2000',25010,400))
insert into veiculo values(21,50000,'Honda','2005',row('123',row('12345671101',row('Rua F',09,'São Paulo','Andradas','1234'),'Fernanda','{{"3323-1121"}}'),'10/10/2010',25000,500))
insert into veiculo values(45,12000,'Reneault','2007',row('121',row('12345118845',row('Rua B',10,'Pedra','Caxambu','1111'),'Marcia','{{"3113-1112"}}'),'11/10/2001',55000,300))
insert into veiculo values(85,12000,'Reneault','2007',row('121',row('12342118845',row('Rua B',10,'Pedra','Caxambu','1111'),'Marcia','{{"3113-1112"}}'),'11/10/2001',55000,300))

insert into carga values(2,40000,'Ford','2001',row('123',row('12345678910',row('Rua B',10,'Bodas','Baependi','1233'),'Bruna','{{"3343-3343"}}'),'10/11/2013',30000,600),10,'3')
insert into carga values(2,10000,'Ford','2001',row('123',row('12345678920',row('Rua D',10,'Diana','Dourados','11'),'Diana','{{"3343-3222"}}'),'09/11/2011',32000,400),20,'1')
insert into carga values(9,43000,'Fiat','2001',row('127',row('12345678933',row('Rua B',10,'Bodas','Baependi','123'),'Bruna','{{"3343-3343"}}'),'10/11/2013',30000,600),10,'3')
insert into carga values(10,35000,'Honda','2002',row('423',row('12345678925',row('Rua D',10,'Diana','Dourados','11'),'Diana','{{"3343-3222"}}'),'09/11/2011',32000,400),20,'1')
insert into carga values(23,21000,'Toyota','2003',row('125',row('12345678945',row('Rua A',10,'Acácia','Andradas','124'),'Ana','{{"3343-1111"}}'),'10/10/2010',25000,300),8,'2')
insert into carga values(51,50000,'Honda','2005',row('123',row('12345678801',row('Rua D',10,'São Paulo','Andradas','1234'),'Fábia','{{"3343-1121"}}'),'10/10/2010',25000,500),10,'1')
insert into carga values(15,12000,'Reneault','2001',row('121',row('12345678845',row('Rua G',10,'Passos','Caxambu','1111'),'Maria','{{"3343-1112"}}'),'11/10/2011',55000,300),20,'2')
insert into carga values(55,52000,'Fiat','2001',row('126',row('12345678915',row('Rua B',11,'Cascata','Andradas','121'),'Ana','{{"3322-1111"}}'),'11/11/2000',25010,400),30,'1')
insert into carga values(3,40000,'Ford','2007',row('113',row('12345678911',row('Rua C',10,'Bodas','Bosque','1233'),'Bruna','{{"3343-3343"}}'),'10/11/2013',30000,600),10,'3')
insert into carga values(21,50000,'Honda','2005',row('123',row('12345671101',row('Rua F',09,'São Paulo','Andradas','1234'),'Fernanda','{{"3323-1121"}}'),'10/10/2010',25000,500),10,'3')

insert into passeio values(1,20000,'Fiat','2009',row('123',row('12345678901',row('Rua A',10,'Acácia','Andradas','1234'),'Ana','{{"3343-1111"},{"3343-1112"}}'),'10/10/2010',25000,300),5)
insert into passeio values(7,21000,'Renealut','2009',row('113',row('12345678331',row('Rua A',10,'Acácia','Andradas','1234'),'Ana','{{"3343-1111"},{"3343-1112"}}'),'10/10/2010',25000,300),5)
insert into passeio values(1,20000,'Fiat','2009',row('123',row('12345678901',row('Rua A',10,'Acácia','Andradas','1234'),'Ana','{{"3343-1111"},{"3343-1112"}}'),'10/10/2010',25000,300),6)
insert into passeio values(5,22000,'Toyota','2009',row('121',row('12345678945',row('Rua A',10,'Acácia','Andradas','124'),'Ana','{{"3343-1111"},{"3343-1112"}}'),'10/10/2010',25000,300),8)
insert into passeio values(11,20000,'Fiat','2009',row('123',row('12345678901',row('Rua A',10,'Acácia','Andradas','1234'),'Ana','{{"3343-1111"},{"3343-1112"}}'),'10/10/2010',25000,300),9)
insert into passeio values(23,21000,'Toyota','2003',row('125',row('12345678945',row('Rua A',10,'Acácia','Passos','124'),'Ana','{{"3343-1111"}}'),'10/10/2010',25000,300),5)
insert into passeio values(51,50000,'Honda','2005',row('123',row('12345678801',row('Rua D',10,'São Paulo','Cruzilia','1234'),'Fábia','{{"3343-1121"}}'),'10/10/2010',25000,500),2)
insert into passeio values(81,55500,'Fiat','2001',row('111',row('12345218331',row('Rua F',10,'Acácia','Sao Paulo','1134'),'Ana','{{"3343-1112"}}'),'10/10/2010',25300,300),2)
insert into passeio values(87,21000,'Ford','2009',row('113',row('12345678331',row('Rua A',10,'Acácia','Andradas','1234'),'Ana','{{"3343-1111"},{"3343-1112"}}'),'10/10/2010',25000,300),5)
insert into passeio values(17,21000,'Pegeault','2002',row('213',row('12311178331',row('Rua G',11,'Acácia','Andradas','4'),'Fábia','{{"3113-1111"},{"3343-1112"}}'),'10/10/2010',25000,300),5)




--funcoes
--funcao financiamento carga
create function realizaFinanciamento(n_renavam int,val real ,mar varchar(10),anoA year,fin financiamento,carg int,numeixo enum)
returns bool as
$body$
	begin
		insert into carga values(n_renavam,val,mar,anoA,fin,carg,numeixo);
		raise notice 'Financiamento realizado com sucesso!';
	return true;	
	end
$body$
language 'plpgsql' volatile
--realiza um financiamento de um carro do tipo carga
select realizaFinanciamento(2,30000.2,'Toyota','2001',row('121',row('12345678911',row('Rua C','10','Caixias','Cruzeiro','1232'),'Carina','{{"3343-1112"}}'),'10/10/2011',25000,600),100,'2')

--funcao financiamento passeio
create function realizaFinanciamento(n_renavam int,val real ,mar varchar(10),anoA year,fin financiamento,qtdpassageiros int)
returns bool as
$body$
	begin
		insert into passeio values(n_renavam,val,mar,anoA,fin,qtdpassageiros);
		raise notice 'Financiamento realizado com sucesso!';
	return true;	
	end
$body$
language 'plpgsql' volatile
--realiza um financiamento de um carro do tipo passeio
select realizaFinanciamento(2,30000.2,'Toyota','2001',row('121',row('12345678911',row('Rua C','10','Caixias','Cruzeiro','1232'),'Carina','{{"3343-1112"}}'),'10/10/2011',25000,600),5)
