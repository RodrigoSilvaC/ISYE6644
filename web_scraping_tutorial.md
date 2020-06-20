# Web scraping

In order to perform the web scraping, we need to install the following
libraries:
* **scrapy** (version 1.6);
* **pylint**; and
* **autopep8**

After that, run a virtual environment (you can run it on the Anaconda
Navigator).

![web_scraping_1](web_scraping_1.png)

After installing the packages, open the terminal in Anaconda Navigator. 

If you enter on the Terminal "scrapy" the Terminal will show several commands: 

![web_scraping_2](web_scraping_2.png)

#### Commands

|Command|What it does|
|--------|-----|
|*bench*     |Run benchmark test to show how fast scrapy can work on your machine   |
|*fetch*     |Fetch (get) the html url of the chosen website **command: fetch (url)**   |
|*genspider*     |This command is used to generate or scaffold a spider using a template   |
|*runspider*     |Create a spider without creating a project     |
|*settings*     |Show default settings    |
|*shell*     |**Important command.** Used to do some experiments with the website before running the spider  |
|*startproject*     |Used to scaffold (set) a project    |
|*version*     |Print scrapy version    |
|*view*     |Open website of your choice on Chrome. Not recommended to use.    |

### Set up project

To set the project, it is recommended to first make a directory in which you're going to save all the project files.
After creating and changing directory, lets create the project with scrapy using
 
 **scrapy startproject [name of the project]**  
 
 ![web_scraping_3](web_scraping_3.png)
 
 The result of this code is that scrapy created two files: 
 1. a file with the name of the project; 
 2. a file named scrapy.cfg

Inside the newly created folder, we have several files 
 
 ![web_scraping_4](web_scraping_4.png)
 
 ### Create a spider

To create a spider, first change directory to the folder you just created with *startproject*. The command to create a spider is: 

**scrapy genspider [how we want to name the spider] [url we want to scrap]**

**IMPORTANT:** When we paste the URL of the website we want to scrap in the code above, remove the last "/", as well as the "http(s)//"

![web_scraping_5](web_scraping_5.png)

![web_scraping_6](web_scraping_6.png)

Now we have a "countries.py" spider on the spiders folder: 

![web_scraping_7](web_scraping_7.png)

### Inside of a spider
If we open the spider we just created, it looks something like this: 

![web_scraping_8](web_scraping_8.png)

As you can see, the spider is a class object. 

|Variable|Meaning|
|--------|-----|
|*name*     |how we named the spider. **IMPORTANT:** A project can have multiple spiders, so it is important to give a unique name to each one of them.   |
|*allowed_domains*     |this variable must contain all the domain names that this spider must be able to access and scrape. **IMPORTANT:** NEVER put the "http(s)://" protocol at the begining of this variable.   |
|*start_urls*     |the URLS the spider will scrape. **IMPORTANT:** scrapy by default sets the protocol as "http://", but if the website you want to scrape uses the https protocol add the "s".   |

Inside the class object, we get a **parse method**. This method parses the response we get back
from the spider.

### how spiders see websites
It is important to know how spiders see websites. They basically see the websites **without** the JavaScript.
To view a website without Javascript:
1. Access on Chrome to the inspect page (CTRL + SHIFT + I)
![web_scraping_14](web_scraping_14.png)
2.  Press (CTRL + SHIFT + P) and type "JavaScript". Choose the second option "Disable JavaScript"
![web_scraping_15](web_scraping_15.png)
3.  Refresh the page
### scrapy shell
The teacher recommended to install the ipython package. (I'm not sure why).

The command to start scrapy shell on the Terminal is: 

**scrappy shell**

![web_scraping_9](web_scraping_9.png)

At the end of the Terminal we can see that this command gave us a list of useful shortcuts we will use commonly.

![web_scraping_10](web_scraping_10.png)

|Shortcut|Meaning|
|--------|-----|
|*fetch(url[, redirect = True])*     ||
|*fetch(req)*     ||
|*shelp*     ||
|*view(response)*     |View a webpage in a browser|

#### method 1 to open a url on the shell: fetch(url)

![web_scraping_11](web_scraping_11.png)

The "GET" we see in the results from using fetch is the type of the request that was sent. 
* 404 is the response status code, meaning that scrapy was not able to find a robots.txt file on the website
* 200 is the response that means scrapy was able fulfill a request for this url. 

#### method 2 to open a url on the shell: constructing a request object

![web_scraping_12](web_scraping_12.png)

If we wanted to obtain the html contents of the webpage we can do it with the command 

**response.body**

![web_scraping_13](web_scraping_13.png)

## Element selection with xpath and css selector
Suppose we want to select the title from the world population by country website.

The first thing we need to do is to disable JavaScript on the browser. 
We do this because scrapy will return raw html markup without JavaScript. So we
in order to see the website like scrapy does, we disable JavaScript.

![web_scraping_16](web_scraping_16.png)
