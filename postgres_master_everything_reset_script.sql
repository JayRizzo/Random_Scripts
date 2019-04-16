-- THIS IS MY MASTER EVERYTHING NEEDED FOR POSTGRES AN ALL IN ONE
--
-- THIS SETS / RESETS:
--    PERMISSIONS
--    CONSTRAINTS
--    PRIMARY KEYS
--    INDEXES OR INDICES
--    ADDED REINDEX ON THE DATABASE
--    REORDERED THE QUERIES USING THE ORDER BY REPLACE THIS IS MANDITORY
--
-- THIS CLEANS THE USER PERMISSIONS 1 BY 1 AND MAKE SURE THAT ONLY THE SPECIFIED ACCESS GROUPS AND ADMIN USERS ARE GIVEN
--
-- MUST BE RAN ON A PER CLIENT DATABASE NEED.
-- ABSOLUTELY NEEDS THE ORDER BY STATEMENT THE DROPS AND REVOKE STATEMENTS MUST BE FIRST THEN RE-ADD WHATEVER YOU NEED.
--
-- ***NOTE**** THIS HAS BEEN GENERICIZED TO PROTECT ANY POTIENTIAL CLIENT CONFLICT OF INTEREST.
--
-- THIS IS STRICTLY TO EXPRESS IN CODE HOW MY MIND WORKS.
--
-- THIS CODE PRESUMES A FEW THINGS AND THIS IS A `USE AT YOUR OWN DISCRESSION` AS I DON'T EXPECT PEOPLE TO UNDERSTAND WHY I HAD TO CREATE SOMETHING LIKE THIS. =)
-- -- YOUR USERS THAT WILL BE MODIFYING YOUR DATA WILL BE UNDER THE `ETL` GROUP
-- -- YOUR RUNNING THIS CODE AS THE ADMIN FOR THE TABLES
-- -- YOUR "YOUR_DESIGNATED_USER" & "YOUR_ADMIN_USER" WILL BE GRANTED DIRECT ACCESS TO THESE TABLES BUT WILL ALLOW USERS UNDER THE ETL GROUP TO STILL USE THESE TABLES.
--
-- THIS WAS THE 71'ST ITTERATION OF THIS AND WAS A DEVELOPMENT PROCESS THAT WAS CREATED DUE TO PERMISSION & PERFORMANCE ISSUES BETWEEN ALL AWS RDS HOST ENVIRONMENTS.


-- ORDER IS
-- *


