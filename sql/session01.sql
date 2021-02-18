--02/09
-- here is the code without creating the database, 'cause sqlive dt need --
-- livesql.oracle.com

create table tb_client(
        client_id int primary key,
        client_name varchar(155),
        client_phone varchar(50),
        client_email varchar(240)
);

select * from tb_client;

insert into tb_client values(1,'João Victor','(11)961878349','joao@gmail.com');
