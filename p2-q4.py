#محمدضا محمدی درویشانی

#بخش اول
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
t = turtle.Turtle()
t.pencolor('red')
wn.setup(width=1200 , height=800)
wn.title('turtle umz question')

def draw_letter(letter):
    if letter == 'ل':
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(100)

    elif letter == 'ا':
        t.penup()
        t.goto(-50, 0)
        t.pendown()
        t.right(180)
        t.forward(100)

    elif letter == 'ت':
        t.penup()
        t.goto(-80, -70)
        t.pendown()
        t.forward(30)
        t.right(90)
        t.forward(50)
        t.penup()
        t.goto(-95 , -40)
        t.pendown()
        t.shape('circle')
        t.stamp()
        t.penup()
        t.goto(-115 , -40)
        t.pendown()
        t.stamp()
        t.shape('triangle')

    elif letter == 'ر':
        t.penup()
        t.goto(-130 , -100)
        t.pendown()
        t.right(90)
        t.circle(50, -100)

    elif letter == 'ج':
        t.penup()
        t.goto(-250, -50)
        t.pendown()
        t.left(55)
        t.forward(50)
        t.right(90)
        t.forward(80)
        t.right(135)
        t.forward(120)
        t.penup()
        t.goto(-200, -120)
        t.shape('circle')
        t.stamp()
        t.pendown()

    elif letter == 'ی':
        t.penup()
        t.goto(-277,-71)
        t.pendown()
        t.forward(30)
        t.circle(18, 180)
        t.forward(10)
        t.left(90)
        t.circle(70 , -180)
        t.left(180)
        t.forward(20)


letters = ['ل', 'ا', 'ت', 'ر', 'ج', 'ی']
for letter in letters:
    draw_letter(letter)
wn.mainloop()