import tkinter as tk 

LIGHT_GRAY="#F5F5F5"
LABEL_COLOR="#25265E"
WHITE="#FFFFFF"
OFFWHITE="#FAF8FF"
LIGHT_BLUE="#CCEDFF"
DEFAULT_FONT_STYLE=("Arial",20)
DIGIT_FONT_STYLE=("Arial",24,"bold")
SMALL_FONT_STYLE=("Arial",16)
LARGE_FONT_STYLE=("Arial",40)

class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator by Bikash Chaudhary")

        self.total_expression=""
        self.current_expression=""

        self.display_frame=self.create_display_frame()

        self.total_label,self.label=self.create_display_label()

        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),".":(4,1)
        }
        self.operations={
            "/":"\u00F7",
            "*":"\u00D7",
            "-":"-",
            "+":"+"
        }
        self.button_frame=self.create_button_frame()

        for x in range(1,5):
            self.button_frame.rowconfigure(x,weight=2)
            self.button_frame.columnconfigure(x,weight=2)
            
        self.create_digit_button()
        self.create_operator_button()
        self.create_special_button()
        self.bind_keys()
        

    
    def create_display_label(self):
        total_label=tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E,bg=LIGHT_GRAY,fg=LABEL_COLOR,padx=24,font=SMALL_FONT_STYLE)
        total_label.pack(expand=True,fill="both")

        label=tk.Label(self.display_frame,text=self.current_expression,anchor=tk.E,bg=LIGHT_GRAY,fg=LABEL_COLOR,padx=24,font=LARGE_FONT_STYLE)
        label.pack(expand=True,fill="both")

        return total_label,label

    def create_display_frame(self):
        frame=tk.Frame(self.window,height=221,bg=LIGHT_GRAY)
        frame.pack(expand=True,fill="both")
        return frame

    def create_digit_button(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.button_frame,text=str(digit),command=lambda x=digit: self.add_to_expression(x),bg=WHITE,fg=LABEL_COLOR,font=DIGIT_FONT_STYLE,borderwidth=0)
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)

    def append_operator(self,operator):
        self.current_expression+=operator
        self.total_expression+=self.current_expression
        self.current_expression=""
        self.update_total_label()
        self.update_label()

    def create_button_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame
    
    def create_operator_button(self):
        i=0
        for operator,symbol in self.operations.items():
            button=tk.Button(self.button_frame,text=symbol,bg=OFFWHITE,fg=LABEL_COLOR,command=lambda x=operator: self.append_operator(x),font=DEFAULT_FONT_STYLE,borderwidth=0)
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    def clear(self):
        self.current_expression=""
        self.total_expression=""
        self.update_label()
        self.update_total_label()


    def create_clear_button(self):
        button=tk.Button(self.button_frame,text="C",bg=OFFWHITE,command=self.clear,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0)
        button.grid(row=0,column=1,sticky=tk.NSEW)

    def square(self):
        self.current_expression=str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button=tk.Button(self.button_frame,text="x\u00b2",bg=OFFWHITE,command=self.square,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0)
        button.grid(row=0,column=2,sticky=tk.NSEW)

    def squareroot(self):
        self.current_expression=str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_squareroot_button(self):
        button=tk.Button(self.button_frame,text="x\u221a",bg=OFFWHITE,command=self.squareroot,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0)
        button.grid(row=0,column=3,sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update_total_label()

        try:
            self.current_expression=str(eval(self.total_expression))
            self.total_expression=""
        except Exception as e:
            self.current_expression="Error"
        finally:
            self.update_label()

    def create_equal_button(self):
        button=tk.Button(self.button_frame,text="=",bg=LIGHT_BLUE,command=self.evaluate,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0)
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)

    def create_special_button(self):
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_squareroot_button()

    def bind_keys(self):
        self.window.bind("<Return>",lambda event:self.evaluate())
        for key in self.digits:
            self.window.bind(str(key),lambda event,digit=key:self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key,lambda event,operator=key:self.append_operator(operator))

    def update_total_label(self):
        expression=self.total_expression
        for operator,symbol in self.operations.items():
            expression=expression.replace(operator,f"{symbol}")
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def add_to_expression(self,value):
        self.current_expression+=str(value)
        self.update_label()



    def run(self):
        self.window.mainloop()



if __name__=="__main__":
    calc=Calculator()
    calc.run()
