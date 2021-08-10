create table  rota (codigo varchar(100) not null primary key,origem varchar(100) not null,destino varchar(100) not null,duracao int not null ,distancia int , paradas varchar(100), dias_semana varchar(100) not null, horario_partida varchar(100)not null , horario_chegada varchar(100)not null)

insert into rota values ('1','sao paulo','rio de janeiro',3,400,'','domingo','1:00','4:00')
insert into rota values ('2','sao pedro','taubate',4,500,'','domingo','1:00','5:00')
insert into rota values ('3','itajuba','vitoria',18,1000,'sao paulo','sabado','1:00','19:00')
insert into rota values ('4','caxambu','salvador',8,1400,'belo horizonte','sexta','1:00','9:00')
insert into rota values ('5','cruzeiro','lorena',12,1400,'','segunda','1:00','13:00')

create table funcionario(cpf varchar(100) not null primary key, nome varchar(100) not null unique, rua varchar(100) not null, numero varchar(100) not null, bairro varchar(100) not null, cidade varchar(100) not null, estado varchar(100) not null, cargo varchar(100) not null, data_nascimento date not null, 
						 check(data_nascimento<'01/07/2002'),check(cargo='GERENTE'  OR cargo='BALCONISTA'OR cargo='COBRADOR'OR cargo='MOTORISTA'))

insert into funcionario values('01','fernando','jose da silva','200','pinheiro','sao paulo','sp','MOTORISTA','01/02/1990')
insert into funcionario values('02','giovany','getulio vargas','124','cascata','itajuba','mg','BALCONISTA','02/01/1990')
insert into funcionario values('03','pedro','palmeiras','300','centro','caxambu','mg','MOTORISTA','11/07/1993')
insert into funcionario values('04','paulo','antonio vieira','201','pedra','cruzeiro','sp','COBRADOR','30/07/1989')
insert into funcionario values('05','maria','camilo soares','223','lagoa','rio de janeiro','rj','GERENTE','10/02/1970')

create table passagem(codigo varchar(100) not null primary key, cod_rota varchar(100) not null, valor float not null,id_funcionario varchar(100)not null,foreign key (cod_rota) references rota(codigo) ,foreign key (id_funcionario) references funcionario(cpf))

insert into passagem values('001','1',80,'02')
insert into passagem values('002','2',100,'02')
insert into passagem values('003','3',780,'02')
insert into passagem values('004','4',810,'02')
insert into passagem values('005','5',801,'02')

create table telefone(id_funcionario varchar(100) not null, telefone varchar(100) not null, primary key(id_funcionario,telefone),foreign key (id_funcionario) references funcionario(cpf))

insert into telefone values('01','9999-9999')
insert into telefone values('02','9999-9998')    
insert into telefone values('03','9999-9923')
insert into telefone values('04','9991-9999')    
insert into telefone values('02','9999-9991') 
insert into telefone values('03','9999-91')
select * from telefone
create or replace function RN_telefone () returns void AS $$
declare t  telefone%ROWTYPE; 
begin
	for t in select * from telefone loop
    
		if(length(t.telefone)!=9)then
            RAISE NOTICE ' ID: %  Telefone : %', t.id_funcionario, t.telefone;
		end if;
	end loop ;
delete from telefone where length(telefone) != 9;
end;
$$
language plpgsql;
Select (RN_telefone())


create  table onibus(codigo varchar(100) not null primary key, modelo varchar(100) not null, ano int not null , quilometragem float not null, tanque float not null, consumo_combustivel float, data_prox_revisao date not null, lugares int not null)

insert into onibus values('0001','mercedes',2000,1200,80,15.5,'01/07/2022',40)
insert into onibus values('0002','fiat',2001,12000,90,20.5,'11/09/2022',50)
insert into onibus values('0003','ford',2010,1300,70,18.5,'01/08/2021',35)
insert into onibus values('0004','mercedes',2012,1700,50,16.5,'01/07/2023',42)
insert into onibus values('0005','fiat',2005,1240,80,15.5,'01/07/2022',40)

create table trajeto(cod_trajeto varchar(100) not null, cod_rota varchar(100) not null, cod_motorista varchar(100) not null ,
 cod_cobrador varchar(100) not null, data date not null unique, consumo float, cod_onibus varchar(100) not null,primary key(cod_trajeto,cod_rota),
foreign key (cod_rota) references rota(codigo)   on update cascade on delete cascade, foreign key (cod_motorista) references funcionario(cpf) ,foreign key (cod_cobrador) 
references funcionario(cpf) ,foreign key(cod_onibus )references onibus(codigo))



