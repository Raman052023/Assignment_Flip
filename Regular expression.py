#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re


# In[3]:


for i in dir(re):
    print(i,end=",")


# In[4]:


2^1


# In[5]:


2^2


# In[6]:


2^3


# In[7]:


2^4


# In[8]:


1^1


# In[9]:


string1="Hellow Data bB science 1"
x=re.findall("[abc]",string1)
print(x)


# In[10]:


string1="Hellow Data Science"
x=re.findall("[a-m]",string1)
print(x)


# In[11]:


string1="Hellow Data science 1"
x=re.findall("[^f-p]",string1)
print(x)


# In[12]:


import re
pattern = "Data Science"
text = "Data Science is a stream and it is a part of AI.You can solave many complex problems using Data Science tools and techs"

matches = re.findall(pattern,text)
print(matches)


# In[13]:


pattern = "Data Science|stream|tools|AI"
text = "Data Science is a stream and it is a part of AI.You can solave many complex problems using Data Science tools and techs"

matches = re.findall(pattern,text)
print(matches)


# In[14]:


pattern="\d"
text="There are 123 apples and 456 oranges."
matches=re.findall(pattern,text)
print(matches)


# In[15]:


pattern="\d+"
text="There are 123 apples and 456 oranges."
matches=re.findall(pattern,text)
print(matches)


# In[16]:


pattern="\D"
text="There are 123 apples and 456 oranges."
matches=re.findall(pattern,text)
print(matches)


# In[17]:


pattern="\D+"
text="There are 123 apples and 456 oranges."
matches=re.findall(pattern,text)
print(matches)


# In[18]:


pattern="[0-9]"
text="There are 123 apples and 456 oranges."
matches=re.findall(pattern,text)
print(matches)


# In[19]:


pattern="[0-9]+"
text="There are 123 apples and 456 oranges."
matches=re.findall(pattern,text)
print(matches)


# In[20]:


pattern="[0-9]+"
text="acbd01234xyz_01"
matches=re.findall(pattern,text)
print(matches)


# In[21]:


pattern="[0-9]"
text="acbd01234xyz_01"
matches=re.findall(pattern,text)
print(matches)


# In[22]:


pattern="[0-9]"
matches=re.findall(pattern,"acbd01234xyz_01")
print(matches)


# In[23]:


#Extracting digits from a list of string
price=["Apple cost rs 50","Rs 60 for each pineaple 120","Rs 150 per watermelon"]
for msg in price:
    matches=re.findall("\d+",msg)
    print(matches)


# In[24]:


target_string="APJ Abdul Kalam was an indian aerospace scientist also known as the missile man of India"
result=re.findall(r"\w{6}",target_string)

print("Match object:",result)


# In[25]:


target_string="APJ Abdul Kalam was an indian aeros123pace scientist also known as the missile man of India"
result=re.findall(r"\w{6}",target_string)

print("Match object:",result)


# In[26]:


target_string="APJ Abdul Kalam was an indian aeros123pace scientist also known as the missile man of India"
result=re.findall(r"\w{4,6}",target_string)

print("Match object:",result)


# {m,n}-m to n times
# {1,3-} occurance between 1 to 3only
# {4}-occurance of 4 only

# A[a-zA-Z]+J=any string starting A and end with J,in between anything can be present , anything means-a to z or A TO Z

# In[27]:


string="APj Abdul Kalam was an indian aeros123pace scientist also known as the missile man of India"
pattern="A[a-zA-Z]+j|A[\w]+l"
result=re.findall(pattern,string)

print(result)


# In[28]:


string="APj Abdul Kalam was an indian aeros123pace scientist also known as the missile man of India Abdu123_l"
pattern="A[a-zA-Z]+J|A[\w]+l"
result=re.findall(pattern,string)

print(result)


# In[29]:


import re
string="AP123 Abdul2_1 Kalam was an indian aeros123pace scientist also known as the missile man of India"
pattern='A[a-zA-Z0-9]+J|A[\w]+l'
result= re.findall(pattern,string)
print(result)


# In[30]:


string="twelve:12 Eighty nine:89."
pattern="\d+"
result=re.split(pattern,string)
print(result)


# In[ ]:





# In[31]:


# split at each white space character (\s is split by space)

text="India is beautiful country"
x=re.split("\s",text)
print(x)


# In[32]:


split_by_position="How is this possible"
x=re.split("\s",split_by_position,2)
print(x)


# # Limit the number of split

# In[33]:


target_string = "12-45+78"
y = re.split(r"\D",target_string,maxsplit=1)

print(y)


# In[34]:


string="12-45+78_75-36"
x=re.split(r"\D",string,maxsplit=2)
print(x)


# # Sub

# In[35]:


#syntax=re.sub(pattern,replacement,string,flag)


# In[36]:


y="Rs"
text="This item cost Rs 2500 and rS 3000"
replaced=re.sub(y,"$",text)
print(replaced)


# In[37]:


a="Rs"
text="This item cost Rs 2500 and Rs 3000"
replaced=re.sub(a,"$",text)
print(replaced)


# In[38]:


y="Rs"
text="This item cost Rs 2500 and rS 3000"
replaced=re.sub(y,"$",text,flags=re.IGNORECASE)
print(replaced)


# In[39]:


target_string="  APJ    Abdul kalam was an   indian aerospace scientist also known as the missile man of India"

res_str =re.sub(r"\s+", "", target_string)   #removing all spaces,including single and multiple spaces(pattern to remove "\s+") 
print(res_str)


# In[40]:


STR="  APJ    Abdul kalam was an   indian aerospace scientist also known as the missile man of India"
x=re.sub(r"\s+", "",STR)
print(x)


# In[41]:


str="APJ abdul kalam was an indian aerospace scientist also known as the missile man of india"
print(str)


