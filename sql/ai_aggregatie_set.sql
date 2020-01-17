CREATE TABLE depositie.glastuinbouw_ai_agg AS ( 				--> DEZE AANPASSEN
	
SELECT ai_code,
			count(rcp_id) as rcp_count,
			sum(nox_dep) as nox_dep_sum,
			n2k_name,
			ai_sq_geom,
			round(avg(dist_rcp_ai),1) as dist_ai_rcp_avg
--			st_union(ai_sq_geom) as ai_union_geom
FROM depositie.glastuinbouw dp 										--> DEZE AANPASSEN
GROUP BY ai_sq_geom, ai_code, n2k_name

UNION

SELECT ai_code,
			count(rcp_id) as rcp_count,
			sum(nox_dep) as nox_dep_sum,
			--count(DISTINCT n2k_name) as n2k_count,
			'Alle natura 2000 gebieden' as n2k_name,
			ai_sq_geom,
			round(avg(dist_rcp_ai),1) as dist_ai_rcp_avg
--			st_union(ai_sq_geom) as ai_union_geom
FROM depositie.glastuinbouw dp 										--> DEZE AANPASSEN
GROUP BY ai_sq_geom, ai_code--
);