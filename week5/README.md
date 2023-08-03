要求三

SQL CRUD 利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令

● 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/34288bde-6dd7-445a-a7c0-4ce67fcdf991)

● 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/572d45c5-3894-43dd-9cb0-1be14ca0a08e)


● 使用 SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/b5836603-66c8-4a21-8fc7-16bd4e8562b9)


● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/319ab9d6-c7dc-4b3d-849b-8bc0edf98642)

● 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/4d92f95c-d92c-4a02-9d1f-b4858b15acef)

● 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/6b892978-adc3-4e52-8286-b5329fe92ef9)


要求四


利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令:


● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/29587739-d15c-4bf7-8b25-f9054a01e960)

● 取得 member 資料表中，所有會員 follower_count 欄位的總和。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/703d068b-ad50-4a0f-be94-549afdaa6eab)

● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/5885fecd-abde-4e9e-a302-549dfe9bf59a)

要求五

● 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者的姓名。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/3158eda8-5342-4205-b273-fb940db418cb)

● 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者的姓名。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/96d5ca70-f346-40bf-adc8-805274be0258)

● 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。

![image](https://github.com/Angiemou06/WeHelp_FirstStage/assets/59827584/28c4f02c-121a-46b5-8a3d-2ea4cdf8c4b5)





