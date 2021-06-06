print ("Hello, My name is Spartan. I am here to equipt you with helpful resourcess for your battle against epilepsy! Please answer the following questions as yes/no. ")

ans = input('Are you in the US? ')
if ans == "yes"or ans == "no":
    print("""
    Most answers will have relevant sites and numbers for this region. 
    Alternate links will be provided for the UK for cerrtain questions. 
    All of these are great resources regardless of where you are.""") 

ans = input("Have you been recently diagnosed with epilepsy?")
if ans == "yes":
   
    print ("""
    Learn more here
    US- https://www.epilepsy.com/learn/about-epilepsy-basics/what-epilepsy
    UK- https://www.epilepsy.org.uk/info/newly-diagnosed""")
else:
    print("Whether your diagnosis was recent or not, epilepsy unites us!")

ans = input("Has you diagnosis of epilepsy changed your mental health?")
if ans == "yes":
    
    print ("""
    Sorry to hear about that. 
    It's not easy for any of us warriors. Know you are not alone. https://www.health.harvard.edu/newsletter_article/Epilepsy_and_psychiatric_disorders""")
else:
    print("Glad to hear you're doing well!")  

ans = input('Do you feel suicidal? NO information is collected, feel free to be honest.')
if ans == "yes":
    print ("""""
    Please let someone close to you know. 
    If you don't know what to do please call US-1-800-273-8255 or copy this link into your browser-
    US- https://suicidepreventionlifeline.org/           
    UK- https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts, Text SHOUT to 85258 """"")
else:
    print("""Good stuff! Remember if you ever feel suicidal it is important you talk to someone you trust and your healthcare provider.
    Save this to your bookmarks for when your in need- US-1-800-273-8255 or copy this link into your browser- https://suicidepreventionlifeline.org/  
    UK- https://www.nhs.uk/mental-health/feelings-symptoms-behaviours/behaviours/help-for-suicidal-thoughts, Text SHOUT to 85258 """) 

ans = input('Have you checked out any epilepsy organizations? ')
if ans == "no":
    print("""
    Check this out: US-https://www.epilepsy.com, they are a major organization that supports the fight to end epilepsy.
    UK-https://www.epilepsy.org.uk""")
else:
    print(""""
    Check this out: Us- https://www.epilepsy.com/
    UK- https://www.epilepsy.org.uk/, you may or may not be familiar with this foundation- always worth a look!""")      

  
print ("Thank you for chatting with me. Hope I was able to help. See you around!")