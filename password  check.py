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
                      
 
               
