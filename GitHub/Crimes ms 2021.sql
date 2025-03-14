-- Os dados disponíveis foram extraídos das soluções SinespJC e Sinesp Integração, 
-- fontes primárias dos seguintes indicadores: Totais de Ocorrências e Totais de Vítimas de estupro, 
-- furto de veículos, homicídio doloso, lesão corporal seguida de morte, roubo à instituição financeira,
 -- roubo de carga, roubo de veículos e roubo seguido de morte.
 -- https://dados.gov.br/dataset/sistema-nacional-de-estatisticas-de-seguranca-publica
create database crimesMS;


use crimesMS;

create table crimes(
    id int auto_increment primary key,
    cidade varchar(100) not null,
    estado varchar (100) not null,
	regiao varchar (100) not null,
    data varchar (10)not null,
    registro int not null
);
 
 
insert into crimes (cidade, estado,regiao,data,registro) values
("Água Clara", "MS", "CENTRO-OESTE", "jan/21", 0),
("Alcinópolis", "MS", "CENTRO-OESTE",	"jan/21", 0),
("Amambai", "MS", "CENTRO-OESTE", "jan/21", 0),
("Anastácio", "MS",	"CENTRO-OESTE", "jan/21", 0),
("Anaurilândia", "MS", "CENTRO-OESTE", "jan/21", 0),
("Angélica", "MS", "CENTRO-OESTE", "jan/21", 0),
("Antônio João",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Aparecida Do Taboado",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Aquidauana", "MS", "CENTRO-OESTE", "jan/21", 0),
("Aral Moreira",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Bandeirantes",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Bataguassu", "MS", "CENTRO-OESTE", "jan/21" , 0),
("Batayporã", "MS", "CENTRO-OESTE", "jan/21", 0),
("Bela Vista", "MS", "CENTRO-OESTE", "jan/21", 0),
("Bodoquena", "MS", "CENTRO-OESTE", "jan/21", 0),
("Bonito", "MS", "CENTRO-OESTE", "jan/21",0),
("Brasilândia",	"MS", "CENTRO-OESTE", "jan/21",	0),
("Caarapó", "MS", "CENTRO-OESTE", "jan/21",	0),
("Camapuã", "MS", "CENTRO-OESTE", "jan/21", 0),
("Campo Grande", "MS", "CENTRO-OESTE", "jan/21", 9),
("Caracol", "MS", "CENTRO-OESTE", "jan/21", 0),
("Cassilândia",	"MS", "CENTRO-OESTE", "jan/21",	0),
("Chapadão Do Sul", "MS", "CENTRO-OESTE", "jan/21", 0),
("Corguinho", "MS", "CENTRO-OESTE", "jan/21", 0),
("Coronel Sapucaia", "MS", "CENTRO-OESTE", "jan/21", 1),
("Corumbá", "MS", "CENTRO-OESTE", "jan/21", 4),
("Costa Rica", "MS", "CENTRO-OESTE", "jan/21", 0),
("Coxim", "MS",	"CENTRO-OESTE",	"jan/21", 1),
("Deodápolis", "MS", "CENTRO-OESTE", "jan/21", 0),
("Dois Irmãos Do Buriti", "MS",	"CENTRO-OESTE",	"jan/21", 0),
("Douradina", "MS", "CENTRO-OESTE", "jan/21", 0),
("Dourados", "MS", "CENTRO-OESTE", "jan/21", 3),
("Eldorado", "MS", "CENTRO-OESTE", "jan/21", 0),
("Fátima Do Sul", "MS",	"CENTRO-OESTE", "jan/21", 1),
("Figueirão", "MS", "CENTRO-OESTE", "jan/21", 0),
("Glória De Dourados", "MS", "CENTRO-OESTE", "jan/21", 0),
("Guia Lopes Da Laguna", "MS", "CENTRO-OESTE", "jan/21", 0),
("Iguatemi", "MS", "CENTRO-OESTE", "jan/21", 0),
("Inocência", "MS", "CENTRO-OESTE", "jan/21", 0),
("Itaporã", "MS", "CENTRO-OESTE", "jan/21", 0),
("Itaquiraí", "MS", "CENTRO-OESTE", "jan/21", 1),
("Ivinhema", "MS", "CENTRO-OESTE", "jan/21", 1),
("Japorã", "MS", "CENTRO-OESTE", "jan/21", 0),
("Jaraguari", "MS", "CENTRO-OESTE", "jan/21", 0),
("Jardim", "MS", "CENTRO-OESTE", "jan/21", 0),
("Jateí", "MS",	"CENTRO-OESTE", "jan/21", 0),
("Juti", "MS", "CENTRO-OESTE", "jan/21", 0),
("Ladário", "MS", "CENTRO-OESTE", "jan/21",0),
("Laguna Carapã", "MS",	"CENTRO-OESTE",	"jan/21", 0),
("Maracaju", "MS", "CENTRO-OESTE", "jan/21", 1),
("Miranda", "MS", "CENTRO-OESTE", "jan/21", 2),
("Mundo Novo", "MS", "CENTRO-OESTE", "jan/21", 0),
("Naviraí", "MS", "CENTRO-OESTE", "jan/21", 0),
("Nioaque", "MS", "CENTRO-OESTE", "jan/21", 0),
("Nova Alvorada Do Sul", "MS", "CENTRO-OESTE", "jan/21", 0),
("Nova Andradina", "MS", "CENTRO-OESTE", "jan/21", 0),
("Novo Horizonte Do Sul", "MS",	"CENTRO-OESTE", "jan/21", 0),
("Paraíso Das Águas", "MS", "CENTRO-OESTE", "jan/21", 0),
("Paranaíba", "MS", "CENTRO-OESTE", "jan/21", 0),
("Paranhos", "MS", "CENTRO-OESTE", "jan/21", 1),
("Pedro Gomes",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Ponta Porã",	"MS", "CENTRO-OESTE", "jan/21",	5),
("Porto Murtinho", "MS", "CENTRO-OESTE", "jan/21", 0),
("Ribas Do Rio Pardo", "MS", "CENTRO-OESTE", "jan/21", 0),
("Rio Brilhante" , "MS", "CENTRO-OESTE", "jan/21", 0),
("Rio Negro", "MS", "CENTRO-OESTE", "jan/21", 0),
("Rio Verde De Mato Grosso", "MS", "CENTRO-OESTE", "jan/21", 0),
("Rochedo", "MS", "CENTRO-OESTE", "jan/21", 0),
("Santa Rita Do Pardo", "MS", "CENTRO-OESTE", "jan/21",	0),
("São Gabriel Do Oeste", "MS", "CENTRO-OESTE", "jan/21", 1),
("Sete Quedas",	"MS", "CENTRO-OESTE", "jan/21",	0),
("Selvíria", "MS", "CENTRO-OESTE", "jan/21", 0),
("Sidrolândia",	"MS", "CENTRO-OESTE", "jan/21",	0),
("Sonora", "MS", "CENTRO-OESTE", "jan/21", 0),
("Tacuru", "MS", "CENTRO-OESTE", "jan/21", 0),
("Taquarussu", "MS", "CENTRO-OESTE", "jan/21", 0),
("Terenos", "MS", "CENTRO-OESTE", "jan/21", 0),
("Três Lagoas",	"MS", "CENTRO-OESTE", "jan/21", 0),
("Vicentina", "MS", "CENTRO-OESTE", "jan/21", 0);

select * from crimes;

select * from crimes where cidade = 'Campo Grande';

select * from crimes where registro > 3;

select cidade, registro from crimes where registro = (select max(registro) from crimes);

select cidade, registro from crimes where registro = (select min(registro) from crimes);

select count(*) from crimes;

select avg (registro) from crimes;

select * from crimes where cidade like "c%";