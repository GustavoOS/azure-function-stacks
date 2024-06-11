create table "public".content (
    id serial primary key,
    title varchar(25) not null,
    color varchar(7) not null
);

alter table "public".content
add constraint color_hex_constraint
check (color is null or color ~* '^#[a-f0-9]{6}$');