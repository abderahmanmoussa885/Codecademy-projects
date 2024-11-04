SELECT title, score
FROM hacker_news
ORDER BY score DESC limit 5;
select sum(score) from hacker_news;
select user , sum(score) from hacker_news
group by user
having sum(score)>200
order by 2 desc;
select (517+309+304+282)/6366.0;
select user , count(*) from hacker_news where url like "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
Group by user
order by count(*) DESC;
SELECT CASE
   WHEN url LIKE '%github.com%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source',
  count(*)
FROM hacker_news
GROUP BY 1;
SELECT timestamp
FROM hacker_news
LIMIT 10;
SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;
SELECT strftime ("%H",timestamp) AS "HOURS" ,
       ROUND(AVG(score),2) AS "SCORE AVERAGE",
       COUNT(*) AS "NUMBER OF STORIES"
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 2 desc;




