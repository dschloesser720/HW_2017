import requests
import re

position_1 = r"(\d) (1)"
position_2 = r"(\d) (2)"
position_3 = r"(\d) (3)"
position_4 = r"(\d) (4)"

def find_state ( current_state, file_output ):
    page = requests.get('https://github.com/dschloesser720/HW_2017/blob/master/Mono_999_R.txt')
    file_text = page.text
    matches = re.findall(current_state, file_text)
    f=open(file_output, "w")
    for i in matches:
        f.write(' '.join(map(str,i))+"\n")
    f.close()

filename_1="%s.txt" % (state_1)
find_state ( position_1, filename_1 )

filename_2="%s.txt" % (state_2)
find_state ( position_2, filename_2 )

filename_3="%s.txt" % (state_3)
find_state ( position_3, filename_3 )

filename_4="%s.txt" % (state_4)
find_state ( position_4, filename_4 )

#not entirely sure if this actually works... The "requests" module doesn't play well with IDLE apparently.
#it says "ImportError: No module named 'requests'" - doing a pip install says that I meet the requirements.
#not too sure, how to go about fixing this issue. 
