from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq 
from googletrans import Translator
import json,re

def Scraper(url):
    page_url = url
    # page_url="https://www.espncricinfo.com/player/isuru-udana-328026"

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    details ={}

    #Name
    name = page_soup.findAll("h2")
    if name =="":
        name = " "
    else:
        name=name[0].text.strip()
        name_en=name
        name_si=Translate(name)

    #country
    country =page_soup.findAll(class_= "player-card__country-name")
    if country =="":
        country =" "
    else:
        country=country[0].text.strip()
        country=Translate(country)

    #Full name, date of birth, playing role, batting style, bowling style
    overviews = page_soup.findAll(class_= "text-uppercase gray-700 mb-0 pb-0-5 player-card-heading")
    containers = page_soup.findAll(class_= "player-card-description gray-900")
    label_list=[]
    for overview in overviews:
        label_list.append(overview.text.strip())


    if "Full Name" in label_list:
        full_name=containers[label_list.index("Full Name")].text.strip() 
        full_name = Translate(full_name)
    else:
        full_name=" "

    if "Born" in label_list:
        date_of_birth = containers[label_list.index("Born")].text.strip()
        date_of_birth = Translate(date_of_birth)
    else:
        date_of_birth=" "

    if "Playing Role" in label_list:
        playing_role = containers[label_list.index("Playing Role")].text.strip() 
        playing_role = Translate(playing_role)
    else:
        playing_role=" "

    if "Batting Style" in label_list:
        bating_style = containers[label_list.index("Batting Style")].text.strip()
        bating_style =Translate(bating_style)
    else:
        bating_style=" "

    if "Bowling Style" in label_list:
        bowling_style = containers[label_list.index("Bowling Style")].text.strip()
        bowling_style = Translate(bowling_style)
    else:
        bowling_style=" "

    #Teams
    Teams =page_soup.findAll(class_= "m-0 ml-2 link-border-bottom player-description-link")
    if Teams =="":
        teams=" "
    else:
        teams=""
        for team in Teams:
            team=team.text.strip()
            teams = teams+team+","
        teams=Translate(teams)

    #Profile
    profile = page_soup.findAll(class_= "more-content-gradient-content")
    if profile =="":
        profile=" "
    else:
        profile = profile[0].text.strip()
        profile=Translate(profile)

    # print("Name: " + name + "\n")
    # print("Full name: " + full_name + "\n")
    # print("Country: " + country + "\n")
    # print("Date of Birth: " + date_of_birth + "\n")
    # print("Playing Role: " + playing_role + "\n")
    # print("Batting Style: " + bating_style + "\n")
    # print("Bowling Style: " + bowling_style + "\n")
    # print("Teams: " + teams + "\n")
    # print("Profile: " + profile + "\n")
    details["Name_En"]=name_en
    details["Name_si"]=name_si
    details["Full Name"]=full_name
    details["Country"]=country
    details["Date of Birth"]=date_of_birth
    details["Playing Role"]=playing_role
    details["Batting Style"]=bating_style
    details["Bowling Style"]=bowling_style
    details["Teams"] = teams
    details["Profile"]=profile
    # details_str="Name_En : "+ name_en + ", " +"Name_Si : "+name_si + ", " + "Full Name : "+full_name + ", " + "Country : "+country + ", "+"Date of Birth : "+date_of_birth+", "+"Playing Role : "+playing_role+", "+"Batting Style : "+bating_style+", "+"Bowling Style : "+bowling_style+", "+"Teams : "+teams+", "+"Profile : "+profile+"\n"
    print(details)
    return details

def Translate(word):
    translator = Translator()
    translation = translator.translate(word,dest='si')
    return translation.text
   
def trans_jon(details):
    # file1 = open('cricketers_si.txt', 'r',encoding='utf-8')
    # #  
    # Lines = file1.readlines()
    # for line in Lines:
    #     print(line)
    with open ('cricketers_corpus/cricketers.json','a') as f:
        f.write(json.dumps(details))

def Cricketers_sinhala():
    file1 = open('cricketers_corpus/cricketers_link.csv', 'r')
    #  
    Lines = file1.readlines()
    for line in Lines:
        details=Scraper(line)
        trans_jon(details)  
        out_filename = "cricketers2.txt"
        f = open(out_filename, "a",encoding='utf-8')
        f.write(str(details))
        f.close()
    # with open ('cricketers_corups/cricketers.json','w+') as f:
    #     f.write(json.dumps(details))

Cricketers_sinhala()
# trans_jon()