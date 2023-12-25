SELECT id
FROM your_table utb
WHERE utb.status = 'standard'
AND utb.collected_modified_on >= DATEADD(day, -1, GETDATE())