insert into trajeto values('00001','1','01','04','12/02/2020',100,'0001')
insert into trajeto values('00002','1','03','04','12/01/2021',null,'0002')
insert into trajeto values('00003','5','03','04','11/07/2018',200,'0003')
insert into trajeto values('00004','3','01','04','12/12/2021',100,'0004')
insert into trajeto values('00005','4','01','04','23/01/2020',100,'0005')
--insert into trajeto values('00005','4','01','04','23/01/2020',100,'0005')

create table vistoria(cod_vistoria varchar(100) not null primary key, cod_onibus varchar(100) not null, 
quilometragem float not  null, data_revisao date not null, estado varchar(100) not null,foreign key (cod_onibus) references onibus(codigo))

insert into vistoria values('11','0001',1000,'12/07/2008','bom')
insert into vistoria values('12','0002',2000,'02/08/2013','bom')
insert into vistoria values('13','0003',3000,'12/07/2004','bom')
insert into vistoria values('14','0004',4000,'10/07/2005','bom')
insert into vistoria values('15','0005',500,'11/06/2018','bom')

create table empresa(CNPJ varchar(100) not null primary key, nome varchar(100) not null unique)

insert into empresa values('31','gardenia')
insert into empresa values('32','coutinho')
insert into empresa values('33','passaro')
insert into empresa values('34','cidade do aco')
insert into empresa values('35','cometa')

create table contrato(codigo varchar(100) not null primary key,vigencia varchar(100) not null, 
	valor float not null)

insert into contrato values('41','23/03/2019-23/03/2025',100000)
insert into contrato values('42','12/03/2019-12/03/2025',200000)
insert into contrato values('43','14/03/2019-14/03/2025',300000)
insert into contrato values('44','23/05/2019-23/05/2025',400000)
insert into contrato values('45','23/03/2018-23/03/2024',500000)

create table possui(CNPJ varchar(100) not null, cod_onibus varchar(100) not null,cod_contrato varchar(100 ) not null,primary key(CNPJ,cod_onibus),
foreign key(CNPJ) references empresa(CNPJ),foreign key(cod_onibus) references onibus(codigo),foreign key(cod_contrato) references contrato(codigo))

insert into possui values('31','0001','41')
insert into possui values('32','0002','42')
insert into possui values('33','0003','43')
insert into possui values('34','0004','44')
insert into possui values('35','0005','45')

--consulta os onibus que têm quilometragem > 1500
create view view_onibus as (select codigo, modelo, ano, quilometragem, tanque, data_prox_revisao, lugares from onibus where quilometragem > 1500)

--Consulta origem,destino e distância da rota , data do trajeto e data da vistoria de onibus que fizeram vistoria após 01/07/2010

create materialized view vtra_vist as select ro.origem, ro.destino, ro.distancia,tra.data,vis.data_revisao from rota ro,
trajeto tra,vistoria vis  where tra.cod_rota = ro.codigo and vis.cod_onibus = tra.cod_onibus  and vis.data_revisao> '01/07/2010'

-- procedure

create or replace function RN_telefone () returns void AS $$
declare t  telefone%ROWTYPE; 
begin
for t in select * from telefone loop
    
if(lenght(t.telefone)!=9)then
            RAISE NOTICE ‘ ID: %  Telefone : %’, t.id_funcionario, t.telefone;
end if;
end loop ;
delete from telefone where length(telefone) != 9;
end;
$$
language plpgsql;
Select (RN_telefone())


--trigger
create or replace function verifica_alocacao () returns trigger AS $$
declare  mot trajeto.cod_motorista%TYPE;
declare  cob trajeto.cod_cobrador%TYPE;
declare  datta trajeto.data%TYPE;
declare t trajeto%rowtype; 
begin
	for t in select * from trajeto loop
	select t.cod_motorista into mot from trajeto; 
	select t.cod_cobrador into cob from trajeto; 
	select t.data into datta from trajeto; 
		if(new.cod_motorista = mot and new.cod_cobrador = cob and new.data  = datta) then
    	raise exception ' Nao eh possivel alocar esses funcionarios';
		end if;
    end loop;
return new;
end;
$$
language plpgsql;

create trigger verifica_alocacao before insert on trajeto for each row execute procedure verifica_alocacao();    
