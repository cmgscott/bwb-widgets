import GEOparse
import json # used to read JSON from eSearch/eSummary/eFetch requests
import urllib.request # used to read JSON from eSearch/eSummary/eFetch requests
import sys # to access command line arguments
import os # delete files

# these phrases/search terms will be hardcoded (not editable)
URL_STEM_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
URL_STEM_ESUM = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?"
DB_NAME = "db=gds" # geo database name
ID_TYPE = "&idtype=acc" # to retrieve accession data and not just ids (necessary to construct FTP address)
TERM = "&term=" # for search term concat
RET_MODE = "&retmode=json" # to get the information in JSON format

# these search terms will be input boxes (potential search terms)
# note: and/or/not boolean operators are allowed (and must be capitalized, or/not not so)
#       wildcards (*) are allowed
any_field = None # [All fields]
author = None # [Author] * is suppoorted, initials are optional
dataset_type = None #[DataSet Type] dropdown list populated with valid search terms
description = None # [DESC] * is supported
entry_type = None # [Entry Type] dropdown list populated with valid search terms
rec_filter = None # [Filter] dropdown list populated with valid search terms
geo_accession = None # [GEO Accession] valid dataset accession
mesh_terms = None # [MeSH Terms] Medical subject headings terms, * is supported
num_platform_probes = None # [Number of Platform Probes] integer, range is supported
num_samples = None # [Number of Samples] integer, range is supported
organism = None # [Organism] * is supported, must use NCBI taxonomy terms
platform_tech_type = None # [Platform Technology Type] dropdown list populated with valid search terms
project = None # [Project] dropdown list populated with valid search terms
pub_date = None # [Publication Date] format YYYY/MM range is supported
related_platform = None # [Related Platform] must be valid dataset accession
related_series = None # [Related Series] must be valid dataset accession
reporter_id = None # [Reporter Identifier] * is supported
sample_source = None # [Sample Source] * is supported
sample_type = None # [Sample Type] dropdown list populated with valid search terms
sample_val_type = None # [Sample Value Type] dropdown list populated with valid search terms
submitter_inst = None # [Institute]
subset_desc = None # [Subset Description] * is supported
subset_var_type = None # [Subset Variable Type] dropdown list populated with valid search terms
supp_files = None # [Supplementary Files] * is supported
tag_len = None # [Tag Length] integer
title = None # [Title] * is supported
update_date = None # [Update Date] format YYYY/MM range is supported

# edits made 10/07 -------------------------------------------------------------------------------------
searchPhrases = " ".join(sys.argv[1:])
print("splitting search terms and iterating through each one") # print update to console
print("sys args: " + searchPhrases)
flagList = str.split(searchPhrases, "--")
flagList = flagList[1:]
dir = ""
print("number of flag items: " + str(len(flagList))) # print update to console
modifiedSearchPhrase = ""
for flagItem in flagList:
    if (len(flagItem) != 0):
        tempArr = flagItem.split(" ", 1)
        flag = tempArr[0]
        if flag == "genSearch":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + " AND"
        elif flag == "directory":
            print(tempArr[1])
            dir = tempArr[1][:-1]
            dir = dir + '/'
        elif flag == "authors":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Author] AND"
        elif flag == "datasetType": # TODO add fixed list check and print to console if not found/being
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[DataSet Type] AND"
        elif flag == "searchDesc":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[DESC] AND"
        elif flag == "numOfSamps":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Number of Samples] AND"
        elif flag == "org":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Organism] AND"
        elif flag == "accessionID":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[GEO Accession] AND"
        elif flag == "MeSH":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[MeSH Terms] AND"
        elif flag == "platformTech": # TODO add fixed list check and print to console if not found/being ignored
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Platform Technology Type] AND"
        elif flag == "project": # TODO add fixed list check and print to console if not found/being ignored
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Project] AND"
        elif flag == "pubDate": # TODO check format
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Publication Date] AND"
        elif flag == "relSeries":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Related Series] AND"
        elif flag == "relPlat":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Related Platform] AND"
        elif flag == "reporterID":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Reporter Identifier] AND"
        elif flag == "sampleSrc":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Sample Source] AND"
        elif flag == "sampleType": # TODO add fixed list check and print to console if not found/being ignored
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Sample Type] AND"
        elif flag == "sampleValType": # TODO add fixed list check and print to console if not found/being ignored
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Sample Value Type] AND"
        elif flag == "subInst":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Institute] AND"
        elif flag == "subsetDesc":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Subset Description] AND"
        elif flag == "subsetVarType": # TODO add fixed list check and print to console if not found/being ignored
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Subset Variable Type] AND"
        elif flag == "suppFiles":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Supplementary Files] AND"
        elif flag == "tagLen":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Tag Length] AND"
        elif flag == "title":
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Title] AND"
        elif flag == "updateDate": # TODO check date format
            itemsTempArr = str.split(tempArr[1], ", ")
            itemsTempArr = [x for x in itemsTempArr if (x != "" and x != " ")]
            for item in itemsTempArr:
                modifiedSearchPhrase += " " + item + "[Update Date] AND"
        elif flag == "outputFile":
            outputFile = tempArr[1]
        else:
            print("invalid flag: " + flag)

print("string is " + modifiedSearchPhrase[:-4])

# search_term = "diet AND human AND coriobacterineae[Organism] AND attribute name strain[Filter]"

def buildSearchTerm(search_input):
    # build with hardcoded stem
    url_string = URL_STEM_ESEARCH + DB_NAME + ID_TYPE + TERM
    # split string for iterating
    input_list = search_input.split(" ")
    # for each word in search term
        # add "+" between each word
    for word in input_list:
        url_string += word + "+"
    url_string = url_string[:-1] # remove trailing "+"
    url_string += RET_MODE # append JSON request
    return url_string

search_term_formatted = buildSearchTerm(modifiedSearchPhrase)

# download JSON (with help from https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script)
with urllib.request.urlopen(search_term_formatted) as url:
    data = json.loads(url.read().decode())
# printed nicer with the help of https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
# print(json.dumps(json.loads(json.dumps(data)), indent=4, sort_keys=True))

id_list = data["esearchresult"]["idlist"]
# create empty list to store JSONs for each selected id
list_of_sum_jsons = []

for id in id_list:
    esum_url_string = URL_STEM_ESUM + DB_NAME + ID_TYPE + "&id=" + id + RET_MODE
    print(esum_url_string)
    with urllib.request.urlopen(esum_url_string) as url:
        data = json.loads(url.read().decode())
    list_of_sum_jsons.append(data.copy())

tostr = "" + list_of_sum_jsons[0]["result"]["uids"][0]

# empty list to store accession numbers
acc_nums = []

uid_count = 0
for result in list_of_sum_jsons:
    uid = "" + id_list[uid_count] # grab uid for json lookup, store as str
    uid_count += 1
    acc_nums.append(result["result"][uid]["accession"])

print("done searching for datasets")
print("moving on")

os.remove(outputfile)
f=open(outputFile, "w+")
for num in acc_nums:
    f.write(num + "\r\n")
f.close()

print(outputFile)
print("written")
print()
print(dir)
f=open(outputFile, "r")
f1 = f.readlines()
for x in f1:
    print(x)

print("done reading. does it exist?")

# write each as an id in file to be passed to the download widget