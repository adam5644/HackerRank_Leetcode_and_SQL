SELECT W1.id
FROM Weather W1, Weather W2
WHERE W1.recordDate = W2.recordDate + 1
AND W1.temperature > W2.temperature;