# pi-stress-test
Calculating Pi using Madhava-Leibniz Series

Pi can be calculated in many ways but I personally really like the Madhava-Leibniz series calculation which is the expansion of the expression pi = arctan(1) using a Taylor Series. As with all infinite series, more terms make the final calculation more accurate to the exact value of pi however that comes at a computation cost, especially with multiple instances of the same calculation. 
Hence, I have attempted to create a stress test to see how fast a computer can calculate pi to 100000000 terms with (n) instances of the calculation running at the same time. (n) is a variable and should be adjusted depending on the test hardware. 
 
Start from 5 instances and increase until your CPU hits 100% utilisation (use hardware monitors to see utilisation) and then let the script run and eventually output time taken for each instance of the program to finish the calculation. Refer to test-results.md for some reference and if you end up testing hardware, I implore you to try and add that data to the file so that the database is more populated and thus, of more use, to others. 

To execute the program, put both files in the same folder and then use commmand prompt to execute pistress.py and type in number of instances as per your requirement. 

Do not run an exceptionally high number of instances and I am not responsible for any damaged hardware that you end up with if you choose to run this script. 

Thanks!
