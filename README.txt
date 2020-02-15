This Application is written in Python using Flask.
----------------------------------------------------------------

Artifact Name :- 

linked-list-api-1.0.zip
---------------------------------------

Minimum System Requirements :-

1. Install Python
2. Install Flask
---------------------------------------

Versions used :-

Python : 3.8.1
Pip : 20.0.2
Flask : 1.1.1
---------------------------------------

How to run :- 

Unzip the contents of the artifact, go to 'src' folder and run the following command : python linkedlistapi.py

-------------------------------------------------------------------------------------------------------------

Assumptions made :-

1.Push functionality : The application allows to add more than one objects (to the specified list) with same 
					   Request Body upon which it will assign a unique "id" to every such object.

2.Remove functionality : In case more than one objects found in the given list that match the Request Body, 
					     the application will remove every such object from the list.
					   
3.An "id" assigned to an object of a list is always incremental irrespective of any operation done on the list.
  For instance, if a list has 3 objects with id = 1, id = 2 and id = 3 and then the objects with id = 2 and id = 3 
  are REMOVED/POPPED, any object PUSHED to the list after this will be assigned id = 4 and so on.
-------------------------------------------------------------------------------------------------------


