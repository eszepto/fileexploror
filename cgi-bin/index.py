import sys,os
print("Content-type:text/html\r\n\r\n")
prev_path = os.path.abspath("../")
def main(current_path=os.getcwd()):
    html = ""

    html += "<html>" + "\n"
    html += "<head></head>" + "\n"
    html += "<body>" + "\n"

    html += "<h1>%s</h1>" %(current_path) + "\n"
    html += '<br/>' + "\n"
    
    for i in os.listdir(current_path):
        html += '<a href="../%s">%s</a>' %(i,i) + "\n"
        html += '<br/>' + "\n"
    

    html += "</body>" + "\n"
    html += "</html>" + "\n"
 
    return html
    

print(main())
