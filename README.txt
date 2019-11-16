**********************************************************
COMS 4111 Introduction to Databases
Project 1 Part 3 
Rosemary Torola rlt2140
Catherine Du yd2386
***********************************************************
PSQL account: yd2386 proj1part2
http://35.237.119.141:8111/search
------------------------------------------------------------------------
Files Included:
server.py
templates/
    home.html
    layout.html
    search.html
static/
    dynamic-menu.js
    search.js
 ----------------------------------------------------------------------  
~ CourseMaster ~
The tool to make school cool!
When you're planning your schedule and you're not sure what to take, use CourseMaster!
CourseMaster is a database of Columbia academic information, that can be used to search for courses by professor, department, and professor rating. No matter the search, CourseMaster provides a list of course options. Each listing includes Course names, call numbers, professors, and reviews. In a format that's easy to use when weighing your options, CourseMaster will bring you your best semester yet!

-----------------------------------------------------------------------
Part 1 Proposal Implementation:
CourseMaster successfully implements the preference selection and returning of courses described in the part 1 proposal. The user can search by nugget, department, nugget and department, or by professor. Each search returns course listings that match the searched term(s), in the same format for any search: courses, professors, departments, and course and professor reviews are returned each time. 

The one part of the Part 1 proposal we did not implement is the student login and information storing. We emailed Ashwin the TA about how setting up user login and information storage would present many additional challenges, and Ashwin told us that we did not have to implement this part of the project. 
------------------------------------------------------------------------
Interesting Database Operations:
The first ineteresting database operation is when the user searches for courses by selecting both a department and a nugget. The selected inputs are used in the SQL search for course and professor information in this department with the correct nugget. This search uses nearly every data table in our database to bring all the information together.

The second interesting database operation is when the user searchs for courses only by department. The department selected in the dropdown menu is used to return course and professor information. Since this search isn't filtered only by a specific nugget, returned results are ranked by nugget.
------------------------------------------------------------------------
