from pyscript import document, display

def gen(event):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    #shows the message
    result = f"""
    Student Profile
    Name   : {name}
    Age    : {age}
    School : {school}

    Summary
    {name} is currently {age} years old and studies at {school}.
    """

    #show the result
    document.getElementById("output1").innerText = result
