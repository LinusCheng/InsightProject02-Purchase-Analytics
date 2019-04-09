# InsightProject02-Purchase-Analytics

## Problem
In this project. We like to know in each department in a store, the numbers of orders people made, the numbers of reorders people made, and the ratios of the two.

## Approach
I use Python 3 to conduct this project.<br>

Firstly, I used a dictionary to map the productID to a list of [ product_name , aisle_id , departmentID ] so that we can access to the departmentID later.<br> Secondly, I read the orders line by line, and count the numbers of products ordered in each department. I have two dictionaries, "count_P" is just to count all the perchases, but "count_P_1" is to count the perchases reordered. After that, I combined the two dictionaries into a list consists of [departmentID, all perchases, reordered perchases, the ratio (reordered/all)].Finally, the data will be generated as a csv file.

