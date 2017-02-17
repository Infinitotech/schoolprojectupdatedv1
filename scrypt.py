import os

def get_class_string(file_name):
    final_string = 'class ' + str(file_name).replace('.html','').strip().replace(' ','_') + \
                   '(View):\n\tdef get(self,request):\n\t\treturn render(request,' + "'"+file_name + "')"
    return final_string

def url_code():
    with open('url.txt','w') as file:
        templates_path = os.getcwd() + '/' + 'templates'
        for template in os.listdir(templates_path):
            file.write("url(r'^"+str(template).replace(' ','\s').replace('.html','') + "'," +
                       str(template).replace(' ','_').replace('.html','') + ".as_view()),\n")

if __name__ == '__main__':
    with open('Views.txt','w') as file:
      #  templates_path = os.getcwd() + '/' + 'templates'
       # for template in os.listdir(templates_path):
          #  file.write(get_class_string(template)+"\n")

    #url_code()

