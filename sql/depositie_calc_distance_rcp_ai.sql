CREATE TABLE temp.glastuinbouw AS ( 																																--EDIT HIER
select 	dep.ai_code::int as ai_code,
			dep.rcp_id::int as rcp_id,
			round(dep.nox_dep::numeric, 4) as nox_dep,
		    dep.n2k_name, 
			dep.rcp_hex_geom,
			dep.ai_sq_geom,
			round(ST_Distance(ST_Centroid(dep.rcp_hex_geom), ST_Centroid(dep.ai_sq_geom))::numeric, 1) as dist_rcp_ai
from depositie.glastuinbouw dep
);																																															--EDIT HIER