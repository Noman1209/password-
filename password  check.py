import re
import streamlit as st 

#page styling
st-page-confing(page_title="Password Strength checkByNoman",page_icon="🌘"centered")
 #  custom css
 st.markdown("""
 <style>
       .main {text-align:center}
        .stTextinpit {width:60%!important;margin:
        .stButton button {width: 50 % bacground-color#4CAF50;color:blue;font-18px;}
         .stButton:hover{background-color#45a049;}
                         
            </style>
""",unsafe_allow_html=True) 


#page title and description 
st.title("🔒password Strength Generator")
st.write ("Enter your password below to check its security level.🔍")

# function to check password strength
def check_password_strength(password):
     score = 0
     feedback=[]
     
     if len (password)>=8:
      score +=1#increase score by 1
     else:
            feedback.append(❌Password should be at least 8 characters long**-**)
      if re.search('[a-z]', password)and re. search(r"[a-z]", password):
          score+=1
      else:
           feedback.append("❌Password should  include **both upper case (and lower case latters)**-**)
        
        if re.search (r"\d" , password):
             score +=1
      else:
       feedback.append("❌password should include **at  least one number (0-9)**-**)
       
       # special characters
      
        if re.search(r" [!@#$&*]", password):  
             score +=1
        else:
             feedback-append("❌ include ** at least one number (0-9)**-**
             
  # display password strength results
  if score == 4:
     st.success("✅ **Storng Pasword ** - your password is secure.")  
  elif score ==3:  
       st.info ("⚠️**Moderate Pasword**-consider imporving security by adding more feature ")     
  else: 
       st.error("❌**Week Password**-Follow the suggestion below to strength it")
      
      
     # feedback  
          with st.expander("🔍**"improve Your password**"):
           for item in feedback: 
               st.write (item)
    passwords = st. tex_input ("Enter youre password:",try="pasword",help="Ensure youre password is storong🔒") 
    
    #Button WORKING 
    if st.button("Check Password"):  
       if password :
        check_password_strength(passwords)    
     else: 
            st.waring("⚠️Please enter a password first!")#show warning if pasword empty     
                      
 
               
