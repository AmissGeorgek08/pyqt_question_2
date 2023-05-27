from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

def app_():
    app = QApplication([])
    main_win = QWidget()
    main_win.setWindowTitle('Memory Card')
    question = QLabel("Which nationality does not exist?")
    RadioGroupBox = QGroupBox("Answer options")
    rbtn_1 = QRadioButton('Enets')
    rbtn_2 = QRadioButton('Smurfs')
    rbtn_3 = QRadioButton('Chulyms')
    rbtn_4 = QRadioButton('Aleuts')
    btn_ = QPushButton("Answer")
    RadioGroupBox2 = QGroupBox("Test result:")
    test_result = QLabel("Correct answer")
    answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    RadioGroupBox2.hide()

    def next():
        shuffle(answers)
        answers[0].setText('Smurfs')
        answers[1].setText('Enents')
        answers[2].setText('Chulyms')
        answers[3].setText('Aleuts')

    next()

    def next_question():
        question.setText("What is Brazil's national language?")
        rbtn_1.setText("Brazilian")
        rbtn_2.setText("Portuguese")
        rbtn_3.setText("Spanish")
        rbtn_4.setText("English")
        shuffle(answers)
        answers[0].setText('Portuguese')
        answers[1].setText('Brazilian')
        answers[2].setText('Spanish')
        answers[3].setText('English')
        
    def elegxos():
        if btn_.text() == 'Answer':
            if answers[0].isChecked():
                    next()
            else:
                next()
                test_result.setText("Wrong answer")
            RadioGroupBox.hide()
            RadioGroupBox2.show()
            question.setText("The most difficult question in the world!")
            btn_.setText("Next question")
        else:
            RadioGroupBox.show()
            RadioGroupBox2.hide()
            next_question()
            btn_.setText("Answer")


    vert = QHBoxLayout()
    hor = QHBoxLayout()

    vert.addWidget(question)
    hor.addWidget(btn_)

    btn_.clicked.connect(elegxos)

    main_v = QVBoxLayout()

    layout_ans1 = QHBoxLayout()
    layout_ans2 = QVBoxLayout()
    layout_ans3 = QVBoxLayout()
    layout_ans4 = QHBoxLayout()

    layout_ans2.addWidget(rbtn_1)
    layout_ans2.addWidget(rbtn_2)
    layout_ans3.addWidget(rbtn_3)
    layout_ans3.addWidget(rbtn_4)
    layout_ans4.addWidget(test_result)
    layout_ans1.addLayout(layout_ans2)
    layout_ans1.addLayout(layout_ans3)

    RadioGroupBox.setLayout(layout_ans1)
    RadioGroupBox2.setLayout(layout_ans4)
    main_v.addLayout(vert)
    main_v.addWidget(RadioGroupBox)
    main_v.addWidget(RadioGroupBox2)
    main_v.addLayout(hor)
    main_win.setLayout(main_v)

    main_win.resize(400, 250)
    main_win.show()
    app.exec_()

app_()