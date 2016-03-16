from bs4 import BeautifulSoup
import requests
usn_prefix = "4so15ee"
last_usn = 50
for num in range(1,last_usn + 1):
    if num < 10 :
    	usn = usn_prefix + "00" + str(num)
    elif num<100 :
    	usn = usn_prefix + "0" + str(num)
    else :
    	usn = usn_prefix + str(num)
    	
    link = "http://result.vtu.ac.in/cbcs_results2016.aspx?usn=" + usn
    r = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    student_name = (soup.find(id="txtName")).get('value')
    sgpa = soup.find(id="lblSGPA").b.string
    if student_name :
        print(usn.upper()+" - "+student_name)
        print("      SGPA = " + sgpa + "\n")

        
