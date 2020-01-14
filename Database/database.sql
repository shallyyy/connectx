create database connectx
    with owner postgres;

create sequence tables.games_gameid_seq;

create sequence tables.moves_moveid_seq;

create sequence tables.users_uid_seq;

create table tables.users
(
    uid      int4 default nextval('tables.users_uid_seq'::regclass) not null
        constraint users_pk
            primary key,
    password varchar(12),
    username varchar                                                not null
        constraint users_username_uindex
            unique
);

create table tables.games
(
    player_1            int4                                                              not null
        constraint games_users_uid_fk
            references tables.users
            on update cascade
        constraint games_users_uid_fk_2
            references tables.users,
    player_2            int4         default 0,
    gameid              int4         default nextval('tables.games_gameid_seq'::regclass) not null,
    gamestate           int4         default '-1'::integer,
    started             timestamp(6) default CURRENT_TIMESTAMP,
    current_player_turn int4
);

create unique index games_gameid_uindex
    on tables.games (gameid);

create unique index games_pk
    on tables.games (gameid);

alter table tables.games
    add constraint games_pk
        primary key (gameid);

create table tables.moves
(
    moveid   int4 default nextval('tables.moves_moveid_seq'::regclass) not null,
    playerid int4                                                      not null
        constraint moves___fk_1
            references tables.users
            on update cascade,
    x        int4                                                      not null,
    y        int4,
    gameid   int4                                                      not null
);

create unique index moves_moveid_uindex
    on tables.moves (moveid);

create unique index moves_pk
    on tables.moves (moveid);

alter table tables.moves
    add constraint moves_pk
        primary key (moveid);

create unique index users_uid_uindex
    on tables.users (uid);

