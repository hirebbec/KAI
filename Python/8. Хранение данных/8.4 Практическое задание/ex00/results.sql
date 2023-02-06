use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
SELECT name FROM test.store;

-- 3. Посчитать общую сумму в деньгах всех продаж
SELECT SUM(total) FROM test.sale;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
SELECT DISTINCT store_id FROM test.sale;

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
SELECT DISTINCT t1.store_id FROM test.store AS t1
LEFT JOIN test.sale AS t2 ON t1.store_id = t2.store_id
WHERE t2.store_id IS NULL

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
SELECT t3.name, AVG(t3.total / t3.quantity) FROM (SELECT t2.name, t1.total, t1.quantity FROM test.sale AS t1
JOIN test.product AS t2 ON t1.product_id = t2.product_id) as t3
GROUP BY t3.name

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
SELECT name FROM test.product  as t3
JOIN (SELECT t1.product_id, count(t1.store_id) FROM (SELECT product_id, store_id FROM test.sale
GROUP BY product_id, store_id) AS t1
GROUP BY product_id
HAVING COUNT(t1.store_id) = 1) as t2 ON t3.product_id = t2.product_id

-- 8. Получить названия всех складов, с которых продавался только один продукт
SELECT name FROM test.store  as t3
JOIN (SELECT t1.store_id, count(t1.product_id) FROM (SELECT product_id, store_id FROM test.sale
GROUP BY product_id, store_id) AS t1
GROUP BY store_id
HAVING COUNT(t1.product_id) = 1) as t2 ON t3.store_id = t2.store_id

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
SELECT * FROM test.sale
WHERE total = (SELECT MAX(total) FROM test.sale)

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
SELECT date FROM test.sale
GROUP BY date
ORDER BY SUM(total) DESC, date
LIMIT 1
