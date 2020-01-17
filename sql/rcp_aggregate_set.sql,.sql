CREATE TABLE depositie.glastuinbouw_rcp_agg AS (		
	SELECT rcp_id,
				count(ai_code) as ai_code_count,
				sum(nox_dep) as nox_dep_sum,
				max(n2k_name) as n2k_name,
				round(avg(dist_rcp_ai),1) as dist_rcp_ai_avg,
				rcp_hex_geom
	--			st_union(ai_sq_geom) as ai_union_geom
	FROM depositie.glastuinbouw dp
	GROUP BY rcp_id, rcp_hex_geom);