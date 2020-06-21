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

#### xpath
In this website, the tag "//h1" is the one which gives us the title. There are cases where the same tag
give us more than one result, and in that case you will need to filter further. 

To get the selector of the title, we use the command: 

**response.xpath("filter used to get the section")**

![web_scraping_17](web_scraping_17.png)

If we want to get only the text and not the markup, we use the expression ***/text()*** in combination with ***.get()***

![web_scraping_18](web_scraping_18.png)

Now, suppose we want to get the names of all the countries. When we select a country name with the browser selector, 
we get the label *//a*.

Here, the problem is that not only the countries have this label, so if we use only this label we will select more values than the countries names.

![web_scraping_21](web_scraping_21.png)

Notice that we want all labels *//a* that are inside the *//td* element. So we change the xpath to ***//td/a*** 

![web_scraping_22](web_scraping_22.png)

Here, because we are selecting more than one text, we need to use the method ***.getall()***

#### css selector

To get the selector of the title, we use the command: 

**response.css("filter used to get the section")**

![web_scraping_19](web_scraping_19.png)

to get the text, we also use the ***.get()*** method

![web_scraping_20](web_scraping_20.png)

### modifying the spider 
After looking at the website with scrapy shell, we now proceed to modify the spider named countries that we created before.

We modify the parse method inside the spider, with the xpath selectors we got previously

![web_scraping_23](web_scraping_23.png)

In scrapy, if you want to return the data, you need to return it as a dictionary. That is why we use the **yield**
function with the dictionary format.

![web_scraping_24](web_scraping_24.png)

**IMPORTANT:** to execute the spider, you need to make sure you are on the same level as the "scrapy.cfg" file

![web_scraping_25](web_scraping_25.png)

Now, to execute the spider, on the Terminal you write the command

**scrapy crawl (name of spider previously created)**

![web_scraping_26](web_scraping_26.png)

### modifying the spider PT.2  
lets modify more the parse method of the spider. 

First, lets stop scraping the title. Then, for the countries variable we previously obtained only the text of the xpath
selector used. However, if we go to the website

![web_scraping_27](web_scraping_27.png)

We can see that from the *a* element we can scrape the *a* element and then we can obtain the name by 
extracting the text content of that element as shown before. 

So, instead of extracting only the text, now we modify the selector to only *//td/a*, in order to extract
the href element and the text element.

![web_scraping_28](web_scraping_28.png)

If we leave the countries response xpath, we will get a list of select objects, which will represent each a node.

![web_scraping_29](web_scraping_29.png)

Each selector objects on the list, have a data attribute that represents the full *a* element.

**Since each country is a selected object, we can execute an xpath expression against it**

![web_scraping_30](web_scraping_30.png)

**IMPORTANT RULE:** When we are executing an xpath expression against a selected object, we ALWAYS start with
"***.//***".

Saving and executing the spider gives us: 

![web_scraping_31](web_scraping_31.png)

As we can see, now we have a dictionary with the info from each country of: 
* name; and 
* link of the country's website

### modifying the spider PT.3

Now, we want to access the website saved on the spider as the variable "link".

Previously we learned to use the fetch command from scrapy. However, we cannot use fetch inside the spiders.

Instead, we will use the **Request** method

![web_scraping_32](web_scraping_32.png)

**IMPORTANT:** We need to add either the *http* or *https*, because if we don't add either of them, we will get the error **Missing scheme** 

![web_scraping_33](web_scraping_33.png)

We can add the absolute url in several ways: 

Pasting the absolute url as string:
![web_scraping_34](web_scraping_34.png)

Using the function *.urljoin()*:
![web_scraping_35](web_scraping_35.png)

Using *response.follow* with the relative url link:
![web_scraping_36](web_scraping_36.png)

Now, we need to catch every country response and parse it. For this, we need to define another method: 

![web_scraping_37](web_scraping_37.png)

With the callback option inside the response.follow method, when scrapy sends a request to each country link, 
the reponse will be sent to the parse_country method. 

In the example we also used the logging library to show a mini log of every request. 

Now, we want to get the population from each year that is located inside the country's website.

![web_scraping_38](web_scraping_38.png)

To select the table, we use the xpath:

**(//table[@class = 'table table-striped table-bordered table-hover table-condensed table-list'])[1]**

![web_scraping_39](web_scraping_39.png)

On the xpath, we used the "[1]" argument to get only the first table.

Now, we want to select from the table the population: 

**(//table[@class = 'table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr**

We now get 18 elements. We put the xpath into the spider, inside the parse_country method: 

![web_scraping_40](web_scraping_40.png)

![web_scraping_41](web_scraping_41.png)


On the new parse_country method:

* First, we got the rows with the xpath selector that we previously obtained. **year is the first *td* element**; 
* Then, we run a loop through the response to get the year and population **the population is in the second td element, inside a strong element**

Note that we don't have the country name variable assigned in the parse_country method. To sync the data between two parse methods, 
we have to use a **request meta**. 

![web_scraping_42](web_scraping_42.png)

The request meta is simply a dictionary, which you create inside the parse method with the variable you want to sync, and then call it
on the other parse method using the *response.request.meta* method.
 
### Building the dataset
Scrapy allow us to export the data in many formats, including *.json*, *.csv* and *.xml* formats. 

To export the data, simply go to the terminal and write the command: 

***scrapy crawl (name of the spider) -o (name and format of the exported file)***

![web_scraping_43](web_scraping_43.png)

### Dealing with multiple pages
For our example, we are going to scrape the website www.tinydeal.com

![web_scraping_44](web_scraping_44.png)

First, we will need to do the usual steps in scraping with scrapy: 

1. Check restrictions of the website in the robots.txt file
![web_scraping_45](web_scraping_45.png)
2. Disable JavaScript on the browser, to see the website like a spider do
3. Copy website URL and go to Anaconda Prompt to create a new project
![web_scraping_46](web_scraping_46.png)
4. Move to the project's name folder (in this case is the tinydeal folder) and create a spider
![web_scraping_47](web_scraping_47.png)
5. Go to VSCode and open the folder
6. Inside the spider we just created: 
    * Modify the allowed domains by deleting the "/specials.html"
    ![web_scraping_48](web_scraping_48.png)
    ![web_scraping_49](web_scraping_49.png)
    * Change the http protocol to https inside the start_urls variable
    ![web_scraping_50](web_scraping_50.png)

Now, we will scrap the contents of the first page: 
![web_scraping_50](web_scraping_50.png)

Notice that when we get the dataset, the file doesn't have an encoding, so we need to fix this
![web_scraping_51](web_scraping_51.png)

To set the encoding, we go to the ***settings.py*** file and write: 

***FEED_EXPORT_ENCODING = 'utif-8'***

![web_scraping_52](web_scraping_52.png)

Finally, the next step is to deal with the pagination
![web_scraping_53](web_scraping_53.png)

