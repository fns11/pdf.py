import streamlit as st

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
 


st.header('Lets go')
          
contact_app = '''
         

<!DOCTYPE html>
<html>
<head>
    <title>Adobe Document Services PDF Embed API Sample</title>
    <meta charset="utf-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta id="viewport" name="viewport" content="width=device-width, initial-scale=1"/>
    <script type="text/javascript" src="index.js"></script>
</head>
<body style="margin: 0px">
    <div id="adobe-dc-view"></div>
    <script type="text/javascript" src="https://documentcloud.adobe.com/view-sdk/main.js"></script>
</body>
</html>


