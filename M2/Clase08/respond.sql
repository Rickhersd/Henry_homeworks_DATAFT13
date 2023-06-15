
create table locales(     
    id_local int not null auto_increment,
    nombre varchar(100) not null, 
    categoria varchar(100) not null,
    direccion varchar(100) not null,     
    barrio varchar(100) not null,
    comuna varchar(100) not null,     
    PRIMARY KEY (id_local) 
    );
