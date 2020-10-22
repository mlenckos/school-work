import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

max_postings = 10

url_list = ['https://www.indeed.com/jobs?q=Data+Scientist&l=']
counter = 10
company_list_found_final = []
location_list_found_final = []
title_list_found_final = []
salary_list_found_final = []
education_list_found_final = []
programming_language_list_found_final = []
soft_skills_list_found_final = []
keywords_list_found_final = []
benefits_list_found_final = []
state_list_found_final = []

for counter in range(10,max_postings,10):
    ## URL_test = requests.get('https://www.indeed.com/jobs?q=Data+Scientist&start='+str(counter))
    url_list.append('https://www.indeed.com/jobs?q=Data+Scientist&start='+str(counter))
        
for URL in url_list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='resultsCol')
    job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')
    print("Loaded: ",URL," urls")
    for job_elem in job_elems:
        # Each job_elem is a new BeautifulSoup object.
        # You can use the same methods on it as you did before.
        title_elem = job_elem.find('div', class_='title')
        company_elem = job_elem.find('span', class_='company')
        location_elem = job_elem.find('div', class_='location')
        salary_elem = job_elem.find('span', class_='salaryText')
        getInthere_url = job_elem.find('a').get('href')
        if None in (title_elem, company_elem, location_elem):
            continue

        #Get in there part
        getInThere_actualurl = "https://www.indeed.com"+getInthere_url.strip()
        git_soup = BeautifulSoup(requests.get(str(getInThere_actualurl)).content, 'html.parser')
        #print(getInThere_actualurl)
        results_git = git_soup.find(id='jobDescriptionText')

        # -- Regex List -- 
        education_list = ["Bachelor","Masters","PHD","Associate","Doctorate",'Boot.{,10}Camp']
        programming_language_list =['Python', ' R ', ' SQL ', ' C/+/+ ', ' C ', ' java ', ' javascript ',' matlab ', 'scala', 'swift', 'julia']
        soft_skills_list = ['Presentation',"Leadership",'Communication',"Remote","Team Player","Cross-cultural","Travel",'Flexible','Dependable','Open minded','Conversationalist','Salesperson','Visionary']
        keywords_list = ['Machine Learning','Deep Learning','Artificial Intelligence','Neural Network']
        benefits_list = ['401K','Retirement','Healthcare','Loan Repayment','Dental','Vision']
        state_list = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','Abbreviation:','DC','MH','Abbreviation:','AE','AA','AE','AE','AE','AP']
        # -- Found List -- 

        try:
            company_list_found = [company_elem.text.strip()]
        except:
            company_list_found = []
        try: 
            location_list_found = [location_elem.text.strip()]
        except:
            location_list_found = []
        try:
            title_list_found  = [title_elem.text.strip()]
        except:
            title_list_found = []
        try:
            salary_list_found = [salary_elem.text.strip()]
        except:
            salary_list_found = []
        education_list_found = []
        programming_language_list_found = []
        soft_skills_list_found = []
        keywords_list_found = []
        benefits_list_found = []
        state_list_found = []

        # -- Start adding stuff to found list -- 
        if results_git == None:
            #print("NoneType Object for the url (aka no actual description page)")
            continue
        else:
            for i in education_list:
                if re.search(re.compile(i,re.IGNORECASE),results_git.text):
                    education_list_found.append(i)
            for i in programming_language_list:
                if re.search(re.compile(i,re.IGNORECASE),results_git.text):
                    programming_language_list_found.append(i)
            for i in soft_skills_list:
                if re.search(i,results_git.text):
                    soft_skills_list_found.append(i)
            for i in keywords_list:
                if re.search(i,results_git.text):
                    keywords_list_found.append(i)
            for i in benefits_list:
                if re.search(i,results_git.text):
                    benefits_list_found.append(i)
            for i in state_list:
                if re.search(i,location_elem.text.strip()):
                    state_list_found.append(i)

    # -- Starting printing stuff -- 
        # print("Company: ",company_list_found)
        # print("Location: ", location_list_found)
        # print("Title: ", title_list_found)
        # print("Salary: ", salary_list_found)
        # print("Education: ",education_list_found)
        # print("Programing Languages: ",programming_language_list_found)
        # print("Soft Skills: ",soft_skills_list_found)
        # print("Keywords: ",keywords_list_found)
        # print("Benefits: ",benefits_list_found)
        # print("State: ",state_list_found)
        # print()
        # print()
        try:
            company_list_found_final.append(company_list_found[0])
        except:
            company_list_found_final.append('')
        try:
            location_list_found_final.append(location_list_found[0])
        except:
            location_list_found_final.append('')
        try:
            title_list_found_final.append(title_list_found[0])
        except:
            title_list_found_final.append('')
        try:
            salary_list_found_final.append(salary_list_found[0])
        except:
            salary_list_found_final.append('')
        try:
            education_list_found_final.append(education_list_found)
        except:
            education_list_found_final.append('')
        try:
            programming_language_list_found_final.append(programming_language_list_found)
        except:
            programming_language_list_found_final.append('')
        try:
            soft_skills_list_found_final.append(soft_skills_list_found)
        except:
            soft_skills_list_found_final.append('')
        try:
            keywords_list_found_final.append(keywords_list_found)
        except:
            keywords_list_found_final.append('')
        try:
            benefits_list_found_final.append(benefits_list_found)
        except:
            benefits_list_found_final.append('')
        try:
            state_list_found_final.append(state_list_found[0])
        except:
            state_list_found_final.append('')
        #print(re.findall("degree",results_git.text))
        #job_elem_git = results_git.find('div', class_='jobsearch-JobComponent-description')
        # print("url: https://www.indeed.com"+getInthere_url.strip())
        # git_job_description = job_elem_git.find('span', class_='jobDescriptionText')
        #print(results_git.find("Bachelor"))
        #print(job_elem_git)

big_list = [company_list_found_final,location_list_found_final,title_list_found_final,salary_list_found_final,education_list_found_final,programming_language_list_found_final,soft_skills_list_found_final,keywords_list_found_final,benefits_list_found_final,state_list_found_final]
df = pd.DataFrame(data = big_list).T
df.columns = ["company_list","location","title","salary",'education','programming_languages','soft_skills','keywords','benefits','state']
print(df)
print(url_list)
df.to_csv("output.csv")