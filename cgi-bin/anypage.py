import sys,os
import cgi, cgitb
import urllib.parse
print("Content-type:text/html\r\n\r\n\n")
form = cgi.FieldStorage() 
user_path = form.getvalue('path')


def GetPrevPath(current_path):
    return current_path[::-1].split('/',maxsplit=1)[1][::-1]
def main(current_path="C:/"):
    
    current_path = current_path.replace('\\','/')
    
    html = ""

    html += "<html>" + "\n"
    html += "<head></head>" + "\n"
    html += "<body>" + "\n"

    html += "<h1>%s</h1>" %(current_path) + "\n"
    html += '<br/>' + "\n"
    
    html+="""
    <form action=/cgi-bin/main.py  >

    <input type="text" name="path"/>
    
    <input type = "submit" value = "GO"  />

    </form>

    """
    prev_path = GetPrevPath(current_path)
    if (prev_path == "C:/"):
        html += """
        
        <form action=/cgi-bin/anypage.py?path=%s>

        <input type="submit" value="<" />

        </form>
        """ %(prev_path)
    else:
        html += """
        
        <form action=/cgi-bin/main.py >

        <input type="submit" value="<" />

        </form>
        """ 
        

    for i in os.listdir(current_path):
        html += '<a href="/cgi-bin/main.py?path=%s"> %s </a>' %(current_path+"/"+i, i) + "\n"
        html += '<br/>' + "\n"
    

    html += "</body>" + "\n"
    html += "</html>" + "\n"
 
    return html
    
if(user_path == None):
    print(main())
else:
    print(user_path)
    print(main(user_path))



    
