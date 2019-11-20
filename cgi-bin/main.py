import sys,os
import cgi, cgitb
import urllib.parse
print("Content-type:text/html\r\n\r\n\n")

form = cgi.FieldStorage() 
user_path = form.getvalue('path')


def main(current_path= str(os.path.dirname(os.path.abspath(__file__))).split('\\')[0]+"/"):
    
    current_path = current_path.replace('\\','/')

    html = ""
    html += "<html>" + "\n"
    html += "<head></head>" + "\n"
    html += "<body>" + "\n"

    html += "<h1>%s</h1>" %(current_path) + "\n"
    html += '<br/>' + "\n"
    
    html+="""
    <form action=/cgi-bin/main.py >

        <input type="text" name="path"/>
    
        <input type = "submit" value = "GO"  />

    </form> 

    """
    
    html += """
    
    <form action=/cgi-bin/main.py method="POST" >

        <input type="submit" value="Root" />

    </form>


    """

    html += """
    
    <form action=/cgi-bin/main.py?path=%s  >

        <input type="submit" value="<" />

    </form>


    """%(os.path.abspath(current_path+"/.."))
    
    if(current_path[-1] != "/"):
        for i in os.listdir(current_path):
            
            html += '<a href="/cgi-bin/main.py?path=%s"> %s </a>' %(current_path+"/"+i, i) + "\n"
            html += '<br/>' + "\n"
    else:
        for i in os.listdir(current_path):
            
            html += '<a href="/cgi-bin/main.py?path=%s"> %s </a>' %(current_path+i, i) + "\n"
            html += '<br/>' + "\n"
    

    html += "</body>" + "\n"
    html += "</html>" + "\n"
 
    return html
    
if(user_path == None):
    print(main())
else:
    print(main(user_path))

print()