SELECT "query_string" FROM (

-- REVOKE FROM ALL INDIVIDUAL USERS AND ONLY TO GROUPS AND YOUR_ADMIN_USER & YOUR_DESIGNATED_USER
SELECT ('REVOKE ALL ON DATABASE "' || TABLE_CATALOG || '" FROM "public";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('REVOKE ALL ON TABLE "' || TABLE_NAME || '" FROM ' || '"' || (SELECT DISTINCT(STRING_AGG(REPLACE("usename", 'rdsadmin', 'public'), '", "')) FROM "pg_user" where usename <> 'YOUR_DESIGNATED_USER' AND usename <> 'YOUR_ADMIN_USER' AND usename <> 'rds_superuser' AND usename <> 'rdsrepladmin') || '"' || ';') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('REVOKE ALL ON DATABASE "' || TABLE_CATALOG || '" FROM ' || '"' || (SELECT DISTINCT(STRING_AGG(REPLACE("usename", 'rdsadmin', 'public'), '", "')) FROM "pg_user" where usename <> 'YOUR_DESIGNATED_USER' AND usename <> 'YOUR_ADMIN_USER' AND usename <> 'rds_superuser' AND usename <> 'rdsrepladmin') || '"' || ';') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('REVOKE ALL ON TABLE "' || TABLE_NAME || '" FROM ' || '"' || (SELECT DISTINCT(STRING_AGG(REPLACE("rolname", 'rdsadmin', 'public'), '", "')) FROM "pg_roles" where rolname <> 'YOUR_DESIGNATED_USER' AND rolname <> 'YOUR_ADMIN_ROLE' AND rolname <> 'rds_superuser' AND rolname <> 'rdsrepladmin') || '"' || ';') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('REVOKE ALL ON DATABASE "' || TABLE_CATALOG || '" FROM ' || '"' || (SELECT DISTINCT(STRING_AGG(REPLACE("rolname", 'rdsadmin', 'public'), '", "')) FROM "pg_roles" where rolname <> 'YOUR_DESIGNATED_USER' AND rolname <> 'YOUR_ADMIN_ROLE' AND rolname <> 'rds_superuser' AND rolname <> 'rdsrepladmin') || '"' || ';') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'

-- SET ALL TABLES AND DATABASE OWNERS TO YOUR_DESIGNATED_USER -- CREATE NEW RESET OWNER QUERIES ONLY IF IT IS NEEDED.
UNION SELECT ('ALTER DATABASE "' || TABLE_CATALOG || '" OWNER TO "YOUR_DESIGNATED_USER";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'  and TABLE_CATALOG NOT IN ( SELECT d.datname as "Name" FROM pg_catalog.pg_database d WHERE d.datname IN (SELECT current_database()) LIMIT 1)
UNION SELECT ('ALTER TABLE "' || TABLE_NAME || '" OWNER TO "YOUR_DESIGNATED_USER";') AS "query_string" FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'public' and TABLE_NAME IN ( select cls.relname as object_name from pg_class cls join pg_roles rol on rol.oid = cls.relowner join pg_namespace nsp on nsp.oid = cls.relnamespace where nsp.nspname not in ('information_schema', 'pg_catalog') and nsp.nspname not like 'pg_toast%' and rol.rolname <> 'YOUR_DESIGNATED_USER')

-- GRANT YOUR_DESIGNATED_USER USER ACCESS TO EVERYTHING
UNION SELECT ('ALTER DEFAULT PRIVILEGES GRANT INSERT, SELECT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER ON TABLES TO "YOUR_DESIGNATED_USER";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO "YOUR_DESIGNATED_USER";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('GRANT ALL ON TABLE "' || TABLE_NAME || '" TO "YOUR_DESIGNATED_USER";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('GRANT ALL ON DATABASE "' || TABLE_CATALOG || '" TO "YOUR_DESIGNATED_USER";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'

-- GRANT YOUR_ADMIN_USER USER ACCESS TO EVERYTHING
UNION SELECT ('ALTER DEFAULT PRIVILEGES GRANT INSERT, SELECT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER ON TABLES TO "YOUR_ADMIN_USER";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO "YOUR_ADMIN_USER";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('GRANT ALL ON DATABASE "' || TABLE_CATALOG || '" TO "YOUR_ADMIN_USER";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('GRANT ALL ON TABLE "' || TABLE_NAME || '" TO "YOUR_ADMIN_USER";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'

-- GRANT ALL TO ETL GROUP
UNION SELECT ('ALTER DEFAULT PRIVILEGES GRANT INSERT, SELECT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER ON TABLES TO GROUP "etl";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO GROUP "etl";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('GRANT ALL ON TABLE "' || TABLE_NAME || '" TO GROUP "etl";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('GRANT ALL ON DATABASE "' || TABLE_CATALOG || '" TO GROUP "etl";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'

-- GRANT ONLY SELECT ACCESS TO THE DEFAULT_PERMISSIONS GROUP - THAT THE APPLICATION USES
UNION SELECT ('ALTER DEFAULT PRIVILEGES GRANT SELECT ON TABLES TO GROUP "default_permissions";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO GROUP "default_permissions";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('GRANT SELECT ON TABLE "' || TABLE_NAME || '" TO GROUP "default_permissions";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('GRANT CONNECT ON DATABASE "' || TABLE_CATALOG || '" TO GROUP "default_permissions";') AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
UNION SELECT ('; ALTER TABLE "' || relname || '" DROP CONSTRAINT IF EXISTS "' || conname || '";') AS "query_string" from "pg_constraint" Join "pg_class" on "pg_constraint"."conrelid" = "pg_class"."oid"

-- SELECTING FROM THE SYSTEM TO SET THE PRIMARY KEYS
UNION SELECT 'ALTER TABLE "' || TABLE_NAME || '" ADD PRIMARY KEY ("' || COLUMN_NAME || '") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND COLUMN_NAME like '%_pk%'

-- SELECTING AND ADDING THE FOREIGNKEY FK TO ALL FACT TABLE INDICES
UNION SELECT 'CREATE INDEX "idx_' || TABLE_NAME || '_' || 'r_foreignkey_fk' || '" ON "' || TABLE_NAME || '" USING btree("' || COLUMN_NAME || '" "pg_catalog"."' || udt_name || '_ops" ASC NULLS LAST);' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND COLUMN_NAME like 'r_foreignkey_fk'

-- DROP STANDARD INDICIES IF THEY EXIST
UNION SELECT ('DROP INDEX IF EXISTS "' || i.relname || '";') as "query_string" FROM pg_index as idx JOIN pg_class as i ON i.oid = idx.indexrelid JOIN pg_am as am ON i.relam = am.oid JOIN pg_namespace as ns ON ns.oid = i.relnamespace AND ns.nspname = ANY(current_schemas(false)) AND i.relname NOT LIKE '%pkey%'

-- CREATE DYNAMIC INDEXES FOR APPLICATION PERFORMANCE
UNION SELECT 'CREATE INDEX "idx_' || TABLE_NAME || '_' || COLUMN_NAME || '" ON "' || TABLE_NAME || '" USING btree("' || COLUMN_NAME || '" "pg_catalog"."' || udt_name || '_ops" ASC NULLS LAST);' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND EXISTS (SELECT DISTINCT "column_name" FROM x_table WHERE COLUMN_NAME LIKE 'r_%' AND x_table."column_name" = information_schema.COLUMNS."column_name")
UNION SELECT 'CREATE INDEX "idx_' || TABLE_NAME || '_' || COLUMN_NAME || '" ON "' || TABLE_NAME || '" USING btree("' || COLUMN_NAME || '" "pg_catalog"."' || udt_name || '_ops" ASC NULLS LAST);' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND (COLUMN_NAME like '%something%' or COLUMN_NAME like '%something%' or COLUMN_NAME like '%something_else_%')
UNION SELECT 'CREATE INDEX "idx_' || TABLE_NAME || '_' || COLUMN_NAME || '" ON "' || TABLE_NAME || '" USING btree("' || COLUMN_NAME || '" "pg_catalog"."' || udt_name || '_ops" ASC NULLS LAST);' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND COLUMN_NAME LIKE '%something%' AND TABLE_NAME <> 'd_date'

-- MAKE ALL _TRUE COLUMS DEFAULT FALSE AND NOT NULL
UNION SELECT 'ALTER TABLE "' || TABLE_NAME || '" ALTER COLUMN "' || COLUMN_NAME || '" SET DEFAULT FALSE;' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND COLUMN_NAME like '%_true%'
UNION SELECT 'ALTER TABLE "' || TABLE_NAME || '" ALTER COLUMN "' || COLUMN_NAME || '" SET NOT NULL;' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND COLUMN_NAME like '%_true%'
UNION SELECT 'ALTER TABLE "' || TABLE_NAME || '" ALTER COLUMN "' || COLUMN_NAME || '" SET NOT NULL;' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND COLUMN_NAME like '%foreign%' and COLUMN_NAME <> 'r_foreignkey_fk' AND TABLE_NAME <> 'f_fact_table_a'

-- MAKE D_ TABLES "NAME" COLUMNS NOT NULL
UNION SELECT 'ALTER TABLE "' || TABLE_NAME || '" ALTER COLUMN "' || COLUMN_NAME || '" SET NOT NULL;' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND COLUMN_NAME like 'name' and table_name not like '%f_fact_table_%' and table_name not like '%d_dim_table_%' and COLUMN_NAME NOT LIKE '%name%'

-- ANALYZE ALL TABLES
UNION SELECT 'ANALYZE "' || TABLE_NAME || '";' AS query_string FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'

-- CREATE HARDCODED THE STANDARD PRIMARY KEYS FOR FACT TABLES FOR THE ONE OFF UNIQUE WEBSITE PERFORMANCE REQUIREMENTS
UNION SELECT 'ALTER TABLE "f_fact_table_a" ADD PRIMARY KEY ("f_fact_table_a_pk") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string"
UNION SELECT 'ALTER TABLE "f_fact_table_b" ADD PRIMARY KEY ("f_fact_table_b_pk") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string"
UNION SELECT 'ALTER TABLE "f_fact_table_c" ADD PRIMARY KEY ("f_fact_table_c_pk") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string"
UNION SELECT 'ALTER TABLE "f_fact_table_d" ADD PRIMARY KEY ("f_fact_table_d_pk") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string"
UNION SELECT 'ALTER TABLE "f_fact_table_e" ADD PRIMARY KEY ("f_fact_table_e_pk") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string"
UNION SELECT 'ALTER TABLE "f_fact_table_f" ADD PRIMARY KEY ("f_fact_table_f_pk") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string"
UNION SELECT 'ALTER TABLE "f_fact_table_g" ADD PRIMARY KEY ("f_fact_table_g_pk") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string"
UNION SELECT 'ALTER TABLE "f_fact_table_h" ADD PRIMARY KEY ("f_fact_table_h_pk") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string"
UNION SELECT 'ALTER TABLE "f_fact_table_i" ADD PRIMARY KEY ("f_fact_table_i_pk", "name", "value") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string"
UNION SELECT 'ALTER TABLE "f_fact_table_j" ADD PRIMARY KEY ("f_fact_table_j_pk", "widget_id", "column_name") NOT DEFERRABLE INITIALLY IMMEDIATE;' AS "query_string"

-- CREATE HARDCODED STANDARD INDICIES FOR DIMENSION TABLES FOR THE ONE OFF UNIQUE WEBSITE SEARCH PERFORMANCE REQUIREMENTS
UNION SELECT 'CREATE INDEX "idx_d_dimension_table_a" ON "d_dimension_a" USING btree("dimension_a_pk" "pg_catalog"."int4_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_d_dimension_table_b" ON "d_dimension_b" USING btree("dimension_b_pk" "pg_catalog"."int4_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_d_dimension_table_c" ON "d_dimension_c" USING btree("dimension_c_pk" "pg_catalog"."int4_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_d_dimension_table_d" ON "d_dimension_d" USING btree("dimension_d_pk" "pg_catalog"."int4_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_d_dimension_table_e" ON "d_dimension_e" USING btree("dimension_e_pk" "pg_catalog"."int4_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_d_dimension_table_f" ON "d_dimension_f" USING btree("dimension_f_pk" "pg_catalog"."int4_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_d_dimension_table_g" ON "d_dimension_g" USING btree("dimension_g_pk" "pg_catalog"."int4_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"

-- CREATE HARDCODED STANDARD INDICIES FOR FACT TABLES FOR THE ONE OFF UNIQUE WEBSITE SEARCH PERFORMANCE REQUIREMENTS
UNION SELECT 'CREATE INDEX "idx_f_fact_table_a" ON "f_fact_a" USING btree("fact_a_fk" "pg_catalog"."int8_ops" ASC NULLS LAST, "transaction_date_fk" "pg_catalog"."int4_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_f_fact_table_b" ON "f_fact_b" USING btree("fact_b_fk" "pg_catalog"."int8_ops" ASC NULLS LAST, "transaction_date_fk" "pg_catalog"."int4_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_f_fact_table_c" ON "f_fact_c" USING btree("fact_c_fk" "pg_catalog"."int8_ops" ASC NULLS LAST, "d_something_true"     "pg_catalog"."bool_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_f_fact_table_d" ON "f_fact_d" USING btree("fact_d_fk" "pg_catalog"."int8_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_f_fact_table_e" ON "f_fact_e" USING btree("fact_e_fk" "pg_catalog"."int8_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_f_fact_table_f" ON "f_fact_f" USING btree("fact_f_fk" "pg_catalog"."int8_ops" ASC NULLS LAST, "r_open_true" "pg_catalog"."bool_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_f_fact_table_g" ON "f_fact_g" USING btree("fact_g_fk" "pg_catalog"."int8_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_f_fact_table_h" ON "f_fact_h" USING btree("fact_h_fk" "pg_catalog"."int8_ops" ASC NULLS LAST, "r_open_true" "pg_catalog"."bool_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_f_fact_table_i" ON "f_fact_i" USING btree("fact_i_fk" "pg_catalog"."int8_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE INDEX "idx_f_fact_table_j" ON "f_fact_j" USING btree("fact_j_fk" "pg_catalog"."int8_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"

-- CREATE HARDCODED UNIQUE INDICIES FOR THE ONE OFF UNIQUE WEBSITE PERFORMANCE REQUIREMENTS
UNION SELECT 'CREATE UNIQUE INDEX "udx_d_dimension_table_a" ON "d_dimension_a" USING btree("d_dimension_a" "pg_catalog"."int4_ops" ASC NULLS LAST, "name_full" "pg_catalog"."text_ops" ASC NULLS LAST, "name_first" "pg_catalog"."text_ops" ASC NULLS LAST, "name_last" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_d_dimension_table_b" ON "d_dimension_b" USING btree("d_dimension_b" "pg_catalog"."int4_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_d_dimension_table_c" ON "d_dimension_c" USING btree("d_dimension_c" "pg_catalog"."int4_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_d_dimension_table_d" ON "d_dimension_d" USING btree("d_dimension_d" "pg_catalog"."int4_ops" ASC NULLS LAST, "r_fact_fk_client" "pg_catalog"."text_ops" ASC NULLS LAST, "onet_fk" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_d_dimension_table_e" ON "d_dimension_e" USING btree("d_dimension_e" "pg_catalog"."int4_ops" ASC NULLS LAST, "r_fact_fk_client" "pg_catalog"."text_ops" ASC NULLS LAST, "onet_fk" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_d_dimension_table_f" ON "d_dimension_f" USING btree("d_dimension_f" "pg_catalog"."int4_ops" ASC NULLS LAST, "r_fact_fk_client" "pg_catalog"."text_ops" ASC NULLS LAST, "onet_fk" "pg_catalog"."text_ops" ASC NULLS LAST, "stuff_txt" ASC NULLS LAST, "stuff_true" "pg_catalog"."bool_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_d_dimension_table_g" ON "d_dimension_g" USING btree("d_dimension_g" "pg_catalog"."int4_ops" ASC NULLS LAST, "name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"

-- CREATE HARDCODED UNIQUE INDICIES FOR THE ONE OFF UNIQUE WEBSITE PERFORMANCE REQUIREMENTS
UNION SELECT 'CREATE UNIQUE INDEX "udx_f_fact_table_a_fk_name" ON "f_fact_a" USING btree("f_fact_a_fk" "pg_catalog"."int8_ops" ASC NULLS LAST,"d_dimension_a_name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_f_fact_table_b_fk_name" ON "f_fact_b" USING btree("f_fact_b_fk" "pg_catalog"."int8_ops" ASC NULLS LAST,"d_dimension_b_name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_f_fact_table_c_fk_name" ON "f_fact_c" USING btree("f_fact_c_fk" "pg_catalog"."int8_ops" ASC NULLS LAST,"d_dimension_c_name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_f_fact_table_d_fk_name" ON "f_fact_d" USING btree("f_fact_d_fk" "pg_catalog"."int8_ops" ASC NULLS LAST,"d_dimension_d_name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_f_fact_table_e_fk_name" ON "f_fact_e" USING btree("f_fact_e_fk" "pg_catalog"."int8_ops" ASC NULLS LAST,"d_dimension_e_name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_f_fact_table_f_fk_name" ON "f_fact_f" USING btree("f_fact_f_fk" "pg_catalog"."int8_ops" ASC NULLS LAST,"d_dimension_f_name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_f_fact_table_g_fk_name" ON "f_fact_g" USING btree("f_fact_g_fk" "pg_catalog"."int8_ops" ASC NULLS LAST,"d_dimension_g_name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_f_fact_table_h_fk_name" ON "f_fact_h" USING btree("f_fact_h_fk" "pg_catalog"."int8_ops" ASC NULLS LAST,"d_dimension_h_name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_f_fact_table_i_fk_name" ON "f_fact_i" USING btree("f_fact_i_fk" "pg_catalog"."int8_ops" ASC NULLS LAST,"d_dimension_i_name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"
UNION SELECT 'CREATE UNIQUE INDEX "udx_f_fact_table_j_fk_name" ON "f_fact_j" USING btree("f_fact_j_fk" "pg_catalog"."int8_ops" ASC NULLS LAST,"d_dimension_j_name" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string"

-- CREATE THIS LAST UNIQUE INDEX, IT IS DYNAMIC AND SHOULD ONLY BE APPLIED IF IT EXISTS IN THE CUSTOM CLIENT SPECIFIC INFORMATION SCHEMA.
UNION SELECT 'CREATE UNIQUE INDEX "udx_d_dimension_h" ON "d_d_dimension_h" USING btree("achievement_type" "pg_catalog"."text_ops" ASC NULLS LAST, "achievement_code" "pg_catalog"."text_ops" ASC NULLS LAST);' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public' AND table_name = 'd_d_dimension_h'

-- THIS REINDEXES THE POSTGRES TABLES FOR EACH CLIENT.  ((EXPECT TO WAIT)): EST. ~600 SECONDS OR LESS PER 50,000,000 RECORDS
-- -- DEPENDING ON THE PERFORMANCE OF YOUR RDS POSTGRES INSTANCE, NETWORK, LOCATION OF YOU IN RELATION OF YOU TO SERVER, LOAD ON THE SERVER, HOW MANY CONNECTIONS ARE TO THE DB, ETC.
UNION SELECT 'REINDEX TABLE "' || TABLE_NAME || '";' AS "query_string" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'public'
) derived_table

-- ALL QUERIES ARE GENERATED TO A STRING FOR YOU TO COPY AND RUN

-- THIS ORDERS ALL QUERIES INTO THE SPECIFIC ORDER TO BE RAN, THIS PREVENTS ERRORS.
ORDER BY replace(replace(replace(replace(replace(replace(replace(replace(replace(replace("query_string", 'ANALYZE', 'ZY'), 'GRANT CONNECT ON', 'aaabbb'), 'ALTER DEFAULT PRIVILEGES', 'aaabb'), 'REINDEX', 'ZZ'), ';', 'AA'), 'ADD PRIMARY KEY', 'W'), 'GRANT', 'AAAB'), 'REVOKE ALL', 'AAAA'), 'DROP', 'AB'), 'CREATE', 'Z');
