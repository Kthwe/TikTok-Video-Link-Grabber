import uuid
import os

base_script = '''
<FORM align="center" ACTION="http://127.0.0.1:9666/flash/add" target="_parent" METHOD="POST">
   <INPUT TYPE="hidden" NAME="dir" VALUE="special_directory_position">   
   <INPUT TYPE="hidden" NAME="package" VALUE="special_username_position">   
   <INPUT TYPE="hidden" NAME="urls" VALUE="
special_links_position
    ">
   <INPUT id="special_uuid_position" class="download_icon" TYPE="SUBMIT" NAME="submit" onclick = "change_Color('special_uuid_position')" VALUE="special_username_position">
   <label class="link_count">Total Links : special_linkcount_position</label>
</FORM>
<div class="clear">&nbsp;</div>
'''

end_script = '''
<style>
.download_icon:focus {
  background-color:cyan;
}
.download_icon {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 50px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 18px;
}
.link_count {
  border: none;
  color: blue;
  padding: 15px 40px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
</style>
<script>
function change_Color(uuid) {
var btn = document.getElementById(uuid);
btn.style.backgroundColor = '#006400';
}         
</script> 
'''


def write_html(links, username, DIR):
    if os.path.exists("C://Users//USER//Desktop//Links.html"):
        # print("Links.html already exists. Attempting to modify.")
        with open("C://Users//USER//Desktop//Links.html", 'r') as fp:
            lines = fp.readlines()
        fp.close()
        formatted_code = "".join(lines).replace(end_script, "")
        with open("C://Users//USER//Desktop//Links.html", 'w') as fp:
            fp.write(formatted_code)
        fp.close()
        # print("Success modifying Links.html.")

    special_uuid = uuid.uuid4()

    formatted_links = '\n'.join([str(link) for link in links])

    formatted_html = base_script.replace("special_username_position", username).replace("special_directory_position", DIR).replace("special_links_position", formatted_links).replace("special_linkcount_position", str(len(links))).replace("special_uuid_position", str(special_uuid))

    file = open("C://Users//USER//Desktop//Links.html".format(username), "a")

    file.write(formatted_html)

    file.close()


def write_final_script():

    file = open("C://Users//USER//Desktop//Links.html", "a")

    file.write(end_script)

    file.close()


if __name__ == '__main__':
    import codecs
    file1 = codecs.open("C://Users//USER//Desktop//Links.html", "r")
    lines = file1.readlines()
    file1.close()
    formatted_str = ''.join([str(link) for link in lines]).replace('\n', "")

    file2 = codecs.open("C://Users//USER//Desktop//Links2.html", "w")
    lines2 = file2.write(formatted_str)
    file2.close()
