dic=eval(input())
annual_income=eval(input())
if dic["INCOME"]== "low":
    base_tax_rate=10/100
elif dic["INCOME"]== "middle":
    base_tax_rate=20/100
else:
    base_tax_rate=30/100       
base_tax= annual_income*base_tax_rate 

child_number=len(dic["CHILD"]) 
if dic["MARITAL_STATUS"]=="married":
    base_tax -= 500 + (300 *child_number)
elif dic["MARITAL_STATUS"]=="single_parent":
    base_tax -= 600 * child_number
  
age_below=len(list(filter(lambda x: x < 18, dic["CHILD"])))
base_tax -= 200 * age_below
if dic["SPECIAL_NEEDS"]==True:
    base_tax -= 1000
if dic["ELDERLY_CARE"]==True:
    base_tax -= 800
  
if dic["CITY_CATEGORY"]=="suburban":
    base_tax -= 200
elif dic["CITY_CATEGORY"]=="rural":  
    base_tax -= 400

if dic["EDUCATION"]==True:
    base_tax -= 500    
if dic["HEALTHCARE"]==True:
    base_tax -= 750   
if dic["GREEN_INITIATIVES"]== True:
    base_tax -= 300        
if dic ["PROPERTY_STATUS"] == "rents":
     base_tax -= 300 
   
if dic["TAXPAYER_DURATION"]== "regular":
    final_base_tax= base_tax *0.95
elif dic["TAXPAYER_DURATION"]== "long_term":
    final_base_tax= base_tax *0.90
else:
    final_base_tax=base_tax
    
final_base_tax = max(0, final_base_tax)
  
print("%.2f" % final_base_tax)   

