-- Bouwen van een hexgrid met alleen unieke geometrieen
-- We nemen de hoogste kritische depositie als waarde
-- Output: rcp_id, n2k, max_critical_dep, geom

CREATE TABLE base.hex_met_n2k_noduplicates AS (
SELECT max(rcp_id)::int as rcp_id, max(natura2001) as n2k, max(critical_dep)::int as max_crit_dep, geom
FROM base.hex_met_n2k
group by geom);