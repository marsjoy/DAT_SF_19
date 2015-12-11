CREATE TABLE top_ten_most_dangerous AS
SELECT ci.country, occurrences, ra.rank
FROM (
  SELECT dc_identifier, occurrences, @dangerRank := @dangerRank + 1 AS rank
  FROM (
    SELECT dc_identifier, COUNT(*) AS occurrences
    FROM feed_entries where feed_id = '100,765'
    GROUP BY dc_identifier
    ) ta
  UNION ALL
  SELECT dc_identifier, occurrences, @dangerRank := @dangerRank + 1 AS rank
  FROM (
    SELECT dc_identifier, COUNT(*) AS occurrences
    FROM feed_entries where feed_id = '100,766'
    GROUP BY dc_identifier
    ) tw
  JOIN (
    SELECT @dangerRank := 0
    ) ra
  ) fe
JOIN country_info ci on ci.iso_alpha2=fe.dc_identifier
group by ci.country
ORDER BY rank DESC
LIMIT 10;