# Sales-and-Operations-Planning-Project

## By Sharonne Kemboi

### User Story

> This is Python program that asks the user to enter the following data: 

* An initial stock level for a product 

* The number of month(s) to plan 

* The planned sales quantity for each month 

> Based on this data, calculate the required production quantity as follows: 

* If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0 

* If the sales quantity is larger than the stock level of the previous month, the production quantity is this difference 

## Sample Output :

> Below is an example execution of the program: 

* Please enter an initial stock level: 500

* Please Enter The Planning Horizon: 5

* Please Enter The Forecasted Sale For Month 1: 300 

* Please Enter The Forecasted Sale For Month 2: 250 

* Please Enter The Forecasted Sale For Month 3: 200 

* Please Enter The Forecasted Sale For Month 4: 400 

* Please Enter The Forecasted Sale For Month 5: 100 

> The resulting production quantities are: 

* Production quantity month 1 - 0 

* Production quantity month 2 - 50 

* Production quantity month 3 - 200 

* Production quantity month 4 - 400 

* Production quantity month 5 - 100 

 
## Explanation:
> Why are those production quantities calculated? 
<p> The initial stock level is 500. In the first month 300 pieces are sold. Therefore, nothing needs to be produced and the resulting stock is 200 (= 500 - 300). </p>
<p> In the second month 250 pieces are sold. The stock level after the previous month is 200. Therefore 50 pieces need to be produced. The resulting stock level is 0 (= 200 + 50 - 250).</p>
<p> In the third month 200 pieces are sold. The stock level after the previous month is 0. Therefore 200 pieces need to be produced. The resulting stock level is 0 (= 200 - 200). </p>


## License

> [The Unlicense](license) this application's source code is free for any open source projects

> Copyright (c) 2022 **Sharonne Kemboi**



## Authors information
> Feel free to add your contribution to the code.

> If you have any questions,comments or advice,feel free to contact me

* [Email](sharonnekay23@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/sharonne-vanessa-kemboi-a118bb135)