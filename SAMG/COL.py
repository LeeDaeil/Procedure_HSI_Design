

b_w = 'QPushButton{border-top-left-radius: 10px;border-top-right-radius: 10px;border-bottom-right-radius: ' \
      '10px;border-bottom-left-radius: 10px;background-color: rgb(234, 234, 234);}' \
      'QPushButton:pressed {background-color: rgb(188, 188, 188);}' \
      'QPushButton {text-align: left;}'

b_g = 'QPushButton{border-top-left-radius: 10px;border-top-right-radius: 10px;border-bottom-right-radius: ' \
      '10px;border-bottom-left-radius: 10px;background-color: rgb(59, 190, 190);}' \
      'QPushButton:pressed {background-color: rgb(188, 188, 188);}' \
      'QPushButton {text-align: left;}'

ti_b ='border-top-left-radius: 10px; border-top-right-radius: 10px; border-bottom-right-radius: 10px;' \
      'border-bottom-left-radius: 10px; background-color: rgb(59, 190, 190); border: 1px solid black;'

guid_dis_back_color = 'background-color: rgb(59, 190, 190);'

test_col = 'background-color: rgb(59, 100, 100);'

button_False = """
                Cont_label{
                    background-color: rgb(234,234,234);  color: rgb(0,0,0);  border-radius: 10px; border: 1px solid black; font: 14pt "Arial";
                }
    
                Cont_label:hover{ 
                    background-color: rgb(150,150,150); color: rgb(0,0,0); border-radius: 10px; border: 1px solid black; font: 14pt "Arial";
                }
    
                Cont_label:pressed{
                    background-color: rgb(59,190,190); color: rgb(0,0,0); border-radius: 10px border: 1px solid black; font: 14pt "Arial";
                }"""

button_True = """
                Cont_label{
                    background-color: rgb(59,190,190);  color: rgb(0,0,0);  border-radius: 10px; border: 1px solid black; font: 14pt "Arial";
                }

                Cont_label:hover{
                    background-color: rgb(150,150,150); color: rgb(0,0,0); border-radius: 10px; border: 1px solid black; font: 14pt "Arial";
                }

                Cont_label:pressed{
                    background-color: rgb(234,234,234); color: rgb(0,0,0); border-radius: 10px border: 1px solid black; font: 14pt "Arial";
                }"""

button_switch_False = """
                Cont_open_close{
                    background-color: rgb(234,234,234);  color: rgb(0,0,0);  border-radius: 10px; border: 1px solid black; font: 14pt "Arial"; text-align: center;
                }
    
                Cont_open_close:hover{
                    background-color: rgb(150,150,150); color: rgb(0,0,0); border-radius: 10px; border: 1px solid black; font: 14pt "Arial"; text-align: center;
                }
    
                Cont_open_close:pressed{
                    background-color: rgb(59,190,190); color: rgb(0,0,0); border-radius: 10px border: 1px solid black; font: 14pt "Arial"; text-align: center;
                }"""
button_switch_True = """
                Cont_open_close{
                    background-color: rgb(59,190,190);  color: rgb(0,0,0);  border-radius: 10px; border: 1px solid black; font: 14pt "Arial"; text-align: center;
                }

                Cont_open_close:hover{
                    background-color: rgb(150,150,150); color: rgb(0,0,0); border-radius: 10px; border: 1px solid black; font: 14pt "Arial"; text-align: center;
                }

                Cont_open_close:pressed{
                    background-color: rgb(234,234,234); color: rgb(0,0,0); border-radius: 10px border: 1px solid black; font: 14pt "Arial"; text-align: center;
                }"""

button_ok_False = """
                Cont_ok{
                    background-color: rgb(234,234,234);  color: rgb(0,0,0);  border-radius: 10px; border: 1px solid black; font: 14pt "Arial";
                }

                Cont_ok:hover{ 
                    background-color: rgb(150,150,150); color: rgb(0,0,0); border-radius: 10px; border: 1px solid black; font: 14pt "Arial";
                }

                Cont_ok:pressed{
                    background-color: rgb(59,190,190); color: rgb(0,0,0); border-radius: 10px border: 1px solid black; font: 14pt "Arial";
                }"""

button_ok_True = """
                Cont_ok{
                    background-color: rgb(59,190,190);  color: rgb(0,0,0);  border-radius: 10px; border: 1px solid black; font: 14pt "Arial";
                }

                Cont_ok:hover{
                    background-color: rgb(150,150,150); color: rgb(0,0,0); border-radius: 10px; border: 1px solid black; font: 14pt "Arial";
                }

                Cont_ok:pressed{
                    background-color: rgb(234,234,234); color: rgb(0,0,0); border-radius: 10px border: 1px solid black; font: 14pt "Arial";
                }"""
