DELETE FROM "Crawler_tagspostagens" WHERE ctid NOT IN(
SELECT max(ctid) FROM "Crawler_tagspostagens" AS tags GROUP BY tags.fk_postagem_id, fk_tag_id);