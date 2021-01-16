#!/usr/bin/python

import sys,os
import cgi, cgitb
import urllib.parse
import time
print("Content-type:text/html\r\n\r\n\n")
suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

def main(current_path= str(os.path.dirname(os.path.abspath(__file__))).split('\\')[0]+"/"):
    
    current_path = current_path.replace('\\','/')

    html = ""
    html += "<html>" + "\n"
    
    html += '<head>'
    html += '<meta charset="UTF-8" />'
    html += '<link rel="stylesheet" href="/styles.css">'
    html += '</head>' + "\n"
    
    html += "<body>" + "\n"

    html += "<h4>%s</h4>" %(current_path) + "\n"
    html += '<br/>' + "\n"
    
    #Home button
    html += """
    <form action='main.py?path=' method="POST" >
        <input type="submit" value="Home" />
    </form>
    """ 
    
    #back Button
    html += """   
    <form action="/cgi-bin/main.py" method="GET" >
        <input type="hidden" name="path" value="%s" />
        <input type="submit" value="Back" />
    </form>
    """%(os.path.abspath(current_path+"/..").replace('\\','/'))  
    
    #go to dir button
    html+="""
    <form action='main.py' >
        <input type="text" name="path" placeholder="Enter the path"/>
        <input type = "submit" value = "GO"  />
    </form> 
    """    
    #SystemFileCheckBox
    html += '<input type="checkbox" id="SystemFileCheckBox" checked>hide systemfile</input>'
    
    html += "<hr>"

    html += '<table cellspacing="0" border="0"  id="tblDisplay" cellpading="0">'
    html += "<thead>"
    html += '<tr id="HeaderRow">' 

    html += '<th><input type="checkbox" id="SelectAllBox"/></th>'
    html += "<th></th>"
    html += '<th><b onclick="SortByName()">filename</b></th>'
    html += "<th>&nbsp;</th>"
    html += "<th><b>date modified</b></th>"
    html += "<th>&nbsp;</th>"
    html += "<th><b>size</b></th>"

    html += "</tr>"
    html += "</thead>"
    
    html += "<tbody>"
    html += ""
    for i in os.scandir(current_path):
        info = i.stat()
       
        if(i.name[0] == "$" or 
           i.name[0] == "." or
           i.name.lower().startswith("boot") or
           i.name.lower().endswith(".sys")):
            
            html += '<tr class="ItemTr SystemItem" hidden>'
        else:
            html += '<tr class="ItemTr">'
        html += '<td><input type="checkbox" class="checky" value="%s" name="checkedItem"/></td>'%i.name
        
        if i.is_dir():   #if is folder, won't show size
            html += "<td>&#128193</td>" # Folder icon
            html += '<td><a href="/cgi-bin/main.py?path=%s">%s<a></td>' %(os.path.join(current_path, i.name).replace("\\","/"), i.name) 
            html += "<td>&nbsp;</td>"
            html += "<td> %s </td>" %(time.strftime('%d/%m/%Y %H:%M', time.localtime(info.st_mtime))) 
            html += "<td>&nbsp;</td>"
            html += "<td>&nbsp</td>"
        elif (i.is_file):
            html += "<td>&#128196</td>"   # File icon
            html += '<td><a href="%s">%s</a></td>'%(os.path.join(current_path, i.name).replace("\\","/"), i.name)
            html += "<td>&nbsp;</td>"
            html += "<td> %s </td>" %(time.strftime('%d/%m/%Y %H:%M', time.localtime(info.st_mtime))) 
            html += "<td>&nbsp;</td>"
            html += "<td> %s </td>" %(humansize(info.st_size))

        html += "</tr>"

    html += "</tbody>"

    html += "</table>" + "\n"
    html += '<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>'
    html += '<script  type="text/javascript"  src="/eventhandler.js"></script>'
    html += "<hr>"
    html+="""
    <div >
    <form action="/cgi-bin/editFile.py" target='_blank'>
        <input type="hidden" name="path" class="rename" value="%s" >
        <input type="hidden"   name="editAction" class="rename" value="rename">
        <input type="hidden"   name="selectedfile" id="selectedfile" class="rename" >
        <input type="text"     name="newName" class="rename"  placeholder="Enter a new name" hidden/>
        
        <input type = "submit"  class="rename" id="renameBtn" value = "Rename" hidden/>
    </form>
    """%(current_path)

    html+="""
    <form style="float: left; padding: 5px;">
        <input type = "submit" name="edit" class="delete" id="deleteBtn" value = "Delete" hidden/>
    </form>
    </div>
    """ 
    html += "</body>" + "\n"
    
    
    html += "</html>" + "\n"
    return html


form = cgi.FieldStorage() 
user_path = form.getvalue('path')
newName = form.getvalue('newName')
selectFile = form.getvalue('checkedItem')
editAction = form.getvalue('edit')

if(user_path == None):
    print(main())
elif(editAction == "Rename"):
    if(newName != None):
        currentPath= user_path
        oldName = os.path.join(currentPath, selectFile)
        newName = os.path.join(currentPath, newName)
        os.rename(oldName, newName)
        print(main(user_path))
elif(editAction == "Delete"):
    currentPath = os.path.join(user_path, selectFile)
    if os.path.isdir(currentPath):
        os.rmdir(currentPath)
    else:
        os.remove(currentPath)
    print(main(user_path))
else:
    print(main(user_path))

print()


