DROP TABLE if exists "swuser" CASCADE;
DROP TABLE if exists "planet_votes";
DROP TABLE if exists "characters";

CREATE TABLE "swuser" (
	"id" serial NOT NULL,
	"username" varchar(30) NOT NULL UNIQUE,
	"password" varchar(80) NOT NULL,
	CONSTRAINT swuser_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "planet_votes" (
	"id" serial NOT NULL,
	"planet_id" integer NOT NULL,
	"user_id" integer NOT NULL,
	"submission_time" timestamp NOT NULL,
	CONSTRAINT planet_votes_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);


CREATE TABLE "characters" (
	"id" serial NOt NULL,
	"char_id" integer NOT NULL,
	"name" varchar(30) NOT NULL,
	"description" text NOT NULL,
	CONSTRAINT characters_pk PRIMARY KEY ("id")
) WITH (
	OIDS=FALSE
);



ALTER TABLE "planet_votes" ADD CONSTRAINT "planet_votes_fk0" FOREIGN KEY ("user_id") REFERENCES "swuser"("id");