str="APJ abdul kalam was an indian aerospace scientist also known as the missile man of india"
y = re.sub(r"\s+$", "",str)  #removing trailing spaces
print(y)


# In[42]:


str="APJ abdul kalam was an indian aerospace scientist also known as the missile man of India"
y = re.sub(r"India$", "",str)  #removing trailing spaces
print(y)


# In[43]:


# try to substitute:re.sub(regexStr,replacement, instr)   -> outstr
substitute=re.sub(r"[0-9]+",r"*","abc0123xyz01_456")


# In[44]:


target_string="  APJ Abdul Kalam was an indian aerospace scientist also known as the missile man of india  "
print(target_string)

x=re.sub(r"^\s+","",target_string)
print(x)


# In[45]:


result=re.sub(r"notes","projects","kagle is the place to data science notes")
print(result)


# # subn()
# 

# This method is smilar to sub() method and used to find a substring where a regex pattern is matches,and then it replaces
# the matched substring with a different string along with different string along with the number of replacements.
# 

# In[46]:


substitute_and_count=re.subn(r"[0-9]+",r"*","abcd123azxs_32_a_09")
print(substitute_and_count)


# # Match object

# In[47]:


string="Virat is a cricket player who was born on november 5  1988"
result=re.match(r"\d{4}",string)
print(result)


# In[48]:


string="1988 Virat is a cricket player who was born on november 5"
result=re.match(r"\d{4}",string)
print(result)


# In[49]:


string="123 abc is an alphanumeric number "
y=re.match(r"\w$",string)
print(y)


# In[50]:


string = "abc is an alphanumeric number 123abc"
result = re.match("\w$",string)
print (result)


# In[51]:


target="123abc is an alphanumeric number"
y=re.match("^\w.+",target)
print(y)


# In[52]:


import regex as re 
msges =["Bananas are very delecious pieces of fruit",
        "They are also super healthy.",
        "Eating two bananas a day can do womders for your health",
        "for example.but for you ever think of sticking of needle into a banana? probaly not,",
       "but you should ,because it is super handy" ]
for msg in msges:
    search=re.search("banana",msg)
    print(search)


# In[53]:


msg="This product is really Great"
search=re.search("^This.*Great$",msg)
print(search)


# In[54]:


msg="this product is really great"
x=re.search("^.*$",msg)
print(x)


# In[55]:


msg="this product is really great"
x=re.search("^this.*$",msg)
print(x)


# In[56]:


import re
target_string= "Emma is a basketball player who was born in 1993.she played 112 matches with a scoring average of 26.12 points per game.Her weight is 51"
string_pattern=r"\d{4}"
regex_pattern=re.compile(string_pattern)
print(type(regex_pattern),"\n")
result = regex_pattern.findall(target_string)
print(result)


# In[57]:


target_string="APJ Abdul Kalam was an indian aeros123pace scientist also known as the missile man of India"
result=re.search(r"\w{6}",target_string)
print("Match object:",result)
print("Match value: ",result.group())


# In[58]:


superRegex=re.compile(r"super(wo)*man")
match_obj1=superRegex.search("The adventure of superman")
match_obj1.group()


# In[59]:


superRegex=re.compile(r"super(wo)*man")
match=superRegex.search("the adventure of superwoman")
match.group()


# In[60]:


msg="if Eating two bananas a day can do wonders for your hEarth"
x=re.search(r"Ea(?=t)",msg)
print(x)


# In[61]:


target="APJ Abdul kalam was an Indian aerospace scientist also known as Missile Missile2 Man of India"
x=re.search(r"\w{6}",target)
print("Match object:",result)
print("Match value:",result.group())


# In[62]:


result=re.search(r"\bMissile\b",target)
print(result)
print(result.group())


# In[63]:


import re
string="Emma is a basketball player who was born in 1993.she played 112 matches with a scoring average of 26.12 points per game.Her weight is 51"
result=re.finditer(r"player|played",string)
for match_object in result:
    print(match_object)
    print(match_object.group())


# In[64]:


import re


# In[65]:


import re
with open("/content/url_related.txt") as file:
    for line in file:
        url=re.findall("https?://(?:[-\w.]|(?:%[\da-zA-Z0-9]{2}))+",line)
        print(url)


# In[ ]:


import pandas as pd
df=pd.DataFrame({"city":["New york","parague","new delhi","venice","new orlence"],
                 "Event":["Music","Poetry","Theatre","Comedy","Tech_summit"],
                 "cost":[10000,5000,15000,2000,12000]})
df                 


# In[ ]:


df["city"].str.contains("^N.*",case=True)


# In[ ]:


df["city"].str.contains("^N.*",case=False)


# In[ ]:


df=pd.read_csv("https://raw.githubusercontent.com/dsrscientist/dataset1/master/titanic_train.csv")
df


# In[ ]:


pattern = r"c\.?A\.?"
mask = df["Ticket"].str.contains(pattern)
df[mask].head(500)


# In[ ]:


df["Name"].sample(5)


# In[ ]:


pattern="\s(\w+)\."
all_ts=df["Name"].str.extract(pattern,expand=False)
unique_ts=all_ts.value_counts()


# In[ ]:


unique_ts


# In[ ]:


pat=r"(\w+),\s(\w+\.\s\w+.*)"
df_names=df["Names"].str.extract(pat,flags=re.I)
df_Names


# In[ ]:


a(b*)


# In[ ]:


sentence="abb news is publishing"
pattern="b*"
result=(pattern,sentence)
print(result)


# In[ ]:


import re

def remove_words_between_length(text):
    pattern = re.compile(r'\b\w{2,4}\b')
    result = re.sub(pattern, '', text)
    return result

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

result_text = remove_words_between_length(sample_text)
print(result_text)


# In[ ]:




