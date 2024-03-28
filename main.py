from kivymd.app import MDApp
from kivy.lang import Builder

screen='''
MDScreen:
             MDLabel:
                          id: Label
                          text: app.button_press
                          halign: 'center'
                          pos_hint:{'center_x':0.5,'center_y':0.6}
                          
             MDRectangleFlatButton:
                          text:'BUTTON'
                          pos_hint:{'center_x':0.5,'center_y':0.5}
                          on_release:app.button()
                          
             MDRectangleFlatButton:
                          text:'Save'
                          pos_hint:{'center_x':0.5,'center_y':0.4}
                          on_release:app.button2()
                          
             MDRectangleFlatButton:
                          text:'Show_saved_data'
                          pos_hint:{'center_x':0.5,'center_y':0.3}
                          on_release:app.button3()
'''

class DemoApp(MDApp):
             
             def build(self):
                          self.button_press='0'
                          return Builder.load_string(screen)
             def button(self):
                          a=self.button_press
                          a=int(a)
                          a=a+1
                          a=str(a)
                          self.button_press=a
                          self.root.ids['Label'].text =a
                          
             def button2(self):
                          try:
                                       f = open('thisisdata1001.txt','w+')
                                       f.write((self.root.ids['Label'].text))
                                       f.close()
                                       
                          except:
                                    self.root.ids['Label'].text='Button2_error'
             def button3(self):
                          try:
                                       f = open('thisisdata1001.txt','r')
                                       data=f.read()
                                       print(data)
                                       self.root.ids['Label'].text=data
                                       f.close()
                          except:
                                    self.root.ids['Label'].text='Button3_error'

DemoApp().run()
