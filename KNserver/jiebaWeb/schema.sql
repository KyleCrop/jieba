drop table if exists entries;
create table entries (
	id integer primary key autoincrement, 
	proc blob not null,
	text text not null);
