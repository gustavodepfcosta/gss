
def html_generator(subject_name, subject_teacher, subject_year, formulary):

    html = f"""{{% load bootstrap4 %}}
    {{% load static %}}
    <DOCTYPE3 html>
        <html lang="en-us">
            <head>
                <meta charset="UTF-8">
                <title>
                    {subject_name} of year {subject_year} Manager
                </title>
                {{% bootstrap_css %}}
                <link rel="stylesheet" href="{{% static 'css/style.css' %}}">

            </head>
            <body>
                <header>
                    <nav id="professors" class="navbar navbar-dark bg-primary">
                        <a class="navbar-brand" href="{{% url 'index.html' %}}">Home Page</a>
                        <a class="navbar-brand" href="{{% url 'enrollments.html' %}}">Enrollments</a>
                        <a class="navbar-brand" href="{{% url 'registrations.html' %}}">Registrations</a>
                        <a class="navbar-brand" href="{{% url 'grades-menu.html' %}}">Grades</a>
                        <a class="navbar-brand" href="{{% url 'contact.html' %}}">Contact</a>
                    </nav>
                </header>
                
                <h1 class="page-describer">
                    Subject{subject_name} - Year: {subject_year}
                </h1>

                <h2 class="page-describer">
                    {subject_teacher}
                </h2>
                <!-- subjects cards being displayed in real time by a python for loop -->
                <div class="subject_shower">
                    <div class="row">

                        {{% for subject in subjects %}}
                        
                        {{% endfor %}}

                    </div>
                </div>
                    
                {{% bootstrap_javascript jquery='full' %}}

            </body>
        </html>
    </DOCTYPE3>
    """
