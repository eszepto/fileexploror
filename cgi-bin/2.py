import sys,os
import cgi, cgitb
print("Content-type:text/html\r\n\r\n\n")
form = cgi.FieldStorage() 
user_path = form.getvalue('path')

prev_path = os.path.abspath("../")

def main(current_path=os.getcwd()):
    
    current_path = current_path.replace('\\','/')
    
    html = ""

    html += "<html>" + "\n"
    html += "<head></head>" + "\n"
    html += "<body>" + "\n"

    html += "<h1>%s</h1>" %(current_path) + "\n"
    html += '<br/>' + "\n"
    
    html+="""
    <form action=/cgi-bin/2.py  >

    <input type="text" name="path"/>
    
    <input type = "submit" value = "GO" />

    </form>

    """
    html += """
    
    <form action=/cgi-bin/2.py  >

    <input type="submit" value="<"/>

    </form>
    """

    for i in os.listdir(current_path):
        html += '<a href="/%s">%s</a>' %(i,i) + "\n"
        html += '<br/>' + "\n"
    

    html += "</body>" + "\n"
    html += "</html>" + "\n"
 
    return html
    
if(user_path == None):
    print(main())
else:
    print(user_path)
    print(main(user_path))


def GetPrevPath(current_path):
    current_path = str(current_path).split('/')
    pass
    return

